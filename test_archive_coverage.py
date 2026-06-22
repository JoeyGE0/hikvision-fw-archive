#!/usr/bin/env python3
"""Archive coverage + HA firmware-update behaviour (no network)."""
import json
import os
import re
import sys
import unittest
from typing import Optional

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from main import HikvisionScraper
from release import generate_firmware_index, index_models_for_firmware, parse_version


def compare_versions(current: str, available: str) -> bool:
    """True when available is newer than current (matches hikvision_isapi)."""
    current_tuple = parse_version(current)
    available_tuple = parse_version(available)
    max_len = max(len(current_tuple), len(available_tuple))
    current_padded = current_tuple + (0,) * (max_len - len(current_tuple))
    available_padded = available_tuple + (0,) * (max_len - len(available_tuple))
    return available_padded > current_padded


def normalize_model(model: str) -> str:
    if not model:
        return ""
    model = re.sub(r"\([^)]*\)", "", model).strip()
    return " ".join(model.split()).upper()


def simulate_ha_coordinator(
    device_model: str,
    installed: str,
    hardware_version: Optional[str] = "IPC_G0",
) -> dict:
    """Mirror hikvision_isapi FirmwareUpdateCoordinator index path."""
    index = generate_firmware_index()
    models = index.get("models") or {}

    normalized_model = normalize_model(device_model)
    normalized_hw = (hardware_version or "UNKNOWN").strip().upper()

    def _model_series_token(model: str) -> str:
        parts = model.upper().split("-")
        return parts[1] if len(parts) >= 2 else model.upper()

    def _model_match_score(device: str, candidate: str) -> int:
        if not device or not candidate:
            return 0
        if device == candidate:
            return 10_000
        if device.startswith(candidate) or candidate.startswith(device):
            return 5_000 + min(len(device), len(candidate))
        if _model_series_token(device) != _model_series_token(candidate):
            return 0
        return 1_000 + min(len(device), len(candidate))

    model_entry = models.get(normalized_model)
    matched_via = "exact"
    if not model_entry:
        best_score = 0
        best_key = None
        for key, entry in models.items():
            score = _model_match_score(normalized_model, normalize_model(key))
            if score > best_score:
                best_score = score
                best_key = key
                model_entry = entry
        if best_score >= 1_000:
            matched_via = f"series:{best_key}"
        else:
            # hikvision_isapi fallback: prefix on model base (e.g. DS-2CD1383G2)
            model_parts = normalized_model.split("-")
            model_base = (
                "-".join(model_parts[:-1]) if len(model_parts) >= 2 else normalized_model
            )
            model_entry = None
            for key, entry in models.items():
                nk = normalize_model(key)
                if nk.startswith(model_base) or model_base in nk:
                    model_entry = entry
                    matched_via = f"prefix:{key}"
                    break

    if not isinstance(model_entry, dict):
        return {"matched": False, "available": False, "ahead_of_archive": False}

    record = model_entry.get("latest") or {}
    by_hw = model_entry.get("by_hardware_version") or {}
    if isinstance(by_hw, dict) and normalized_hw in by_hw:
        record = by_hw[normalized_hw]

    archive_version = (record.get("version") or "").strip()
    available = bool(
        archive_version and compare_versions(installed, archive_version)
    )
    ahead = bool(
        archive_version and compare_versions(archive_version, installed)
    )
    return {
        "matched": True,
        "matched_via": matched_via,
        "matched_model": record.get("model"),
        "archive_latest": archive_version,
        "download_url": record.get("download_url"),
        "available": available,
        "ahead_of_archive": ahead and not available,
        "ha_shows_up_to_date": not available,
    }


class TestNoDownloadFilter(unittest.TestCase):
    def test_scraper_has_no_download_allowlist(self):
        scraper = HikvisionScraper()
        self.assertFalse(hasattr(scraper, "model_eligible_for_download"))
        self.assertNotIn("DOWNLOAD_MODEL_PREFIXES", dir(sys.modules["main"]))

    def test_non_ds2cd_model_not_blocked_by_removed_filter(self):
        """Regression: DS-K3 and similar must not be skipped by a DS-2CD allowlist."""
        scraper = HikvisionScraper()
        self.assertFalse(hasattr(scraper, "model_eligible_for_download"))


class TestIndexModelsForFirmware(unittest.TestCase):
    """Regression: supported_models must not widen index beyond applied_to."""

    def test_supported_models_ignored_when_applied_to_present(self):
        firmware = {
            "model": "DS-2CD1063G2-LIU(F)",
            "applied_to": (
                "Applied to: DS-2CD1063G2-LIU(F), DS-2CD1063G2-LIUF/SL"
            ),
            "supported_models": [
                "DS-2CD1063G2-LIUF/SL",
                "DS-2CD1383G2-LIUF/SL",
            ],
        }
        keys = index_models_for_firmware(firmware)
        self.assertIn("DS-2CD1063G2-LIUF/SL", keys)
        self.assertNotIn("DS-2CD1383G2-LIUF/SL", keys)

    def test_supported_models_used_when_applied_to_missing(self):
        firmware = {
            "model": "DS-TEST-MODEL",
            "supported_models": ["DS-TEST-MODEL", "DS-TEST-VARIANT"],
        }
        keys = index_models_for_firmware(firmware)
        self.assertIn("DS-TEST-MODEL", keys)
        self.assertIn("DS-TEST-VARIANT", keys)


class TestUserCameraArchive(unittest.TestCase):
    USER_MODEL = "DS-2CD1383G2-LIUF"
    INSTALLED = "5.8.41"

    @unittest.skipUnless(os.path.exists("firmwares_live.json"), "needs firmwares_live.json")
    def test_no_exact_liuf_firmware_rows(self):
        with open("firmwares_live.json", encoding="utf-8") as f:
            live = json.load(f)
        hits = []
        for key, row in live.items():
            if not isinstance(row, dict):
                continue
            blob = json.dumps(row)
            if self.USER_MODEL in blob or row.get("model") == self.USER_MODEL:
                hits.append(
                    (key, row.get("model"), row.get("version"), row.get("filename"))
                )
        self.assertEqual(
            hits,
            [],
            f"expected no archive rows for {self.USER_MODEL}, got {hits}",
        )

    @unittest.skipUnless(os.path.exists("firmwares_live.json"), "needs firmwares_live.json")
    def test_closest_variant_is_g2p_not_liuf(self):
        with open("firmwares_live.json", encoding="utf-8") as f:
            live = json.load(f)
        p_rows = [
            (k, v.get("version"))
            for k, v in live.items()
            if isinstance(v, dict) and v.get("model") == "DS-2CD1383G2P-LIUF"
        ]
        self.assertTrue(p_rows, "DS-2CD1383G2P-LIUF should exist in archive")
        versions = {v for _, v in p_rows}
        self.assertIn("5.8.11", versions)
        self.assertNotIn(self.INSTALLED, versions)

    @unittest.skipUnless(os.path.exists("firmwares_live.json"), "needs firmwares_live.json")
    def test_5841_exists_for_other_models_not_user_sku(self):
        with open("firmwares_live.json", encoding="utf-8") as f:
            live = json.load(f)
        v41 = [
            (v.get("model"), v.get("version"))
            for v in live.values()
            if isinstance(v, dict) and v.get("version") == "5.8.41"
        ]
        self.assertTrue(v41, "5.8.41 should exist somewhere in archive")
        for model, _ in v41:
            self.assertNotEqual(
                normalize_model(model),
                normalize_model(self.USER_MODEL),
                "5.8.41 should not be keyed to user's exact SKU yet",
            )

    @unittest.skipUnless(os.path.exists("firmware_index.json"), "needs firmware_index.json")
    def test_index_has_no_liuf_key(self):
        with open("firmware_index.json", encoding="utf-8") as f:
            index = json.load(f)
        models = index.get("models") or {}
        self.assertNotIn(normalize_model(self.USER_MODEL), models)
        self.assertNotIn(normalize_model("DS-2CD1383G2-LIUF/SL"), models)

    def test_ha_shows_up_to_date_not_update_available(self):
        state = simulate_ha_coordinator(self.USER_MODEL, self.INSTALLED)
        self.assertTrue(state["matched"], "should fuzzy-match DS-2CD1383G2P-LIUF")
        self.assertEqual(state["archive_latest"], "5.8.11")
        self.assertFalse(state["available"])
        self.assertTrue(state["ha_shows_up_to_date"])
        self.assertTrue(state["ahead_of_archive"])

    def test_install_would_be_blocked_as_downgrade(self):
        state = simulate_ha_coordinator(self.USER_MODEL, self.INSTALLED)
        archive = state["archive_latest"]
        self.assertFalse(compare_versions(self.INSTALLED, archive))


class TestWorkflowFilterRemoved(unittest.TestCase):
    def test_update_yml_has_no_download_prefix_env(self):
        path = os.path.join(os.path.dirname(__file__), ".github", "workflows", "update.yml")
        with open(path, encoding="utf-8") as f:
            content = f.read()
        self.assertNotIn("DOWNLOAD_MODEL_PREFIXES", content)


if __name__ == "__main__":
    unittest.main()
