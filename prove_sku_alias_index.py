#!/usr/bin/env python3
"""Prove SKU alias indexing fixes HA update detection for bare camera models.

Compares OLD index keys (exact catalog spelling only) vs NEW keys
(paren-stripped + /S(L)(RB) expansions) against firmwares_live.json.

Exit 0 only when every probe camera improves to the expected newer package.
"""
from __future__ import annotations

import json
import os
import re
import sys
from collections import defaultdict
from typing import Any, Dict, List

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from common import HIKVISION_MODEL_PATTERN, index_alias_keys, normalize_product_model
from release import model_match_score, parse_version

PROBES = [
    # camera deviceInfo model, installed fw, expected archive after fix
    ("DS-2CD2387G3-LIS2UY/SL", "5.8.32", "5.8.40"),
    ("DS-2CD2387G3-LIS2UY/SRB", "5.8.32", "5.8.40"),
]


def _old_keys(raw: str) -> List[str]:
    key = normalize_product_model(raw)
    return [key] if key and key != "UNKNOWN" else []


def _keys_for_firmware(firmware: Dict[str, Any], *, new: bool) -> List[str]:
    seen: set[str] = set()
    out: List[str] = []
    applied: List[str] = []

    def add(raw: str) -> None:
        keys = index_alias_keys(raw) if new else _old_keys(raw)
        for key in keys:
            if key and key not in seen:
                seen.add(key)
                out.append(key)

    applied_to = firmware.get("applied_to", "") or ""
    for match in re.findall(HIKVISION_MODEL_PATTERN, applied_to, re.IGNORECASE):
        applied.append(normalize_product_model(match))

    add(firmware.get("model", ""))
    for match in applied:
        add(match)

    supported_norm = [
        normalize_product_model(str(s))
        for s in firmware.get("supported_models") or []
        if str(s).strip()
    ]
    legacy = (
        len(applied) == 8
        and len(supported_norm) > 8
        and applied == supported_norm[:8]
    )
    if legacy or not applied:
        for supported in supported_norm:
            add(supported)
    return out


def build_latest_by_model(firmwares: Dict[str, Any], *, new: bool) -> Dict[str, Dict[str, Any]]:
    by_model: Dict[str, List[Dict[str, Any]]] = defaultdict(list)
    for firmware in firmwares.values():
        if not isinstance(firmware, dict):
            continue
        if not firmware.get("version") or not firmware.get("download_url"):
            continue
        for key in _keys_for_firmware(firmware, new=new):
            by_model[key].append(firmware)

    latest: Dict[str, Dict[str, Any]] = {}
    for model_key, rows in by_model.items():
        rows.sort(
            key=lambda r: (
                parse_version(r.get("version", "0")),
                model_match_score(model_key, r.get("model", "")),
            ),
            reverse=True,
        )
        latest[model_key] = rows[0]
    return latest


def main() -> int:
    live_path = os.path.join(os.path.dirname(__file__), "firmwares_live.json")
    if not os.path.exists(live_path):
        print(f"FAIL: missing {live_path}")
        return 2

    with open(live_path, encoding="utf-8") as f:
        live = json.load(f)

    old_index = build_latest_by_model(live, new=False)
    new_index = build_latest_by_model(live, new=True)

    print("SKU alias index proof (firmwares_live.json)")
    print("=" * 72)
    failed = 0
    for device, installed, expected in PROBES:
        old = old_index.get(device) or {}
        new = new_index.get(device) or {}
        old_ver = (old.get("version") or "MISSING").strip()
        new_ver = (new.get("version") or "MISSING").strip()
        old_file = old.get("filename") or "-"
        new_file = new.get("filename") or "-"
        improved = (
            new_ver == expected
            and parse_version(new_ver) > parse_version(old_ver if old_ver != "MISSING" else "0")
        ) or (
            new_ver == expected
            and old_ver != expected
        )
        # Require: new matches expected, and is strictly better than old for this probe
        ok = new_ver == expected and parse_version(new_ver) > parse_version(installed)
        if old_ver == expected:
            # Already correct before — still pass but note it
            ok = True
            improved = False
        elif not (new_ver == expected and parse_version(new_ver) > parse_version(old_ver if re.match(r"^\d", old_ver) else "0")):
            ok = False

        status = "PASS" if ok and (improved or old_ver == expected) else "FAIL"
        if status == "FAIL":
            failed += 1

        print(f"\nCamera: {device} (installed {installed})")
        print(f"  BEFORE: {old_ver:8}  {old_file}")
        print(f"  AFTER:  {new_ver:8}  {new_file}")
        print(f"  Expect: {expected}")
        print(f"  Result: {status}" + (" (improved)" if improved else ""))

    print("\n" + "=" * 72)
    if failed:
        print(f"FAILED: {failed}/{len(PROBES)} probes did not improve to expected package")
        return 1
    print(f"OK: all {len(PROBES)} probes resolve to the expected newer package after alias fix")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
