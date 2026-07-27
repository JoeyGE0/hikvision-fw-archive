#!/usr/bin/env python3
"""Unit tests for regional catalog rotation (no network)."""
import json
import os
import tempfile
import unittest
from pathlib import Path
from unittest import mock

import main


class RegionRotationTests(unittest.TestCase):
    def test_catalog_url_for_region(self):
        self.assertEqual(
            main.catalog_url_for_region('ca-en'),
            'https://www.hikvision.com/ca-en/support/download/firmware/',
        )
        self.assertEqual(
            main.home_url_for_region('us-en'),
            'https://www.hikvision.com/us-en/',
        )

    def test_firmware_regions_env_override(self):
        with mock.patch.dict(os.environ, {'FIRMWARE_REGIONS': 'ca-en, au-en'}, clear=False):
            self.assertEqual(main.firmware_regions(), ['ca-en', 'au-en'])

    def test_round_robin_advances(self):
        with tempfile.TemporaryDirectory() as tmp:
            cwd = Path.cwd()
            try:
                os.chdir(tmp)
                Path('status.json').write_text(
                    json.dumps({'catalog_region': 'en'}), encoding='utf-8'
                )
                # Avoid loading huge live JSON from missing files
                with mock.patch.object(main, 'load_json', side_effect=self._load_json):
                    scraper = main.HikvisionScraper()
                    with mock.patch.dict(os.environ, {'FIRMWARE_REGION': ''}, clear=False):
                        region = scraper.select_catalog_region()
                self.assertEqual(region, 'us-en')
                self.assertIn('/us-en/support/download/firmware/', scraper.firmware_url)
            finally:
                os.chdir(cwd)

    def test_force_region(self):
        with tempfile.TemporaryDirectory() as tmp:
            cwd = Path.cwd()
            try:
                os.chdir(tmp)
                with mock.patch.object(main, 'load_json', side_effect=self._load_json):
                    scraper = main.HikvisionScraper()
                    with mock.patch.dict(os.environ, {'FIRMWARE_REGION': 'ca-en'}, clear=False):
                        region = scraper.select_catalog_region()
                self.assertEqual(region, 'ca-en')
                self.assertTrue(scraper.firmware_url.endswith('/ca-en/support/download/firmware/'))
            finally:
                os.chdir(cwd)

    @staticmethod
    def _load_json(path):
        if path == 'status.json' and Path(path).exists():
            return json.loads(Path(path).read_text(encoding='utf-8'))
        return {}


if __name__ == '__main__':
    unittest.main()
