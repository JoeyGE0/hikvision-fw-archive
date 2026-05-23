#!/usr/bin/env python3
"""Tests for heal + priority-first behaviour (no network)."""
import copy
import json
import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from main import HikvisionScraper, MAX_FIRMWARES_TO_DOWNLOAD


class TestMetadataAndPriority(unittest.TestCase):
    def test_parse_title_fixes_unknown_model(self):
        scraper = HikvisionScraper()
        html = (
            'firmware-collapse-1'
            '<a data-title="Applied to: DS-2CD2387G3-LIS2UY/SL(2.8mm)" '
            'data-href="https://assets.hikvision.com/x/Firmware__V5.8.32_260330.zip">'
            '</a>'
        )
        entries = scraper.parse_catalog_entries(html)
        self.assertEqual(len(entries), 1)
        self.assertEqual(entries[0]['model'], 'DS-2CD2387G3-LIS2UY')

    def test_find_live_key_hw_mismatch(self):
        scraper = HikvisionScraper()
        scraper.firmwares_live = {
            'DS-2CD2387G3-LIS2UY_IPC_G0_5.8.32': {'model': 'DS-2CD2387G3-LIS2UY'},
        }
        key = scraper._find_live_firmware_key(
            'DS-2CD2387G3-LIS2UY', 'UNKNOWN', '5.8.32'
        )
        self.assertEqual(key, 'DS-2CD2387G3-LIS2UY_IPC_G0_5.8.32')
        self.assertTrue(
            scraper.firmware_is_archived('DS-2CD2387G3-LIS2UY', 'UNKNOWN', '5.8.32', set())
        )

    def test_heal_fills_applied_to(self):
        scraper = HikvisionScraper()
        scraper.firmwares_live = {
            'DS-2CD1383G2P-LIUF_IPC_G0_5.8.12': {
                'model': 'DS-2CD1383G2P-LIUF',
                'hardware_version': 'IPC_G0',
                'version': '5.8.12',
                'supported_models': ['DS-2CD1383G2P-LIUF'],
                'applied_to': '',
            },
        }
        scraper.heal_firmware_metadata()
        entry = scraper.firmwares_live['DS-2CD1383G2P-LIUF_IPC_G0_5.8.12']
        self.assertTrue(entry['applied_to'].startswith('Applied to:'))

    def test_priority_first_still_scans_full_catalog(self):
        """Regression: must NOT stop after priority rows only."""
        scraper = HikvisionScraper()
        scraper._priority_patterns = ['DS-2CD2387G3-LIS2UY']
        catalog = [
            {'model': 'DS-2CD2387G3-LIS2UY', 'date': '2026-04-01', 'label': ''},
            {'model': 'DS-2CD9999-OTHER', 'date': '2026-05-01', 'label': ''},
        ]
        sorted_cat = scraper.sort_catalog_by_priority(catalog)
        self.assertEqual(len(sorted_cat), 2)
        self.assertEqual(sorted_cat[0]['model'], 'DS-2CD2387G3-LIS2UY')
        # Simulate download loop: full catalog, stop at limit
        scraper.firmwares_live = {}
        new_count = 0
        for entry in sorted_cat:
            if new_count >= MAX_FIRMWARES_TO_DOWNLOAD:
                break
            if scraper.firmware_is_archived(
                entry['model'], 'UNKNOWN', '9.9.9', set()
            ):
                continue
            new_count += 1
        # Both would be "new" — proves we can reach non-priority row
        self.assertEqual(new_count, 2)

    def test_process_archived_metadata_without_file(self):
        scraper = HikvisionScraper()
        scraper.firmwares_live = {
            'DS-2CD2387G3-LIS2UY_IPC_G0_5.8.32': {
                'model': 'DS-2CD2387G3-LIS2UY',
                'hardware_version': 'IPC_G0',
                'version': '5.8.32',
                'applied_to': '',
                'supported_models': ['DS-2CD2387G3-LIS2UY'],
            },
        }
        scraper.process_firmware({
            'model': 'DS-2CD2387G3-LIS2UY',
            'hardware_version': 'UNKNOWN',
            'version': '5.8.32',
            'local_file_path': '',
            'applied_to': 'Applied to: DS-2CD2387G3-LIS2UY/SL(2.8mm)',
            'supported_models': ['DS-2CD2387G3-LIS2UY'],
        })
        entry = scraper.firmwares_live['DS-2CD2387G3-LIS2UY_IPC_G0_5.8.32']
        self.assertIn('Applied to:', entry['applied_to'])


class TestHealOnLiveJson(unittest.TestCase):
    def test_heal_reduces_missing_applied_to_on_synthetic_data(self):
        scraper = HikvisionScraper()
        scraper.firmwares_live = {
            f'DS-2CD1023G2-LIUF_IPC_G0_5.8.{i}': {
                'model': 'DS-2CD1023G2-LIUF',
                'hardware_version': 'IPC_G0',
                'version': f'5.8.{i}',
                'supported_models': ['DS-2CD1023G2-LIUF'],
                'applied_to': '',
            }
            for i in range(10)
        }
        before = sum(
            1 for v in scraper.firmwares_live.values()
            if not (v.get('applied_to') or '').strip()
        )
        self.assertEqual(before, 10)
        scraper.heal_firmware_metadata()
        after = sum(
            1 for v in scraper.firmwares_live.values()
            if not (v.get('applied_to') or '').strip()
        )
        self.assertEqual(after, 0)

    @unittest.skipUnless(
        os.path.exists('firmwares_live.json'),
        'firmwares_live.json not present',
    )
    def test_live_json_few_unknown_models_remain(self):
        with open('firmwares_live.json', encoding='utf-8') as f:
            live = json.load(f)
        unknown_models = sum(
            1 for v in live.values() if (v.get('model') or '').upper() == 'UNKNOWN'
        )
        missing_applied = sum(
            1 for v in live.values() if not (v.get('applied_to') or '').strip()
        )
        self.assertLessEqual(unknown_models, 10)
        self.assertLessEqual(missing_applied, 10)


if __name__ == '__main__':
    unittest.main()
