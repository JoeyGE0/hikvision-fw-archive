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
    extract_release_notes_url,
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

HTTP_USER_AGENT = (
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
    'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
)

HTTP_HEADERS = {
    'User-Agent': HTTP_USER_AGENT,
    'Accept': (
        'text/html,application/xhtml+xml,application/xml;q=0.9,'
        'image/avif,image/webp,image/apng,*/*;q=0.8'
    ),
    'Accept-Language': 'en-US,en;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Referer': FIRMWARE_URL,
    'DNT': '1',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'Cache-Control': 'max-age=0',
}

# Default: HTTP catalog parse (fast, reliable). Set USE_PLAYWRIGHT=1 to use legacy browser scraper.
USE_HTTP_SCRAPER = os.environ.get('USE_PLAYWRIGHT', '').lower() not in ('1', 'true', 'yes')

# GitHub repo info for releases sync
GITHUB_REPO = "JoeyGE0/hikvision-fw-archive"
GITHUB_API_BASE = "https://api.github.com/repos"

# TEST MODE: Set to True to only scrape 1 firmware file (prevents IP banning/rate limiting)
# Maximum number of firmware files to download (0 = unlimited)
# Set this to limit downloads and avoid hitting rate limits
MAX_FIRMWARES_TO_DOWNLOAD = 10  # Downloads 10 new firmwares per run (20 per day)

# Stop when this many models in a row have only already-archived firmware (caught-up runs)
CONSECUTIVE_FULLY_SKIPPED_MODELS_LIMIT = int(
    os.environ.get('CONSECUTIVE_FULLY_SKIPPED_MODELS_LIMIT', '40')
)

# Legacy TEST_MODE (deprecated - use MAX_FIRMWARES_TO_DOWNLOAD instead)
TEST_MODE = False
MAX_FIRMWARES_IN_TEST_MODE = 1

# One-shot priority list (see priority_models.json.example)
PRIORITY_MODELS_FILE = 'priority_models.json'


class HikvisionScraper:
    """Scraper that actually works with Hikvision's site structure."""
    
    def __init__(self):
        self.devices = load_json('devices.json')
        self.firmwares_live = load_json('firmwares_live.json')
        self.firmwares_manual = load_json('firmwares_manual.json')
        self.firmware_info = load_json('firmware_info.json')
        self.scraped_count = 0
        self.errors = []
        self._catalog_fetch_method = 'unknown'
        self._catalog_entry_count = 0
        self._priority_patterns: List[str] = []
        self._priority_one_shot = False
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

    @staticmethod
    def _expand_priority_patterns(raw_patterns: List[str]) -> List[str]:
        """Split comma/slash-separated user patterns into match tokens."""
        expanded: List[str] = []
        seen: set = set()

        def add_pattern(part: str) -> None:
            part = part.strip().upper()
            if not part or part in seen:
                return
            seen.add(part)
            expanded.append(part)
            # Hikvision often uses G2P-LIUF in catalog vs G2-LIUF on the label
            if 'G2-LIUF' in part and 'G2P-LIUF' not in part:
                add_pattern(part.replace('G2-LIUF', 'G2P-LIUF'))
            elif 'G2P-LIUF' in part and 'G2-LIUF' not in part:
                add_pattern(part.replace('G2P-LIUF', 'G2-LIUF'))

        for raw in raw_patterns:
            if not raw:
                continue
            for part in re.split(r'[/,]+', str(raw).strip()):
                add_pattern(part)
        return expanded

    def load_priority_models(self) -> List[str]:
        """Load one-shot priority model list from file or PRIORITY_MODELS env."""
        patterns: List[str] = []
        one_shot = True

        env_raw = os.environ.get('PRIORITY_MODELS', '').strip()
        if env_raw:
            patterns = self._expand_priority_patterns(
                [p.strip() for p in re.split(r'[,\n]+', env_raw) if p.strip()]
            )
            one_shot = os.environ.get('PRIORITY_MODELS_ONE_SHOT', '1').lower() not in (
                '0', 'false', 'no',
            )
        elif os.path.exists(PRIORITY_MODELS_FILE):
            data = load_json(PRIORITY_MODELS_FILE)
            if isinstance(data, list):
                patterns = self._expand_priority_patterns([str(x) for x in data])
            elif isinstance(data, dict):
                patterns = self._expand_priority_patterns(
                    [str(x) for x in data.get('models', [])]
                )
                one_shot = bool(data.get('one_shot', True))

        self._priority_patterns = patterns
        self._priority_one_shot = one_shot and bool(patterns)
        if patterns:
            logger.info(
                f'[PRIORITY] {len(patterns)} pattern(s), '
                f'{"one-shot" if self._priority_one_shot else "repeat"}: '
                f'{", ".join(patterns)}'
            )
        elif os.path.exists(PRIORITY_MODELS_FILE):
            logger.info(f'[PRIORITY] {PRIORITY_MODELS_FILE} exists but has no models')
        else:
            logger.info('[PRIORITY] none (no file or env)')
        return patterns

    def model_matches_priority(self, model: str) -> bool:
        """True if catalog model matches any priority pattern (prefix / substring)."""
        m = (model or '').upper()
        if not m or m == 'UNKNOWN':
            return False
        for pattern in self._priority_patterns:
            if len(pattern) < 8:
                continue
            if m.startswith(pattern) or pattern in m:
                return True
        return False

    def entry_matches_priority(self, entry: Dict) -> bool:
        """Match priority patterns against model and firmware title/label text."""
        if self.model_matches_priority(entry.get('model', '')):
            return True
        text = f"{entry.get('label', '')} {entry.get('model', '')}".upper()
        for pattern in self._priority_patterns:
            if len(pattern) >= 8 and pattern in text:
                return True
        return False

    def sort_catalog_by_priority(self, catalog: List[Dict]) -> List[Dict]:
        """Put priority model firmware first (newest date first within each group)."""
        if not self._priority_patterns:
            return catalog
        priority_rows: List[Dict] = []
        other_rows: List[Dict] = []
        for entry in catalog:
            if self.entry_matches_priority(entry):
                priority_rows.append(entry)
            else:
                other_rows.append(entry)
        by_date = lambda rows: sorted(
            rows, key=lambda e: e.get('date') or '0000-00-00', reverse=True
        )
        logger.info(
            f'[PRIORITY] {len(priority_rows)} catalog row(s) matched; '
            f'{len(other_rows)} deferred'
        )
        if self._priority_patterns and not priority_rows:
            logger.warning(
                '[PRIORITY] no catalog rows matched — check model names '
                f'(patterns: {", ".join(self._priority_patterns)})'
            )
        return by_date(priority_rows) + by_date(other_rows)

    def clear_priority_models_file(self) -> None:
        """Clear one-shot priority file after a successful priority run."""
        if not os.path.exists(PRIORITY_MODELS_FILE):
            return
        save_json(PRIORITY_MODELS_FILE, {'models': [], 'one_shot': False})
        self._priority_patterns = []
        logger.info(f'[PRIORITY] cleared {PRIORITY_MODELS_FILE} (one-shot done)')

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
        if 'DS-2CD' in model or 'DS-2DE' in model or 'IDS-2CD' in model:
            return 'IPC_G0'
        elif 'DS-76' in model or 'DS-77' in model:
            return 'NVR_G0'
        return 'UNKNOWN'

    @staticmethod
    def _canonical_firmware_key(model: str, hw_version: str, version: str) -> str:
        return f"{model}_{hw_version}_{version}"

    def _metadata_from_catalog_label(self, label: str, model: str) -> tuple:
        """Derive applied_to text and supported_models from a catalog firmware title."""
        label = (label or '').strip()
        model = (model or '').strip().upper()
        applied_to = extract_applied_to(label)
        if not applied_to and re.search(r'Applied\s+to\s*:', label, re.IGNORECASE):
            applied_to = ' '.join(label.split())
        models = extract_models(f'{label} {applied_to}')
        if model and model != 'UNKNOWN':
            if model not in [m.upper() for m in models]:
                models.insert(0, model)
        elif models:
            model = models[0]
        if not models and model and model != 'UNKNOWN':
            models = [model]
        return applied_to, models, model

    def _migrate_firmware_entry(self, old_key: str, new_key: str, fw_data: Dict) -> None:
        """Move or merge a firmware entry when canonical model/hw/version key changes."""
        if old_key == new_key:
            return
        if new_key in self.firmwares_live:
            existing = self.firmwares_live[new_key]
            for field in (
                'applied_to', 'notes', 'changes', 'date', 'download_url', 'filename',
            ):
                new_val = (fw_data.get(field) or '').strip()
                if new_val and not (existing.get(field) or '').strip():
                    existing[field] = fw_data[field]
            merged_models: List[str] = []
            seen: set = set()
            for m in list(existing.get('supported_models') or []) + list(
                fw_data.get('supported_models') or []
            ):
                mm = str(m).strip().upper()
                if mm and mm != 'UNKNOWN' and mm not in seen:
                    seen.add(mm)
                    merged_models.append(mm)
            if merged_models:
                existing['supported_models'] = merged_models
        else:
            self.firmwares_live[new_key] = fw_data
        if old_key in self.firmwares_live:
            del self.firmwares_live[old_key]

    def heal_firmware_metadata(self) -> None:
        """Backfill model, hardware version, applied_to, and supported_models on existing JSON."""
        healed_records = 0
        migrated_keys = 0

        for old_key in list(self.firmwares_live.keys()):
            if old_key not in self.firmwares_live:
                continue
            fw = self.firmwares_live[old_key]
            changed = False

            model = (fw.get('model') or '').strip().upper()
            hw_version = (fw.get('hardware_version') or 'UNKNOWN').strip().upper()
            version = (fw.get('version') or '').strip()
            applied_to = (fw.get('applied_to') or '').strip()
            text_blob = ' '.join(
                x for x in (
                    applied_to,
                    fw.get('notes', ''),
                    fw.get('changes', ''),
                    fw.get('filename', ''),
                    old_key,
                ) if x
            )

            if not model or model == 'UNKNOWN':
                key_model = re.match(
                    r'^(DS-[0-9A-Z-]+|AE-[0-9A-Z-]+|IDS-[0-9A-Z-]+)_',
                    old_key,
                    re.IGNORECASE,
                )
                candidates: List[str] = []
                if key_model:
                    candidates.append(key_model.group(1).upper())
                candidates.extend(
                    str(m).strip().upper()
                    for m in (fw.get('supported_models') or [])
                    if str(m).strip().upper() not in ('', 'UNKNOWN')
                )
                candidates.extend(extract_models(applied_to))
                candidates.extend(extract_models(text_blob))
                filename_model = self.extract_model(fw.get('filename', '') or '')
                if filename_model:
                    candidates.append(filename_model)
                for candidate in candidates:
                    if candidate and candidate != 'UNKNOWN':
                        model = candidate
                        fw['model'] = model
                        changed = True
                        break

            if not applied_to:
                supported = [
                    str(m).strip()
                    for m in (fw.get('supported_models') or [])
                    if str(m).strip().upper() not in ('', 'UNKNOWN')
                ]
                if supported:
                    if len(supported) == 1:
                        fw['applied_to'] = f'Applied to: {supported[0]}'
                    else:
                        fw['applied_to'] = 'Applied to: ' + ', '.join(supported[:8])
                        if len(supported) > 8:
                            fw['applied_to'] += f', and {len(supported) - 8} more'
                    applied_to = fw['applied_to']
                    changed = True

            merged_models: List[str] = []
            seen_models: set = set()
            for m in list(fw.get('supported_models') or []) + extract_models(
                f'{applied_to} {text_blob}'
            ):
                mm = str(m).strip().upper()
                if mm and mm != 'UNKNOWN' and mm not in seen_models:
                    seen_models.add(mm)
                    merged_models.append(mm)
            if model and model != 'UNKNOWN' and model not in seen_models:
                merged_models.insert(0, model)
            if merged_models and merged_models != fw.get('supported_models'):
                fw['supported_models'] = merged_models
                changed = True

            if hw_version == 'UNKNOWN' and model and model != 'UNKNOWN':
                key_hw = re.match(
                    rf'^{re.escape(model)}_([^_]+)_{re.escape(version)}$',
                    old_key,
                    re.IGNORECASE,
                )
                if key_hw and key_hw.group(1).upper() != 'UNKNOWN':
                    hw_version = key_hw.group(1).upper()
                else:
                    hw_version = self.extract_hardware_version(text_blob, model)
                if hw_version != 'UNKNOWN':
                    fw['hardware_version'] = hw_version
                    changed = True

            if model and model != 'UNKNOWN' and version:
                new_key = self._canonical_firmware_key(
                    model, fw.get('hardware_version', 'UNKNOWN'), version
                )
                if new_key != old_key:
                    self._migrate_firmware_entry(old_key, new_key, fw)
                    migrated_keys += 1
                    changed = True

            if changed:
                healed_records += 1

        if healed_records > 0 or migrated_keys > 0:
            logger.info(
                f'  🩹 Healed {healed_records} firmware record(s), '
                f'migrated {migrated_keys} key(s)'
            )

    def dismiss_page_overlays(self, page) -> int:
        """Dismiss cookie banners, region prompts, and other blocking overlays."""
        dismissed = 0

        # Hikvision GDPR cookie bar (a.gdpr-button-accept) + OneTrust fallback
        try:
            page.wait_for_selector(
                'a.gdpr-button-accept, #onetrust-accept-btn-handler, .gdpr-info-wrapper',
                state='visible',
                timeout=8000,
            )
        except Exception:
            pass
        for sel in (
            'a.gdpr-button-accept',
            '#onetrust-accept-btn-handler',
            '.gdpr-button-wrapper a:has-text("Accept All")',
        ):
            try:
                btn = page.locator(sel).first
                if btn.count() > 0 and btn.is_visible():
                    btn.click(timeout=5000, force=True)
                    dismissed += 1
                    logger.info('  → Clicked cookie consent: Accept All')
                    time.sleep(0.6)
                    break
            except Exception:
                pass

        accept_labels = ['Accept All', 'Accept all', 'I Agree', 'Got it']
        for label in accept_labels:
            try:
                btn = page.get_by_role('button', name=label, exact=False)
                if btn.count() > 0 and btn.first.is_visible():
                    btn.first.click(timeout=3000, force=True)
                    dismissed += 1
                    logger.info(f'  → Clicked overlay button: {label}')
                    time.sleep(0.4)
            except Exception:
                pass

        # Region redirect (.ip-wrap — "visit Australia & New Zealand")
        try:
            region_close = page.locator('.ip-wrap span.cha, .ip-box span.cha').first
            if region_close.count() > 0 and region_close.is_visible():
                region_close.click(timeout=3000, force=True)
                dismissed += 1
                logger.info('  → Closed region redirect overlay')
                time.sleep(0.4)
        except Exception:
            pass

        close_selectors = [
            '[aria-label="Close"]',
            '[aria-label="close"]',
            'button.close',
            '.modal-close',
            '.close-btn',
        ]
        for sel in close_selectors:
            try:
                for btn in page.query_selector_all(sel):
                    if btn.is_visible():
                        btn.click(timeout=2000, force=True)
                        dismissed += 1
                        time.sleep(0.3)
            except Exception:
                pass

        try:
            page.keyboard.press('Escape')
        except Exception:
            pass
        return dismissed

    def cookie_banner_visible(self, page) -> bool:
        """True if Hikvision GDPR / OneTrust cookie UI is still on screen."""
        for sel in (
            'a.gdpr-button-accept',
            '.gdpr-info-wrapper',
            '#onetrust-banner-sdk',
            '#onetrust-accept-btn-handler',
        ):
            try:
                loc = page.locator(sel).first
                if loc.count() > 0 and loc.is_visible():
                    return True
            except Exception:
                pass
        try:
            return page.locator('text=Accept All').first.is_visible()
        except Exception:
            return False

    def region_popup_visible(self, page) -> bool:
        """True if geo redirect banner (.ip-wrap) is still on screen."""
        try:
            loc = page.locator('.ip-wrap .ip-box').first
            return loc.count() > 0 and loc.is_visible()
        except Exception:
            return False

    def find_materials_license_download_link(self, page):
        """Materials License modal: red Agree is <a class="agree a-download-href"> with the .zip URL."""
        try:
            link = page.locator(
                'a.agree.a-download-href[href*=".zip"], '
                'a.agree.a-download-href[href*=".dav"], '
                'a.agree.a-download-href[href*=".pak"], '
                'a.agree.a-download-href[href*=".bin"]'
            ).first
            if link.count() > 0 and link.is_visible():
                return link
        except Exception:
            pass
        return None

    def dismiss_download_interstitials(self, page) -> int:
        """Close blocking popups before download (eBay Notice). Does not click Agree — use expect_download."""
        dismissed = 0
        for _ in range(3):
            acted = False

            # Hikvision "Notice" / eBay market statement — close with X (don't use Read more)
            try:
                notice_dlg = page.locator('[role="dialog"], dialog, .modal, section').filter(
                    has_text=re.compile(r'eBay online market|HIKVISION eBay', re.I)
                )
                if notice_dlg.count() == 0:
                    notice_dlg = page.locator('[role="dialog"], dialog').filter(
                        has=page.locator('text=Notice')
                    )
                if notice_dlg.count() > 0 and notice_dlg.first.is_visible():
                    box = notice_dlg.first
                    for sel in (
                        'button.close',
                        '[aria-label="Close"]',
                        '.close',
                        'span.cha',
                        'button:has-text("×")',
                    ):
                        close_btn = box.locator(sel).first
                        if close_btn.count() > 0 and close_btn.is_visible():
                            close_btn.click(timeout=3000, force=True)
                            dismissed += 1
                            acted = True
                            logger.info('  → Closed Notice / eBay statement popup')
                            time.sleep(0.8)
                            break
                    if not acted:
                        try:
                            page.keyboard.press('Escape')
                            dismissed += 1
                            acted = True
                            logger.info('  → Closed Notice popup (Escape)')
                            time.sleep(0.5)
                        except Exception:
                            pass
            except Exception:
                pass

            if not acted:
                break
        return dismissed

    def find_firmware_download_modal(self, page):
        """Return dialog element that contains a firmware file link, or None."""
        for modal in page.query_selector_all('[role="dialog"], dialog'):
            try:
                if not modal.is_visible():
                    continue
                for link in modal.query_selector_all('a[href]'):
                    href = (link.get_attribute('href') or '').lower()
                    if any(ext in href for ext in ['.dav', '.zip', '.pak', '.bin']):
                        return modal
            except Exception:
                continue
        return None

    def close_firmware_modal(self, page) -> None:
        """Close license-agreement modal if open."""
        close_btn = page.query_selector(
            'dialog button, [role="dialog"] button, '
            'dialog [aria-label*="close" i], [role="dialog"] [aria-label*="close" i]'
        )
        if close_btn:
            close_btn.click()
            time.sleep(0.4)

    def _find_live_firmware_key(
        self, model: str, hw_version: str, version: str
    ) -> Optional[str]:
        """Find firmwares_live key; match model+version even if HW differs (e.g. UNKNOWN vs IPC_G0)."""
        if not model or not version:
            return None
        model = model.strip().upper()
        hw_version = (hw_version or 'UNKNOWN').strip().upper()
        version = version.strip()
        exact = f'{model}_{hw_version}_{version}'
        if exact in self.firmwares_live:
            return exact
        prefix = f'{model}_'
        suffix = f'_{version}'
        for key in self.firmwares_live:
            if key.startswith(prefix) and key.endswith(suffix):
                return key
        return None

    def firmware_is_archived(
        self,
        normalized_model: str,
        hw_version: str,
        version: str,
        downloaded_in_this_run: set,
    ) -> bool:
        if not version:
            return False
        firmware_key = f"{normalized_model}_{hw_version}_{version}"
        return (
            self._find_live_firmware_key(normalized_model, hw_version, version) is not None
            or firmware_key in downloaded_in_this_run
        )

    def firmware_file_in_archive(self, filename: str) -> bool:
        """True if any archived entry already uses this release filename."""
        if not filename:
            return False
        return any(
            (fw.get('filename') or '') == filename
            for fw in self.firmwares_live.values()
        )

    def append_existing_firmware_record(
        self,
        firmwares: List[Dict],
        *,
        normalized_model: str,
        hw_version: str,
        version: str,
        supported_models: List[str],
        applied_to_text: str,
        release_notes_url: str,
    ) -> None:
        firmwares.append({
            'model': normalized_model,
            'hardware_version': hw_version,
            'version': version,
            'download_url': '',
            'local_file_path': '',
            'filename': '',
            'supported_models': supported_models,
            'applied_to': applied_to_text,
            'date': '',
            'changes': '',
            'notes': release_notes_url,
            'source': 'live',
            'already_exists': True,
        })

    @staticmethod
    def _date_from_text(text: str) -> str:
        """Extract YYYY-MM-DD from firmware filename or label (YYMMDD in names)."""
        for date_code in re.findall(r'(\d{6}|\d{8})', text):
            if len(date_code) == 6:
                year = int('20' + date_code[:2])
                month = int(date_code[2:4])
                day = int(date_code[4:6])
            else:
                year = int(date_code[:4])
                month = int(date_code[4:6])
                day = int(date_code[6:8])
            if 2000 <= year <= 2100 and 1 <= month <= 12 and 1 <= day <= 31:
                return f"{year:04d}-{month:02d}-{day:02d}"
        return ''

    @staticmethod
    def catalog_html_looks_valid(html: str) -> bool:
        """True if SSR catalog markup is present (not a block/captcha page)."""
        if not html:
            return False
        has_panel = 'firmware-collapse-' in html
        has_downloads = 'data-href="https://assets.hikvision.com' in html
        return has_panel and has_downloads and len(html) > 200_000

    def fetch_catalog_html_http(self) -> Optional[str]:
        if not REQUESTS_AVAILABLE:
            return None
        session = requests.Session()
        last_size = 0
        for attempt in range(1, 4):
            logger.info(f'  → Fetching firmware catalog page (HTTP, attempt {attempt}/3)...')
            t0 = time.time()
            try:
                session.headers.update(HTTP_HEADERS)
                session.get(f'{BASE_URL}/en/', timeout=60)
                time.sleep(0.5)
                session.headers['Referer'] = f'{BASE_URL}/en/'
                session.headers['Sec-Fetch-Site'] = 'same-origin'
                response = session.get(FIRMWARE_URL, timeout=120)
                response.raise_for_status()
                html = response.text
                last_size = len(response.content)
                size_mb = last_size / (1024 * 1024)
                logger.info(f'  ✓ Downloaded {size_mb:.1f} MB in {time.time() - t0:.1f}s')
                if self.catalog_html_looks_valid(html):
                    return html
                logger.warning(
                    f'  ⚠ HTTP page missing catalog markup ({last_size:,} bytes) — retrying'
                )
            except Exception as err:
                logger.warning(f'  ⚠ HTTP fetch attempt {attempt} failed: {err}')
            if attempt < 3:
                time.sleep(5 * attempt)
        logger.warning(
            f'  ⚠ HTTP catalog fetch failed after 3 attempts (last size {last_size:,} bytes)'
        )
        return None

    def fetch_catalog_html_playwright(self) -> str:
        """Load full SSR catalog via browser context (GitHub Actions / blocked HTTP)."""
        if not PLAYWRIGHT_AVAILABLE:
            raise RuntimeError(
                'Catalog page blocked over HTTP and Playwright is not installed. '
                'pip install playwright && playwright install chromium'
            )
        logger.info('  → Fetching firmware catalog (Playwright API request)...')
        t0 = time.time()
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            try:
                context = browser.new_context(user_agent=HTTP_USER_AGENT)
                page = context.new_page()
                page.goto(f'{BASE_URL}/en/', wait_until='domcontentloaded', timeout=60_000)
                page.wait_for_timeout(800)
                page.goto(FIRMWARE_URL, wait_until='domcontentloaded', timeout=120_000)
                page.wait_for_timeout(1500)
                self.dismiss_page_overlays(page)
                page.wait_for_timeout(500)

                # Full ~13MB SSR HTML (page.content() is only partial DOM).
                req_headers = {**HTTP_HEADERS, 'Referer': FIRMWARE_URL}
                response = context.request.get(
                    FIRMWARE_URL,
                    headers=req_headers,
                    timeout=120_000,
                )
                html = response.text() if response.ok else ''
                if self.catalog_html_looks_valid(html):
                    logger.info(
                        f'  ✓ Playwright API catalog ({len(html) / (1024 * 1024):.1f} MB) '
                        f'in {time.time() - t0:.1f}s'
                    )
                    return html

                logger.warning(
                    f'  ⚠ Playwright API response invalid ({len(html):,} bytes, '
                    f'status {response.status}) — trying rendered DOM'
                )
                html = page.content()
            finally:
                browser.close()
        if not self.catalog_html_looks_valid(html):
            raise RuntimeError(
                f'Playwright catalog still invalid ({len(html):,} bytes) — may be blocked'
            )
        logger.info(
            f'  ✓ Playwright DOM catalog ({len(html) / (1024 * 1024):.1f} MB) '
            f'in {time.time() - t0:.1f}s'
        )
        return html

    def fetch_catalog_html(self) -> str:
        # GitHub datacenter IPs are often blocked by requests; prefer Playwright there.
        on_ci = os.environ.get('GITHUB_ACTIONS', '').lower() == 'true'
        if on_ci and PLAYWRIGHT_AVAILABLE:
            try:
                self._catalog_fetch_method = 'playwright'
                return self.fetch_catalog_html_playwright()
            except Exception as err:
                logger.warning(f'  ⚠ Playwright catalog fetch failed on CI: {err}')

        html = self.fetch_catalog_html_http()
        if html:
            self._catalog_fetch_method = 'http'
            return html
        if PLAYWRIGHT_AVAILABLE:
            self._catalog_fetch_method = 'playwright'
            return self.fetch_catalog_html_playwright()
        raise RuntimeError(
            'Firmware catalog blocked over HTTP (common on GitHub Actions). '
            'Install Playwright in CI or set USE_PLAYWRIGHT=1 for a browser fallback.'
        )

    def parse_catalog_entries(self, html: str) -> List[Dict]:
        """Parse model + firmware URLs from SSR HTML (data-href on agreement links)."""
        logger.info('  → Parsing catalog from HTML...')
        t0 = time.time()

        model_by_id: Dict[str, str] = {}
        for match in re.finditer(r'data-target="(#firmware-collapse-\d+)"', html):
            tid = match.group(1)
            chunk = html[match.end():match.end() + 800]
            model_match = re.search(
                r'(DS-[0-9A-Z-]+|AE-[0-9A-Z-]+|IDS-[0-9A-Z-]+)',
                chunk,
                re.I,
            )
            if model_match:
                model_by_id[tid] = normalize_model_name(model_match.group(1)).upper()

        entries: List[Dict] = []
        parts = re.split(r'(firmware-collapse-\d+)', html)
        for i in range(1, len(parts), 2):
            panel_id = parts[i]
            chunk = parts[i + 1] if i + 1 < len(parts) else ''
            model = model_by_id.get(f'#{panel_id}', 'UNKNOWN')
            if model == 'UNKNOWN':
                inferred = self.extract_model(chunk)
                if inferred:
                    model = inferred
            hw_version = self.extract_hardware_version(chunk, model)

            for title, url in re.findall(
                r'data-title="([^"]*)".*?data-href="(https://assets\.hikvision\.com[^"]+\.(?:zip|dav|pak|bin))"',
                chunk,
                re.DOTALL | re.I,
            ):
                entry_model = model
                title_models = extract_models(title)
                if entry_model == 'UNKNOWN' and title_models:
                    entry_model = title_models[0]
                elif entry_model == 'UNKNOWN':
                    title_model = self.extract_model(title)
                    if title_model:
                        entry_model = title_model
                version = self.extract_version(title + ' ' + url) or ''
                date_str = self._date_from_text(title) or self._date_from_text(url)
                notes = ''
                pdf = re.search(
                    r'href="(https://assets\.hikvision\.com[^"]+\.pdf[^"]*)"',
                    chunk,
                    re.I,
                )
                if pdf:
                    notes = pdf.group(1)
                entries.append({
                    'model': entry_model,
                    'hardware_version': hw_version,
                    'version': version,
                    'url': url,
                    'label': title,
                    'date': date_str,
                    'notes': notes,
                })

        if len(entries) < 100:
            logger.warning('  Panel parse weak — using global data-href scan')
            entries = []
            for title, url in re.findall(
                r'data-title="([^"]*)".*?data-href="(https://assets\.hikvision\.com[^"]+\.(?:zip|dav|pak|bin))"',
                html,
                re.DOTALL | re.I,
            ):
                version = self.extract_version(title + ' ' + url) or ''
                title_models = extract_models(title)
                fallback_model = title_models[0] if title_models else (
                    self.extract_model(title) or 'UNKNOWN'
                )
                entries.append({
                    'model': fallback_model,
                    'hardware_version': 'UNKNOWN',
                    'version': version,
                    'url': url,
                    'label': title,
                    'date': self._date_from_text(title) or self._date_from_text(url),
                    'notes': '',
                })

        entries.sort(key=lambda e: e.get('date') or '0000-00-00', reverse=True)
        logger.info(f'  ✓ Parsed {len(entries)} firmware URL(s) in {time.time() - t0:.1f}s')
        return entries

    def download_firmware_http(self, url: str, filename: str) -> Path:
        firmware_dir = Path('firmwares')
        firmware_dir.mkdir(exist_ok=True)
        path = firmware_dir / filename
        logger.info(f'    ↓ Downloading {filename}...')
        t0 = time.time()
        with requests.get(url, headers=HTTP_HEADERS, stream=True, timeout=600) as response:
            response.raise_for_status()
            content_type = (response.headers.get('content-type') or '').lower()
            if 'html' in content_type:
                raise RuntimeError('CDN returned HTML (check Referer)')
            total = 0
            with open(path, 'wb') as handle:
                for chunk in response.iter_content(chunk_size=1024 * 256):
                    if chunk:
                        handle.write(chunk)
                        total += len(chunk)
        if total < 10_000:
            path.unlink(missing_ok=True)
            raise RuntimeError(f'Download too small ({total} bytes)')
        logger.info(
            f'    ✓ Saved {path.name} ({total:,} bytes) in {time.time() - t0:.1f}s'
        )
        return path

    def scrape_via_http(self) -> List[Dict]:
        """Scrape via one HTTP GET + HTML parse (no Playwright)."""
        html = self.fetch_catalog_html()
        catalog = self.parse_catalog_entries(html)
        catalog = self.sort_catalog_by_priority(catalog)
        self._catalog_entry_count = len(catalog)
        if len(catalog) < 1000:
            logger.warning(
                f'  ⚠ Catalog only has {len(catalog)} entries — page may be incomplete'
            )

        firmwares: List[Dict] = []
        new_downloads_count = 0
        skipped_existing_count = 0
        priority_new_downloads = 0
        priority_skipped_archived = 0
        downloaded_in_this_run: set = set()
        downloaded_filenames_this_run: set = set()

        priority_row_count = (
            sum(1 for e in catalog if self.entry_matches_priority(e))
            if self._priority_patterns else 0
        )
        if self._priority_patterns:
            logger.info(
                f'  → Priority-first downloads: {priority_row_count} priority row(s) '
                f'first, then rest of catalog (max {MAX_FIRMWARES_TO_DOWNLOAD} new files)'
            )
        else:
            logger.info('  → Downloading new firmware(s) (newest first)...')

        for entry in catalog:
            is_priority_row = bool(
                self._priority_patterns and self.entry_matches_priority(entry)
            )
            if MAX_FIRMWARES_TO_DOWNLOAD > 0 and new_downloads_count >= MAX_FIRMWARES_TO_DOWNLOAD:
                logger.info(
                    f'  ⏹️  Download limit reached ({MAX_FIRMWARES_TO_DOWNLOAD})'
                )
                break

            model = entry['model']
            hw_version = entry['hardware_version']
            version = entry['version']
            url = entry['url']

            if not version:
                continue
            firmware_key = f"{model}_{hw_version}_{version}"
            filename = url.split('/')[-1].split('?')[0]

            if self.firmware_is_archived(model, hw_version, version, downloaded_in_this_run):
                skipped_existing_count += 1
                if is_priority_row:
                    priority_skipped_archived += 1
                if firmware_key not in downloaded_in_this_run:
                    logger.info(
                        f'    ⊘ Skipping existing: {model} {hw_version} v{version} '
                        f'({skipped_existing_count} skipped)'
                    )
                applied_to, supported_models, resolved_model = self._metadata_from_catalog_label(
                    entry.get('label', ''), model
                )
                if resolved_model and resolved_model != 'UNKNOWN':
                    model = resolved_model
                if hw_version == 'UNKNOWN' and model != 'UNKNOWN':
                    hw_version = self.extract_hardware_version(
                        f"{applied_to} {entry.get('label', '')}", model
                    )
                self.append_existing_firmware_record(
                    firmwares,
                    normalized_model=model,
                    hw_version=hw_version,
                    version=version,
                    supported_models=supported_models,
                    applied_to_text=applied_to,
                    release_notes_url=entry.get('notes', ''),
                )
                continue

            local_file_path = ''
            stored_filename = ''
            file_already_fetched = (
                filename in downloaded_filenames_this_run
                or self.firmware_file_in_archive(filename)
            )
            filepath = Path('firmwares') / filename

            if file_already_fetched and filepath.exists():
                logger.info(
                    f'    ⊘ Reusing firmware file {filename} for {model} v{version}'
                )
                local_file_path = str(filepath)
                stored_filename = filename
                downloaded_in_this_run.add(firmware_key)
            else:
                try:
                    filepath = self.download_firmware_http(url, filename)
                    local_file_path = str(filepath)
                    stored_filename = filename
                    downloaded_filenames_this_run.add(filename)
                    downloaded_in_this_run.add(firmware_key)
                    new_downloads_count += 1
                    if is_priority_row:
                        priority_new_downloads += 1
                    logger.info(f'    ✓ NEW firmware #{new_downloads_count}')
                except Exception as err:
                    logger.warning(f'    ⚠ Download failed for {model} v{version}: {err}')
                    self.errors.append(f'Download failed {model} v{version}: {err}')
                    continue

            applied_to, supported_models, resolved_model = self._metadata_from_catalog_label(
                entry.get('label', ''), model
            )
            if resolved_model and resolved_model != 'UNKNOWN':
                model = resolved_model
            if hw_version == 'UNKNOWN' and model != 'UNKNOWN':
                hw_version = self.extract_hardware_version(
                    f"{applied_to} {entry.get('label', '')}", model
                )

            firmwares.append({
                'model': model,
                'hardware_version': hw_version,
                'version': version,
                'download_url': '',
                'local_file_path': local_file_path,
                'filename': stored_filename,
                'supported_models': supported_models,
                'applied_to': applied_to,
                'date': format_date(entry.get('date', '')),
                'changes': '',
                'notes': entry.get('notes', ''),
                'source': 'live',
            })

        logger.info('=' * 60)
        logger.info('📊 HTTP Download Summary:')
        logger.info(f'  • Catalog entries: {len(catalog)}')
        logger.info(f'  • Already existing (skipped): {skipped_existing_count}')
        logger.info(f'  • New downloads this run: {new_downloads_count}')
        if new_downloads_count == 0:
            logger.info('  ✓ No new firmwares — archive caught up for scanned items')
        if self._priority_patterns:
            logger.info(
                f'[PRIORITY] summary: {priority_new_downloads} new from priority rows, '
                f'{priority_skipped_archived} priority already archived, '
                f'{priority_row_count} priority row(s) in catalog; '
                f'{new_downloads_count} total new downloads (limit {MAX_FIRMWARES_TO_DOWNLOAD})'
            )
        logger.info('=' * 60)
        return firmwares

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
        consecutive_fully_skipped_models = 0
        browser = None
        
        try:
            with sync_playwright() as p:
                logger.info("  → Launching browser...")
                browser = p.chromium.launch(headless=True)
                context = browser.new_context(
                    locale='en-NZ',
                    timezone_id='Pacific/Auckland',
                    user_agent=(
                        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) '
                        'AppleWebKit/537.36 (KHTML, like Gecko) '
                        'Chrome/120.0.0.0 Safari/537.36'
                    ),
                )
                page = context.new_page()
                
                logger.info("Loading firmware page...")
                page.goto(FIRMWARE_URL, wait_until='networkidle', timeout=60000)
                time.sleep(5)
                overlay_count = self.dismiss_page_overlays(page)
                time.sleep(1)
                overlay_count += self.dismiss_page_overlays(page)
                if overlay_count:
                    logger.info(f"  → Dismissed {overlay_count} overlay(s) on load")
                
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
                        overlay_count = self.dismiss_page_overlays(page)
                        if overlay_count:
                            logger.info(f"  → Dismissed {overlay_count} overlay(s) after search")
                        search_input = page.query_selector('input.firmware-search') or search_input
                        
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
                        
                        # Flag to break out of nested loops (download limit or caught-up early exit)
                        test_mode_limit_reached = False
                        stop_reason = ''
                        
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
                                    if i % 15 == 1:
                                        self.dismiss_page_overlays(page)
                                        self.dismiss_download_interstitials(page)

                                    logger.info(f"    Processing item {i}...")
                                    model_text = title_element.inner_text().strip()
                                    logger.info(f"    Model text extracted: {model_text[:50]}...")
                                    model = self.extract_model(model_text)
                                    logger.info(f"    Extracted model: {model}")

                                    model_firmware_links = 0
                                    model_skipped_existing = 0
                                    model_got_new_download = False
                                    
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
                                                        stop_reason = 'download_limit'
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
                                                        
                                                        # Extract release notes PDF URL from collapse content
                                                        release_notes_url = extract_release_notes_url(collapse_content)
                                                        
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
                                                            model_firmware_links += 1
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
                                                                    model_firmware_links += 1
                                                                    model_skipped_existing += 1
                                                                    self.append_existing_firmware_record(
                                                                        firmwares,
                                                                        normalized_model=normalized_model,
                                                                        hw_version=hw_version,
                                                                        version=version,
                                                                        supported_models=supported_models,
                                                                        applied_to_text=applied_to_text,
                                                                        release_notes_url=release_notes_url,
                                                                    )
                                                                    continue
                                                                
                                                                # Check download limit for NEW firmwares (direct links)
                                                                if MAX_FIRMWARES_TO_DOWNLOAD > 0 and new_downloads_count >= MAX_FIRMWARES_TO_DOWNLOAD:
                                                                    logger.info(f"  ⏹️  Download limit reached: Downloaded {new_downloads_count} NEW firmware(s) (limit: {MAX_FIRMWARES_TO_DOWNLOAD}), stopping...")
                                                                    test_mode_limit_reached = True
                                                                    stop_reason = 'download_limit'
                                                                    break

                                                                # TODO: Direct links could be downloaded here, but currently only modal links are downloaded
                                                                # For now, just skip direct links (they'll be processed via modal if available)
                                                                logger.debug(f"    Found direct link but skipping download (modal links preferred): {normalized_model} {hw_version} v{version}")
                                                                continue
                                                        # License agreement link (needs to be clicked to get actual URL)
                                                        elif href == '#download-agreement' or 'download-agreement' in href.lower():
                                                            is_firmware_link = True
                                                            model_firmware_links += 1
                                                            logger.info(f"    Found license agreement link: {link_text[:50]}...")

                                                            # Skip modal when version already archived (newest-first still walks older links)
                                                            if version and self.firmware_is_archived(
                                                                normalized_model, hw_version, version, downloaded_in_this_run
                                                            ):
                                                                if f"{normalized_model}_{hw_version}_{version}" in downloaded_in_this_run:
                                                                    logger.info(
                                                                        f"    ⊘ Skipping duplicate firmware (already downloaded this run): "
                                                                        f"{normalized_model} {hw_version} v{version}"
                                                                    )
                                                                else:
                                                                    skipped_existing_count += 1
                                                                    model_skipped_existing += 1
                                                                    logger.info(
                                                                        f"    ⊘ Skipping existing firmware (no modal): "
                                                                        f"{normalized_model} {hw_version} v{version} ({skipped_existing_count} skipped)"
                                                                    )
                                                                self.append_existing_firmware_record(
                                                                    firmwares,
                                                                    normalized_model=normalized_model,
                                                                    hw_version=hw_version,
                                                                    version=version,
                                                                    supported_models=supported_models,
                                                                    applied_to_text=applied_to_text,
                                                                    release_notes_url=release_notes_url,
                                                                )
                                                                continue
                                                            
                                                            # Click to open modal
                                                            try:
                                                                # Use JavaScript click to avoid timeout issues
                                                                logger.info(f"    Clicking license agreement link...")
                                                                page.evaluate('(element) => { element.click(); }', link)
                                                                time.sleep(2)
                                                                self.dismiss_download_interstitials(page)
                                                                time.sleep(0.5)

                                                                agree_link = self.find_materials_license_download_link(page)
                                                                if agree_link:
                                                                    actual_download_url = agree_link.get_attribute('href') or ''
                                                                    logger.info(
                                                                        '    ✓ Materials License Agreement — '
                                                                        'download via Agree link'
                                                                    )
                                                                    logger.info(f"      URL: {actual_download_url[:100]}...")
                                                                else:
                                                                    modal = self.find_firmware_download_modal(page)
                                                                    if not modal:
                                                                        logger.warning(
                                                                            f"    ⚠ Could not find download link after agreement "
                                                                            f"(license/notice popup may be blocking)"
                                                                        )
                                                                        self.close_firmware_modal(page)
                                                                        continue

                                                                    logger.info(f"    ✓ Download modal found")
                                                                    agree_link = None
                                                                    all_modal_links = modal.query_selector_all('a[href]')
                                                                    logger.info(
                                                                        f"    Checking {len(all_modal_links)} links in modal..."
                                                                    )
                                                                    for modal_link in all_modal_links:
                                                                        modal_href = modal_link.get_attribute('href') or ''
                                                                        modal_text = modal_link.inner_text().strip()
                                                                        if any(
                                                                            ext in modal_href.lower()
                                                                            for ext in ['.dav', '.zip', '.pak', '.bin']
                                                                        ):
                                                                            agree_link = modal_link
                                                                            actual_download_url = modal_href
                                                                            logger.info(
                                                                                f"    ✓ Found download link: {modal_text[:50]}..."
                                                                            )
                                                                            logger.info(
                                                                                f"      URL: {modal_href[:100]}..."
                                                                            )
                                                                            break

                                                                if agree_link:
                                                                    if not actual_download_url:
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
                                                                                model_skipped_existing += 1
                                                                                logger.info(f"    ⊘ Skipping existing firmware: {normalized_model} {hw_version} v{version} ({skipped_existing_count} skipped)")
                                                                            self.close_firmware_modal(page)
                                                                            self.append_existing_firmware_record(
                                                                                firmwares,
                                                                                normalized_model=normalized_model,
                                                                                hw_version=hw_version,
                                                                                version=version,
                                                                                supported_models=supported_models,
                                                                                applied_to_text=applied_to_text,
                                                                                release_notes_url=release_notes_url,
                                                                            )
                                                                            continue
                                                                    
                                                                    # Check download limit for NEW firmwares
                                                                    if MAX_FIRMWARES_TO_DOWNLOAD > 0 and new_downloads_count >= MAX_FIRMWARES_TO_DOWNLOAD:
                                                                        logger.info(f"  ⏹️  Download limit reached: Downloaded {new_downloads_count} NEW firmware(s) (limit: {MAX_FIRMWARES_TO_DOWNLOAD}), stopping...")
                                                                        # Close modal
                                                                        close_btn = page.query_selector('dialog button, [role="dialog"] button')
                                                                        if close_btn:
                                                                            close_btn.click()
                                                                        test_mode_limit_reached = True
                                                                        stop_reason = 'download_limit'
                                                                        break

                                                                    logger.info(f"    Starting download...")
                                                                    self.dismiss_page_overlays(page)
                                                                    self.dismiss_download_interstitials(page)

                                                                    # Click the link to trigger download (with browser context)
                                                                    try:
                                                                        # Wait for download and click simultaneously - this maintains browser session
                                                                        with page.expect_download(timeout=120000) as download_info:  # 2 min timeout for large files
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
                                                                            model_got_new_download = True
                                                                            consecutive_fully_skipped_models = 0
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
                                                            'notes': release_notes_url,  # Store PDF URL in notes field
                                                            'source': 'live'
                                                        })
                                                    except Exception as link_err:
                                                        logger.debug(f"    Link processing error: {link_err}")
                                                        continue

                                                # Caught-up detection: every link for this model was already archived
                                                if (
                                                    model_firmware_links > 0
                                                    and model_skipped_existing == model_firmware_links
                                                    and not model_got_new_download
                                                ):
                                                    consecutive_fully_skipped_models += 1
                                                    logger.info(
                                                        f"    ↳ Model fully archived "
                                                        f"({consecutive_fully_skipped_models}/"
                                                        f"{CONSECUTIVE_FULLY_SKIPPED_MODELS_LIMIT} consecutive)"
                                                    )
                                                    if (
                                                        new_downloads_count == 0
                                                        and consecutive_fully_skipped_models
                                                        >= CONSECUTIVE_FULLY_SKIPPED_MODELS_LIMIT
                                                    ):
                                                        logger.info(
                                                            f"  ⏹️  Caught up: {consecutive_fully_skipped_models} models in a row "
                                                            f"fully archived with no new downloads — stopping early"
                                                        )
                                                        test_mode_limit_reached = True
                                                        stop_reason = 'caught_up'
                                                elif model_firmware_links > 0:
                                                    consecutive_fully_skipped_models = 0
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
                            if stop_reason == 'caught_up':
                                logger.info(
                                    "  ⏹️  Stopped early — archive appears caught up for scanned models"
                                )
                            else:
                                logger.info(
                                    f"  ⏹️  Stopped early after reaching download limit of "
                                    f"{MAX_FIRMWARES_TO_DOWNLOAD} firmware(s)"
                                )
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
        if new_downloads_count == 0 and consecutive_fully_skipped_models >= CONSECUTIVE_FULLY_SKIPPED_MODELS_LIMIT:
            logger.info(
                f"  ⏹️  Early exit: stopped after {consecutive_fully_skipped_models} "
                f"fully-archived models in a row"
            )
        logger.info("=" * 60)
        
        return unique_firmwares
    
    def _merge_firmware_metadata(self, existing: Dict, fw_data: Dict) -> List[str]:
        """Merge catalog/release metadata into an existing firmwares_live entry."""
        updated_fields: List[str] = []

        new_notes = (fw_data.get('notes') or '').strip()
        if new_notes and not (existing.get('notes') or '').strip():
            existing['notes'] = new_notes
            updated_fields.append('notes')

        new_applied_to = (fw_data.get('applied_to') or '').strip()
        if new_applied_to and not (existing.get('applied_to') or '').strip():
            existing['applied_to'] = new_applied_to
            updated_fields.append('applied_to')

        existing_models = existing.get('supported_models') or []
        new_models = fw_data.get('supported_models') or []
        merged_models: List[str] = []
        seen_models: set = set()
        for m in list(existing_models) + list(new_models):
            mm = str(m).strip().upper()
            if mm and mm != 'UNKNOWN' and mm not in seen_models:
                seen_models.add(mm)
                merged_models.append(mm)
        if merged_models and merged_models != existing_models:
            existing['supported_models'] = merged_models
            updated_fields.append('supported_models')

        new_date = format_date(fw_data.get('date', ''))
        if new_date and not (existing.get('date') or '').strip():
            existing['date'] = new_date
            updated_fields.append('date')

        return updated_fields

    def process_firmware(self, fw_data: Dict):
        """Process and save firmware."""
        model = fw_data.get('model', '')
        hw_version = fw_data.get('hardware_version', '')
        version = fw_data.get('version', '')
        
        if not all([model, version]):
            return
        
        local_file_path = fw_data.get('local_file_path', '')
        key = self._find_live_firmware_key(model, hw_version, version) or (
            f"{model}_{hw_version}_{version}"
        )

        # Archived firmware: refresh metadata from catalog without re-downloading
        if not local_file_path and key in self.firmwares_live:
            existing = self.firmwares_live[key]
            updated_fields = self._merge_firmware_metadata(existing, fw_data)
            if updated_fields:
                self.firmwares_live[key] = existing
                logger.info(
                    f'  ↻ Updated archived firmware metadata: {model} {hw_version} '
                    f'v{version} ({", ".join(updated_fields)})'
                )
            return

        # Don't add NEW entries if download failed (no local file)
        if not local_file_path:
            logger.debug(
                f'  ⊘ Skipping firmware without downloaded file: {model} {hw_version} v{version}'
            )
            return
        
        # Get/create device ID
        device_id = get_device_id(self.devices, model, hw_version)
        if device_id is None:
            device_id = create_device_id(self.devices, model, hw_version)
            logger.debug(f"Created device: {model} {hw_version} -> ID {device_id}")
        
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
            existing = self.firmwares_live.get(key, {})
            updated_fields = self._merge_firmware_metadata(existing, fw_data)

            if updated_fields:
                self.firmwares_live[key] = existing
                logger.info(
                    f"  ↻ Updated existing firmware metadata: {model} {hw_version} v{version} ({', '.join(updated_fields)})"
                )
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
        """Remove devices that are not referenced by any firmware entry."""
        # Get all device IDs referenced by firmwares
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
        
        # Remove devices without firmware references
        removed_count = 0
        devices_to_remove = []
        for device_id in self.devices.keys():
            if device_id not in devices_with_firmwares and device_id not in devices_with_files:
                devices_to_remove.append(device_id)
        
        for device_id in devices_to_remove:
            del self.devices[device_id]
            removed_count += 1
        
        if removed_count > 0:
            logger.info(f"  🧹 Cleaned up {removed_count} device(s) without firmwares or files")

    def repair_and_validate_entries(self):
        """Repair recoverable entries and remove irrecoverably invalid records."""
        repaired_count = 0
        removed_count = 0
        keys_to_remove = []

        # Build reverse lookup for known devices by model/hardware pair
        device_pair_to_id = {}
        for did, dinfo in self.devices.items():
            model = (dinfo.get('model') or '').strip().upper()
            hw = (dinfo.get('hardware_version') or 'UNKNOWN').strip().upper()
            if model:
                device_pair_to_id[(model, hw)] = int(did)

        for key, fw_data in self.firmwares_live.items():
            model = (fw_data.get('model') or '').strip().upper()
            hw_version = (fw_data.get('hardware_version') or 'UNKNOWN').strip().upper()
            version = (fw_data.get('version') or '').strip()
            filename = (fw_data.get('filename') or '').strip()
            download_url = (fw_data.get('download_url') or '').strip()

            # Try to repair missing version from key as fallback.
            if not version and isinstance(key, str):
                version_match = re.search(r'(\d+\.\d+\.\d+(?:\.\d+)?)$', key)
                if version_match:
                    fw_data['version'] = version_match.group(1)
                    version = fw_data['version']
                    repaired_count += 1

            # Try to repair missing model from supported_models first.
            if not model:
                supported = fw_data.get('supported_models') or []
                if isinstance(supported, list) and supported:
                    first_model = str(supported[0]).strip().upper()
                    if first_model:
                        fw_data['model'] = first_model
                        model = first_model
                        repaired_count += 1

            # Remove entries that cannot possibly be resolved.
            if not model or not version:
                keys_to_remove.append(key)
                continue

            # Normalize canonical fields
            fw_data['model'] = model
            fw_data['hardware_version'] = hw_version or 'UNKNOWN'
            if not fw_data.get('supported_models'):
                fw_data['supported_models'] = [model]

            # If filename missing but URL has a usable filename, infer it.
            if not filename and download_url:
                inferred = download_url.split('/')[-1].split('?')[0]
                if inferred and any(inferred.lower().endswith(ext) for ext in ['.zip', '.dav', '.pak', '.bin']):
                    fw_data['filename'] = inferred
                    repaired_count += 1

            # Ensure device_id points to an existing device mapping.
            pair_key = (model, fw_data.get('hardware_version', 'UNKNOWN'))
            device_id = fw_data.get('device_id')
            if pair_key not in device_pair_to_id:
                new_id = create_device_id(self.devices, pair_key[0], pair_key[1])
                device_pair_to_id[pair_key] = new_id
                fw_data['device_id'] = new_id
                repaired_count += 1
            else:
                canonical_id = device_pair_to_id[pair_key]
                if not device_id or str(device_id) != str(canonical_id):
                    fw_data['device_id'] = canonical_id
                    repaired_count += 1

        for key in keys_to_remove:
            del self.firmwares_live[key]
            removed_count += 1

        if repaired_count > 0:
            logger.info(f"  🛠️  Repaired {repaired_count} firmware field issue(s)")
        if removed_count > 0:
            logger.info(f"  🧹 Removed {removed_count} irrecoverably invalid firmware entry(ies)")

    def integrity_report(self) -> dict:
        """Return integrity report for dry-run verification."""
        report = {
            'firmwares_missing_model': 0,
            'firmwares_missing_version': 0,
            'firmwares_missing_device_id': 0,
            'firmwares_with_unknown_model': 0,
            'firmwares_missing_notes': 0,
            'orphan_device_entries': 0,
        }

        referenced_device_ids = set()
        for fw_data in self.firmwares_live.values():
            model = (fw_data.get('model') or '').strip()
            version = (fw_data.get('version') or '').strip()
            device_id = fw_data.get('device_id')
            if not model:
                report['firmwares_missing_model'] += 1
            if not version:
                report['firmwares_missing_version'] += 1
            if not device_id:
                report['firmwares_missing_device_id'] += 1
            if model.upper() == 'UNKNOWN':
                report['firmwares_with_unknown_model'] += 1
            if not (fw_data.get('notes') or '').strip():
                report['firmwares_missing_notes'] += 1
            if device_id:
                referenced_device_ids.add(str(device_id))

        for did in self.devices.keys():
            if did not in referenced_device_ids:
                report['orphan_device_entries'] += 1

        return report
    
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

                supported_match = re.search(
                    r'\*\*Supported Devices:\*\*\s*([^\n]+)',
                    section,
                    re.IGNORECASE,
                )
                applied_to = supported_match.group(1).strip() if supported_match else ''
                section_models = extract_models(f'{applied_to} {section}')
                if model == 'UNKNOWN' and section_models:
                    model = section_models[0]
                elif model == 'UNKNOWN':
                    continue
                if not applied_to and section_models:
                    applied_to = 'Applied to: ' + ', '.join(section_models[:5])

                # Extract date: "Release Date: YYYY-MM-DD"
                date_match = re.search(r'Release Date:\s*(\d{4}-\d{2}-\d{2})', section, re.IGNORECASE)
                date_str = date_match.group(1) if date_match else ''

                # Extract filename from download link: "[📥 Download FILENAME](...)"
                filename_match = re.search(r'\[📥\s*Download\s+([^\]]+)\]', section, re.IGNORECASE)
                if filename_match:
                    filename = filename_match.group(1).strip()
                    if model not in section_models:
                        section_models.insert(0, model)
                    filename_to_info[filename] = {
                        'model': model,
                        'version': version,
                        'date': date_str,
                        'applied_to': applied_to,
                        'supported_models': section_models or [model],
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

        # Normalize existing entries to GitHub-style download URLs for consistency.
        # This makes JSON/README/releases consistent for HA consumers.
        normalized_url_count = 0
        for fw_data in self.firmwares_live.values():
            filename = (fw_data.get('filename') or '').strip()
            download_url = (fw_data.get('download_url') or '').strip()

            # Try to infer filename from URL if missing.
            if not filename and download_url:
                inferred = download_url.split('/')[-1].split('?')[0]
                if inferred and any(inferred.lower().endswith(ext) for ext in ['.zip', '.dav', '.pak', '.bin']):
                    filename = inferred
                    fw_data['filename'] = inferred

            if filename:
                github_url = f"https://github.com/{GITHUB_REPO}/releases/latest/download/{filename}"
                if fw_data.get('download_url') != github_url:
                    fw_data['download_url'] = github_url
                    normalized_url_count += 1

        if normalized_url_count > 0:
            logger.info(f"  🔗 Normalized {normalized_url_count} firmware download URL(s) to GitHub release links")
        
        # Find files in releases that aren't in JSON
        added_count = 0
        for filename in release_filenames:
            # Check if this file is already in JSON
            found = False
            release_info = filename_to_info.get(filename)
            for key, fw_data in self.firmwares_live.items():
                if fw_data.get('filename') == filename:
                    found = True
                    # Backfill release metadata for existing entries, but do not
                    # replace good data with blanks.
                    if release_info:
                        if release_info.get('date') and not fw_data.get('date'):
                            fw_data['date'] = release_info['date']
                        if release_info.get('model') and (
                            not fw_data.get('model')
                            or str(fw_data.get('model', '')).upper() == 'UNKNOWN'
                        ):
                            fw_data['model'] = release_info['model']
                        if release_info.get('version') and not fw_data.get('version'):
                            fw_data['version'] = release_info['version']
                        if release_info.get('applied_to') and not (
                            fw_data.get('applied_to') or ''
                        ).strip():
                            fw_data['applied_to'] = release_info['applied_to']
                        if release_info.get('supported_models') and (
                            not fw_data.get('supported_models')
                            or fw_data.get('supported_models') == ['UNKNOWN']
                        ):
                            fw_data['supported_models'] = release_info['supported_models']
                    break
            
            if not found:
                # Try to get model/version from release notes first
                info = release_info
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
            
            # Only prune entries that were created by GitHub release sync itself and
            # now reference missing release assets.
            if (
                fw_data.get('source') == 'github_releases_sync'
                and filename
                and 'github.com' in download_url
                and filename not in release_filenames
            ):
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
        # Backfill UNKNOWN models, hardware versions, and applied_to metadata
        self.heal_firmware_metadata()
        # Repair malformed records and ensure device mappings are consistent
        self.repair_and_validate_entries()
        # Clean up incomplete UNKNOWN entries
        self.cleanup_unknown_entries()
        # Clean up failed downloads before saving
        self.cleanup_failed_downloads()
        # Clean up devices without firmwares
        self.cleanup_empty_devices()
        save_json('devices.json', self.devices)
        save_json('firmwares_live.json', self.firmwares_live)
        logger.info("Data saved")
    
    def save_status_running(self):
        """Mark scrape as in progress (so README does not show stale SUCCESS)."""
        from datetime import datetime
        existing = load_json('status.json') or {}
        self.status = {
            **existing,
            'status': 'running',
            'last_run': datetime.now().isoformat(),
            'firmwares_found': len(self.firmwares_live),
            'new_firmwares': 0,
            'errors': self.errors[-10:],
            'test_mode': TEST_MODE,
        }
        save_json('status.json', self.status)
        logger.info("  → Status set to running")

    def save_status(self):
        """Save status and errors to status.json."""
        from datetime import datetime
        self.status['last_run'] = datetime.now().isoformat()
        self.status['firmwares_found'] = len(self.firmwares_live)
        self.status['new_firmwares'] = self.scraped_count
        self.status['scraper_mode'] = 'http'
        self.status['catalog_fetch'] = self._catalog_fetch_method
        self.status['catalog_entries'] = self._catalog_entry_count
        if self._priority_patterns:
            self.status['priority_models'] = self._priority_patterns
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
        if USE_HTTP_SCRAPER:
            logger.info("Mode: HTTP catalog (no browser)")
        else:
            logger.info("Mode: Playwright browser (USE_PLAYWRIGHT=1)")
        logger.info("Starting Hikvision firmware scrape...")
        logger.info("=" * 60)
        
        start_time = time.time()
        self.save_status_running()
        self.load_priority_models()
        
        try:
            if USE_HTTP_SCRAPER:
                firmwares = self.scrape_via_http()
            else:
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
            self.save_status()
            if (
                self._priority_one_shot
                and self.status.get('status') in ('success', 'no_new_firmwares')
                and self.scraped_count > 0
            ):
                self.clear_priority_models_file()
            elif self._priority_one_shot and self.scraped_count == 0:
                logger.info(
                    '[PRIORITY] keeping priority_models.json — no new downloads this run '
                    '(firmware may already be archived; re-run or clear file manually)'
                )


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
