#!/usr/bin/env python3
"""Diagnose UNKNOWN model/hw_version from Hikvision catalog parse."""
import json
import re
from collections import Counter, defaultdict

from main import HikvisionScraper

TARGET_FILES = [
    'S3000715287',  # 5.5.61 UNKNOWN
    'S3000716059',  # 5.5.506 UNKNOWN
    'S3000720327',  # 5.7.11
]
TARGET_MODELS = [
    'DS-2DF4420',
    'DS-2DE4425W',
]


def main():
    scraper = HikvisionScraper()
    html = scraper.fetch_catalog_html()
    entries = scraper.parse_catalog_entries(html)

    print(f"Catalog entries: {len(entries)}")
    print(f"Fetch method: {scraper._catalog_fetch_method}\n")

    unknown_model = [e for e in entries if e.get('model') == 'UNKNOWN']
    unknown_hw = [e for e in entries if e.get('hardware_version') == 'UNKNOWN' and e.get('model') != 'UNKNOWN']

    print(f"Entries with model=UNKNOWN: {len(unknown_model)}")
    print(f"Entries with hw=UNKNOWN (model known): {len(unknown_hw)}\n")

    print("=" * 70)
    print("UNKNOWN model samples (first 20 unique labels)")
    seen = set()
    for e in unknown_model:
        label = e.get('label', '')[:120]
        if label in seen:
            continue
        seen.add(label)
        print(f"  label: {repr(e.get('label', '')[:200])}")
        print(f"  url:   {e.get('url', '')[-60:]}")
        print(f"  ver:   {e.get('version')}")
        print()
        if len(seen) >= 20:
            break

    print("=" * 70)
    print("Target firmware files in catalog:")
    for token in TARGET_FILES:
        hits = [e for e in entries if token in e.get('url', '')]
        print(f"\n--- {token} ({len(hits)} hit(s)) ---")
        for e in hits[:5]:
            applied_to, supported, resolved = scraper._metadata_from_catalog_label(
                e.get('label', ''), e.get('model', '')
            )
            print(json.dumps({
                'model': e.get('model'),
                'resolved_model': resolved,
                'hw': e.get('hardware_version'),
                'version': e.get('version'),
                'label': e.get('label', '')[:250],
                'supported_models': supported[:5],
                'applied_to': applied_to[:120] if applied_to else '',
            }, indent=2))

    print("\n" + "=" * 70)
    print("Target model families:")
    for prefix in TARGET_MODELS:
        hits = [e for e in entries if prefix in e.get('model', '') or prefix in e.get('label', '')]
        hw_counts = Counter(e.get('hardware_version') for e in hits)
        print(f"\n{prefix}: {len(hits)} entries, hw breakdown: {dict(hw_counts)}")
        for e in hits[:3]:
            print(f"  {e.get('model')} | hw={e.get('hardware_version')} | {e.get('label', '')[:80]}")

    # Panel mapping failures: chunk has firmware but model UNKNOWN
    print("\n" + "=" * 70)
    print("Panel model inference check for UNKNOWN entries")
    model_by_id = {}
    for match in re.finditer(r'data-target="(#firmware-collapse-\d+)"', html):
        tid = match.group(1)
        chunk = html[match.end():match.end() + 800]
        model_match = re.search(
            r'(DS-[0-9A-Z-]+|AE-[0-9A-Z-]+|IDS-[0-9A-Z-]+)',
            chunk,
            re.I,
        )
        if model_match:
            model_by_id[tid] = model_match.group(1).upper()

    # Group unknown by whether title has models
    no_title_model = 0
    has_title_model = 0
    for e in unknown_model:
        title_models = __import__('common').extract_models(e.get('label', ''))
        if title_models:
            has_title_model += 1
        else:
            no_title_model += 1
    print(f"  UNKNOWN with models in label: {has_title_model}")
    print(f"  UNKNOWN with NO models in label: {no_title_model}")

    if no_title_model:
        print("\n  Labels with no extractable model:")
        seen2 = set()
        for e in unknown_model:
            label = e.get('label', '')
            if __import__('common').extract_models(label):
                continue
            if label in seen2:
                continue
            seen2.add(label)
            print(f"    {repr(label[:200])}")
            if len(seen2) >= 15:
                break


if __name__ == '__main__':
    main()
