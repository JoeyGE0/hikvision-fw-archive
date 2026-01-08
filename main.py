#!/usr/bin/env python3
"""Hikvision firmware scraper - actually works with their site structure."""
import argparse
import json
import logging
import os
import re
import time
from pathlib import Path
from typing import Dict, List, Optional
from urllib.parse import urljoin

try:
    from playwright.sync_api import sync_playwright
    PLAYWRIGHT_AVAILABLE = True
except ImportError:
    PLAYWRIGHT_AVAILABLE = False

from common import (
    create_device_id,
    format_date,
    get_device_id,
    is_beta_firmware,
    load_json,
    normalize_model_name,
    parse_version,
    save_json,
)

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# For GitHub Actions, also log to stderr so it shows in workflow logs
import sys
if 'GITHUB_ACTIONS' in os.environ:
    handler = logging.StreamHandler(sys.stderr)
    handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
    logger.addHandler(handler)

BASE_URL = "https://www.hikvision.com"
FIRMWARE_URL = f"{BASE_URL}/en/support/download/firmware/"

# TEST MODE: Set to True to only scrape 1 firmware file (prevents IP banning/rate limiting)
# Maximum number of firmware files to download (0 = unlimited)
# Set this to limit downloads and avoid hitting rate limits
MAX_FIRMWARES_TO_DOWNLOAD = 5  # Change this to set your desired limit (0 = unlimited)

# Legacy TEST_MODE (deprecated - use MAX_FIRMWARES_TO_DOWNLOAD instead)
TEST_MODE = False
MAX_FIRMWARES_IN_TEST_MODE = 1


class HikvisionScraper:
    """Scraper that actually works with Hikvision's site structure."""
    
    def __init__(self):
        self.devices = load_json('devices.json')
        self.firmwares_live = load_json('firmwares_live.json')
        self.firmwares_manual = load_json('firmwares_manual.json')
        self.firmware_info = load_json('firmware_info.json')
        self.scraped_count = 0
        self.errors = []
        self.status = {
            'last_run': None,
            'status': 'unknown',
            'firmwares_found': 0,
            'new_firmwares': 0,
            'errors': [],
            'test_mode': TEST_MODE
        }
        
    def extract_model(self, text: str) -> Optional[str]:
        """Extract model from text."""
        match = re.search(r'(DS-[0-9A-Z-]+|AE-[0-9A-Z-]+|IDS-[0-9A-Z-]+)', text, re.IGNORECASE)
        return match.group(1).upper() if match else None
    
    def extract_version(self, text: str) -> Optional[str]:
        """Extract version from text."""
        match = re.search(r'[Vv]?(\d+\.\d+\.\d+(?:\.\d+)?)', text)
        return match.group(1) if match else None
    
    def extract_hardware_version(self, text: str, model: str) -> str:
        """Extract hardware version."""
        # Look for IPC_, NVR_, etc.
        hw_match = re.search(r'(IPC_[A-Z0-9]+|NVR_[A-Z0-9]+|DVR_[A-Z0-9]+)', text, re.IGNORECASE)
        if hw_match:
            return hw_match.group(1).upper()
        
        # Default based on model
        if 'DS-2CD' in model or 'DS-2DE' in model:
            return 'IPC_G0'
        elif 'DS-76' in model or 'DS-77' in model:
            return 'NVR_G0'
        return 'UNKNOWN'
    
    def scrape_with_playwright(self) -> List[Dict]:
        """Actually scrape Hikvision's site using the real structure."""
        if not PLAYWRIGHT_AVAILABLE:
            logger.error("Playwright required")
            return []
        
        firmwares = []
        new_downloads_count = 0  # Track how many NEW firmwares we've downloaded
        skipped_existing_count = 0  # Track how many existing firmwares we skipped
        total_found_count = 0  # Track total firmwares found on website
        browser = None
        
        try:
            with sync_playwright() as p:
                logger.info("  → Launching browser...")
                browser = p.chromium.launch(headless=True)
                page = browser.new_page()
                
                logger.info("Loading firmware page...")
                page.goto(FIRMWARE_URL, wait_until='networkidle', timeout=60000)
                time.sleep(5)
                
                # Find the search box with class "firmware-search"
                search_input = page.query_selector('input.firmware-search')
                if not search_input:
                    logger.warning("Could not find firmware search input")
                    browser.close()
                    return []
                
                # Search for common model prefixes
                search_terms = [
                    'DS-2CD',  # IP Cameras
                    'DS-2DE',  # PTZ Cameras
                    'DS-76',   # NVRs
                    'DS-77',   # NVRs
                    'DS-2TD',  # Thermal cameras
                    'AE-',     # Access control
                ]
                
                total_search_terms = len(search_terms)
                for search_idx, search_term in enumerate(search_terms, 1):
                    try:
                        logger.info(f"[{search_idx}/{total_search_terms}] Searching for: {search_term}")
                    
                        # Clear and fill search
                        logger.info(f"  → Entering search term...")
                        search_input.fill('')
                        search_input.fill(search_term)
                        search_input.press('Enter')
                        logger.info(f"  → Waiting for results to load...")
                        time.sleep(5)  # Wait for results
                        
                        # Click "View more" button multiple times to load all results
                        logger.info(f"  → Loading all results (clicking 'View more' buttons)...")
                        view_more_clicked = 0
                        while view_more_clicked < 10:  # Limit to prevent infinite loop
                            view_more_btn = page.query_selector('div.action-btn:has-text("View more")')
                            if view_more_btn and view_more_btn.is_visible():
                                view_more_btn.click()
                                time.sleep(2)
                                view_more_clicked += 1
                                if view_more_clicked % 3 == 0:
                                    logger.info(f"    Clicked 'View more' {view_more_clicked} times...")
                            else:
                                break
                        
                        if view_more_clicked > 0:
                            logger.info(f"  → Finished loading ({view_more_clicked} clicks)")
                        
                        # Find all firmware model titles
                        firmware_titles = page.query_selector_all('div.main-title')
                        logger.info(f"  → Found {len(firmware_titles)} firmware models for {search_term}")
                        
                        if len(firmware_titles) == 0:
                            logger.warning(f"  ⚠ No models found for {search_term}, skipping...")
                            continue
                        
                        # Process all models (download limit will stop when reached)
                            # Limit processing to prevent crashes on huge batches
                            MAX_MODELS_PER_SEARCH = 500
                            if len(firmware_titles) > MAX_MODELS_PER_SEARCH:
                                logger.warning(f"  ⚠ Found {len(firmware_titles)} models, limiting to first {MAX_MODELS_PER_SEARCH} to prevent crashes")
                                firmware_titles = firmware_titles[:MAX_MODELS_PER_SEARCH]
                        
                        # Process all firmware items
                        fw_count_before = len(firmwares)
                        # Process in smaller batches to avoid crashes
                        batch_size = 100
                        total_batches = (len(firmware_titles) + batch_size - 1) // batch_size
                        
                        # Flag to break out of nested loops in test mode
                        test_mode_limit_reached = False
                        
                        for batch_num in range(total_batches):
                            if test_mode_limit_reached:
                                break
                            start_idx = batch_num * batch_size
                            end_idx = min(start_idx + batch_size, len(firmware_titles))
                            batch = firmware_titles[start_idx:end_idx]
                            
                            logger.info(f"  → Processing batch {batch_num + 1}/{total_batches} (items {start_idx + 1}-{end_idx})...")
                            
                            for i, title_element in enumerate(batch, start_idx + 1):
                                if test_mode_limit_reached:
                                    break
                                try:
                                    logger.info(f"    Processing item {i}...")
                                    model_text = title_element.inner_text().strip()
                                    logger.info(f"    Model text extracted: {model_text[:50]}...")
                                    model = self.extract_model(model_text)
                                    logger.info(f"    Extracted model: {model}")
                                    
                                    if not model:
                                        logger.warning(f"    Could not extract model from: {model_text}")
                                        continue
                                    
                                    # Get target_id before clicking
                                    target_id = title_element.get_attribute('data-target') or ''
                                    logger.info(f"    Processing model {i}: {model} (data-target: {target_id})")
                                    
                                    # Click to expand - scroll into view first, then click
                                    logger.info(f"    Attempting to click title element for {model}...")
                                    try:
                                        # Scroll element into view using JavaScript
                                        page.evaluate('(element) => element.scrollIntoView({ behavior: "smooth", block: "center" })', title_element)
                                        time.sleep(0.3)  # Brief wait after scrolling
                                        
                                        # Try clicking - Playwright handles visibility automatically, but use JS click as fallback
                                        try:
                                            # First try normal click with shorter timeout
                                            title_element.click(timeout=10000)
                                            logger.info(f"    Normal click successful")
                                        except Exception as normal_click_err:
                                            # Fallback: use JavaScript click
                                            logger.info(f"    Normal click failed ({normal_click_err}), trying JavaScript click...")
                                            page.evaluate('(element) => { element.click(); }', title_element)
                                            logger.info(f"    JavaScript click executed")
                                        
                                        logger.info(f"    Click successful, waiting for content to expand...")
                                        # Wait for collapse content to become visible
                                        if target_id:
                                            target_id_clean = target_id.replace('#', '')
                                            # Wait for the collapse element to appear and become visible
                                            try:
                                                # Try waiting for common Bootstrap collapse classes or visible state
                                                page.wait_for_selector(f'#{target_id_clean}.show, #{target_id_clean}.in, #{target_id_clean}.collapse.show', timeout=5000)
                                                logger.info(f"    Collapse content became visible (found .show class)")
                                            except:
                                                # If selector wait fails, wait a bit and check visibility manually
                                                logger.info(f"    Waiting for collapse animation...")
                                                time.sleep(2.5)
                                        else:
                                            time.sleep(1.5)
                                    except Exception as click_err:
                                        logger.warning(f"    Click failed for item {i}: {click_err}")
                                        import traceback
                                        logger.debug(f"    Traceback: {traceback.format_exc()}")
                                        continue
                                    
                                    # Find the collapse content
                                    if target_id:
                                        target_id = target_id.replace('#', '')
                                        collapse_content = page.query_selector(f'#{target_id}')
                                        
                                        if collapse_content:
                                            # Check visibility multiple ways - Bootstrap uses .show class
                                            has_show_class = page.evaluate('(element) => element.classList.contains("show")', collapse_content)
                                            offset_height = page.evaluate('(element) => element.offsetHeight', collapse_content)
                                            is_visible_playwright = collapse_content.is_visible()
                                            
                                            # Consider visible if it has .show class OR has height OR Playwright says it's visible
                                            is_visible = has_show_class or offset_height > 0 or is_visible_playwright
                                            
                                            logger.info(f"    Collapse content found for {model}, .show class: {has_show_class}, height: {offset_height}, Playwright visible: {is_visible_playwright}, final visible: {is_visible}")
                                            if is_visible:
                                                # Get all links in expanded content
                                                links = collapse_content.query_selector_all('a[href]')
                                                logger.info(f"    Found {len(links)} links in expanded content for {model}")
                                                
                                                firmware_links_found = 0
                                                for link_idx, link in enumerate(links, 1):
                                                    if test_mode_limit_reached:
                                                        break
                                                    try:
                                                        href = link.get_attribute('href') or ''
                                                        link_text = link.inner_text().strip()
                                                        
                                                        # Log all links for debugging (limit to first few)
                                                        if link_idx <= 5:
                                                            logger.debug(f"      Link {link_idx}: {link_text[:40]}... | href={href[:60]}...")
                                                        
                                                        # Check if this is a firmware link (either direct file link or license agreement link)
                                                        is_firmware_link = False
                                                        actual_download_url = href
                                                        local_file_path = ''  # Will be set if download succeeds
                                                        
                                                        # Extract version and model (we'll check existence AFTER getting real URL)
                                                        version = self.extract_version(link_text + ' ' + href)
                                                        context_text = collapse_content.inner_text()
                                                        hw_version = self.extract_hardware_version(context_text, model)
                                                        normalized_model = normalize_model_name(model)
                                                        
                                                        # Increment total found counter (count all firmwares we find)
                                                        total_found_count += 1
                                                        
                                                        # Direct firmware file link
                                                        if any(ext in href.lower() for ext in ['.dav', '.zip', '.pak', '.bin']):
                                                            is_firmware_link = True
                                                            # For direct links, check existence now
                                                            if version:
                                                                firmware_key = f"{normalized_model}_{hw_version}_{version}"
                                                                firmware_exists = firmware_key in self.firmwares_live
                                                                
                                                                if firmware_exists:
                                                                    skipped_existing_count += 1
                                                                    logger.info(f"    ⊘ Skipping existing firmware: {normalized_model} {hw_version} v{version} ({skipped_existing_count} skipped)")
                                                                    firmwares.append({
                                                                        'model': normalized_model,
                                                                        'hardware_version': hw_version,
                                                                        'version': version,
                                                                        'download_url': href,
                                                                        'local_file_path': '',
                                                                        'date': '',
                                                                        'changes': '',
                                                                        'notes': '',
                                                                        'source': 'live',
                                                                        'already_exists': True
                                                                    })
                                                                    continue
                                                        # License agreement link (needs to be clicked to get actual URL)
                                                        elif href == '#download-agreement' or 'download-agreement' in href.lower():
                                                            is_firmware_link = True
                                                            logger.info(f"    Found license agreement link: {link_text[:50]}...")
                                                            
                                                            # Click to open modal
                                                            try:
                                                                # Use JavaScript click to avoid timeout issues
                                                                logger.info(f"    Clicking license agreement link...")
                                                                page.evaluate('(element) => { element.click(); }', link)
                                                                time.sleep(3)  # Wait for modal to appear and load
                                                                
                                                                # Find modal - simplified approach that works
                                                                modal = page.query_selector('[role="dialog"]')
                                                                if not modal:
                                                                    # Try alternative selector
                                                                    modal = page.query_selector('dialog')
                                                                
                                                                if not modal:
                                                                    logger.warning(f"    ⚠ Could not find modal after clicking agreement link")
                                                                    continue
                                                                
                                                                logger.info(f"    ✓ Modal found")
                                                                
                                                                # Find the download link - SIMPLIFIED: just check all links in modal
                                                                agree_link = None
                                                                all_modal_links = modal.query_selector_all('a[href]')
                                                                logger.info(f"    Checking {len(all_modal_links)} links in modal...")
                                                                
                                                                for modal_link in all_modal_links:
                                                                    modal_href = modal_link.get_attribute('href') or ''
                                                                    modal_text = modal_link.inner_text().strip()
                                                                    
                                                                    # Check if it's a firmware file URL (most reliable)
                                                                    if any(ext in modal_href.lower() for ext in ['.dav', '.zip', '.pak', '.bin']):
                                                                        agree_link = modal_link
                                                                        logger.info(f"    ✓ Found download link: {modal_text[:50]}...")
                                                                        logger.info(f"      URL: {modal_href[:100]}...")
                                                                        break
                                                                
                                                                if agree_link:
                                                                    actual_download_url = agree_link.get_attribute('href') or ''
                                                                    logger.info(f"    ✓ Found download URL: {actual_download_url[:100]}...")
                                                                    
                                                                    # NOW check if firmware already exists (we have the real URL now)
                                                                    if version:
                                                                        firmware_key = f"{normalized_model}_{hw_version}_{version}"
                                                                        firmware_exists = firmware_key in self.firmwares_live
                                                                        
                                                                        if firmware_exists:
                                                                            skipped_existing_count += 1
                                                                            logger.info(f"    ⊘ Skipping existing firmware: {normalized_model} {hw_version} v{version} ({skipped_existing_count} skipped)")
                                                                            # Close modal
                                                                            close_btn = page.query_selector('dialog button, [role="dialog"] button, dialog [aria-label*="close" i], [role="dialog"] [aria-label*="close" i]')
                                                                            if close_btn:
                                                                                close_btn.click()
                                                                                time.sleep(0.5)
                                                                            firmwares.append({
                                                                                'model': normalized_model,
                                                                                'hardware_version': hw_version,
                                                                                'version': version,
                                                                                'download_url': actual_download_url,
                                                                                'local_file_path': '',
                                                                                'date': '',
                                                                                'changes': '',
                                                                                'notes': '',
                                                                                'source': 'live',
                                                                                'already_exists': True
                                                                            })
                                                                            continue
                                                                    
                                                                    # Check download limit for NEW firmwares
                                                                    if MAX_FIRMWARES_TO_DOWNLOAD > 0 and new_downloads_count >= MAX_FIRMWARES_TO_DOWNLOAD:
                                                                        logger.info(f"  ⏹️  Download limit reached: Downloaded {new_downloads_count} NEW firmware(s) (limit: {MAX_FIRMWARES_TO_DOWNLOAD}), stopping...")
                                                                        # Close modal
                                                                        close_btn = page.query_selector('dialog button, [role="dialog"] button')
                                                                        if close_btn:
                                                                            close_btn.click()
                                                                        test_mode_limit_reached = True
                                                                        break
                                                                    
                                                                    logger.info(f"    Starting download...")
                                                                    
                                                                    # Click the link to trigger download (with browser context)
                                                                    try:
                                                                        # Wait for download and click simultaneously - this maintains browser session
                                                                        with page.expect_download(timeout=120000) as download_info:  # 2 min timeout for large files
                                                                            # Scroll into view and click - ensures it's visible
                                                                            page.evaluate('(el) => { el.scrollIntoView({block: "center"}); el.click(); }', agree_link)
                                                                        
                                                                        download = download_info.value
                                                                        
                                                                        # Generate filename
                                                                        suggested_filename = download.suggested_filename
                                                                        if suggested_filename:
                                                                            filename = suggested_filename
                                                                        else:
                                                                            # Try to get filename from URL
                                                                            filename = actual_download_url.split('/')[-1].split('?')[0]
                                                                            if not filename or '.' not in filename:
                                                                                # Fallback: use model and extract version from link text
                                                                                version_match = re.search(r'[Vv]?(\d+\.\d+\.\d+(?:\.\d+)?)', link_text)
                                                                                version_str = version_match.group(1) if version_match else 'unknown'
                                                                                ext = '.zip' if '.zip' in actual_download_url.lower() else '.dav' if '.dav' in actual_download_url.lower() else '.bin'
                                                                                filename = f"{model}_v{version_str}{ext}"
                                                                        
                                                                        # Save to firmwares directory
                                                                        firmware_dir = Path('firmwares')
                                                                        firmware_dir.mkdir(exist_ok=True)
                                                                        filepath = firmware_dir / filename
                                                                        
                                                                        download.save_as(filepath)
                                                                        local_file_path = str(filepath)  # Store for firmware dict
                                                                        new_downloads_count += 1  # Increment counter for new download
                                                                        
                                                                        # Verify file was actually saved
                                                                        if filepath.exists():
                                                                            file_size = filepath.stat().st_size
                                                                            logger.info(f"    ✓ File downloaded to: {filepath} ({file_size:,} bytes) (NEW firmware #{new_downloads_count})")
                                                                        else:
                                                                            logger.error(f"    ✗ File download failed: {filepath} does not exist!")
                                                                            local_file_path = ''  # Clear path if file doesn't exist
                                                                    except Exception as download_err:
                                                                        logger.warning(f"    ⚠ Download failed: {download_err}")
                                                                        import traceback
                                                                        logger.debug(f"    Traceback: {traceback.format_exc()}")
                                                                    
                                                                    logger.info(f"    ✓ Download URL: {actual_download_url[:80]}...")
                                                                else:
                                                                    logger.warning(f"    ⚠ Could not find download URL in modal after all strategies")
                                                                    # Close modal and continue
                                                                    close_btn = page.query_selector('dialog button, [role="dialog"] button, dialog [aria-label*="close" i], [role="dialog"] [aria-label*="close" i]')
                                                                    if close_btn:
                                                                        close_btn.click()
                                                                        time.sleep(0.5)
                                                                    continue
                                                            except Exception as modal_err:
                                                                logger.warning(f"    ⚠ Error handling modal: {modal_err}")
                                                                import traceback
                                                                logger.debug(f"    Traceback: {traceback.format_exc()}")
                                                                # Try to close modal if open
                                                                try:
                                                                    close_btn = page.query_selector('dialog button, [role="dialog"] button, dialog [aria-label*="close" i], [role="dialog"] [aria-label*="close" i]')
                                                                    if close_btn:
                                                                        close_btn.click()
                                                                        time.sleep(0.5)
                                                                except:
                                                                    pass
                                                                continue
                                                        
                                                        if not is_firmware_link:
                                                            continue
                                                        
                                                        firmware_links_found += 1
                                                        logger.info(f"    Found firmware link #{firmware_links_found}: {link_text[:50]}... | {actual_download_url[:80]}...")
                                                        
                                                        # Normalize URL
                                                        if actual_download_url.startswith('/'):
                                                            actual_download_url = urljoin(BASE_URL, actual_download_url)
                                                        elif not actual_download_url.startswith('http'):
                                                            actual_download_url = urljoin(FIRMWARE_URL, actual_download_url)
                                                        
                                                        # Version/model already extracted earlier, reuse them
                                                        if not version:
                                                            logger.warning(f"    ⚠ Could not extract version from: {link_text[:50]}... | {actual_download_url[:80]}...")
                                                            continue
                                                        
                                                        # Extract date
                                                        date_match = re.search(r'(\d{6}|\d{8})', actual_download_url + link_text)
                                                        date_str = ''
                                                        if date_match:
                                                            date_code = date_match.group(1)
                                                            if len(date_code) == 6:
                                                                date_str = f"20{date_code[:2]}-{date_code[2:4]}-{date_code[4:6]}"
                                                        
                                                        # Add firmware to list (download happened in modal handling above)
                                                        firmwares.append({
                                                            'model': normalized_model,
                                                            'hardware_version': hw_version,
                                                            'version': version,
                                                            'download_url': actual_download_url,
                                                            'local_file_path': local_file_path,  # Path to downloaded file (if download succeeded)
                                                            'date': date_str,
                                                            'changes': '',
                                                            'notes': '',
                                                            'source': 'live'
                                                        })
                                                    except Exception as link_err:
                                                        logger.debug(f"    Link processing error: {link_err}")
                                                        continue
                                            else:
                                                logger.warning(f"    Collapse content exists but not visible for {model}")
                                                continue
                                        else:
                                            logger.warning(f"    Could not find collapse content with ID: {target_id}")
                                            continue
                                    else:
                                        logger.warning(f"    No data-target attribute found for {model}")
                                        continue
                                
                                except Exception as e:
                                    logger.debug(f"  Error on item {i}: {e}")
                                    continue
                            
                            # Small delay between batches
                            if batch_num < total_batches - 1 and not test_mode_limit_reached:
                                time.sleep(1)
                        
                        if test_mode_limit_reached:
                            logger.info(f"  ⏹️  Stopped early after reaching download limit of {MAX_FIRMWARES_TO_DOWNLOAD} firmware(s)")
                            break
                            
                            # Small delay between batches
                            if batch_num < total_batches - 1:
                                time.sleep(1)
                        
                        fw_count_after = len(firmwares)
                        fw_found_this_search = fw_count_after - fw_count_before
                        logger.info(f"  ✓ Found {fw_found_this_search} firmwares from {search_term} (total so far: {fw_count_after})")
                        
                        time.sleep(2)  # Be respectful
                    
                    except Exception as e:
                        error_msg = f"Search failed for {search_term}: {str(e)}"
                        logger.warning(error_msg)
                        self.errors.append(error_msg)
                        continue
                
                browser.close()
        except KeyboardInterrupt:
            logger.warning("Scraping interrupted by user")
            if browser:
                browser.close()
        except Exception as e:
            error_msg = f"Playwright error: {str(e)}"
            logger.error(error_msg)
            self.errors.append(error_msg)
            logger.info(f"Collected {len(firmwares)} firmwares before error")
            if browser:
                try:
                    browser.close()
                except:
                    pass
        
        # Deduplicate
        logger.info(f"→ Deduplicating {len(firmwares)} firmwares...")
        seen = set()
        unique_firmwares = []
        duplicates = 0
        for fw in firmwares:
            key = (fw['model'], fw['hardware_version'], fw['version'])
            if key not in seen:
                seen.add(key)
                unique_firmwares.append(fw)
            else:
                duplicates += 1
        
        logger.info(f"✓ Deduplication complete: {len(unique_firmwares)} unique firmwares ({duplicates} duplicates removed)")
        
        # Calculate summary statistics
        skipped = sum(1 for fw in unique_firmwares if fw.get('already_exists'))
        
        logger.info("=" * 60)
        logger.info("📊 Download Summary:")
        logger.info(f"  • Total firmwares found this run: {total_found_count}")
        logger.info(f"  • Already existing (skipped): {skipped}")
        logger.info(f"  • New downloads this run: {new_downloads_count}")
        if MAX_FIRMWARES_TO_DOWNLOAD > 0 and new_downloads_count >= MAX_FIRMWARES_TO_DOWNLOAD:
            logger.info(f"  ⏹️  Download limit reached ({MAX_FIRMWARES_TO_DOWNLOAD}) - more firmwares may be available on next run")
        elif skipped > 0 and new_downloads_count == 0:
            logger.info(f"  ✓ All found firmwares already exist - you're caught up!")
        logger.info("=" * 60)
        
        return unique_firmwares
    
    def process_firmware(self, fw_data: Dict):
        """Process and save firmware."""
        model = fw_data.get('model', '')
        hw_version = fw_data.get('hardware_version', '')
        version = fw_data.get('version', '')
        
        if not all([model, version]):
            return
        
        # Get/create device ID
        device_id = get_device_id(self.devices, model, hw_version)
        if device_id is None:
            device_id = create_device_id(self.devices, model, hw_version)
            logger.debug(f"Created device: {model} {hw_version} -> ID {device_id}")
        
        # Create key
        key = f"{model}_{hw_version}_{version}"
        
        if key not in self.firmwares_live:
            self.firmwares_live[key] = {
                'device_id': device_id,
                'model': model,
                'hardware_version': hw_version,
                'version': version,
                'date': format_date(fw_data.get('date', '')),
                'download_url': fw_data.get('download_url', ''),
                'changes': fw_data.get('changes', ''),
                'notes': fw_data.get('notes', ''),
                'is_beta': is_beta_firmware(version, fw_data.get('notes', '')),
                'source': fw_data.get('source', 'live')
            }
            self.scraped_count += 1
            logger.info(f"  ✓ Added NEW firmware: {model} {hw_version} v{version}")
            if self.scraped_count % 50 == 0:
                logger.info(f"  Added {self.scraped_count} new firmwares so far...")
        else:
            logger.debug(f"  ⊘ Skipped existing firmware: {model} {hw_version} v{version}")
    
    def save(self):
        """Save all data."""
        save_json('devices.json', self.devices)
        save_json('firmwares_live.json', self.firmwares_live)
        logger.info("Data saved")
    
    def save_status(self):
        """Save status and errors to status.json."""
        from datetime import datetime
        self.status['last_run'] = datetime.now().isoformat()
        self.status['firmwares_found'] = len(self.firmwares_live)
        self.status['new_firmwares'] = self.scraped_count
        self.status['errors'] = self.errors[-10:]  # Keep last 10 errors
        if self.errors:
            self.status['status'] = 'error'
        elif self.scraped_count > 0:
            self.status['status'] = 'success'
        else:
            self.status['status'] = 'no_new_firmwares'
        save_json('status.json', self.status)
    
    def scrape(self):
        """Main scrape method."""
        logger.info("=" * 60)
        if TEST_MODE:
            logger.info("🧪 TEST MODE ENABLED")
        if MAX_FIRMWARES_TO_DOWNLOAD > 0:
            logger.info(f"📥 Download limit: {MAX_FIRMWARES_TO_DOWNLOAD} firmware file(s)")
        else:
            logger.info("📥 Download limit: Unlimited")
        logger.info("Starting Hikvision firmware scrape...")
        logger.info("=" * 60)
        
        start_time = time.time()
        
        try:
            firmwares = self.scrape_with_playwright()
            
            logger.info(f"→ Processing {len(firmwares)} firmwares into database...")
            processed = 0
            for idx, fw in enumerate(firmwares, 1):
                if idx % 100 == 0 or idx == len(firmwares):
                    logger.info(f"  Processing firmware {idx}/{len(firmwares)}...")
                logger.debug(f"  Processing firmware: {fw.get('model', 'NO MODEL')} v{fw.get('version', 'NO VERSION')}")
                try:
                    self.process_firmware(fw)
                    processed += 1
                    # Periodic save every 50 firmwares to avoid losing progress on crash
                    if processed % 50 == 0:
                        logger.debug(f"  Periodic save: {processed} firmwares processed so far...")
                        self.save()
                except Exception as process_err:
                    logger.warning(f"  ⚠ Failed to process firmware {idx}: {process_err}")
                    self.errors.append(f"Failed to process firmware {idx}: {str(process_err)}")
                    continue  # Continue with next firmware
            
            logger.info(f"→ Saving data to JSON files...")
            self.save()
            
            elapsed = time.time() - start_time
            logger.info("=" * 60)
            logger.info(f"✓ Scraping complete!")
            logger.info(f"  • Total firmwares found: {len(firmwares)}")
            logger.info(f"  • New firmwares added: {self.scraped_count}")
            logger.info(f"  • Time taken: {elapsed:.1f} seconds")
            logger.info("=" * 60)
        except Exception as e:
            error_msg = f"Scraping failed: {str(e)}"
            logger.error(error_msg)
            self.errors.append(error_msg)
            # Save any successfully processed firmwares before exiting
            if self.scraped_count > 0:
                logger.info(f"→ Saving {self.scraped_count} successfully processed firmwares before exit...")
                try:
                    self.save()
                except Exception as save_err:
                    logger.error(f"Failed to save data: {save_err}")
        finally:
            # Always save status, even on error
            self.save_status()


def main():
    parser = argparse.ArgumentParser(description='Hikvision firmware scraper')
    parser.add_argument('command', choices=['scrape', 'add'], help='Command to run')
    parser.add_argument('url', nargs='?', help='Firmware URL (for add command)')
    parser.add_argument('--model', help='Device model')
    parser.add_argument('--hw-version', dest='hw_version', help='Hardware version')
    parser.add_argument('--version', help='Firmware version')
    parser.add_argument('--date', help='Release date')
    parser.add_argument('--changes', help='Changelog')
    parser.add_argument('--notes', help='Additional notes')
    parser.add_argument('-g', '--github', action='store_true', help='GitHub Actions mode (outputs JSON)')
    
    args = parser.parse_args()
    
    scraper = HikvisionScraper()
    
    if args.command == 'scrape':
        scraper.scrape()
        
        # Generate README after scraping
        from release import main as release_main
        release_main()
        
        # GitHub Actions mode: output JSON with new firmwares count
        if args.github:
            import json
            print(json.dumps(scraper.scraped_count))
    elif args.command == 'add':
        if not args.url:
            logger.error("URL required for add command")
            return
        
        fw_data = {
            'model': args.model or '',
            'hardware_version': args.hw_version or 'UNKNOWN',
            'version': args.version or '',
            'download_url': args.url,
            'date': args.date or '',
            'changes': args.changes or '',
            'notes': args.notes or '',
            'source': 'manual'
        }
        scraper.process_firmware(fw_data)
        scraper.save()


if __name__ == '__main__':
    main()
