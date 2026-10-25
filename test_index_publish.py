"""firmware_index.json must stay under GitHub's 100 MiB blob limit."""
import json
import unittest

from release import dumps_firmware_index, publishable_firmware_index


def _record(version, filename, **extra):
    row = {
        "model": "DS-2CD2387G3-LI",
        "hardware_version": "UNKNOWN",
        "version": version,
        "date": "2026-01-01",
        "filename": filename,
        "download_url": f"https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1/{filename}",
        "applied_to": "Applied to: DS-2CD2387G3-LI",
        "changes": "Fixed known issues",
        "notes": "https://assets.hikvision.com/notes.pdf",
        "notes_pdf_url": "https://assets.hikvision.com/notes.pdf",
        "release_page_url": "https://github.com/JoeyGE0/hikvision-fw-archive/releases/tag/1",
        "license_url": "https://www.hikvision.com/en/policies/materials-license-agreement/",
        "archive_url": "https://github.com/JoeyGE0/hikvision-fw-archive",
    }
    row.update(extra)
    return row


class TestIndexPublish(unittest.TestCase):
    def _index(self):
        latest = _record("5.8.40", "new.zip")
        older = _record("5.8.10", "old.zip", hardware_version="V1")
        return {
            "generated_at": "2026-10-25T00:00:00+00:00",
            "models": {
                "DS-2CD2387G3-LI": {
                    "latest": latest,
                    "by_hardware_version": {"UNKNOWN": latest},
                    "all_versions": [latest, older],
                },
                "DS-2CD2387G3-LIUF": {
                    "latest": latest,
                    "by_hardware_version": {"UNKNOWN": latest, "V1": older},
                    "all_versions": [latest, older],
                },
            },
        }

    def test_drops_derived_fields_and_duplicate_hardware_copy(self):
        published = publishable_firmware_index(self._index())
        single = published["models"]["DS-2CD2387G3-LI"]
        self.assertNotIn("by_hardware_version", single)
        latest = single["latest"]
        self.assertEqual(latest["version"], "5.8.40")
        self.assertNotIn("license_url", latest)
        self.assertNotIn("notes_pdf_url", latest)
        self.assertNotIn("release_page_url", latest)
        self.assertEqual(latest["notes"], "https://assets.hikvision.com/notes.pdf")
        self.assertEqual(len(single["all_versions"]), 2)

        multi = published["models"]["DS-2CD2387G3-LIUF"]
        self.assertIn("V1", multi["by_hardware_version"])
        self.assertEqual(multi["by_hardware_version"]["V1"]["filename"], "old.zip")

    def test_compact_json_stays_under_github_limit(self):
        raw = dumps_firmware_index(self._index())
        self.assertLess(len(raw), 100 * 1024 * 1024)
        parsed = json.loads(raw)
        self.assertIn("DS-2CD2387G3-LI", parsed["models"])

    def test_drops_all_versions_when_over_budget(self):
        raw = dumps_firmware_index(self._index(), budget_bytes=1)
        parsed = json.loads(raw)
        entry = parsed["models"]["DS-2CD2387G3-LI"]
        self.assertNotIn("all_versions", entry)
        self.assertEqual(entry["latest"]["version"], "5.8.40")
        self.assertLess(len(raw), 100 * 1024 * 1024)


if __name__ == "__main__":
    unittest.main()
