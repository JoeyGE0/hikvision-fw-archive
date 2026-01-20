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

try:
    import requests
    REQUESTS_AVAILABLE = True
except ImportError:
    REQUESTS_AVAILABLE = False

from common import (
    create_device_id,
    extract_applied_to,
    extract_models,
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

# GitHub repo info for releases sync
GITHUB_REPO = "JoeyGE0/hikvision-fw-archive"
GITHUB_API_BASE = "https://api.github.com/repos"

# TEST MODE: Set to True to only scrape 1 firmware file (prevents IP banning/rate limiting)
# Maximum number of firmware files to download (0 = unlimited)
# Set this to limit downloads and avoid hitting rate limits
MAX_FIRMWARES_TO_DOWNLOAD = 10  # Downloads 10 new firmwares per run (20 per day)

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
        downloaded_in_this_run = set()  # Track firmware keys downloaded in this run to prevent duplicates
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
                                                
                                                # Sort links by date (newest first) to prioritize recent releases
                                                def extract_link_date(link_element):
                                                    """Extract date from link for sorting."""
                                                    try:
                                                        href = link_element.get_attribute('href') or ''
                                                        link_text = link_element.inner_text().strip()
                                                        
                                                        # Try to find date in link_text (filename) - more accurate
                                                        date_match = re.search(r'(\d{6}|\d{8})', link_text)
                                                        if date_match:
                                                            date_code = date_match.group(1)
                                                            if len(date_code) == 6:
                                                                return f"20{date_code[:2]}-{date_code[2:4]}-{date_code[4:6]}"
                                                            elif len(date_code) == 8:
                                                                return f"{date_code[:4]}-{date_code[4:6]}-{date_code[6:8]}"
                                                        
                                                        # If no date in filename, try URL
                                                        date_match = re.search(r'(\d{6}|\d{8})', href)
                                                        if date_match:
                                                            date_code = date_match.group(1)
                                                            if len(date_code) == 8:
                                                                return f"{date_code[:4]}-{date_code[4:6]}-{date_code[6:8]}"
                                                            elif len(date_code) == 6:
                                                                if date_code[:2] in ['20', '21', '22', '23']:
                                                                    return f"20{date_code[:2]}-{date_code[2:4]}-{date_code[4:6]}"
                                                        
                                                        # No date found - put at end (oldest)
                                                        return '0000-00-00'
                                                    except:
                                                        return '0000-00-00'
                                                
                                                # Sort links by date (newest first)
                                                links_with_dates = [(link, extract_link_date(link)) for link in links]
                                                links_with_dates.sort(key=lambda x: x[1], reverse=True)  # Newest first
                                                links = [link for link, _ in links_with_dates]
                                                
                                                logger.info(f"    Sorted {len(links)} links by date (newest first)")
                                                
                                                firmware_links_found = 0
                                                for link_idx, link in enumerate(links, 1):
                                                    if test_mode_limit_reached:
                                                        break
                                                    
                                                    # Check download limit BEFORE processing link (saves time)
                                                    if MAX_FIRMWARES_TO_DOWNLOAD > 0 and new_downloads_count >= MAX_FIRMWARES_TO_DOWNLOAD:
                                                        logger.info(f"  ⏹️  Download limit reached: Downloaded {new_downloads_count} NEW firmware(s) (limit: {MAX_FIRMWARES_TO_DOWNLOAD}), stopping...")
                                                        test_mode_limit_reached = True
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
                                                        stored_filename = ''  # Will be set if download succeeds
                                                        
                                                        # Extract version and model (we'll check existence AFTER getting real URL)
                                                        version = self.extract_version(link_text + ' ' + href)
                                                        context_text = collapse_content.inner_text()
                                                        hw_version = self.extract_hardware_version(context_text, model)
                                                        normalized_model = normalize_model_name(model)
                                                        
                                                        # Extract "Applied to:" section (e.g., "Applied to: DS-1200KI camera")
                                                        applied_to_text = extract_applied_to(context_text)
                                                        
                                                        # Extract all supported models from context (might include variants)
                                                        supported_models = extract_models(context_text + ' ' + link_text)
                                                        # Ensure the primary model is included
                                                        if normalized_model not in supported_models:
                                                            supported_models.insert(0, normalized_model)
                                                        
                                                        # Increment total found counter (count all firmwares we find)
                                                        total_found_count += 1
                                                        
                                                        # Direct firmware file link
                                                        if any(ext in href.lower() for ext in ['.dav', '.zip', '.pak', '.bin']):
                                                            is_firmware_link = True
                                                            # For direct links, check existence now
                                                            if version:
                                                                firmware_key = f"{normalized_model}_{hw_version}_{version}"
                                                                firmware_exists = firmware_key in self.firmwares_live
                                                                firmware_downloaded_this_run = firmware_key in downloaded_in_this_run
                                                                
                                                                if firmware_exists or firmware_downloaded_this_run:
                                                                    if firmware_downloaded_this_run:
                                                                        logger.info(f"    ⊘ Skipping duplicate firmware (already downloaded this run): {normalized_model} {hw_version} v{version}")
                                                                    else:
                                                                        skipped_existing_count += 1
                                                                        logger.info(f"    ⊘ Skipping existing firmware: {normalized_model} {hw_version} v{version} ({skipped_existing_count} skipped)")
                                                                    firmwares.append({
                                                                        'model': normalized_model,
                                                                        'hardware_version': hw_version,
                                                                        'version': version,
                                                                        'download_url': href,
                                                                        'local_file_path': '',
                                                                        'filename': '',
                                                                        'supported_models': supported_models,
                                                                        'applied_to': applied_to_text,
                                                                        'date': '',
                                                                        'changes': '',
                                                                        'notes': '',
                                                                        'source': 'live',
                                                                        'already_exists': True
                                                                    })
                                                                    continue
                                                                
                                                                # Check download limit for NEW firmwares (direct links)
                                                                if MAX_FIRMWARES_TO_DOWNLOAD > 0 and new_downloads_count >= MAX_FIRMWARES_TO_DOWNLOAD:
                                                                    logger.info(f"  ⏹️  Download limit reached: Downloaded {new_downloads_count} NEW firmware(s) (limit: {MAX_FIRMWARES_TO_DOWNLOAD}), stopping...")
                                                                    test_mode_limit_reached = True
                                                                    break
                                                                
                                                                # TODO: Direct links could be downloaded here, but currently only modal links are downloaded
                                                                # For now, just skip direct links (they'll be processed via modal if available)
                                                                logger.debug(f"    Found direct link but skipping download (modal links preferred): {normalized_model} {hw_version} v{version}")
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
                                                                        firmware_downloaded_this_run = firmware_key in downloaded_in_this_run
                                                                        
                                                                        if firmware_exists or firmware_downloaded_this_run:
                                                                            if firmware_downloaded_this_run:
                                                                                logger.info(f"    ⊘ Skipping duplicate firmware (already downloaded this run): {normalized_model} {hw_version} v{version}")
                                                                            else:
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
                                                                                'filename': '',
                                                                                'supported_models': supported_models,
                                                                                'applied_to': applied_to_text,
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
                                                                        
                                                                        # Verify file was actually saved BEFORE counting as successful
                                                                        if filepath.exists():
                                                                            file_size = filepath.stat().st_size
                                                                            local_file_path = str(filepath)  # Store for firmware dict
                                                                            stored_filename = filename  # Store filename for GitHub release linking
                                                                            
                                                                            # Track this firmware as downloaded in this run (prevent duplicates)
                                                                            if version:
                                                                                firmware_key = f"{normalized_model}_{hw_version}_{version}"
                                                                                downloaded_in_this_run.add(firmware_key)
                                                                            
                                                                            new_downloads_count += 1  # Only increment on successful download
                                                                            logger.info(f"    ✓ File downloaded to: {filepath} ({file_size:,} bytes) (NEW firmware #{new_downloads_count})")
                                                                        else:
                                                                            logger.error(f"    ✗ File download failed: {filepath} does not exist!")
                                                                            local_file_path = ''  # Clear path if file doesn't exist
                                                                            stored_filename = ''  # Clear filename if file doesn't exist
                                                                            # Don't increment counter - download failed
                                                                    except Exception as download_err:
                                                                        logger.warning(f"    ⚠ Download failed: {download_err}")
                                                                        import traceback
                                                                        logger.debug(f"    Traceback: {traceback.format_exc()}")
                                                                        local_file_path = ''  # Clear path on error
                                                                        stored_filename = ''  # Clear filename on error
                                                                        # Don't increment counter - download failed, continue to next firmware
                                                                        # Close modal and continue to next link
                                                                        try:
                                                                            close_btn = page.query_selector('dialog button, [role="dialog"] button, dialog [aria-label*="close" i], [role="dialog"] [aria-label*="close" i]')
                                                                            if close_btn:
                                                                                close_btn.click()
                                                                                time.sleep(0.5)
                                                                        except:
                                                                            pass  # Modal might already be closed
                                                                        continue  # Skip to next firmware link (don't add failed download to list)
                                                                    
                                                                    # Only log success message if download actually succeeded
                                                                    if local_file_path:
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
                                                        # Prioritize filename date over URL path date
                                                        # Filename dates are more accurate (e.g., 220822 = 2022-08-22)
                                                        # URL path dates are just year-month (e.g., /202211/ = 2022-11)
                                                        date_str = ''
                                                        
                                                        # First try to find date in link_text (filename) - more accurate
                                                        date_match = re.search(r'(\d{6}|\d{8})', link_text)
                                                        if date_match:
                                                            date_code = date_match.group(1)
                                                            if len(date_code) == 6:
                                                                date_str = f"20{date_code[:2]}-{date_code[2:4]}-{date_code[4:6]}"
                                                            elif len(date_code) == 8:
                                                                date_str = f"{date_code[:4]}-{date_code[4:6]}-{date_code[6:8]}"
                                                        
                                                        # If no date in filename, try URL (but URL dates are less reliable)
                                                        if not date_str:
                                                            date_match = re.search(r'(\d{6}|\d{8})', actual_download_url)
                                                            if date_match:
                                                                date_code = date_match.group(1)
                                                                # Only use URL date if it's 8 digits (YYYYMMDD), not 6 (could be YYMMDD or YYYYMM)
                                                                if len(date_code) == 8:
                                                                    date_str = f"{date_code[:4]}-{date_code[4:6]}-{date_code[6:8]}"
                                                                elif len(date_code) == 6:
                                                                    # Check if it looks like YYMMDD (starts with 20-23) vs YYYYMM (starts with 19-20)
                                                                    if date_code[:2] in ['20', '21', '22', '23']:
                                                                        # Likely YYMMDD format
                                                                        date_str = f"20{date_code[:2]}-{date_code[2:4]}-{date_code[4:6]}"
                                                                    # Otherwise skip - could be YYYYMM which isn't a full date
                                                        
                                                        # Add firmware to list (download happened in modal handling above)
                                                        firmwares.append({
                                                            'model': normalized_model,
                                                            'hardware_version': hw_version,
                                                            'version': version,
                                                            'download_url': actual_download_url,
                                                            'local_file_path': local_file_path,  # Path to downloaded file (if download succeeded)
                                                            'filename': stored_filename,  # Filename for GitHub release linking
                                                            'supported_models': supported_models,  # List of models this firmware supports
                                                            'applied_to': applied_to_text,  # "Applied to:" text from page
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
        
        # IMPORTANT: Only add firmware if download succeeded (has local_file_path)
        # Skip entries that failed to download
        local_file_path = fw_data.get('local_file_path', '')
        already_exists = fw_data.get('already_exists', False)
        
        # Don't add NEW entries if download failed (no local file)
        # If it already exists, we'll skip it at line 628 anyway
        if not local_file_path:
            logger.debug(f"  ⊘ Skipping firmware without downloaded file: {model} {hw_version} v{version}")
            return
        
        # Get/create device ID
        device_id = get_device_id(self.devices, model, hw_version)
        if device_id is None:
            device_id = create_device_id(self.devices, model, hw_version)
            logger.debug(f"Created device: {model} {hw_version} -> ID {device_id}")
        
        # Create key
        key = f"{model}_{hw_version}_{version}"
        
        if key not in self.firmwares_live:
            # Extract filename from local_file_path if available
            filename = fw_data.get('filename', '')
            if not filename and local_file_path:
                from pathlib import Path
                filename = Path(local_file_path).name
            
            self.firmwares_live[key] = {
                'device_id': device_id,
                'model': model,
                'hardware_version': hw_version,
                'version': version,
                'date': format_date(fw_data.get('date', '')),
                'download_url': fw_data.get('download_url', ''),
                'filename': filename,  # Filename for GitHub release linking
                'supported_models': fw_data.get('supported_models', [model]),  # List of models this firmware supports
                'applied_to': fw_data.get('applied_to', ''),  # "Applied to:" text from page
                'changes': fw_data.get('changes', ''),
                'notes': fw_data.get('notes', ''),
                'is_beta': is_beta_firmware(version, fw_data.get('notes', '')),
                'source': fw_data.get('source', 'live')
            }
            # Only count as scraped if we actually downloaded a file
            if local_file_path:
                self.scraped_count += 1
                logger.info(f"  ✓ Added NEW firmware: {model} {hw_version} v{version}")
                if self.scraped_count % 50 == 0:
                    logger.info(f"  Added {self.scraped_count} new firmwares so far...")
        else:
            logger.debug(f"  ⊘ Skipped existing firmware: {model} {hw_version} v{version}")
    
    def cleanup_failed_downloads(self):
        """Remove firmware entries that don't have corresponding files."""
        firmware_dir = Path('firmwares')
        if not firmware_dir.exists():
            return
        
        # Get list of actual firmware files
        firmware_files = set()
        for ext in ['.zip', '.dav', '.pak', '.bin']:
            for filepath in firmware_dir.glob(f'*{ext}'):
                firmware_files.add(filepath.name)
        
        # Remove entries that don't have files
        removed_count = 0
        keys_to_remove = []
        for key, fw_data in self.firmwares_live.items():
            # Check filename field first (most reliable)
            filename = fw_data.get('filename', '')
            if filename:
                if filename not in firmware_files:
                    # Try to match by version in filename (files might have different names)
                    version = fw_data.get('version', '')
                    found = False
                    if version:
                        # Try to find file with matching version
                        version_pattern = version.replace('.', '_')
                        for fname in firmware_files:
                            if version_pattern in fname.replace('.', '_') or f"V{version}" in fname:
                                # Found matching file - update filename
                                fw_data['filename'] = fname
                                found = True
                                logger.debug(f"  ✓ Matched file by version: {fname} -> {key}")
                                break
                    if not found:
                        # Don't remove if it has a model (might be synced from elsewhere)
                        model = fw_data.get('model', '')
                        if model == 'UNKNOWN':
                            keys_to_remove.append(key)
                        else:
                            logger.debug(f"  ⊘ Keeping entry without file (will sync): {key}")
                continue
            else:
                # Fallback: check download_url
                download_url = fw_data.get('download_url', '')
                if download_url:
                    # Extract filename from URL
                    url_filename = download_url.split('/')[-1].split('?')[0]
                    if url_filename and url_filename not in firmware_files:
                        # Check if file exists with different name pattern
                        model = fw_data.get('model', '')
                        version = fw_data.get('version', '')
                        # Try to find file by model/version pattern
                        found = False
                        for fname in firmware_files:
                            if version and (version.replace('.', '_') in fname.replace('.', '_') or f"V{version}" in fname):
                                # Found matching file - update filename
                                fw_data['filename'] = fname
                                found = True
                                break
                        if not found:
                            keys_to_remove.append(key)
                else:
                    # No filename and no download_url - might be a ghost entry
                    # But don't remove if it has a model (might be synced from elsewhere)
                    model = fw_data.get('model', '')
                    if model == 'UNKNOWN':
                        keys_to_remove.append(key)
        
        for key in keys_to_remove:
            del self.firmwares_live[key]
            removed_count += 1
        
        if removed_count > 0:
            logger.info(f"  🧹 Cleaned up {removed_count} firmware entry(ies) without files")
    
    def sync_firmwares_directory(self):
        """Sync firmware files in directory with JSON entries - add missing entries."""
        firmware_dir = Path('firmwares')
        if not firmware_dir.exists():
            return
        
        # Get list of actual firmware files
        firmware_files = {}
        for ext in ['.zip', '.dav', '.pak', '.bin']:
            for filepath in firmware_dir.glob(f'*{ext}'):
                firmware_files[filepath.name] = filepath
        
        # Find files that aren't in JSON
        added_count = 0
        for filename, filepath in firmware_files.items():
            # Check if this file is already in JSON
            found = False
            for key, fw_data in self.firmwares_live.items():
                if fw_data.get('filename') == filename:
                    found = True
                    # Update filename if it was missing
                    if not fw_data.get('filename'):
                        fw_data['filename'] = filename
                    break
            
            if not found:
                # Try to match by filename to existing entries first (might have model info)
                matched_existing = False
                for key, fw_data in self.firmwares_live.items():
                    existing_filename = fw_data.get('filename', '')
                    if existing_filename == filename:
                        # File already matched to an entry, skip
                        matched_existing = True
                        break
                    # Try to match by version if filename doesn't match
                    existing_version = fw_data.get('version', '')
                    match = re.search(r'V(\d+\.\d+\.\d+(?:\.\d+)?)', filename, re.IGNORECASE)
                    version = match.group(1) if match else None
                    if version and existing_version == version:
                        # Update existing entry with filename if missing
                        if not existing_filename:
                            fw_data['filename'] = filename
                            logger.debug(f"  ✓ Matched file to existing entry: {filename} -> {key}")
                            matched_existing = True
                            break
                
                if matched_existing:
                    continue
                
                # Try to extract model/version from filename
                # Pattern: Firmware__V1.0.6_191031_S3000312642.zip
                # Pattern: Firmware_Asia_V4.75.013_240919_S3000600889.zip
                match = re.search(r'V(\d+\.\d+\.\d+(?:\.\d+)?)', filename, re.IGNORECASE)
                version = match.group(1) if match else None
                
                # Try to extract model from filename - DON'T create entries without model info
                model_match = re.search(r'(DS-[0-9A-Z-]+|AE-[0-9A-Z-]+|IDS-[0-9A-Z-]+)', filename, re.IGNORECASE)
                model = model_match.group(1).upper() if model_match else None
                
                # Only sync if we can extract both model AND version from filename
                # Skip files without model info (they'll be synced from releases or scraping)
                if not model or not version:
                    logger.debug(f"  ⊘ Skipping firmware file without model info: {filename}")
                    continue
                
                # Extract date from filename if possible
                date_match = re.search(r'(\d{6}|\d{8})', filename)
                date_str = ''
                if date_match:
                    date_code = date_match.group(1)
                    if len(date_code) == 6:
                        date_str = f"20{date_code[:2]}-{date_code[2:4]}-{date_code[4:6]}"
                    elif len(date_code) == 8:
                        date_str = f"{date_code[:4]}-{date_code[4:6]}-{date_code[6:8]}"
                
                # Get or create device ID
                hw_version = 'UNKNOWN'
                device_id = get_device_id(self.devices, model, hw_version)
                if device_id is None:
                    device_id = create_device_id(self.devices, model, hw_version)
                
                # Create key
                key = f"{model}_{hw_version}_{version}"
                
                # Check if entry already exists with different filename (avoid duplicates)
                if key in self.firmwares_live:
                    # Update filename if missing
                    if not self.firmwares_live[key].get('filename'):
                        self.firmwares_live[key]['filename'] = filename
                        logger.debug(f"  ✓ Updated filename for existing entry: {key}")
                    continue
                
                # Add to JSON
                self.firmwares_live[key] = {
                    'device_id': device_id,
                    'model': model,
                    'hardware_version': hw_version,
                    'version': version,
                    'date': date_str,
                    'download_url': '',  # Will be filled from release if available
                    'filename': filename,
                    'supported_models': [model],
                    'applied_to': '',
                    'changes': '',
                    'notes': 'Synced from firmware directory',
                    'is_beta': is_beta_firmware(version, ''),
                    'source': 'directory_sync'
                }
                added_count += 1
                logger.info(f"  ✓ Synced firmware from directory: {filename} ({model} v{version})")
        
        if added_count > 0:
            logger.info(f"  📦 Synced {added_count} firmware file(s) from directory to JSON")
    
    def cleanup_empty_devices(self):
        """Remove devices that have no firmwares AND no files."""
        # Get all device IDs that have firmwares
        devices_with_firmwares = set()
        for fw_data in self.firmwares_live.values():
            device_id = fw_data.get('device_id')
            if device_id:
                devices_with_firmwares.add(str(device_id))
        
        # Check which devices have firmware files
        firmware_dir = Path('firmwares')
        devices_with_files = set()
        if firmware_dir.exists():
            for ext in ['.zip', '.dav', '.pak', '.bin']:
                for filepath in firmware_dir.glob(f'*{ext}'):
                    filename = filepath.name
                    # Try to match file to device by checking all firmwares
                    for fw_data in self.firmwares_live.values():
                        if fw_data.get('filename') == filename:
                            device_id = fw_data.get('device_id')
                            if device_id:
                                devices_with_files.add(str(device_id))
        
        # Remove devices without firmwares AND without files
        removed_count = 0
        devices_to_remove = []
        for device_id in self.devices.keys():
            if device_id not in devices_with_firmwares and device_id not in devices_with_files:
                # Only remove if device is UNKNOWN and has no files
                device_info = self.devices.get(device_id, {})
                if device_info.get('model') == 'UNKNOWN':
                    devices_to_remove.append(device_id)
        
        for device_id in devices_to_remove:
            del self.devices[device_id]
            removed_count += 1
        
        if removed_count > 0:
            logger.info(f"  🧹 Cleaned up {removed_count} device(s) without firmwares or files")
    
    def cleanup_unknown_entries(self):
        """Remove firmware entries with UNKNOWN model that don't have files or useful info."""
        firmware_dir = Path('firmwares')
        firmware_files = set()
        if firmware_dir.exists():
            for ext in ['.zip', '.dav', '.pak', '.bin']:
                for filepath in firmware_dir.glob(f'*{ext}'):
                    firmware_files.add(filepath.name)
        
        removed_count = 0
        keys_to_remove = []
        
        for key, fw_data in self.firmwares_live.items():
            model = fw_data.get('model', '')
            # Only remove UNKNOWN entries that:
            # 1. Are from directory sync (not from scraping)
            # 2. Don't have a file
            # 3. Don't have download_url or applied_to
            if model == 'UNKNOWN':
                filename = fw_data.get('filename', '')
                download_url = fw_data.get('download_url', '')
                applied_to = fw_data.get('applied_to', '')
                source = fw_data.get('source', '')
                
                # Keep if it has a file OR has useful info
                has_file = filename and filename in firmware_files
                has_useful_info = download_url or applied_to
                
                # Only remove if it's from directory sync AND has no file AND no useful info
                if source == 'directory_sync' and not has_file and not has_useful_info:
                    keys_to_remove.append(key)
        
        for key in keys_to_remove:
            del self.firmwares_live[key]
            removed_count += 1
        
        if removed_count > 0:
            logger.info(f"  🧹 Cleaned up {removed_count} incomplete UNKNOWN firmware entry(ies) without files")
    
    def sync_github_releases(self):
        """Sync GitHub releases with JSON - add missing entries from releases."""
        if not REQUESTS_AVAILABLE:
            logger.debug("  ⚠ Requests library not available, skipping GitHub releases sync")
            return
        
        logger.info("  🔄 Syncing GitHub releases with JSON...")
        
        # Get GitHub token if available (for higher rate limits)
        github_token = os.environ.get('GITHUB_TOKEN')
        headers = {}
        if github_token:
            headers['Authorization'] = f'token {github_token}'
        
        # Get all releases
        releases_url = f"{GITHUB_API_BASE}/{GITHUB_REPO}/releases"
        try:
            response = requests.get(releases_url, headers=headers, timeout=30)
            response.raise_for_status()
            releases = response.json()
        except Exception as e:
            logger.warning(f"  ⚠ Failed to fetch GitHub releases: {e}")
            return
        
        # Build mapping of filename -> model/version/date from release bodies
        # Release notes format: "### MODEL - vVERSION\n\n- **Supported Devices:** ...\n- **Release Date:** YYYY-MM-DD\n- **Download:** [📥 Download FILENAME](...)"
        filename_to_info = {}
        for release in releases:
            body = release.get('body', '')
            if not body:
                continue
            
            # Parse release body to extract model/version/date for each firmware
            # Pattern: "### MODEL - vVERSION" or "### UNKNOWN - vVERSION"
            # Split body into sections by "###"
            sections = re.split(r'###\s+', body)
            for section in sections[1:]:  # Skip first empty section
                # Extract model and version from header: "MODEL - vVERSION"
                header_match = re.match(r'([^-]+)\s+-\s+v(\d+\.\d+\.\d+(?:\.\d+)?)', section, re.IGNORECASE)
                if not header_match:
                    continue
                
                model = header_match.group(1).strip().upper()
                version = header_match.group(2).strip()
                
                # Skip UNKNOWN entries (they don't have model info)
                if model == 'UNKNOWN':
                    continue
                
                # Extract date: "Release Date: YYYY-MM-DD"
                date_match = re.search(r'Release Date:\s*(\d{4}-\d{2}-\d{2})', section, re.IGNORECASE)
                date_str = date_match.group(1) if date_match else ''
                
                # Extract filename from download link: "[📥 Download FILENAME](...)"
                # Pattern: [📥 Download FILENAME](url) - extract text between [ and ]
                filename_match = re.search(r'\[📥\s*Download\s+([^\]]+)\]', section, re.IGNORECASE)
                if filename_match:
                    filename = filename_match.group(1).strip()
                    filename_to_info[filename] = {
                        'model': model,
                        'version': version,
                        'date': date_str
                    }
                    logger.debug(f"  ✓ Extracted from release notes: {filename} -> {model} v{version}")
        
        # Also collect all firmware filenames from assets (fallback if not in release notes)
        release_filenames = set()
        for release in releases:
            assets = release.get('assets', [])
            for asset in assets:
                filename = asset.get('name', '')
                if filename and any(filename.lower().endswith(ext) for ext in ['.zip', '.dav', '.pak', '.bin']):
                    release_filenames.add(filename)
        
        logger.info(f"  Found {len(release_filenames)} firmware file(s) in GitHub releases")
        if filename_to_info:
            logger.info(f"  Extracted model info from {len(filename_to_info)} release note(s)")
        
        # Find files in releases that aren't in JSON
        added_count = 0
        for filename in release_filenames:
            # Check if this file is already in JSON
            found = False
            for key, fw_data in self.firmwares_live.items():
                if fw_data.get('filename') == filename:
                    found = True
                    break
            
            if not found:
                # Try to get model/version from release notes first
                info = filename_to_info.get(filename)
                if info:
                    model = info['model']
                    version = info['version']
                    date_str = info['date']
                else:
                    # Fallback: Try to extract model/version from filename
                    match = re.search(r'V(\d+\.\d+\.\d+(?:\.\d+)?)', filename, re.IGNORECASE)
                    version = match.group(1) if match else None
                    
                    # Try to extract model from filename
                    model_match = re.search(r'(DS-[0-9A-Z-]+|AE-[0-9A-Z-]+|IDS-[0-9A-Z-]+)', filename, re.IGNORECASE)
                    model = model_match.group(1).upper() if model_match else None
                    date_str = ''
                
                # Only sync if we have both model AND version
                if not model or not version:
                    logger.debug(f"  ⊘ Skipping release file without model info: {filename}")
                    continue
                
                # Extract date from filename if not already extracted from release notes
                if not date_str:
                    date_match = re.search(r'(\d{6}|\d{8})', filename)
                    if date_match:
                        date_code = date_match.group(1)
                        if len(date_code) == 6:
                            date_str = f"20{date_code[:2]}-{date_code[2:4]}-{date_code[4:6]}"
                        elif len(date_code) == 8:
                            date_str = f"{date_code[:4]}-{date_code[4:6]}-{date_code[6:8]}"
                
                if version:
                    # Get or create device ID
                    hw_version = 'UNKNOWN'
                    device_id = get_device_id(self.devices, model, hw_version)
                    if device_id is None:
                        device_id = create_device_id(self.devices, model, hw_version)
                    
                    # Create key
                    key = f"{model}_{hw_version}_{version}"
                    
                    # Create download URL (latest release)
                    download_url = f"https://github.com/{GITHUB_REPO}/releases/latest/download/{filename}"
                    
                    # Add to JSON
                    self.firmwares_live[key] = {
                        'device_id': device_id,
                        'model': model,
                        'hardware_version': hw_version,
                        'version': version,
                        'date': date_str,
                        'download_url': download_url,
                        'filename': filename,
                        'supported_models': [model],
                        'applied_to': '',
                        'changes': '',
                        'notes': 'Synced from GitHub releases',
                        'is_beta': is_beta_firmware(version, ''),
                        'source': 'github_releases_sync'
                    }
                    added_count += 1
                    logger.info(f"  ✓ Synced firmware from GitHub releases: {filename} ({model} v{version})")
        
        if added_count > 0:
            logger.info(f"  📦 Synced {added_count} firmware file(s) from GitHub releases to JSON")
        
        # Clean up entries that claim files exist in releases but don't
        removed_count = 0
        keys_to_remove = []
        for key, fw_data in self.firmwares_live.items():
            filename = fw_data.get('filename', '')
            download_url = fw_data.get('download_url', '')
            
            # If it claims to be from GitHub releases but file doesn't exist in releases
            if filename and 'github.com' in download_url and filename not in release_filenames:
                # Check if file exists locally
                firmware_dir = Path('firmwares')
                local_file_exists = False
                if firmware_dir.exists():
                    local_file_exists = (firmware_dir / filename).exists()
                
                # Only remove if not in releases AND not locally
                if not local_file_exists:
                    keys_to_remove.append(key)
        
        for key in keys_to_remove:
            del self.firmwares_live[key]
            removed_count += 1
        
        if removed_count > 0:
            logger.info(f"  🧹 Cleaned up {removed_count} firmware entry(ies) that don't exist in releases or locally")
    
    def save(self):
        """Save all data."""
        # Sync GitHub releases with JSON (add missing entries from releases)
        self.sync_github_releases()
        # Sync firmware directory with JSON (add missing entries)
        self.sync_firmwares_directory()
        # Clean up incomplete UNKNOWN entries
        self.cleanup_unknown_entries()
        # Clean up failed downloads before saving
        self.cleanup_failed_downloads()
        # Clean up devices without firmwares
        self.cleanup_empty_devices()
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
