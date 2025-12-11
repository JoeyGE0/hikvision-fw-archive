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
        
        with sync_playwright() as p:
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
            
            for search_term in search_terms:
                try:
                    logger.info(f"Searching for: {search_term}")
                    
                    # Clear and fill search
                    search_input.fill('')
                    search_input.fill(search_term)
                    search_input.press('Enter')
                    time.sleep(5)  # Wait for results
                    
                    # Click "View more" button multiple times to load all results
                    view_more_clicked = 0
                    while view_more_clicked < 10:  # Limit to prevent infinite loop
                        view_more_btn = page.query_selector('div.action-btn:has-text("View more")')
                        if view_more_btn and view_more_btn.is_visible():
                            view_more_btn.click()
                            time.sleep(2)
                            view_more_clicked += 1
                        else:
                            break
                    
                    # Find all firmware model titles - limit to first 100 to avoid timeout
                    firmware_titles = page.query_selector_all('div.main-title')
                    logger.info(f"Found {len(firmware_titles)} firmware models (processing first 100)")
                    
                    # Process only first 100 to avoid timeout
                    for i, title_element in enumerate(firmware_titles[:100]):
                        try:
                            model_text = title_element.inner_text().strip()
                            model = self.extract_model(model_text)
                            
                            if not model:
                                continue
                            
                            # Click to expand
                            title_element.click()
                            time.sleep(0.5)  # Shorter wait
                            
                            # Find the collapse content
                            target_id = title_element.get_attribute('data-target') or ''
                            if target_id:
                                target_id = target_id.replace('#', '')
                                collapse_content = page.query_selector(f'#{target_id}')
                                
                                if collapse_content and collapse_content.is_visible():
                                    # Get all links in expanded content
                                    links = collapse_content.query_selector_all('a[href]')
                                    
                                    for link in links:
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
                                            logger.info(f"Found: {model} {hw_version} v{version}")
                            
                        except Exception as e:
                            logger.debug(f"Error on item {i}: {e}")
                            continue
                    
                    time.sleep(2)  # Be respectful
                    
                except Exception as e:
                    logger.warning(f"Search failed for {search_term}: {e}")
                    continue
            
            browser.close()
        
        # Deduplicate
        seen = set()
        unique_firmwares = []
        for fw in firmwares:
            key = (fw['model'], fw['hardware_version'], fw['version'])
            if key not in seen:
                seen.add(key)
                unique_firmwares.append(fw)
        
        logger.info(f"Found {len(unique_firmwares)} unique firmwares")
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
            logger.info(f"Created device: {model} {hw_version} -> ID {device_id}")
        
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
            logger.info(f"Added: {model} {hw_version} v{version}")
    
    def save(self):
        """Save all data."""
        save_json('devices.json', self.devices)
        save_json('firmwares_live.json', self.firmwares_live)
        logger.info("Data saved")
    
    def scrape(self):
        """Main scrape method."""
        logger.info("Starting Hikvision firmware scrape...")
        firmwares = self.scrape_with_playwright()
        
        for fw in firmwares:
            self.process_firmware(fw)
        
        self.save()
        logger.info(f"Scraping complete. Added {self.scraped_count} new firmwares.")


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
