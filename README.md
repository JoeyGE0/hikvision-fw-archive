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

### Data files

| File | Purpose |
|------|---------|
| `devices.json` | Internal device IDs → model + hardware version |
| `firmwares_live.json` | Firmware scraped from Hikvision (main database) |
| `firmwares_manual.json` | Entries added by hand / PR |
| `firmware_info.json` | Extra metadata |
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
| **Status** | ✅ SUCCESS |
| **Last run** | 2026-05-25 23:53:26 UTC |
| **Scraper** | HTTP |
| **Catalog fetch** | playwright |
| **Catalog rows parsed** | 864 |
| **Firmware records** | 230 |
| **New last run** | 10 |
| **Test mode** | Disabled |



---

## Firmware list

Collapsible sections per model and hardware line (newest firmware first within each section).

Total: 230



<details>
<summary><h2>AE-DC5113-F6S - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 1.2.8 | Applied to: [AE-DC5113-F6S](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779750762/Firmware__V1.2.8_260509_S3000723501.zip) | 2021-05-13 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779750762/Firmware__V1.2.8_260509_S3000723501.zip) | — |

</details>


<details>
<summary><h2>AE-DI5052-G40 PRO - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 4.7.5 | Applied to: [[[AE-DI5052-G40](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779186905/Firmware__V4.7.5_260409_S3000716981.zip)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779186905/Firmware__V4.7.5_260409_S3000716981.zip)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779186905/Firmware__V4.7.5_260409_S3000716981.zip) PRO, AE-DI5052-G40 PRO(EU), AE-DI5052-G40 PRO(US) | 2026-04-09 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779186905/Firmware__V4.7.5_260409_S3000716981.zip) | — |

</details>


<details>
<summary><h2>AE-MD5043-SD - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.1 | Applied to: [AE-MD5043-SD/GLF(EU-STD)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.8.11_260409_S3000714729.zip) | 2024-11-21 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.8.11_260409_S3000714729.zip) | — |

</details>


<details>
<summary><h2>AE-MH0408 - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.1 | Applied to: [AE-MH0408(1T)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.8.11_260409_S3000714729.zip)(RJ45) | 2024-11-21 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.8.11_260409_S3000714729.zip) | — |

</details>


<details>
<summary><h2>DS-2CD1043G2-LIUF/SL - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.41 | Applied to: [DS-2CD1043G2-LIUF/SL](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779302890/Firmware__V5.8.41_260401_S3000712602.zip), [DS-2CD1043G2-LIUF/SL(2.8MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779302890/Firmware__V5.8.41_260401_S3000712602.zip), [DS-2CD1043G2-LIUF/SL(4MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779302890/Firmware__V5.8.41_260401_S3000712602.zip), [DS-2CD1047G2H-LIU(F)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779302890/Firmware__V5.8.41_260401_S3000712602.zip), [[DS-2CD1047G2H-LIU(2.8MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779302890/Firmware__V5.8.41_260401_S3000712602.zip)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779302890/Firmware__V5.8.41_260401_S3000712602.zip)(BLACK), [DS-2CD1047G2H-LIUF(2.8MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779302890/Firmware__V5.8.41_260401_S3000712602.zip), [DS-2CD1047G2H-LIUF(4MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779302890/Firmware__V5.8.41_260401_S3000712602.zip), DS-2CD1047G2H-LIU(2.8MM) | 2026-04-01 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779302890/Firmware__V5.8.41_260401_S3000712602.zip) | 1. Fixed some bugs to enhance system stability. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202604/releasenote%5CNetwork_Camera-V5.8.41_SP1_Release_Note-E10.pdf) |

</details>


<details>
<summary><h2>DS-2CD1363G2P-LIUF - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.11 | Applied to: [DS-2CD1363G2P-LIUF/SL(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.8.11_260409_S3000714729.zip) | 2025-10-29 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.8.11_260409_S3000714729.zip) | — |

</details>


<details>
<summary><h2>DS-2CD1363G2P-LIUF/S(L)(RB) - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.12 | Applied to: [DS-2CD1363G2P-LIUF/S(L)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779174169/Firmware__V5.8.12_260416_S3000716513.zip)(RB), [DS-2CD1363G2P-LIUF/SL(2.8MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779174169/Firmware__V5.8.12_260416_S3000716513.zip), [DS-2CD1367G2HP-LIUF/S(L)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779174169/Firmware__V5.8.12_260416_S3000716513.zip)(RB), [DS-2CD1367G2HP-LIUF/SRB(2.8MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779174169/Firmware__V5.8.12_260416_S3000716513.zip), [DS-2CD1367G2HP-LIUF/SL(2.8MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779174169/Firmware__V5.8.12_260416_S3000716513.zip), [DS-2CD1383G2P-LIUF/S(L)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779174169/Firmware__V5.8.12_260416_S3000716513.zip)(RB), [DS-2CD1383G2P-LIUF/SRB(2MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779174169/Firmware__V5.8.12_260416_S3000716513.zip), [DS-2CD1383G2P-LIUF/SL(2MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779174169/Firmware__V5.8.12_260416_S3000716513.zip) | 2026-04-16 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779174169/Firmware__V5.8.12_260416_S3000716513.zip) | some bugs to enhance system stability. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202605/releasenote%5CNetwork_Camera-V5.8.12_260416_Release_IPCE_P_E11.pdf) |

</details>


<details>
<summary><h2>DS-2CD1367G2HP-LIUF - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.11 | Applied to: [DS-2CD1367G2HP-LIUF/SL(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.8.11_260409_S3000714729.zip) | 2025-10-29 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.8.11_260409_S3000714729.zip) | — |

</details>


<details>
<summary><h2>DS-2CD1383G2P-LIUF - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.11 | Applied to: [DS-2CD1383G2P-LIUF/SL(2mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.8.11_260409_S3000714729.zip) | 2025-10-29 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.8.11_260409_S3000714729.zip) | — |

</details>


<details>
<summary><h2>DS-2CD1T63G2P-LIUF - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.11 | Applied to: [DS-2CD1T63G2P-LIUF/SL(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.8.11_260409_S3000714729.zip) | 2025-10-29 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.8.11_260409_S3000714729.zip) | the screen flickering issue for 4G/WI-FI cameras · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202511/releasenote%5CNetwork_Camera-V5.8.11_SP1_251029_Release_Note-IPCE_P_E11.pdf) |

</details>


<details>
<summary><h2>DS-2CD1T67G2HP-LIUF - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.11 | Applied to: [DS-2CD1T67G2HP-LIUF/SRB(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.8.11_260409_S3000714729.zip) | 2025-10-29 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.8.11_260409_S3000714729.zip) | the screen flickering issue for 4G/WI-FI cameras · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202511/releasenote%5CNetwork_Camera-V5.8.11_SP1_251029_Release_Note-IPCE_P_E11.pdf) |

</details>


<details>
<summary><h2>DS-2CD1T83G2P-LIUF - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.11 | Applied to: [DS-2CD1T83G2P-LIUF/SL(2mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.8.11_260409_S3000714729.zip) | 2025-10-29 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.8.11_260409_S3000714729.zip) | the screen flickering issue for 4G/WI-FI cameras · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202511/releasenote%5CNetwork_Camera-V5.8.11_SP1_251029_Release_Note-IPCE_P_E11.pdf) |

</details>


<details>
<summary><h2>DS-2CD2023G2-I - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.0 | Applied to: [DS-2CD2023G2-I(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.7.0_260327_S3000711576.zip)(D) | 2024-10-23 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.7.0_260327_S3000711576.zip) | 1. Fix the issue of no Motion Detection alarms for the cameras with live guard. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202507/releasenote%5CNetwork_Camera-V5.7.0_SP6_Release_Note-G6_I.pdf) |

</details>


<details>
<summary><h2>DS-2CD2023G2-IU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.0 | Applied to: [DS-2CD2023G2-I(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.7.0_260327_S3000711576.zip)(D) | 2024-10-23 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.7.0_260327_S3000711576.zip) | 1. Fix the issue of no Motion Detection alarms for the cameras with live guard. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202507/releasenote%5CNetwork_Camera-V5.7.0_SP6_Release_Note-G6_I.pdf) |

</details>


<details>
<summary><h2>DS-2CD2026G2-I - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.0 | Applied to: [DS-2CD2026G2-I(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.7.0_260327_S3000711576.zip) | 2024-10-23 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.7.0_260327_S3000711576.zip) | Version maintenance of HC library permission authentication issues. · [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202408/releasenote%5CNetwork_Camera-V5.5.820_Release_Note-G3.pdf) |

</details>


<details>
<summary><h2>DS-2CD2026G2-I-U- - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.820 | Applied to: [DS-2CD2026G2-I-U-](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.7.0_260327_S3000711576.zip) | 2026-03-27 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.7.0_260327_S3000711576.zip) | Version maintenance of HC library permission authentication issues. · [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202408/releasenote%5CNetwork_Camera-V5.5.820_Release_Note-G3.pdf) |

</details>


<details>
<summary><h2>DS-2CD2046G3-IZ(2U)Y - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.32 | Applied to: [DS-2CD2046G3-IZ(2U)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779320667/Firmware__V5.8.32_260330_S3000710893.zip)Y, [DS-2CD2046G3-IZY(2.8/4MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779320667/Firmware__V5.8.32_260330_S3000710893.zip), [DS-2CD2046G3-IZ2UY(2.8/4MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779320667/Firmware__V5.8.32_260330_S3000710893.zip), [DS-2CD2046G3-IZ2UY/S(L)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779320667/Firmware__V5.8.32_260330_S3000710893.zip)(RB), [DS-2CD2046G3-IZ2UY/SRB(2.8/4)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779320667/Firmware__V5.8.32_260330_S3000710893.zip)O-STDBLACK, [DS-2CD2046G3-IZ2UY/SRB(2.8/4MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779320667/Firmware__V5.8.32_260330_S3000710893.zip), [[DS-2CD2046G3-IZ2UY/SL(2.8/4MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779320667/Firmware__V5.8.32_260330_S3000710893.zip)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779320667/Firmware__V5.8.32_260330_S3000710893.zip), DS-2CD2046G3-IZ2UY/SL(2.8/4MM)O-STDBLACK | 2026-03-30 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779320667/Firmware__V5.8.32_260330_S3000710893.zip) | New PT33 AI-ISP Camera Series · a) PTZ control is supported in the preview interface, with 16 preset points; patrol function and · motion tracking are available; one-click self-test is supported. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202604/releasenote%5CNetwork_Camera-V5.8.32_SP1_260330_Release_Note-H13U.pdf) |

</details>


<details>
<summary><h2>DS-2CD2087G3-LI(2U)Y - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.32 | Applied to: [DS-2CD2087G3-LI(2U)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779320667/Firmware__V5.8.32_260330_S3000710937.zip)Y, [DS-2CD2087G3-LI2UY(2.8MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779320667/Firmware__V5.8.32_260330_S3000710937.zip)(BLACK), [DS-2CD2087G3-LIY(2.8MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779320667/Firmware__V5.8.32_260330_S3000710937.zip), [DS-2CD2087G3-LIY(4MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779320667/Firmware__V5.8.32_260330_S3000710937.zip), [DS-2CD2167G3-LI(S2U)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779320667/Firmware__V5.8.32_260330_S3000710937.zip)Y, [[DS-2CD2167G3-LIS2UY(2.8MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779320667/Firmware__V5.8.32_260330_S3000710937.zip)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779320667/Firmware__V5.8.32_260330_S3000710937.zip), [DS-2CD2167G3-LIS2UY(4MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779320667/Firmware__V5.8.32_260330_S3000710937.zip), DS-2CD2167G3-LIS2UY(2.8MM)(BLACK) | 2026-03-30 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779320667/Firmware__V5.8.32_260330_S3000710937.zip) | 1. The 2 series products have added support for perimeter animals and non-motor vehicles. The · detection targets are set to animals and others by default. · 2. Add a master control switch（Device Linkage Control）for sound and flash alarm functions, · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202604/releasenote%5CNetwork_Camera-V5.8.32_SP1_260330_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD2123G2-I - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.0 | Applied to: [DS-2CD2123G2-I(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.7.0_260327_S3000711576.zip)(D)(BLACK) | 2024-10-23 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.7.0_260327_S3000711576.zip) | 1. Fix the issue of no Motion Detection alarms for the cameras with live guard. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202507/releasenote%5CNetwork_Camera-V5.7.0_SP6_Release_Note-G6_I.pdf) |

</details>


<details>
<summary><h2>DS-2CD2123G2-IU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.0 | Applied to: [DS-2CD2123G2-IU(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.7.0_260327_S3000711576.zip)(D) | 2024-10-23 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.7.0_260327_S3000711576.zip) | 1. Fix the issue of no Motion Detection alarms for the cameras with live guard. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202507/releasenote%5CNetwork_Camera-V5.7.0_SP6_Release_Note-G6_I.pdf) |

</details>


<details>
<summary><h2>DS-2CD2126G2-I - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.0 | Applied to: [DS-2CD2126G2-ISU(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.7.0_260327_S3000711576.zip)(C) | 2024-10-23 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.7.0_260327_S3000711576.zip) | 1. Change of capture mode for 6/8 MP camera：P system delet e 3200x180025, only reserved · 3840x216025, The N system remains unchanged. · 2. Newly Add 38 boxes camera: DS-2CD3843G2-AP2. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.19_241207_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD23127G3P-LIS2UY/S(L)(RB) - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.110 | Applied to: [DS-2CD23127G3P-LIS2UY/S(L)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1778673224/Firmware__V5.8.110_260421_S3000717992.zip)(RB), [[DS-2CD23127G3P-LIS2UY/SRB(180°)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1778673224/Firmware__V5.8.110_260421_S3000717992.zip)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1778673224/Firmware__V5.8.110_260421_S3000717992.zip), DS-2CD23127G3P-LIS2UY/SRB(180°)OSTDBLACK, [[DS-2CD23127G3P-LIS2UY/SL(180°)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1778673224/Firmware__V5.8.110_260421_S3000717992.zip)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1778673224/Firmware__V5.8.110_260421_S3000717992.zip)O-STDBLACK, DS-2CD23127G3P-LIS2UY/SL(180°), [DS-2CD23167G3P-LIS2UY/S(L)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1778673224/Firmware__V5.8.110_260421_S3000717992.zip)(RB), [DS-2CD23167G3P-LIS2UY/SRB(180°)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1778673224/Firmware__V5.8.110_260421_S3000717992.zip), [DS-2CD23167G3P-LIS2UY/SL(180°)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1778673224/Firmware__V5.8.110_260421_S3000717992.zip) | 2026-04-21 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1778673224/Firmware__V5.8.110_260421_S3000717992.zip) | — |

</details>


<details>
<summary><h2>DS-2CD2323G2-I - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.0 | Applied to: [DS-2CD2323G2-I(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.7.0_260327_S3000711576.zip)(D) | 2024-10-23 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.7.0_260327_S3000711576.zip) | 1. Fix the issue of no Motion Detection alarms for the cameras with live guard. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202507/releasenote%5CNetwork_Camera-V5.7.0_SP6_Release_Note-G6_I.pdf) |

</details>


<details>
<summary><h2>DS-2CD2323G2-IU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.0 | Applied to: [DS-2CD2323G2-I(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.7.0_260327_S3000711576.zip)(D) | 2024-10-23 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.7.0_260327_S3000711576.zip) | 1. Fix the issue of no Motion Detection alarms for the cameras with live guard. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202507/releasenote%5CNetwork_Camera-V5.7.0_SP6_Release_Note-G6_I.pdf) |

</details>


<details>
<summary><h2>DS-2CD2326G2-I - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.0 | Applied to: [DS-2CD2326G2-IU(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.7.0_260327_S3000711576.zip) | 2024-10-23 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.7.0_260327_S3000711576.zip) | 1. Improved Features  Fix security issue in ISAPI. · [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/330c4c2c-5730-4877-a942-0be87cea67ca.pdf) |

</details>


<details>
<summary><h2>DS-2CD2326G2-I-U- - IPC_G3 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.0 | Applied to: [DS-2CD2326G2-I-U-](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.7.0_260327_S3000711576.zip) | 2026-03-27 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.7.0_260327_S3000711576.zip) | 1. Improved Features  Fix security issue in ISAPI. · [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/330c4c2c-5730-4877-a942-0be87cea67ca.pdf) |
| 5.5.800 | Applied to: [DS-2CD2326G2-I-U-](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.7.0_260327_S3000711576.zip) | 2026-03-27 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.7.0_260327_S3000711576.zip) | 1. Improved Features  Fix security issue in ISAPI. · [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/330c4c2c-5730-4877-a942-0be87cea67ca.pdf) |

</details>


<details>
<summary><h2>DS-2CD2326G2-ISU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.0 | Applied to: [DS-2CD2326G2-ISU/SL(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.7.0_260327_S3000711576.zip)(D) | 2024-10-23 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.7.0_260327_S3000711576.zip) | 1. Fix the issue of no Motion Detection alarms for the cameras with live guard. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202507/releasenote%5CNetwork_Camera-V5.7.0_SP6_Release_Note-G6_I.pdf) |

</details>


<details>
<summary><h2>DS-2CD2343G2D-LIZ2UY - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.11 | Applied to: [DS-2CD2343G2D-LIZ2UY/SL(2.8/4mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.8.11_260409_S3000714729.zip) | 2025-12-16 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.8.11_260409_S3000714729.zip) | Fix the network abnormal issue. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.8.11_251216_Release_Note-IPCE_D_H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD2343G2P-LISU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.11 | Applied to: [DS-2CD2343G2P-LISU/SL(180°)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.8.11_260409_S3000714729.zip) | 2025-10-29 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.8.11_260409_S3000714729.zip) | the screen flickering issue for 4G/WI-FI cameras · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.8.11_SP1_251029_Release_Note-IPCE_P_E11.pdf) |

</details>


<details>
<summary><h2>DS-2CD2346G3D-IZ2UY - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.11 | Applied to: [DS-2CD2346G3D-IZ2UY/SRB(2.8/4)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.8.11_260409_S3000714729.zip)O-STDBLACK | 2025-12-16 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.8.11_260409_S3000714729.zip) | Fix the network abnormal issue. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.8.11_251216_Release_Note-IPCE_D_H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD2346G3D-IZ2UY-S-L--RB- - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.11 | Applied to: [DS-2CD2346G3D-IZ2UY-S-L--RB-](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.8.11_260409_S3000714729.zip) | 2026-03-26 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.8.11_260409_S3000714729.zip) | some bugs to enhance system stability. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202605/releasenote%5CNetwork_Camera-V5.8.11_260326_Release_IPCE_D_H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD2363G2P-LISU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.11 | Applied to: [DS-2CD2363G2P-LISU/SL(180°)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.8.11_260409_S3000714729.zip) | 2025-10-29 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.8.11_260409_S3000714729.zip) | the screen flickering issue for 4G/WI-FI cameras · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.8.11_SP1_251029_Release_Note-IPCE_P_E11.pdf) |

</details>


<details>
<summary><h2>DS-2CD2383G2P-LISU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.11 | Applied to: [DS-2CD2383G2P-LISU/SL(180°)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.8.11_260409_S3000714729.zip) | 2025-10-29 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.8.11_260409_S3000714729.zip) | the screen flickering issue for 4G/WI-FI cameras · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.8.11_SP1_251029_Release_Note-IPCE_P_E11.pdf) |

</details>


<details>
<summary><h2>DS-2CD2523G2-I - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.0 | Applied to: [DS-2CD2523G2-I(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.7.0_260327_S3000711576.zip)(D) | 2024-10-23 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.7.0_260327_S3000711576.zip) | 1. Fix the issue of no Motion Detection alarms for the cameras with live guard. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202507/releasenote%5CNetwork_Camera-V5.7.0_SP6_Release_Note-G6_I.pdf) |

</details>


<details>
<summary><h2>DS-2CD2523G2-IS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.0 | Applied to: [DS-2CD2523G2-I(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.7.0_260327_S3000711576.zip)(D) | 2024-10-23 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.7.0_260327_S3000711576.zip) | 1. Fix the issue of no Motion Detection alarms for the cameras with live guard. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202507/releasenote%5CNetwork_Camera-V5.7.0_SP6_Release_Note-G6_I.pdf) |

</details>


<details>
<summary><h2>DS-2CD2526G2-IS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.0 | Applied to: [DS-2CD2526G2-I(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.7.0_260327_S3000711576.zip)(D) | 2024-10-23 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.7.0_260327_S3000711576.zip) | 1. Fix the issue of no Motion Detection alarms for the cameras with live guard. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202507/releasenote%5CNetwork_Camera-V5.7.0_SP6_Release_Note-G6_I.pdf) |

</details>


<details>
<summary><h2>DS-2CD2623G2-IZS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.0 | Applied to: [DS-2CD2623G2-IZS(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.7.0_260327_S3000711576.zip)(US Branch) | 2024-10-23 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.7.0_260327_S3000711576.zip) | 1. New Products: 2 series Fixed-focus dual-light cameras: 2xx8G2. · 2. Motion Detection alarm of HC reflects human and vehicle attributes. · 1. 2/3 Series: Change the name of face capture in VCA Resource from Face Recognition to Face · [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202312/releasenote%5CNetwork_Camera-V5.7.13_Release_Note-G5.pdf) |

</details>


<details>
<summary><h2>DS-2CD2626G2-IZS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.0 | Applied to: [DS-2CD2626G2-IZS(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.7.0_260327_S3000711576.zip) | 2024-10-23 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.7.0_260327_S3000711576.zip) | Version maintenance of HC library permission authentication issues. · [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202408/releasenote%5CNetwork_Camera-V5.5.820_Release_Note-G3.pdf) |

</details>


<details>
<summary><h2>DS-2CD2626G2-IZSU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.0 | Applied to: [DS-2CD2626G2-IZSU/SL(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.7.0_260327_S3000711576.zip) | 2024-10-23 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.7.0_260327_S3000711576.zip) | Version maintenance of HC library permission authentication issues. · [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202408/releasenote%5CNetwork_Camera-V5.5.820_Release_Note-G3.pdf) |

</details>


<details>
<summary><h2>DS-2CD2626G2T-IZS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.0 | Applied to: [DS-2CD2626G2T-IZS(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.7.0_260327_S3000711576.zip)(D) | 2024-10-23 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.7.0_260327_S3000711576.zip) | 1. Fix the issue of no Motion Detection alarms for the cameras with live guard. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202507/releasenote%5CNetwork_Camera-V5.7.0_SP6_Release_Note-G6_I.pdf) |

</details>


<details>
<summary><h2>DS-2CD2647G3-LIZS2UY/S(L)(RB) - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.32 | Applied to: [DS-2CD2647G3-LIZS2UY/S(L)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779750762/Firmware__V5.8.32_260423_S3000719136.zip)(RB), [DS-2CD2647G3-LIZS2UY/SRB(2.8-12MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779750762/Firmware__V5.8.32_260423_S3000719136.zip)/O-STD, [DS-2CD2647G3-LIZS2UY/SRB(2.8-12)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779750762/Firmware__V5.8.32_260423_S3000719136.zip)O-STDBLK, [[DS-2CD2647G3-LIZS2UY/SL(2.8-12MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779750762/Firmware__V5.8.32_260423_S3000719136.zip)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779750762/Firmware__V5.8.32_260423_S3000719136.zip)OSTDBLK, DS-2CD2647G3-LIZS2UY/SL(2.8-12MM), [DS-2CD2647G3-LIZSY](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779750762/Firmware__V5.8.32_260423_S3000719136.zip), [[DS-2CD2647G3-LIZSY(2.8-12MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779750762/Firmware__V5.8.32_260423_S3000719136.zip)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779750762/Firmware__V5.8.32_260423_S3000719136.zip), DS-2CD2647G3-LIZSY(2.8-12MM)/O-STD/BLACK | 2026-04-23 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779750762/Firmware__V5.8.32_260423_S3000719136.zip) | — |

</details>


<details>
<summary><h2>DS-2CD2723G2-IZS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.0 | Applied to: [DS-2CD2723G2-IZS(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.7.0_260327_S3000711576.zip)(D) | 2024-10-23 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.7.0_260327_S3000711576.zip) | 1. Fix the issue of no Motion Detection alarms for the cameras with live guard. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202507/releasenote%5CNetwork_Camera-V5.7.0_SP6_Release_Note-G6_I.pdf) |

</details>


<details>
<summary><h2>DS-2CD2726G2-IZS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.0 | Applied to: [DS-2CD2726G2-IZS(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.7.0_260327_S3000711576.zip) | 2024-10-23 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.7.0_260327_S3000711576.zip) | Version maintenance of HC library permission authentication issues. · [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202408/releasenote%5CNetwork_Camera-V5.5.820_Release_Note-G3.pdf) |

</details>


<details>
<summary><h2>DS-2CD2726G2T-IZS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.0 | Applied to: [DS-2CD2726G2T-IZS(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.7.0_260327_S3000711576.zip)(D) | 2024-10-23 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.7.0_260327_S3000711576.zip) | 1. Fix the issue of no Motion Detection alarms for the cameras with live guard. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202507/releasenote%5CNetwork_Camera-V5.7.0_SP6_Release_Note-G6_I.pdf) |

</details>


<details>
<summary><h2>DS-2CD2D25G1-D/NF - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.210 | Applied to: [DS-2CD2D25G1-D/NF](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779302890/Firmware__V5.7.210_260402_S3000713526.zip), [DS-2CD2D25G1-D/NF(2.8MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779302890/Firmware__V5.7.210_260402_S3000713526.zip), [DS-2CD2D25G1-D/NF(3.7MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779302890/Firmware__V5.7.210_260402_S3000713526.zip), [DS-2CD2D45G1/M-D/NF](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779302890/Firmware__V5.7.210_260402_S3000713526.zip), [DS-2CD2D45G1/M-D/NF(2.8MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779302890/Firmware__V5.7.210_260402_S3000713526.zip), [DS-2CD2D45G1/M-D/NF(4MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779302890/Firmware__V5.7.210_260402_S3000713526.zip), [DS-2CD6425G1-XX](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779302890/Firmware__V5.7.210_260402_S3000713526.zip), [DS-2CD6425G1-10(3.7MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779302890/Firmware__V5.7.210_260402_S3000713526.zip)2M | 2026-04-02 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779302890/Firmware__V5.7.210_260402_S3000713526.zip) | — |

</details>


<details>
<summary><h2>DS-2CD2T23G2-2I - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.0 | Applied to: [DS-2CD2T23G2-2I(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.7.0_260327_S3000711576.zip)(D) | 2024-10-23 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.7.0_260327_S3000711576.zip) | 1. Fix the issue of no Motion Detection alarms for the cameras with live guard. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202507/releasenote%5CNetwork_Camera-V5.7.0_SP6_Release_Note-G6_I.pdf) |

</details>


<details>
<summary><h2>DS-2CD2T26G2-2I - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.0 | Applied to: [DS-2CD2T26G2-4I(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.7.0_260327_S3000711576.zip) | 2024-10-23 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.7.0_260327_S3000711576.zip) | Version maintenance of HC library permission authentication issues. · [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202408/releasenote%5CNetwork_Camera-V5.5.820_Release_Note-G3.pdf) |

</details>


<details>
<summary><h2>DS-2CD2T26G2-ISU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.0 | Applied to: [DS-2CD2T26G2-ISU/SL(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.7.0_260327_S3000711576.zip) | 2024-10-23 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.7.0_260327_S3000711576.zip) | 1. Improved Features  Fix security issue in ISAPI. · [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/330c4c2c-5730-4877-a942-0be87cea67ca.pdf) |

</details>


<details>
<summary><h2>DS-2CD2T43G2P-LISU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.11 | Applied to: [DS-2CD2T43G2P-LISU/SL(180°)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.8.11_260409_S3000714729.zip) | 2025-10-29 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.8.11_260409_S3000714729.zip) | the screen flickering issue for 4G/WI-FI cameras · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.8.11_SP1_251029_Release_Note-IPCE_P_E11.pdf) |

</details>


<details>
<summary><h2>DS-2CD2T63G2P-LISU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.11 | Applied to: [DS-2CD2T63G2P-LISU/SL(180°)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.8.11_260409_S3000714729.zip) | 2025-10-29 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.8.11_260409_S3000714729.zip) | the screen flickering issue for 4G/WI-FI cameras · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.8.11_SP1_251029_Release_Note-IPCE_P_E11.pdf) |

</details>


<details>
<summary><h2>DS-2CD2T83G2P-LISU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.11 | Applied to: [DS-2CD2T83G2P-LISU/SL(180°)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.8.11_260409_S3000714729.zip) | 2025-10-29 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.8.11_260409_S3000714729.zip) | the screen flickering issue for 4G/WI-FI cameras · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.8.11_SP1_251029_Release_Note-IPCE_P_E11.pdf) |

</details>


<details>
<summary><h2>DS-2CD3186G3-LISU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.11 | Applied to: [DS-2CD3186G3-LISUY(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.8.11_260409_S3000714729.zip)(eF) | 2025-10-22 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.8.11_260409_S3000714729.zip) | 1. New products: 3 series PTRZ camera, 3X6(8)6G3(PTRZ), 3X6(8)7G3(PTRZ). · (1) Support independent or combined movement in P/T/R directions, supports speed adjustment in gears 1 -7, · and maintains consistent position before and after restart and upgrade. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD3343G2 - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.11 | Applied to: [DS-2CD3343G2/X2-LIZSUY/SL(2.8/4mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.8.11_260409_S3000714729.zip)O-STD | 2025-12-16 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.8.11_260409_S3000714729.zip) | Fix the network abnormal issue. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.8.11_251216_Release_Note-IPCE_D_H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD3343G2-X2-LIZSUY-SL - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.11 | Applied to: [DS-2CD3343G2-X2-LIZSUY-SL](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.8.11_260409_S3000714729.zip) | 2026-03-26 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.8.11_260409_S3000714729.zip) | some bugs to enhance system stability. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202605/releasenote%5CNetwork_Camera-V5.8.11_260326_Release_IPCE_D_H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD3646G2T-LIDZSU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.1 | Applied to: [DS-2CD3646G2T-LIDZSU/4G/SL(2.7-13.5)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.8.11_260409_S3000714729.zip)OSTD | 2025-08-07 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.8.11_260409_S3000714729.zip) | 1. Supports EN18031 certification · 2. Supports acuseek · 3. Supports 4G · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202508/releasenote%5CNetwork_Camera-V5.8.1_250807_Release_Note-IPCE_HGL_G5.pdf) |

</details>


<details>
<summary><h2>DS-2CD3686G2T-LIDZSU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.1 | Applied to: [DS-2CD3686G2T-LIDZSU/4G/SL(2.7-13.5)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.8.11_260409_S3000714729.zip)OSTD | 2025-08-07 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.8.11_260409_S3000714729.zip) | 1. Supports EN18031 certification · 2. Supports acuseek · 3. Supports 4G · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202508/releasenote%5CNetwork_Camera-V5.8.1_250807_Release_Note-IPCE_HGL_G5.pdf) |

</details>


<details>
<summary><h2>DS-2CD3A26G2T-IZS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.0 | Applied to: [DS-2CD3A26G2T-IZS(4.7-71mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.7.0_260327_S3000711576.zip) | 2023-06-27 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.7.0_260327_S3000711576.zip) | 1. Fix EZVIZ library permission authentication issue · The camera uses a ZD25 electric lens. In scenes with a large depth of field, due to the problem of infrared non · confocal, the camera may refocus on the foreground/background, resulting in a change in the desired focus · [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202408/releasenote%5CNetwork_Camera-V5.7.0_SP2_Release_Note-IPCE_LZ_H8_230627.pdf) |

</details>


<details>
<summary><h2>DS-2CD3T46G2-LIDSU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.1 | Applied to: [DS-2CD3T46G2-LIDSU/4G/SL(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.8.11_260409_S3000714729.zip) | 2025-08-07 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.8.11_260409_S3000714729.zip) | 1. Supports EN18031 certification · 2. Supports acuseek · 3. Supports 4G · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202508/releasenote%5CNetwork_Camera-V5.8.1_250807_Release_Note-IPCE_HGL_G5.pdf) |

</details>


<details>
<summary><h2>DS-2CD3T86G2-LIDSU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.1 | Applied to: [DS-2CD3T86G2-LIDSU/4G/SL(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.8.11_260409_S3000714729.zip) | 2025-08-07 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.8.11_260409_S3000714729.zip) | 1. Supports EN18031 certification · 2. Supports acuseek · 3. Supports 4G · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202508/releasenote%5CNetwork_Camera-V5.8.1_250807_Release_Note-IPCE_HGL_G5.pdf) |

</details>


<details>
<summary><h2>DS-2CD6425G2-C1 - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.20 | Applied to: [DS-2CD6425G2-C1](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779302890/Firmware__V5.8.20_260402_S3000713059.zip), [DS-2CD6425G2-C2](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779302890/Firmware__V5.8.20_260402_S3000713059.zip), [DS-2CD6445G2-C1/HDMI](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779302890/Firmware__V5.8.20_260402_S3000713059.zip) | 2026-04-02 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779302890/Firmware__V5.8.20_260402_S3000713059.zip) | — |

</details>


<details>
<summary><h2>DS-2CD6924G0-IHS - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.1 | Applied to: [DS-2CD6924G0-IHS(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779750762/Firmware__V5.7.11_260506_S3000720327.zip)(C) | 2024-06-13 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779750762/Firmware__V5.7.11_260506_S3000720327.zip) | — |
| 5.7.0 | Applied to: [DS-2CD6924G0-IHS/NFC(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.7.0_260327_S3000711576.zip) | 2024-01-29 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.7.0_260327_S3000711576.zip) | New function · Fix the issue of no stream when using the ONVIF protocol to connect to third -party platforms after · restarting in panoramic multi-channel mode. · [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202312/releasenote%5CIPCP_H5_5.5.820_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD6944G0-IHS - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.1 | Applied to: [DS-2CD6944G0-IHS(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779750762/Firmware__V5.7.11_260506_S3000720327.zip)(C) | 2024-06-13 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779750762/Firmware__V5.7.11_260506_S3000720327.zip) | — |
| 5.7.0 | Applied to: [DS-2CD6944G0-IHS(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.7.0_260327_S3000711576.zip) | 2024-01-29 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.7.0_260327_S3000711576.zip) | New function · Fix the issue of no stream when using the ONVIF protocol to connect to third -party platforms after · restarting in panoramic multi-channel mode. · [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202312/releasenote%5CIPCP_H5_5.5.820_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD6944G1-IHS-U-Y - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.1 | Applied to: [DS-2CD6944G1-IHS-U-Y](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.8.11_260409_S3000714729.zip) | 2026-03-25 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.8.11_260409_S3000714729.zip) | — |

</details>


<details>
<summary><h2>DS-2CD6951G2-IS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.11 | Applied to: [DS-2CD6951G2-IS(2mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.8.11_260409_S3000714729.zip) | 2025-11-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.8.11_260409_S3000714729.zip) | Modified Features · Optimize product functionality · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CIPCG_PS_G5_Camera_V5.8.11_251114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD6984G0-IH - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.0 | Applied to: [DS-2CD6984G0-IHSAC/NFC(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.7.0_260327_S3000711576.zip) | 2024-01-29 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.7.0_260327_S3000711576.zip) | New function · Fix the issue of no stream when using the ONVIF protocol to connect to third -party platforms after · restarting in panoramic multi-channel mode. · [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202312/releasenote%5CIPCP_H5_5.5.820_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD6984G0-IHS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.0 | Applied to: [DS-2CD6984G0-IHS/NFC(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.7.0_260327_S3000711576.zip) | 2024-01-29 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.7.0_260327_S3000711576.zip) | 1. Improved Features  Fix security issue in ISAPI. · [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/b28e00a3-3d4d-405a-94e7-c3f287c0b839.pdf) |

</details>


<details>
<summary><h2>DS-2CD6984G1-IHS-U-Y--NFC- - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.1 | Applied to: [DS-2CD6984G1-IHS-U-Y--NFC-](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.8.11_260409_S3000714729.zip) | 2026-03-25 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.8.11_260409_S3000714729.zip) | — |

</details>


<details>
<summary><h2>DS-2CD6B35G0-PLW - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.12 | Applied to: [DS-2CD6B35G0-PLW](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1778212177/Firmware__V5.8.12_260414_S3000717550.zip), [DS-2CD6B35G0-PLW(4MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1778212177/Firmware__V5.8.12_260414_S3000717550.zip) | 2026-04-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1778212177/Firmware__V5.8.12_260414_S3000717550.zip) | — |

</details>


<details>
<summary><h2>DS-2CD6D42G0-IS - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.21 | Applied to: [DS-2CD6D42G0-IS](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.21_260402_S3000713101.zip), [DS-2CD6D42G0-IS(4MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.21_260402_S3000713101.zip), [DS-2CD6D42G0-IS(6MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.21_260402_S3000713101.zip) | 2026-04-02 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.21_260402_S3000713101.zip) | — |
| 5.8.11 | Applied to: [DS-2CD6D42G0-IS(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.8.11_260409_S3000714729.zip) | 2023-08-07 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.8.11_260409_S3000714729.zip) | 1. Release new model PanoVu camera DS-2CD6951G2-IS · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202508/releasenote%5CIPCG_PS_G5_Camera_V5.8.11_250730_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD6D44G1-IZS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.9.12 | Applied to: [DS-2CD6D44G1-IZS](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1777592712/Firmware__V5.9.12_260407_S3000713711.zip), [DS-2CD6D44G1-IZS(2.8-8MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1777592712/Firmware__V5.9.12_260407_S3000713711.zip), [DS-2CD6D44G1H-IZS](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1777592712/Firmware__V5.9.12_260407_S3000713711.zip), [DS-2CD6D44G1H-IZS(2.8-12MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1777592712/Firmware__V5.9.12_260407_S3000713711.zip) | 2026-04-07 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1777592712/Firmware__V5.9.12_260407_S3000713711.zip) | — |

</details>


<details>
<summary><h2>DS-2CD6D52G0-IH(S) - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.820 | Applied to: [DS-2CD6D52G0-IH(S)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779178727/Firmware__V5.5.820_260410_S3000715634.zip), [DS-2CD6D52G0-IHS(2.8MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779178727/Firmware__V5.5.820_260410_S3000715634.zip), [DS-2CD6D52G0-IH(2.8MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779178727/Firmware__V5.5.820_260410_S3000715634.zip), [DS-2CD6D52G0-IH(4MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779178727/Firmware__V5.5.820_260410_S3000715634.zip), [DS-2CD6D52G0-IH(6MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779178727/Firmware__V5.5.820_260410_S3000715634.zip), [DS-2CD6D52G0-IHS(4MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779178727/Firmware__V5.5.820_260410_S3000715634.zip), [DS-2CD6D52G0-IHS(6MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779178727/Firmware__V5.5.820_260410_S3000715634.zip), [DS-2CD6D82G0-IH(S)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779178727/Firmware__V5.5.820_260410_S3000715634.zip) | 2026-04-10 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779178727/Firmware__V5.5.820_260410_S3000715634.zip) | — |

</details>


<details>
<summary><h2>DS-2CFW02(/EU) - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.23 | Applied to: [DS-2CFW02(/EU)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779264543/Firmware__V5.8.23_260403_S3000712869.zip), [DS-2CFW02(2.8MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779264543/Firmware__V5.8.23_260403_S3000712869.zip), [DS-2CFW02(4MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779264543/Firmware__V5.8.23_260403_S3000712869.zip), [DS-2CV1023G2-LIDW(F)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779264543/Firmware__V5.8.23_260403_S3000712869.zip)(B), [DS-2CV1023G2-LIDWF(2.8MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779264543/Firmware__V5.8.23_260403_S3000712869.zip)(B), [DS-2CV1023G2-LIDWF(4MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779264543/Firmware__V5.8.23_260403_S3000712869.zip)(B), [DS-2CV1F23G2-LIDWF(B)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779264543/Firmware__V5.8.23_260403_S3000712869.zip), [DS-2CV1F23G2-LIDWF(2.8MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779264543/Firmware__V5.8.23_260403_S3000712869.zip)(B) | 2026-04-03 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779264543/Firmware__V5.8.23_260403_S3000712869.zip) | 1. Fixed some bugs to enhance system stability. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202605/releasenote%5CNetwork_Camera-V5.8.23_SP1_Release_Note-E9_E10.pdf) |

</details>


<details>
<summary><h2>DS-2CFW06-P - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.10 | Applied to: [DS-2CFW06-P](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.10_260330_S3000712753.zip), [DS-2CFW06-P(2.8MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.10_260330_S3000712753.zip) | 2026-03-30 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.10_260330_S3000712753.zip) | — |

</details>


<details>
<summary><h2>DS-2CFWQ3 - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.100 | Applied to: [DS-2CFWQ3](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779174169/Firmware__V5.8.100_260416_S3000716492.zip), [DS-2CFWQ3(2.8MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779174169/Firmware__V5.8.100_260416_S3000716492.zip), [DS-2CFWQ3(4MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779174169/Firmware__V5.8.100_260416_S3000716492.zip), [DS-2CFWQ5](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779174169/Firmware__V5.8.100_260416_S3000716492.zip), [DS-2CFWQ5(2.8MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779174169/Firmware__V5.8.100_260416_S3000716492.zip), [DS-2CFWQ5(4MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779174169/Firmware__V5.8.100_260416_S3000716492.zip), NKS4223WBTH, [DS-J142I](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779174169/Firmware__V5.8.100_260416_S3000716492.zip) | 2026-04-16 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779174169/Firmware__V5.8.100_260416_S3000716492.zip) | — |

</details>


<details>
<summary><h2>DS-2CFWQ6-D - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.110 | Applied to: [DS-2CFWQ6-D](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.110_260416_S3000716493.zip), [DS-2CFWQ6-D(2.8+4MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.110_260416_S3000716493.zip) | 2026-04-16 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.110_260416_S3000716493.zip) | — |

</details>


<details>
<summary><h2>DS-2DE2A204IW-DE3 - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.11 | Applied to: [DS-2DE2A204IW-DE3(C0)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779750762/Firmware__V5.7.11_260506_S3000720327.zip)(S6)(C) | 2023-06-12 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779750762/Firmware__V5.7.11_260506_S3000720327.zip) | - Fixed some known bugs, recommended upgrade · [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202312/releasenote%5CRelease_Note_E7_V5.7.11_230612.pdf) |

</details>


<details>
<summary><h2>DS-2DE2A204IWG1-E - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.9.5 | Applied to: [DS-2DE2A204IWG1-E](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.9.5_260420_S3000717076.zip), [DS-2DE2A404IWG1-E](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.9.5_260420_S3000717076.zip), [DS-2DE2A604IWG1-E](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.9.5_260420_S3000717076.zip) | 2026-04-20 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.9.5_260420_S3000717076.zip) | — |

</details>


<details>
<summary><h2>DS-2DE2A204IWG1-E/W - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.9.2 | Applied to: [DS-2DE2A204IWG1-E/W](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779174169/Firmware__V5.9.2_260416_S3000716258.zip), [DS-2DE2A404IWG1-E/W](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779174169/Firmware__V5.9.2_260416_S3000716258.zip), [DS-2DE2A604IWG1-E/W](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779174169/Firmware__V5.9.2_260416_S3000716258.zip) | 2026-04-16 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779174169/Firmware__V5.9.2_260416_S3000716258.zip) | 1. Algorithm optimization and updates. 2. Fix some bugs. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202604/releasenote%5CV5.9.2_260416_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2DE2A404IW-DE3 - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.11 | Applied to: [DS-2DE2A404IW-DE3(C0)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779750762/Firmware__V5.7.11_260506_S3000720327.zip)(S6)(C) | 2023-06-12 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779750762/Firmware__V5.7.11_260506_S3000720327.zip) | - Fixed some known bugs, recommended upgrade · [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202312/releasenote%5CRelease_Note_E7_V5.7.11_230612.pdf) |

</details>


<details>
<summary><h2>DS-2DE2C600MWG-E - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.1 | Applied to: [DS-2DE2C600MWG-E(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.8.11_260409_S3000714729.zip) | 2025-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.8.11_260409_S3000714729.zip) | 1. Algorithm optimization and updates. 2. Fix some bugs. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CV5.8.1_250114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2DE3204W-DE - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.1 | Applied to: [DS-2DE3204W-DE(T5)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.8.11_260409_S3000714729.zip) | 2023-11-08 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.8.11_260409_S3000714729.zip) | 1. Algorithm optimization and updates. 2. Fix some bugs. · [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202408/releasenote%5CIPDE_C_H8_V5.8.1_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2DE3A400BW-DE(T5) - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.0 | Applied to: [DS-2DE3A400BW-DE(T5)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779264543/Firmware__V5.8.0_260404_S3000716054.zip), [DS-2DE3A400BW-DE(F1)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779264543/Firmware__V5.8.0_260404_S3000716054.zip)(T5), [DS-2DE3A404IWG-E/W](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779264543/Firmware__V5.8.0_260404_S3000716054.zip), [DS-2DE4225WG-E3](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779264543/Firmware__V5.8.0_260404_S3000716054.zip), [DS-2DE4A225IWG-E](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779264543/Firmware__V5.8.0_260404_S3000716054.zip), [DS-2DE7A220MCG-EB](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779264543/Firmware__V5.8.0_260404_S3000716054.zip), [DS-2DE7A412MCG-EB](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779264543/Firmware__V5.8.0_260404_S3000716054.zip), [DS-2DE7A812MCG-EB](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779264543/Firmware__V5.8.0_260404_S3000716054.zip) | 2026-04-04 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779264543/Firmware__V5.8.0_260404_S3000716054.zip) | — |

</details>


<details>
<summary><h2>DS-2DE4215IW-DE - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.11 | Applied to: [DS-2DE4215IW-DE(S6)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779750762/Firmware__V5.7.11_260506_S3000720327.zip) | 2022-09-05 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779750762/Firmware__V5.7.11_260506_S3000720327.zip) | Modified Features · Support ezviz cloud online upgrade · Compatible with the new hardware modules: NL668-CN30 · [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202312/releasenote%5CV5.7.11_Release_Note--E7.pdf) |

</details>


<details>
<summary><h2>DS-2DE4215IWG1-E - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.1 | Applied to: [DS-2DE4215IWG1-E](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.8.11_260409_S3000714729.zip) | 2026-01-15 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.8.11_260409_S3000714729.zip) | 1. Add Tracking function to the 4 series 4MP PTZ camera.  Modify Features 1. Cybersecurity Compliance Remediation. 2. Update the SDK and PHY network interface controller. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202603/releasenote%5CV5.8.1_260115_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2DE4225IW-DE - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.11 | Applied to: [DS-2DE4225IW-DE(S6)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779750762/Firmware__V5.7.11_260506_S3000720327.zip) | 2022-09-05 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779750762/Firmware__V5.7.11_260506_S3000720327.zip) | Modified Features · Support ezviz cloud online upgrade · Compatible with the new hardware modules: NL668-CN30 · [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202312/releasenote%5CV5.7.11_Release_Note--E7.pdf) |

</details>


<details>
<summary><h2>DS-2DE4225IWG1-E - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.1 | Applied to: [DS-2DE4225IWG1-E](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.8.11_260409_S3000714729.zip) | 2026-01-15 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.8.11_260409_S3000714729.zip) | 1. Add Tracking function to the 4 series 4MP PTZ camera.  Modify Features 1. Cybersecurity Compliance Remediation. 2. Update the SDK and PHY network interface controller. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202603/releasenote%5CV5.8.1_260115_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2DE4225W-DE - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.11 | Applied to: [DS-2DE4225W-DE(S6)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779750762/Firmware__V5.7.11_260506_S3000720327.zip) | 2022-09-05 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779750762/Firmware__V5.7.11_260506_S3000720327.zip) | Modified Features · Support ezviz cloud online upgrade · Compatible with the new hardware modules: NL668-CN30 · [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202312/releasenote%5CV5.7.11_Release_Note--E7.pdf) |

</details>


<details>
<summary><h2>DS-2DE4225W-DE3 - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.11 | Applied to: [DS-2DE4225W-DE3(S6)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779750762/Firmware__V5.7.11_260506_S3000720327.zip) | 2022-09-05 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779750762/Firmware__V5.7.11_260506_S3000720327.zip) | Modified Features · Support ezviz cloud online upgrade · Compatible with the new hardware modules: NL668-CN30 · [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202312/releasenote%5CV5.7.11_Release_Note--E7.pdf) |

</details>


<details>
<summary><h2>DS-2DE4225WG1-E3 - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.1 | Applied to: [DS-2DE4225WG1-E3](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.8.11_260409_S3000714729.zip) | 2026-01-15 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.8.11_260409_S3000714729.zip) | 1. Add Tracking function to the 4 series 4MP PTZ camera.  Modify Features 1. Cybersecurity Compliance Remediation. 2. Update the SDK and PHY network interface controller. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202603/releasenote%5CV5.8.1_260115_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2DE4415IW-DE - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.11 | Applied to: [DS-2DE4415IW-DE(S6)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779750762/Firmware__V5.7.11_260506_S3000720327.zip) | 2022-09-05 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779750762/Firmware__V5.7.11_260506_S3000720327.zip) | Modified Features · Support ezviz cloud online upgrade · Compatible with the new hardware modules: NL668-CN30 · [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202312/releasenote%5CV5.7.11_Release_Note--E7.pdf) |

</details>


<details>
<summary><h2>DS-2DE4415IWG1-E - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.1 | Applied to: [DS-2DE4415IWG1-E](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.8.11_260409_S3000714729.zip) | 2026-01-15 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.8.11_260409_S3000714729.zip) | 1. Add Tracking function to the 4 series 4MP PTZ camera.  Modify Features 1. Cybersecurity Compliance Remediation. 2. Update the SDK and PHY network interface controller. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202603/releasenote%5CV5.8.1_260115_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2DE4425IW-DE - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.11 | Applied to: [DS-2DE4425IW-DE(S6)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779750762/Firmware__V5.7.11_260506_S3000720327.zip) | 2022-09-05 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779750762/Firmware__V5.7.11_260506_S3000720327.zip) | Modified Features · Support ezviz cloud online upgrade · Compatible with the new hardware modules: NL668-CN30 · [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202312/releasenote%5CV5.7.11_Release_Note--E7.pdf) |

</details>


<details>
<summary><h2>DS-2DE4425IWG1-E - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.1 | Applied to: [DS-2DE4425IWG1-E](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.8.11_260409_S3000714729.zip) | 2026-01-15 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.8.11_260409_S3000714729.zip) | 1. Add Tracking function to the 4 series 4MP PTZ camera.  Modify Features 1. Cybersecurity Compliance Remediation. 2. Update the SDK and PHY network interface controller. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202603/releasenote%5CV5.8.1_260115_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2DE4425W-DE - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.11 | Applied to: [DS-2DE4425W-DE(S6)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779750762/Firmware__V5.7.11_260506_S3000720327.zip) | 2022-09-05 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779750762/Firmware__V5.7.11_260506_S3000720327.zip) | Modified Features · Support ezviz cloud online upgrade · Compatible with the new hardware modules: NL668-CN30 · [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202312/releasenote%5CV5.7.11_Release_Note--E7.pdf) |

</details>


<details>
<summary><h2>DS-2DE4425W-DE3 - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.11 | Applied to: [DS-2DE4425W-DE3(S6)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779750762/Firmware__V5.7.11_260506_S3000720327.zip) | 2022-09-05 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779750762/Firmware__V5.7.11_260506_S3000720327.zip) | Modified Features · Support ezviz cloud online upgrade · Compatible with the new hardware modules: NL668-CN30 · [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202312/releasenote%5CV5.7.11_Release_Note--E7.pdf) |

</details>


<details>
<summary><h2>DS-2DE4425WG1-E3 - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.1 | Applied to: [DS-2DE4425WG1-E3](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.8.11_260409_S3000714729.zip) | 2026-01-15 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.8.11_260409_S3000714729.zip) | 1. Add Tracking function to the 4 series 4MP PTZ camera.  Modify Features 1. Cybersecurity Compliance Remediation. 2. Update the SDK and PHY network interface controller. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202603/releasenote%5CV5.8.1_260115_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2DE4825IWG1-E - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.1 | Applied to: [DS-2DE4825IWG1-E](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.8.11_260409_S3000714729.zip) | 2026-01-15 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.8.11_260409_S3000714729.zip) | 1. Add Tracking function to the 4 series 4MP PTZ camera.  Modify Features 1. Cybersecurity Compliance Remediation. 2. Update the SDK and PHY network interface controller. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202603/releasenote%5CV5.8.1_260115_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2DE4A225IW-DE - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.11 | Applied to: [DS-2DE4A225IW-DE(S6)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779750762/Firmware__V5.7.11_260506_S3000720327.zip) | 2023-06-12 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779750762/Firmware__V5.7.11_260506_S3000720327.zip) | - Fixed some known bugs, recommended upgrade · [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202312/releasenote%5CRelease_Note_E7_V5.7.11_230612.pdf) |

</details>


<details>
<summary><h2>DS-2DE4A225IWG1-E - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.1 | Applied to: [DS-2DE4A225IWG1-E](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.8.11_260409_S3000714729.zip) | 2026-01-15 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.8.11_260409_S3000714729.zip) | 1. Add Tracking function to the 4 series 4MP PTZ camera.  Modify Features 1. Cybersecurity Compliance Remediation. 2. Update the SDK and PHY network interface controller. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202603/releasenote%5CV5.8.1_260115_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2DE4A425IW-DE - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.11 | Applied to: [DS-2DE4A425IW-DE(S6)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779750762/Firmware__V5.7.11_260506_S3000720327.zip) | 2023-06-12 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779750762/Firmware__V5.7.11_260506_S3000720327.zip) | - Fixed some known bugs, recommended upgrade · [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202312/releasenote%5CRelease_Note_E7_V5.7.11_230612.pdf) |

</details>


<details>
<summary><h2>DS-2DE4A425IWG1-E - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.1 | Applied to: [DS-2DE4A425IWG1-E](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.8.11_260409_S3000714729.zip) | 2026-01-15 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.8.11_260409_S3000714729.zip) | 1. Add Tracking function to the 4 series 4MP PTZ camera.  Modify Features 1. Cybersecurity Compliance Remediation. 2. Update the SDK and PHY network interface controller. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202603/releasenote%5CV5.8.1_260115_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2DE5225IW-AE - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.11 | Applied to: [DS-2DE5225IW-AE(S6)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779750762/Firmware__V5.7.11_260506_S3000720327.zip) | 2023-06-12 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779750762/Firmware__V5.7.11_260506_S3000720327.zip) | - Fixed some known bugs, recommended upgrade · [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202312/releasenote%5CRelease_Note_E7_V5.7.11_230612.pdf) |

</details>


<details>
<summary><h2>DS-2DE5232IW-AE - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.11 | Applied to: [DS-2DE5232IW-AE(S6)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779750762/Firmware__V5.7.11_260506_S3000720327.zip) | 2023-06-12 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779750762/Firmware__V5.7.11_260506_S3000720327.zip) | - Fixed some known bugs, recommended upgrade · [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202312/releasenote%5CRelease_Note_E7_V5.7.11_230612.pdf) |

</details>


<details>
<summary><h2>DS-2DE5232W-AE - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.11 | Applied to: [DS-2DE5232W-AE(S6)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779750762/Firmware__V5.7.11_260506_S3000720327.zip) | 2023-06-12 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779750762/Firmware__V5.7.11_260506_S3000720327.zip) | - Fixed some known bugs, recommended upgrade · [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202312/releasenote%5CRelease_Note_E7_V5.7.11_230612.pdf) |

</details>


<details>
<summary><h2>DS-2DE5425IW-AE - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.11 | Applied to: [DS-2DE5425IW-AE(S6)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779750762/Firmware__V5.7.11_260506_S3000720327.zip) | 2023-06-12 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779750762/Firmware__V5.7.11_260506_S3000720327.zip) | - Fixed some known bugs, recommended upgrade · [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202312/releasenote%5CRelease_Note_E7_V5.7.11_230612.pdf) |

</details>


<details>
<summary><h2>DS-2DE5425IWG1-E - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.1 | Applied to: [DS-2DE5425IWG1-E](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.8.11_260409_S3000714729.zip) | 2026-01-15 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.8.11_260409_S3000714729.zip) | 1. Add Tracking function to the 4 series 4MP PTZ camera.  Modify Features 1. Cybersecurity Compliance Remediation. 2. Update the SDK and PHY network interface controller. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202603/releasenote%5CV5.8.1_260115_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2DE5425WG1-E - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.1 | Applied to: [DS-2DE5425WG1-E](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.8.11_260409_S3000714729.zip) | 2026-01-15 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.8.11_260409_S3000714729.zip) | 1. Add Tracking function to the 4 series 4MP PTZ camera.  Modify Features 1. Cybersecurity Compliance Remediation. 2. Update the SDK and PHY network interface controller. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202603/releasenote%5CV5.8.1_260115_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2DE5432IWG1-E - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.1 | Applied to: [DS-2DE5432IWG1-E](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.8.11_260409_S3000714729.zip) | 2026-01-15 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.8.11_260409_S3000714729.zip) | 1. Add Tracking function to the 4 series 4MP PTZ camera.  Modify Features 1. Cybersecurity Compliance Remediation. 2. Update the SDK and PHY network interface controller. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202603/releasenote%5CV5.8.1_260115_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2DE5432WG1-E - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.1 | Applied to: [DS-2DE5432WG1-E](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.8.11_260409_S3000714729.zip) | 2026-01-15 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.8.11_260409_S3000714729.zip) | 1. Add Tracking function to the 4 series 4MP PTZ camera.  Modify Features 1. Cybersecurity Compliance Remediation. 2. Update the SDK and PHY network interface controller. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202603/releasenote%5CV5.8.1_260115_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2DE7225IW-AE - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.11 | Applied to: [DS-2DE7225IW-AE(S6)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779750762/Firmware__V5.7.11_260506_S3000720327.zip) | 2022-09-05 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779750762/Firmware__V5.7.11_260506_S3000720327.zip) | Modified Features · Support ezviz cloud online upgrade · Compatible with the new hardware modules: NL668-CN30 · [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202312/releasenote%5CV5.7.11_Release_Note--E7.pdf) |

</details>


<details>
<summary><h2>DS-2DE7A225IWG-EB/SL - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.13 | Applied to: [DS-2DE7A225IWG-EB/SL](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.13_260422_S3000719553.zip), [DS-2DE7A232IWG-EB/SL](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.13_260422_S3000719553.zip) | 2026-04-22 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.13_260422_S3000719553.zip) | — |

</details>


<details>
<summary><h2>DS-2DF4220-DX(S6/316L) - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.11 | Applied to: [[DS-2DF4220-DX(S6/316L)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779178727/Firmware__V5.7.11_260413_S3000716685.zip)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779178727/Firmware__V5.7.11_260413_S3000716685.zip), DS-2DF4220-DX(S6/316L)(C), [[DS-2DF4420-DX(S6)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779178727/Firmware__V5.7.11_260413_S3000716685.zip)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779178727/Firmware__V5.7.11_260413_S3000716685.zip)(C)(304), DS-2DF4420-DX(S6)(C), [DS-2DF4420-DX(S6/316L)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779178727/Firmware__V5.7.11_260413_S3000716685.zip)(C), [DS-2DF4420WG-XEY](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779178727/Firmware__V5.7.11_260413_S3000716685.zip) | 2026-04-13 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779178727/Firmware__V5.7.11_260413_S3000716685.zip) | — |

</details>


<details>
<summary><h2>DS-2DF4220-DX-S6-316L- - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.11 | Applied to: [DS-2DF4220-DX-S6-316L-](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779750762/Firmware__V5.7.11_260506_S3000720327.zip) | 2026-04-13 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779750762/Firmware__V5.7.11_260506_S3000720327.zip) | — |

</details>


<details>
<summary><h2>DS-2DF4220-DX-S6-316L--C- - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.11 | Applied to: [DS-2DF4220-DX-S6-316L--C-](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779750762/Firmware__V5.7.11_260506_S3000720327.zip) | 2026-04-13 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779750762/Firmware__V5.7.11_260506_S3000720327.zip) | — |

</details>


<details>
<summary><h2>DS-2DF4420-DX(304)(E) - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.9.3 | Applied to: [DS-2DF4420-DX(304)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779174169/Firmware__V5.9.3_260417_S3000717323.zip)(E), [DS-2DF4420-DX(316L)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779174169/Firmware__V5.9.3_260417_S3000717323.zip)(E), [DS-2DF4420WG-XEY(ADC)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779174169/Firmware__V5.9.3_260417_S3000717323.zip)(E) | 2026-04-17 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779174169/Firmware__V5.9.3_260417_S3000717323.zip) | — |

</details>


<details>
<summary><h2>DS-2DF4420-DX-S6--C--304- - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.11 | Applied to: [DS-2DF4420-DX-S6--C--304-](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779750762/Firmware__V5.7.11_260506_S3000720327.zip) | 2026-04-13 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779750762/Firmware__V5.7.11_260506_S3000720327.zip) | — |

</details>


<details>
<summary><h2>DS-2DF4420-DX-S6-316L--C- - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.11 | Applied to: [DS-2DF4420-DX-S6-316L--C-](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779750762/Firmware__V5.7.11_260506_S3000720327.zip) | 2026-04-13 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779750762/Firmware__V5.7.11_260506_S3000720327.zip) | — |

</details>


<details>
<summary><h2>DS-2DF4420WG-XEY - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.11 | Applied to: [DS-2DF4420WG-XEY](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779750762/Firmware__V5.7.11_260506_S3000720327.zip) | 2026-04-13 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779750762/Firmware__V5.7.11_260506_S3000720327.zip) | — |

</details>


<details>
<summary><h2>DS-2DF6223-CX(T5/316L) - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.7 | Applied to: [DS-2DF6223-CX(T5/316L)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779178727/Firmware__V5.7.7_260410_S3000716682.zip), [DS-2DF6231-CX(T5/316L)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779178727/Firmware__V5.7.7_260410_S3000716682.zip), [DS-2DF6C431-CX(T5/316L)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779178727/Firmware__V5.7.7_260410_S3000716682.zip), [DS-2DF8432IWG-CXF(316L)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779178727/Firmware__V5.7.7_260410_S3000716682.zip) | 2026-04-10 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779178727/Firmware__V5.7.7_260410_S3000716682.zip) | — |

</details>


<details>
<summary><h2>DS-2DF7C432MXG1-(W)R - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.9.60 | Applied to: [[DS-2DF7C432MXG1-(W)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779264543/Firmware__V5.9.60_260403_S3000716051.zip)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779264543/Firmware__V5.9.60_260403_S3000716051.zip)R, [DS-2DF7C432MXG1-R](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779264543/Firmware__V5.9.60_260403_S3000716051.zip), [DS-2DF7C432MXG1-WR](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779264543/Firmware__V5.9.60_260403_S3000716051.zip), DS-2DF7C432MXG1-(W)R/4G, [DS-2DF7C432MXG1-WR/4G](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779264543/Firmware__V5.9.60_260403_S3000716051.zip), [DS-2DF7C432MXG1-WR/4G(LA)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779264543/Firmware__V5.9.60_260403_S3000716051.zip), [DS-2DF7C432MXG1-R/4G](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779264543/Firmware__V5.9.60_260403_S3000716051.zip), [DS-2DF7C432MXG1-R/4G(LA)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779264543/Firmware__V5.9.60_260403_S3000716051.zip) | 2026-04-03 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779264543/Firmware__V5.9.60_260403_S3000716051.zip) | — |

</details>


<details>
<summary><h2>DS-2DT5432MWG-T (PA) - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.63 | Applied to: [DS-2DT5432MWG-T](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779186905/Firmware__V5.7.63_260409_S3000714667.zip) (PA), [DS-2DT5432MWG-T(PA)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779186905/Firmware__V5.7.63_260409_S3000714667.zip) | 2026-04-09 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779186905/Firmware__V5.7.63_260409_S3000714667.zip) | — |

</details>


<details>
<summary><h2>DS-2DT5432MWG-T/4G (PA) - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.63 | Applied to: [DS-2DT5432MWG-T/4G](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779302890/Firmware__V5.7.63_260402_S3000712819.zip) (PA), [DS-2DT5432MWG-T/4G(PA)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779302890/Firmware__V5.7.63_260402_S3000712819.zip) | 2026-04-02 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779302890/Firmware__V5.7.63_260402_S3000712819.zip) | — |

</details>


<details>
<summary><h2>DS-2DY5225IX-AE(T5) - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.2 | Applied to: [DS-2DY5225IX-AE(T5)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779186905/Firmware__V5.8.2_260408_S3000715172.zip), [DS-2DY5225IX-DM(T5)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779186905/Firmware__V5.8.2_260408_S3000715172.zip), [DS-2DY5425IXG-E](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779186905/Firmware__V5.8.2_260408_S3000715172.zip), [DS-2DY5432IXG-E](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779186905/Firmware__V5.8.2_260408_S3000715172.zip), [DS-2DY5432IXG-M](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779186905/Firmware__V5.8.2_260408_S3000715172.zip), [DS-2DY5440IXG-E](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779186905/Firmware__V5.8.2_260408_S3000715172.zip) | 2026-04-08 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779186905/Firmware__V5.8.2_260408_S3000715172.zip) | — |

</details>


<details>
<summary><h2>DS-2DY7236IX-A(T5) - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.7 | Applied to: [DS-2DY7236IX-A(T5)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779186905/Firmware__V5.7.7_260409_S3000715198.zip), [DS-2DY9240IX-A(T5)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779186905/Firmware__V5.7.7_260409_S3000715198.zip), [DS-2DY9250IAX-A(T5)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779186905/Firmware__V5.7.7_260409_S3000715198.zip), [DS-2DY9250X-A(T5)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779186905/Firmware__V5.7.7_260409_S3000715198.zip) | 2026-04-09 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779186905/Firmware__V5.7.7_260409_S3000715198.zip) | — |

</details>


<details>
<summary><h2>DS-2DY7432IXG-XY - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.2 | Applied to: [DS-2DY7432IXG-XY](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779216345/Firmware__V5.8.2_260408_S3000715189.zip), [[[DS-2DY7436IXG-CXLWF(316L)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779216345/Firmware__V5.8.2_260408_S3000715189.zip)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779216345/Firmware__V5.8.2_260408_S3000715189.zip)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779216345/Firmware__V5.8.2_260408_S3000715189.zip), DS-2DY7436IXG-CXLWF(316L)5M, DS-2DY7436IXG-CXLWF(316L)10M, [[[DS-2DY7845IXG-CXLWF(316L)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779216345/Firmware__V5.8.2_260408_S3000715189.zip)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779216345/Firmware__V5.8.2_260408_S3000715189.zip)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779216345/Firmware__V5.8.2_260408_S3000715189.zip), DS-2DY7845IXG-CXLWF(316L)10M, DS-2DY7845IXG-CXLWF(316L)5M, [DS-2DY9236I-CWX(T5/316L)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779216345/Firmware__V5.8.2_260408_S3000715189.zip) | 2026-04-08 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779216345/Firmware__V5.8.2_260408_S3000715189.zip) | — |

</details>


<details>
<summary><h2>DS-2SE7C432IWG-4G/14(F0) - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.4 | Applied to: [[[DS-2SE7C432IWG-4G/14(F0)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779216345/Firmware__V5.8.4_260407_S3000716241.zip)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779216345/Firmware__V5.8.4_260407_S3000716241.zip)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779216345/Firmware__V5.8.4_260407_S3000716241.zip), DS-2SE7C432IWG-4G/14(F0)(LA), DS-2SE7C432IWG-4G/14(F0)(JP) | 2026-04-07 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779216345/Firmware__V5.8.4_260407_S3000716241.zip) | — |

</details>


<details>
<summary><h2>DS-2ST4C420MWG-E/14(PA) - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.9.62 | Applied to: [[DS-2ST4C420MWG-E/14(PA)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779174169/Firmware__V5.9.62_260416_S3000716213.zip)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779174169/Firmware__V5.9.62_260416_S3000716213.zip), DS-2ST4C420MWG-E/14(PA)(F1) | 2026-04-16 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779174169/Firmware__V5.9.62_260416_S3000716213.zip) | — |

</details>


<details>
<summary><h2>DS-2TD1217-2-QA - THERMAL_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.338 | Applied to: [DS-2TD1217-2-QA](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.5.338_260413_S3000716448.zip) | 2026-04-13 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.5.338_260413_S3000716448.zip) | 1.1 Issues fixes： 1) Fixed known software issues. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202605/releasenote%5CGeneral_Firmware_Update_Release_notes.pdf) |

</details>


<details>
<summary><h2>DS-2TD1217-2/QA - THERMAL_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.338 | Applied to: [DS-2TD1217-2/QA](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.5.338_260413_S3000716448.zip), [DS-2TD1217-3/QA](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.5.338_260413_S3000716448.zip), [DS-2TD1217-6/QA](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.5.338_260413_S3000716448.zip), [DS-2TD1228-2/QA](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.5.338_260413_S3000716448.zip), [DS-2TD1228-3/QA](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.5.338_260413_S3000716448.zip), [DS-2TD1228-7/QA](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.5.338_260413_S3000716448.zip), [DS-2TD1228T-2/QA](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.5.338_260413_S3000716448.zip), [DS-2TD1228T-2/QA(B)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.5.338_260413_S3000716448.zip) | 2026-04-13 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.5.338_260413_S3000716448.zip) | 1.1 Issues fixes： 1) Fixed known software issues. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202605/releasenote%5CGeneral_Firmware_Update_Release_notes.pdf) |

</details>


<details>
<summary><h2>DS-2TD1217-3-QA - THERMAL_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.338 | Applied to: [DS-2TD1217-3-QA](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.5.338_260413_S3000716448.zip) | 2026-04-13 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.5.338_260413_S3000716448.zip) | 1.1 Issues fixes： 1) Fixed known software issues. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202605/releasenote%5CGeneral_Firmware_Update_Release_notes.pdf) |

</details>


<details>
<summary><h2>DS-2TD1217-6-QA - THERMAL_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.338 | Applied to: [DS-2TD1217-6-QA](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.5.338_260413_S3000716448.zip) | 2026-04-13 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.5.338_260413_S3000716448.zip) | 1.1 Issues fixes： 1) Fixed known software issues. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202605/releasenote%5CGeneral_Firmware_Update_Release_notes.pdf) |

</details>


<details>
<summary><h2>DS-2TD1228-2-QA - THERMAL_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.338 | Applied to: [DS-2TD1228-2-QA](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.5.338_260413_S3000716448.zip) | 2026-04-13 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.5.338_260413_S3000716448.zip) | 1.1 Issues fixes： 1) Fixed known software issues. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202605/releasenote%5CGeneral_Firmware_Update_Release_notes.pdf) |

</details>


<details>
<summary><h2>DS-2TD1228-3-QA - THERMAL_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.338 | Applied to: [DS-2TD1228-3-QA](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.5.338_260413_S3000716448.zip) | 2026-04-13 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.5.338_260413_S3000716448.zip) | 1.1 Issues fixes： 1) Fixed known software issues. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202605/releasenote%5CGeneral_Firmware_Update_Release_notes.pdf) |

</details>


<details>
<summary><h2>DS-2TD1228-7-QA - THERMAL_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.338 | Applied to: [DS-2TD1228-7-QA](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.5.338_260413_S3000716448.zip) | 2026-04-13 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.5.338_260413_S3000716448.zip) | 1.1 Issues fixes： 1) Fixed known software issues. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202605/releasenote%5CGeneral_Firmware_Update_Release_notes.pdf) |

</details>


<details>
<summary><h2>DS-2TD1228T-2-QA - THERMAL_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.338 | Applied to: [DS-2TD1228T-2-QA](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.5.338_260413_S3000716448.zip) | 2026-04-13 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.5.338_260413_S3000716448.zip) | 1.1 Issues fixes： 1) Fixed known software issues. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202605/releasenote%5CGeneral_Firmware_Update_Release_notes.pdf) |

</details>


<details>
<summary><h2>DS-2TD1228T-2-QA-B- - THERMAL_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.338 | Applied to: [DS-2TD1228T-2-QA-B-](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.5.338_260413_S3000716448.zip) | 2026-04-13 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.5.338_260413_S3000716448.zip) | 1.1 Issues fixes： 1) Fixed known software issues. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202605/releasenote%5CGeneral_Firmware_Update_Release_notes.pdf) |

</details>


<details>
<summary><h2>DS-2TD1228T-3-QA - THERMAL_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.338 | Applied to: [DS-2TD1228T-3-QA](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.5.338_260413_S3000716448.zip) | 2026-04-13 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.5.338_260413_S3000716448.zip) | 1.1 Issues fixes： 1) Fixed known software issues. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202605/releasenote%5CGeneral_Firmware_Update_Release_notes.pdf) |

</details>


<details>
<summary><h2>DS-2TD1228T-3-QA-B- - THERMAL_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.338 | Applied to: [DS-2TD1228T-3-QA-B-](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.5.338_260413_S3000716448.zip) | 2026-04-13 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.5.338_260413_S3000716448.zip) | 1.1 Issues fixes： 1) Fixed known software issues. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202605/releasenote%5CGeneral_Firmware_Update_Release_notes.pdf) |

</details>


<details>
<summary><h2>DS-2TD2137T-4-QY0 - THERMAL_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.338 | Applied to: [DS-2TD2137T-4-QY0](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.5.338_260413_S3000716448.zip) | 2026-04-13 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.5.338_260413_S3000716448.zip) | 1.1 Issues fixes： 1) Fixed known software issues. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202605/releasenote%5CGeneral_Firmware_Update_Release_notes.pdf) |

</details>


<details>
<summary><h2>DS-2TD2137T-7-QY0 - THERMAL_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.338 | Applied to: [DS-2TD2137T-7-QY0](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.5.338_260413_S3000716448.zip) | 2026-04-13 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.5.338_260413_S3000716448.zip) | 1.1 Issues fixes： 1) Fixed known software issues. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202605/releasenote%5CGeneral_Firmware_Update_Release_notes.pdf) |

</details>


<details>
<summary><h2>DS-2TD2138-10-QY - THERMAL_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.338 | Applied to: [DS-2TD2138-10-QY](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.5.338_260413_S3000716448.zip) | 2026-04-13 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.5.338_260413_S3000716448.zip) | 1.1 Issues fixes： 1) Fixed known software issues. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202605/releasenote%5CGeneral_Firmware_Update_Release_notes.pdf) |

</details>


<details>
<summary><h2>DS-2TD2138-13-QY - THERMAL_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.338 | Applied to: [DS-2TD2138-13-QY](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.5.338_260413_S3000716448.zip) | 2026-04-13 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.5.338_260413_S3000716448.zip) | 1.1 Issues fixes： 1) Fixed known software issues. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202605/releasenote%5CGeneral_Firmware_Update_Release_notes.pdf) |

</details>


<details>
<summary><h2>DS-2TD2138-15-QY - THERMAL_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.338 | Applied to: [DS-2TD2138-15-QY](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.5.338_260413_S3000716448.zip) | 2026-04-13 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.5.338_260413_S3000716448.zip) | 1.1 Issues fixes： 1) Fixed known software issues. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202605/releasenote%5CGeneral_Firmware_Update_Release_notes.pdf) |

</details>


<details>
<summary><h2>DS-2TD2138-25-QY - THERMAL_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.338 | Applied to: [DS-2TD2138-25-QY](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.5.338_260413_S3000716448.zip) | 2026-04-13 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.5.338_260413_S3000716448.zip) | 1.1 Issues fixes： 1) Fixed known software issues. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202605/releasenote%5CGeneral_Firmware_Update_Release_notes.pdf) |

</details>


<details>
<summary><h2>DS-2TD2138-35-QY - THERMAL_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.338 | Applied to: [DS-2TD2138-35-QY](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.5.338_260413_S3000716448.zip) | 2026-04-13 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.5.338_260413_S3000716448.zip) | 1.1 Issues fixes： 1) Fixed known software issues. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202605/releasenote%5CGeneral_Firmware_Update_Release_notes.pdf) |

</details>


<details>
<summary><h2>DS-2TD2138-4-QY - THERMAL_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.338 | Applied to: [DS-2TD2138-4-QY](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.5.338_260413_S3000716448.zip) | 2026-04-13 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.5.338_260413_S3000716448.zip) | 1.1 Issues fixes： 1) Fixed known software issues. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202605/releasenote%5CGeneral_Firmware_Update_Release_notes.pdf) |

</details>


<details>
<summary><h2>DS-2TD2138-7-QY - THERMAL_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.338 | Applied to: [DS-2TD2138-7-QY](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.5.338_260413_S3000716448.zip) | 2026-04-13 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.5.338_260413_S3000716448.zip) | 1.1 Issues fixes： 1) Fixed known software issues. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202605/releasenote%5CGeneral_Firmware_Update_Release_notes.pdf) |

</details>


<details>
<summary><h2>DS-2TD2367-100-PY - THERMAL_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.98 | Applied to: [DS-2TD2367-100-PY](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779750762/Firmware__V5.5.98_260512_S3000723889.zip) | 2026-05-12 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779750762/Firmware__V5.5.98_260512_S3000723889.zip) | — |

</details>


<details>
<summary><h2>DS-2TD2367-100/PY - THERMAL_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.98 | Applied to: [DS-2TD2367-100/PY](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779750762/Firmware__V5.5.98_260512_S3000723889.zip), [DS-2TD2367-75/PY](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779750762/Firmware__V5.5.98_260512_S3000723889.zip) | 2026-05-12 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779750762/Firmware__V5.5.98_260512_S3000723889.zip) | — |

</details>


<details>
<summary><h2>DS-2TD2367-75-PY - THERMAL_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.98 | Applied to: [DS-2TD2367-75-PY](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779750762/Firmware__V5.5.98_260512_S3000723889.zip) | 2026-05-12 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779750762/Firmware__V5.5.98_260512_S3000723889.zip) | — |

</details>


<details>
<summary><h2>DS-2TD2528T-10-Q-C- - THERMAL_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.338 | Applied to: [DS-2TD2528T-10-Q-C-](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.5.338_260413_S3000716448.zip) | 2026-04-13 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.5.338_260413_S3000716448.zip) | 1.1 Issues fixes： 1) Fixed known software issues. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202605/releasenote%5CGeneral_Firmware_Update_Release_notes.pdf) |

</details>


<details>
<summary><h2>DS-2TD2528T-3-Q-C- - THERMAL_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.338 | Applied to: [DS-2TD2528T-3-Q-C-](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.5.338_260413_S3000716448.zip) | 2026-04-13 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.5.338_260413_S3000716448.zip) | 1.1 Issues fixes： 1) Fixed known software issues. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202605/releasenote%5CGeneral_Firmware_Update_Release_notes.pdf) |

</details>


<details>
<summary><h2>DS-2TD2528T-7-Q-C- - THERMAL_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.338 | Applied to: [DS-2TD2528T-7-Q-C-](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.5.338_260413_S3000716448.zip) | 2026-04-13 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.5.338_260413_S3000716448.zip) | 1.1 Issues fixes： 1) Fixed known software issues. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202605/releasenote%5CGeneral_Firmware_Update_Release_notes.pdf) |

</details>


<details>
<summary><h2>DS-2TD2537T-10-Q-C- - THERMAL_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.338 | Applied to: [DS-2TD2537T-10-Q-C-](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.5.338_260413_S3000716448.zip) | 2026-04-13 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.5.338_260413_S3000716448.zip) | 1.1 Issues fixes： 1) Fixed known software issues. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202605/releasenote%5CGeneral_Firmware_Update_Release_notes.pdf) |

</details>


<details>
<summary><h2>DS-2TD2537T-15-Q-C- - THERMAL_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.338 | Applied to: [DS-2TD2537T-15-Q-C-](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.5.338_260413_S3000716448.zip) | 2026-04-13 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.5.338_260413_S3000716448.zip) | 1.1 Issues fixes： 1) Fixed known software issues. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202605/releasenote%5CGeneral_Firmware_Update_Release_notes.pdf) |

</details>


<details>
<summary><h2>DS-2TD2537T-4-Q-C- - THERMAL_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.338 | Applied to: [DS-2TD2537T-4-Q-C-](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.5.338_260413_S3000716448.zip) | 2026-04-13 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.5.338_260413_S3000716448.zip) | 1.1 Issues fixes： 1) Fixed known software issues. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202605/releasenote%5CGeneral_Firmware_Update_Release_notes.pdf) |

</details>


<details>
<summary><h2>DS-2TD2568T-15-G0-T1Y - THERMAL_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.348 | Applied to: [DS-2TD2568T-15-G0-T1Y](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779750762/Firmware__V5.5.348_260427_S3000719140.zip) | 2026-04-27 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779750762/Firmware__V5.5.348_260427_S3000719140.zip) | 1.1 Issues fixes： 1) Fixed known software issues. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202605/releasenote%5CGeneral_Firmware_Update_Release_notes.pdf) |

</details>


<details>
<summary><h2>DS-2TD2568T-15/G0/T1Y - THERMAL_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.348 | Applied to: [DS-2TD2568T-15/G0/T1Y](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779750762/Firmware__V5.5.348_260427_S3000719140.zip), [DS-2TD2568T-5/G0/T1Y](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779750762/Firmware__V5.5.348_260427_S3000719140.zip), HM-TD1218-2/G0/T1A, HM-TD1218-3/G0/T1A, HM-TD1218-7/G0/T1A, HM-TD2618-10/G0/T1A, HM-TD2618-3/G0/T1A, HM-TD2618-7/G0/T1A | 2026-04-27 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779750762/Firmware__V5.5.348_260427_S3000719140.zip) | 1.1 Issues fixes： 1) Fixed known software issues. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202605/releasenote%5CGeneral_Firmware_Update_Release_notes.pdf) |

</details>


<details>
<summary><h2>DS-2TD2568T-5-G0-T1Y - THERMAL_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.348 | Applied to: [DS-2TD2568T-5-G0-T1Y](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779750762/Firmware__V5.5.348_260427_S3000719140.zip) | 2026-04-27 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779750762/Firmware__V5.5.348_260427_S3000719140.zip) | 1.1 Issues fixes： 1) Fixed known software issues. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202605/releasenote%5CGeneral_Firmware_Update_Release_notes.pdf) |

</details>


<details>
<summary><h2>DS-2TD2608-1-QA - THERMAL_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.338 | Applied to: [DS-2TD2608-1-QA](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.5.338_260413_S3000716448.zip) | 2026-04-13 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.5.338_260413_S3000716448.zip) | 1.1 Issues fixes： 1) Fixed known software issues. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202605/releasenote%5CGeneral_Firmware_Update_Release_notes.pdf) |

</details>


<details>
<summary><h2>DS-2TD2608-1-QA-FP - THERMAL_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.338 | Applied to: [DS-2TD2608-1-QA-FP](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.5.338_260413_S3000716448.zip) | 2026-04-13 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.5.338_260413_S3000716448.zip) | 1.1 Issues fixes： 1) Fixed known software issues. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202605/releasenote%5CGeneral_Firmware_Update_Release_notes.pdf) |

</details>


<details>
<summary><h2>DS-2TD2608-2-QA - THERMAL_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.338 | Applied to: [DS-2TD2608-2-QA](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.5.338_260413_S3000716448.zip) | 2026-04-13 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.5.338_260413_S3000716448.zip) | 1.1 Issues fixes： 1) Fixed known software issues. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202605/releasenote%5CGeneral_Firmware_Update_Release_notes.pdf) |

</details>


<details>
<summary><h2>DS-2TD2608-2-QA-FP - THERMAL_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.338 | Applied to: [DS-2TD2608-2-QA-FP](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.5.338_260413_S3000716448.zip) | 2026-04-13 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.5.338_260413_S3000716448.zip) | 1.1 Issues fixes： 1) Fixed known software issues. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202605/releasenote%5CGeneral_Firmware_Update_Release_notes.pdf) |

</details>


<details>
<summary><h2>DS-2TD2617-10-QA - THERMAL_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.338 | Applied to: [DS-2TD2617-10-QA](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.5.338_260413_S3000716448.zip) | 2026-04-13 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.5.338_260413_S3000716448.zip) | 1.1 Issues fixes： 1) Fixed known software issues. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202605/releasenote%5CGeneral_Firmware_Update_Release_notes.pdf) |

</details>


<details>
<summary><h2>DS-2TD2617-3-QA - THERMAL_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.338 | Applied to: [DS-2TD2617-3-QA](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.5.338_260413_S3000716448.zip) | 2026-04-13 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.5.338_260413_S3000716448.zip) | 1.1 Issues fixes： 1) Fixed known software issues. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202605/releasenote%5CGeneral_Firmware_Update_Release_notes.pdf) |

</details>


<details>
<summary><h2>DS-2TD2617-6-QA - THERMAL_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.338 | Applied to: [DS-2TD2617-6-QA](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.5.338_260413_S3000716448.zip) | 2026-04-13 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.5.338_260413_S3000716448.zip) | 1.1 Issues fixes： 1) Fixed known software issues. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202605/releasenote%5CGeneral_Firmware_Update_Release_notes.pdf) |

</details>


<details>
<summary><h2>DS-2TD2628-10-QA - THERMAL_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.338 | Applied to: [DS-2TD2628-10-QA](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.5.338_260413_S3000716448.zip) | 2026-04-13 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.5.338_260413_S3000716448.zip) | 1.1 Issues fixes： 1) Fixed known software issues. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202605/releasenote%5CGeneral_Firmware_Update_Release_notes.pdf) |

</details>


<details>
<summary><h2>DS-2TD2628-10/QA/GLT - THERMAL_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.118 | Applied to: [DS-2TD2628-10/QA/GLT](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779186905/Firmware__V5.5.118_260410_S3000715525.zip), [DS-2TD2628-10/QA/GLT(LA)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779186905/Firmware__V5.5.118_260410_S3000715525.zip), [DS-2TD2628-3/QA/GLT](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779186905/Firmware__V5.5.118_260410_S3000715525.zip), [DS-2TD2628-7/QA/GLT](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779186905/Firmware__V5.5.118_260410_S3000715525.zip), [DS-2TXS2628-10P/QA/GLT/CH30S80](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779186905/Firmware__V5.5.118_260410_S3000715525.zip), [DS-2TXS2628-10P/QA/GLT/CH30S80(LA)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779186905/Firmware__V5.5.118_260410_S3000715525.zip), [DS-2TXS2628-10P/QA/GLT/CH36S80](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779186905/Firmware__V5.5.118_260410_S3000715525.zip), [DS-2TXS2628-3P/QA/GLT/CH30S80](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779186905/Firmware__V5.5.118_260410_S3000715525.zip) | 2026-04-10 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779186905/Firmware__V5.5.118_260410_S3000715525.zip) | 1.1 Issues fixes： 1) Fixed known software issues. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202605/releasenote%5CGeneral_Firmware_Update_Release_notes.pdf) |

</details>


<details>
<summary><h2>DS-2TD2628-3-QA - THERMAL_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.338 | Applied to: [DS-2TD2628-3-QA](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.5.338_260413_S3000716448.zip) | 2026-04-13 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.5.338_260413_S3000716448.zip) | 1.1 Issues fixes： 1) Fixed known software issues. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202605/releasenote%5CGeneral_Firmware_Update_Release_notes.pdf) |

</details>


<details>
<summary><h2>DS-2TD2628-7-QA - THERMAL_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.338 | Applied to: [DS-2TD2628-7-QA](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.5.338_260413_S3000716448.zip) | 2026-04-13 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.5.338_260413_S3000716448.zip) | 1.1 Issues fixes： 1) Fixed known software issues. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202605/releasenote%5CGeneral_Firmware_Update_Release_notes.pdf) |

</details>


<details>
<summary><h2>DS-2TD2628T-3-QA - THERMAL_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.338 | Applied to: [DS-2TD2628T-3-QA](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.5.338_260413_S3000716448.zip) | 2026-04-13 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.5.338_260413_S3000716448.zip) | 1.1 Issues fixes： 1) Fixed known software issues. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202605/releasenote%5CGeneral_Firmware_Update_Release_notes.pdf) |

</details>


<details>
<summary><h2>DS-2TD2628T-7-QA - THERMAL_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.338 | Applied to: [DS-2TD2628T-7-QA](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.5.338_260413_S3000716448.zip) | 2026-04-13 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.5.338_260413_S3000716448.zip) | 1.1 Issues fixes： 1) Fixed known software issues. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202605/releasenote%5CGeneral_Firmware_Update_Release_notes.pdf) |

</details>


<details>
<summary><h2>DS-2TD2637-10-QY - THERMAL_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.338 | Applied to: [DS-2TD2637-10-QY](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.5.338_260413_S3000716448.zip) | 2026-04-13 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.5.338_260413_S3000716448.zip) | 1.1 Issues fixes： 1) Fixed known software issues. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202605/releasenote%5CGeneral_Firmware_Update_Release_notes.pdf) |

</details>


<details>
<summary><h2>DS-2TD2637-25-QY - THERMAL_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.338 | Applied to: [DS-2TD2637-25-QY](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.5.338_260413_S3000716448.zip) | 2026-04-13 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.5.338_260413_S3000716448.zip) | 1.1 Issues fixes： 1) Fixed known software issues. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202605/releasenote%5CGeneral_Firmware_Update_Release_notes.pdf) |

</details>


<details>
<summary><h2>DS-2TD2637-35-QY-B- - THERMAL_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.338 | Applied to: [DS-2TD2637-35-QY-B-](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.5.338_260413_S3000716448.zip) | 2026-04-13 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.5.338_260413_S3000716448.zip) | 1.1 Issues fixes： 1) Fixed known software issues. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202605/releasenote%5CGeneral_Firmware_Update_Release_notes.pdf) |

</details>


<details>
<summary><h2>DS-2TD2637-7-QY - THERMAL_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.338 | Applied to: [DS-2TD2637-7-QY](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.5.338_260413_S3000716448.zip) | 2026-04-13 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.5.338_260413_S3000716448.zip) | 1.1 Issues fixes： 1) Fixed known software issues. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202605/releasenote%5CGeneral_Firmware_Update_Release_notes.pdf) |

</details>


<details>
<summary><h2>DS-2TD2637T-10-QY - THERMAL_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.338 | Applied to: [DS-2TD2637T-10-QY](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.5.338_260413_S3000716448.zip) | 2026-04-13 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.5.338_260413_S3000716448.zip) | 1.1 Issues fixes： 1) Fixed known software issues. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202605/releasenote%5CGeneral_Firmware_Update_Release_notes.pdf) |

</details>


<details>
<summary><h2>DS-2TD2637T-15-QY - THERMAL_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.338 | Applied to: [DS-2TD2637T-15-QY](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.5.338_260413_S3000716448.zip) | 2026-04-13 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.5.338_260413_S3000716448.zip) | 1.1 Issues fixes： 1) Fixed known software issues. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202605/releasenote%5CGeneral_Firmware_Update_Release_notes.pdf) |

</details>


<details>
<summary><h2>DS-2TD2637T-7-QY - THERMAL_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.338 | Applied to: [DS-2TD2637T-7-QY](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.5.338_260413_S3000716448.zip) | 2026-04-13 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.5.338_260413_S3000716448.zip) | 1.1 Issues fixes： 1) Fixed known software issues. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202605/releasenote%5CGeneral_Firmware_Update_Release_notes.pdf) |

</details>


<details>
<summary><h2>DS-2TD4228-10/W - THERMAL_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.109 | Applied to: [DS-2TD4228-10/W](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779264543/Firmware__V5.5.109_260410_S3000716161.zip) | 2026-04-10 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779264543/Firmware__V5.5.109_260410_S3000716161.zip) | 1.1 Issues fixes： 1) Fixed known software issues. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202605/releasenote%5CGeneral_Firmware_Update_Release_notes.pdf) |

</details>


<details>
<summary><h2>DS-2TX3742-10A-Q - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.338 | Applied to: [DS-2TX3742-10A-Q](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.5.338_260413_S3000716448.zip) | 2026-04-13 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.5.338_260413_S3000716448.zip) | 1.1 Issues fixes： 1) Fixed known software issues. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202605/releasenote%5CGeneral_Firmware_Update_Release_notes.pdf) |

</details>


<details>
<summary><h2>DS-2TX3742-10P-Q - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.338 | Applied to: [DS-2TX3742-10P-Q](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.5.338_260413_S3000716448.zip) | 2026-04-13 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.5.338_260413_S3000716448.zip) | 1.1 Issues fixes： 1) Fixed known software issues. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202605/releasenote%5CGeneral_Firmware_Update_Release_notes.pdf) |

</details>


<details>
<summary><h2>DS-2TX3742-25A-Q - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.338 | Applied to: [DS-2TX3742-25A-Q](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.5.338_260413_S3000716448.zip) | 2026-04-13 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.5.338_260413_S3000716448.zip) | 1.1 Issues fixes： 1) Fixed known software issues. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202605/releasenote%5CGeneral_Firmware_Update_Release_notes.pdf) |

</details>


<details>
<summary><h2>DS-2TX3742-25P-Q - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.338 | Applied to: [DS-2TX3742-25P-Q](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.5.338_260413_S3000716448.zip) | 2026-04-13 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.5.338_260413_S3000716448.zip) | 1.1 Issues fixes： 1) Fixed known software issues. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202605/releasenote%5CGeneral_Firmware_Update_Release_notes.pdf) |

</details>


<details>
<summary><h2>DS-2TX3742-35A-Q - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.338 | Applied to: [DS-2TX3742-35A-Q](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.5.338_260413_S3000716448.zip) | 2026-04-13 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.5.338_260413_S3000716448.zip) | 1.1 Issues fixes： 1) Fixed known software issues. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202605/releasenote%5CGeneral_Firmware_Update_Release_notes.pdf) |

</details>


<details>
<summary><h2>DS-2TX3742-35P-Q - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.338 | Applied to: [DS-2TX3742-35P-Q](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.5.338_260413_S3000716448.zip) | 2026-04-13 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.5.338_260413_S3000716448.zip) | 1.1 Issues fixes： 1) Fixed known software issues. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202605/releasenote%5CGeneral_Firmware_Update_Release_notes.pdf) |

</details>


<details>
<summary><h2>DS-2XC6046G0-LIS(316L) - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.3 | Applied to: [[[DS-2XC6046G0-LIS(316L)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779174169/Firmware__V5.8.3_260416_S3000716238.zip)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779174169/Firmware__V5.8.3_260416_S3000716238.zip)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779174169/Firmware__V5.8.3_260416_S3000716238.zip), DS-2XC6046G0-LIS(316L)(2.8MM), DS-2XC6046G0-LIS(316L)(4MM) | 2026-04-16 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779174169/Firmware__V5.8.3_260416_S3000716238.zip) | — |

</details>


<details>
<summary><h2>DS-3E1506P-EI/M-4P1T1F - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 3.4.2 | Applied to: [DS-3E1506P-EI/M-4P1T1F](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779216345/Firmware__V3.4.2_260407_S3000718999.zip) | 2026-04-07 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779216345/Firmware__V3.4.2_260407_S3000718999.zip) | — |

</details>


<details>
<summary><h2>DS-3WR18X - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 1.7.100 | Applied to: [DS-3WR18X](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779750762/Firmware__V1.7.100_260429_S3000720515.zip), [DS-3WR30X](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779750762/Firmware__V1.7.100_260429_S3000720515.zip), [DS-3WR30X-V](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779750762/Firmware__V1.7.100_260429_S3000720515.zip), [[DS-3WRM18X](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779750762/Firmware__V1.7.100_260429_S3000720515.zip)/1](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779750762/Firmware__V1.7.100_260429_S3000720515.zip), DS-3WRM18X, [DS-3WRM18X/2](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779750762/Firmware__V1.7.100_260429_S3000720515.zip), [DS-3WRM18X/3](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779750762/Firmware__V1.7.100_260429_S3000720515.zip), [DS-3WRM30X/1](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779750762/Firmware__V1.7.100_260429_S3000720515.zip) | 2026-04-29 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779750762/Firmware__V1.7.100_260429_S3000720515.zip) | — |

</details>


<details>
<summary><h2>DS-7104NI-S2/WX - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 4.32.406 | Applied to: [DS-7104NI-S2/WX](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779750762/Firmware__V4.32.406_260427_S3000720971.zip), NKS4223WBTH, [DS-J142I](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779750762/Firmware__V4.32.406_260427_S3000720971.zip), NKS422WBH, NKS422WBPH, NKS4245WBTH, NKS424WBH, NKS424WBPH | 2026-04-27 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779750762/Firmware__V4.32.406_260427_S3000720971.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202605/releasenote%5CNVS_V4.32.406_20260427_ReleaseNote.pdf) |

</details>


<details>
<summary><h2>DS-7232HGHI-M2/T-2K - DVR_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 4.84.101 | Applied to: [DS-7232HGHI-M2/T-2K](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779750762/Firmware_Asia_V4.84.101_260518_S3000724190.zip) | 2026-05-18 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779750762/Firmware_Asia_V4.84.101_260518_S3000724190.zip) | — |

</details>


<details>
<summary><h2>DS-C80N-01HI - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 1.2.0 | Applied to: [DS-C80N-01HI](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V1.2.0_260423_S3000720433.zip), [DS-C80N-01HI/4K](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V1.2.0_260423_S3000720433.zip), [DS-C80N-01HO](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V1.2.0_260423_S3000720433.zip), [DS-C80N-01HO/4K](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V1.2.0_260423_S3000720433.zip) | 2026-04-23 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V1.2.0_260423_S3000720433.zip) | — |

</details>


<details>
<summary><h2>DS-K1105EDB - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 1.0.2 | Applied to: [DS-K1105EDB](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779178727/Firmware__V1.0.2_260414_S3000716047.zip), [DS-K1105EDKB](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779178727/Firmware__V1.0.2_260414_S3000716047.zip), [DS-K1105EDKB-QR](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779178727/Firmware__V1.0.2_260414_S3000716047.zip), [DS-K1105EMB](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779178727/Firmware__V1.0.2_260414_S3000716047.zip), [DS-K1105EMKB](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779178727/Firmware__V1.0.2_260414_S3000716047.zip), [DS-K1105EMKB-QR](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779178727/Firmware__V1.0.2_260414_S3000716047.zip) | 2026-04-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779178727/Firmware__V1.0.2_260414_S3000716047.zip) | — |

</details>


<details>
<summary><h2>DS-K1T670MFWX - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 4.48.20 | Applied to: [DS-K1T670MFWX](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779750762/Firmware__V4.48.20_260427_S3000719622.zip), [DS-K1T670MWX-QR](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779750762/Firmware__V4.48.20_260427_S3000719622.zip), [DS-K1T670MWX-WBQR](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779750762/Firmware__V4.48.20_260427_S3000719622.zip), [DS-K1T670MWX-WEQR](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779750762/Firmware__V4.48.20_260427_S3000719622.zip), [DS-K1T670MX](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779750762/Firmware__V4.48.20_260427_S3000719622.zip), [DS-K1T670MX-QR](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779750762/Firmware__V4.48.20_260427_S3000719622.zip), [DS-K1T670MX-WB](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779750762/Firmware__V4.48.20_260427_S3000719622.zip), [DS-K1T670MX-WE](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779750762/Firmware__V4.48.20_260427_S3000719622.zip) | 2026-04-27 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779750762/Firmware__V4.48.20_260427_S3000719622.zip) | — |

</details>


<details>
<summary><h2>HM-TD1018-1/QR - THERMAL_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.61 | Applied to: HM-TD1018-1/QR | 2026-04-13 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.5.61_260413_S3000715287.zip) | 1.1 Issues fixes： 1) Fixed known software issues. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202605/releasenote%5CGeneral_Firmware_Update_Release_notes.pdf) |

</details>


<details>
<summary><h2>HM-TD1228-2/G1/T3A - THERMAL_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.348 | Applied to: HM-TD1228-2/G1/T3A, HM-TD1228-3/G1/T3A, HM-TD1228-7/G1/T3A, HM-TD2628-10/G1/T3A, HM-TD2628-3/G1/T3A, HM-TD2628-7/G1/T3A, HM-TD2638-10/G1/T3Y | 2026-04-27 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779750762/Firmware__V5.5.348_260427_S3000719141.zip) | 1.1 Issues fixes： 1) Fixed known software issues. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202605/releasenote%5CGeneral_Firmware_Update_Release_notes.pdf) |

</details>


<details>
<summary><h2>HM-TD1228T-2/G1/T3A - THERMAL_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.348 | Applied to: HM-TD1228T-2/G1/T3A, HM-TD1228T-3/G1/T3A, HM-TD2168-5/G1/T3Y, HM-TD2168T-5/G1/T3Y, HM-TD2628T-3/G1/T3A, HM-TD2628T-7/G1/T3A, HM-TD2638-15/G1/T3Y, HM-TD2638-25/G1/T3Y | 2026-04-10 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.348_260410_S3000714871.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202604/releasenote%5CThermal_Network_Fixed_Camera_V5.5.348_Release_Notes.pdf) |

</details>


<details>
<summary><h2>HM-TD2168-5/G0/T1Y - THERMAL_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.348 | Applied to: HM-TD2168-5/G0/T1Y, HM-TD2168T-5/G0/T1Y, HM-TD2638-10/G0/T1Y, HM-TD2638-15/G0/T1Y, HM-TD2638-25/G0/T1Y, HM-TD2638-35/G0/T1Y, HM-TD2638-4/G0/T1Y, HM-TD2638-8/G0/T1Y | 2026-04-10 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.348_260410_S3000714869.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202604/releasenote%5CThermal_Network_Fixed_Camera_V5.5.348_Release_Notes.pdf) |

</details>


<details>
<summary><h2>HM-TD3028T-2/Q(B) - THERMAL_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.342 | Applied to: HM-TD3028T-2/Q(B), HM-TD3028T-3/Q(B) | 2026-04-16 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779522628/Firmware__V5.5.342_260416_S3000717610.zip) | 1.1 Issues fixes： 1) Fixed known software issues. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202605/releasenote%5CGeneral_Firmware_Update_Release_notes.pdf) |

</details>


<details>
<summary><h2>HM-TD63C8-100C4L/G0/T2Y - THERMAL_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.11 | Applied to: HM-TD63C8-100C4L/G0/T2Y, HM-TD63C8-75C4L/G0/T2Y, HM-TD81C8-150ZK4FL/G0/T2 | 2026-05-06 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779750762/Firmware__V5.7.11_260506_S3000720327.zip) | — |

</details>


<details>
<summary><h2>HM-TX2840-10/G0/T1 - THERMAL_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.506 | Applied to: HM-TX2840-10/G0/T1, HM-TX3840-10/G0/T1, HM-TX3840-15/G0/T1, HM-TX3840-25/G0/T1 | 2026-04-01 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.5.506_260401_S3000716059.zip) | fixed camera models supporting Guanlan Large-scale. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202604/releasenote%5CThermal_TandemVu_Series_V5.5.506_Release_note.pdf) |

</details>


<details>
<summary><h2>IDS-2CD5347G2/V-XS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.9.21 | Applied to: [IDS-2CD5347G2/V-XS](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.9.21_260423_S3000719054.zip), [IDS-2CD5347G2/V-XS(2.8MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.9.21_260423_S3000719054.zip), [IDS-2CD5347G2/V-XS(4MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.9.21_260423_S3000719054.zip), [IDS-2CD5387G2/V-XS](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.9.21_260423_S3000719054.zip), [IDS-2CD5387G2/V-XS(2.8MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.9.21_260423_S3000719054.zip), [IDS-2CD5387G2/V-XS(4MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.9.21_260423_S3000719054.zip), [IDS-2CD5A46G2/V-XZ(H)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.9.21_260423_S3000719054.zip)S(Y), [IDS-2CD5A46G2/V-XZHSY(2.8-12MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.9.21_260423_S3000719054.zip) | 2026-04-23 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.9.21_260423_S3000719054.zip) | 1. Support AI Encoding of main stream in Smart Event VCA mode. 2. Modify Features NA · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202605/releasenote%5CDeepinViewX_Network_Camera_V5.9.21_Release_Note_--H9.pdf) |

</details>


<details>
<summary><h2>IDS-2CD70166G2-AP - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.9.23 | Applied to: [IDS-2CD70166G2-AP](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779216345/Firmware__V5.9.23_260407_S3000714059.zip), [IDS-2CD70166G2/E-IHSYR](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779216345/Firmware__V5.9.23_260407_S3000714059.zip), [IDS-2CD70166G2/E-IHSYR(3.8-16MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779216345/Firmware__V5.9.23_260407_S3000714059.zip), [IDS-2CD70166G2/E-IHSYR(11-40MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779216345/Firmware__V5.9.23_260407_S3000714059.zip), [IDS-2CD7046G2-AP](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779216345/Firmware__V5.9.23_260407_S3000714059.zip), [IDS-2CD7046G2/E-IHSYR](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779216345/Firmware__V5.9.23_260407_S3000714059.zip), [IDS-2CD7046G2/E-IHSYR(11-40MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779216345/Firmware__V5.9.23_260407_S3000714059.zip), [IDS-2CD7046G2/E-IHSYR(3.8-16MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779216345/Firmware__V5.9.23_260407_S3000714059.zip) | 2026-04-07 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779216345/Firmware__V5.9.23_260407_S3000714059.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202605/releasenote%5CDeepinView_Camera_V5.9.23_Release_Note.pdf) |

</details>


<details>
<summary><h2>IDS-2CD7046G0-H-AP - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.9.1 | Applied to: [IDS-2CD7046G0-H-AP](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.9.14_260401_S3000712573.zip) | 2026-04-02 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.9.14_260401_S3000712573.zip) |  Improved functionality Fix some known bugs and improve system stability. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202605/releasenote%5CG7-V5.9.1_Release_Note.pdf) |

</details>


<details>
<summary><h2>IDS-2CD7046G0/H-AP - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.9.1 | Applied to: [IDS-2CD7046G0/H-AP](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779324458/Firmware__V5.9.1_260402_S3000713087.zip), [IDS-2CD7086G0/H-AP](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779324458/Firmware__V5.9.1_260402_S3000713087.zip), [IDS-2CD70C5G0/H-AP](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779324458/Firmware__V5.9.1_260402_S3000713087.zip), [IDS-2CD7146G0/H-IZ(H)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779324458/Firmware__V5.9.1_260402_S3000713087.zip)S(Y), [IDS-2CD7146G0/H-IZS(2.8-12MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779324458/Firmware__V5.9.1_260402_S3000713087.zip), [IDS-2CD7146G0/H-IZS(8-32MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779324458/Firmware__V5.9.1_260402_S3000713087.zip), [IDS-2CD7146G0/H-IZHSY(8-32MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779324458/Firmware__V5.9.1_260402_S3000713087.zip), [IDS-2CD7146G0/H-IZHSY(2.8-12MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779324458/Firmware__V5.9.1_260402_S3000713087.zip) | 2026-04-02 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779324458/Firmware__V5.9.1_260402_S3000713087.zip) |  Improved functionality Fix some known bugs and improve system stability. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202605/releasenote%5CG7-V5.9.1_Release_Note.pdf) |

</details>


<details>
<summary><h2>IDS-2CD7046G2/EP-IHSYR - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.9.23 | Applied to: [IDS-2CD7046G2/EP-IHSYR](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779216345/Firmware__V5.9.23_260407_S3000714058.zip), [IDS-2CD7046G2/EP-IHSYR(3.8-16MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779216345/Firmware__V5.9.23_260407_S3000714058.zip), [IDS-2CD7046G2/EP-IHSYR(11-40MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779216345/Firmware__V5.9.23_260407_S3000714058.zip), [IDS-2CD7086G2/EP-IHSYR](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779216345/Firmware__V5.9.23_260407_S3000714058.zip), [IDS-2CD7086G2/EP-IHSYR(11-40MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779216345/Firmware__V5.9.23_260407_S3000714058.zip), [IDS-2CD7086G2/EP-IHSYR(3.8-16MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779216345/Firmware__V5.9.23_260407_S3000714058.zip), [IDS-2CD7546G2/P-XZHS(Y)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779216345/Firmware__V5.9.23_260407_S3000714058.zip), [IDS-2CD7546G2/P-XZHSY(2.8-12MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779216345/Firmware__V5.9.23_260407_S3000714058.zip) | 2026-04-07 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779216345/Firmware__V5.9.23_260407_S3000714058.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202605/releasenote%5CDeepinView_Camera_V5.9.23_Release_Note.pdf) |

</details>


<details>
<summary><h2>IDS-2CD7086G0-H-AP - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.9.1 | Applied to: [IDS-2CD7086G0-H-AP](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.9.14_260401_S3000712573.zip) | 2026-04-02 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.9.14_260401_S3000712573.zip) |  Improved functionality Fix some known bugs and improve system stability. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202605/releasenote%5CG7-V5.9.1_Release_Note.pdf) |

</details>


<details>
<summary><h2>IDS-2CD70C5G0-H-AP - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.9.1 | Applied to: [IDS-2CD70C5G0-H-AP](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.9.14_260401_S3000712573.zip) | 2026-04-02 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.9.14_260401_S3000712573.zip) |  Improved functionality Fix some known bugs and improve system stability. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202605/releasenote%5CG7-V5.9.1_Release_Note.pdf) |

</details>


<details>
<summary><h2>IDS-2CD7146G0-H-IZ-H-S-Y- - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.9.1 | Applied to: [IDS-2CD7146G0-H-IZ-H-S-Y-](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.9.14_260401_S3000712573.zip) | 2026-04-02 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.9.14_260401_S3000712573.zip) |  Improved functionality Fix some known bugs and improve system stability. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202605/releasenote%5CG7-V5.9.1_Release_Note.pdf) |

</details>


<details>
<summary><h2>IDS-2CD7186G0-H-IZ-H-S-Y- - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.9.1 | Applied to: [IDS-2CD7186G0-H-IZ-H-S-Y-](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.9.14_260401_S3000712573.zip) | 2026-04-02 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.9.14_260401_S3000712573.zip) |  Improved functionality Fix some known bugs and improve system stability. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202605/releasenote%5CG7-V5.9.1_Release_Note.pdf) |

</details>


<details>
<summary><h2>IDS-2CD71C5G0-H-IZ-H-S-Y- - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.9.1 | Applied to: [IDS-2CD71C5G0-H-IZ-H-S-Y-](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.9.14_260401_S3000712573.zip) | 2026-04-02 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.9.14_260401_S3000712573.zip) |  Improved functionality Fix some known bugs and improve system stability. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202605/releasenote%5CG7-V5.9.1_Release_Note.pdf) |

</details>


<details>
<summary><h2>IDS-2CD7347G0-XS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.2 | Applied to: [IDS-2CD7347G0-XS](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779264543/Firmware__V5.8.2_260404_S3000714561.zip), [IDS-2CD7347G0-XS(2.8MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779264543/Firmware__V5.8.2_260404_S3000714561.zip), [IDS-2CD7347G0-XS(4MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779264543/Firmware__V5.8.2_260404_S3000714561.zip), [IDS-2CD7387G0-XS](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779264543/Firmware__V5.8.2_260404_S3000714561.zip), [IDS-2CD7387G0-XS(2.8MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779264543/Firmware__V5.8.2_260404_S3000714561.zip), [IDS-2CD7387G0-XS(4MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779264543/Firmware__V5.8.2_260404_S3000714561.zip), [IDS-2CD7D47G0-XS](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779264543/Firmware__V5.8.2_260404_S3000714561.zip), [IDS-2CD7D47G0-XS(2.8MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779264543/Firmware__V5.8.2_260404_S3000714561.zip) | 2026-04-04 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779264543/Firmware__V5.8.2_260404_S3000714561.zip) | NA 2. Modify Features Fix some known bugs and improve system stability. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202605/releasenote%5CNetwork_Camera_V5.8.2_Release_Note_--G5.pdf) |

</details>


<details>
<summary><h2>IDS-2CD7A45G0-IZ(H)S(Y) - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.50 | Applied to: [IDS-2CD7A45G0-IZ(H)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779178727/Firmware__V5.8.50_260415_S3000716272.zip)S(Y), [IDS-2CD7A45G0-IZHSY(4.7-118MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779178727/Firmware__V5.8.50_260415_S3000716272.zip), [IDS-2CD7A45G0-IZS(4.7-118MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779178727/Firmware__V5.8.50_260415_S3000716272.zip), [IDS-2CD7A45G0/P-IZHS(Y)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779178727/Firmware__V5.8.50_260415_S3000716272.zip), [IDS-2CD7A45G0/P-IZHS(4.7-118MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779178727/Firmware__V5.8.50_260415_S3000716272.zip) | 2026-04-15 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779178727/Firmware__V5.8.50_260415_S3000716272.zip) | NA 2. Modify Features Fix some known bugs and improve system stability. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202605/releasenote%5CNetwork_Camera_V5.8.50_Release_Note_--H8.pdf) |

</details>


<details>
<summary><h2>IDS-2CD7A46G0-H-IZHS-Y- - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.9.1 | Applied to: [IDS-2CD7A46G0-H-IZHS-Y-](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.9.14_260401_S3000712573.zip) | 2026-04-02 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.9.14_260401_S3000712573.zip) |  Improved functionality Fix some known bugs and improve system stability. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202605/releasenote%5CG7-V5.9.1_Release_Note.pdf) |

</details>


<details>
<summary><h2>IDS-2CD7A86G0-H-IZHS-Y- - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.9.1 | Applied to: [IDS-2CD7A86G0-H-IZHS-Y-](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.9.14_260401_S3000712573.zip) | 2026-04-02 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.9.14_260401_S3000712573.zip) |  Improved functionality Fix some known bugs and improve system stability. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202605/releasenote%5CG7-V5.9.1_Release_Note.pdf) |

</details>


<details>
<summary><h2>IDS-2CD7A86G0-H-IZHSY - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.9.1 | Applied to: [IDS-2CD7A86G0-H-IZHSY](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.9.14_260401_S3000712573.zip) | 2026-04-02 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.9.14_260401_S3000712573.zip) |  Improved functionality Fix some known bugs and improve system stability. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202605/releasenote%5CG7-V5.9.1_Release_Note.pdf) |

</details>


<details>
<summary><h2>IDS-2CD7AC5G0-H-IZHS-Y- - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.9.1 | Applied to: [IDS-2CD7AC5G0-H-IZHS-Y-](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.9.14_260401_S3000712573.zip) | 2026-04-02 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.9.14_260401_S3000712573.zip) |  Improved functionality Fix some known bugs and improve system stability. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202605/releasenote%5CG7-V5.9.1_Release_Note.pdf) |

</details>


<details>
<summary><h2>IDS-2CD8A87G0P/PW - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.901 | Applied to: [IDS-2CD8A87G0P/PW](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779216345/Firmware__V5.5.901_260407_S3000719947.zip), [IDS-2CD8A87G0P/PW(6MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779216345/Firmware__V5.5.901_260407_S3000719947.zip) | 2026-04-07 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779216345/Firmware__V5.5.901_260407_S3000719947.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202605/releasenote%5CHigh-Rise_Littering_Detection_Camera_V5.5.901_Release_Note.pdf) |

</details>


<details>
<summary><h2>IDS-2CD8V446G0/X2-XZHS(Y) - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.10.0 | Applied to: [IDS-2CD8V446G0/X2-XZHS(Y)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.10.0_260423_S3000718071.zip), [IDS-2CD8V446G0/X2-XZHSY(1050/1050)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.10.0_260423_S3000718071.zip)/O-STD, [IDS-2CD8V447G0E/X2-XZS](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.10.0_260423_S3000718071.zip), [IDS-2CD8V447G0E/X2-XZS(4-6/4-6)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.10.0_260423_S3000718071.zip), [IDS-2CD8V447G0E/X2-XZS(6-9/6-9)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.10.0_260423_S3000718071.zip), [IDS-2CD8V886G0/X2-XZHS(Y)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.10.0_260423_S3000718071.zip), [IDS-2CD8V886G0/X2-XZHSY(1050/1050)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.10.0_260423_S3000718071.zip)/O-STD | 2026-04-23 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.10.0_260423_S3000718071.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202605/releasenote%5CDeepinView_Dual-Lens_Omni_Camera_V5.10.0_Release_Note.pdf) |

</details>


<details>
<summary><h2>IKS-2042BH-PH/W - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.23 | Applied to: IKS-2042BH-PH/W, [DS-J142I](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779522628/Firmware__V5.8.23_260403_S3000712866.zip), IKS-2042BPH-PH/W, IKS-2042BTH-PH/W, IPC-CFW02(/EU), IPC-CFW02(2.8MM)(HILOOKSTD)/EU, IPC-CFW02(4MM)(HILOOKSTD)/EU | 2026-04-03 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779522628/Firmware__V5.8.23_260403_S3000712866.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202509/releasenote%5CNVS_V4.32.205_250811__V4.32.401_250811_ReleaseNotes.pdf) |

</details>


<details>
<summary><h2>IPC-B129HAA-LU(F)(/SL)(/SRB) - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.9.14 | Applied to: IPC-B129HAA-LU(F)(/SL)(/SRB), IPC-B129HAA-LU(2.8MM)(HILOOKSTD), IPC-B129HAA-LU(4MM)(HILOOKSTD), IPC-B129HAA-LUF/SL(2.8MM)(HILOOKSTD), IPC-B129HAA-LUF/SL(4MM)(HILOOKSTD), IPC-B129HAA-LUF/SRB(2.8MM)(HILOOKSTD), IPC-B129HAA-LUF/SRB(4MM)(HILOOKSTD), IPC-B149HAA-LU(F)(/SL)(/SRB) | 2026-04-01 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.9.14_260401_S3000712573.zip) | — |

</details>


<details>
<summary><h2>IPC-B160HA-LU - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.41 | Applied to: IPC-B160HA-LU, IPC-B160HA-LU(2.8MM)(HILOOKSTD), IPC-B160HA-LU(4MM)(HILOOKSTD), IPC-B160HA-LUF/SL, IPC-B160HA-LUF/SL(2.8MM)(HILOOKSTD), IPC-B160HA-LUF/SL(4MM)(HILOOKSTD), IPC-B160HAP-LUF/SL, IPC-B160HAP-LUF/SL(2.8MM)(HILOOKSTD) | 2026-04-01 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779522628/Firmware__V5.8.41_260401_S3000712617.zip) | 1. Fixed some bugs to enhance system stability. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202604/releasenote%5CNetwork_Camera-V5.8.41_SP1_Release_Note-G6.pdf) |

</details>


<details>
<summary><h2>IPC-B460HAD-LUF/S(L)(RB) - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.12 | Applied to: IPC-B460HAD-LUF/S(L)(RB), IPC-B460HAD-LUF/SL(2.8MM)(HILOOKSTD), IPC-B460HAD-LUF/SRB(2.8MM)(HILOOKSTD), IPC-B469HAD-LUF/S(L)(RB), IPC-B469HAD-LUF/SRB(2.8MM)(HILOOKSTD), IPC-B469HAD-LUF/SL(2.8MM)(HILOOKSTD), IPC-B480HAD-LUF/S(L)(RB), IPC-B480HAD-LUF/SL(2MM)(HILOOKSTD) | 2026-04-16 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779522628/Firmware__V5.8.12_260416_S3000716519.zip) | some bugs to enhance system stability. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202605/releasenote%5CNetwork_Camera-V5.8.12_260416_Release_IPCE_P_E11.pdf) |

</details>


<details>
<summary><h2>ISD-SMG318L - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 1.2.8 | Applied to: ISD-SMG318L, ISD-SMG133L, ISD-SMG333L, ISD-SMG572L, ISD-SMG572LC-I | 2026-05-09 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779750762/Firmware__V1.2.8_260509_S3000723501.zip) | — |

</details>


<details>
<summary><h2>PTZ-N2204I-DE3 - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.9.5 | Applied to: PTZ-N2204I-DE3, PTZ-N2204I-DE3(HILOOKSTD), PTZ-N2204I-DE3(HILOOKSTD)(G), PTZ-N2404I-DE3, PTZ-N2404I-DE3(HILOOKSTD)(G), PTZ-N4215-DE3, PTZ-N4215-DE3(HILOOKSTD), PTZ-N4215-DE3(HILOOKSTD)(J) | 2026-04-16 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779522628/Firmware__V5.9.5_260416_S3000716247.zip) | 1. Algorithm optimization and updates. 2. Fix some bugs. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202507/releasenote%5CRelease_Note.pdf) |

</details>


<details>
<summary><h2>PTZ-N2C200C-D/4G - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.11 | Applied to: PTZ-N2C200C-D/4G, PTZ-N2C200C-D/4G(2.8MM)(HILOOKSTD)/EU, PTZ-N2C200C-D/4G(4MM)(HILOOKSTD)/EU | 2026-04-09 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.8.11_260409_S3000714729.zip) | some bugs to enhance system stability. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202605/releasenote%5CNetwork_Camera-V5.8.11_260409Release_IPDE_E9.pdf) |

</details>
