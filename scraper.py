#!/usr/bin/env python3
"""
Hikvision firmware scraper - built specifically for how Hikvision's site actually works.
Not a copy of Reolink - this is Hikvision-specific.
"""
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

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

BASE_URL = "https://www.hikvision.com"


def load_json(filepath: str) -> dict:
    """Load JSON file."""
    if Path(filepath).exists():
        with open(filepath, 'r') as f:
            return json.load(f)
    return {}


def save_json(filepath: str, data: dict):
    """Save JSON file."""
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def extract_model_from_text(text: str) -> Optional[str]:
    """Extract Hikvision model number from text."""
    # Hikvision models: DS-2CD, DS-2DE, DS-76, etc.
    match = re.search(r'(DS-[0-9A-Z-]+)', text, re.IGNORECASE)
    return match.group(1).upper() if match else None


def extract_version_from_text(text: str) -> Optional[str]:
    """Extract firmware version from text."""
    # Versions like V5.7.0, 5.7.0, etc.
    match = re.search(r'[Vv]?(\d+\.\d+\.\d+(?:\.\d+)?)', text)
    return match.group(1) if match else None


class HikvisionScraper:
    """Scraper built specifically for Hikvision's site structure."""
    
    def __init__(self):
        self.firmwares = load_json('firmwares.json')
        self.use_playwright = PLAYWRIGHT_AVAILABLE
        
    def scrape(self) -> List[Dict]:
        """Scrape firmware from Hikvision's site."""
        if not self.use_playwright:
            logger.error("Playwright required for Hikvision's JavaScript-heavy site")
            return []
        
        firmwares = []
        
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()
            
            # Hikvision's firmware page
            firmware_url = f"{BASE_URL}/en/support/download/firmware/"
            logger.info(f"Loading {firmware_url}")
            page.goto(firmware_url, wait_until='networkidle', timeout=60000)
            time.sleep(3)
            
            # Hikvision uses search - need to find how it actually works
            # For now, collect any firmware links we can find
            links = page.query_selector_all('a[href]')
            logger.info(f"Found {len(links)} links on page")
            
            for link in links:
                href = link.get_attribute('href') or ''
                text = link.inner_text().strip()
                
                # Look for firmware file links
                if any(ext in href.lower() for ext in ['.dav', '.zip', '.pak', '.bin']):
                    if href.startswith('/'):
                        href = urljoin(BASE_URL, href)
                    
                    model = extract_model_from_text(text + ' ' + href)
                    version = extract_version_from_text(text + ' ' + href)
                    
                    if model and version:
                        firmwares.append({
                            'model': model,
                            'version': version,
                            'url': href,
                            'source': 'hikvision'
                        })
                        logger.info(f"Found: {model} v{version}")
            
            browser.close()
        
        return firmwares
    
    def save(self):
        """Save scraped firmwares."""
        # Merge with existing
        for fw in self.firmwares.values():
            key = f"{fw['model']}_{fw['version']}"
            if key not in self.firmwares:
                self.firmwares[key] = fw
        
        save_json('firmwares.json', self.firmwares)


if __name__ == '__main__':
    scraper = HikvisionScraper()
    firmwares = scraper.scrape()
    logger.info(f"Scraped {len(firmwares)} firmwares")
    scraper.save()
