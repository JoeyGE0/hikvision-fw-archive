#!/usr/bin/env python3
"""Hikvision firmware scraper - actually works with their site structure."""
import argparse
import json
import logging
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

BASE_URL = "https://www.hikvision.com"
FIRMWARE_URL = f"{BASE_URL}/en/support/download/firmware/"


class HikvisionScraper:
    """Scraper that actually works with Hikvision's site structure."""
    
    def __init__(self):
        self.devices = load_json('devices.json')
        self.firmwares_live = load_json('firmwares_live.json')
        self.firmwares_manual = load_json('firmwares_manual.json')
        self.firmware_info = load_json('firmware_info.json')
        self.scraped_count = 0
        
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
                        
                        for batch_num in range(total_batches):
                            start_idx = batch_num * batch_size
                            end_idx = min(start_idx + batch_size, len(firmware_titles))
                            batch = firmware_titles[start_idx:end_idx]
                            
                            logger.info(f"  → Processing batch {batch_num + 1}/{total_batches} (items {start_idx + 1}-{end_idx})...")
                            
                            for i, title_element in enumerate(batch, start_idx + 1):
                                try:
                                    model_text = title_element.inner_text().strip()
                                    model = self.extract_model(model_text)
                                    
                                    if not model:
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
                                            
                                            for link in links:
                                                try:
                                                    href = link.get_attribute('href') or ''
                                                    link_text = link.inner_text().strip()
                                                    
                                                    # Only process actual firmware file links
                                                    if any(ext in href.lower() for ext in ['.dav', '.zip', '.pak', '.bin']):
                                                        if href.startswith('/'):
                                                            href = urljoin(BASE_URL, href)
                                                        elif not href.startswith('http'):
                                                            href = urljoin(FIRMWARE_URL, href)
                                                        
                                                        version = self.extract_version(link_text + ' ' + href)
                                                        if not version:
                                                            continue
                                                        
                                                        context_text = collapse_content.inner_text()
                                                        hw_version = self.extract_hardware_version(context_text, model)
                                                        
                                                        # Extract date
                                                        date_match = re.search(r'(\d{6}|\d{8})', href + link_text)
                                                        date_str = ''
                                                        if date_match:
                                                            date_code = date_match.group(1)
                                                            if len(date_code) == 6:
                                                                date_str = f"20{date_code[:2]}-{date_code[2:4]}-{date_code[4:6]}"
                                                        
                                                        firmwares.append({
                                                            'model': normalize_model_name(model),
                                                            'hardware_version': hw_version,
                                                            'version': version,
                                                            'download_url': href,
                                                            'date': date_str,
                                                            'changes': '',
                                                            'notes': '',
                                                            'source': 'live'
                                                        })
                                                except Exception as link_err:
                                                    logger.debug(f"    Link processing error: {link_err}")
                                                    continue
                                
                                except Exception as e:
                                    logger.debug(f"  Error on item {i}: {e}")
                                    continue
                            
                            # Small delay between batches
                            if batch_num < total_batches - 1:
                                time.sleep(1)
                        
                        fw_count_after = len(firmwares)
                        fw_found_this_search = fw_count_after - fw_count_before
                        logger.info(f"  ✓ Found {fw_found_this_search} firmwares from {search_term} (total so far: {fw_count_after})")
                        
                        time.sleep(2)  # Be respectful
                    
                    except Exception as e:
                        logger.warning(f"Search failed for {search_term}: {e}")
                        continue
                
                browser.close()
        except KeyboardInterrupt:
            logger.warning("Scraping interrupted by user")
            if browser:
                browser.close()
        except Exception as e:
            logger.error(f"Playwright error: {e}")
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
            if self.scraped_count % 50 == 0:
                logger.info(f"  Added {self.scraped_count} new firmwares so far...")
    
    def save(self):
        """Save all data."""
        save_json('devices.json', self.devices)
        save_json('firmwares_live.json', self.firmwares_live)
        logger.info("Data saved")
    
    def scrape(self):
        """Main scrape method."""
        logger.info("=" * 60)
        logger.info("Starting Hikvision firmware scrape...")
        logger.info("=" * 60)
        
        start_time = time.time()
        firmwares = self.scrape_with_playwright()
        
        logger.info(f"→ Processing {len(firmwares)} firmwares into database...")
        processed = 0
        for idx, fw in enumerate(firmwares, 1):
            if idx % 100 == 0 or idx == len(firmwares):
                logger.info(f"  Processing firmware {idx}/{len(firmwares)}...")
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
    
    args = parser.parse_args()
    
    scraper = HikvisionScraper()
    
    if args.command == 'scrape':
        scraper.scrape()
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
