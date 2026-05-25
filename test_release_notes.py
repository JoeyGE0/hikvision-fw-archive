#!/usr/bin/env python3
"""Tests for release-note PDF text summarization."""
import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from release_notes import extract_changes_summary, normalize_pdf_text


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


if __name__ == '__main__':
    unittest.main()
