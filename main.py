#!/usr/bin/env python3
"""Main script for Hikvision firmware archive."""
import argparse
import json
import logging
import re
import sys
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional
from urllib.parse import urljoin, urlparse

import requests
from bs4 import BeautifulSoup
from dateutil import parser as date_parser

from common import (
    create_device_id,
    format_date,
    get_device_id,
    is_beta_firmware,
    load_json,
    merge_dicts,
    normalize_model_name,
    parse_version,
    save_json,
)

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Hikvision download center URLs
HIKVISION_BASE_URL = "https://www.hikvision.com"
HIKVISION_DOWNLOAD_URL = "https://www.hikvision.com/en/support/download/firmware/"

# User agent to avoid blocking
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}


class HikvisionFirmwareScraper:
    """Scraper for Hikvision firmware download center."""
    
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update(HEADERS)
        self.devices = load_json('devices.json')
        self.firmwares_live = load_json('firmwares_live.json')
        self.firmwares_manual = load_json('firmwares_manual.json')
        self.firmware_info = load_json('firmware_info.json')
    
    def fetch_page(self, url: str) -> Optional[BeautifulSoup]:
        """Fetch and parse a webpage."""
        try:
            response = self.session.get(url, timeout=30)
            response.raise_for_status()
            return BeautifulSoup(response.content, 'html.parser')
        except Exception as e:
            logger.error(f"Error fetching {url}: {e}")
            return None
    
    def extract_firmware_info(self, firmware_element) -> Optional[Dict]:
        """Extract firmware information from HTML element."""
        # This is a placeholder - actual implementation depends on Hikvision's HTML structure
        # You'll need to inspect their website to get the correct selectors
        try:
            # Example structure (adjust based on actual HTML):
            # - Model name
            # - Hardware version
            # - Firmware version
            # - Release date
            # - Download link
            # - Changelog/notes
            
            firmware_data = {
                'version': '',
                'date': '',
                'download_url': '',
                'changes': '',
                'notes': ''
            }
            
            # TODO: Implement actual extraction based on Hikvision's HTML structure
            # This will require inspecting their download center page
            
            return firmware_data if firmware_data['version'] else None
        except Exception as e:
            logger.error(f"Error extracting firmware info: {e}")
            return None
    
    def scrape_firmwares(self) -> List[Dict]:
        """Scrape firmware information from Hikvision download center."""
        logger.info("Starting firmware scrape...")
        firmwares = []
        
        # Fetch the download center page
        soup = self.fetch_page(HIKVISION_DOWNLOAD_URL)
        if not soup:
            logger.error("Failed to fetch download center page")
            return firmwares
        
        # TODO: Implement actual scraping logic
        # This will require:
        # 1. Finding product categories/pages
        # 2. Navigating to individual product pages
        # 3. Extracting firmware information
        # 4. Following pagination if needed
        
        logger.info(f"Found {len(firmwares)} firmwares")
        return firmwares
    
    def process_firmware(self, firmware_data: Dict) -> None:
        """Process a single firmware entry."""
        model = normalize_model_name(firmware_data.get('model', ''))
        hardware_version = firmware_data.get('hardware_version', '')
        version = firmware_data.get('version', '')
        
        if not all([model, hardware_version, version]):
            logger.warning(f"Incomplete firmware data: {firmware_data}")
            return
        
        # Get or create device ID
        device_id = get_device_id(self.devices, model, hardware_version)
        if device_id is None:
            device_id = create_device_id(self.devices, model, hardware_version)
            logger.info(f"Created new device: {model} ({hardware_version}) -> ID {device_id}")
        
        # Create firmware key
        firmware_key = f"{model}_{hardware_version}_{version}"
        
        # Check if firmware already exists
        if firmware_key in self.firmwares_live:
            logger.debug(f"Firmware already exists: {firmware_key}")
            return
        
        # Add firmware
        firmware_entry = {
            'device_id': device_id,
            'model': model,
            'hardware_version': hardware_version,
            'version': version,
            'date': format_date(firmware_data.get('date', '')),
            'download_url': firmware_data.get('download_url', ''),
            'changes': firmware_data.get('changes', ''),
            'notes': firmware_data.get('notes', ''),
            'is_beta': is_beta_firmware(version, firmware_data.get('notes', '')),
            'source': firmware_data.get('source', 'live')
        }
        
        self.firmwares_live[firmware_key] = firmware_entry
        logger.info(f"Added firmware: {model} {hardware_version} v{version}")
    
    def save_data(self):
        """Save all data to JSON files."""
        save_json('devices.json', self.devices)
        save_json('firmwares_live.json', self.firmwares_live)
        logger.info("Data saved successfully")
    
    def add_firmware_manual(self, url: str, model: str = '', hardware_version: str = '', 
                           version: str = '', date: str = '', changes: str = '', 
                           notes: str = '', source: str = 'manual'):
        """Manually add a firmware entry."""
        if not url:
            logger.error("URL is required")
            return
        
        # Try to extract info from URL if not provided
        if not all([model, hardware_version, version]):
            # Attempt to extract from URL or filename
            parsed_url = urlparse(url)
            filename = Path(parsed_url.path).name
            
            # Try to parse filename for model/version info
            # This is Hikvision-specific - adjust based on their naming convention
            # Example: DS-2CD2XXX_5.7.0_220123.zip
            match = re.search(r'([A-Z0-9-]+)_?([0-9.]+)', filename, re.IGNORECASE)
            if match:
                if not model:
                    model = match.group(1)
                if not version:
                    version = match.group(2)
        
        if not all([model, hardware_version, version]):
            logger.error("Could not determine model, hardware_version, and version. Please provide them manually.")
            return
        
        firmware_data = {
            'model': normalize_model_name(model),
            'hardware_version': hardware_version,
            'version': version,
            'download_url': url,
            'date': format_date(date) if date else '',
            'changes': changes,
            'notes': notes,
            'source': source
        }
        
        self.process_firmware(firmware_data)
        self.save_data()
        logger.info(f"Manually added firmware: {model} {hardware_version} v{version}")


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(description='Hikvision firmware archive scraper')
    subparsers = parser.add_subparsers(dest='command', help='Commands')
    
    # Scrape command
    scrape_parser = subparsers.add_parser('scrape', help='Scrape firmware data from Hikvision website')
    
    # Add command
    add_parser = subparsers.add_parser('add', help='Manually add a firmware')
    add_parser.add_argument('url', help='Firmware download URL')
    add_parser.add_argument('--model', help='Device model name')
    add_parser.add_argument('--hw-version', dest='hardware_version', help='Hardware version')
    add_parser.add_argument('--version', help='Firmware version')
    add_parser.add_argument('--date', help='Release date (YYYY-MM-DD)')
    add_parser.add_argument('--changes', help='Changelog/description')
    add_parser.add_argument('--notes', help='Additional notes')
    add_parser.add_argument('--source', default='manual', help='Source of firmware')
    
    args = parser.parse_args()
    
    scraper = HikvisionFirmwareScraper()
    
    if args.command == 'scrape':
        firmwares = scraper.scrape_firmwares()
        for firmware in firmwares:
            scraper.process_firmware(firmware)
        scraper.save_data()
        logger.info(f"Scraping complete. Processed {len(firmwares)} firmwares.")
    elif args.command == 'add':
        scraper.add_firmware_manual(
            url=args.url,
            model=args.model or '',
            hardware_version=args.hardware_version or '',
            version=args.version or '',
            date=args.date or '',
            changes=args.changes or '',
            notes=args.notes or '',
            source=args.source
        )
    else:
        parser.print_help()


if __name__ == '__main__':
    main()
