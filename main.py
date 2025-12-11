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

# Playwright for JavaScript rendering (optional but recommended)
try:
    from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeoutError
    PLAYWRIGHT_AVAILABLE = True
except ImportError:
    PLAYWRIGHT_AVAILABLE = False
    logger.warning("Playwright not available - JavaScript-rendered content will not be accessible")

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
    
    def __init__(self, use_playwright: bool = True):
        self.session = requests.Session()
        self.session.headers.update(HEADERS)
        self.devices = load_json('devices.json')
        self.firmwares_live = load_json('firmwares_live.json')
        self.firmwares_manual = load_json('firmwares_manual.json')
        self.firmware_info = load_json('firmware_info.json')
        self.scraped_count = 0
        self.use_playwright = use_playwright and PLAYWRIGHT_AVAILABLE
        if self.use_playwright:
            logger.info("Using Playwright for JavaScript rendering")
        else:
            logger.warning("Playwright not available - limited scraping capability")
        
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
    
    def search_firmwares_by_model(self, model_query: str) -> List[Dict]:
        """Search for firmwares by model name/query.
        
        Hikvision's search is at /en/search/ with keyword parameter.
        However, results are likely loaded via JavaScript, so this may not work
        with static HTML parsing alone.
        """
        firmwares = []
        
        # Hikvision search endpoint
        search_url = "https://www.hikvision.com/en/search/"
        params = {'keyword': model_query}
        
        try:
            response = self.session.get(search_url, params=params, timeout=30)
            response.raise_for_status()
            soup = BeautifulSoup(response.content, 'html.parser')
        except Exception as e:
            logger.error(f"Search failed for {model_query}: {e}")
            return firmwares
        
        # The search results page may have:
        # - Links to product pages (not direct firmware downloads)
        # - JavaScript-rendered results (not accessible via static HTML)
        # - Product cards/items that need further navigation
        
        # Look for product/firmware result containers
        # Common patterns: result-item, product-item, download-item, etc.
        result_selectors = [
            {'class': lambda x: x and 'result' in str(x).lower()},
            {'class': lambda x: x and 'product' in str(x).lower()},
            {'class': lambda x: x and 'item' in str(x).lower()},
            {'class': lambda x: x and 'firmware' in str(x).lower()},
        ]
        
        found_links = set()
        for selector in result_selectors:
            results = soup.find_all(['div', 'article', 'li', 'a'], selector)
            for result in results:
                # Look for download links within results
                links = result.find_all('a', href=True) if result.name != 'a' else [result]
                for link in links:
                    href = link.get('href', '')
                    if href and href not in found_links:
                        found_links.add(href)
                        # Check if it's a firmware download link
                        if any(ext in href.lower() for ext in ['.dav', '.zip', '.pak', '.bin']):
                            page_firmwares = self.parse_firmware_page(href)
                            firmwares.extend(page_firmwares)
                        # Or if it's a product page that might contain firmware links
                        elif 'firmware' in href.lower() or 'download' in href.lower():
                            page_firmwares = self.parse_firmware_page(href)
                            firmwares.extend(page_firmwares)
        
        return firmwares
    
    def scrape_with_playwright(self) -> List[Dict]:
        """Scrape using Playwright to handle JavaScript rendering."""
        if not self.use_playwright:
            return []
        
        firmwares = []
        logger.info("Starting Playwright-based scraping...")
        
        with sync_playwright() as p:
            # Launch browser (headless for GitHub Actions)
            browser = p.chromium.launch(headless=True)
            context = browser.new_context(
                user_agent=HEADERS['User-Agent'],
                viewport={'width': 1920, 'height': 1080}
            )
            page = context.new_page()
            
            try:
                # Navigate to firmware page
                logger.info(f"Loading {HIKVISION_DOWNLOAD_URL}...")
                page.goto(HIKVISION_DOWNLOAD_URL, wait_until='networkidle', timeout=60000)
                time.sleep(3)  # Wait for JS to load
                
                # Get page content after JS rendering
                html = page.content()
                soup = BeautifulSoup(html, 'html.parser')
                
                # Look for firmware download links in rendered content
                download_links = soup.find_all('a', href=True)
                logger.info(f"Found {len(download_links)} links on page")
                
                for link in download_links:
                    href = link.get('href', '')
                    if any(ext in href.lower() for ext in ['.dav', '.zip', '.pak', '.bin']):
                        # Make absolute URL
                        if href.startswith('/'):
                            href = urljoin(HIKVISION_BASE_URL, href)
                        elif not href.startswith('http'):
                            href = urljoin(HIKVISION_DOWNLOAD_URL, href)
                        
                        # Extract firmware info
                        text = link.get_text(strip=True)
                        parent_text = ''
                        if link.find_parent():
                            parent_text = link.find_parent().get_text(strip=True)
                        
                        model = self.extract_model_from_filename(href) or self.extract_model_from_filename(text)
                        version = self.extract_version_from_filename(href) or self.extract_version_from_filename(text)
                        
                        if model and version:
                            hardware_version = self.extract_hardware_version(text + ' ' + parent_text, model)
                            
                            firmware_data = {
                                'model': normalize_model_name(model),
                                'hardware_version': hardware_version,
                                'version': version,
                                'download_url': href,
                                'date': '',
                                'changes': '',
                                'notes': '',
                                'source': 'live'
                            }
                            firmwares.append(firmware_data)
                            logger.debug(f"Found firmware: {model} {hardware_version} v{version}")
                
                # Try searching for common models
                logger.info("Searching for common camera models...")
                common_models = [
                    'DS-2CD2',   # IP Camera series
                    'DS-2DE',    # PTZ Cameras
                    'DS-76',     # NVRs
                    'DS-77',     # NVRs
                ]
                
                for model_query in common_models:
                    try:
                        logger.info(f"Searching for {model_query}...")
                        search_url = f"https://www.hikvision.com/en/search/?keyword={model_query}"
                        page.goto(search_url, wait_until='networkidle', timeout=60000)
                        time.sleep(3)  # Wait for results to load
                        
                        # Get search results
                        search_html = page.content()
                        search_soup = BeautifulSoup(search_html, 'html.parser')
                        
                        # Find firmware links in search results
                        result_links = search_soup.find_all('a', href=True)
                        for link in result_links:
                            href = link.get('href', '')
                            if any(ext in href.lower() for ext in ['.dav', '.zip', '.pak', '.bin', 'firmware']):
                                if href.startswith('/'):
                                    href = urljoin(HIKVISION_BASE_URL, href)
                                
                                # Navigate to firmware page if it's a product page
                                if 'firmware' in href.lower() and '.dav' not in href.lower():
                                    try:
                                        page.goto(href, wait_until='networkidle', timeout=30000)
                                        time.sleep(2)
                                        fw_page_html = page.content()
                                        fw_soup = BeautifulSoup(fw_page_html, 'html.parser')
                                        page_firmwares = self.parse_firmware_page_from_soup(fw_soup, href)
                                        firmwares.extend(page_firmwares)
                                    except Exception as e:
                                        logger.debug(f"Could not load {href}: {e}")
                        
                        time.sleep(2)  # Be respectful
                    except Exception as e:
                        logger.warning(f"Search failed for {model_query}: {e}")
                
            finally:
                browser.close()
        
        return firmwares
    
    def parse_firmware_page_from_soup(self, soup: BeautifulSoup, base_url: str) -> List[Dict]:
        """Parse firmware information from a BeautifulSoup object."""
        firmwares = []
        download_links = soup.find_all('a', href=True)
        
        for link in download_links:
            href = link.get('href', '')
            if any(ext in href.lower() for ext in ['.dav', '.zip', '.pak', '.bin']):
                if href.startswith('/'):
                    href = urljoin(HIKVISION_BASE_URL, href)
                elif not href.startswith('http'):
                    href = urljoin(base_url, href)
                
                text = link.get_text(strip=True)
                context = soup.get_text()
                
                model = self.extract_model_from_filename(href) or self.extract_model_from_filename(text)
                version = self.extract_version_from_filename(href) or self.extract_version_from_filename(text)
                
                if model and version:
                    hardware_version = self.extract_hardware_version(context, model)
                    firmware_data = {
                        'model': normalize_model_name(model),
                        'hardware_version': hardware_version,
                        'version': version,
                        'download_url': href,
                        'date': '',
                        'changes': '',
                        'notes': '',
                        'source': 'live'
                    }
                    firmwares.append(firmware_data)
        
        return firmwares
    
    def scrape_firmwares(self) -> List[Dict]:
        """Scrape firmware information from Hikvision download center.
        
        Uses Playwright if available to handle JavaScript rendering.
        Falls back to static HTML scraping if Playwright is not available.
        """
        logger.info("Starting Hikvision firmware scrape...")
        firmwares = []
        
        # Use Playwright if available (handles JavaScript)
        if self.use_playwright:
            logger.info("Using Playwright for JavaScript rendering...")
            firmwares.extend(self.scrape_with_playwright())
        else:
            # Fallback to static HTML scraping
            logger.warning("Playwright not available - using static HTML scraping (limited)")
            soup = self.fetch_page(HIKVISION_DOWNLOAD_URL)
            if soup:
                firmwares.extend(self.parse_firmware_page_from_soup(soup, HIKVISION_DOWNLOAD_URL))
        
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
