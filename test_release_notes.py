#!/usr/bin/env python3
"""Tests for release-note PDF text summarization."""
import json
import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from release_notes import (
    extract_changes_summary,
    fetch_pdf_summary,
    normalize_pdf_text,
    pdf_text_from_bytes,
    strip_line_prefix,
)

BULLET = '\uf06c'

SAMPLE = """
Network Camera-V5.8.11_SP1 Release Note- E11
Firmware Basic Information Firmware version: V5.8.11_SP1
New Features
Modify Function
Fixed the screen flickering issue for 4G/WI-FI cameras
Customer Impact and Recommended Action
This update refers to function/compatibility improvement
Supported Product List
Product Category Model Number
IPC 1 Series DS-2CD1363G2P-LIUF/SRB(2.8mm)(O-STD)
"""


class TestReleaseNotes(unittest.TestCase):
    def test_extract_modify_function_line(self):
        summary = extract_changes_summary(SAMPLE)
        self.assertIn('screen flickering', summary.lower())

    def test_stops_before_supported_product_list(self):
        summary = extract_changes_summary(SAMPLE)
        self.assertNotIn('DS-2CD1363', summary)
        self.assertNotIn('Product Category', summary)

    def test_features_section(self):
        text = normalize_pdf_text("""
Features
Improved functionality
Fix some known bugs and improve system stability.
Customer Impact
""")
        summary = extract_changes_summary(text)
        self.assertTrue(summary)
        self.assertIn('stability', summary.lower())

    def test_empty_input(self):
        self.assertEqual(extract_changes_summary(''), '')

    def test_numbered_new_optimized_and_issues_fixes(self):
        text = normalize_pdf_text("""
1) New & Optimized Features
1.1 Issues fixes：
1) Fixed known software issues.
Customer Impact and Recommended Action
""")
        summary = extract_changes_summary(text)
        self.assertIn('known software issues', summary.lower())

    def test_modify_features_bullets(self):
        text = normalize_pdf_text(f"""
{BULLET} New Features
1. Add Tracking function to the 4 series 4MP PTZ camera.
{BULLET} Modify Features
1. Cybersecurity Compliance Remediation.
2. Update the SDK and PHY network interface controller.
Customer Impact and Recommended Action
""")
        summary = extract_changes_summary(text)
        self.assertIn('tracking function', summary.lower())
        self.assertIn('cybersecurity', summary.lower())
        self.assertNotIn('modify features', summary.lower())

    def test_modified_features_dash(self):
        text = normalize_pdf_text("""
Modified Features
- Fixed some known bugs, recommended upgrade
Customer Impact and Recommended Action
""")
        summary = extract_changes_summary(text)
        self.assertIn('known bugs', summary.lower())

    def test_stops_at_note_not_lens_paragraph(self):
        text = normalize_pdf_text("""
New Features
Modify Function
1. Fix EZVIZ library permission authentication issue
Note
The camera uses a ZD25 electric lens. In scenes with a large depth of field.
Customer Impact and Recommended Action
""")
        summary = extract_changes_summary(text)
        self.assertIn('ezviz', summary.lower())
        self.assertNotIn('zd25', summary.lower())
        self.assertNotIn('electric lens', summary.lower())

    def test_strip_line_prefix_numbered(self):
        self.assertEqual(
            strip_line_prefix('1) New & Optimized Features'),
            'New & Optimized Features',
        )
        self.assertEqual(
            strip_line_prefix(f'{BULLET} Modify Features'),
            'Modify Features',
        )


class TestLiveReleaseNotePdfs(unittest.TestCase):
    """Fetch real Hikvision PDFs referenced in firmwares_live.json."""

    @classmethod
    def setUpClass(cls):
        cls.urls: list[str] = []
        path = os.path.join(os.path.dirname(__file__), 'firmwares_live.json')
        if not os.path.isfile(path):
            return
        with open(path, encoding='utf-8') as f:
            data = json.load(f)
        items = data if isinstance(data, list) else data.values()
        seen: set[str] = set()
        for fw in items:
            if not isinstance(fw, dict):
                continue
            url = (fw.get('notes') or '').strip()
            if url.lower().endswith('.pdf') and url not in seen:
                seen.add(url)
                cls.urls.append(url)

    def test_live_pdfs_produce_summaries(self):
        if not self.urls:
            self.skipTest('firmwares_live.json missing or has no PDF notes')
        if os.environ.get('SKIP_LIVE_PDF_TESTS'):
            self.skipTest('SKIP_LIVE_PDF_TESTS set')

        try:
            import requests  # noqa: F401
        except ImportError:
            self.skipTest('requests not installed')

        headers = {
            'User-Agent': 'Mozilla/5.0 (compatible; hikvision-fw-archive/1.0)',
        }
        cache: dict = {}
        ok = 0
        failed: list[str] = []
        for url in self.urls:
            summary = fetch_pdf_summary(url, cache, headers=headers, timeout=60)
            if summary and len(summary) >= 12:
                ok += 1
            else:
                failed.append(url.split('/')[-1][:60])

        # Most catalog PDFs use standard section headers; allow a few edge cases.
        min_ok = max(1, int(len(self.urls) * 0.7))
        self.assertGreaterEqual(
            ok,
            min_ok,
            f'Only {ok}/{len(self.urls)} PDFs parsed; missing: {failed[:5]}',
        )


if __name__ == '__main__':
    unittest.main()
