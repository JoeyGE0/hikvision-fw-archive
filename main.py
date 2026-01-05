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
TEST_MODE = True
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
                # TEST MODE: Only search first term to limit requests
                search_terms = [
                    'DS-2CD',  # IP Cameras
                    # 'DS-2DE',  # PTZ Cameras - COMMENTED OUT FOR TEST MODE
                    # 'DS-76',   # NVRs - COMMENTED OUT FOR TEST MODE
                    # 'DS-77',   # NVRs - COMMENTED OUT FOR TEST MODE
                    # 'DS-2TD',  # Thermal cameras - COMMENTED OUT FOR TEST MODE
                    # 'AE-',     # Access control - COMMENTED OUT FOR TEST MODE
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
                        
                        # TEST MODE: Limit to just 1 model to scrape only 1 firmware file
                        if TEST_MODE:
                            logger.info(f"  🧪 TEST MODE: Limiting to 1 model only")
                            firmware_titles = firmware_titles[:1]
                        else:
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
                                    model_text = title_element.inner_text().strip()
                                    model = self.extract_model(model_text)
                                    
                                    if not model:
                                        logger.debug(f"    Could not extract model from: {model_text}")
                                        continue
                                    
                                    # Click to expand
                                    try:
                                        title_element.click()
                                        time.sleep(0.3)  # Shorter wait
                                    except Exception as click_err:
                                        logger.debug(f"    Click failed for item {i}: {click_err}")
                                        continue
                                    
                                    # Find the collapse content
                                    target_id = title_element.get_attribute('data-target') or ''
                                    if target_id:
                                        target_id = target_id.replace('#', '')
                                        collapse_content = page.query_selector(f'#{target_id}')
                                        
                                        if collapse_content and collapse_content.is_visible():
                                            # Get all links in expanded content
                                            links = collapse_content.query_selector_all('a[href]')
                                            logger.info(f"    Found {len(links)} links in expanded content for {model}")
                                            
                                            firmware_links_found = 0
                                            for link in links:
                                                if test_mode_limit_reached:
                                                    break
                                                try:
                                                    href = link.get_attribute('href') or ''
                                                    link_text = link.inner_text().strip()
                                                    
                                                    # Check if this is a firmware link (either direct file link or license agreement link)
                                                    is_firmware_link = False
                                                    actual_download_url = href
                                                    
                                                    # Direct firmware file link
                                                    if any(ext in href.lower() for ext in ['.dav', '.zip', '.pak', '.bin']):
                                                        is_firmware_link = True
                                                    # License agreement link (needs to be clicked to get actual URL)
                                                    elif href == '#download-agreement' or 'download-agreement' in href.lower():
                                                        is_firmware_link = True
                                                        logger.info(f"    Found license agreement link: {link_text[:50]}...")
                                                        
                                                        # Click to open modal
                                                        try:
                                                            link.click()
                                                            time.sleep(1)  # Wait for modal to appear
                                                            
                                                            # Find the "Agree" link in the modal
                                                            agree_link = page.query_selector('dialog a[href*=".zip"], dialog a[href*=".dav"], dialog a[href*=".pak"], dialog a[href*=".bin"]')
                                                            if not agree_link:
                                                                # Try finding by text content
                                                                all_modal_links = page.query_selector_all('dialog a[href]')
                                                                for modal_link in all_modal_links:
                                                                    modal_href = modal_link.get_attribute('href') or ''
                                                                    modal_text = modal_link.inner_text().strip().lower()
                                                                    if (any(ext in modal_href.lower() for ext in ['.dav', '.zip', '.pak', '.bin']) or
                                                                        'agree' in modal_text):
                                                                        agree_link = modal_link
                                                                        break
                                                            
                                                            if agree_link:
                                                                actual_download_url = agree_link.get_attribute('href') or ''
                                                                logger.info(f"    ✓ Found actual download URL in modal: {actual_download_url[:80]}...")
                                                            else:
                                                                logger.warning(f"    ⚠ Could not find download URL in modal")
                                                                # Close modal and continue
                                                                close_btn = page.query_selector('dialog button, dialog [aria-label*="close" i]')
                                                                if close_btn:
                                                                    close_btn.click()
                                                                    time.sleep(0.5)
                                                                continue
                                                        except Exception as modal_err:
                                                            logger.warning(f"    ⚠ Error handling modal: {modal_err}")
                                                            # Try to close modal if open
                                                            try:
                                                                close_btn = page.query_selector('dialog button, dialog [aria-label*="close" i]')
                                                                if close_btn:
                                                                    close_btn.click()
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
                                                    
                                                    version = self.extract_version(link_text + ' ' + actual_download_url)
                                                    if not version:
                                                        logger.warning(f"    ⚠ Could not extract version from: {link_text[:50]}... | {actual_download_url[:80]}...")
                                                        continue
                                                    logger.info(f"    ✓ Extracted version: {version}")
                                                    
                                                    context_text = collapse_content.inner_text()
                                                    hw_version = self.extract_hardware_version(context_text, model)
                                                    
                                                    # Extract date
                                                    date_match = re.search(r'(\d{6}|\d{8})', actual_download_url + link_text)
                                                    date_str = ''
                                                    if date_match:
                                                        date_code = date_match.group(1)
                                                        if len(date_code) == 6:
                                                            date_str = f"20{date_code[:2]}-{date_code[2:4]}-{date_code[4:6]}"
                                                    
                                                    firmwares.append({
                                                        'model': normalize_model_name(model),
                                                        'hardware_version': hw_version,
                                                        'version': version,
                                                        'download_url': actual_download_url,
                                                        'date': date_str,
                                                        'changes': '',
                                                        'notes': '',
                                                        'source': 'live'
                                                    })
                                                    
                                                    # TEST MODE: Stop after finding 1 firmware file
                                                    if TEST_MODE and len(firmwares) >= MAX_FIRMWARES_IN_TEST_MODE:
                                                        logger.info(f"  🧪 TEST MODE: Found {len(firmwares)} firmware(s), stopping...")
                                                        test_mode_limit_reached = True
                                                        break
                                                except Exception as link_err:
                                                    logger.debug(f"    Link processing error: {link_err}")
                                                    continue
                                
                                except Exception as e:
                                    logger.debug(f"  Error on item {i}: {e}")
                                    continue
                            
                            # Small delay between batches
                            if batch_num < total_batches - 1 and not test_mode_limit_reached:
                                time.sleep(1)
                        
                        if test_mode_limit_reached:
                            logger.info(f"  🧪 TEST MODE: Stopped early after finding {MAX_FIRMWARES_IN_TEST_MODE} firmware(s)")
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
            logger.info("🧪 TEST MODE ENABLED - Only scraping 1 firmware file")
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
                self.process_firmware(fw)
                processed += 1
            
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
        finally:
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
