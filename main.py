#!/usr/bin/env python3
"""Main script for Hikvision firmware archive scraper."""
import argparse
import json
import logging
import re
import time
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional
from urllib.parse import urljoin, urlparse, parse_qs

import requests
from bs4 import BeautifulSoup
from dateutil import parser as date_parser

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

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Hikvision download center URLs
HIKVISION_BASE_URL = "https://www.hikvision.com"
HIKVISION_DOWNLOAD_URL = "https://www.hikvision.com/en/support/download/firmware/"
HIKVISION_API_BASE = "https://www.hikvision.com/en/api"

# User agent to avoid blocking
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
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
        self.scraped_count = 0
        
    def fetch_page(self, url: str, retries: int = 3) -> Optional[BeautifulSoup]:
        """Fetch and parse a webpage with retry logic."""
        for attempt in range(retries):
            try:
                response = self.session.get(url, timeout=30)
                response.raise_for_status()
                return BeautifulSoup(response.content, 'html.parser')
            except requests.exceptions.RequestException as e:
                if attempt < retries - 1:
                    wait_time = (attempt + 1) * 2
                    logger.warning(f"Error fetching {url} (attempt {attempt + 1}/{retries}): {e}. Retrying in {wait_time}s...")
                    time.sleep(wait_time)
                else:
                    logger.error(f"Error fetching {url} after {retries} attempts: {e}")
                    return None
        return None
    
    def extract_model_from_filename(self, filename: str) -> Optional[str]:
        """Extract model number from Hikvision firmware filename.
        
        Hikvision filenames often contain model info:
        - digicap.dav (generic, model in metadata)
        - DS-2CD2XXX_5.7.0_220123.dav
        - IPC_XXX_5.7.0_220123.dav
        """
        # Try common patterns
        patterns = [
            r'([DS]-?2?[CD][A-Z0-9-]+)',  # DS-2CD2XXX, DS-2CD, etc.
            r'(IPC_[A-Z0-9-]+)',  # IPC_XXX
            r'(NVR_[A-Z0-9-]+)',  # NVR_XXX
            r'(DVR_[A-Z0-9-]+)',  # DVR_XXX
        ]
        
        for pattern in patterns:
            match = re.search(pattern, filename, re.IGNORECASE)
            if match:
                return match.group(1).upper()
        return None
    
    def extract_version_from_filename(self, filename: str) -> Optional[str]:
        """Extract firmware version from Hikvision filename.
        
        Common patterns:
        - V5.7.0_220123
        - 5.7.0_220123
        - V5.7.0 build 220123
        """
        # Remove extension
        name = Path(filename).stem
        
        # Try version patterns
        patterns = [
            r'[Vv]?(\d+\.\d+\.\d+(?:\.\d+)?)',  # V5.7.0 or 5.7.0
            r'(\d+\.\d+\.\d+)',  # 5.7.0
        ]
        
        for pattern in patterns:
            match = re.search(pattern, name)
            if match:
                return match.group(1)
        return None
    
    def extract_hardware_version(self, text: str, model: str) -> str:
        """Extract hardware version from text or infer from context.
        
        Hikvision hardware versions are often:
        - IPC_XXX (for IP cameras)
        - NVR_XXX (for NVRs)
        - DVR_XXX (for DVRs)
        - Or specific codes like "IPC_G0" etc.
        """
        # Look for hardware version patterns
        hw_patterns = [
            r'(IPC_[A-Z0-9]+)',
            r'(NVR_[A-Z0-9]+)',
            r'(DVR_[A-Z0-9]+)',
            r'Hardware[:\s]+([A-Z0-9_-]+)',
            r'HW[:\s]+([A-Z0-9_-]+)',
        ]
        
        for pattern in hw_patterns:
            match = re.search(pattern, text, re.IGNORECASE)
            if match:
                return match.group(1).upper()
        
        # Default based on model prefix
        if model.startswith('DS-2CD') or 'IPC' in model.upper():
            return 'IPC_G0'  # Generic IPC hardware
        elif 'NVR' in model.upper():
            return 'NVR_G0'  # Generic NVR hardware
        elif 'DVR' in model.upper():
            return 'DVR_G0'  # Generic DVR hardware
        
        return 'UNKNOWN'
    
    def parse_firmware_page(self, url: str) -> List[Dict]:
        """Parse a firmware download page and extract firmware information."""
        firmwares = []
        soup = self.fetch_page(url)
        if not soup:
            return firmwares
        
        # Hikvision pages typically have download links in various formats
        # Look for download links (common patterns)
        download_links = soup.find_all('a', href=True)
        
        for link in download_links:
            href = link.get('href', '')
            text = link.get_text(strip=True)
            
            # Skip non-firmware links
            if not any(ext in href.lower() for ext in ['.dav', '.zip', '.pak', '.bin']):
                continue
            
            # Make absolute URL
            if href.startswith('/'):
                href = urljoin(HIKVISION_BASE_URL, href)
            elif not href.startswith('http'):
                href = urljoin(url, href)
            
            # Try to extract info from link text and surrounding context
            parent = link.find_parent()
            context_text = parent.get_text() if parent else text
            
            # Extract model
            model = self.extract_model_from_filename(href) or self.extract_model_from_filename(text)
            if not model:
                # Try to find model in nearby text
                model_match = re.search(r'([DS]-?2?[CD][A-Z0-9-]+)', context_text, re.IGNORECASE)
                if model_match:
                    model = model_match.group(1).upper()
            
            # Extract version
            version = self.extract_version_from_filename(href) or self.extract_version_from_filename(text)
            
            # Extract hardware version
            hardware_version = self.extract_hardware_version(context_text, model or '')
            
            # Extract date from filename or context
            date_match = re.search(r'(\d{6}|\d{8})', href + text)
            date_str = ''
            if date_match:
                date_code = date_match.group(1)
                # Hikvision often uses YYMMDD format
                if len(date_code) == 6:
                    try:
                        year = '20' + date_code[:2]
                        month = date_code[2:4]
                        day = date_code[4:6]
                        date_str = f"{year}-{month}-{day}"
                    except:
                        pass
            
            # Extract changelog/notes from surrounding text
            changes = ''
            notes = ''
            
            # Look for release notes or changelog links
            release_notes_link = None
            for note_link in soup.find_all('a', href=True):
                note_text = note_link.get_text(strip=True).lower()
                if any(keyword in note_text for keyword in ['release note', 'changelog', 'what\'s new']):
                    release_notes_link = note_link.get('href')
                    break
            
            if model and version:
                firmware_data = {
                    'model': normalize_model_name(model),
                    'hardware_version': hardware_version,
                    'version': version,
                    'download_url': href,
                    'date': format_date(date_str) if date_str else '',
                    'changes': changes,
                    'notes': notes,
                    'source': 'live'
                }
                firmwares.append(firmware_data)
                logger.debug(f"Found firmware: {model} {hardware_version} v{version}")
        
        return firmwares
    
    def search_firmwares_by_model(self, model_prefix: str) -> List[Dict]:
        """Search for firmwares by model prefix/pattern."""
        firmwares = []
        
        # Hikvision's site uses search - try common model prefixes
        search_url = f"{HIKVISION_DOWNLOAD_URL}?keyword={model_prefix}"
        soup = self.fetch_page(search_url)
        
        if not soup:
            return firmwares
        
        # Find all firmware download links on search results page
        download_links = soup.find_all('a', href=True)
        
        for link in download_links:
            href = link.get('href', '')
            if any(ext in href.lower() for ext in ['.dav', '.zip', '.pak', '.bin']):
                # Parse individual firmware pages
                page_firmwares = self.parse_firmware_page(href)
                firmwares.extend(page_firmwares)
        
        return firmwares
    
    def scrape_firmwares(self) -> List[Dict]:
        """Scrape firmware information from Hikvision download center."""
        logger.info("Starting Hikvision firmware scrape...")
        firmwares = []
        
        # Fetch main download page
        soup = self.fetch_page(HIKVISION_DOWNLOAD_URL)
        if not soup:
            logger.error("Failed to fetch download center page")
            return firmwares
        
        # Hikvision's site structure varies - try multiple approaches
        
        # Approach 1: Find all download links on main page
        logger.info("Scanning main page for firmware links...")
        main_page_firmwares = self.parse_firmware_page(HIKVISION_DOWNLOAD_URL)
        firmwares.extend(main_page_firmwares)
        
        # Approach 2: Search common model prefixes
        common_prefixes = [
            'DS-2CD',  # IP Cameras
            'DS-2DE',  # PTZ Cameras
            'DS-76',   # NVRs
            'DS-77',   # NVRs
            'DS-86',   # NVRs
            'DS-96',   # NVRs
        ]
        
        logger.info(f"Searching for firmwares by model prefixes...")
        for prefix in common_prefixes:
            logger.info(f"Searching for {prefix}...")
            prefix_firmwares = self.search_firmwares_by_model(prefix)
            firmwares.extend(prefix_firmwares)
            time.sleep(1)  # Be nice to their servers
        
        # Deduplicate by model+hardware+version
        seen = set()
        unique_firmwares = []
        for fw in firmwares:
            key = (fw.get('model'), fw.get('hardware_version'), fw.get('version'))
            if key and key not in seen:
                seen.add(key)
                unique_firmwares.append(fw)
        
        logger.info(f"Found {len(unique_firmwares)} unique firmwares")
        return unique_firmwares
    
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
        self.scraped_count += 1
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
            parsed_url = urlparse(url)
            filename = Path(parsed_url.path).name
            
            # Extract model from filename
            if not model:
                model = self.extract_model_from_filename(filename) or ''
            
            # Extract version from filename
            if not version:
                version = self.extract_version_from_filename(filename) or ''
            
            # Extract hardware version
            if not hardware_version and model:
                hardware_version = self.extract_hardware_version(filename, model)
            
            # Extract date from filename
            if not date:
                date_match = re.search(r'(\d{6}|\d{8})', filename)
                if date_match:
                    date_code = date_match.group(1)
                    if len(date_code) == 6:
                        try:
                            year = '20' + date_code[:2]
                            month = date_code[2:4]
                            day = date_code[4:6]
                            date = f"{year}-{month}-{day}"
                        except:
                            pass
        
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
    add_parser.add_argument('--model', help='Device model name (e.g., DS-2CD2XXX)')
    add_parser.add_argument('--hw-version', dest='hardware_version', help='Hardware version (e.g., IPC_G0)')
    add_parser.add_argument('--version', help='Firmware version (e.g., 5.7.0)')
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
        logger.info(f"Scraping complete. Processed {scraper.scraped_count} new firmwares.")
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
