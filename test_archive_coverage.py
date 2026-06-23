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
    """Regression: manual rows for user SKUs must index and offer safe updates."""

    USER_CAMERAS = [
        ("DS-2CD2387G3-LIS2UY/SL", "5.8.10", "5.8.32", "S3000732541"),
        ("DS-2CD2387G3-LIS2UY/SRB", "5.8.10", "5.8.32", "S3000732541"),
        ("DS-2CD1383G2-LIUF", "5.8.5", "5.8.41", "S3000712595"),
        ("DS-2CD1383G2-LIUF/SL", "5.8.5", "5.8.41", "S3000712595"),
    ]

    @unittest.skipUnless(os.path.exists("firmwares_manual.json"), "needs firmwares_manual.json")
    def test_manual_rows_present(self):
        with open("firmwares_manual.json", encoding="utf-8") as f:
            manual = json.load(f)
        models = {v.get("model") for v in manual.values() if isinstance(v, dict)}
        self.assertIn("DS-2CD1383G2-LIUF", models)
        self.assertIn("DS-2CD1383G2-LIUF/SL", models)
        self.assertIn("DS-2CD2387G3-LIS2UY/S(L)(RB)", models)

    @unittest.skipUnless(os.path.exists("firmware_index.json"), "needs firmware_index.json")
    def test_index_has_user_model_keys(self):
        with open("firmware_index.json", encoding="utf-8") as f:
            index = json.load(f)
        models = index.get("models") or {}
        for device_model, _, _, _ in self.USER_CAMERAS:
            self.assertIn(normalize_model(device_model), models)

    def test_ha_offers_verified_updates(self):
        for device_model, installed, expected_version, expected_zip in self.USER_CAMERAS:
            state = simulate_ha_coordinator(device_model, installed)
            self.assertTrue(state["matched"], device_model)
            self.assertEqual(state["archive_latest"], expected_version, device_model)
            self.assertTrue(state["available"], device_model)
            self.assertIn(expected_zip, state["download_url"] or "")

    @unittest.skipUnless(os.path.exists("firmwares_live.json"), "needs firmwares_live.json")
    def test_1063_bulk_not_used_for_1383(self):
        with open("firmwares_live.json", encoding="utf-8") as f:
            live = json.load(f)
        bulk = live.get("DS-2CD1063G2-LIU(F)_IPC_G0_5.8.41", {})
        self.assertEqual(bulk.get("filename"), "Firmware__V5.8.41_260401_S3000712568.zip")
        state = simulate_ha_coordinator("DS-2CD1383G2-LIUF/SL", "5.8.5")
        self.assertNotIn("S3000712568", state["download_url"] or "")


class TestWorkflowFilterRemoved(unittest.TestCase):
    def test_update_yml_has_no_download_prefix_env(self):
        path = os.path.join(os.path.dirname(__file__), ".github", "workflows", "update.yml")
        with open(path, encoding="utf-8") as f:
            content = f.read()
        self.assertNotIn("DOWNLOAD_MODEL_PREFIXES", content)


if __name__ == "__main__":
    unittest.main()
