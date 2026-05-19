#!/usr/bin/env python3
"""
HTTP-only firmware test: fetch catalog HTML, parse URLs, download exactly 1 file.
No Playwright. Logs timing for each step.

Usage:
  python3 test_http_download_one.py
"""
import json
import logging
import re
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

import requests

FIRMWARE_PAGE = 'https://www.hikvision.com/en/support/download/firmware/'
OUT_DIR = Path('firmwares_http_test')
LOG_FILE = Path('firmwares_http_test/run_log.json')
HEADERS = {
    'User-Agent': (
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) '
        'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    ),
    'Referer': FIRMWARE_PAGE,
}

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s | %(levelname)s | %(message)s',
    datefmt='%H:%M:%S',
)
log = logging.getLogger('http_firmware_test')


def step(name: str):
    """Context manager for timed steps."""
    class _Step:
        def __init__(self, n):
            self.name = n
            self.t0 = None
            self.sec = None

        def __enter__(self):
            log.info('▶ START: %s', self.name)
            self.t0 = time.perf_counter()
            return self

        def __exit__(self, *args):
            self.sec = time.perf_counter() - self.t0
            log.info('✓ DONE:  %s (%.2fs)', self.name, self.sec)

    return _Step(name)


def fetch_page() -> str:
    with step('Download firmware HTML page'):
        r = requests.get(FIRMWARE_PAGE, timeout=120, headers=HEADERS)
        r.raise_for_status()
        size_mb = len(r.content) / (1024 * 1024)
        log.info('  HTTP %s | %.2f MB', r.status_code, size_mb)
        if size_mb < 1:
            raise RuntimeError('Page suspiciously small — may be blocked or wrong region')
        return r.text


def parse_entries(html: str) -> list:
    with step('Parse firmware URLs from HTML (regex)'):
        # Model titles + collapse ids
        blocks = re.findall(
            r'<div class="main-title"[^>]*data-target="(#firmware-collapse-\d+)"[^>]*>\s*'
            r'(?:<[^>]+>\s*)*([^<]+?)\s*</div>',
            html,
            re.DOTALL,
        )
        model_by_id = {tid: name.strip() for tid, name in blocks}
        log.info('  Found %d model row(s)', len(model_by_id))

        entries = []
        for m in re.finditer(
            r'id="(firmware-collapse-\d+)".*?</div>\s*</motion>',
            html,
            re.DOTALL,
        ):
            panel_id = m.group(1)
            chunk = m.group(0)
            model = model_by_id.get(f'#{panel_id}', model_by_id.get(panel_id, 'UNKNOWN'))
            if not model or model == 'UNKNOWN':
                # fallback: search near chunk start
                mt = re.search(
                    r'data-target="#' + re.escape(panel_id) + r'"[^>]*>\s*(?:<[^>]+>\s*)*([^<]+)',
                    html,
                )
                if mt:
                    model = mt.group(1).strip()

            for href, title in re.findall(
                r'data-href="(https://assets\.hikvision\.com[^"]+\.(?:zip|dav|pak|bin))"'
                r'[^>]*data-title="([^"]*)"',
                chunk,
                re.I,
            ):
                ver_m = re.search(r'[Vv]?(\d+\.\d+\.\d+(?:\.\d+)?)', title + ' ' + href)
                entries.append({
                    'model': model,
                    'version': ver_m.group(1) if ver_m else '',
                    'url': href,
                    'label': title,
                })

        # Simpler fallback if pairing failed
        if len(entries) < 100:
            log.warning('  Panel pairing weak (%d entries) — using global URL scan', len(entries))
            entries = []
            for href in re.findall(
                r'data-href="(https://assets\.hikvision\.com[^"]+\.(?:zip|dav|pak|bin))"',
                html,
                re.I,
            ):
                title_m = re.search(r'/([^/]+\.(?:zip|dav|pak|bin))', href, re.I)
                label = title_m.group(1) if title_m else href
                ver_m = re.search(r'[Vv]?(\d+\.\d+\.\d+(?:\.\d+)?)', label)
                entries.append({
                    'model': 'UNKNOWN',
                    'version': ver_m.group(1) if ver_m else '',
                    'url': href,
                    'label': label,
                })

        log.info('  Parsed %d firmware file URL(s)', len(entries))
        if not entries:
            raise RuntimeError('No firmware URLs found in HTML')
        return entries


def pick_one(entries: list) -> dict:
    with step('Pick 1 firmware to download (prefer small file for quick test)'):
        sample = entries[:80]
        best = None
        best_size = None
        for e in sample:
            try:
                h = requests.head(e['url'], headers=HEADERS, timeout=15, allow_redirects=True)
                if h.status_code >= 400:
                    continue
                cl = int(h.headers.get('content-length') or 0)
                if cl <= 0:
                    continue
                if best is None or cl < best_size:
                    best, best_size = e, cl
            except Exception:
                continue
        if best:
            log.info('  Selected smallest of %d probed: %s (%.2f MB)', len(sample), best['label'][:60], best_size / 1e6)
            log.info('  URL: %s', best['url'][:100])
            return best
        choice = entries[0]
        log.info('  HEAD probe failed; using first URL')
        log.info('  URL: %s', choice['url'][:100])
        return choice


def download_one(entry: dict) -> Path:
    OUT_DIR.mkdir(exist_ok=True)
    name = entry['url'].split('/')[-1].split('?')[0]
    path = OUT_DIR / name

    with step('Download 1 firmware file (full file)'):
        log.info('  Saving to: %s', path)
        t0 = time.perf_counter()
        with requests.get(entry['url'], headers=HEADERS, stream=True, timeout=300) as r:
            r.raise_for_status()
            ct = r.headers.get('content-type', '')
            cl = r.headers.get('content-length')
            log.info('  HTTP %s | Content-Type: %s | Content-Length: %s', r.status_code, ct, cl)
            if 'html' in ct.lower():
                raise RuntimeError('CDN returned HTML — missing Referer or blocked')
            total = 0
            with open(path, 'wb') as f:
                for chunk in r.iter_content(chunk_size=1024 * 256):
                    if chunk:
                        f.write(chunk)
                        total += len(chunk)
        elapsed = time.perf_counter() - t0
        mb = total / (1024 * 1024)
        speed = mb / elapsed if elapsed > 0 else 0
        log.info('  Downloaded %.2f MB in %.1fs (%.2f MB/s)', mb, elapsed, speed)

        if total < 10_000:
            raise RuntimeError(f'File too small ({total} bytes) — probably an error page')
        if path.read_bytes()[:2] != b'PK' and not name.lower().endswith('.dav'):
            log.warning('  File does not start with PK (zip magic) — may still be valid .dav')

        return path


def main() -> int:
    report = {
        'started_at': datetime.now(timezone.utc).isoformat(),
        'method': 'http_only_no_playwright',
        'steps': {},
        'success': False,
        'errors': [],
    }
    total_t0 = time.perf_counter()

    log.info('=' * 60)
    log.info('HTTP FIRMWARE TEST — download 1 file')
    log.info('=' * 60)

    try:
        html = fetch_page()
        report['steps']['fetch_page_sec'] = None  # filled by step logs below

        entries = parse_entries(html)
        report['firmware_urls_found'] = len(entries)

        choice = pick_one(entries)
        report['selected'] = choice

        path = download_one(choice)
        report['saved_path'] = str(path.resolve())
        report['saved_bytes'] = path.stat().st_size
        report['success'] = True

    except Exception as e:
        log.error('✗ FAILED: %s', e)
        report['errors'].append(str(e))
        report['success'] = False

    report['total_sec'] = round(time.perf_counter() - total_t0, 2)
    OUT_DIR.mkdir(exist_ok=True)
    LOG_FILE.write_text(json.dumps(report, indent=2), encoding='utf-8')

    log.info('=' * 60)
    log.info('SUMMARY')
    log.info('  Success: %s', report['success'])
    log.info('  Total time: %.2fs', report['total_sec'])
    log.info('  URLs found: %s', report.get('firmware_urls_found', 'n/a'))
    if report.get('saved_path'):
        log.info('  File: %s (%.2f MB)', report['saved_path'], report.get('saved_bytes', 0) / 1e6)
    log.info('  Log written: %s', LOG_FILE.resolve())
    log.info('=' * 60)
    log.info('Compare: Playwright scrape often takes minutes–hours; this test targets <3 min total.')

    return 0 if report['success'] else 1


if __name__ == '__main__':
    sys.exit(main())
