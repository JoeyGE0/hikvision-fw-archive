#!/usr/bin/env python3
"""
Remove firmware DB rows whose zip download URL is missing, broken, or not GitHub.

Keeps Hikvision links in `notes` (release-note PDFs). Only purges firmware
download URLs — never touches readme_header.md.

Default is dry-run. Use --apply to write JSON + regenerate README.md.

Examples:
  python3 purge_invalid_firmwares.py              # preview only
  python3 purge_invalid_firmwares.py --apply      # purge + save + README
"""
from __future__ import annotations

import argparse
import json
import logging
import sys
import time
from collections import defaultdict
from pathlib import Path
from typing import Dict, List, Optional, Tuple
from urllib.parse import urlparse

try:
    import requests
except ImportError:
    print("Install requests: pip install requests", file=sys.stderr)
    sys.exit(1)

from common import load_json, save_json

logging.basicConfig(level=logging.INFO, format="%(message)s")
logger = logging.getLogger(__name__)

GITHUB_REPO = "JoeyGE0/hikvision-fw-archive"
FIRMWARE_EXTS = (".zip", ".dav", ".pak", ".bin")
HIKVISION_HOSTS = ("hikvision.com", "assets.hikvision.com")


def is_firmware_extension(url_or_path: str) -> bool:
    path = urlparse(url_or_path).path if "://" in url_or_path else url_or_path
    return path.lower().endswith(FIRMWARE_EXTS)


def is_hikvision_firmware_download(url: str) -> bool:
    if not url:
        return False
    host = urlparse(url).netloc.lower()
    if not any(h in host for h in HIKVISION_HOSTS):
        return False
    return is_firmware_extension(url)


def is_github_release_download(url: str) -> bool:
    if not url:
        return False
    u = url.lower()
    return "github.com" in u and "/releases/" in u and "download" in u


def build_github_latest_url(filename: str) -> str:
    return f"https://github.com/{GITHUB_REPO}/releases/latest/download/{filename}"


def effective_download_url(fw: dict) -> str:
    url = (fw.get("download_url") or "").strip()
    if url:
        return url
    filename = (fw.get("filename") or "").strip()
    if filename:
        return build_github_latest_url(filename)
    return ""


def classify_url(url: str) -> str:
    """Return removal reason, or empty string if URL should be HTTP-checked."""
    if not url:
        return "missing_url"
    if "materials-license-agreement" in url.lower():
        return "license_page"
    if is_hikvision_firmware_download(url):
        return "hikvision_zip"
    if "github.com" not in url.lower():
        return "non_github"
    if not is_github_release_download(url):
        return "non_github_release"
    return ""


def check_url_exists(url: str, session: requests.Session, timeout: int = 20) -> Tuple[bool, int]:
    try:
        r = session.head(url, allow_redirects=True, timeout=timeout)
        if r.status_code == 405:
            r = session.get(url, stream=True, allow_redirects=True, timeout=timeout)
            r.close()
        return (200 <= r.status_code < 300, r.status_code)
    except requests.RequestException as exc:
        logger.debug("HEAD failed for %s: %s", url, exc)
        return (False, 0)


def load_firmware_stores() -> Tuple[dict, dict]:
    live = load_json("firmwares_live.json") or {}
    manual = load_json("firmwares_manual.json") or {}
    return live, manual


def cleanup_orphan_devices(devices: dict, live: dict, manual: dict) -> List[str]:
    referenced = set()
    for fw in {**live, **manual}.values():
        device_id = fw.get("device_id")
        if device_id is not None:
            referenced.add(str(device_id))
    removed = []
    for device_id in list(devices.keys()):
        if device_id not in referenced:
            del devices[device_id]
            removed.append(device_id)
    return removed


def regenerate_readme() -> None:
    from release import generate_readme

    Path("README.md").write_text(generate_readme(), encoding="utf-8")
    logger.info("Regenerated README.md")


def run_purge(apply: bool, timeout: int) -> int:
    live, manual = load_firmware_stores()
    devices = load_json("devices.json") or {}
    combined: Dict[str, Tuple[str, dict]] = {}
    for key, fw in live.items():
        combined[key] = ("firmwares_live.json", fw)
    for key, fw in manual.items():
        combined[key] = ("firmwares_manual.json", fw)

    session = requests.Session()
    session.headers.update({"User-Agent": "hikvision-fw-archive-purge/1.0"})

    # Check each unique download URL once
    url_cache: Dict[str, Tuple[bool, int]] = {}
    url_to_keys: Dict[str, List[str]] = defaultdict(list)

    preclassified: Dict[str, str] = {}
    for key, (_, fw) in combined.items():
        url = effective_download_url(fw)
        reason = classify_url(url)
        if reason:
            preclassified[key] = reason
            continue
        url_to_keys[url].append(key)

    logger.info("Checking %s unique GitHub download URL(s)...", len(url_to_keys))
    for idx, url in enumerate(url_to_keys, 1):
        ok, status = check_url_exists(url, session, timeout=timeout)
        url_cache[url] = (ok, status)
        if idx % 25 == 0:
            logger.info("  ... checked %s/%s", idx, len(url_to_keys))
        time.sleep(0.05)

    to_remove: Dict[str, str] = dict(preclassified)
    for url, keys in url_to_keys.items():
        ok, status = url_cache[url]
        if not ok:
            for key in keys:
                to_remove[key] = f"broken_url (HTTP {status or 'error'})"

    # Summarise
    by_reason: Dict[str, List[str]] = defaultdict(list)
    for key, reason in to_remove.items():
        by_reason[reason.split(" ")[0]].append(key)

    kept = len(combined) - len(to_remove)
    logger.info("")
    logger.info("=" * 60)
    logger.info("PURGE PREVIEW (%s)", "APPLY" if apply else "DRY-RUN")
    logger.info("=" * 60)
    logger.info("Total firmware rows:     %s", len(combined))
    logger.info("Keep (valid GitHub zip): %s", kept)
    logger.info("Remove:                  %s", len(to_remove))
    for reason, keys in sorted(by_reason.items(), key=lambda x: -len(x[1])):
        logger.info("  - %-20s %s", reason + ":", len(keys))

    samples = []
    for key in sorted(to_remove)[:30]:
        store, fw = combined[key]
        samples.append(
            {
                "key": key,
                "store": store,
                "model": fw.get("model"),
                "version": fw.get("version"),
                "download_url": effective_download_url(fw),
                "notes": fw.get("notes", ""),
                "reason": to_remove[key],
            }
        )

    report = {
        "mode": "apply" if apply else "dry-run",
        "summary": {
            "total": len(combined),
            "keep": kept,
            "remove": len(to_remove),
            "by_reason": {k: len(v) for k, v in by_reason.items()},
        },
        "remove_samples": samples,
        "remove_keys": sorted(to_remove.keys()),
    }
    report_path = Path("purge_invalid_firmwares_report.json")
    report_path.write_text(json.dumps(report, indent=2), encoding="utf-8")
    logger.info("")
    logger.info("Sample removals (first 15):")
    for row in samples[:15]:
        logger.info(
            "  %s v%s | %s | %s",
            row["model"],
            row["version"],
            row["reason"],
            row["download_url"][:80] + ("..." if len(row["download_url"]) > 80 else ""),
        )
    if len(to_remove) > 15:
        logger.info("  ... and %s more (see %s)", len(to_remove) - 15, report_path)
    else:
        logger.info("Full list: %s", report_path)

    if not apply:
        logger.info("")
        logger.info("Dry-run only — no files changed. Re-run with --apply to purge.")
        return 0

    if not to_remove:
        logger.info("Nothing to remove.")
        return 0

    for key in to_remove:
        if key in live:
            del live[key]
        if key in manual:
            del manual[key]

    removed_devices = cleanup_orphan_devices(devices, live, manual)

    save_json("firmwares_live.json", live)
    save_json("firmwares_manual.json", manual)
    save_json("devices.json", devices)
    regenerate_readme()

    logger.info("")
    logger.info("Removed %s firmware row(s) and %s orphan device(s).", len(to_remove), len(removed_devices))
    logger.info("Updated firmwares_live.json, firmwares_manual.json, devices.json, README.md")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Purge firmware rows with missing/broken/non-GitHub zip download URLs."
    )
    parser.add_argument(
        "--apply",
        action="store_true",
        help="Write changes (default is dry-run preview only).",
    )
    parser.add_argument(
        "--timeout",
        type=int,
        default=20,
        help="HTTP timeout per URL check (seconds).",
    )
    args = parser.parse_args()
    return run_purge(apply=args.apply, timeout=args.timeout)


if __name__ == "__main__":
    sys.exit(main())
