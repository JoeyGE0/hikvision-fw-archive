# Hikvision Firmware Archive

Unofficial archive of **Hikvision** IP camera, NVR/DVR, door station, and related firmware. Maintained automatically so older builds stay findable when Hikvision’s site only highlights the latest package.

**This is not affiliated with Hikvision.** Firmware remains subject to the [Hikvision Materials License Agreement](https://www.hikvision.com/en/policies/materials-license-agreement/).

- [About](#about)
- [Why this exists](#why-this-exists)
- [How this archive works](#how-this-archive-works)
- [Finding and downloading firmware](#finding-and-downloading-firmware)
- [Important warnings](#important-warnings)
- [Contributing](#contributing)
- [Automation status](#automation-status)
- [Firmware list](#firmware-list)

## About

Hikvision publishes firmware through a large web catalog ([firmware download center](https://www.hikvision.com/en/support/download/firmware/)). The catalog mixes many models and revisions; over time, older packages are hard to match to a specific device.

This repository:

- Tracks **model**, **hardware line** (e.g. `IPC_G0`), **version**, and **release date** where we can parse them
- Stores **direct download links** (GitHub Releases for files we have mirrored, plus metadata for others)
- Regenerates this README from JSON so the list stays searchable on GitHub

It does **not** host every Hikvision product forever. Coverage grows as the scraper runs (see limits below).

## Why this exists

| Problem on Hikvision’s site | What this repo does |
|----------------------------|---------------------|
| Hard to see full history for one model | Groups firmware rows by model / hardware in the list below |
| “Applied to” text is easy to miss | Stores `applied_to` and `supported_models` when the catalog provides them |
| Links are easy to lose | Mirrors new `.zip` / `.dav` files to **GitHub Releases** |
| Rollback after a bad upgrade | Keeps older versions we already captured |

## How this archive works

### Scheduled automation

GitHub Actions runs **twice daily** (04:20 and 16:20 UTC) and can be started manually from the **Actions** tab.

Each run:

1. **Fetches the firmware catalog** — usually one HTTP request to Hikvision’s SSR page; on GitHub’s network, **Playwright** is used when plain HTTP is blocked
2. **Parses thousands of download URLs** from the HTML (`data-href` / panel structure), not by clicking every model in a browser
3. **Downloads up to 10 new firmware files** per run (20 per day at most) to avoid hammering Hikvision and GitHub
4. **Updates JSON** (`devices.json`, `firmwares_live.json`, etc.) and **heals metadata** (fills missing `applied_to`, fixes many `UNKNOWN` labels from titles and release notes)
5. **Regenerates this README** and opens a **GitHub Release** when new binaries were downloaded

Firmware binaries are **not** stored in the git tree (too large). They appear as release assets, e.g.  
`https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/<filename>.zip`

### Optional priority models

To bump specific models to the **front of the queue** for one run (still only 10 downloads total, then the rest of the catalog as usual):

1. Copy `priority_models.json.example` → `priority_models.json`
2. Add model prefixes, e.g. `DS-2CD2387G3-LIS2UY`
3. Commit and push, or set env `PRIORITY_MODELS` in a workflow dispatch

With `"one_shot": true`, the file is cleared after a run that actually downloads new files.

**Download allowlist:** CI only downloads firmware for **`DS-2CD`** models by default (`DOWNLOAD_MODEL_PREFIXES=DS-2CD`). Set `DOWNLOAD_MODEL_PREFIXES=all` to re-enable other product lines later.

### Data files

| File | Purpose |
|------|---------|
| `devices.json` | Internal device IDs → model + hardware version |
| `firmwares_live.json` | Firmware scraped from Hikvision (main database) |
| `firmwares_manual.json` | Entries added by hand / PR |
| `firmware_info.json` | Extra metadata |
| `firmware_index.json` | Per-model firmware summary for integrations ([Home Assistant ISAPI](https://github.com/JoeyGE0/hikvision_isapi)): version, date, download URL, PDF notes, change summary |
| `status.json` | Last scraper run (status, counts, errors) |

### Local development

```bash
pip install -r requirements.txt
# Optional, for catalog fallback on blocked networks:
# pip install playwright && playwright install chromium

python main.py scrape          # scrape + regenerate README
python main.py scrape -g       # same; prints new count for CI
python -m unittest test_metadata_and_priority.py  # sanity checks
```

## Finding and downloading firmware

1. **Search this page** (Ctrl+F) for your exact model, e.g. `DS-2CD2387G3-LIS2UY`
2. Open the collapsible section for your **hardware version** (`IPC_G0`, `DVR_V4`, etc.)
3. Pick the **version / date** you need (newest listed first)
4. Use the **Download** link — usually our GitHub Release mirror

### Model prefixes (common)

- **DS-2CD**, **DS-2DE**, **DS-2DF** — cameras and PTZ
- **DS-76**, **DS-77**, **DS-86**, **DS-96** — recorders
- **DS-K** — door / access
- **AE-** — automotive / mobile DVR lines
- **IDS-** — industrial / special lines

### Hardware version

Check **Configuration → System → System Settings → Device Information** (wording varies). The value must match the archive row (e.g. `IPC_G0`). Wrong hardware + firmware combinations can brick a device.

### “Supported models” / Applied to

Many packages apply to several SKU variants. The table’s **Supported Models** column comes from Hikvision’s “Applied to:” text when we could parse it. If it shows `UNKNOWN`, the catalog row had no model string — open an issue with your model and a screenshot/link if you can.

## Important warnings

1. **Unofficial** — community mirror; no warranty
2. **Verify model and hardware** before flashing
3. **Backup configuration** before upgrade
4. **Stable power** during flash (UPS recommended)
5. **Regional / language builds** — filenames may include `Europe`, region codes, etc.
6. **Beta** entries are marked when detected in version/notes
7. Use **SADP**, **iVMS-4200**, or the device web UI as Hikvision documents; follow their license agreement

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for details.

**Quick options:**

- **Missing firmware** — open a GitHub issue with model, hardware version, firmware version, and a source URL if you have one
- **Add a link manually** — `python main.py add "<url>" --model DS-... --hw-version IPC_G0 --version 5.8.0`
- **Code** — improve `main.py` / `release.py`; run `python -m unittest test_metadata_and_priority.py` before opening a PR

**Do not edit the firmware table in `README.md` by hand** — edit `readme_header.md` in the repo or the JSON sources; CI regenerates the list.

## Automation status

| | |
|--|--|
| **Status** | {{STATUS}} |
| **Last run** | {{LAST_RUN}} |
| **Scraper** | {{SCRAPER_MODE}} |
| **Catalog fetch** | {{CATALOG_FETCH}} |
| **Catalog rows parsed** | {{CATALOG_ENTRIES}} |
| **Firmware records** | {{FIRMWARES_FOUND}} |
| **New last run** | {{NEW_FIRMWARES}} |
| **Test mode** | {{TEST_MODE}} |

{{ERRORS}}

---

## Firmware list

Collapsible sections per model and hardware line (newest firmware first within each section).

Total: 0
