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
| **Status** | ✅ SUCCESS |
| **Last run** | 2026-06-07 08:21:04 UTC |
| **Scraper** | HTTP |
| **Catalog fetch** | playwright |
| **Catalog rows parsed** | 1079 |
| **Firmware records** | 517 |
| **New last run** | 10 |
| **Test mode** | Disabled |



---

## Firmware list

Collapsible sections per model and hardware line (newest firmware first within each section).

Total: 517



<details>
<summary><h2>AE-DC2022-V200 - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 1.1.1 | Applied to: [AE-DC2022-V200](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V1.1.1_260326_S3000712339.zip), [AE-DC2022-V200(2CH)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V1.1.1_260326_S3000712339.zip), [AE-DC2032-V300](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V1.1.1_260326_S3000712339.zip), [AE-DC2032-V300(3CH)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V1.1.1_260326_S3000712339.zip), [AE-DC2032-V300(N4G)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V1.1.1_260326_S3000712339.zip) | 2026-03-26 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V1.1.1_260326_S3000712339.zip) | — |

</details>


<details>
<summary><h2>AE-DC5113-F6S - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 1.2.8 | Applied to: [AE-DC5113-F6S](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779750762/Firmware__V1.2.8_260509_S3000723501.zip) | 2021-05-13 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779750762/Firmware__V1.2.8_260509_S3000723501.zip) | — |

</details>


<details>
<summary><h2>AE-DI2032-G40/V2 - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 6.0.1 | Applied to: [AE-DI2032-G40/V2](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1769711476/Firmware__V6.0.1_260104_S3000696935.zip), [[[[AE-DI2032-G40(V2)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1769711476/Firmware__V6.0.1_260104_S3000696935.zip)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1769711476/Firmware__V6.0.1_260104_S3000696935.zip)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1769711476/Firmware__V6.0.1_260104_S3000696935.zip)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1769711476/Firmware__V6.0.1_260104_S3000696935.zip)(B)(US)(INTEGRATED), AE-DI2032-G40(V2)(B)(EU)(INTEGRATED), AE-DI2032-G40(V2)(B)(US), AE-DI2032-G40(V2)(B)(EU) | 2026-01-04 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1769711476/Firmware__V6.0.1_260104_S3000696935.zip) | — |

</details>


<details>
<summary><h2>AE-DI5052-G40 PRO - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 4.7.5 | Applied to: [[[AE-DI5052-G40](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779186905/Firmware__V4.7.5_260409_S3000716981.zip)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779186905/Firmware__V4.7.5_260409_S3000716981.zip)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779186905/Firmware__V4.7.5_260409_S3000716981.zip) PRO, AE-DI5052-G40 PRO(EU), AE-DI5052-G40 PRO(US) | 2026-04-09 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779186905/Firmware__V4.7.5_260409_S3000716981.zip) | Fixed an issue where APN parameters could not be configured successfully when Card 2 was inserted with an APN card while Card 1 was not inserted. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202606/releasenote%5C【Release_Note】G40Pro_V4.7.5.pdf) |

</details>


<details>
<summary><h2>AE-MD5043-SD - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.1 | Applied to: [AE-MD5043-SD/GLF(EU-STD)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.8.1_260330_S3000711487.zip) | 2024-11-21 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.8.1_260330_S3000711487.zip) | — |

</details>


<details>
<summary><h2>AE-MH0408 - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.1 | Applied to: [AE-MH0408(1T)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.8.1_260330_S3000711487.zip)(RJ45) | 2024-11-21 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.8.1_260330_S3000711487.zip) | — |

</details>


<details>
<summary><h2>AE-VC3B2I-ISF - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 4.3.3 | Applied to: [AE-VC3B2I-ISF](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1777486932/Firmware__V4.3.3_260311_S3000717251.zip), [AE-VC3B2I-ISF(RJ45)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1777486932/Firmware__V4.3.3_260311_S3000717251.zip)(6MM), [AE-VC3B2I-ISF(M12)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1777486932/Firmware__V4.3.3_260311_S3000717251.zip)(6MM) | 2026-03-11 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1777486932/Firmware__V4.3.3_260311_S3000717251.zip) | — |

</details>


<details>
<summary><h2>DS-1100KI(C) - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.1.2 | Applied to: [DS-1100KI(C)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1769059248/Firmware__V5.1.2_251024_S3000683492.zip) | 2025-10-24 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1769059248/Firmware__V5.1.2_251024_S3000683492.zip) | — |

</details>


<details>
<summary><h2>DS-1105KI - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.1.2 | Applied to: [DS-1105KI](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1769059248/Firmware__V5.1.2_251024_S3000683489.zip), [DS-1105KI(B)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1769059248/Firmware__V5.1.2_251024_S3000683489.zip) | 2025-10-24 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1769059248/Firmware__V5.1.2_251024_S3000683489.zip) | — |

</details>


<details>
<summary><h2>DS-2CD1023G0-IUF - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.25 | Applied to: [DS-2CD1023G0-IUF](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.7.25_260401_S3000715096.zip), [DS-2CD1023G0-IUF(2.8MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.7.25_260401_S3000715096.zip)(C), [DS-2CD1023G0-IUF(4MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.7.25_260401_S3000715096.zip)(C), [DS-2CD1023G0E-I](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.7.25_260401_S3000715096.zip), [[DS-2CD1023G0E-I(2.8MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.7.25_260401_S3000715096.zip)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.7.25_260401_S3000715096.zip), [[DS-2CD1023G0E-I(4MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.7.25_260401_S3000715096.zip)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.7.25_260401_S3000715096.zip), DS-2CD1023G0E-I(2.8MM)(C), DS-2CD1023G0E-I(4MM)(C) | 2026-04-01 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.7.25_260401_S3000715096.zip) | Fixed some bugs to enhance system stability. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202605/releasenote%5CNetwork_Camera-V5.7.25_260401_Release_Note-E8.pdf) |

</details>


<details>
<summary><h2>DS-2CD1023G0E-I - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.84 | Applied to: [DS-2CD1023G0E-I](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1769319633/c3afe62f-4071-4e50-a292-ded015321289.zip), [DS-2CD1023G0E-I(2.8MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1769319633/c3afe62f-4071-4e50-a292-ded015321289.zip), [DS-2CD1023G0E-I(4MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1769319633/c3afe62f-4071-4e50-a292-ded015321289.zip), [DS-2CD1123G0E-I](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1769319633/c3afe62f-4071-4e50-a292-ded015321289.zip), [DS-2CD1123G0E-I(2.8MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1769319633/c3afe62f-4071-4e50-a292-ded015321289.zip), [DS-2CD1323G0E-I](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1769319633/c3afe62f-4071-4e50-a292-ded015321289.zip), [DS-2CD1323G0E-I(2.8MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1769319633/c3afe62f-4071-4e50-a292-ded015321289.zip), [DS-2CD1323G0E-I(6MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1769319633/c3afe62f-4071-4e50-a292-ded015321289.zip) | 2021-01-04 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1769319633/c3afe62f-4071-4e50-a292-ded015321289.zip) | — |

</details>


<details>
<summary><h2>DS-2CD1023G2-LIDUF/4G/SL - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.34 | Applied to: [DS-2CD1023G2-LIDUF/4G/SL](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780617965/Firmware__V5.8.34_260403_S3000712880.zip), [[DS-2CD1023G2-LIDUF/4G/SL(2.8)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780617965/Firmware__V5.8.34_260403_S3000712880.zip)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780617965/Firmware__V5.8.34_260403_S3000712880.zip)OSTD/LA/FUS, [[DS-2CD1023G2-LIDUF/4G/SL(4)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780617965/Firmware__V5.8.34_260403_S3000712880.zip)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780617965/Firmware__V5.8.34_260403_S3000712880.zip)/O-STD/LA/FUS, [DS-2CD1023G2-LIDUF/4G/SL(4MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780617965/Firmware__V5.8.34_260403_S3000712880.zip), [DS-2CD1023G2-LIDUF/4G/SL(2.8MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780617965/Firmware__V5.8.34_260403_S3000712880.zip)/O-STD/EU, DS-2CD1023G2-LIDUF/4G/SL(2.8)OSTD/JP/FUS, DS-2CD1023G2-LIDUF/4G/SL(4)/O-STD/JP/FUS, [DS-2DE2C200MWG-4G](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780617965/Firmware__V5.8.34_260403_S3000712880.zip) | 2026-04-03 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780617965/Firmware__V5.8.34_260403_S3000712880.zip) | — |

</details>


<details>
<summary><h2>DS-2CD1023G2-LIU(F) - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.41 | Applied to: [DS-2CD1023G2-LIU(F)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.8.41_260401_S3000712568.zip), [DS-2CD1023G2-LIU(2.8MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.8.41_260401_S3000712568.zip), [DS-2CD1023G2-LIU(4MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.8.41_260401_S3000712568.zip), [DS-2CD1023G2-LIUF(2.8MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.8.41_260401_S3000712568.zip), [DS-2CD1023G2-LIUF(4MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.8.41_260401_S3000712568.zip), [DS-2CD1027G2-L(UF)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.8.41_260401_S3000712568.zip), [DS-2CD1027G2-L(2.8MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.8.41_260401_S3000712568.zip), [DS-2CD1027G2-L(4MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.8.41_260401_S3000712568.zip) | 2026-04-01 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.8.41_260401_S3000712568.zip) | Fixed some bugs to enhance system stability. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202604/releasenote%5CNetwork_Camera-V5.8.41_SP1_Release_Note-E9.pdf) |

</details>


<details>
<summary><h2>DS-2CD1023G2-LIUF/SL - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.41 | Applied to: [DS-2CD1023G2-LIUF/SL](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.8.41_260401_S3000712568.zip), [DS-2CD1023G2-LIUF/SL(2.8MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.8.41_260401_S3000712568.zip), [DS-2CD1023G2-LIUF/SL(4MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.8.41_260401_S3000712568.zip), [DS-2CD1027G2H-LIU(F)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.8.41_260401_S3000712568.zip), [DS-2CD1027G2H-LIU(2.8MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.8.41_260401_S3000712568.zip), [DS-2CD1027G2H-LIU(4MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.8.41_260401_S3000712568.zip), [DS-2CD1027G2H-LIUF(2.8MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.8.41_260401_S3000712568.zip), [DS-2CD1027G2H-LIUF(4MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.8.41_260401_S3000712568.zip) | 2026-04-01 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.8.41_260401_S3000712568.zip) | Fixed some bugs to enhance system stability. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202604/releasenote%5CNetwork_Camera-V5.8.41_260401_Release_Note-E9.pdf) |

</details>


<details>
<summary><h2>DS-2CD1023G3-LIU(F)(/SX) - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.9.15 | Applied to: [DS-2CD1023G3-LIU(F)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780563030/Firmware__V5.9.15_260508_S3000721729.zip)(/SX), [DS-2CD1023G3-LIUF(2.8MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780563030/Firmware__V5.9.15_260508_S3000721729.zip), [DS-2CD1023G3-LIUF(4MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780563030/Firmware__V5.9.15_260508_S3000721729.zip), [DS-2CD1023G3-LIU(2.8MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780563030/Firmware__V5.9.15_260508_S3000721729.zip), [DS-2CD1023G3-LIU(4MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780563030/Firmware__V5.9.15_260508_S3000721729.zip), [DS-2CD1043G3-LIU(F)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780563030/Firmware__V5.9.15_260508_S3000721729.zip)(/SX), [[DS-2CD1043G3-LIU(2.8MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780563030/Firmware__V5.9.15_260508_S3000721729.zip)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780563030/Firmware__V5.9.15_260508_S3000721729.zip), DS-2CD1043G3-LIU(2.8MM)(BLACK) | 2026-05-08 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780563030/Firmware__V5.9.15_260508_S3000721729.zip) | Animal detection is newly supported, with detection targets including large animals (horses, sheep, · cattle, etc.), small animals (cats, dogs), and poultry (birds). By default, it is not selected and needs to · be manually enabled. It supports SMART events such as intrusion detection. · The 1XX3 and 3XX1G3(E) series products are newly added. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202606/releasenote%5CNetwork_Camera-V5.9.15_260508_Release_IPCE_E_E15.pdf) |

</details>


<details>
<summary><h2>DS-2CD1027G3-LIU(F)(/SL)(/SRB) - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.9.14 | Applied to: [DS-2CD1027G3-LIU(F)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780683636/Firmware__V5.9.14_260401_S3000712572.zip)(/SL)(/SRB), [DS-2CD1027G3-LIUF/SL(2.8MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780683636/Firmware__V5.9.14_260401_S3000712572.zip), [DS-2CD1027G3-LIUF/SL(4MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780683636/Firmware__V5.9.14_260401_S3000712572.zip), [DS-2CD1027G3-LIU/SL(2.8MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780683636/Firmware__V5.9.14_260401_S3000712572.zip), [DS-2CD1027G3-LIU/SL(4MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780683636/Firmware__V5.9.14_260401_S3000712572.zip), [DS-2CD1027G3-LIUF/SRB(2.8MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780683636/Firmware__V5.9.14_260401_S3000712572.zip), [DS-2CD1027G3-LIUF/SRB(4MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780683636/Firmware__V5.9.14_260401_S3000712572.zip), [DS-2CD1027G3-LIU(2.8MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780683636/Firmware__V5.9.14_260401_S3000712572.zip) | 2026-04-01 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780683636/Firmware__V5.9.14_260401_S3000712572.zip) | Fixed some bugs to enhance system stability. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202604/releasenote%5CNetwork_Camera-V5.9.14_260401_Release_Note-E15.pdf) |

</details>


<details>
<summary><h2>DS-2CD1043G0-I(UF) - IPC_E7S (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.820 | Applied to: [DS-2CD1043G0-I(UF)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780649800/Firmware__V5.5.820_260402_S3000712894.zip), [DS-2CD1043G0-IUF(2.8MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780649800/Firmware__V5.5.820_260402_S3000712894.zip)(B), [DS-2CD1043G0-IUF(4MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780649800/Firmware__V5.5.820_260402_S3000712894.zip)(B), [[DS-2CD1043G0-I(2.8MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780649800/Firmware__V5.5.820_260402_S3000712894.zip)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780649800/Firmware__V5.5.820_260402_S3000712894.zip), [DS-2CD1043G0-I(4MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780649800/Firmware__V5.5.820_260402_S3000712894.zip), DS-2CD1043G0-I(2.8MM)(B), [DS-2CD1143G0-IUF](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780649800/Firmware__V5.5.820_260402_S3000712894.zip), [DS-2CD1143G0-IUF(2.8MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780649800/Firmware__V5.5.820_260402_S3000712894.zip)(B) | 2023-11-09 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780649800/Firmware__V5.5.820_260402_S3000712894.zip) | Modify Function Note · [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202401/releasenote%5CNetwork_Camera-V5.5.820_SP1_Release_Note-IPC_E7S_231109.pdf) |

</details>


<details>
<summary><h2>DS-2CD1043G2-I(UF) - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.41 | Applied to: [DS-2CD1043G2-I(UF)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.8.41_260401_S3000712568.zip), [DS-2CD1043G2-I(2.8MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.8.41_260401_S3000712568.zip)(BLACK), [DS-2CD1043G2-LIU(F)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.8.41_260401_S3000712568.zip), [[DS-2CD1043G2-LIU(2.8MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.8.41_260401_S3000712568.zip)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.8.41_260401_S3000712568.zip), [[DS-2CD1043G2-LIU(4MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.8.41_260401_S3000712568.zip)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.8.41_260401_S3000712568.zip), DS-2CD1043G2-LIU(2.8MM)(T), DS-2CD1043G2-LIU(4MM)(T), [DS-2CD1043G2-LIUF(2.8MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.8.41_260401_S3000712568.zip) | 2026-04-01 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.8.41_260401_S3000712568.zip) | 1. Fixed some bugs to enhance system stability. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202604/releasenote%5CNetwork_Camera-V5.8.41_SP1_Release_Note-E10.pdf) |

</details>


<details>
<summary><h2>DS-2CD1043G2-LIDUF/4G/SL - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.34 | Applied to: [DS-2CD1043G2-LIDUF/4G/SL](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780617965/Firmware__V5.8.34_260403_S3000712883.zip), [DS-2CD1043G2-LIDUF/4G/SL(2.8MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780617965/Firmware__V5.8.34_260403_S3000712883.zip)/O-STD/EU, [DS-2CD1043G2-LIDUF/4G/SL(4MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780617965/Firmware__V5.8.34_260403_S3000712883.zip), [[[DS-2CD1043G2-LIDUF/4G/SL(4)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780617965/Firmware__V5.8.34_260403_S3000712883.zip)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780617965/Firmware__V5.8.34_260403_S3000712883.zip)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780617965/Firmware__V5.8.34_260403_S3000712883.zip)/O-STD/IN/INA, [[DS-2CD1043G2-LIDUF/4G/SL(2.8)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780617965/Firmware__V5.8.34_260403_S3000712883.zip)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780617965/Firmware__V5.8.34_260403_S3000712883.zip)OSTD/LA/FUS, DS-2CD1043G2-LIDUF/4G/SL(4)/O-STD/LA/FUS, DS-2CD1043G2-LIDUF/4G/SL(2.8)OSTD/JP/FUS, DS-2CD1043G2-LIDUF/4G/SL(4)/O-STD/JP/FUS | 2026-04-03 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780617965/Firmware__V5.8.34_260403_S3000712883.zip) | — |

</details>


<details>
<summary><h2>DS-2CD1043G2-LIUF/SL - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.41 | Applied to: [DS-2CD1043G2-LIUF/SL](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.8.41_260401_S3000712568.zip), [DS-2CD1043G2-LIUF/SL(2.8MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.8.41_260401_S3000712568.zip), [DS-2CD1043G2-LIUF/SL(4MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.8.41_260401_S3000712568.zip), [DS-2CD1047G2H-LIU(F)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.8.41_260401_S3000712568.zip), [[DS-2CD1047G2H-LIU(2.8MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.8.41_260401_S3000712568.zip)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.8.41_260401_S3000712568.zip)(BLACK), [DS-2CD1047G2H-LIUF(2.8MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.8.41_260401_S3000712568.zip), [DS-2CD1047G2H-LIUF(4MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.8.41_260401_S3000712568.zip), DS-2CD1047G2H-LIU(2.8MM) | 2026-04-01 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.8.41_260401_S3000712568.zip) | 1. Fixed some bugs to enhance system stability. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202604/releasenote%5CNetwork_Camera-V5.8.41_SP1_Release_Note-E10.pdf) |

</details>


<details>
<summary><h2>DS-2CD1047G3H-LIU(F)(/SL)(/SRB) - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.32 | Applied to: [DS-2CD1047G3H-LIU(F)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780390224/Firmware__V5.8.32_260320_S3000708449.zip)(/SL)(/SRB), [DS-2CD1047G3H-LIU(2.8MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780390224/Firmware__V5.8.32_260320_S3000708449.zip), [DS-2CD1047G3H-LIU(4MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780390224/Firmware__V5.8.32_260320_S3000708449.zip), [DS-2CD1047G3H-LIUF/SL(2.8MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780390224/Firmware__V5.8.32_260320_S3000708449.zip), [DS-2CD1047G3H-LIUF/SL(4MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780390224/Firmware__V5.8.32_260320_S3000708449.zip), [DS-2CD1047G3H-LIUF/SRB(2.8MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780390224/Firmware__V5.8.32_260320_S3000708449.zip), [DS-2CD1047G3H-LIUF/SRB(4MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780390224/Firmware__V5.8.32_260320_S3000708449.zip), [DS-2CD1047G3H-LIUF(2.8MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780390224/Firmware__V5.8.32_260320_S3000708449.zip) | 2026-03-20 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780390224/Firmware__V5.8.32_260320_S3000708449.zip) | — |

</details>


<details>
<summary><h2>DS-2CD1053G0-I(UF) - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.89 | Applied to: [DS-2CD1053G0-I(UF)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1770319630/87acab3e-5d46-45cd-88c4-87b51139b600.zip), [[DS-2CD1053G0-I(2.8MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1770319630/87acab3e-5d46-45cd-88c4-87b51139b600.zip)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1770319630/87acab3e-5d46-45cd-88c4-87b51139b600.zip), [[DS-2CD1053G0-I(4MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1770319630/87acab3e-5d46-45cd-88c4-87b51139b600.zip)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1770319630/87acab3e-5d46-45cd-88c4-87b51139b600.zip), DS-2CD1053G0-I(2.8MM)(B), DS-2CD1053G0-I(4MM)(B), [DS-2CD1153G0-I](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1770319630/87acab3e-5d46-45cd-88c4-87b51139b600.zip), [DS-2CD1153G0-I(2.8MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1770319630/87acab3e-5d46-45cd-88c4-87b51139b600.zip), [DS-2CD1153G0-I(4MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1770319630/87acab3e-5d46-45cd-88c4-87b51139b600.zip) | 2021-04-29 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1770319630/87acab3e-5d46-45cd-88c4-87b51139b600.zip) | Improved Features · After the device is upgraded to V5.5.89 version, it cannot be upgraded back to a version lower · than V5.5.89. · [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202312/releasenote%5CNetwork_Camera_V5.5.89_Release_Note_--G0.pdf) |

</details>


<details>
<summary><h2>DS-2CD1063G2-LIU(F) - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.41 | Applied to: [DS-2CD1063G2-LIU(F)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.8.41_260401_S3000712568.zip), [DS-2CD1063G2-LIU(2.8MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.8.41_260401_S3000712568.zip), [DS-2CD1063G2-LIU(4MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.8.41_260401_S3000712568.zip), [DS-2CD1063G2-LIUF(2.8MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.8.41_260401_S3000712568.zip), [DS-2CD1063G2-LIUF(4MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.8.41_260401_S3000712568.zip), [DS-2CD1063G2-LIUF/SL](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.8.41_260401_S3000712568.zip), [DS-2CD1063G2-LIUF/SL(2.8MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.8.41_260401_S3000712568.zip), [DS-2CD1063G2-LIUF/SL(4MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.8.41_260401_S3000712568.zip) | 2026-04-01 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.8.41_260401_S3000712568.zip) | 1. Fixed some bugs to enhance system stability. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202604/releasenote%5CNetwork_Camera-V5.8.41_SP1_Release_Note-G6.pdf) |

</details>


<details>
<summary><h2>DS-2CD1183G0-I - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD1183G0-I](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1776295655/Firmware__V5.7.23_260320_S3000708441.zip), [DS-2CD1183G0-I(2.8MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1776295655/Firmware__V5.7.23_260320_S3000708441.zip), [DS-2CD1183G0-I(4MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1776295655/Firmware__V5.7.23_260320_S3000708441.zip), [DS-2CD2026G2-I(U)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1776295655/Firmware__V5.7.23_260320_S3000708441.zip), [[DS-2CD2026G2-I(2.8MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1776295655/Firmware__V5.7.23_260320_S3000708441.zip)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1776295655/Firmware__V5.7.23_260320_S3000708441.zip), [[DS-2CD2026G2-I(4MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1776295655/Firmware__V5.7.23_260320_S3000708441.zip)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1776295655/Firmware__V5.7.23_260320_S3000708441.zip), DS-2CD2026G2-I(2.8MM)(D), DS-2CD2026G2-I(4MM)(D) | 2026-03-20 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1776295655/Firmware__V5.7.23_260320_S3000708441.zip) | 1. PTRZ product shading hood motor motion logic optimization: · 1) After the movement in the P and T directions comes to a complete stop, the sunshade motor lifts · the ball cover on top again . When starting to move, the sunshade motor will retract first, and only · [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202410/releasenote%5CNetwork_Camera-V5.7.18_240826_Release_Note-G5.pdf) |
| 5.7.18 | Applied to: [DS-2CD1183G0-I](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1778212177/Firmware__V5.7.18_240826_S3000597013.zip), [DS-2CD1183G0-I(2.8MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1778212177/Firmware__V5.7.18_240826_S3000597013.zip), [DS-2CD1183G0-I(4MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1778212177/Firmware__V5.7.18_240826_S3000597013.zip), [DS-2CD1183G0-IUF](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1778212177/Firmware__V5.7.18_240826_S3000597013.zip), [DS-2CD1183G0-IUF(2.8MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1778212177/Firmware__V5.7.18_240826_S3000597013.zip), [DS-2CD1383G0-I](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1778212177/Firmware__V5.7.18_240826_S3000597013.zip), [DS-2CD1383G0-I(2.8MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1778212177/Firmware__V5.7.18_240826_S3000597013.zip), [DS-2CD1383G0-I(4MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1778212177/Firmware__V5.7.18_240826_S3000597013.zip) | 2024-08-26 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1778212177/Firmware__V5.7.18_240826_S3000597013.zip) | 1. PTRZ product shading hood motor motion logic optimization: · 1) After the movement in the P and T directions comes to a complete stop, the sunshade motor lifts · the ball cover on top again . When starting to move, the sunshade motor will retract first, and only · [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202410/releasenote%5CNetwork_Camera-V5.7.18_240826_Release_Note-G5.pdf) |

</details>


<details>
<summary><h2>DS-2CD1363G2P-LIUF - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.11 | Applied to: [DS-2CD1363G2P-LIUF/SL(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780599961/Firmware__V5.8.110_260421_S3000718008.zip) | 2025-10-29 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780599961/Firmware__V5.8.110_260421_S3000718008.zip) | — |

</details>


<details>
<summary><h2>DS-2CD1363G2P-LIUF/S(L)(RB) - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.12 | Applied to: [DS-2CD1363G2P-LIUF/S(L)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780617965/Firmware__V5.8.12_260407_S3000714560.zip)(RB), [DS-2CD1363G2P-LIUF/SL(2.8MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780617965/Firmware__V5.8.12_260407_S3000714560.zip), [DS-2CD1367G2HP-LIUF/S(L)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780617965/Firmware__V5.8.12_260407_S3000714560.zip)(RB), [DS-2CD1367G2HP-LIUF/SRB(2.8MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780617965/Firmware__V5.8.12_260407_S3000714560.zip), [DS-2CD1367G2HP-LIUF/SL(2.8MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780617965/Firmware__V5.8.12_260407_S3000714560.zip), [DS-2CD1383G2P-LIUF/S(L)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780617965/Firmware__V5.8.12_260407_S3000714560.zip)(RB), [DS-2CD1383G2P-LIUF/SRB(2MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780617965/Firmware__V5.8.12_260407_S3000714560.zip), [DS-2CD1383G2P-LIUF/SL(2MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780617965/Firmware__V5.8.12_260407_S3000714560.zip) | 2026-04-16 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780617965/Firmware__V5.8.12_260407_S3000714560.zip) | some bugs to enhance system stability. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202605/releasenote%5CNetwork_Camera-V5.8.12_260416_Release_IPCE_P_E11.pdf) |

</details>


<details>
<summary><h2>DS-2CD1367G2HP-LIUF - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.11 | Applied to: [DS-2CD1367G2HP-LIUF/SL(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780599961/Firmware__V5.8.110_260421_S3000718008.zip) | 2025-10-29 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780599961/Firmware__V5.8.110_260421_S3000718008.zip) | — |

</details>


<details>
<summary><h2>DS-2CD1383G0-I - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.19 | Applied to: [DS-2CD1383G0-I](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1770537966/Firmware__V5.7.19_241207_S3000618481.zip), [DS-2CD1383G0-I(2.8MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1770537966/Firmware__V5.7.19_241207_S3000618481.zip), [DS-2CD1383G0-I(4MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1770537966/Firmware__V5.7.19_241207_S3000618481.zip) | 2024-12-07 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1770537966/Firmware__V5.7.19_241207_S3000618481.zip) | 1. Change of capture mode for 6/8 MP camera：P system delet e 3200x180025, only reserved · 3840x216025, The N system remains unchanged. · 2. Newly Add 38 boxes camera: DS-2CD3843G2-AP2. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.19_241207_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD1383G2P-LIUF - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.11 | Applied to: [DS-2CD1383G2P-LIUF/SL(2mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780599961/Firmware__V5.8.110_260421_S3000718008.zip) | 2025-10-29 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780599961/Firmware__V5.8.110_260421_S3000718008.zip) | — |

</details>


<details>
<summary><h2>DS-2CD1623G0-I(Z) - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.25 | Applied to: [DS-2CD1623G0-I(Z)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.7.25_260401_S3000715096.zip), [[DS-2CD1623G0-IZ(2.8-12MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.7.25_260401_S3000715096.zip)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.7.25_260401_S3000715096.zip), DS-2CD1623G0-IZ(2.8-12MM)(C), [DS-2CD1623G0-IZS(2.8-12MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.7.25_260401_S3000715096.zip)(C), [DS-2CD1643G0-I(Z)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.7.25_260401_S3000715096.zip), [[DS-2CD1643G0-IZ(2.8-12MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.7.25_260401_S3000715096.zip)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.7.25_260401_S3000715096.zip), [DS-2CD1643G0-I(2.8-12MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.7.25_260401_S3000715096.zip), DS-2CD1643G0-IZ(2.8-12MM)(C) | 2026-04-01 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.7.25_260401_S3000715096.zip) | Fixed some bugs to enhance system stability. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202605/releasenote%5CNetwork_Camera-V5.7.25_260401_Release_Note-E8.pdf) |
| 5.5.800 | Applied to: [DS-2CD1623G0-I(Z)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1769449958/5d0fc94c-b0e2-48ab-9a55-9c49876b7081.zip), [DS-2CD1623G0-IZ(2.8-12MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1769449958/5d0fc94c-b0e2-48ab-9a55-9c49876b7081.zip), [DS-2CD1723G0-I(Z)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1769449958/5d0fc94c-b0e2-48ab-9a55-9c49876b7081.zip), [DS-2CD1723G0-I(2.8-12MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1769449958/5d0fc94c-b0e2-48ab-9a55-9c49876b7081.zip), [DS-2CD1723G0-IZ(2.8-12MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1769449958/5d0fc94c-b0e2-48ab-9a55-9c49876b7081.zip) | 2021-06-28 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1769449958/5d0fc94c-b0e2-48ab-9a55-9c49876b7081.zip) | — |

</details>


<details>
<summary><h2>DS-2CD1T63G2P-LIUF - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.11 | Applied to: [DS-2CD1T63G2P-LIUF/SL(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780599961/Firmware__V5.8.110_260421_S3000718008.zip) | 2025-10-29 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780599961/Firmware__V5.8.110_260421_S3000718008.zip) | the screen flickering issue for 4G/WI-FI cameras · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202511/releasenote%5CNetwork_Camera-V5.8.11_SP1_251029_Release_Note-IPCE_P_E11.pdf) |

</details>


<details>
<summary><h2>DS-2CD1T67G2HP-LIUF - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.11 | Applied to: [DS-2CD1T67G2HP-LIUF/SRB(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780599961/Firmware__V5.8.110_260421_S3000718008.zip) | 2025-10-29 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780599961/Firmware__V5.8.110_260421_S3000718008.zip) | the screen flickering issue for 4G/WI-FI cameras · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202511/releasenote%5CNetwork_Camera-V5.8.11_SP1_251029_Release_Note-IPCE_P_E11.pdf) |

</details>


<details>
<summary><h2>DS-2CD1T83G2P-LIUF - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.11 | Applied to: [DS-2CD1T83G2P-LIUF/SL(2mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780599961/Firmware__V5.8.110_260421_S3000718008.zip) | 2025-10-29 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780599961/Firmware__V5.8.110_260421_S3000718008.zip) | the screen flickering issue for 4G/WI-FI cameras · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202511/releasenote%5CNetwork_Camera-V5.8.11_SP1_251029_Release_Note-IPCE_P_E11.pdf) |

</details>


<details>
<summary><h2>DS-2CD20123G2-LI(U)Y - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.3 | Applied to: [DS-2CD20123G2-LI(U)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780649800/Firmware__V5.8.3_260402_S3000712976.zip)Y, [DS-2CD20123G2-LIY(2.8MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780649800/Firmware__V5.8.3_260402_S3000712976.zip), [DS-2CD20123G2-LIY(4MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780649800/Firmware__V5.8.3_260402_S3000712976.zip), [DS-2CD20123G2-LIY(6MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780649800/Firmware__V5.8.3_260402_S3000712976.zip), [[DS-2CD20123G2-LIUY(2.8MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780649800/Firmware__V5.8.3_260402_S3000712976.zip)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780649800/Firmware__V5.8.3_260402_S3000712976.zip)(BLACK), DS-2CD20123G2-LIUY(2.8MM), [DS-2CD20123G2-LIUY(4MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780649800/Firmware__V5.8.3_260402_S3000712976.zip), [DS-2CD20123G2-LIUY(6MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780649800/Firmware__V5.8.3_260402_S3000712976.zip) | 2026-03-20 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780649800/Firmware__V5.8.3_260402_S3000712976.zip) | 1. Fixed the issue of device IP modification failure under the SADPV3.1.1 version and resolved · network parameter configuration error. · 2. Fixed some bugs to enhance system stability. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202604/releasenote%5CNetwork_Camera-V5.8.3_SP1_260320_Release_Note-IPCE_G9.pdf) |

</details>


<details>
<summary><h2>DS-2CD20126G3-IUY/S(L)(RB) - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.3 | Applied to: [DS-2CD20126G3-IUY/S(L)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780649800/Firmware__V5.8.3_260402_S3000712976.zip)(RB), [[DS-2CD20126G3-IUY/SRB(2.8MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780649800/Firmware__V5.8.3_260402_S3000712976.zip)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780649800/Firmware__V5.8.3_260402_S3000712976.zip)EFO-STDBLACK, DS-2CD20126G3-IUY/SRB(2.8MM)(EF), [DS-2CD20126G3-IUY/SRB(4MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780649800/Firmware__V5.8.3_260402_S3000712976.zip)(EF), [DS-2CD20126G3-IUY/SRB(6MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780649800/Firmware__V5.8.3_260402_S3000712976.zip)(EF), [[DS-2CD20126G3-IUY/SL(2.8MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780649800/Firmware__V5.8.3_260402_S3000712976.zip)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780649800/Firmware__V5.8.3_260402_S3000712976.zip)/EFO-STDBLACK, DS-2CD20126G3-IUY/SL(2.8MM)(EF), [DS-2CD20126G3-IUY/SL(4MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780649800/Firmware__V5.8.3_260402_S3000712976.zip)(EF) | 2026-03-20 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780649800/Firmware__V5.8.3_260402_S3000712976.zip) | 1. Fixed the issue of device IP modification failure under the SADPV3.1.1 version and resolved · network parameter configuration error. · 2. Fixed some bugs to enhance system stability. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202604/releasenote%5CNetwork_Camera-V5.8.3_SP1_260320_Release_Note-IPCE_G9.pdf) |

</details>


<details>
<summary><h2>DS-2CD2021G1-I(W) - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.800 | Applied to: [DS-2CD2021G1-I(W)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1771317420/2b726e56-901f-4e8d-9fd4-e9d67bc8e80a.zip), [DS-2CD2021G1-I(2.8MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1771317420/2b726e56-901f-4e8d-9fd4-e9d67bc8e80a.zip)(B), [DS-2CD2021G1-I(4MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1771317420/2b726e56-901f-4e8d-9fd4-e9d67bc8e80a.zip)(B), [DS-2CD2021G1-IDW](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1771317420/2b726e56-901f-4e8d-9fd4-e9d67bc8e80a.zip), [[DS-2CD2021G1-IDW1(2.8MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1771317420/2b726e56-901f-4e8d-9fd4-e9d67bc8e80a.zip)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1771317420/2b726e56-901f-4e8d-9fd4-e9d67bc8e80a.zip), DS-2CD2021G1-IDW1(2.8MM)(D), [DS-2CD2021G1-IDW1(4MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1771317420/2b726e56-901f-4e8d-9fd4-e9d67bc8e80a.zip)(D), [DS-2CD2121G0-I(W)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1771317420/2b726e56-901f-4e8d-9fd4-e9d67bc8e80a.zip)(S) | 2021-06-28 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1771317420/2b726e56-901f-4e8d-9fd4-e9d67bc8e80a.zip) | — |

</details>


<details>
<summary><h2>DS-2CD2023G0-I - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.6.821 | Applied to: [DS-2CD2023G0-I](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.6.821_260330_S3000711149.zip), [[DS-2CD2023G0-I(2.8MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.6.821_260330_S3000711149.zip)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.6.821_260330_S3000711149.zip)(BLACK), [[DS-2CD2023G0-I(4MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.6.821_260330_S3000711149.zip)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.6.821_260330_S3000711149.zip)(BLACK), DS-2CD2023G0-I(2.8MM), DS-2CD2023G0-I(4MM), [DS-2CD2023G0-I(6MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.6.821_260330_S3000711149.zip), [DS-2CD2025FHWD-I](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.6.821_260330_S3000711149.zip), [DS-2CD2025FHWD-I(2.8MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.6.821_260330_S3000711149.zip) | 2026-03-30 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.6.821_260330_S3000711149.zip) | — |

</details>


<details>
<summary><h2>DS-2CD2023G2-I - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.0 | Applied to: [DS-2CD2023G2-I(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780096165/Firmware__V5.7.0_230221_S3000488889.zip)(D) | 2024-10-23 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780096165/Firmware__V5.7.0_230221_S3000488889.zip) | 1. Fix the issue of no Motion Detection alarms for the cameras with live guard. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202507/releasenote%5CNetwork_Camera-V5.7.0_SP6_Release_Note-G6_I.pdf) |

</details>


<details>
<summary><h2>DS-2CD2023G2-I(U) - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.0 | Applied to: [DS-2CD2023G2-I(U)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780096165/Firmware__V5.7.0_230221_S3000488889.zip), [DS-2CD2023G2-I(2.8MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780096165/Firmware__V5.7.0_230221_S3000488889.zip)(D), [DS-2CD2023G2-I(4MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780096165/Firmware__V5.7.0_230221_S3000488889.zip)(D), [DS-2CD2023G2-I(6MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780096165/Firmware__V5.7.0_230221_S3000488889.zip)(D), [[DS-2CD2023G2-IU(2.8MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780096165/Firmware__V5.7.0_230221_S3000488889.zip)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780096165/Firmware__V5.7.0_230221_S3000488889.zip)(D), [DS-2CD2023G2-IU(4MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780096165/Firmware__V5.7.0_230221_S3000488889.zip)(D), [DS-2CD2023G2-IU(6MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780096165/Firmware__V5.7.0_230221_S3000488889.zip)(D), DS-2CD2023G2-IU(2.8MM) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780096165/Firmware__V5.7.0_230221_S3000488889.zip) | 1. Fix the issue of no Motion Detection alarms for the cameras with live guard. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202507/releasenote%5CNetwork_Camera-V5.7.0_SP6_Release_Note-G6_I.pdf) |

</details>


<details>
<summary><h2>DS-2CD2023G2-IU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.0 | Applied to: [DS-2CD2023G2-I(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780096165/Firmware__V5.7.0_230221_S3000488889.zip)(D) | 2024-10-23 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780096165/Firmware__V5.7.0_230221_S3000488889.zip) | 1. Fix the issue of no Motion Detection alarms for the cameras with live guard. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202507/releasenote%5CNetwork_Camera-V5.7.0_SP6_Release_Note-G6_I.pdf) |

</details>


<details>
<summary><h2>DS-2CD2025FHWD-I - IPC_G1 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.6.821 | Applied to: [DS-2CD2025FHWD-I](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.6.821_260330_S3000711149.zip), [DS-2CD2025FHWD-I(2.8MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.6.821_260330_S3000711149.zip), [DS-2CD2025FHWD-I(4MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.6.821_260330_S3000711149.zip), [DS-2CD2025FHWD-I(6MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.6.821_260330_S3000711149.zip), [DS-2CD2025FWD-I](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.6.821_260330_S3000711149.zip), [DS-2CD2025FWD-I(2.8MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.6.821_260330_S3000711149.zip), [DS-2CD2025FWD-I(4MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.6.821_260330_S3000711149.zip), [DS-2CD2025FWD-I(6MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.6.821_260330_S3000711149.zip) | 2023-08-31 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.6.821_260330_S3000711149.zip) | Improve real-time performance during multiple LiveView. · [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202401/releasenote%5CNetwork_Camera-V5.6.821_Release_Note-IPC_G1_230831.pdf) |

</details>


<details>
<summary><h2>DS-2CD2025FWD-I - IPC_G1 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.6.821 | Applied to: [DS-2CD2025FWD-I](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.6.821_260330_S3000711149.zip), [[DS-2CD2025FWD-I(2.8MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.6.821_260330_S3000711149.zip)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.6.821_260330_S3000711149.zip), [[DS-2CD2025FWD-I(4MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.6.821_260330_S3000711149.zip)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.6.821_260330_S3000711149.zip), [DS-2CD2025FWD-I(6MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.6.821_260330_S3000711149.zip), DS-2CD2025FWD-I(2.8MM)(BLACK), DS-2CD2025FWD-I(4MM)(BLACK), [DS-2CD2045FWD-I](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.6.821_260330_S3000711149.zip), [DS-2CD2045FWD-I(2.8MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.6.821_260330_S3000711149.zip)(BLACK) | 2023-08-31 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.6.821_260330_S3000711149.zip) | Improve real-time performance during multiple LiveView. · [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202401/releasenote%5CNetwork_Camera-V5.6.821_Release_Note-IPC_G1_230831.pdf) |

</details>


<details>
<summary><h2>DS-2CD2026G2-I - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.0 | Applied to: [DS-2CD2026G2-I(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780096165/Firmware__V5.7.0_230221_S3000488889.zip) | 2024-10-23 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780096165/Firmware__V5.7.0_230221_S3000488889.zip) | Version maintenance of HC library permission authentication issues. · [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202408/releasenote%5CNetwork_Camera-V5.5.820_Release_Note-G3.pdf) |

</details>


<details>
<summary><h2>DS-2CD2026G2-I(U) - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.820 | Applied to: [DS-2CD2026G2-I(U)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780649800/Firmware__V5.5.820_260402_S3000712894.zip), [[DS-2CD2026G2-I(2.8MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780649800/Firmware__V5.5.820_260402_S3000712894.zip)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780649800/Firmware__V5.5.820_260402_S3000712894.zip), [[DS-2CD2026G2-I(4MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780649800/Firmware__V5.5.820_260402_S3000712894.zip)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780649800/Firmware__V5.5.820_260402_S3000712894.zip), DS-2CD2026G2-I(2.8MM)(D), DS-2CD2026G2-I(4MM)(D), [DS-2CD2026G2-I(6MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780649800/Firmware__V5.5.820_260402_S3000712894.zip)(D), [DS-2CD2026G2-IU(2.8MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780649800/Firmware__V5.5.820_260402_S3000712894.zip), [DS-2CD2026G2-IU(4MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780649800/Firmware__V5.5.820_260402_S3000712894.zip) | 2026-03-27 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780649800/Firmware__V5.5.820_260402_S3000712894.zip) | Version maintenance of HC library permission authentication issues. · [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202408/releasenote%5CNetwork_Camera-V5.5.820_Release_Note-G3.pdf) |
| 5.5.800 | Applied to: [DS-2CD2026G2-I(U)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1778184600/7ddcc773-b084-4adc-a9e1-08ed4b8252f4.zip), [[DS-2CD2026G2-I(2.8MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1778184600/7ddcc773-b084-4adc-a9e1-08ed4b8252f4.zip)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1778184600/7ddcc773-b084-4adc-a9e1-08ed4b8252f4.zip), [[DS-2CD2026G2-I(4MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1778184600/7ddcc773-b084-4adc-a9e1-08ed4b8252f4.zip)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1778184600/7ddcc773-b084-4adc-a9e1-08ed4b8252f4.zip), DS-2CD2026G2-I(2.8MM)(D), DS-2CD2026G2-I(4MM)(D), [DS-2CD2026G2-I(6MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1778184600/7ddcc773-b084-4adc-a9e1-08ed4b8252f4.zip)(D), [DS-2CD2026G2-IU(2.8MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1778184600/7ddcc773-b084-4adc-a9e1-08ed4b8252f4.zip), [DS-2CD2026G2-IU(4MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1778184600/7ddcc773-b084-4adc-a9e1-08ed4b8252f4.zip) | 2021-10-09 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1778184600/7ddcc773-b084-4adc-a9e1-08ed4b8252f4.zip) | Version maintenance of HC library permission authentication issues. · [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202408/releasenote%5CNetwork_Camera-V5.5.820_Release_Note-G3.pdf) |

</details>


<details>
<summary><h2>DS-2CD2026G2-I-U- - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.820 | Applied to: [DS-2CD2026G2-I-U-](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780649800/Firmware__V5.5.820_260402_S3000712894.zip) | 2026-03-27 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780649800/Firmware__V5.5.820_260402_S3000712894.zip) | Version maintenance of HC library permission authentication issues. · [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202408/releasenote%5CNetwork_Camera-V5.5.820_Release_Note-G3.pdf) |

</details>


<details>
<summary><h2>DS-2CD2027G2-L(U) - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.820 | Applied to: [DS-2CD2027G2-L(U)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780649800/Firmware__V5.5.820_260402_S3000712894.zip), [DS-2CD2027G2-LU(2.8MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780649800/Firmware__V5.5.820_260402_S3000712894.zip), [DS-2CD2027G2-LU(4MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780649800/Firmware__V5.5.820_260402_S3000712894.zip), [[DS-2CD2027G2-L(2.8MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780649800/Firmware__V5.5.820_260402_S3000712894.zip)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780649800/Firmware__V5.5.820_260402_S3000712894.zip)(C), [[DS-2CD2027G2-L(4MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780649800/Firmware__V5.5.820_260402_S3000712894.zip)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780649800/Firmware__V5.5.820_260402_S3000712894.zip)(C), [DS-2CD2027G2-L(6MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780649800/Firmware__V5.5.820_260402_S3000712894.zip)(C), DS-2CD2027G2-L(2.8MM), DS-2CD2027G2-L(4MM) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780649800/Firmware__V5.5.820_260402_S3000712894.zip) | Version maintenance of HC library permission authentication issues. · [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202408/releasenote%5CNetwork_Camera-V5.5.820_Release_Note-G3.pdf) |

</details>


<details>
<summary><h2>DS-2CD2041G1-IDW - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.82 | Applied to: [DS-2CD2041G1-IDW](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780649800/Firmware__V5.5.820_260402_S3000712894.zip), [[[DS-2CD2041G1-IDW1(2.8MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780649800/Firmware__V5.5.820_260402_S3000712894.zip)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780649800/Firmware__V5.5.820_260402_S3000712894.zip)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780649800/Firmware__V5.5.820_260402_S3000712894.zip), DS-2CD2041G1-IDW1(2.8MM)(T), DS-2CD2041G1-IDW1(2.8MM)(D), [DS-2CD2051G1-IDW](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780649800/Firmware__V5.5.820_260402_S3000712894.zip), [DS-2CD2051G1-IDW1(2.8MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780649800/Firmware__V5.5.820_260402_S3000712894.zip), [DS-2CD2141G1-IDW](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780649800/Firmware__V5.5.820_260402_S3000712894.zip), [DS-2CD2141G1-IDW1(2.8MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780649800/Firmware__V5.5.820_260402_S3000712894.zip)(T) | 2019-01-30 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780649800/Firmware__V5.5.820_260402_S3000712894.zip) | Improved Features · After the device is upgraded to V5.5.89 version, it cannot be upgraded back to a version lower · than V5.5.89. · [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202312/releasenote%5CNetwork_Camera_V5.5.89_Release_Note_--G0.pdf) |

</details>


<details>
<summary><h2>DS-2CD2043G2-LIZ(2U)Y - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.32 | Applied to: [DS-2CD2043G2-LIZ(2U)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779320667/Firmware__V5.8.32_260330_S3000710893.zip)Y, [DS-2CD2043G2-LIZY(2.8/4MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779320667/Firmware__V5.8.32_260330_S3000710893.zip), [[DS-2CD2043G2-LIZ2UY(2.8/4MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779320667/Firmware__V5.8.32_260330_S3000710893.zip)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779320667/Firmware__V5.8.32_260330_S3000710893.zip), DS-2CD2043G2-LIZ2UY(2.8/4MM)/O-STD/BLACK, [DS-2CD2043G2-LIZ2UY/S(L)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779320667/Firmware__V5.8.32_260330_S3000710893.zip)(RB), [DS-2CD2043G2-LIZ2UY/SRB(2.8/4MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779320667/Firmware__V5.8.32_260330_S3000710893.zip), [DS-2CD2043G2-LIZ2UY/SRB(2.8/4)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779320667/Firmware__V5.8.32_260330_S3000710893.zip)O-STDBLACK, [DS-2CD2043G2-LIZ2UY/SL(2.8/4MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779320667/Firmware__V5.8.32_260330_S3000710893.zip) | 2026-03-30 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779320667/Firmware__V5.8.32_260330_S3000710893.zip) | New PT33 AI-ISP Camera Series · a) PTZ control is supported in the preview interface, with 16 preset points; patrol function and · motion tracking are available; one-click self-test is supported. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202604/releasenote%5CNetwork_Camera-V5.8.32_SP1_260330_Release_Note-H13U.pdf) |
| 5.8.30 | Applied to: [DS-2CD2043G2-LIZ(2U)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1777592712/Firmware__V5.8.30_251210_S3000691330.zip)Y, [DS-2CD2043G2-LIZY(2.8/4MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1777592712/Firmware__V5.8.30_251210_S3000691330.zip), [[DS-2CD2043G2-LIZ2UY(2.8/4MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1777592712/Firmware__V5.8.30_251210_S3000691330.zip)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1777592712/Firmware__V5.8.30_251210_S3000691330.zip), DS-2CD2043G2-LIZ2UY(2.8/4MM)/O-STD/BLACK, [DS-2CD2043G2-LIZ2UY/S(L)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1777592712/Firmware__V5.8.30_251210_S3000691330.zip)(RB), [DS-2CD2043G2-LIZ2UY/SRB(2.8/4MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1777592712/Firmware__V5.8.30_251210_S3000691330.zip), [DS-2CD2043G2-LIZ2UY/SRB(2.8/4)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1777592712/Firmware__V5.8.30_251210_S3000691330.zip)O-STDBLACK, [DS-2CD2043G2-LIZ2UY/SL(2.8/4MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1777592712/Firmware__V5.8.30_251210_S3000691330.zip) | 2025-12-10 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1777592712/Firmware__V5.8.30_251210_S3000691330.zip) | 1. New products: · 2,3 series fixed point-to-point zoom PTR camera, 2143G2, 2146G3, 3143G2. · 2 series 4MP PTRZ camera, 2X46G3, 2X47G3. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13U.pdf) |

</details>


<details>
<summary><h2>DS-2CD2045FWD-I - IPC_G1 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.6.821 | Applied to: [DS-2CD2045FWD-I](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.6.821_260330_S3000711149.zip), [[DS-2CD2045FWD-I(2.8MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.6.821_260330_S3000711149.zip)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.6.821_260330_S3000711149.zip)(BLACK), [[DS-2CD2045FWD-I(4MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.6.821_260330_S3000711149.zip)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.6.821_260330_S3000711149.zip)(BLACK), DS-2CD2045FWD-I(2.8MM), DS-2CD2045FWD-I(4MM), [DS-2CD2045FWD-I(6MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.6.821_260330_S3000711149.zip), [DS-2CD2065G1-I](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.6.821_260330_S3000711149.zip), [DS-2CD2065G1-I(2.8MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.6.821_260330_S3000711149.zip)(BLACK) | 2023-08-31 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.6.821_260330_S3000711149.zip) | Improve real-time performance during multiple LiveView. · [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202401/releasenote%5CNetwork_Camera-V5.6.821_Release_Note-IPC_G1_230831.pdf) |

</details>


<details>
<summary><h2>DS-2CD2046G3-IZ(2U)Y - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.32 | Applied to: [DS-2CD2046G3-IZ(2U)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780390224/Firmware__V5.8.32_260320_S3000708449.zip)Y, [DS-2CD2046G3-IZY(2.8/4MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780390224/Firmware__V5.8.32_260320_S3000708449.zip), [DS-2CD2046G3-IZ2UY(2.8/4MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780390224/Firmware__V5.8.32_260320_S3000708449.zip), [DS-2CD2046G3-IZ2UY/S(L)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780390224/Firmware__V5.8.32_260320_S3000708449.zip)(RB), [DS-2CD2046G3-IZ2UY/SRB(2.8/4)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780390224/Firmware__V5.8.32_260320_S3000708449.zip)O-STDBLACK, [DS-2CD2046G3-IZ2UY/SRB(2.8/4MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780390224/Firmware__V5.8.32_260320_S3000708449.zip), [[DS-2CD2046G3-IZ2UY/SL(2.8/4MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780390224/Firmware__V5.8.32_260320_S3000708449.zip)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780390224/Firmware__V5.8.32_260320_S3000708449.zip), DS-2CD2046G3-IZ2UY/SL(2.8/4MM)O-STDBLACK | 2026-03-30 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780390224/Firmware__V5.8.32_260320_S3000708449.zip) | New PT33 AI-ISP Camera Series · a) PTZ control is supported in the preview interface, with 16 preset points; patrol function and · motion tracking are available; one-click self-test is supported. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202604/releasenote%5CNetwork_Camera-V5.8.32_SP1_260330_Release_Note-H13U.pdf) |

</details>


<details>
<summary><h2>DS-2CD2046G3-IZ2UY/S(L)(RB) - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.32 | Applied to: [DS-2CD2046G3-IZ2UY/S(L)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780390224/Firmware__V5.8.32_260320_S3000708449.zip)(RB), [DS-2CD2046G3-IZ2UY/SRB(2.8/4)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780390224/Firmware__V5.8.32_260320_S3000708449.zip)O-STDBLACK, [DS-2CD2046G3-IZ2UY/SRB(2.8/4MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780390224/Firmware__V5.8.32_260320_S3000708449.zip), [[DS-2CD2046G3-IZ2UY/SL(2.8/4MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780390224/Firmware__V5.8.32_260320_S3000708449.zip)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780390224/Firmware__V5.8.32_260320_S3000708449.zip), DS-2CD2046G3-IZ2UY/SL(2.8/4MM)O-STDBLACK, [DS-2CD2047G3-LI(2U)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780390224/Firmware__V5.8.32_260320_S3000708449.zip)Y, [DS-2CD2047G3-LIY(2.8MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780390224/Firmware__V5.8.32_260320_S3000708449.zip), [DS-2CD2047G3-LIY(4MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780390224/Firmware__V5.8.32_260320_S3000708449.zip) | 2026-03-30 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780390224/Firmware__V5.8.32_260320_S3000708449.zip) | New PT33 AI-ISP Camera Series · a) PTZ control is supported in the preview interface, with 16 preset points; patrol function and · motion tracking are available; one-click self-test is supported. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202604/releasenote%5CNetwork_Camera-V5.8.32_SP1_260330_Release_Note-H13U.pdf) |

</details>


<details>
<summary><h2>DS-2CD2067G3-LI(2U)Y - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD2067G3-LI(2U)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1772836007/Firmware__V5.8.30_251210_S3000691342.zip)Y, [[DS-2CD2067G3-LI2UY(2.8MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1772836007/Firmware__V5.8.30_251210_S3000691342.zip)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1772836007/Firmware__V5.8.30_251210_S3000691342.zip), [DS-2CD2067G3-LI2UY(4MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1772836007/Firmware__V5.8.30_251210_S3000691342.zip), DS-2CD2067G3-LI2UY(2.8MM)(BLACK), [DS-2CD2067G3-LIY(2.8MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1772836007/Firmware__V5.8.30_251210_S3000691342.zip), [DS-2CD2067G3-LIY(4MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1772836007/Firmware__V5.8.30_251210_S3000691342.zip), [DS-2CD2067G3-LI2UY/S(L)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1772836007/Firmware__V5.8.30_251210_S3000691342.zip)(RB), [DS-2CD2067G3-LI2UY/SL(2.8MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1772836007/Firmware__V5.8.30_251210_S3000691342.zip) | 2025-12-10 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1772836007/Firmware__V5.8.30_251210_S3000691342.zip) | 1. New products: 3 series PTRZ camera, 3X6(8)6G3(PTRZ), 3X6(8)7G3(PTRZ). · (1) Support independent or combined movement in P/T/R directions, supports speed adjustment in gears 1 -7, · and maintains consistent position before and after restart and upgrade. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD2085G1-I - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.6.820 | Applied to: [DS-2CD2085G1-I](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1771663989/f18aceb7-b896-4c7d-ad2e-8f0d2a91bcc3.zip), [[DS-2CD2085G1-I(2.8MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1771663989/f18aceb7-b896-4c7d-ad2e-8f0d2a91bcc3.zip)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1771663989/f18aceb7-b896-4c7d-ad2e-8f0d2a91bcc3.zip)(BLACK), [[DS-2CD2085G1-I(4MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1771663989/f18aceb7-b896-4c7d-ad2e-8f0d2a91bcc3.zip)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1771663989/f18aceb7-b896-4c7d-ad2e-8f0d2a91bcc3.zip)(BLACK), DS-2CD2085G1-I(2.8MM), DS-2CD2085G1-I(4MM), [DS-2CD2085G1-I(6MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1771663989/f18aceb7-b896-4c7d-ad2e-8f0d2a91bcc3.zip), [DS-2CD2125FHWD-I(S)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1771663989/f18aceb7-b896-4c7d-ad2e-8f0d2a91bcc3.zip), [DS-2CD2125FHWD-I(2.8MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1771663989/f18aceb7-b896-4c7d-ad2e-8f0d2a91bcc3.zip) |  | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1771663989/f18aceb7-b896-4c7d-ad2e-8f0d2a91bcc3.zip) | Improved Features · Fixed some known bugs for ONVIF. · [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202301/Network%20Camera%20V5.6.820%20Release%20Note%20--G1.pdf) |

</details>


<details>
<summary><h2>DS-2CD2087G2-L(U) - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2087G2-L(U)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1778212177/Firmware__V5.7.23_260114_S3000702187.zip), [DS-2CD2087G2-LU(2.8MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1778212177/Firmware__V5.7.23_260114_S3000702187.zip)(C), [DS-2CD2087G2-LU(4MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1778212177/Firmware__V5.7.23_260114_S3000702187.zip)(C), [DS-2CD2087G2-LU(6MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1778212177/Firmware__V5.7.23_260114_S3000702187.zip)(C), [DS-2CD2087G2-L(2.8MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1778212177/Firmware__V5.7.23_260114_S3000702187.zip)(C), [DS-2CD2087G2-L(4MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1778212177/Firmware__V5.7.23_260114_S3000702187.zip)(C), [DS-2CD2087G2-L(6MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1778212177/Firmware__V5.7.23_260114_S3000702187.zip)(C), [DS-2CD2526G2-IS](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1778212177/Firmware__V5.7.23_260114_S3000702187.zip) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1778212177/Firmware__V5.7.23_260114_S3000702187.zip) | Associated camera model updates. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2087G3-LI(2U)Y - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.32 | Applied to: [DS-2CD2087G3-LI(2U)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780390224/Firmware__V5.8.32_260320_S3000708449.zip)Y, [DS-2CD2087G3-LI2UY(2.8MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780390224/Firmware__V5.8.32_260320_S3000708449.zip)(BLACK), [DS-2CD2087G3-LIY(2.8MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780390224/Firmware__V5.8.32_260320_S3000708449.zip), [DS-2CD2087G3-LIY(4MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780390224/Firmware__V5.8.32_260320_S3000708449.zip), [DS-2CD2167G3-LI(S2U)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780390224/Firmware__V5.8.32_260320_S3000708449.zip)Y, [[DS-2CD2167G3-LIS2UY(2.8MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780390224/Firmware__V5.8.32_260320_S3000708449.zip)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780390224/Firmware__V5.8.32_260320_S3000708449.zip), [DS-2CD2167G3-LIS2UY(4MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780390224/Firmware__V5.8.32_260320_S3000708449.zip), DS-2CD2167G3-LIS2UY(2.8MM)(BLACK) | 2026-03-30 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780390224/Firmware__V5.8.32_260320_S3000708449.zip) | 1. The 2 series products have added support for perimeter animals and non-motor vehicles. The · detection targets are set to animals and others by default. · 2. Add a master control switch（Device Linkage Control）for sound and flash alarm functions, · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202604/releasenote%5CNetwork_Camera-V5.8.32_SP1_260330_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD2121G1-IDW - IPC_E6 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.821 | Applied to: [DS-2CD2121G1-IDW](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1772754001/Firmware__V5.5.821_231108_S3000539548.zip), [[[DS-2CD2121G1-IDW1(2.8MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1772754001/Firmware__V5.5.821_231108_S3000539548.zip)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1772754001/Firmware__V5.5.821_231108_S3000539548.zip)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1772754001/Firmware__V5.5.821_231108_S3000539548.zip), [DS-2CD2121G1-IDW2(2.8MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1772754001/Firmware__V5.5.821_231108_S3000539548.zip), DS-2CD2121G1-IDW1(2.8MM)(D), DS-2CD2121G1-IDW1(2.8MM)(B), [DS-2CV2Q21FD-IW](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1772754001/Firmware__V5.5.821_231108_S3000539548.zip), [[DS-2CV2Q21FD-IW(2.8MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1772754001/Firmware__V5.5.821_231108_S3000539548.zip)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1772754001/Firmware__V5.5.821_231108_S3000539548.zip), DS-2CV2Q21FD-IW(2.8MM)(B) | 2023-11-08 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1772754001/Firmware__V5.5.821_231108_S3000539548.zip) | Optimization · Fixed the bug of EZVIZ. · Internal · [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202404/1712790068455/releasenote%5CIPC_E6_5.5.821_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2123G2-I - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.0 | Applied to: [DS-2CD2123G2-I(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780096165/Firmware__V5.7.0_230221_S3000488889.zip)(D)(BLACK) | 2024-10-23 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780096165/Firmware__V5.7.0_230221_S3000488889.zip) | 1. Fix the issue of no Motion Detection alarms for the cameras with live guard. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202507/releasenote%5CNetwork_Camera-V5.7.0_SP6_Release_Note-G6_I.pdf) |

</details>


<details>
<summary><h2>DS-2CD2123G2-IU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.0 | Applied to: [DS-2CD2123G2-IU(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780096165/Firmware__V5.7.0_230221_S3000488889.zip)(D) | 2024-10-23 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780096165/Firmware__V5.7.0_230221_S3000488889.zip) | 1. Fix the issue of no Motion Detection alarms for the cameras with live guard. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202507/releasenote%5CNetwork_Camera-V5.7.0_SP6_Release_Note-G6_I.pdf) |

</details>


<details>
<summary><h2>DS-2CD2126G2-I - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.0 | Applied to: [DS-2CD2126G2-ISU(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780096165/Firmware__V5.7.0_230221_S3000488889.zip)(C) | 2024-10-23 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780096165/Firmware__V5.7.0_230221_S3000488889.zip) | 1. Change of capture mode for 6/8 MP camera：P system delet e 3200x180025, only reserved · 3840x216025, The N system remains unchanged. · 2. Newly Add 38 boxes camera: DS-2CD3843G2-AP2. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.19_241207_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2143G2-LIPTRZ(S2U)Y - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD2143G2-LIPTRZ(S2U)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1774474874/Firmware__V5.8.32_260320_S3000708455.zip)Y, [DS-2CD2143G2-LIPTRZS2UY(2.8/4MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1774474874/Firmware__V5.8.32_260320_S3000708455.zip), [[DS-2CD2143G2-LIPTRZY(2.8/4MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1774474874/Firmware__V5.8.32_260320_S3000708455.zip)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1774474874/Firmware__V5.8.32_260320_S3000708455.zip), DS-2CD2143G2-LIPTRZY(2.8/4MM)/O-STDBLACK, [DS-2CD2143G2-LIPTRZS2UY(2.8/4)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1774474874/Firmware__V5.8.32_260320_S3000708455.zip)O-STDBLACK | 2026-03-20 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1774474874/Firmware__V5.8.32_260320_S3000708455.zip) | 1. New products: · 2,3 series fixed point-to-point zoom PTR camera, 2143G2, 2146G3, 3143G2. · 2 series 4MP PTRZ camera, 2X46G3, 2X47G3. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13U.pdf) |

</details>


<details>
<summary><h2>DS-2CD23127G3P-LIS2UY/S(L)(RB) - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.110 | Applied to: [DS-2CD23127G3P-LIS2UY/S(L)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780599961/Firmware__V5.8.110_260421_S3000718008.zip)(RB), [[DS-2CD23127G3P-LIS2UY/SRB(180°)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780599961/Firmware__V5.8.110_260421_S3000718008.zip)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780599961/Firmware__V5.8.110_260421_S3000718008.zip), DS-2CD23127G3P-LIS2UY/SRB(180°)OSTDBLACK, [[DS-2CD23127G3P-LIS2UY/SL(180°)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780599961/Firmware__V5.8.110_260421_S3000718008.zip)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780599961/Firmware__V5.8.110_260421_S3000718008.zip)O-STDBLACK, DS-2CD23127G3P-LIS2UY/SL(180°), [DS-2CD23167G3P-LIS2UY/S(L)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780599961/Firmware__V5.8.110_260421_S3000718008.zip)(RB), [DS-2CD23167G3P-LIS2UY/SRB(180°)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780599961/Firmware__V5.8.110_260421_S3000718008.zip), [DS-2CD23167G3P-LIS2UY/SL(180°)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780599961/Firmware__V5.8.110_260421_S3000718008.zip) | 2026-04-21 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780599961/Firmware__V5.8.110_260421_S3000718008.zip) | — |

</details>


<details>
<summary><h2>DS-2CD2323G2-I - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.0 | Applied to: [DS-2CD2323G2-I(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780096165/Firmware__V5.7.0_230221_S3000488889.zip)(D) | 2024-10-23 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780096165/Firmware__V5.7.0_230221_S3000488889.zip) | 1. Fix the issue of no Motion Detection alarms for the cameras with live guard. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202507/releasenote%5CNetwork_Camera-V5.7.0_SP6_Release_Note-G6_I.pdf) |

</details>


<details>
<summary><h2>DS-2CD2323G2-I(U) - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.0 | Applied to: [DS-2CD2323G2-I(U)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780096165/Firmware__V5.7.0_230221_S3000488889.zip), [[DS-2CD2323G2-I(2.8MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780096165/Firmware__V5.7.0_230221_S3000488889.zip)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780096165/Firmware__V5.7.0_230221_S3000488889.zip)(D), [[DS-2CD2323G2-I(4MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780096165/Firmware__V5.7.0_230221_S3000488889.zip)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780096165/Firmware__V5.7.0_230221_S3000488889.zip)(D), [[DS-2CD2323G2-IU(2.8MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780096165/Firmware__V5.7.0_230221_S3000488889.zip)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780096165/Firmware__V5.7.0_230221_S3000488889.zip), [DS-2CD2323G2-IU(4MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780096165/Firmware__V5.7.0_230221_S3000488889.zip), DS-2CD2323G2-I(2.8MM), DS-2CD2323G2-I(4MM), DS-2CD2323G2-IU(2.8MM)(D) | 2024-10-23 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780096165/Firmware__V5.7.0_230221_S3000488889.zip) | 1. Fix the issue of no Motion Detection alarms for the cameras with live guard. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202507/releasenote%5CNetwork_Camera-V5.7.0_SP6_Release_Note-G6_I.pdf) |

</details>


<details>
<summary><h2>DS-2CD2323G2-IU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.0 | Applied to: [DS-2CD2323G2-I(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780096165/Firmware__V5.7.0_230221_S3000488889.zip)(D) | 2024-10-23 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780096165/Firmware__V5.7.0_230221_S3000488889.zip) | 1. Fix the issue of no Motion Detection alarms for the cameras with live guard. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202507/releasenote%5CNetwork_Camera-V5.7.0_SP6_Release_Note-G6_I.pdf) |

</details>


<details>
<summary><h2>DS-2CD2326G1-I/SL - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.6.0 | Applied to: [DS-2CD2326G1-I/SL](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1771404236/18db80e0-2712-4496-8bd3-646f5014a59b.zip), [DS-2CD2326G1-I/SL(2.8MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1771404236/18db80e0-2712-4496-8bd3-646f5014a59b.zip), [DS-2CD2326G1-I/SL(4MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1771404236/18db80e0-2712-4496-8bd3-646f5014a59b.zip), [DS-2CD2346G1-I/SL](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1771404236/18db80e0-2712-4496-8bd3-646f5014a59b.zip), [DS-2CD2346G1-I/SL(4MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1771404236/18db80e0-2712-4496-8bd3-646f5014a59b.zip), [DS-2CD2346G1-I/SL(2.8MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1771404236/18db80e0-2712-4496-8bd3-646f5014a59b.zip), [DS-2CD2646G1-IZS](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1771404236/18db80e0-2712-4496-8bd3-646f5014a59b.zip), [DS-2CD2646G1-IZS(2.8-12MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1771404236/18db80e0-2712-4496-8bd3-646f5014a59b.zip) | 2019-05-07 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1771404236/18db80e0-2712-4496-8bd3-646f5014a59b.zip) | — |

</details>


<details>
<summary><h2>DS-2CD2326G2-I - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.0 | Applied to: [DS-2CD2326G2-IU(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780096165/Firmware__V5.7.0_230221_S3000488889.zip) | 2024-10-23 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780096165/Firmware__V5.7.0_230221_S3000488889.zip) | 1. Improved Features  Fix security issue in ISAPI. · [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/330c4c2c-5730-4877-a942-0be87cea67ca.pdf) |

</details>


<details>
<summary><h2>DS-2CD2326G2-I(U) - IPC_G3 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.800 | Applied to: [DS-2CD2326G2-I(U)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1770450029/IPC_G3_EN_STD_5.5.820_220520.zip), [DS-2CD2326G2-IU(2.8MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1770450029/IPC_G3_EN_STD_5.5.820_220520.zip), [DS-2CD2326G2-IU(4MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1770450029/IPC_G3_EN_STD_5.5.820_220520.zip), [DS-2CD2326G2-IU(6MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1770450029/IPC_G3_EN_STD_5.5.820_220520.zip), [[DS-2CD2326G2-I(2.8MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1770450029/IPC_G3_EN_STD_5.5.820_220520.zip)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1770450029/IPC_G3_EN_STD_5.5.820_220520.zip), [[DS-2CD2326G2-I(4MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1770450029/IPC_G3_EN_STD_5.5.820_220520.zip)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1770450029/IPC_G3_EN_STD_5.5.820_220520.zip), DS-2CD2326G2-I(2.8MM)(D), DS-2CD2326G2-I(4MM)(D) | 2022-05-20 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1770450029/IPC_G3_EN_STD_5.5.820_220520.zip) | 1. Improved Features  Fix security issue in ISAPI. · [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/330c4c2c-5730-4877-a942-0be87cea67ca.pdf) |

</details>


<details>
<summary><h2>DS-2CD2326G2-I-U- - IPC_G3 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.0 | Applied to: [DS-2CD2326G2-I-U-](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780096165/Firmware__V5.7.0_230221_S3000488889.zip) | 2026-03-27 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780096165/Firmware__V5.7.0_230221_S3000488889.zip) | 1. Improved Features  Fix security issue in ISAPI. · [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/330c4c2c-5730-4877-a942-0be87cea67ca.pdf) |
| 5.5.800 | Applied to: [DS-2CD2326G2-I-U-](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.7.0_260327_S3000711576.zip) | 2026-03-27 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779747633/Firmware__V5.7.0_260327_S3000711576.zip) | 1. Improved Features  Fix security issue in ISAPI. · [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/330c4c2c-5730-4877-a942-0be87cea67ca.pdf) |

</details>


<details>
<summary><h2>DS-2CD2326G2-ISU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.0 | Applied to: [DS-2CD2326G2-ISU/SL(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780096165/Firmware__V5.7.0_230221_S3000488889.zip)(D) | 2024-10-23 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780096165/Firmware__V5.7.0_230221_S3000488889.zip) | 1. Fix the issue of no Motion Detection alarms for the cameras with live guard. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202507/releasenote%5CNetwork_Camera-V5.7.0_SP6_Release_Note-G6_I.pdf) |

</details>


<details>
<summary><h2>DS-2CD2343G2D-LIZ2UY - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.11 | Applied to: [DS-2CD2343G2D-LIZ2UY/SL(2.8/4mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780599961/Firmware__V5.8.110_260421_S3000718008.zip) | 2025-12-16 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780599961/Firmware__V5.8.110_260421_S3000718008.zip) | Fix the network abnormal issue. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.8.11_251216_Release_Note-IPCE_D_H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD2343G2D-LIZ2UY/S(L)(RB) - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.11 | Applied to: [DS-2CD2343G2D-LIZ2UY/S(L)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780599961/Firmware__V5.8.110_260421_S3000718008.zip)(RB), [DS-2CD2343G2D-LIZ2UY/SL(2.8/4MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780599961/Firmware__V5.8.110_260421_S3000718008.zip), [DS-2CD2343G2D-LIZ2UY/SRB(2.8/4MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780599961/Firmware__V5.8.110_260421_S3000718008.zip), [DS-2CD2343G2D-LIZ2UY/SL(2.8/4)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780599961/Firmware__V5.8.110_260421_S3000718008.zip)O-STDBLACK, [DS-2CD2343G2D-LIZ2UY/SRB(2.8/4)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780599961/Firmware__V5.8.110_260421_S3000718008.zip)OSTDBLACK | 2025-12-16 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780599961/Firmware__V5.8.110_260421_S3000718008.zip) | Fix the network abnormal issue. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.8.11_251216_Release_Note-IPCE_D_H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD2343G2P-LISU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.11 | Applied to: [DS-2CD2343G2P-LISU/SL(180°)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780599961/Firmware__V5.8.110_260421_S3000718008.zip) | 2025-10-29 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780599961/Firmware__V5.8.110_260421_S3000718008.zip) | the screen flickering issue for 4G/WI-FI cameras · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.8.11_SP1_251029_Release_Note-IPCE_P_E11.pdf) |

</details>


<details>
<summary><h2>DS-2CD2346G3D-IZ2UY - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.11 | Applied to: [DS-2CD2346G3D-IZ2UY/SRB(2.8/4)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780599961/Firmware__V5.8.110_260421_S3000718008.zip)O-STDBLACK | 2025-12-16 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780599961/Firmware__V5.8.110_260421_S3000718008.zip) | Fix the network abnormal issue. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.8.11_251216_Release_Note-IPCE_D_H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD2346G3D-IZ2UY-S-L--RB- - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.11 | Applied to: [DS-2CD2346G3D-IZ2UY-S-L--RB-](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780599961/Firmware__V5.8.110_260421_S3000718008.zip) | 2026-03-26 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780599961/Firmware__V5.8.110_260421_S3000718008.zip) | some bugs to enhance system stability. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202605/releasenote%5CNetwork_Camera-V5.8.11_260326_Release_IPCE_D_H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD2346G3D-IZ2UY/S(L)(RB) - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.11 | Applied to: [DS-2CD2346G3D-IZ2UY/S(L)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780599961/Firmware__V5.8.110_260421_S3000718008.zip)(RB), [DS-2CD2346G3D-IZ2UY/SRB(2.8/4)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780599961/Firmware__V5.8.110_260421_S3000718008.zip)O-STDBLACK, [DS-2CD2346G3D-IZ2UY/SRB(2.8/4MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780599961/Firmware__V5.8.110_260421_S3000718008.zip), [DS-2CD2346G3D-IZ2UY/SL(2.8/4MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780599961/Firmware__V5.8.110_260421_S3000718008.zip), [DS-2CD2346G3D-IZ2UY/SL(2.8/4)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780599961/Firmware__V5.8.110_260421_S3000718008.zip)O-STDBLACK, [DS-2CD3343G2/X2-LIZSUY/SL](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780599961/Firmware__V5.8.110_260421_S3000718008.zip), [DS-2CD3343G2/X2-LIZSUY/SL(2.8/4MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780599961/Firmware__V5.8.110_260421_S3000718008.zip)O-STD | 2026-03-26 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780599961/Firmware__V5.8.110_260421_S3000718008.zip) | some bugs to enhance system stability. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202605/releasenote%5CNetwork_Camera-V5.8.11_260326_Release_IPCE_D_H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD2347G3P-LIS2UY/S(L)(RB) - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.100 | Applied to: [DS-2CD2347G3P-LIS2UY/S(L)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779522628/Firmware__V5.8.100_260325_S3000712063.zip)(RB), [[DS-2CD2347G3P-LIS2UY/SRB(180°)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779522628/Firmware__V5.8.100_260325_S3000712063.zip)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779522628/Firmware__V5.8.100_260325_S3000712063.zip), DS-2CD2347G3P-LIS2UY/SRB(180°)O-STDBLACK, [[DS-2CD2347G3P-LIS2UY/SL(180°)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779522628/Firmware__V5.8.100_260325_S3000712063.zip)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779522628/Firmware__V5.8.100_260325_S3000712063.zip), DS-2CD2347G3P-LIS2UY/SL(180°)/O-STDBLACK, [DS-2CD2367G3P-LIS2UY/S(L)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779522628/Firmware__V5.8.100_260325_S3000712063.zip)(RB), [[DS-2CD2367G3P-LIS2UY/SRB(180°)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779522628/Firmware__V5.8.100_260325_S3000712063.zip)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779522628/Firmware__V5.8.100_260325_S3000712063.zip), DS-2CD2367G3P-LIS2UY/SRB(180°)O-STDBLACK | 2026-03-25 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779522628/Firmware__V5.8.100_260325_S3000712063.zip) | New 2/3 Series 4, 6MP Panoramic ColorVu Camera · a) Supports Acuseek / Supports DeepinView Perimeter Detection · b) Does not support face capture · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202604/releasenote%5CNetwork_Camera-V5.8.100_260325_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2363G2P-LISU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.11 | Applied to: [DS-2CD2363G2P-LISU/SL(180°)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780599961/Firmware__V5.8.110_260421_S3000718008.zip) | 2025-10-29 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780599961/Firmware__V5.8.110_260421_S3000718008.zip) | the screen flickering issue for 4G/WI-FI cameras · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.8.11_SP1_251029_Release_Note-IPCE_P_E11.pdf) |

</details>


<details>
<summary><h2>DS-2CD2366G2P-ISU/SL - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.20 | Applied to: [DS-2CD2366G2P-ISU/SL](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1772360105/Firmware__V5.7.20_251125_S3000690065.zip), [DS-2CD2366G2P-ISU/SL(2.8MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1772360105/Firmware__V5.7.20_251125_S3000690065.zip)(C), [DS-2CD2367G2P-LSU/SL](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1772360105/Firmware__V5.7.20_251125_S3000690065.zip), [DS-2CD2367G2P-LSU/SL(2.8MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1772360105/Firmware__V5.7.20_251125_S3000690065.zip)(C), [DS-2CD2T46G2P-ISU/SL](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1772360105/Firmware__V5.7.20_251125_S3000690065.zip), [DS-2CD2T46G2P-ISU/SL(2.8MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1772360105/Firmware__V5.7.20_251125_S3000690065.zip)(C), [DS-2CD2T66G2P-ISU/SL](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1772360105/Firmware__V5.7.20_251125_S3000690065.zip), [DS-2CD2T66G2P-ISU/SL(2.8MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1772360105/Firmware__V5.7.20_251125_S3000690065.zip)(C) | 2025-11-25 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1772360105/Firmware__V5.7.20_251125_S3000690065.zip) | Https and rtsp over https are supported by default · Web usability optimization: When the browser is zoomed to 150%, the page style will ensure the · effect, and the video will not displayed out of the box · Web resource update: Pos is disabled by default · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.20_251125_Release_Note-IPCE_P_G5.pdf) |

</details>


<details>
<summary><h2>DS-2CD2383G2P-LISU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.11 | Applied to: [DS-2CD2383G2P-LISU/SL(180°)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780599961/Firmware__V5.8.110_260421_S3000718008.zip) | 2025-10-29 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780599961/Firmware__V5.8.110_260421_S3000718008.zip) | the screen flickering issue for 4G/WI-FI cameras · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.8.11_SP1_251029_Release_Note-IPCE_P_E11.pdf) |

</details>


<details>
<summary><h2>DS-2CD2387G2P-LSU/SL - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.20 | Applied to: [DS-2CD2387G2P-LSU/SL](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779754560/Firmware__V5.7.20_260320_S3000708463.zip), [DS-2CD2387G2P-LSU/SL(4MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779754560/Firmware__V5.7.20_260320_S3000708463.zip)(C)/O-STD/BLACK, [DS-2CD2T87G2P-LSU/SL](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779754560/Firmware__V5.7.20_260320_S3000708463.zip), [DS-2CD2T87G2P-LSU/SL(4MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779754560/Firmware__V5.7.20_260320_S3000708463.zip)(C)/O-STD/BLACK, [DS-2CD3T87G2P-LSU/SL](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779754560/Firmware__V5.7.20_260320_S3000708463.zip), [DS-2CD3T87G2P-LSU/SL(4MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779754560/Firmware__V5.7.20_260320_S3000708463.zip)(C) | 2026-03-20 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779754560/Firmware__V5.7.20_260320_S3000708463.zip) | — |

</details>


<details>
<summary><h2>DS-2CD2421G0-I(D)(W) - IPC_E6 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.821 | Applied to: [DS-2CD2421G0-I(D)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1770623430/Firmware__V5.5.821_231108_S3000539541.zip)(W), [DS-2CD2421G0-I(2.8MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1770623430/Firmware__V5.5.821_231108_S3000539541.zip), [DS-2CD2421G0-I(2.0MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1770623430/Firmware__V5.5.821_231108_S3000539541.zip), [DS-2CD2421G0-I(4MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1770623430/Firmware__V5.5.821_231108_S3000539541.zip) | 2023-11-08 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1770623430/Firmware__V5.5.821_231108_S3000539541.zip) | Optimization · Fixed the bug of EZVIZ. · Internal · [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202404/1712790070190/releasenote%5CIPC_E6_5.5.821_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2423G0-I(W) - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.83 | Applied to: [DS-2CD2423G0-I(W)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1770752379/52faab7e-03ae-4dee-9dbd-a67988b4b16b.zip), [DS-2CD2423G0-IW(2.8MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1770752379/52faab7e-03ae-4dee-9dbd-a67988b4b16b.zip), [DS-2CD2443G0-I(W)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1770752379/52faab7e-03ae-4dee-9dbd-a67988b4b16b.zip), [DS-2CD2443G0-IW(2.8MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1770752379/52faab7e-03ae-4dee-9dbd-a67988b4b16b.zip) | 2019-02-21 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1770752379/52faab7e-03ae-4dee-9dbd-a67988b4b16b.zip) | Improve Features · [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202207/Network%20Camera%20V5.5.83%20Release%20Note%20--G1.pdf) |

</details>


<details>
<summary><h2>DS-2CD2423G0-I(W) - IPC_G1 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.6.821 | Applied to: [DS-2CD2423G0-I(W)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.6.821_260330_S3000711149.zip), [DS-2CD2423G0-I(2.8MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.6.821_260330_S3000711149.zip), [DS-2CD2423G0-IW(2.8MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.6.821_260330_S3000711149.zip), [DS-2CD2443G0-I(W)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.6.821_260330_S3000711149.zip), [DS-2CD2443G0-I(2.8MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.6.821_260330_S3000711149.zip), [DS-2CD2443G0-I(4MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.6.821_260330_S3000711149.zip), [DS-2CD2443G0-IW(2.8MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.6.821_260330_S3000711149.zip) | 2023-08-31 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.6.821_260330_S3000711149.zip) | Improve real-time performance during multiple LiveView. · [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202401/releasenote%5CNetwork_Camera-V5.6.821_Release_Note-IPC_G1_230831.pdf) |

</details>


<details>
<summary><h2>DS-2CD2523G0-I(W)(S) - IPC_G1 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.6.821 | Applied to: [DS-2CD2523G0-I(W)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.6.821_260330_S3000711149.zip)(S), [[DS-2CD2523G0-I(2.8MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.6.821_260330_S3000711149.zip)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.6.821_260330_S3000711149.zip), [DS-2CD2523G0-I(4MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.6.821_260330_S3000711149.zip), DS-2CD2523G0-I(2.8MM)(BLACK), [DS-2CD2523G0-IS(2.8MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.6.821_260330_S3000711149.zip)(BLACK), [DS-2CD2523G0-IS(4MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.6.821_260330_S3000711149.zip)(BLACK), [DS-2CD2523G0-IWS(2.8MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.6.821_260330_S3000711149.zip), [DS-2CD2523G0-IWS(4MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.6.821_260330_S3000711149.zip) | 2023-08-31 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.6.821_260330_S3000711149.zip) | Improve real-time performance during multiple LiveView. · [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202401/releasenote%5CNetwork_Camera-V5.6.821_Release_Note-IPC_G1_230831.pdf) |

</details>


<details>
<summary><h2>DS-2CD2523G2-I - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.0 | Applied to: [DS-2CD2523G2-I(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780096165/Firmware__V5.7.0_230221_S3000488889.zip)(D) | 2024-10-23 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780096165/Firmware__V5.7.0_230221_S3000488889.zip) | 1. Fix the issue of no Motion Detection alarms for the cameras with live guard. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202507/releasenote%5CNetwork_Camera-V5.7.0_SP6_Release_Note-G6_I.pdf) |

</details>


<details>
<summary><h2>DS-2CD2523G2-IS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.0 | Applied to: [DS-2CD2523G2-I(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780096165/Firmware__V5.7.0_230221_S3000488889.zip)(D) | 2024-10-23 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780096165/Firmware__V5.7.0_230221_S3000488889.zip) | 1. Fix the issue of no Motion Detection alarms for the cameras with live guard. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202507/releasenote%5CNetwork_Camera-V5.7.0_SP6_Release_Note-G6_I.pdf) |

</details>


<details>
<summary><h2>DS-2CD2526G2-IS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.0 | Applied to: [DS-2CD2526G2-I(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780096165/Firmware__V5.7.0_230221_S3000488889.zip)(D) | 2024-10-23 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780096165/Firmware__V5.7.0_230221_S3000488889.zip) | 1. Fix the issue of no Motion Detection alarms for the cameras with live guard. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202507/releasenote%5CNetwork_Camera-V5.7.0_SP6_Release_Note-G6_I.pdf) |

</details>


<details>
<summary><h2>DS-2CD2543G2-LI(W)Z(S)(2U)Y - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD2543G2-LI(W)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1777592712/Firmware__V5.8.30_251210_S3000691330.zip)Z(S)(2U)Y, [[DS-2CD2543G2-LIZS2UY(2.8/4MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1777592712/Firmware__V5.8.30_251210_S3000691330.zip)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1777592712/Firmware__V5.8.30_251210_S3000691330.zip)/O-STDBLACK, [DS-2CD2543G2-LIZ2UY(2.8/4MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1777592712/Firmware__V5.8.30_251210_S3000691330.zip), DS-2CD2543G2-LIZS2UY(2.8/4MM) | 2025-12-10 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1777592712/Firmware__V5.8.30_251210_S3000691330.zip) | 1. New products: · 2,3 series fixed point-to-point zoom PTR camera, 2143G2, 2146G3, 3143G2. · 2 series 4MP PTRZ camera, 2X46G3, 2X47G3. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13U.pdf) |

</details>


<details>
<summary><h2>DS-2CD2545FWD-I(W)(S) - IPC_G1 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.6.821 | Applied to: [DS-2CD2545FWD-I(W)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.6.821_260330_S3000711149.zip)(S), [DS-2CD2545FWD-IWS(2.8MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.6.821_260330_S3000711149.zip)(D), [[DS-2CD2545FWD-I(2.8MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.6.821_260330_S3000711149.zip)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.6.821_260330_S3000711149.zip)(BLACK), [[DS-2CD2545FWD-IS(2.8MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.6.821_260330_S3000711149.zip)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.6.821_260330_S3000711149.zip)(BLACK), DS-2CD2545FWD-IS(2.8MM), [DS-2CD2545FWD-IS(4MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.6.821_260330_S3000711149.zip), [DS-2CD2545FWD-IS(6MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.6.821_260330_S3000711149.zip), DS-2CD2545FWD-I(2.8MM) | 2023-08-31 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.6.821_260330_S3000711149.zip) | Improve real-time performance during multiple LiveView. · [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202401/releasenote%5CNetwork_Camera-V5.6.821_Release_Note-IPC_G1_230831.pdf) |

</details>


<details>
<summary><h2>DS-2CD2545FWD-I(W)(S) - IPC_V5 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.6.3 | Applied to: [DS-2CD2545FWD-I(W)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1770838965/fd283720-cf75-46b4-a8b9-aaa670def906.zip)(S), [DS-2CD2545FWD-IS(6MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1770838965/fd283720-cf75-46b4-a8b9-aaa670def906.zip), [DS-2CD2545FWD-I(6MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1770838965/fd283720-cf75-46b4-a8b9-aaa670def906.zip) | 2019-09-23 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1770838965/fd283720-cf75-46b4-a8b9-aaa670def906.zip) | Description of Iris Mode: Modify “Manual” to “fixed”. · Fixed the compatibility issue with third party platform Digifort. · Fixed the issue that camera cannot update dynamic IP address on Hik-Connect server. · Fixed the issue that IE login failed caused by exception of port 80. · [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202312/releasenote%5CIPC_V5.6.3_G1_Release_Note--External.pdf) |

</details>


<details>
<summary><h2>DS-2CD2623G2-IZS - IPC_G0 (3 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2623G2-IZS](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1770925789/Firmware__V5.7.13_230403_S3000490228.zip), [[[DS-2CD2623G2-IZS(2.8-12MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1770925789/Firmware__V5.7.13_230403_S3000490228.zip)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1770925789/Firmware__V5.7.13_230403_S3000490228.zip)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1770925789/Firmware__V5.7.13_230403_S3000490228.zip), DS-2CD2623G2-IZS(2.8-12MM) /D, DS-2CD2623G2-IZS(2.8-12MM)(D) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1770925789/Firmware__V5.7.13_230403_S3000490228.zip) | Associated camera model updates. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |
| 5.7.0 | Applied to: [DS-2CD2623G2-IZS(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780096165/Firmware__V5.7.0_230221_S3000488889.zip)(US Branch) | 2024-10-23 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780096165/Firmware__V5.7.0_230221_S3000488889.zip) | 1. New Products: 2 series Fixed-focus dual-light cameras: 2xx8G2. · 2. Motion Detection alarm of HC reflects human and vehicle attributes. · 1. 2/3 Series: Change the name of face capture in VCA Resource from Face Recognition to Face · [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202312/releasenote%5CNetwork_Camera-V5.7.13_Release_Note-G5.pdf) |
| 5.7.13 | Applied to: [DS-2CD2623G2-IZS](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1770925789/Firmware__V5.7.13_230403_S3000490228.zip), [[[DS-2CD2623G2-IZS(2.8-12MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1770925789/Firmware__V5.7.13_230403_S3000490228.zip)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1770925789/Firmware__V5.7.13_230403_S3000490228.zip)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1770925789/Firmware__V5.7.13_230403_S3000490228.zip), DS-2CD2623G2-IZS(2.8-12MM) /D, DS-2CD2623G2-IZS(2.8-12MM)(D) | 2023-04-03 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1770925789/Firmware__V5.7.13_230403_S3000490228.zip) | 1. New Products: 2 series Fixed-focus dual-light cameras: 2xx8G2. · 2. Motion Detection alarm of HC reflects human and vehicle attributes. · 1. 2/3 Series: Change the name of face capture in VCA Resource from Face Recognition to Face · [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202312/releasenote%5CNetwork_Camera-V5.7.13_Release_Note-G5.pdf) |

</details>


<details>
<summary><h2>DS-2CD2626G2-IZS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.0 | Applied to: [DS-2CD2626G2-IZS(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780096165/Firmware__V5.7.0_230221_S3000488889.zip) | 2024-10-23 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780096165/Firmware__V5.7.0_230221_S3000488889.zip) | Version maintenance of HC library permission authentication issues. · [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202408/releasenote%5CNetwork_Camera-V5.5.820_Release_Note-G3.pdf) |

</details>


<details>
<summary><h2>DS-2CD2626G2-IZSU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.0 | Applied to: [DS-2CD2626G2-IZSU/SL(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780096165/Firmware__V5.7.0_230221_S3000488889.zip) | 2024-10-23 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780096165/Firmware__V5.7.0_230221_S3000488889.zip) | Version maintenance of HC library permission authentication issues. · [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202408/releasenote%5CNetwork_Camera-V5.5.820_Release_Note-G3.pdf) |

</details>


<details>
<summary><h2>DS-2CD2626G2T-IZS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.0 | Applied to: [DS-2CD2626G2T-IZS(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780096165/Firmware__V5.7.0_230221_S3000488889.zip)(D) | 2024-10-23 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780096165/Firmware__V5.7.0_230221_S3000488889.zip) | 1. Fix the issue of no Motion Detection alarms for the cameras with live guard. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202507/releasenote%5CNetwork_Camera-V5.7.0_SP6_Release_Note-G6_I.pdf) |

</details>


<details>
<summary><h2>DS-2CD2647G3-LIZS2UY/S(L)(RB) - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.32 | Applied to: [DS-2CD2647G3-LIZS2UY/S(L)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780390224/Firmware__V5.8.32_260320_S3000708449.zip)(RB), [DS-2CD2647G3-LIZS2UY/SRB(2.8-12MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780390224/Firmware__V5.8.32_260320_S3000708449.zip)/O-STD, [DS-2CD2647G3-LIZS2UY/SRB(2.8-12)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780390224/Firmware__V5.8.32_260320_S3000708449.zip)O-STDBLK, [[DS-2CD2647G3-LIZS2UY/SL(2.8-12MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780390224/Firmware__V5.8.32_260320_S3000708449.zip)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780390224/Firmware__V5.8.32_260320_S3000708449.zip)OSTDBLK, DS-2CD2647G3-LIZS2UY/SL(2.8-12MM), [DS-2CD2647G3-LIZSY](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780390224/Firmware__V5.8.32_260320_S3000708449.zip), [[DS-2CD2647G3-LIZSY(2.8-12MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780390224/Firmware__V5.8.32_260320_S3000708449.zip)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780390224/Firmware__V5.8.32_260320_S3000708449.zip), DS-2CD2647G3-LIZSY(2.8-12MM)/O-STD/BLACK | 2026-04-23 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780390224/Firmware__V5.8.32_260320_S3000708449.zip) | — |

</details>


<details>
<summary><h2>DS-2CD2723G2-IZS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.0 | Applied to: [DS-2CD2723G2-IZS(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780096165/Firmware__V5.7.0_230221_S3000488889.zip)(D) | 2024-10-23 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780096165/Firmware__V5.7.0_230221_S3000488889.zip) | 1. Fix the issue of no Motion Detection alarms for the cameras with live guard. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202507/releasenote%5CNetwork_Camera-V5.7.0_SP6_Release_Note-G6_I.pdf) |

</details>


<details>
<summary><h2>DS-2CD2726G2-IZS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.0 | Applied to: [DS-2CD2726G2-IZS(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780096165/Firmware__V5.7.0_230221_S3000488889.zip) | 2024-10-23 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780096165/Firmware__V5.7.0_230221_S3000488889.zip) | Version maintenance of HC library permission authentication issues. · [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202408/releasenote%5CNetwork_Camera-V5.5.820_Release_Note-G3.pdf) |

</details>


<details>
<summary><h2>DS-2CD2726G2T-IZS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.0 | Applied to: [DS-2CD2726G2T-IZS(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780096165/Firmware__V5.7.0_230221_S3000488889.zip)(D) | 2024-10-23 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780096165/Firmware__V5.7.0_230221_S3000488889.zip) | 1. Fix the issue of no Motion Detection alarms for the cameras with live guard. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202507/releasenote%5CNetwork_Camera-V5.7.0_SP6_Release_Note-G6_I.pdf) |

</details>


<details>
<summary><h2>DS-2CD2935FWD-I - IPC_V5 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.4.52 | Applied to: [DS-2CD2935FWD-I](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1771143373/7d4a69ad-ffac-4b30-a09d-66f19a538df0.zip), [DS-2CD2935FWD-I(1.16MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1771143373/7d4a69ad-ffac-4b30-a09d-66f19a538df0.zip), [DS-2CD2935FWD-IS(1.16MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1771143373/7d4a69ad-ffac-4b30-a09d-66f19a538df0.zip), [DS-2CD2955FWD-I](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1771143373/7d4a69ad-ffac-4b30-a09d-66f19a538df0.zip), [DS-2CD2955FWD-IS(1.05MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1771143373/7d4a69ad-ffac-4b30-a09d-66f19a538df0.zip), [DS-2CD2955FWD-I(1.05MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1771143373/7d4a69ad-ffac-4b30-a09d-66f19a538df0.zip) | 2020-04-16 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1771143373/7d4a69ad-ffac-4b30-a09d-66f19a538df0.zip) | Hik-Connect multi-screen display function: Device newly supports software decoding on · Hik-Connect. · Fixed the known issue. · Compatibility Update · [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202312/releasenote%5CIPC_V5.4.52_G1__Release_Note--External.pdf) |

</details>


<details>
<summary><h2>DS-2CD2D25G1-D/NF - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.210 | Applied to: [DS-2CD2D25G1-D/NF](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780683636/Firmware__V5.7.210_260402_S3000713546.zip), [DS-2CD2D25G1-D/NF(2.8MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780683636/Firmware__V5.7.210_260402_S3000713546.zip), [DS-2CD2D25G1-D/NF(3.7MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780683636/Firmware__V5.7.210_260402_S3000713546.zip), [DS-2CD2D45G1/M-D/NF](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780683636/Firmware__V5.7.210_260402_S3000713546.zip), [DS-2CD2D45G1/M-D/NF(2.8MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780683636/Firmware__V5.7.210_260402_S3000713546.zip), [DS-2CD2D45G1/M-D/NF(4MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780683636/Firmware__V5.7.210_260402_S3000713546.zip), [DS-2CD6425G1-XX](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780683636/Firmware__V5.7.210_260402_S3000713546.zip), [DS-2CD6425G1-10(3.7MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780683636/Firmware__V5.7.210_260402_S3000713546.zip)2M | 2026-04-02 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780683636/Firmware__V5.7.210_260402_S3000713546.zip) | — |

</details>


<details>
<summary><h2>DS-2CD2H55FWD-IZS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.51 | Applied to: [DS-2CD2H55FWD-IZS](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1771230878/3e919f73-e198-45cf-aa44-a0652b9caf97.zip), [DS-2CD2H55FWD-IZS(2.8-12MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1771230878/3e919f73-e198-45cf-aa44-a0652b9caf97.zip) | 2018-03-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1771230878/3e919f73-e198-45cf-aa44-a0652b9caf97.zip) | — |

</details>


<details>
<summary><h2>DS-2CD2T23G2-2I - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.0 | Applied to: [DS-2CD2T23G2-2I(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780096165/Firmware__V5.7.0_230221_S3000488889.zip)(D) | 2024-10-23 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780096165/Firmware__V5.7.0_230221_S3000488889.zip) | 1. Fix the issue of no Motion Detection alarms for the cameras with live guard. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202507/releasenote%5CNetwork_Camera-V5.7.0_SP6_Release_Note-G6_I.pdf) |

</details>


<details>
<summary><h2>DS-2CD2T26G2-2I - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.0 | Applied to: [DS-2CD2T26G2-4I(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780096165/Firmware__V5.7.0_230221_S3000488889.zip) | 2024-10-23 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780096165/Firmware__V5.7.0_230221_S3000488889.zip) | Version maintenance of HC library permission authentication issues. · [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202408/releasenote%5CNetwork_Camera-V5.5.820_Release_Note-G3.pdf) |

</details>


<details>
<summary><h2>DS-2CD2T26G2-ISU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.0 | Applied to: [DS-2CD2T26G2-ISU/SL(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780096165/Firmware__V5.7.0_230221_S3000488889.zip) | 2024-10-23 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780096165/Firmware__V5.7.0_230221_S3000488889.zip) | 1. Improved Features  Fix security issue in ISAPI. · [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/330c4c2c-5730-4877-a942-0be87cea67ca.pdf) |

</details>


<details>
<summary><h2>DS-2CD2T43G2P-LISU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.11 | Applied to: [DS-2CD2T43G2P-LISU/SL(180°)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780599961/Firmware__V5.8.110_260421_S3000718008.zip) | 2025-10-29 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780599961/Firmware__V5.8.110_260421_S3000718008.zip) | the screen flickering issue for 4G/WI-FI cameras · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.8.11_SP1_251029_Release_Note-IPCE_P_E11.pdf) |

</details>


<details>
<summary><h2>DS-2CD2T63G2P-LISU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.11 | Applied to: [DS-2CD2T63G2P-LISU/SL(180°)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780599961/Firmware__V5.8.110_260421_S3000718008.zip) | 2025-10-29 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780599961/Firmware__V5.8.110_260421_S3000718008.zip) | the screen flickering issue for 4G/WI-FI cameras · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.8.11_SP1_251029_Release_Note-IPCE_P_E11.pdf) |

</details>


<details>
<summary><h2>DS-2CD2T83G2P-LISU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.11 | Applied to: [DS-2CD2T83G2P-LISU/SL(180°)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780599961/Firmware__V5.8.110_260421_S3000718008.zip) | 2025-10-29 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780599961/Firmware__V5.8.110_260421_S3000718008.zip) | the screen flickering issue for 4G/WI-FI cameras · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.8.11_SP1_251029_Release_Note-IPCE_P_E11.pdf) |

</details>


<details>
<summary><h2>DS-2CD3027G2-LS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.820 | Applied to: [DS-2CD3027G2-LS](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780649800/Firmware__V5.5.820_260402_S3000712894.zip), [DS-2CD3027G2-LS(2.8MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780649800/Firmware__V5.5.820_260402_S3000712894.zip), [DS-2CD3027G2-LS(4MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780649800/Firmware__V5.5.820_260402_S3000712894.zip), [DS-2CD3047G2-LS](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780649800/Firmware__V5.5.820_260402_S3000712894.zip), [DS-2CD3047G2-LS(2.8MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780649800/Firmware__V5.5.820_260402_S3000712894.zip), [DS-2CD3047G2-LS(4MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780649800/Firmware__V5.5.820_260402_S3000712894.zip), [DS-2CD3327G2-LS(U)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780649800/Firmware__V5.5.820_260402_S3000712894.zip), [DS-2CD3327G2-LSU(2.8MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780649800/Firmware__V5.5.820_260402_S3000712894.zip) | 2023-11-08 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780649800/Firmware__V5.5.820_260402_S3000712894.zip) | Version maintenance of HC library permission authentication issues. · [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202403/releasenote%5CNetwork_Camera-V5.5.820_Release_Note-G3.pdf) |

</details>


<details>
<summary><h2>DS-2CD3046G2-IU/SL - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.10 | Applied to: [DS-2CD3046G2-IU/SL](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780617965/Firmware__V5.8.10_260403_S3000714421.zip), [DS-2CD3046G2-IU/SL(4MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780617965/Firmware__V5.8.10_260403_S3000714421.zip)(D), [DS-2CD3186G2-IS(U)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780617965/Firmware__V5.8.10_260403_S3000714421.zip), [DS-2CD3186G2-IS(2.8MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780617965/Firmware__V5.8.10_260403_S3000714421.zip)(D), [DS-2CD3646G2-IZS](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780617965/Firmware__V5.8.10_260403_S3000714421.zip), [DS-2CD3646G2-IZS(2.7-13.5MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780617965/Firmware__V5.8.10_260403_S3000714421.zip)(D), [DS-2CD3646G2-IZS(7-35MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780617965/Firmware__V5.8.10_260403_S3000714421.zip)(D), [DS-2CD3646G2HT-LIZS(Y)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780617965/Firmware__V5.8.10_260403_S3000714421.zip) | 2026-04-03 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780617965/Firmware__V5.8.10_260403_S3000714421.zip) | — |

</details>


<details>
<summary><h2>DS-2CD3046G3-IU(Y) - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD3046G3-IU(Y)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779388610/Firmware__V5.8.30_260326_S3000711818.zip), [DS-2CD3046G3-IUY(2.8MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779388610/Firmware__V5.8.30_260326_S3000711818.zip), [DS-2CD3046G3-IUY(4MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779388610/Firmware__V5.8.30_260326_S3000711818.zip), [DS-2CD3046G3-IU/SL(Y)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779388610/Firmware__V5.8.30_260326_S3000711818.zip), [[DS-2CD3046G3-IUY/SL(2.8MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779388610/Firmware__V5.8.30_260326_S3000711818.zip)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779388610/Firmware__V5.8.30_260326_S3000711818.zip), [DS-2CD3046G3-IUY/SL(4MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779388610/Firmware__V5.8.30_260326_S3000711818.zip), DS-2CD3046G3-IUY/SL(2.8MM)(BLACK), [DS-2CD3046G3-LIU(Y)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779388610/Firmware__V5.8.30_260326_S3000711818.zip) | 2026-03-26 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779388610/Firmware__V5.8.30_260326_S3000711818.zip) | some bugs to enhance system stability. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202605/releasenote%5CNetwork_Camera-V5.8.30_260326_Release_IPCE_H_H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD3066G2-IS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.51 | Applied to: [DS-2CD3066G2-IS](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1771533808/Firmware__V5.7.51_230829_S3000522021.zip), [DS-2CD3066G2-IS(2.8MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1771533808/Firmware__V5.7.51_230829_S3000522021.zip)(BRA STD)SKD | 2023-08-29 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1771533808/Firmware__V5.7.51_230829_S3000522021.zip) | — |

</details>


<details>
<summary><h2>DS-2CD3186G3-LISU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.11 | Applied to: [DS-2CD3186G3-LISUY(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780599961/Firmware__V5.8.110_260421_S3000718008.zip)(eF) | 2025-10-22 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780599961/Firmware__V5.8.110_260421_S3000718008.zip) | 1. New products: 3 series PTRZ camera, 3X6(8)6G3(PTRZ), 3X6(8)7G3(PTRZ). · (1) Support independent or combined movement in P/T/R directions, supports speed adjustment in gears 1 -7, · and maintains consistent position before and after restart and upgrade. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD33167G3P-LIHSUY/SL - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.110 | Applied to: [DS-2CD33167G3P-LIHSUY/SL](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780599961/Firmware__V5.8.110_260421_S3000718008.zip), [DS-2CD33167G3P-LIHSUY/SL(2.8MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780599961/Firmware__V5.8.110_260421_S3000718008.zip), [DS-2CD3387G3P-LIHSUY/SL](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780599961/Firmware__V5.8.110_260421_S3000718008.zip), [[DS-2CD3387G3P-LIHSUY/SL(2.8MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780599961/Firmware__V5.8.110_260421_S3000718008.zip)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780599961/Firmware__V5.8.110_260421_S3000718008.zip), DS-2CD3387G3P-LIHSUY/SL(2.8MM)OSTD/BLACK, [DS-2CD33C7G3P-LIHSUY/SL](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780599961/Firmware__V5.8.110_260421_S3000718008.zip), [[DS-2CD33C7G3P-LIHSUY/SL(2.8MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780599961/Firmware__V5.8.110_260421_S3000718008.zip)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780599961/Firmware__V5.8.110_260421_S3000718008.zip), DS-2CD33C7G3P-LIHSUY/SL(2.8MM)OSTD/BLACK | 2026-04-21 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780599961/Firmware__V5.8.110_260421_S3000718008.zip) | — |

</details>


<details>
<summary><h2>DS-2CD3343G2 - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.11 | Applied to: [DS-2CD3343G2/X2-LIZSUY/SL(2.8/4mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780599961/Firmware__V5.8.110_260421_S3000718008.zip)O-STD | 2025-12-16 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780599961/Firmware__V5.8.110_260421_S3000718008.zip) | Fix the network abnormal issue. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.8.11_251216_Release_Note-IPCE_D_H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD3343G2-X2-LIZSUY-SL - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.11 | Applied to: [DS-2CD3343G2-X2-LIZSUY-SL](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780599961/Firmware__V5.8.110_260421_S3000718008.zip) | 2026-03-26 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780599961/Firmware__V5.8.110_260421_S3000718008.zip) | some bugs to enhance system stability. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202605/releasenote%5CNetwork_Camera-V5.8.11_260326_Release_IPCE_D_H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD3586G2-IS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.19 | Applied to: [DS-2CD3586G2-IS](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1771793105/Firmware__V5.7.19_241207_S3000618493.zip), [DS-2CD3586G2-IS(2.8MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1771793105/Firmware__V5.7.19_241207_S3000618493.zip)(C) | 2024-12-07 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1771793105/Firmware__V5.7.19_241207_S3000618493.zip) | 1. Change of capture mode for 6/8 MP camera：P system delet e 3200x180025, only reserved · 3840x216025, The N system remains unchanged. · 2. Newly Add 38 boxes camera: DS-2CD3843G2-AP2. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.19_241207_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD3621G2-LIZS(U) - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.12 | Applied to: [DS-2CD3621G2-LIZS(U)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780732335/Firmware__V5.7.120_260401_S3000712806.zip), [DS-2CD3621G2-LIZS(2.7-13.5MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780732335/Firmware__V5.7.120_260401_S3000712806.zip)(PRAMA)/PR, [DS-2CD3721G2-LIZS(U)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780732335/Firmware__V5.7.120_260401_S3000712806.zip), [DS-2CD3721G2-LIZS(2.7-13.5MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780732335/Firmware__V5.7.120_260401_S3000712806.zip)(PRAMA)/PR | 2023-06-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780732335/Firmware__V5.7.120_260401_S3000712806.zip) | Fix the problem that image parameters are lost after upgrading in version earlier than 5.7.10. · Fix the screen issue when HC event capture. · Custom audio function is removed from some models. · [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202411/releasenote%5CNetwork_Camera-V5.7.12_SP1_Release_Note-E10.pdf) |

</details>


<details>
<summary><h2>DS-2CD3646G2T-LIDZSU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.1 | Applied to: [DS-2CD3646G2T-LIDZSU/4G/SL(2.7-13.5)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.8.1_260330_S3000711487.zip)OSTD | 2025-08-07 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.8.1_260330_S3000711487.zip) | 1. Supports EN18031 certification · 2. Supports acuseek · 3. Supports 4G · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202508/releasenote%5CNetwork_Camera-V5.8.1_250807_Release_Note-IPCE_HGL_G5.pdf) |

</details>


<details>
<summary><h2>DS-2CD3686G2T-LIDZSU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.1 | Applied to: [DS-2CD3686G2T-LIDZSU/4G/SL(2.7-13.5)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.8.1_260330_S3000711487.zip)OSTD | 2025-08-07 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.8.1_260330_S3000711487.zip) | 1. Supports EN18031 certification · 2. Supports acuseek · 3. Supports 4G · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202508/releasenote%5CNetwork_Camera-V5.8.1_250807_Release_Note-IPCE_HGL_G5.pdf) |

</details>


<details>
<summary><h2>DS-2CD3956G2-IS(U) - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.40 | Applied to: [DS-2CD3956G2-IS(U)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780617965/Firmware__V5.7.40_260403_S3000712702.zip), [DS-2CD3956G2-IS(1.05MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780617965/Firmware__V5.7.40_260403_S3000712702.zip) | 2026-04-03 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780617965/Firmware__V5.7.40_260403_S3000712702.zip) | — |

</details>


<details>
<summary><h2>DS-2CD3A26G2T-IZS - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.0 | Applied to: [DS-2CD3A26G2T-IZS](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780649800/Firmware__V5.8.0_260402_S3000712887.zip), [DS-2CD3A26G2T-IZS(4.7-71MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780649800/Firmware__V5.8.0_260402_S3000712887.zip) | 2026-05-15 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780649800/Firmware__V5.8.0_260402_S3000712887.zip) | SP version · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202605/releasenote%5CNetwork_Camera-V5.8.0_260515_Release_IPCE_LZ_H8.pdf) |
| 5.7.0 | Applied to: [DS-2CD3A26G2T-IZS(4.7-71mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780096165/Firmware__V5.7.0_230221_S3000488889.zip) | 2023-06-27 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780096165/Firmware__V5.7.0_230221_S3000488889.zip) | 1. Fix EZVIZ library permission authentication issue · The camera uses a ZD25 electric lens. In scenes with a large depth of field, due to the problem of infrared non · confocal, the camera may refocus on the foreground/background, resulting in a change in the desired focus · [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202408/releasenote%5CNetwork_Camera-V5.7.0_SP2_Release_Note-IPCE_LZ_H8_230627.pdf) |

</details>


<details>
<summary><h2>DS-2CD3A46G2T-IZHS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.0 | Applied to: [DS-2CD3A46G2T-IZHS](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.0_260327_S3000712832.zip), [DS-2CD3A46G2T-IZHS(6-60MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.0_260327_S3000712832.zip) | 2026-03-27 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.0_260327_S3000712832.zip) | — |

</details>


<details>
<summary><h2>DS-2CD3T23G1-I/4G - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.52 | Applied to: [DS-2CD3T23G1-I/4G](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780617965/Firmware__V5.7.52_260404_S3000713499.zip), [DS-2CD3T23G1-I/4G(2.8MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780617965/Firmware__V5.7.52_260404_S3000713499.zip), [DS-2CD3T23G1-I/4G(4MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780617965/Firmware__V5.7.52_260404_S3000713499.zip), [DS-2CD3T23G1-I/4G(8MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780617965/Firmware__V5.7.52_260404_S3000713499.zip) | 2026-04-04 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780617965/Firmware__V5.7.52_260404_S3000713499.zip) | — |
| 5.7.51 | Applied to: [DS-2CD3T23G1-I/4G](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1772228122/Firmware__V5.7.51_240320_S3000563201.zip), [DS-2CD3T23G1-I/4G(8MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1772228122/Firmware__V5.7.51_240320_S3000563201.zip) | 2024-03-20 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1772228122/Firmware__V5.7.51_240320_S3000563201.zip) | — |

</details>


<details>
<summary><h2>DS-2CD3T46G2-LIDSU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.1 | Applied to: [DS-2CD3T46G2-LIDSU/4G/SL(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.8.1_260330_S3000711487.zip) | 2025-08-07 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.8.1_260330_S3000711487.zip) | 1. Supports EN18031 certification · 2. Supports acuseek · 3. Supports 4G · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202508/releasenote%5CNetwork_Camera-V5.8.1_250807_Release_Note-IPCE_HGL_G5.pdf) |

</details>


<details>
<summary><h2>DS-2CD3T86G2-LIDSU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.1 | Applied to: [DS-2CD3T86G2-LIDSU/4G/SL(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.8.1_260330_S3000711487.zip) | 2025-08-07 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.8.1_260330_S3000711487.zip) | 1. Supports EN18031 certification · 2. Supports acuseek · 3. Supports 4G · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202508/releasenote%5CNetwork_Camera-V5.8.1_250807_Release_Note-IPCE_HGL_G5.pdf) |

</details>


<details>
<summary><h2>DS-2CD3T87G3-LISU(Y) - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD3T87G3-LISU(Y)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779754560/Firmware__V5.8.10_260430_S3000722532.zip), [DS-2CD3T87G3-LISUY(2.8MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779754560/Firmware__V5.8.10_260430_S3000722532.zip), [DS-2CD3T87G3-LISUY(4MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779754560/Firmware__V5.8.10_260430_S3000722532.zip), [DS-2CD3T87G3-LISU(2.8MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779754560/Firmware__V5.8.10_260430_S3000722532.zip), [[DS-2CD3T87G3-LISU(4MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779754560/Firmware__V5.8.10_260430_S3000722532.zip)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779754560/Firmware__V5.8.10_260430_S3000722532.zip), DS-2CD3T87G3-LISU(4MM)(VIE HUANUO), [DS-2CD3T87G3-LISU(6MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779754560/Firmware__V5.8.10_260430_S3000722532.zip)(VIE HUANUO) | 2026-03-26 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779754560/Firmware__V5.8.10_260430_S3000722532.zip) | some bugs to enhance system stability. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202605/releasenote%5CNetwork_Camera-V5.8.30_260326_Release_IPCE_H_H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD4A24FWD-IZ(H)(S)(T) - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.84 | Applied to: [DS-2CD4A24FWD-IZ(H)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1778418467/d555f2de-098a-40f4-b417-e8db8a68a42a.zip)(S)(T), [DS-2CD4A24FWD-IZ(4.7-94MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1778418467/d555f2de-098a-40f4-b417-e8db8a68a42a.zip)(T), [DS-2CD4A24FWD-IZS(4.7-94MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1778418467/d555f2de-098a-40f4-b417-e8db8a68a42a.zip)(T), [DS-2CD4A24FWD-IZHS(4.7-94MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1778418467/d555f2de-098a-40f4-b417-e8db8a68a42a.zip)(T), [DS-2CD4A24FWD-IZH(4.7-94MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1778418467/d555f2de-098a-40f4-b417-e8db8a68a42a.zip)(T), [DS-2CD4B45G0-IZS](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1778418467/d555f2de-098a-40f4-b417-e8db8a68a42a.zip), [[DS-2CD4B45G0-IZS(4.7-65.8MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1778418467/d555f2de-098a-40f4-b417-e8db8a68a42a.zip)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1778418467/d555f2de-098a-40f4-b417-e8db8a68a42a.zip), DS-2CD4B45G0-IZS(4.7-65.8MM)(B) | 2019-05-07 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1778418467/d555f2de-098a-40f4-b417-e8db8a68a42a.zip) | — |

</details>


<details>
<summary><h2>DS-2CD4A45G0-IZ(H)S - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.85 | Applied to: [DS-2CD4A45G0-IZ(H)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1772360105/d3b888f5-d9e5-4f4a-8eac-251e4f17471c.zip)S, [DS-2CD4A45G0-IZHS(4.7-94MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1772360105/d3b888f5-d9e5-4f4a-8eac-251e4f17471c.zip)(B), [DS-2CD4A45G0-IZS(4.7-94MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1772360105/d3b888f5-d9e5-4f4a-8eac-251e4f17471c.zip)(B), [DS-2CD4B45G0-IZS](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1772360105/d3b888f5-d9e5-4f4a-8eac-251e4f17471c.zip), [[DS-2CD4B45G0-IZS(4.7-65.8MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1772360105/d3b888f5-d9e5-4f4a-8eac-251e4f17471c.zip)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1772360105/d3b888f5-d9e5-4f4a-8eac-251e4f17471c.zip), DS-2CD4B45G0-IZS(4.7-65.8MM)(B) | 2019-11-07 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1772360105/d3b888f5-d9e5-4f4a-8eac-251e4f17471c.zip) | — |

</details>


<details>
<summary><h2>DS-2CD4B26FWD-IZ(S) - IPC_V5 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.91 | Applied to: [DS-2CD4B26FWD-IZ(S)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1772360105/560e73e2-270f-4f2d-b248-d18f6e89e09e.zip), [DS-2CD4B26FWD-IZS(2.8-12MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1772360105/560e73e2-270f-4f2d-b248-d18f6e89e09e.zip), [DS-2CD4B36FWD-IZ(S)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1772360105/560e73e2-270f-4f2d-b248-d18f6e89e09e.zip), [DS-2CD4B36FWD-IZS(2.8-12MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1772360105/560e73e2-270f-4f2d-b248-d18f6e89e09e.zip), [DS-2CD4D36FWD-IZ(S)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1772360105/560e73e2-270f-4f2d-b248-d18f6e89e09e.zip), [DS-2CD4D36FWD-IZS(2.8-12MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1772360105/560e73e2-270f-4f2d-b248-d18f6e89e09e.zip), [DS-2CD4D36FWD-IZ/V(2.8-12MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1772360105/560e73e2-270f-4f2d-b248-d18f6e89e09e.zip) | 2021-04-29 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1772360105/560e73e2-270f-4f2d-b248-d18f6e89e09e.zip) | improve product performance, and will take effect automatically after upgrading from previous versions. · [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202312/releasenote%5C%E3%80%90Release_Note%E3%80%91Mobile_IPC_V5.5.91_210429.pdf) |

</details>


<details>
<summary><h2>DS-2CD6045G0/SC-IZRS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.6 | Applied to: [DS-2CD6045G0/SC-IZRS](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.8.6_260331_S3000713808.zip), [DS-2CD6045G0/SC-IZRS(2.8-12MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.8.6_260331_S3000713808.zip), [DS-2CD6045G0/SC-IZRS(8-32MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.8.6_260331_S3000713808.zip), [DS-2CD6085G0/SC-IZRS](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.8.6_260331_S3000713808.zip), [DS-2CD6085G0/SC-IZRS(2.8-12MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.8.6_260331_S3000713808.zip), [DS-2CD6085G0/SC-IZRS(8-32MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.8.6_260331_S3000713808.zip) | 2026-03-25 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.8.6_260331_S3000713808.zip) | — |

</details>


<details>
<summary><h2>DS-2CD6365G1-IVS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.3 | Applied to: [DS-2CD6365G1-IVS](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780649800/Firmware__V5.8.3_260402_S3000712976.zip), [DS-2CD6365G1-IVS(1.16MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780649800/Firmware__V5.8.3_260402_S3000712976.zip), [DS-2CD6365G1-S/RC](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780649800/Firmware__V5.8.3_260402_S3000712976.zip), [DS-2CD6365G1-S/RC(1.16MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780649800/Firmware__V5.8.3_260402_S3000712976.zip), [DS-2CD63C5G1-IVS](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780649800/Firmware__V5.8.3_260402_S3000712976.zip), [DS-2CD63C5G1-IVS(1.29MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780649800/Firmware__V5.8.3_260402_S3000712976.zip), [DS-2CD63C5G1-S/RC](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780649800/Firmware__V5.8.3_260402_S3000712976.zip), [DS-2CD63C5G1-S/RC(1.29MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780649800/Firmware__V5.8.3_260402_S3000712976.zip) | 2026-04-02 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780649800/Firmware__V5.8.3_260402_S3000712976.zip) | — |

</details>


<details>
<summary><h2>DS-2CD6425G2-C1 - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.20 | Applied to: [DS-2CD6425G2-C1](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.8.20_260330_S3000711486.zip), [DS-2CD6425G2-C2](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.8.20_260330_S3000711486.zip), [DS-2CD6445G2-C1/HDMI](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.8.20_260330_S3000711486.zip) | 2026-04-02 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.8.20_260330_S3000711486.zip) | — |

</details>


<details>
<summary><h2>DS-2CD6825G0/C-I(S) - IPC_V5 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.850 | Applied to: [DS-2CD6825G0/C-I(S)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1772401117/IPCDC_H7_EN_STD_5.5.850_220421.zip), [DS-2CD6825G0/C-I(2MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1772401117/IPCDC_H7_EN_STD_5.5.850_220421.zip), [DS-2CD6825G0/C-IS(2MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1772401117/IPCDC_H7_EN_STD_5.5.850_220421.zip), [DS-2CD6825G0/C-I(V)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1772401117/IPCDC_H7_EN_STD_5.5.850_220421.zip)(S), [DS-2CD6825G0/C-IV(2MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1772401117/IPCDC_H7_EN_STD_5.5.850_220421.zip), [DS-2CD6825G0/C-IVS(2MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1772401117/IPCDC_H7_EN_STD_5.5.850_220421.zip) | 2022-04-21 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1772401117/IPCDC_H7_EN_STD_5.5.850_220421.zip) | improve product performance, and will take effect automatically after upgrading from previous versions. · [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202207/IPC_V5.5.850_build_220421_Release%20Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD6924G0-IHS - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.1 | Applied to: [DS-2CD6924G0-IHS(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780732335/Firmware__V5.7.120_260401_S3000712806.zip)(C) | 2024-06-13 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780732335/Firmware__V5.7.120_260401_S3000712806.zip) | — |
| 5.7.0 | Applied to: [DS-2CD6924G0-IHS/NFC(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780096165/Firmware__V5.7.0_230221_S3000488889.zip) | 2024-01-29 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780096165/Firmware__V5.7.0_230221_S3000488889.zip) | New function · Fix the issue of no stream when using the ONVIF protocol to connect to third -party platforms after · restarting in panoramic multi-channel mode. · [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202312/releasenote%5CIPCP_H5_5.5.820_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD6924G0-IHS(/NFC) - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.820 | Applied to: [DS-2CD6924G0-IHS(/NFC)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780649800/Firmware__V5.5.820_260402_S3000713027.zip), [DS-2CD6924G0-IHS/NFC(2.8MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780649800/Firmware__V5.5.820_260402_S3000713027.zip), [DS-2CD6924G0-IHS/NFC(6MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780649800/Firmware__V5.5.820_260402_S3000713027.zip), [[DS-2CD6924G0-IHS(2.8MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780649800/Firmware__V5.5.820_260402_S3000713027.zip)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780649800/Firmware__V5.5.820_260402_S3000713027.zip), [DS-2CD6924G0-IHS(6MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780649800/Firmware__V5.5.820_260402_S3000713027.zip), DS-2CD6924G0-IHS(2.8MM)(D), [DS-2CD6944G0-IHS(/NFC)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780649800/Firmware__V5.5.820_260402_S3000713027.zip), [DS-2CD6944G0-IHS/NFC(2.8MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780649800/Firmware__V5.5.820_260402_S3000713027.zip) | 2026-04-02 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780649800/Firmware__V5.5.820_260402_S3000713027.zip) | New function · Fixed some known issues · [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202402/releasenote%5CH10_PanoVu-V5.7.0_SP2_Release_Note.pdf) |
| 5.7.0 | Applied to: [DS-2CD6924G0-IHS(/NFC)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780096165/Firmware__V5.7.0_230221_S3000488889.zip), [DS-2CD6924G0-IHS(2.8MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780096165/Firmware__V5.7.0_230221_S3000488889.zip)(D), [DS-2CD6944G0-IHS(/NFC)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780096165/Firmware__V5.7.0_230221_S3000488889.zip), [DS-2CD6944G0-IHS/NFC(2.8MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780096165/Firmware__V5.7.0_230221_S3000488889.zip), [DS-2CD6944G0-IHS/NFC(6MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780096165/Firmware__V5.7.0_230221_S3000488889.zip), [DS-2CD6944G0-IHS(2.8MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780096165/Firmware__V5.7.0_230221_S3000488889.zip)(D), [DS-2CD6984G0-IH(S)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780096165/Firmware__V5.7.0_230221_S3000488889.zip)(AC)(/NFC), [DS-2CD6984G0-IHS/NFC(2.8MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780096165/Firmware__V5.7.0_230221_S3000488889.zip) | 2024-01-29 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780096165/Firmware__V5.7.0_230221_S3000488889.zip) | New function · Fixed some known issues · [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202402/releasenote%5CH10_PanoVu-V5.7.0_SP2_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD6924G0-IHS(C) - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.3 | Applied to: [DS-2CD6924G0-IHS(C)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780683636/Firmware__V5.7.3_260401_S3000712942.zip), [DS-2CD6924G0-IHS(2.8MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780683636/Firmware__V5.7.3_260401_S3000712942.zip)(C), [DS-2CD6924G0-IHSY(2.8MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780683636/Firmware__V5.7.3_260401_S3000712942.zip)(C), [DS-2CD6944G0-IHS(C)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780683636/Firmware__V5.7.3_260401_S3000712942.zip), [DS-2CD6944G0-IHS(2.8MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780683636/Firmware__V5.7.3_260401_S3000712942.zip)(C) | 2026-04-01 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780683636/Firmware__V5.7.3_260401_S3000712942.zip) | — |

</details>


<details>
<summary><h2>DS-2CD6944G0-IHS - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.1 | Applied to: [DS-2CD6944G0-IHS(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780732335/Firmware__V5.7.120_260401_S3000712806.zip)(C) | 2024-06-13 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780732335/Firmware__V5.7.120_260401_S3000712806.zip) | — |
| 5.7.0 | Applied to: [DS-2CD6944G0-IHS(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780096165/Firmware__V5.7.0_230221_S3000488889.zip) | 2024-01-29 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780096165/Firmware__V5.7.0_230221_S3000488889.zip) | New function · Fix the issue of no stream when using the ONVIF protocol to connect to third -party platforms after · restarting in panoramic multi-channel mode. · [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202312/releasenote%5CIPCP_H5_5.5.820_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD6944G0-IHS(/NFC) - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.800 | Applied to: [DS-2CD6944G0-IHS(/NFC)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1778418467/34fbba54-1d37-4561-bb64-efceb8d155cb.zip), [DS-2CD6944G0-IHS/NFC(2.8MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1778418467/34fbba54-1d37-4561-bb64-efceb8d155cb.zip), [DS-2CD6944G0-IHS/NFC(6MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1778418467/34fbba54-1d37-4561-bb64-efceb8d155cb.zip), [DS-2CD6944G0-IHS(2.8MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1778418467/34fbba54-1d37-4561-bb64-efceb8d155cb.zip)(D), [DS-2CD6984G0-IH(S)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1778418467/34fbba54-1d37-4561-bb64-efceb8d155cb.zip)(AC)(/NFC), [DS-2CD6984G0-IHS/NFC(2.8MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1778418467/34fbba54-1d37-4561-bb64-efceb8d155cb.zip), [DS-2CD6984G0-IHS(2.8MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1778418467/34fbba54-1d37-4561-bb64-efceb8d155cb.zip)(D), [DS-2CD6984G0-IHSY(2.8MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1778418467/34fbba54-1d37-4561-bb64-efceb8d155cb.zip)(D) | 2021-10-09 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1778418467/34fbba54-1d37-4561-bb64-efceb8d155cb.zip) | 1. Improved Features  Fix security issue in ISAPI. · [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/b28e00a3-3d4d-405a-94e7-c3f287c0b839.pdf) |

</details>


<details>
<summary><h2>DS-2CD6944G1-IHS(U)Y - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.1 | Applied to: [DS-2CD6944G1-IHS(U)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.8.1_260330_S3000711487.zip)Y, [DS-2CD6944G1-IHSUY(2.8MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.8.1_260330_S3000711487.zip), [DS-2CD6984G1-IHS(U)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.8.1_260330_S3000711487.zip)Y(/NFC), [DS-2CD6984G1-IHSUY/NFC(2.8MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.8.1_260330_S3000711487.zip), [DS-2CD6984G1-IHSUY(2.8MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.8.1_260330_S3000711487.zip) | 2026-03-25 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.8.1_260330_S3000711487.zip) | — |

</details>


<details>
<summary><h2>DS-2CD6944G1-IHS-U-Y - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.1 | Applied to: [DS-2CD6944G1-IHS-U-Y](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.8.1_260330_S3000711487.zip) | 2026-03-25 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.8.1_260330_S3000711487.zip) | — |

</details>


<details>
<summary><h2>DS-2CD6951G2-IS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.11 | Applied to: [DS-2CD6951G2-IS(2mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780599961/Firmware__V5.8.110_260421_S3000718008.zip) | 2025-11-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780599961/Firmware__V5.8.110_260421_S3000718008.zip) | Modified Features · Optimize product functionality · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CIPCG_PS_G5_Camera_V5.8.11_251114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD6982G0-WU/4G - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.9.0 | Applied to: [DS-2CD6982G0-WU/4G](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780732335/Firmware__V5.9.0_260401_S3000711309.zip), [DS-2CD6982G0-WU/4G(2.8MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780732335/Firmware__V5.9.0_260401_S3000711309.zip)(ARGENTINA) | 2026-04-01 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780732335/Firmware__V5.9.0_260401_S3000711309.zip) | — |

</details>


<details>
<summary><h2>DS-2CD6984G0-IH - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.0 | Applied to: [DS-2CD6984G0-IHSAC/NFC(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780096165/Firmware__V5.7.0_230221_S3000488889.zip) | 2024-01-29 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780096165/Firmware__V5.7.0_230221_S3000488889.zip) | New function · Fix the issue of no stream when using the ONVIF protocol to connect to third -party platforms after · restarting in panoramic multi-channel mode. · [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202312/releasenote%5CIPCP_H5_5.5.820_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD6984G0-IH(S)(AC)(/NFC) - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.0 | Applied to: [DS-2CD6984G0-IH(S)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780096165/Firmware__V5.7.0_230221_S3000488889.zip)(AC)(/NFC), [DS-2CD6984G0-IHS/NFC(2.8MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780096165/Firmware__V5.7.0_230221_S3000488889.zip), [DS-2CD6984G0-IHS(2.8MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780096165/Firmware__V5.7.0_230221_S3000488889.zip)(D), [DS-2CD6984G0-IHSY(2.8MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780096165/Firmware__V5.7.0_230221_S3000488889.zip)(D) | 2023-02-21 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780096165/Firmware__V5.7.0_230221_S3000488889.zip) | 1. Improved Features  Fix security issue in ISAPI. · [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/b28e00a3-3d4d-405a-94e7-c3f287c0b839.pdf) |

</details>


<details>
<summary><h2>DS-2CD6984G0-IHS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.0 | Applied to: [DS-2CD6984G0-IHS/NFC(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780096165/Firmware__V5.7.0_230221_S3000488889.zip) | 2024-01-29 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780096165/Firmware__V5.7.0_230221_S3000488889.zip) | 1. Improved Features  Fix security issue in ISAPI. · [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/b28e00a3-3d4d-405a-94e7-c3f287c0b839.pdf) |

</details>


<details>
<summary><h2>DS-2CD6984G1-IHS-U-Y--NFC- - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.1 | Applied to: [DS-2CD6984G1-IHS-U-Y--NFC-](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.8.1_260330_S3000711487.zip) | 2026-03-25 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.8.1_260330_S3000711487.zip) | — |

</details>


<details>
<summary><h2>DS-2CD6B35G0-PLW - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.12 | Applied to: [DS-2CD6B35G0-PLW](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780617965/Firmware__V5.8.12_260407_S3000714560.zip), [DS-2CD6B35G0-PLW(4MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780617965/Firmware__V5.8.12_260407_S3000714560.zip) | 2026-04-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780617965/Firmware__V5.8.12_260407_S3000714560.zip) | — |

</details>


<details>
<summary><h2>DS-2CD6B55G0-PL(/T1) - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.211 | Applied to: [DS-2CD6B55G0-PL(/T1)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.7.211_260331_S3000713599.zip), [DS-2CD6B55G0-PL(4MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.7.211_260331_S3000713599.zip), [DS-2CD6B55G0-PL/T1(4MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.7.211_260331_S3000713599.zip) | 2026-03-31 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.7.211_260331_S3000713599.zip) | — |

</details>


<details>
<summary><h2>DS-2CD6D24FWD-IZHS(B) - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.821 | Applied to: [DS-2CD6D24FWD-IZHS(B)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1772533726/Firmware__V5.5.821_230830_S3000530199.zip), [DS-2CD6D24FWD-IZHS(2.8-12MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1772533726/Firmware__V5.5.821_230830_S3000530199.zip)(B), [DS-2CD6D54G1-IZS(B)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1772533726/Firmware__V5.5.821_230830_S3000530199.zip), [DS-2CD6D54G1-IZS(2.8-8MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1772533726/Firmware__V5.5.821_230830_S3000530199.zip)(B) | 2023-08-30 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1772533726/Firmware__V5.5.821_230830_S3000530199.zip) | New function · Fixed some known issues · [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202310/releasenote%5CIPCMC_H3_V5.5.821_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD6D42G0-IS - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.21 | Applied to: [DS-2CD6D42G0-IS](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779753206/Firmware__V5.8.21_260402_S3000713101.zip), [DS-2CD6D42G0-IS(4MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779753206/Firmware__V5.8.21_260402_S3000713101.zip), [DS-2CD6D42G0-IS(6MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779753206/Firmware__V5.8.21_260402_S3000713101.zip) | 2026-04-02 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779753206/Firmware__V5.8.21_260402_S3000713101.zip) | — |
| 5.8.11 | Applied to: [DS-2CD6D42G0-IS(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780599961/Firmware__V5.8.110_260421_S3000718008.zip) | 2023-08-07 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780599961/Firmware__V5.8.110_260421_S3000718008.zip) | 1. Release new model PanoVu camera DS-2CD6951G2-IS · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202508/releasenote%5CIPCG_PS_G5_Camera_V5.8.11_250730_Release_Note.pdf) |

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
| 5.5.820 | Applied to: [DS-2CD6D52G0-IH(S)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780649800/Firmware__V5.5.820_260402_S3000712894.zip), [DS-2CD6D52G0-IHS(2.8MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780649800/Firmware__V5.5.820_260402_S3000712894.zip), [DS-2CD6D52G0-IH(2.8MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780649800/Firmware__V5.5.820_260402_S3000712894.zip), [DS-2CD6D52G0-IH(4MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780649800/Firmware__V5.5.820_260402_S3000712894.zip), [DS-2CD6D52G0-IH(6MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780649800/Firmware__V5.5.820_260402_S3000712894.zip), [DS-2CD6D52G0-IHS(4MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780649800/Firmware__V5.5.820_260402_S3000712894.zip), [DS-2CD6D52G0-IHS(6MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780649800/Firmware__V5.5.820_260402_S3000712894.zip), [DS-2CD6D82G0-IH(S)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780649800/Firmware__V5.5.820_260402_S3000712894.zip) | 2026-04-10 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780649800/Firmware__V5.5.820_260402_S3000712894.zip) | — |

</details>


<details>
<summary><h2>DS-2CD6D54FWD-(I)(Z)(H)(S)(/NFC) - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.801 | Applied to: [DS-2CD6D54FWD-(I)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1778212177/4c6ede40-0464-4a88-a0e4-f87cc45b37a2.zip)(Z)(H)(S)(/NFC), [DS-2CD6D54FWD-IZHS(2.8-12MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1778212177/4c6ede40-0464-4a88-a0e4-f87cc45b37a2.zip), [DS-2CD6D54FWD-IZHS/NFC(2.8-12MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1778212177/4c6ede40-0464-4a88-a0e4-f87cc45b37a2.zip), [DS-2CD6D54FWD-Z(2.8-12MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1778212177/4c6ede40-0464-4a88-a0e4-f87cc45b37a2.zip), [DS-2CD6D54FWD-IZ(2.8-12MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1778212177/4c6ede40-0464-4a88-a0e4-f87cc45b37a2.zip), [DS-2CD6D54FWD-IZS(2.8-12MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1778212177/4c6ede40-0464-4a88-a0e4-f87cc45b37a2.zip), [DS-2CD6D54G1-IZ(S)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1778212177/4c6ede40-0464-4a88-a0e4-f87cc45b37a2.zip), [DS-2CD6D54G1-IZS(2.8-8MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1778212177/4c6ede40-0464-4a88-a0e4-f87cc45b37a2.zip) | 2021-09-27 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1778212177/4c6ede40-0464-4a88-a0e4-f87cc45b37a2.zip) | improve product performance, and will take effect automatically after upgrading from previous versions. · [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202207/IPC%20V5.5.801%20build%20210927%20Release%20Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD6F82G0-S - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.3 | Applied to: [DS-2CD6F82G0-S](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780649800/Firmware__V5.8.3_260402_S3000712976.zip), [DS-2CD6F82G0-S(4MM/8MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780649800/Firmware__V5.8.3_260402_S3000712976.zip), [DS-2CD6F82G0-S(2.8MM/6MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780649800/Firmware__V5.8.3_260402_S3000712976.zip), [DS-2CD6F82G0-WS](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780649800/Firmware__V5.8.3_260402_S3000712976.zip), [DS-2CD6F82G0-WS(4MM/8MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780649800/Firmware__V5.8.3_260402_S3000712976.zip), [DS-2CD6F82G0-WS(2.8MM/6MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780649800/Firmware__V5.8.3_260402_S3000712976.zip) | 2026-05-12 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780649800/Firmware__V5.8.3_260402_S3000712976.zip) | — |

</details>


<details>
<summary><h2>DS-2CFW02(/EU) - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.23 | Applied to: [DS-2CFW02(/EU)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780649800/Firmware__V5.8.23_260403_S3000712854.zip), [DS-2CFW02(2.8MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780649800/Firmware__V5.8.23_260403_S3000712854.zip), [DS-2CFW02(4MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780649800/Firmware__V5.8.23_260403_S3000712854.zip), [DS-2CV1023G2-LIDW(F)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780649800/Firmware__V5.8.23_260403_S3000712854.zip)(B), [DS-2CV1023G2-LIDWF(2.8MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780649800/Firmware__V5.8.23_260403_S3000712854.zip)(B), [DS-2CV1023G2-LIDWF(4MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780649800/Firmware__V5.8.23_260403_S3000712854.zip)(B), [DS-2CV1F23G2-LIDWF(B)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780649800/Firmware__V5.8.23_260403_S3000712854.zip), [DS-2CV1F23G2-LIDWF(2.8MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780649800/Firmware__V5.8.23_260403_S3000712854.zip)(B) | 2026-04-03 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780649800/Firmware__V5.8.23_260403_S3000712854.zip) | 1. Fixed some bugs to enhance system stability. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202605/releasenote%5CNetwork_Camera-V5.8.23_SP1_Release_Note-E9_E10.pdf) |

</details>


<details>
<summary><h2>DS-2CFW04(/EU) - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.23 | Applied to: [DS-2CFW04(/EU)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780649800/Firmware__V5.8.23_260403_S3000712854.zip), [DS-2CFW04(2.8MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780649800/Firmware__V5.8.23_260403_S3000712854.zip), [DS-2CFW04(4MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780649800/Firmware__V5.8.23_260403_S3000712854.zip), [DS-2CV1043G2-LIDW(F)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780649800/Firmware__V5.8.23_260403_S3000712854.zip)(B), [DS-2CV1043G2-LIDWF(2.8MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780649800/Firmware__V5.8.23_260403_S3000712854.zip)(B), [DS-2CV1043G2-LIDWF(4MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780649800/Firmware__V5.8.23_260403_S3000712854.zip)(B), [DS-2CV1F43G2-LIDWF(B)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780649800/Firmware__V5.8.23_260403_S3000712854.zip), [DS-2CV1F43G2-LIDWF(2.8MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780649800/Firmware__V5.8.23_260403_S3000712854.zip)(B) | 2026-04-03 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780649800/Firmware__V5.8.23_260403_S3000712854.zip) | 1. Fixed some bugs to enhance system stability. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202605/releasenote%5CNetwork_Camera-V5.8.23_SP1_Release_Note-E9_E10.pdf) |

</details>


<details>
<summary><h2>DS-2CFW06-P - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.10 | Applied to: [DS-2CFW06-P](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780617965/Firmware__V5.8.10_260403_S3000714421.zip), [DS-2CFW06-P(2.8MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780617965/Firmware__V5.8.10_260403_S3000714421.zip) | 2026-03-30 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780617965/Firmware__V5.8.10_260403_S3000714421.zip) | — |

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
| 5.8.110 | Applied to: [DS-2CFWQ6-D](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780599961/Firmware__V5.8.110_260421_S3000718008.zip), [DS-2CFWQ6-D(2.8+4MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780599961/Firmware__V5.8.110_260421_S3000718008.zip) | 2026-04-16 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780599961/Firmware__V5.8.110_260421_S3000718008.zip) | — |

</details>


<details>
<summary><h2>DS-2DE2A204IW-DE3 - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.11 | Applied to: [DS-2DE2A204IW-DE3(C0)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780683636/Firmware__V5.7.11_260402_S3000713041.zip)(S6)(C) | 2023-06-12 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780683636/Firmware__V5.7.11_260402_S3000713041.zip) | - Fixed some known bugs, recommended upgrade · [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202312/releasenote%5CRelease_Note_E7_V5.7.11_230612.pdf) |

</details>


<details>
<summary><h2>DS-2DE2A204IW-DE3(S6) - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.30 | Applied to: [DS-2DE2A204IW-DE3(S6)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779474355/Firmware__V5.7.30_260326_S3000711197.zip), [DS-2DE2A204IW-DE3(C0)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779474355/Firmware__V5.7.30_260326_S3000711197.zip)(S6)(C), [DS-2DE2A404IW-DE3(S6)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779474355/Firmware__V5.7.30_260326_S3000711197.zip), [DS-2DE2A404IW-DE3(C0)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779474355/Firmware__V5.7.30_260326_S3000711197.zip)(S6)(C), [DS-2DE4A225IW-DE(S6)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779474355/Firmware__V5.7.30_260326_S3000711197.zip), [DS-2DE4A425IW-DE(S6)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779474355/Firmware__V5.7.30_260326_S3000711197.zip), [DS-2DE5225IW-AE(S6)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779474355/Firmware__V5.7.30_260326_S3000711197.zip), [DS-2DE5232IW-AE(S6)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779474355/Firmware__V5.7.30_260326_S3000711197.zip) | 2026-03-26 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779474355/Firmware__V5.7.30_260326_S3000711197.zip) | — |

</details>


<details>
<summary><h2>DS-2DE2A204IWG1-E - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.9.5 | Applied to: [DS-2DE2A204IWG1-E](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780649800/Firmware__V5.9.51_260403_S3000712992.zip), [DS-2DE2A404IWG1-E](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780649800/Firmware__V5.9.51_260403_S3000712992.zip), [DS-2DE2A604IWG1-E](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780649800/Firmware__V5.9.51_260403_S3000712992.zip) | 2026-04-20 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780649800/Firmware__V5.9.51_260403_S3000712992.zip) | — |

</details>


<details>
<summary><h2>DS-2DE2A204IWG1-E/W - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.9.2 | Applied to: [DS-2DE2A204IWG1-E/W](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779753206/Firmware__V5.9.21_260423_S3000719054.zip), [DS-2DE2A404IWG1-E/W](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779753206/Firmware__V5.9.21_260423_S3000719054.zip), [DS-2DE2A604IWG1-E/W](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779753206/Firmware__V5.9.21_260423_S3000719054.zip) | 2026-04-16 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779753206/Firmware__V5.9.21_260423_S3000719054.zip) | 1. Algorithm optimization and updates. 2. Fix some bugs. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202604/releasenote%5CV5.9.2_260416_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2DE2A404IW-DE3 - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.11 | Applied to: [DS-2DE2A404IW-DE3(C0)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780683636/Firmware__V5.7.11_260402_S3000713041.zip)(S6)(C) | 2023-06-12 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780683636/Firmware__V5.7.11_260402_S3000713041.zip) | - Fixed some known bugs, recommended upgrade · [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202312/releasenote%5CRelease_Note_E7_V5.7.11_230612.pdf) |

</details>


<details>
<summary><h2>DS-2DE2C600MWG-E - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.1 | Applied to: [DS-2DE2C600MWG-E(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.8.1_260330_S3000711487.zip) | 2025-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.8.1_260330_S3000711487.zip) | 1. Algorithm optimization and updates. 2. Fix some bugs. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CV5.8.1_250114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2DE3204W-DE - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.1 | Applied to: [DS-2DE3204W-DE(T5)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.8.1_260330_S3000711487.zip) | 2023-11-08 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.8.1_260330_S3000711487.zip) | 1. Algorithm optimization and updates. 2. Fix some bugs. · [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202408/releasenote%5CIPDE_C_H8_V5.8.1_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2DE3204W-DE(T5) - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.1 | Applied to: [DS-2DE3204W-DE(T5)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.8.1_260330_S3000711487.zip) | 2026-04-02 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.8.1_260330_S3000711487.zip) | — |

</details>


<details>
<summary><h2>DS-2DE3A400BW-DE(T5) - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.0 | Applied to: [DS-2DE3A400BW-DE(T5)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780649800/Firmware__V5.8.0_260402_S3000712887.zip), [DS-2DE3A400BW-DE(F1)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780649800/Firmware__V5.8.0_260402_S3000712887.zip)(T5), [DS-2DE3A404IWG-E/W](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780649800/Firmware__V5.8.0_260402_S3000712887.zip), [DS-2DE4225WG-E3](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780649800/Firmware__V5.8.0_260402_S3000712887.zip), [DS-2DE4A225IWG-E](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780649800/Firmware__V5.8.0_260402_S3000712887.zip), [DS-2DE7A220MCG-EB](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780649800/Firmware__V5.8.0_260402_S3000712887.zip), [DS-2DE7A412MCG-EB](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780649800/Firmware__V5.8.0_260402_S3000712887.zip), [DS-2DE7A812MCG-EB](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780649800/Firmware__V5.8.0_260402_S3000712887.zip) | 2026-04-04 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780649800/Firmware__V5.8.0_260402_S3000712887.zip) | — |

</details>


<details>
<summary><h2>DS-2DE4215IW-DE - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.11 | Applied to: [DS-2DE4215IW-DE(S6)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780683636/Firmware__V5.7.11_260402_S3000713041.zip) | 2022-09-05 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780683636/Firmware__V5.7.11_260402_S3000713041.zip) | Modified Features · Support ezviz cloud online upgrade · Compatible with the new hardware modules: NL668-CN30 · [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202312/releasenote%5CV5.7.11_Release_Note--E7.pdf) |

</details>


<details>
<summary><h2>DS-2DE4215IW-DE(T5) - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.13 | Applied to: [DS-2DE4215IW-DE(T5)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780649800/Firmware__V5.8.13_260402_S3000713021.zip), [DS-2DE4215IWG-E](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780649800/Firmware__V5.8.13_260402_S3000713021.zip), [DS-2DE4215IWG-E(B)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780649800/Firmware__V5.8.13_260402_S3000713021.zip), [DS-2DE4225IW-DE(T5)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780649800/Firmware__V5.8.13_260402_S3000713021.zip), [DS-2DE4225IWG-E](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780649800/Firmware__V5.8.13_260402_S3000713021.zip), [DS-2DE4225IWG-E(B)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780649800/Firmware__V5.8.13_260402_S3000713021.zip), [DS-2DE4415IW-DE(T5)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780649800/Firmware__V5.8.13_260402_S3000713021.zip), [DS-2DE4415IWG-E](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780649800/Firmware__V5.8.13_260402_S3000713021.zip) | 2026-04-02 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780649800/Firmware__V5.8.13_260402_S3000713021.zip) | — |

</details>


<details>
<summary><h2>DS-2DE4215IWG1-E - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.1 | Applied to: [DS-2DE4215IWG1-E](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.8.1_260330_S3000711487.zip) | 2026-01-15 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.8.1_260330_S3000711487.zip) | 1. Add Tracking function to the 4 series 4MP PTZ camera.  Modify Features 1. Cybersecurity Compliance Remediation. 2. Update the SDK and PHY network interface controller. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202603/releasenote%5CV5.8.1_260115_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2DE4225IW-DE - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.11 | Applied to: [DS-2DE4225IW-DE(S6)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780683636/Firmware__V5.7.11_260402_S3000713041.zip) | 2022-09-05 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780683636/Firmware__V5.7.11_260402_S3000713041.zip) | Modified Features · Support ezviz cloud online upgrade · Compatible with the new hardware modules: NL668-CN30 · [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202312/releasenote%5CV5.7.11_Release_Note--E7.pdf) |

</details>


<details>
<summary><h2>DS-2DE4225IWG1-E - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.1 | Applied to: [DS-2DE4225IWG1-E](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.8.1_260330_S3000711487.zip) | 2026-01-15 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.8.1_260330_S3000711487.zip) | 1. Add Tracking function to the 4 series 4MP PTZ camera.  Modify Features 1. Cybersecurity Compliance Remediation. 2. Update the SDK and PHY network interface controller. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202603/releasenote%5CV5.8.1_260115_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2DE4225W-DE - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.11 | Applied to: [DS-2DE4225W-DE(S6)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780683636/Firmware__V5.7.11_260402_S3000713041.zip) | 2022-09-05 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780683636/Firmware__V5.7.11_260402_S3000713041.zip) | Modified Features · Support ezviz cloud online upgrade · Compatible with the new hardware modules: NL668-CN30 · [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202312/releasenote%5CV5.7.11_Release_Note--E7.pdf) |

</details>


<details>
<summary><h2>DS-2DE4225W-DE3 - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.11 | Applied to: [DS-2DE4225W-DE3(S6)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780683636/Firmware__V5.7.11_260402_S3000713041.zip) | 2022-09-05 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780683636/Firmware__V5.7.11_260402_S3000713041.zip) | Modified Features · Support ezviz cloud online upgrade · Compatible with the new hardware modules: NL668-CN30 · [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202312/releasenote%5CV5.7.11_Release_Note--E7.pdf) |

</details>


<details>
<summary><h2>DS-2DE4225WG1-E3 - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.1 | Applied to: [DS-2DE4225WG1-E3](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.8.1_260330_S3000711487.zip) | 2026-01-15 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.8.1_260330_S3000711487.zip) | 1. Add Tracking function to the 4 series 4MP PTZ camera.  Modify Features 1. Cybersecurity Compliance Remediation. 2. Update the SDK and PHY network interface controller. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202603/releasenote%5CV5.8.1_260115_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2DE4415IW-DE - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.11 | Applied to: [DS-2DE4415IW-DE(S6)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780683636/Firmware__V5.7.11_260402_S3000713041.zip) | 2022-09-05 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780683636/Firmware__V5.7.11_260402_S3000713041.zip) | Modified Features · Support ezviz cloud online upgrade · Compatible with the new hardware modules: NL668-CN30 · [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202312/releasenote%5CV5.7.11_Release_Note--E7.pdf) |

</details>


<details>
<summary><h2>DS-2DE4415IWG1-E - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.1 | Applied to: [DS-2DE4415IWG1-E](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.8.1_260330_S3000711487.zip) | 2026-01-15 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.8.1_260330_S3000711487.zip) | 1. Add Tracking function to the 4 series 4MP PTZ camera.  Modify Features 1. Cybersecurity Compliance Remediation. 2. Update the SDK and PHY network interface controller. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202603/releasenote%5CV5.8.1_260115_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2DE4425IW-DE - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.11 | Applied to: [DS-2DE4425IW-DE(S6)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780683636/Firmware__V5.7.11_260402_S3000713041.zip) | 2022-09-05 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780683636/Firmware__V5.7.11_260402_S3000713041.zip) | Modified Features · Support ezviz cloud online upgrade · Compatible with the new hardware modules: NL668-CN30 · [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202312/releasenote%5CV5.7.11_Release_Note--E7.pdf) |

</details>


<details>
<summary><h2>DS-2DE4425IWG1-E - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.1 | Applied to: [DS-2DE4425IWG1-E](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.8.1_260330_S3000711487.zip) | 2026-01-15 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.8.1_260330_S3000711487.zip) | 1. Add Tracking function to the 4 series 4MP PTZ camera.  Modify Features 1. Cybersecurity Compliance Remediation. 2. Update the SDK and PHY network interface controller. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202603/releasenote%5CV5.8.1_260115_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2DE4425W-DE - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.11 | Applied to: [DS-2DE4425W-DE(S6)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780683636/Firmware__V5.7.11_260402_S3000713041.zip) | 2022-09-05 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780683636/Firmware__V5.7.11_260402_S3000713041.zip) | Modified Features · Support ezviz cloud online upgrade · Compatible with the new hardware modules: NL668-CN30 · [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202312/releasenote%5CV5.7.11_Release_Note--E7.pdf) |

</details>


<details>
<summary><h2>DS-2DE4425W-DE3 - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.11 | Applied to: [DS-2DE4425W-DE3(S6)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780683636/Firmware__V5.7.11_260402_S3000713041.zip) | 2022-09-05 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780683636/Firmware__V5.7.11_260402_S3000713041.zip) | Modified Features · Support ezviz cloud online upgrade · Compatible with the new hardware modules: NL668-CN30 · [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202312/releasenote%5CV5.7.11_Release_Note--E7.pdf) |

</details>


<details>
<summary><h2>DS-2DE4425WG1-E3 - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.1 | Applied to: [DS-2DE4425WG1-E3](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.8.1_260330_S3000711487.zip) | 2026-01-15 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.8.1_260330_S3000711487.zip) | 1. Add Tracking function to the 4 series 4MP PTZ camera.  Modify Features 1. Cybersecurity Compliance Remediation. 2. Update the SDK and PHY network interface controller. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202603/releasenote%5CV5.8.1_260115_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2DE4432WG-E3 - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.0 | Applied to: [DS-2DE4432WG-E3](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780649800/Firmware__V5.8.0_260402_S3000712887.zip), [DS-2DE4825WG-E3](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780649800/Firmware__V5.8.0_260402_S3000712887.zip) | 2026-04-02 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780649800/Firmware__V5.8.0_260402_S3000712887.zip) | — |

</details>


<details>
<summary><h2>DS-2DE4825IWG1-E - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.1 | Applied to: [DS-2DE4825IWG1-E](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.8.1_260330_S3000711487.zip) | 2026-01-15 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.8.1_260330_S3000711487.zip) | 1. Add Tracking function to the 4 series 4MP PTZ camera.  Modify Features 1. Cybersecurity Compliance Remediation. 2. Update the SDK and PHY network interface controller. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202603/releasenote%5CV5.8.1_260115_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2DE4A225IW-DE - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.11 | Applied to: [DS-2DE4A225IW-DE(S6)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780683636/Firmware__V5.7.11_260402_S3000713041.zip) | 2023-06-12 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780683636/Firmware__V5.7.11_260402_S3000713041.zip) | - Fixed some known bugs, recommended upgrade · [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202312/releasenote%5CRelease_Note_E7_V5.7.11_230612.pdf) |

</details>


<details>
<summary><h2>DS-2DE4A225IWG1-E - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.1 | Applied to: [DS-2DE4A225IWG1-E](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.8.1_260330_S3000711487.zip) | 2026-01-15 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.8.1_260330_S3000711487.zip) | 1. Add Tracking function to the 4 series 4MP PTZ camera.  Modify Features 1. Cybersecurity Compliance Remediation. 2. Update the SDK and PHY network interface controller. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202603/releasenote%5CV5.8.1_260115_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2DE4A425IW-DE - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.11 | Applied to: [DS-2DE4A425IW-DE(S6)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780683636/Firmware__V5.7.11_260402_S3000713041.zip) | 2023-06-12 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780683636/Firmware__V5.7.11_260402_S3000713041.zip) | - Fixed some known bugs, recommended upgrade · [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202312/releasenote%5CRelease_Note_E7_V5.7.11_230612.pdf) |

</details>


<details>
<summary><h2>DS-2DE4A425IWG1-E - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.1 | Applied to: [DS-2DE4A425IWG1-E](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.8.1_260330_S3000711487.zip) | 2026-01-15 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.8.1_260330_S3000711487.zip) | 1. Add Tracking function to the 4 series 4MP PTZ camera.  Modify Features 1. Cybersecurity Compliance Remediation. 2. Update the SDK and PHY network interface controller. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202603/releasenote%5CV5.8.1_260115_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2DE5225IW-AE - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.11 | Applied to: [DS-2DE5225IW-AE(S6)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780683636/Firmware__V5.7.11_260402_S3000713041.zip) | 2023-06-12 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780683636/Firmware__V5.7.11_260402_S3000713041.zip) | - Fixed some known bugs, recommended upgrade · [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202312/releasenote%5CRelease_Note_E7_V5.7.11_230612.pdf) |

</details>


<details>
<summary><h2>DS-2DE5232IW-AE - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.11 | Applied to: [DS-2DE5232IW-AE(S6)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780683636/Firmware__V5.7.11_260402_S3000713041.zip) | 2023-06-12 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780683636/Firmware__V5.7.11_260402_S3000713041.zip) | - Fixed some known bugs, recommended upgrade · [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202312/releasenote%5CRelease_Note_E7_V5.7.11_230612.pdf) |

</details>


<details>
<summary><h2>DS-2DE5232W-AE - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.11 | Applied to: [DS-2DE5232W-AE(S6)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780683636/Firmware__V5.7.11_260402_S3000713041.zip) | 2023-06-12 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780683636/Firmware__V5.7.11_260402_S3000713041.zip) | - Fixed some known bugs, recommended upgrade · [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202312/releasenote%5CRelease_Note_E7_V5.7.11_230612.pdf) |

</details>


<details>
<summary><h2>DS-2DE5425IW-AE - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.11 | Applied to: [DS-2DE5425IW-AE(S6)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780683636/Firmware__V5.7.11_260402_S3000713041.zip) | 2023-06-12 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780683636/Firmware__V5.7.11_260402_S3000713041.zip) | - Fixed some known bugs, recommended upgrade · [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202312/releasenote%5CRelease_Note_E7_V5.7.11_230612.pdf) |

</details>


<details>
<summary><h2>DS-2DE5425IWG1-E - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.1 | Applied to: [DS-2DE5425IWG1-E](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.8.1_260330_S3000711487.zip) | 2026-01-15 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.8.1_260330_S3000711487.zip) | 1. Add Tracking function to the 4 series 4MP PTZ camera.  Modify Features 1. Cybersecurity Compliance Remediation. 2. Update the SDK and PHY network interface controller. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202603/releasenote%5CV5.8.1_260115_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2DE5425WG1-E - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.1 | Applied to: [DS-2DE5425WG1-E](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.8.1_260330_S3000711487.zip) | 2026-01-15 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.8.1_260330_S3000711487.zip) | 1. Add Tracking function to the 4 series 4MP PTZ camera.  Modify Features 1. Cybersecurity Compliance Remediation. 2. Update the SDK and PHY network interface controller. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202603/releasenote%5CV5.8.1_260115_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2DE5432IWG1-E - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.1 | Applied to: [DS-2DE5432IWG1-E](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.8.1_260330_S3000711487.zip) | 2026-01-15 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.8.1_260330_S3000711487.zip) | 1. Add Tracking function to the 4 series 4MP PTZ camera.  Modify Features 1. Cybersecurity Compliance Remediation. 2. Update the SDK and PHY network interface controller. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202603/releasenote%5CV5.8.1_260115_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2DE5432WG1-E - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.1 | Applied to: [DS-2DE5432WG1-E](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.8.1_260330_S3000711487.zip) | 2026-01-15 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.8.1_260330_S3000711487.zip) | 1. Add Tracking function to the 4 series 4MP PTZ camera.  Modify Features 1. Cybersecurity Compliance Remediation. 2. Update the SDK and PHY network interface controller. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202603/releasenote%5CV5.8.1_260115_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2DE7225IW-AE - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.11 | Applied to: [DS-2DE7225IW-AE(S6)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780683636/Firmware__V5.7.11_260402_S3000713041.zip) | 2022-09-05 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780683636/Firmware__V5.7.11_260402_S3000713041.zip) | Modified Features · Support ezviz cloud online upgrade · Compatible with the new hardware modules: NL668-CN30 · [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202312/releasenote%5CV5.7.11_Release_Note--E7.pdf) |

</details>


<details>
<summary><h2>DS-2DE7A225IWG-EB/SL - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.13 | Applied to: [DS-2DE7A225IWG-EB/SL](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780649800/Firmware__V5.8.13_260402_S3000713021.zip), [DS-2DE7A232IWG-EB/SL](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780649800/Firmware__V5.8.13_260402_S3000713021.zip) | 2026-04-22 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780649800/Firmware__V5.8.13_260402_S3000713021.zip) | — |

</details>


<details>
<summary><h2>DS-2DF3C400SCG-D(/4G)(/WL15 WL40)(F1) - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.12 | Applied to: [DS-2DF3C400SCG-D(/4G)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780617965/Firmware__V5.8.12_260407_S3000714560.zip)(/WL15 WL40)(F1), [DS-2DF3C400SCG-D/WL40(F1)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780617965/Firmware__V5.8.12_260407_S3000714560.zip), [DS-2DF3C400SCG-D/4G/WL15(F1)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780617965/Firmware__V5.8.12_260407_S3000714560.zip), [DS-2DF3C400SCG-D/WL15(F1)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780617965/Firmware__V5.8.12_260407_S3000714560.zip), [DS-2DF3C400SCG-D/4G/WL40(F1)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780617965/Firmware__V5.8.12_260407_S3000714560.zip) | 2026-04-07 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780617965/Firmware__V5.8.12_260407_S3000714560.zip) | — |

</details>


<details>
<summary><h2>DS-2DF4220-DX(S6/316L) - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.11 | Applied to: [[DS-2DF4220-DX(S6/316L)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780683636/Firmware__V5.7.11_260402_S3000713041.zip)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780683636/Firmware__V5.7.11_260402_S3000713041.zip), DS-2DF4220-DX(S6/316L)(C), [[DS-2DF4420-DX(S6)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780683636/Firmware__V5.7.11_260402_S3000713041.zip)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780683636/Firmware__V5.7.11_260402_S3000713041.zip)(C)(304), DS-2DF4420-DX(S6)(C), [DS-2DF4420-DX(S6/316L)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780683636/Firmware__V5.7.11_260402_S3000713041.zip)(C), [DS-2DF4420WG-XEY](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780683636/Firmware__V5.7.11_260402_S3000713041.zip) | 2026-04-13 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780683636/Firmware__V5.7.11_260402_S3000713041.zip) | — |

</details>


<details>
<summary><h2>DS-2DF4220-DX-S6-316L- - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.11 | Applied to: [DS-2DF4220-DX-S6-316L-](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780683636/Firmware__V5.7.11_260402_S3000713041.zip) | 2026-04-13 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780683636/Firmware__V5.7.11_260402_S3000713041.zip) | — |

</details>


<details>
<summary><h2>DS-2DF4220-DX-S6-316L--C- - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.11 | Applied to: [DS-2DF4220-DX-S6-316L--C-](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780683636/Firmware__V5.7.11_260402_S3000713041.zip) | 2026-04-13 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780683636/Firmware__V5.7.11_260402_S3000713041.zip) | — |

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
| 5.7.11 | Applied to: [DS-2DF4420-DX-S6--C--304-](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780683636/Firmware__V5.7.11_260402_S3000713041.zip) | 2026-04-13 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780683636/Firmware__V5.7.11_260402_S3000713041.zip) | — |

</details>


<details>
<summary><h2>DS-2DF4420-DX-S6-316L--C- - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.11 | Applied to: [DS-2DF4420-DX-S6-316L--C-](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780683636/Firmware__V5.7.11_260402_S3000713041.zip) | 2026-04-13 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780683636/Firmware__V5.7.11_260402_S3000713041.zip) | — |

</details>


<details>
<summary><h2>DS-2DF4420WG-XEY - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.11 | Applied to: [DS-2DF4420WG-XEY](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780683636/Firmware__V5.7.11_260402_S3000713041.zip) | 2026-04-13 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780683636/Firmware__V5.7.11_260402_S3000713041.zip) | — |

</details>


<details>
<summary><h2>DS-2DF5225X-AE3(T5) - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.7 | Applied to: [DS-2DF5225X-AE3(T5)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779352270/Firmware__V5.8.7_260330_S3000712757.zip), [DS-2DF5232X-AE3(T5)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779352270/Firmware__V5.8.7_260330_S3000712757.zip), [DS-2DF5232X-AEL(T5)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779352270/Firmware__V5.8.7_260330_S3000712757.zip), [DS-2DF6A225X-AEL(T5)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779352270/Firmware__V5.8.7_260330_S3000712757.zip), [DS-2DF6A436X-AEL(T5)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779352270/Firmware__V5.8.7_260330_S3000712757.zip), [DS-2DF6A436X-AELY(T5)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779352270/Firmware__V5.8.7_260330_S3000712757.zip), [DS-2DF6A832X-DE3(T5)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779352270/Firmware__V5.8.7_260330_S3000712757.zip), [DS-2DF6A836X-AEL(T5)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779352270/Firmware__V5.8.7_260330_S3000712757.zip) | 2026-03-30 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779352270/Firmware__V5.8.7_260330_S3000712757.zip) | — |

</details>


<details>
<summary><h2>DS-2DF6223-CX(T5/316L) - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.7 | Applied to: [DS-2DF6223-CX(T5/316L)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779178727/Firmware__V5.7.7_260410_S3000716682.zip), [DS-2DF6231-CX(T5/316L)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779178727/Firmware__V5.7.7_260410_S3000716682.zip), [DS-2DF6C431-CX(T5/316L)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779178727/Firmware__V5.7.7_260410_S3000716682.zip), [DS-2DF8432IWG-CXF(316L)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779178727/Firmware__V5.7.7_260410_S3000716682.zip) | 2026-04-10 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779178727/Firmware__V5.7.7_260410_S3000716682.zip) | — |

</details>


<details>
<summary><h2>DS-2DF6A225IWG1-EL - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.9.71 | Applied to: [DS-2DF6A225IWG1-EL](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.9.71_260331_S3000713857.zip), [DS-2DF6A425IWG1-EL](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.9.71_260331_S3000713857.zip), [DS-2DF6A632IWG1-EL](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.9.71_260331_S3000713857.zip), [DS-2DF6A825IXG1-EL](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.9.71_260331_S3000713857.zip), [[DS-2DF6C225IWG1-EL](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.9.71_260331_S3000713857.zip)(W)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.9.71_260331_S3000713857.zip), [DS-2DF6C225IWG1-ELW](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.9.71_260331_S3000713857.zip), DS-2DF6C225IWG1-EL, [DS-2DF6C425IWG1-EL(W)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.9.71_260331_S3000713857.zip) | 2026-03-31 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.9.71_260331_S3000713857.zip) | — |

</details>


<details>
<summary><h2>DS-2DF6A436XG1-EL(Y) - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.9.5 | Applied to: [[DS-2DF6A436XG1-EL](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780649800/Firmware__V5.9.51_260403_S3000712992.zip)(Y)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780649800/Firmware__V5.9.51_260403_S3000712992.zip), [DS-2DF6A436XG1-ELY](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780649800/Firmware__V5.9.51_260403_S3000712992.zip), DS-2DF6A436XG1-EL, [DS-2DF6A836XG1-EL](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780649800/Firmware__V5.9.51_260403_S3000712992.zip), [DS-2DF7C425IXG1-EL(W)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780649800/Firmware__V5.9.51_260403_S3000712992.zip)(Y), [DS-2DF7C425IXG1-ELY](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780649800/Firmware__V5.9.51_260403_S3000712992.zip), [DS-2DF7C425IXG1-ELW](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780649800/Firmware__V5.9.51_260403_S3000712992.zip), [DS-2DF7C425IXG1-ELWY](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780649800/Firmware__V5.9.51_260403_S3000712992.zip) | 2026-03-30 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780649800/Firmware__V5.9.51_260403_S3000712992.zip) | — |

</details>


<details>
<summary><h2>DS-2DF7C425IXR-AEL(T5) - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.7 | Applied to: [DS-2DF7C425IXR-AEL(T5)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779324458/Firmware__V5.8.7_260330_S3000711514.zip), [DS-2DF7C432IXR-AEL(T5)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779324458/Firmware__V5.8.7_260330_S3000711514.zip), [DS-2DF7C445IXR-AEL(T5)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779324458/Firmware__V5.8.7_260330_S3000711514.zip) | 2026-03-30 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779324458/Firmware__V5.8.7_260330_S3000711514.zip) | — |

</details>


<details>
<summary><h2>DS-2DF7C432MXG1-(W)R - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.9.60 | Applied to: [[DS-2DF7C432MXG1-(W)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780617965/Firmware__V5.9.60_260408_S3000715280.zip)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780617965/Firmware__V5.9.60_260408_S3000715280.zip)R, [DS-2DF7C432MXG1-R](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780617965/Firmware__V5.9.60_260408_S3000715280.zip), [DS-2DF7C432MXG1-WR](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780617965/Firmware__V5.9.60_260408_S3000715280.zip), DS-2DF7C432MXG1-(W)R/4G, [DS-2DF7C432MXG1-WR/4G](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780617965/Firmware__V5.9.60_260408_S3000715280.zip), [DS-2DF7C432MXG1-WR/4G(LA)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780617965/Firmware__V5.9.60_260408_S3000715280.zip), [DS-2DF7C432MXG1-R/4G](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780617965/Firmware__V5.9.60_260408_S3000715280.zip), [DS-2DF7C432MXG1-R/4G(LA)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780617965/Firmware__V5.9.60_260408_S3000715280.zip) | 2026-04-03 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780617965/Firmware__V5.9.60_260408_S3000715280.zip) | — |

</details>


<details>
<summary><h2>DS-2DF7C432MXG1-WRP/4G - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.9.63 | Applied to: [DS-2DF7C432MXG1-WRP/4G](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780732335/Firmware__V5.9.63_260401_S3000712674.zip) | 2026-04-01 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780732335/Firmware__V5.9.63_260401_S3000712674.zip) | — |

</details>


<details>
<summary><h2>DS-2DF7C442IXG1-ELWYP - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.9.63 | Applied to: [DS-2DF7C442IXG1-ELWYP](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780732335/Firmware__V5.9.63_260401_S3000712674.zip), [DS-2DF7C842IXG1-ELWYP](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780732335/Firmware__V5.9.63_260401_S3000712674.zip), [DS-2DF8C435MHG1-ELWYP](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780732335/Firmware__V5.9.63_260401_S3000712674.zip) | 2026-03-25 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780732335/Firmware__V5.9.63_260401_S3000712674.zip) | — |

</details>


<details>
<summary><h2>DS-2DF8425IX-AEL(T5) - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.7 | Applied to: [DS-2DF8425IX-AEL(T5)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779352270/Firmware__V5.8.7_260330_S3000712735.zip), [DS-2DF8425IX-AELW(T5)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779352270/Firmware__V5.8.7_260330_S3000712735.zip), [DS-2DF8C260I5XG-ELW](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779352270/Firmware__V5.8.7_260330_S3000712735.zip), [DS-2DF8C442IXS-AL/5G(T5)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779352270/Firmware__V5.8.7_260330_S3000712735.zip), [DS-2DF8C448I5XG-ELW](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779352270/Firmware__V5.8.7_260330_S3000712735.zip), [DS-2DF8C848I5XG-ELW](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779352270/Firmware__V5.8.7_260330_S3000712735.zip), [DS-2DF9C453LXG-LW](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779352270/Firmware__V5.8.7_260330_S3000712735.zip), [DS-2DF9C848LXG-LW](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779352270/Firmware__V5.8.7_260330_S3000712735.zip) | 2026-03-30 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779352270/Firmware__V5.8.7_260330_S3000712735.zip) | — |

</details>


<details>
<summary><h2>DS-2DF8C425MHS-DEL - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.7 | Applied to: [DS-2DF8C425MHS-DEL](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779437855/Firmware__V5.8.7_260326_S3000711610.zip), [DS-2DF8C425MHS-DELW](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779437855/Firmware__V5.8.7_260326_S3000711610.zip), [DS-2DF8C435MHS-DEL](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779437855/Firmware__V5.8.7_260326_S3000711610.zip), [DS-2DF8C435MHS-DELW](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779437855/Firmware__V5.8.7_260326_S3000711610.zip) | 2026-03-26 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779437855/Firmware__V5.8.7_260326_S3000711610.zip) | — |

</details>


<details>
<summary><h2>DS-2DP0818ZIXS-DE/440(F0)(P4) - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.120 | Applied to: [DS-2DP0818ZIXS-DE/440(F0)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780732335/Firmware__V5.7.120_260401_S3000712806.zip)(P4), [DS-2DP1618ZIXS-DE/440(F0)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780732335/Firmware__V5.7.120_260401_S3000712806.zip)(P4), [DS-2DP2427ZIXS-DE/440(F0)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780732335/Firmware__V5.7.120_260401_S3000712806.zip)(P4), [DS-2DP3236ZIXS-D/440(F0)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780732335/Firmware__V5.7.120_260401_S3000712806.zip)(P4), [DS-2DP8A440IXG-LEF/408(F0)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780732335/Firmware__V5.7.120_260401_S3000712806.zip)(B), [DS-2DP8A440IXG-LEF/416(F0)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780732335/Firmware__V5.7.120_260401_S3000712806.zip)(B), [DS-2DP8A440IXG-LEF/624(F0)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780732335/Firmware__V5.7.120_260401_S3000712806.zip)(B), [DS-2DP8A440IXG-LF/832(F0)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780732335/Firmware__V5.7.120_260401_S3000712806.zip)(B) | 2026-04-01 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780732335/Firmware__V5.7.120_260401_S3000712806.zip) | — |

</details>


<details>
<summary><h2>DS-2DP1618ZIXS-D/440(F0)(P5) - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.5 | Applied to: [DS-2DP1618ZIXS-D/440(F0)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780043044/Firmware__V5.8.5_260522_S3000724366.zip)(P5), [DS-2DP3236ZIXS-D/440(F0)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780043044/Firmware__V5.8.5_260522_S3000724366.zip)(P5) | 2026-05-22 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780043044/Firmware__V5.8.5_260522_S3000724366.zip) | — |

</details>


<details>
<summary><h2>DS-2DP3D404IWG1-E/36 - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.0 | Applied to: [DS-2DP3D404IWG1-E/36](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780649800/Firmware__V5.8.0_260402_S3000712887.zip), [DS-2DP3D404IWG1-E/36(F5)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780649800/Firmware__V5.8.0_260402_S3000712887.zip) | 2026-03-26 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780649800/Firmware__V5.8.0_260402_S3000712887.zip) | — |

</details>


<details>
<summary><h2>DS-2DP7A410MCG1-LEF/416 - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.9.60 | Applied to: [DS-2DP7A410MCG1-LEF/416](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780617965/Firmware__V5.9.60_260408_S3000715280.zip), [DS-2DP7A410MCG1-LEF/416(F0)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780617965/Firmware__V5.9.60_260408_S3000715280.zip), [DS-2DP7A410MCG1-LEF/624](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780617965/Firmware__V5.9.60_260408_S3000715280.zip), [DS-2DP7A410MCG1-LEF/624(F0)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780617965/Firmware__V5.9.60_260408_S3000715280.zip), [DS-2DP7A410MCG1-LEF/832](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780617965/Firmware__V5.9.60_260408_S3000715280.zip), [DS-2DP7A410MCG1-LEF/832(F0)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780617965/Firmware__V5.9.60_260408_S3000715280.zip), [DS-2DP7A420MCG1-LEF/416](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780617965/Firmware__V5.9.60_260408_S3000715280.zip), [DS-2DP7A420MCG1-LEF/416(F0)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780617965/Firmware__V5.9.60_260408_S3000715280.zip) | 2026-04-08 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780617965/Firmware__V5.9.60_260408_S3000715280.zip) | — |

</details>


<details>
<summary><h2>DS-2DP7D825IXG1-LEF(Y)/432 - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.9.71 | Applied to: [DS-2DP7D825IXG1-LEF(Y)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.9.71_260331_S3000713857.zip)/432, [DS-2DP7D825IXG1-LEFY/432(F0)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.9.71_260331_S3000713857.zip), [DS-2DP7D825IXG1-LEF/432(F0)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.9.71_260331_S3000713857.zip), [[DS-2DP7D836IXG1-LEF(Y)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.9.71_260331_S3000713857.zip)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.9.71_260331_S3000713857.zip)/432, [DS-2DP7D836IXG1-LEF/432(F0)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.9.71_260331_S3000713857.zip), [DS-2DP7D836IXG1-LEFY/432(F0)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.9.71_260331_S3000713857.zip), DS-2DP7D836IXG1-LEF(Y)/432(IR), [DS-2DP7D836IXG1-LEF/432(IR)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.9.71_260331_S3000713857.zip)(F0) | 2026-03-26 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.9.71_260331_S3000713857.zip) | — |

</details>


<details>
<summary><h2>DS-2DP8A440IXG1-LEF/416(F0) - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.9.51 | Applied to: [[DS-2DP8A440IXG1-LEF/416(F0)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780649800/Firmware__V5.9.51_260403_S3000712992.zip)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780649800/Firmware__V5.9.51_260403_S3000712992.zip), DS-2DP8A440IXG1-LEF/416(F0)(B), [[DS-2DP8A440IXG1-LEF/624(F0)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780649800/Firmware__V5.9.51_260403_S3000712992.zip)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780649800/Firmware__V5.9.51_260403_S3000712992.zip), DS-2DP8A440IXG1-LEF/624(F0)(B), [[DS-2DP8A440IXG1-LEF/832(F0)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780649800/Firmware__V5.9.51_260403_S3000712992.zip)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780649800/Firmware__V5.9.51_260403_S3000712992.zip), DS-2DP8A440IXG1-LEF/832(F0)(B), [DS-2DP8A440IXG1-LEWF/416(F0)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780649800/Firmware__V5.9.51_260403_S3000712992.zip), [DS-2DP8A440IXG1-LEWF/624(F0)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780649800/Firmware__V5.9.51_260403_S3000712992.zip) | 2026-04-03 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780649800/Firmware__V5.9.51_260403_S3000712992.zip) | — |

</details>


<details>
<summary><h2>DS-2DT5432MWG-T (PA) - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.63 | Applied to: [DS-2DT5432MWG-T](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780043044/Firmware__V5.7.63_251106_S3000684477.zip) (PA), [DS-2DT5432MWG-T(PA)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780043044/Firmware__V5.7.63_251106_S3000684477.zip) | 2026-04-09 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780043044/Firmware__V5.7.63_251106_S3000684477.zip) | — |

</details>


<details>
<summary><h2>DS-2DT5432MWG-T/4G (PA) - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.63 | Applied to: [DS-2DT5432MWG-T/4G](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780043044/Firmware__V5.7.63_251106_S3000684477.zip) (PA), [DS-2DT5432MWG-T/4G(PA)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780043044/Firmware__V5.7.63_251106_S3000684477.zip) | 2026-04-02 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780043044/Firmware__V5.7.63_251106_S3000684477.zip) | — |

</details>


<details>
<summary><h2>DS-2DT8C442MXG-ELWT - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.9.72 | Applied to: [DS-2DT8C442MXG-ELWT](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779474355/Firmware__V5.9.72_260326_S3000719694.zip), [DS-2DT8C842MXG-ELWT](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779474355/Firmware__V5.9.72_260326_S3000719694.zip) | 2026-03-26 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779474355/Firmware__V5.9.72_260326_S3000719694.zip) | — |

</details>


<details>
<summary><h2>DS-2DY5225IX-AE(T5) - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.2 | Applied to: [DS-2DY5225IX-AE(T5)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.8.20_260330_S3000711486.zip), [DS-2DY5225IX-DM(T5)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.8.20_260330_S3000711486.zip), [DS-2DY5425IXG-E](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.8.20_260330_S3000711486.zip), [DS-2DY5432IXG-E](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.8.20_260330_S3000711486.zip), [DS-2DY5432IXG-M](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.8.20_260330_S3000711486.zip), [DS-2DY5440IXG-E](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.8.20_260330_S3000711486.zip) | 2026-04-08 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.8.20_260330_S3000711486.zip) | — |

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
| 5.8.2 | Applied to: [DS-2DY7432IXG-XY](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.8.20_260330_S3000711486.zip), [[[DS-2DY7436IXG-CXLWF(316L)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.8.20_260330_S3000711486.zip)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.8.20_260330_S3000711486.zip)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.8.20_260330_S3000711486.zip), DS-2DY7436IXG-CXLWF(316L)5M, DS-2DY7436IXG-CXLWF(316L)10M, [[[DS-2DY7845IXG-CXLWF(316L)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.8.20_260330_S3000711486.zip)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.8.20_260330_S3000711486.zip)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.8.20_260330_S3000711486.zip), DS-2DY7845IXG-CXLWF(316L)10M, DS-2DY7845IXG-CXLWF(316L)5M, [DS-2DY9236I-CWX(T5/316L)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.8.20_260330_S3000711486.zip) | 2026-04-08 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.8.20_260330_S3000711486.zip) | — |

</details>


<details>
<summary><h2>DS-2DY9C260LXG-LWY/12 - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.2 | Applied to: [DS-2DY9C260LXG-LWY/12](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.8.2_260331_S3000713832.zip), [DS-2DY9C260LXG-LWY/12(F2)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.8.2_260331_S3000713832.zip), [DS-2DY9C280LXG-LWY/12](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.8.2_260331_S3000713832.zip), [DS-2DY9C280LXG-LWY/12(F2)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.8.2_260331_S3000713832.zip), [DS-2DY9C440IXG-LWY/14](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.8.2_260331_S3000713832.zip), [DS-2DY9C440IXG-LWY/14(F1)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.8.2_260331_S3000713832.zip), [DS-2DY9C460LXG-LWY/14](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.8.2_260331_S3000713832.zip), [DS-2DY9C460LXG-LWY/14(F2)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.8.2_260331_S3000713832.zip) | 2026-03-31 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.8.2_260331_S3000713832.zip) | — |

</details>


<details>
<summary><h2>DS-2DYH2A0IXS-D(T2) - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.820 | Applied to: [DS-2DYH2A0IXS-D(T2)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780649800/Firmware__V5.5.820_260402_S3000712894.zip) | 2026-04-02 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780649800/Firmware__V5.5.820_260402_S3000712894.zip) | — |

</details>


<details>
<summary><h2>DS-2SE2C200MWG-E/12 - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.4 | Applied to: [DS-2SE2C200MWG-E/12](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.8.41_260401_S3000712568.zip), [DS-2SE2C200MWG-E/12(2.8/8MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.8.41_260401_S3000712568.zip), [DS-2SE2C400MWG-E/14](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.8.41_260401_S3000712568.zip), [DS-2SE2C400MWG-E/14(2.8/8MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.8.41_260401_S3000712568.zip) | 2026-03-25 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.8.41_260401_S3000712568.zip) | — |

</details>


<details>
<summary><h2>DS-2SE3C204MWG-4G/12 - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.11 | Applied to: [DS-2SE3C204MWG-4G/12](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780599961/Firmware__V5.8.110_260421_S3000718008.zip), [DS-2SE3C204MWG-4G/12(2.8MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780599961/Firmware__V5.8.110_260421_S3000718008.zip)(EU), [DS-2SE3C204MWG-E/12](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780599961/Firmware__V5.8.110_260421_S3000718008.zip), [DS-2SE3C204MWG-E/12(2.8MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780599961/Firmware__V5.8.110_260421_S3000718008.zip), [DS-2SE3C210MWG-E/12](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780599961/Firmware__V5.8.110_260421_S3000718008.zip), [DS-2SE3C210MWG-E/12(2.8MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780599961/Firmware__V5.8.110_260421_S3000718008.zip), [DS-2SE3C404MWG-4G/14](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780599961/Firmware__V5.8.110_260421_S3000718008.zip), [DS-2SE3C404MWG-4G/14(2.8MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780599961/Firmware__V5.8.110_260421_S3000718008.zip)(EU) | 2026-03-25 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780599961/Firmware__V5.8.110_260421_S3000718008.zip) | — |

</details>


<details>
<summary><h2>DS-2SE4C225MWG-E/26(F0) - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.2 | Applied to: [DS-2SE4C225MWG-E/26(F0)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.8.20_260330_S3000711486.zip) | 2026-03-25 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.8.20_260330_S3000711486.zip) | — |

</details>


<details>
<summary><h2>DS-2SE7C425MWG-EB/26(F0) - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.2 | Applied to: [DS-2SE7C425MWG-EB/26(F0)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.8.20_260330_S3000711486.zip), [DS-2SE7C432MWG-EB/26(F0)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.8.20_260330_S3000711486.zip) | 2026-03-24 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.8.20_260330_S3000711486.zip) | — |

</details>


<details>
<summary><h2>DS-2SE7C432IWG-4G/14(F0) - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.4 | Applied to: [[[DS-2SE7C432IWG-4G/14(F0)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.8.41_260401_S3000712568.zip)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.8.41_260401_S3000712568.zip)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.8.41_260401_S3000712568.zip), DS-2SE7C432IWG-4G/14(F0)(LA), DS-2SE7C432IWG-4G/14(F0)(JP) | 2026-04-07 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.8.41_260401_S3000712568.zip) | — |

</details>


<details>
<summary><h2>DS-2SF7C420MXG0-EL(W)(Y)/2C - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.9.1 | Applied to: [DS-2SF7C420MXG0-EL(W)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780683636/Firmware__V5.9.14_260401_S3000712572.zip)(Y)/2C, [DS-2SF7C420MXG0-ELWY/2C(F0)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780683636/Firmware__V5.9.14_260401_S3000712572.zip), [DS-2SF7C420MXG0-ELW/2C(F0)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780683636/Firmware__V5.9.14_260401_S3000712572.zip), [DS-2SF7C420MXG0-EL/2C(F0)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780683636/Firmware__V5.9.14_260401_S3000712572.zip), [DS-2SF7C420MXG0-ELY/2C(F0)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780683636/Firmware__V5.9.14_260401_S3000712572.zip) | 2026-04-02 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780683636/Firmware__V5.9.14_260401_S3000712572.zip) | — |

</details>


<details>
<summary><h2>DS-2SF8C425MXG-ELW/26 - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.20 | Applied to: [DS-2SF8C425MXG-ELW/26](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.8.20_260330_S3000711486.zip), [DS-2SF8C425MXG-ELW/26(F0)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.8.20_260330_S3000711486.zip), [DS-2SF8C425MXG-EL/26(F0)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.8.20_260330_S3000711486.zip), [DS-2SF8C442MXG-ELW/26](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.8.20_260330_S3000711486.zip), [DS-2SF8C442MXG-ELW/26(F0)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.8.20_260330_S3000711486.zip), [DS-2SF8C442MXG-EL/26(F0)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.8.20_260330_S3000711486.zip) | 2026-03-30 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.8.20_260330_S3000711486.zip) | — |

</details>


<details>
<summary><h2>DS-2SF8C432MXG-WD/14(F1) - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.63 | Applied to: [DS-2SF8C432MXG-WD/14(F1)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780043044/Firmware__V5.7.63_251106_S3000684477.zip), [DS-2SF8C432MXG-WD/4G/14(F1)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780043044/Firmware__V5.7.63_251106_S3000684477.zip) | 2026-03-25 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780043044/Firmware__V5.7.63_251106_S3000684477.zip) | — |

</details>


<details>
<summary><h2>DS-2SF8C442MXS-DLW(14F1)(P3) - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.1 | Applied to: [DS-2SF8C442MXS-DLW(14F1)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.8.1_260330_S3000711487.zip)(P3) | 2026-05-06 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.8.1_260330_S3000711487.zip) | — |

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
| 5.5.348 | Applied to: [DS-2TD2568T-15-G0-T1Y](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779753206/Firmware__V5.5.348_260410_S3000714869.zip) | 2026-04-27 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779753206/Firmware__V5.5.348_260410_S3000714869.zip) | 1.1 Issues fixes： 1) Fixed known software issues. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202605/releasenote%5CGeneral_Firmware_Update_Release_notes.pdf) |

</details>


<details>
<summary><h2>DS-2TD2568T-15/G0/T1Y - THERMAL_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.348 | Applied to: [DS-2TD2568T-15/G0/T1Y](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779753206/Firmware__V5.5.348_260410_S3000714869.zip), [DS-2TD2568T-5/G0/T1Y](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779753206/Firmware__V5.5.348_260410_S3000714869.zip), HM-TD1218-2/G0/T1A, HM-TD1218-3/G0/T1A, HM-TD1218-7/G0/T1A, HM-TD2618-10/G0/T1A, HM-TD2618-3/G0/T1A, HM-TD2618-7/G0/T1A | 2026-04-27 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779753206/Firmware__V5.5.348_260410_S3000714869.zip) | 1.1 Issues fixes： 1) Fixed known software issues. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202605/releasenote%5CGeneral_Firmware_Update_Release_notes.pdf) |

</details>


<details>
<summary><h2>DS-2TD2568T-5-G0-T1Y - THERMAL_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.348 | Applied to: [DS-2TD2568T-5-G0-T1Y](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779753206/Firmware__V5.5.348_260410_S3000714869.zip) | 2026-04-27 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779753206/Firmware__V5.5.348_260410_S3000714869.zip) | 1.1 Issues fixes： 1) Fixed known software issues. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202605/releasenote%5CGeneral_Firmware_Update_Release_notes.pdf) |

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
<summary><h2>DS-2TD4137-25/WY - THERMAL_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.139 | Applied to: [DS-2TD4137-25/WY](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780531020/Firmware__V5.5.139_260409_S3000714189.zip), [DS-2TD4137-25/WY(B)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780531020/Firmware__V5.5.139_260409_S3000714189.zip), [DS-2TD4137-50/WY](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780531020/Firmware__V5.5.139_260409_S3000714189.zip), [DS-2TD4137-50/WY(B)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780531020/Firmware__V5.5.139_260409_S3000714189.zip), [DS-2TD4137T-25/W](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780531020/Firmware__V5.5.139_260409_S3000714189.zip), [DS-2TD4137T-25/W(B)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780531020/Firmware__V5.5.139_260409_S3000714189.zip), [DS-2TD4137T-9/W](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780531020/Firmware__V5.5.139_260409_S3000714189.zip), [DS-2TD4137T-9/W(B)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780531020/Firmware__V5.5.139_260409_S3000714189.zip) | 2026-04-09 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780531020/Firmware__V5.5.139_260409_S3000714189.zip) | 1.1 Issues fixes： 1) Fixed known software issues. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202605/releasenote%5CGeneral_Firmware_Update_Release_notes.pdf) |

</details>


<details>
<summary><h2>DS-2TD4228-10/S2 - THERMAL_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.137 | Applied to: [DS-2TD4228-10/S2](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780531020/Firmware__V5.5.137_260415_S3000717670.zip), [DS-2TD4228-7/S2](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780531020/Firmware__V5.5.137_260415_S3000717670.zip), [DS-2TD4228T-10/S2](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780531020/Firmware__V5.5.137_260415_S3000717670.zip), [DS-2TD4228T-7/S2](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780531020/Firmware__V5.5.137_260415_S3000717670.zip), [DS-2TD4238-10/S2](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780531020/Firmware__V5.5.137_260415_S3000717670.zip), [DS-2TD4238-10/S2(B)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780531020/Firmware__V5.5.137_260415_S3000717670.zip), [DS-2TD4238-25/S2](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780531020/Firmware__V5.5.137_260415_S3000717670.zip), [DS-2TD4238-25/S2(B)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780531020/Firmware__V5.5.137_260415_S3000717670.zip) | 2026-04-15 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780531020/Firmware__V5.5.137_260415_S3000717670.zip) | 1.1 Issues fixes： 1) Fixed known software issues. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202605/releasenote%5CGeneral_Firmware_Update_Release_notes.pdf) |

</details>


<details>
<summary><h2>DS-2TD4228-10/W - THERMAL_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.109 | Applied to: [DS-2TD4228-10/W](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779264543/Firmware__V5.5.109_260410_S3000716161.zip) | 2026-04-10 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779264543/Firmware__V5.5.109_260410_S3000716161.zip) | 1.1 Issues fixes： 1) Fixed known software issues. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202605/releasenote%5CGeneral_Firmware_Update_Release_notes.pdf) |

</details>


<details>
<summary><h2>DS-2TD4538-25A4/W - THERMAL_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.141 | Applied to: [DS-2TD4538-25A4/W](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780531020/Firmware__V5.5.141_260512_S3000722086.zip), [DS-2TD4538-35A4/W](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780531020/Firmware__V5.5.141_260512_S3000722086.zip), [DS-2TD4568-25A4/W](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780531020/Firmware__V5.5.141_260512_S3000722086.zip), [DS-2TD4568-35A4/W](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780531020/Firmware__V5.5.141_260512_S3000722086.zip), [DS-2TD4638-25A4/W](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780531020/Firmware__V5.5.141_260512_S3000722086.zip), [DS-2TD4638-35A4/W](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780531020/Firmware__V5.5.141_260512_S3000722086.zip), [DS-2TD4667T-25A4/W](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780531020/Firmware__V5.5.141_260512_S3000722086.zip), [DS-2TD4668-25A4/W](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780531020/Firmware__V5.5.141_260512_S3000722086.zip) | 2026-05-12 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780531020/Firmware__V5.5.141_260512_S3000722086.zip) | 1.1 Issues fixes： 1) Fixed known software issues. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202605/releasenote%5CGeneral_Firmware_Update_Release_notes.pdf) |

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
<summary><h2>DS-2XC3146G0H-LI(S)(U) (PA) - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.63 | Applied to: [DS-2XC3146G0H-LI(S)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780043044/Firmware__V5.7.63_251106_S3000684477.zip)(U) (PA), [[DS-2XC3146G0H-LIS(PA)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780043044/Firmware__V5.7.63_251106_S3000684477.zip)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780043044/Firmware__V5.7.63_251106_S3000684477.zip)(2.8MM), DS-2XC3146G0H-LIS(PA)(4MM), [[DS-2XC3146G0H-LISU(PA)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780043044/Firmware__V5.7.63_251106_S3000684477.zip)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780043044/Firmware__V5.7.63_251106_S3000684477.zip)(2.8MM), DS-2XC3146G0H-LISU(PA)(4MM), [DS-2XC3146G0H-LISU/SL](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780043044/Firmware__V5.7.63_251106_S3000684477.zip) (PA), [[DS-2XC3146G0H-LISU/SL(PA)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780043044/Firmware__V5.7.63_251106_S3000684477.zip)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780043044/Firmware__V5.7.63_251106_S3000684477.zip)(2.8MM), DS-2XC3146G0H-LISU/SL(PA)(4MM) | 2026-03-24 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780043044/Firmware__V5.7.63_251106_S3000684477.zip) | — |

</details>


<details>
<summary><h2>DS-2XC6046G0-LIS(316L) - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.3 | Applied to: [[[DS-2XC6046G0-LIS(316L)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780649800/Firmware__V5.8.3_260402_S3000712976.zip)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780649800/Firmware__V5.8.3_260402_S3000712976.zip)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780649800/Firmware__V5.8.3_260402_S3000712976.zip), DS-2XC6046G0-LIS(316L)(2.8MM), DS-2XC6046G0-LIS(316L)(4MM) | 2026-04-16 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780649800/Firmware__V5.8.3_260402_S3000712976.zip) | — |

</details>


<details>
<summary><h2>DS-2XC6142FWD-IS(C) - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.63 | Applied to: [DS-2XC6142FWD-IS(C)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780043044/Firmware__V5.7.63_251106_S3000684477.zip), [DS-2XC6142FWD-IS(2.8MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780043044/Firmware__V5.7.63_251106_S3000684477.zip)(C), [DS-2XC6142FWD-IS(4MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780043044/Firmware__V5.7.63_251106_S3000684477.zip)(C), [DS-2XC6142FWD-IS(6MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780043044/Firmware__V5.7.63_251106_S3000684477.zip)(C), [DS-2XC6244G0-L](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780043044/Firmware__V5.7.63_251106_S3000684477.zip), [DS-2XC6244G0-L(2.8-12MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780043044/Firmware__V5.7.63_251106_S3000684477.zip), [DS-2XC6245G0-L](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780043044/Firmware__V5.7.63_251106_S3000684477.zip), [DS-2XC6245G0-L(2.8-12MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780043044/Firmware__V5.7.63_251106_S3000684477.zip) | 2026-03-25 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780043044/Firmware__V5.7.63_251106_S3000684477.zip) | — |

</details>


<details>
<summary><h2>DS-2XC6625G0(D) - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.63 | Applied to: [DS-2XC6625G0(D)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780043044/Firmware__V5.7.63_251106_S3000684477.zip), [DS-2XC6625G0-IZHRS(2.8-12MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780043044/Firmware__V5.7.63_251106_S3000684477.zip)(D), [DS-2XC6625G0-IZHRS(8-32MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780043044/Firmware__V5.7.63_251106_S3000684477.zip)(D), [DS-2XC6645G0(D)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780043044/Firmware__V5.7.63_251106_S3000684477.zip), [DS-2XC6645G0-IZHRS(2.8-12MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780043044/Firmware__V5.7.63_251106_S3000684477.zip)(D), [DS-2XC6645G0-IZHRS(8-32MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780043044/Firmware__V5.7.63_251106_S3000684477.zip)(D), [DS-2XC6685G0(D)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780043044/Firmware__V5.7.63_251106_S3000684477.zip), [DS-2XC6685G0-IZHRS(2.8-12MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780043044/Firmware__V5.7.63_251106_S3000684477.zip)(D) | 2025-11-06 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780043044/Firmware__V5.7.63_251106_S3000684477.zip) | Algorithm optimization and updates. 2. Fix some bugs. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CV5.7.63_251106_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2XM6825G1/C-IV(S)(M)(/ND) - IPC_V4 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 4.2.2 | Applied to: [DS-2XM6825G1/C-IV(S)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780531020/Firmware__V4.2.2_251022_S3000681518.zip)(M)(/ND), [DS-2XM6825G1/C-IMS(2MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780531020/Firmware__V4.2.2_251022_S3000681518.zip), [DS-2XM6825G1/C-IS(2MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780531020/Firmware__V4.2.2_251022_S3000681518.zip) | 2025-10-22 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780531020/Firmware__V4.2.2_251022_S3000681518.zip) | Support the counting of special vehicles (bicycle, baby stroller, wheelchair). · Support device cloning. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5C【Release_Note】Mobile_People_Counting_IPC_V4.2.2.pdf) |

</details>


<details>
<summary><h2>DS-2XS6A46G1-IZS/4G - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.72 | Applied to: [DS-2XS6A46G1-IZS/4G](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779388610/Firmware__V5.7.72_260330_S3000714332.zip), [DS-2XS6A46G1-IZS/4G(8-32MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779388610/Firmware__V5.7.72_260330_S3000714332.zip), [DS-2XS6A46G1-IZS/4G(2.8-12MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779388610/Firmware__V5.7.72_260330_S3000714332.zip), [DS-2XS6A46G1-LIZS/4G](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779388610/Firmware__V5.7.72_260330_S3000714332.zip), [DS-2XS6A46G1-LIZS/4G(2.8-12MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779388610/Firmware__V5.7.72_260330_S3000714332.zip), [[DS-2XS6A46G1-LIZS/4G(8-32MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779388610/Firmware__V5.7.72_260330_S3000714332.zip)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779388610/Firmware__V5.7.72_260330_S3000714332.zip), DS-2XS6A46G1-LIZS/4G(8-32MM)(LA), [DS-2XS6A47G1-LS/4G](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779388610/Firmware__V5.7.72_260330_S3000714332.zip) | 2026-03-30 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779388610/Firmware__V5.7.72_260330_S3000714332.zip) | Support diagnose logs to obtain temperature information. · Modified Features · 1. The camera’s factory default set tings include lo w power mode and 24 -hour sleep; and · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202605/releasenote%5CSolar-powered_Security_Camera_V5.7.72_260330_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2XS6A46G1/P-IZS/4G - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.72 | Applied to: [DS-2XS6A46G1/P-IZS/4G](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779352270/Firmware__V5.7.72_260330_S3000714333.zip), [DS-2XS6A46G1/P-IZS/4G(2.8-12MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779352270/Firmware__V5.7.72_260330_S3000714333.zip), [DS-2XS6A46G1/P-IZS/4G(8-32MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779352270/Firmware__V5.7.72_260330_S3000714333.zip) | 2026-03-30 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779352270/Firmware__V5.7.72_260330_S3000714333.zip) | Support diagnose logs to obtain temperature information. · Modified Features · 1. The camera’s factory default set tings include lo w power mode and 24 -hour sleep; and · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202605/releasenote%5CSolar-powered_Security_Camera_V5.7.72_260330_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2XV6646G0-LIZH(R)S - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.6 | Applied to: [DS-2XV6646G0-LIZH(R)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.8.6_260331_S3000713808.zip)S, [DS-2XV6646G0-LIZHRS(2.8-12MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.8.6_260331_S3000713808.zip), [DS-2XV6646G0-LIZHRS(8-32MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.8.6_260331_S3000713808.zip), [DS-2XV6686G0-LIZH(R)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.8.6_260331_S3000713808.zip)S, [DS-2XV6686G0-LIZHRS(2.8-12MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.8.6_260331_S3000713808.zip), [DS-2XV6686G0-LIZHRS(8-32MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.8.6_260331_S3000713808.zip), [DS-2XV6A46G0-LIZH(R)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.8.6_260331_S3000713808.zip)SY(316L), [DS-2XV6A46G0-LIZHRSY(316L)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.8.6_260331_S3000713808.zip)(2.8-12)O-STD | 2026-03-31 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.8.6_260331_S3000713808.zip) | — |

</details>


<details>
<summary><h2>DS-3E1506P-EI/M-4P1T1F - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 3.4.2 | Applied to: [DS-3E1506P-EI/M-4P1T1F](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779216345/Firmware__V3.4.2_260407_S3000718999.zip) | 2026-04-07 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779216345/Firmware__V3.4.2_260407_S3000718999.zip) | — |

</details>


<details>
<summary><h2>DS-3E1510P-SI-8P2F - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 3.3.3 | Applied to: [DS-3E1510P-SI-8P2F](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779758234/Firmware__V3.3.3_260119_S3000703088.zip), [DS-3E1512HP-SI-8P2T2F](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779758234/Firmware__V3.3.3_260119_S3000703088.zip), [DS-3E1518P-SI-16P2F](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779758234/Firmware__V3.3.3_260119_S3000703088.zip), [DS-3E1520HP-SI-16P2T2F](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779758234/Firmware__V3.3.3_260119_S3000703088.zip), [DS-3E1524-SI-16F8T](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779758234/Firmware__V3.3.3_260119_S3000703088.zip), [DS-3E1526P-SI-24P2F](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779758234/Firmware__V3.3.3_260119_S3000703088.zip), [DS-3E1528-SI-24T4F](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779758234/Firmware__V3.3.3_260119_S3000703088.zip), [DS-3E1528HP-SI-24P2T2F](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779758234/Firmware__V3.3.3_260119_S3000703088.zip) | 2026-01-19 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779758234/Firmware__V3.3.3_260119_S3000703088.zip) | — |

</details>


<details>
<summary><h2>DS-3E1516-EI V2(O-STD) - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 3.3.0 | Applied to: [[[DS-3E1516-EI](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780081037/Firmware__V3.3.0_251027_S3000681148.zip)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780081037/Firmware__V3.3.0_251027_S3000681148.zip)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780081037/Firmware__V3.3.0_251027_S3000681148.zip) V2(O-STD), DS-3E1516-EI V2, DS-3E1516-EI, [DS-3E1518P-EI](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780081037/Firmware__V3.3.0_251027_S3000681148.zip), [[DS-3E1518P-EI/M](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780081037/Firmware__V3.3.0_251027_S3000681148.zip)(O-STD)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780081037/Firmware__V3.3.0_251027_S3000681148.zip), DS-3E1518P-EI/M, [[DS-3E1524-EI](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780081037/Firmware__V3.3.0_251027_S3000681148.zip)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780081037/Firmware__V3.3.0_251027_S3000681148.zip) V2(O-STD), DS-3E1524-EI V2 | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780081037/Firmware__V3.3.0_251027_S3000681148.zip) | — |

</details>


<details>
<summary><h2>DS-3E1552-SI-48T4F - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 3.3.3 | Applied to: [DS-3E1552-SI-48T4F](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779758234/Firmware__V3.3.3_260119_S3000703087.zip), [DS-3E1552P-SI](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779758234/Firmware__V3.3.3_260119_S3000703087.zip) | 2026-01-19 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779758234/Firmware__V3.3.3_260119_S3000703087.zip) | — |

</details>


<details>
<summary><h2>DS-3E1710HP-EI - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 3.3.2 | Applied to: [DS-3E1710HP-EI](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780563030/Firmware__V3.3.2_260507_S3000721074.zip), [DS-3E1726HP-EI](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780563030/Firmware__V3.3.2_260507_S3000721074.zip) | 2025-10-31 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780563030/Firmware__V3.3.2_260507_S3000721074.zip) | — |

</details>


<details>
<summary><h2>DS-3E1710HP-SI-8P2X - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 3.3.6 | Applied to: [DS-3E1710HP-SI-8P2X](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779994076/Firmware__V3.3.6_251204_S3000692850.zip), [DS-3E1726HP-SI-24P2X](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779994076/Firmware__V3.3.6_251204_S3000692850.zip) | 2025-12-04 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779994076/Firmware__V3.3.6_251204_S3000692850.zip) | — |

</details>


<details>
<summary><h2>DS-3E2510-SI-8T2F - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 1.4.902 | Applied to: [DS-3E2510-SI-8T2F](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779754560/Firmware__V1.4.902_260324_S3000715220.zip), [DS-3E2510P-SI-8P2F](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779754560/Firmware__V1.4.902_260324_S3000715220.zip), [DS-3E2528-SI-24T4F](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779754560/Firmware__V1.4.902_260324_S3000715220.zip), [DS-3E2528P-SI-24P4F](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779754560/Firmware__V1.4.902_260324_S3000715220.zip) | 2026-03-24 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779754560/Firmware__V1.4.902_260324_S3000715220.zip) | — |

</details>


<details>
<summary><h2>DS-3E2728-SI-24T4X - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 1.4.902 | Applied to: [DS-3E2728-SI-24T4X](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779754560/Firmware__V1.4.902_260324_S3000715202.zip), [DS-3E2752-SI-48F4X](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779754560/Firmware__V1.4.902_260324_S3000715202.zip), [DS-3E2752-SI-48T4X](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779754560/Firmware__V1.4.902_260324_S3000715202.zip) | 2026-03-24 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779754560/Firmware__V1.4.902_260324_S3000715202.zip) | — |

</details>


<details>
<summary><h2>DS-3E3728-SI-24T4X - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 1.4.902 | Applied to: [DS-3E3728-SI-24T4X](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779754560/Firmware__V1.4.902_260324_S3000715219.zip), [DS-3E3752-SI-48F4X](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779754560/Firmware__V1.4.902_260324_S3000715219.zip), [DS-3E3752-SI-48T4X](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779754560/Firmware__V1.4.902_260324_S3000715219.zip) | 2026-03-24 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779754560/Firmware__V1.4.902_260324_S3000715219.zip) | — |

</details>


<details>
<summary><h2>DS-3E6600-16X-SA - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 1.5.300 | Applied to: [DS-3E6600-16X-SA](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779758234/Firmware__V1.5.300_260129_S3000703336.zip), [DS-3E6600-24F2X-SA](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779758234/Firmware__V1.5.300_260129_S3000703336.zip), [DS-3E6600-24T24F2X-SA](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779758234/Firmware__V1.5.300_260129_S3000703336.zip), [DS-3E6600-24T2X-SA](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779758234/Firmware__V1.5.300_260129_S3000703336.zip), [DS-3E6600-48F2X-SA](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779758234/Firmware__V1.5.300_260129_S3000703336.zip) | 2026-01-29 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779758234/Firmware__V1.5.300_260129_S3000703336.zip) | — |

</details>


<details>
<summary><h2>DS-3T1506HP-EI-UPS - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 3.3.2 | Applied to: [DS-3T1506HP-EI-UPS](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780563030/Firmware__V3.3.2_260507_S3000721074.zip) | 2026-05-07 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780563030/Firmware__V3.3.2_260507_S3000721074.zip) | — |

</details>


<details>
<summary><h2>DS-3WAP521-SI - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 1.1.6601 | Applied to: [DS-3WAP521-SI](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779821021/Firmware__V1.1.6601_251223_S3000698255.zip) | 2025-12-23 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779821021/Firmware__V1.1.6601_251223_S3000698255.zip) | — |

</details>


<details>
<summary><h2>DS-3WAP522-SI - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 1.1.6601 | Applied to: [DS-3WAP522-SI](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779821021/Firmware__V1.1.6601_251223_S3000698255.zip) | 2025-12-23 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779821021/Firmware__V1.1.6601_251223_S3000698255.zip) | — |

</details>


<details>
<summary><h2>DS-3WAP621E-SI - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 1.1.6601 | Applied to: [DS-3WAP621E-SI](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779821021/Firmware__V1.1.6601_251223_S3000698255.zip) | 2025-12-23 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779821021/Firmware__V1.1.6601_251223_S3000698255.zip) | — |

</details>


<details>
<summary><h2>DS-3WAP622E-SI - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 1.1.6601 | Applied to: [DS-3WAP622E-SI](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779821021/Firmware__V1.1.6601_251223_S3000698254.zip) | 2025-12-23 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779821021/Firmware__V1.1.6601_251223_S3000698254.zip) | — |

</details>


<details>
<summary><h2>DS-3WAP622G-SI - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 1.1.6601 | Applied to: [DS-3WAP622G-SI](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779821021/Firmware__V1.1.6601_251223_S3000698255.zip) | 2025-12-23 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779821021/Firmware__V1.1.6601_251223_S3000698255.zip) | — |

</details>


<details>
<summary><h2>DS-3WAP623E-SI - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 1.1.6601 | Applied to: [DS-3WAP623E-SI](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779821021/Firmware__V1.1.6601_251223_S3000698256.zip) | 2025-12-23 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779821021/Firmware__V1.1.6601_251223_S3000698256.zip) | — |

</details>


<details>
<summary><h2>DS-3WF02-5AC/D - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 1.3.0 | Applied to: [DS-3WF02-5AC/D](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780081037/Firmware__V1.3.0_251210_S3000691986.zip) | 2026-01-09 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780081037/Firmware__V1.3.0_251210_S3000691986.zip) | — |

</details>


<details>
<summary><h2>DS-3WF02C-5AC/O - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 1.3.0 | Applied to: [DS-3WF02C-5AC/O](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780081037/Firmware__V1.3.0_251210_S3000691986.zip) | 2026-01-09 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780081037/Firmware__V1.3.0_251210_S3000691986.zip) | — |

</details>


<details>
<summary><h2>DS-3WF0BC-2NT(B) - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 1.2.3 | Applied to: [DS-3WF0BC-2NT(B)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780043044/Firmware__V1.2.3_251114_S3000687333.zip) | 2025-11-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780043044/Firmware__V1.2.3_251114_S3000687333.zip) | — |

</details>


<details>
<summary><h2>DS-3WF0EC-2NT - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 1.3.0 | Applied to: [DS-3WF0EC-2NT](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780081037/Firmware__V1.3.0_251210_S3000691986.zip) | 2026-01-09 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780081037/Firmware__V1.3.0_251210_S3000691986.zip) | — |

</details>


<details>
<summary><h2>DS-3WF0EC-5ACT(B) - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 1.3.0 | Applied to: [DS-3WF0EC-5ACT(B)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780081037/Firmware__V1.3.0_251210_S3000691986.zip), [DS-3WF3000-EI-5AC/P](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780081037/Firmware__V1.3.0_251210_S3000691986.zip), [DS-3WF3000S-EI-5AC/P](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780081037/Firmware__V1.3.0_251210_S3000691986.zip) | 2026-01-09 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780081037/Firmware__V1.3.0_251210_S3000691986.zip) | — |

</details>


<details>
<summary><h2>DS-3WF1000-EI-2N - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 1.3.0 | Applied to: [DS-3WF1000-EI-2N](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780081037/Firmware__V1.3.0_251210_S3000691986.zip), [DS-3WF1000-EI-2N/P](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780081037/Firmware__V1.3.0_251210_S3000691986.zip), [DS-3WF1000S-EI-2N](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780081037/Firmware__V1.3.0_251210_S3000691986.zip), [DS-3WF1000S-EI-2N/P](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780081037/Firmware__V1.3.0_251210_S3000691986.zip), [DS-3WF500T-EI-2N/P](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780081037/Firmware__V1.3.0_251210_S3000691986.zip) | 2026-01-09 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780081037/Firmware__V1.3.0_251210_S3000691986.zip) | — |

</details>


<details>
<summary><h2>DS-3WF5000-EI-5ACG/3P - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 1.3.0 | Applied to: [DS-3WF5000-EI-5ACG/3P](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780081037/Firmware__V1.3.0_251210_S3000691986.zip), [DS-3WF5000S-EI-5ACG/3P](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780081037/Firmware__V1.3.0_251210_S3000691986.zip) | 2026-01-09 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780081037/Firmware__V1.3.0_251210_S3000691986.zip) | — |

</details>


<details>
<summary><h2>DS-3WF5000-SI-5ACG/2P - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 1.3.0 | Applied to: [DS-3WF5000-SI-5ACG/2P](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780081037/Firmware__V1.3.0_251210_S3000691986.zip), [DS-3WF5000S-SI-5ACG/2P](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780081037/Firmware__V1.3.0_251210_S3000691986.zip) | 2026-01-09 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780081037/Firmware__V1.3.0_251210_S3000691986.zip) | — |

</details>


<details>
<summary><h2>DS-3WFB-EI-5ACG - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 1.3.0 | Applied to: [DS-3WFB-EI-5ACG](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780081037/Firmware__V1.3.0_251210_S3000691986.zip) | 2026-01-09 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780081037/Firmware__V1.3.0_251210_S3000691986.zip) | — |

</details>


<details>
<summary><h2>DS-3WG105G-SI - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 1.0.6601 | Applied to: [DS-3WG105G-SI](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779821021/Firmware__V1.0.6601_251223_S3000698146.zip) | 2025-12-23 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779821021/Firmware__V1.0.6601_251223_S3000698146.zip) | — |

</details>


<details>
<summary><h2>DS-3WG105GP-SI - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 1.0.6601 | Applied to: [DS-3WG105GP-SI](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779821021/Firmware__V1.0.6601_251223_S3000698145.zip) | 2025-12-23 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779821021/Firmware__V1.0.6601_251223_S3000698145.zip) | — |

</details>


<details>
<summary><h2>DS-3WG210GP-SI - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 1.0.6601 | Applied to: [DS-3WG210GP-SI](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779821021/Firmware__V1.0.6601_251223_S3000698147.zip) | 2025-12-23 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779821021/Firmware__V1.0.6601_251223_S3000698147.zip) | — |

</details>


<details>
<summary><h2>DS-3WG507G-SI - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 1.0.6601 | Applied to: [DS-3WG507G-SI](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779821021/Firmware__V1.0.6601_251223_S3000698148.zip) | 2025-12-23 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779821021/Firmware__V1.0.6601_251223_S3000698148.zip) | — |

</details>


<details>
<summary><h2>DS-3WR12C-E - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 1.7.2 | Applied to: [DS-3WR12C-E](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780732335/Firmware__V1.7.2_260429_S3000724886.zip), [DS-3WR12C-H](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780732335/Firmware__V1.7.2_260429_S3000724886.zip), [DS-3WRM12C](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780732335/Firmware__V1.7.2_260429_S3000724886.zip), [DS-3WRM12C/2](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780732335/Firmware__V1.7.2_260429_S3000724886.zip), [DS-3WRM12C/3](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780732335/Firmware__V1.7.2_260429_S3000724886.zip) | 2026-04-29 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780732335/Firmware__V1.7.2_260429_S3000724886.zip) | — |

</details>


<details>
<summary><h2>DS-3WR12GC-E - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 1.7.2 | Applied to: [DS-3WR12GC-E](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780732335/Firmware__V1.7.2_260429_S3000724886.zip), [DS-3WR12GC-H](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780732335/Firmware__V1.7.2_260429_S3000724886.zip), [DS-3WRM12GC](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780732335/Firmware__V1.7.2_260429_S3000724886.zip), [DS-3WRM12GC/2](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780732335/Firmware__V1.7.2_260429_S3000724886.zip), [DS-3WRM12GC/3](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780732335/Firmware__V1.7.2_260429_S3000724886.zip) | 2026-04-29 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780732335/Firmware__V1.7.2_260429_S3000724886.zip) | — |

</details>


<details>
<summary><h2>DS-3WR18X - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 1.7.100 | Applied to: [DS-3WR18X](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779750762/Firmware__V1.7.100_260429_S3000720515.zip), [DS-3WR30X](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779750762/Firmware__V1.7.100_260429_S3000720515.zip), [DS-3WR30X-V](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779750762/Firmware__V1.7.100_260429_S3000720515.zip), [[DS-3WRM18X](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779750762/Firmware__V1.7.100_260429_S3000720515.zip)/1](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779750762/Firmware__V1.7.100_260429_S3000720515.zip), DS-3WRM18X, [DS-3WRM18X/2](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779750762/Firmware__V1.7.100_260429_S3000720515.zip), [DS-3WRM18X/3](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779750762/Firmware__V1.7.100_260429_S3000720515.zip), [DS-3WRM30X/1](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779750762/Firmware__V1.7.100_260429_S3000720515.zip) | 2026-04-29 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779750762/Firmware__V1.7.100_260429_S3000720515.zip) | — |

</details>


<details>
<summary><h2>DS-3WR3N - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 1.0.7 | Applied to: [DS-3WR3N](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779994076/Firmware__V1.0.7_251120_S3000689921.zip) | 2025-11-20 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779994076/Firmware__V1.0.7_251120_S3000689921.zip) | — |

</details>


<details>
<summary><h2>DS-3WRM12C - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 1.7.0 | Applied to: [DS-3WRM12C](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779474355/Firmware__V1.7.0_260326_S3000710449.zip), [DS-3WRM12C/2](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779474355/Firmware__V1.7.0_260326_S3000710449.zip), [DS-3WRM12C/3](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779474355/Firmware__V1.7.0_260326_S3000710449.zip) | 2026-03-26 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779474355/Firmware__V1.7.0_260326_S3000710449.zip) | — |

</details>


<details>
<summary><h2>DS-6920UDI-U(D) - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 1.0.0 | Applied to: [DS-6920UDI-U(D)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780617965/Firmware__V1.0.0_260417_S3000718427.zip), [DS-6924UDI-U(D)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780617965/Firmware__V1.0.0_260417_S3000718427.zip), [DS-6932UDI-U(D)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780617965/Firmware__V1.0.0_260417_S3000718427.zip) | 2026-04-17 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780617965/Firmware__V1.0.0_260417_S3000718427.zip) | — |

</details>


<details>
<summary><h2>DS-7104HGHI-M1 - DVR_V4 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 4.83.614 | Applied to: [DS-7104HGHI-M1](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779994076/Firmware_Asia_V4.83.614_251210_S3000691935.zip), [DS-7104HGHI-M1(C)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779994076/Firmware_Asia_V4.83.614_251210_S3000691935.zip) | 2025-12-10 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779994076/Firmware_Asia_V4.83.614_251210_S3000691935.zip) | Fix known issues Customer Impact and Recommended Action This new firmware upgrade is to improve product performance, and will take effect automatically after upgrading from previous versions. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CTurbo_HD_DVR_V4.83.614build251210_Release_Notes.pdf) |

</details>


<details>
<summary><h2>DS-7104HGHI-M1/T - DVR_V4 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 4.83.614 | Applied to: [DS-7104HGHI-M1/T](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779994076/Firmware_Asia_V4.83.614_251210_S3000691935.zip), [DS-7204HGHI-M1/T](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779994076/Firmware_Asia_V4.83.614_251210_S3000691935.zip) | 2025-12-10 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779994076/Firmware_Asia_V4.83.614_251210_S3000691935.zip) | Fix known issues Customer Impact and Recommended Action This new firmware upgrade is to improve product performance, and will take effect automatically after upgrading from previous versions. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CTurbo_HD_DVR_V4.83.614build251210_Release_Notes.pdf) |

</details>


<details>
<summary><h2>DS-7104NI-Q1 - NVR_V4 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 4.76.108 | Applied to: [DS-7104NI-Q1](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779821021/Firmware__V4.76.108_251219_S3000692754.zip), [DS-7104NI-Q1(D)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779821021/Firmware__V4.76.108_251219_S3000692754.zip), [DS-7104NI-Q1/4P](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779821021/Firmware__V4.76.108_251219_S3000692754.zip), [DS-7104NI-Q1/4P(D)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779821021/Firmware__V4.76.108_251219_S3000692754.zip), [DS-7108NI-Q1](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779821021/Firmware__V4.76.108_251219_S3000692754.zip), [DS-7108NI-Q1(D)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779821021/Firmware__V4.76.108_251219_S3000692754.zip), NK42E1H-1T(WD), [DS-J142I/NK42E1H-1T(WD)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779821021/Firmware__V4.76.108_251219_S3000692754.zip)(C) | 2025-12-19 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779821021/Firmware__V4.76.108_251219_S3000692754.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CEUI_NVR_V4.76.108_251219_ReleaseNote.pdf) |

</details>


<details>
<summary><h2>DS-7104NI-S2/WX - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 4.32.406 | Applied to: [DS-7104NI-S2/WX](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779750762/Firmware__V4.32.406_260427_S3000720971.zip), NKS4223WBTH, [DS-J142I](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779750762/Firmware__V4.32.406_260427_S3000720971.zip), NKS422WBH, NKS422WBPH, NKS4245WBTH, NKS424WBH, NKS424WBPH | 2026-04-27 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779750762/Firmware__V4.32.406_260427_S3000720971.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202605/releasenote%5CNVS_V4.32.406_20260427_ReleaseNote.pdf) |

</details>


<details>
<summary><h2>DS-7108HGHI-M1 - DVR_V4 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 4.83.614 | Applied to: [DS-7108HGHI-M1](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779994076/Firmware_Asia_V4.83.614_251210_S3000691935.zip), [DS-7108HGHI-M1(C)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779994076/Firmware_Asia_V4.83.614_251210_S3000691935.zip) | 2025-12-10 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779994076/Firmware_Asia_V4.83.614_251210_S3000691935.zip) | Fix known issues Customer Impact and Recommended Action This new firmware upgrade is to improve product performance, and will take effect automatically after upgrading from previous versions. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CTurbo_HD_DVR_V4.83.614build251210_Release_Notes.pdf) |

</details>


<details>
<summary><h2>DS-7108HGHI-M1/T - DVR_V4 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 4.83.614 | Applied to: [DS-7108HGHI-M1/T](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779994076/Firmware_Asia_V4.83.614_251210_S3000691935.zip), [DS-7208HGHI-M1/T](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779994076/Firmware_Asia_V4.83.614_251210_S3000691935.zip) | 2025-12-10 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779994076/Firmware_Asia_V4.83.614_251210_S3000691935.zip) | Fix known issues Customer Impact and Recommended Action This new firmware upgrade is to improve product performance, and will take effect automatically after upgrading from previous versions. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CTurbo_HD_DVR_V4.83.614build251210_Release_Notes.pdf) |

</details>


<details>
<summary><h2>DS-7116HGHI-M1 - DVR_V4 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 4.83.614 | Applied to: [DS-7116HGHI-M1](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779994076/Firmware_Asia_V4.83.614_251210_S3000691935.zip), [DS-7116HGHI-M1(E)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779994076/Firmware_Asia_V4.83.614_251210_S3000691935.zip), [DS-7116HGHI-M1(F)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779994076/Firmware_Asia_V4.83.614_251210_S3000691935.zip), [DS-7216HGHI-M1](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779994076/Firmware_Asia_V4.83.614_251210_S3000691935.zip), [DS-7216HGHI-M1(E)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779994076/Firmware_Asia_V4.83.614_251210_S3000691935.zip), [DS-7216HGHI-M1(F)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779994076/Firmware_Asia_V4.83.614_251210_S3000691935.zip) | 2025-12-10 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779994076/Firmware_Asia_V4.83.614_251210_S3000691935.zip) | Fix known issues Customer Impact and Recommended Action This new firmware upgrade is to improve product performance, and will take effect automatically after upgrading from previous versions. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CTurbo_HD_DVR_V4.83.614build251210_Release_Notes.pdf) |

</details>


<details>
<summary><h2>DS-7208HGHI-M1 - DVR_V4 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 4.83.613 | Applied to: [DS-7208HGHI-M1](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780081037/Firmware_Asia_V4.83.613_251028_S3000681702.zip), [DS-7208HGHI-M1(C)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780081037/Firmware_Asia_V4.83.613_251028_S3000681702.zip) | 2025-10-28 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780081037/Firmware_Asia_V4.83.613_251028_S3000681702.zip) | improve product performance, and will take effect automatically after upgrading from previous versions. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202511/releasenote%5CTurbo_HD_DVR_V4.83.613build251028_Release_Notes.pdf) |

</details>


<details>
<summary><h2>DS-7232HGHI-M2 - DVR_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 4.75.021 | Applied to: [DS-7232HGHI-M2](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779754560/Firmware_Asia_V4.75.021_260325_S3000714250.zip) | 2026-03-25 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779754560/Firmware_Asia_V4.75.021_260325_S3000714250.zip) | — |

</details>


<details>
<summary><h2>DS-7232HGHI-M2/T-2K - DVR_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 4.84.101 | Applied to: [DS-7232HGHI-M2/T-2K](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779956347/Firmware__V4.84.101_251212_S3000693705.zip) | 2026-05-18 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779956347/Firmware__V4.84.101_251212_S3000693705.zip) | — |

</details>


<details>
<summary><h2>DS-7232HGHI-M2/T-2K - DVR_V4 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 4.84.100 | Applied to: [DS-7232HGHI-M2/T-2K](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779324458/Firmware_Europe_V4.84.100_260425_S3000719711.zip) | 2026-04-25 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779324458/Firmware_Europe_V4.84.100_260425_S3000719711.zip) | improve product performance, and will take effect automatically after upgrading from previous versions. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202605/releasenote%5CTurbo_HD_DVR_V4.84.100build260425_Release_Notes.pdf) |

</details>


<details>
<summary><h2>DS-7604NI-Q1 - NVR_V4 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 4.83.107 | Applied to: [DS-7604NI-Q1](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779758234/Firmware__V4.83.107_260127_S3000700909.zip), [DS-7604NI-Q1(D)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779758234/Firmware__V4.83.107_260127_S3000700909.zip), [DS-7604NI-Q1(E)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779758234/Firmware__V4.83.107_260127_S3000700909.zip), [DS-7604NI-Q1/4P](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779758234/Firmware__V4.83.107_260127_S3000700909.zip), [DS-7604NI-Q1/4P(D)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779758234/Firmware__V4.83.107_260127_S3000700909.zip), [DS-7604NI-Q1/4P(E)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779758234/Firmware__V4.83.107_260127_S3000700909.zip), [DS-7608NI-Q1](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779758234/Firmware__V4.83.107_260127_S3000700909.zip), [DS-7608NI-Q1(D)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779758234/Firmware__V4.83.107_260127_S3000700909.zip) | 2026-01-27 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779758234/Firmware__V4.83.107_260127_S3000700909.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202604/releasenote%5CEUI_NVR_V4.83.107_260127_ReleaseNote.pdf) |

</details>


<details>
<summary><h2>DS-7604NI-Q1/W - NVR_V4 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 4.85.001 | Applied to: [DS-7604NI-Q1/W](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779956347/Firmware__V4.85.001_251211_S3000693149.zip), [DS-7608NI-Q1/W](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779956347/Firmware__V4.85.001_251211_S3000693149.zip), NK842WBH, [DS-J142I](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779956347/Firmware__V4.85.001_251211_S3000693149.zip), NK844WBH, NK844WDH | 2025-12-11 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779956347/Firmware__V4.85.001_251211_S3000693149.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CEUI_NVR_V4.85.001_251211_ReleaseNote.pdf) |

</details>


<details>
<summary><h2>DS-7604NXI-K1 - NVR_V4 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 4.73.110 | Applied to: [DS-7604NXI-K1](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779907479/Firmware__V4.73.110_251216_S3000692833.zip), [DS-7604NXI-K1(B)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779907479/Firmware__V4.73.110_251216_S3000692833.zip), [DS-7604NXI-K1/4P](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779907479/Firmware__V4.73.110_251216_S3000692833.zip), [DS-7604NXI-K1/4P(B)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779907479/Firmware__V4.73.110_251216_S3000692833.zip), [DS-7608NXI-K1](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779907479/Firmware__V4.73.110_251216_S3000692833.zip), [DS-7608NXI-K1(B)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779907479/Firmware__V4.73.110_251216_S3000692833.zip), [DS-7608NXI-K1/8P](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779907479/Firmware__V4.73.110_251216_S3000692833.zip), [DS-7608NXI-K1/8P(B)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779907479/Firmware__V4.73.110_251216_S3000692833.zip) | 2025-12-16 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779907479/Firmware__V4.73.110_251216_S3000692833.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CEUI_NVR_V4.73.110_251216_ReleaseNote.pdf) |

</details>


<details>
<summary><h2>DS-7604NXI-K1(D) - NVR_V4 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 4.84.101 | Applied to: [DS-7604NXI-K1(D)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779956347/Firmware__V4.84.101_251212_S3000693705.zip), [DS-7604NXI-K1/4P(D)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779956347/Firmware__V4.84.101_251212_S3000693705.zip), [DS-7608NXI-K1(D)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779956347/Firmware__V4.84.101_251212_S3000693705.zip), [DS-7608NXI-K1/8P(D)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779956347/Firmware__V4.84.101_251212_S3000693705.zip), [DS-7608NXI-K2(D)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779956347/Firmware__V4.84.101_251212_S3000693705.zip), [DS-7608NXI-K2/8P(D)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779956347/Firmware__V4.84.101_251212_S3000693705.zip), [DS-7616NXI-K1(D)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779956347/Firmware__V4.84.101_251212_S3000693705.zip), [DS-7616NXI-K2(D)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779956347/Firmware__V4.84.101_251212_S3000693705.zip) | 2025-12-12 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779956347/Firmware__V4.84.101_251212_S3000693705.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CEUI_NVR_V4.84.101_251212_ReleaseNote.pdf) |

</details>


<details>
<summary><h2>DS-7604NXI-K1(E) - NVR_V4 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 4.84.121 | Applied to: [DS-7604NXI-K1(E)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779782863/Firmware__V4.84.121_260107_S3000699228.zip), [DS-7604NXI-K1/4P(E)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779782863/Firmware__V4.84.121_260107_S3000699228.zip), [DS-7608NXI-K1(E)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779782863/Firmware__V4.84.121_260107_S3000699228.zip), [DS-7608NXI-K1/8P(E)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779782863/Firmware__V4.84.121_260107_S3000699228.zip), [DS-7608NXI-K2(E)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779782863/Firmware__V4.84.121_260107_S3000699228.zip), [DS-7608NXI-K2/8P(E)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779782863/Firmware__V4.84.121_260107_S3000699228.zip), [DS-7616NXI-K1(E)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779782863/Firmware__V4.84.121_260107_S3000699228.zip), [DS-7616NXI-K2(E)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779782863/Firmware__V4.84.121_260107_S3000699228.zip) | 2026-01-07 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779782863/Firmware__V4.84.121_260107_S3000699228.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202603/releasenote%5CEUI_NVR_V4.84.121_260107_ReleaseNote.pdf) |

</details>


<details>
<summary><h2>DS-7604NXI-K1/4P - NVR_V4 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 4.73.110 | Applied to: [DS-7604NXI-K1/4P](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779907479/Firmware__V4.73.109_250904_S3000672512.zip), [DS-7604NXI-K1/4P(B)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779907479/Firmware__V4.73.109_250904_S3000672512.zip) | 2025-12-16 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779907479/Firmware__V4.73.109_250904_S3000672512.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CEUI_NVR_V4.73.110_251216_ReleaseNote.pdf) |

</details>


<details>
<summary><h2>DS-7604NXI-K1/4P/VPRO - NVR_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 4.90.400 | Applied to: [DS-7604NXI-K1/4P/VPRO](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780531020/Firmware__V4.90.400_260525_S3000725563.zip), [DS-7604NXI-K1/VPRO](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780531020/Firmware__V4.90.400_260525_S3000725563.zip), [DS-7608NXI-K1/8P/VPRO](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780531020/Firmware__V4.90.400_260525_S3000725563.zip), [DS-7608NXI-K1/VPRO](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780531020/Firmware__V4.90.400_260525_S3000725563.zip), [DS-7608NXI-K2/8P/VPRO](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780531020/Firmware__V4.90.400_260525_S3000725563.zip), [DS-7608NXI-K2/VPRO](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780531020/Firmware__V4.90.400_260525_S3000725563.zip), [DS-7616NXI-K1/VPRO](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780531020/Firmware__V4.90.400_260525_S3000725563.zip), [DS-7616NXI-K2/16P/VPRO](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780531020/Firmware__V4.90.400_260525_S3000725563.zip) | 2026-05-25 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780531020/Firmware__V4.90.400_260525_S3000725563.zip) | — |
| 4.90.320 | Applied to: [DS-7604NXI-K1/4P/VPRO](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779758234/Firmware__V4.90.320_260313_S3000707041.zip), [DS-7604NXI-K1/VPRO](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779758234/Firmware__V4.90.320_260313_S3000707041.zip), [DS-7608NXI-K1/8P/VPRO](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779758234/Firmware__V4.90.320_260313_S3000707041.zip), [DS-7608NXI-K1/VPRO](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779758234/Firmware__V4.90.320_260313_S3000707041.zip), [DS-7608NXI-K2/8P/VPRO](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779758234/Firmware__V4.90.320_260313_S3000707041.zip), [DS-7608NXI-K2/VPRO](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779758234/Firmware__V4.90.320_260313_S3000707041.zip), [DS-7616NXI-K1/VPRO](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779758234/Firmware__V4.90.320_260313_S3000707041.zip), [DS-7616NXI-K2/16P/VPRO](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779758234/Firmware__V4.90.320_260313_S3000707041.zip) | 2026-03-13 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779758234/Firmware__V4.90.320_260313_S3000707041.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202605/releasenote%5CKvpro_V4.90.320_260313_ReleaseNote.pdf) |

</details>


<details>
<summary><h2>DS-7608NI-M2 - NVR_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.04.081 | Applied to: [DS-7608NI-M2](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779764110/Firmware__V5.04.081_260112_S3000698467.zip), [DS-7608NI-M2/8P](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779764110/Firmware__V5.04.081_260112_S3000698467.zip), [DS-7608NI-M2/8P(2T)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779764110/Firmware__V5.04.081_260112_S3000698467.zip), [DS-7608NI-M2/8P(4T)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779764110/Firmware__V5.04.081_260112_S3000698467.zip), [DS-7616NI-M2](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779764110/Firmware__V5.04.081_260112_S3000698467.zip), [DS-7616NI-M2/16P](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779764110/Firmware__V5.04.081_260112_S3000698467.zip), [DS-7616NI-M2/16P(4T)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779764110/Firmware__V5.04.081_260112_S3000698467.zip), [DS-7708NI-M4/8P](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779764110/Firmware__V5.04.081_260112_S3000698467.zip) | 2026-01-12 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779764110/Firmware__V5.04.081_260112_S3000698467.zip) | Modified functions · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202604/releasenote%5CK21B1_K22B1_V5.04.081_build260112_ReleaseNotes.pdf) |

</details>


<details>
<summary><h2>DS-96128NI-H16R - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.03.107 | Applied to: [DS-96128NI-H16R](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779782863/Firmware__V5.03.107_251231_S3000695780.zip), [DS-96128NI-H24R](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779782863/Firmware__V5.03.107_251231_S3000695780.zip), [DS-96128NI-H24R/LCD](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779782863/Firmware__V5.03.107_251231_S3000695780.zip), [DS-96128NI-H30R](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779782863/Firmware__V5.03.107_251231_S3000695780.zip), [DS-96128NI-H30R/LCD](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779782863/Firmware__V5.03.107_251231_S3000695780.zip), [DS-96256NI-H16R](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779782863/Firmware__V5.03.107_251231_S3000695780.zip), [DS-96256NI-H24R](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779782863/Firmware__V5.03.107_251231_S3000695780.zip), [DS-96256NI-H30R](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779782863/Firmware__V5.03.107_251231_S3000695780.zip) | 2025-12-31 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779782863/Firmware__V5.03.107_251231_S3000695780.zip) | Modified functions · Related product list: · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202604/releasenote%5CV5.03.107_X100_ReleaseNotes.pdf) |

</details>


<details>
<summary><h2>DS-96128NXI-S16 - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.03.416 | Applied to: [DS-96128NXI-S16](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779821021/Firmware__V5.03.416_251222_S3000695209.zip), [DS-96128NXI-S16(LCD)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779821021/Firmware__V5.03.416_251222_S3000695209.zip), [DS-96128NXI-S16R](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779821021/Firmware__V5.03.416_251222_S3000695209.zip), [DS-96128NXI-S16R(LCD)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779821021/Firmware__V5.03.416_251222_S3000695209.zip), [DS-96128NXI-S24R](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779821021/Firmware__V5.03.416_251222_S3000695209.zip), [DS-96128NXI-S24R(LCD)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779821021/Firmware__V5.03.416_251222_S3000695209.zip), [DS-96128NXI-S8](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779821021/Firmware__V5.03.416_251222_S3000695209.zip), [DS-96128NXI-S8R](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779821021/Firmware__V5.03.416_251222_S3000695209.zip) | 2025-12-22 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779821021/Firmware__V5.03.416_251222_S3000695209.zip) | Modified functions · Related product list: · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202604/releasenote%5CV5.03.416_H10_ReleaseNotes.pdf) |

</details>


<details>
<summary><h2>DS-C80N-01HI - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 1.2.0 | Applied to: [DS-C80N-01HI](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780531020/Firmware__V1.2.0_251022_S3000681572.zip), [DS-C80N-01HI/4K](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780531020/Firmware__V1.2.0_251022_S3000681572.zip), [DS-C80N-01HO](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780531020/Firmware__V1.2.0_251022_S3000681572.zip), [DS-C80N-01HO/4K](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780531020/Firmware__V1.2.0_251022_S3000681572.zip) | 2026-04-23 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780531020/Firmware__V1.2.0_251022_S3000681572.zip) | — |

</details>


<details>
<summary><h2>DS-E04NI-Q1/4P - NVR_V4 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 4.30.410 | Applied to: [DS-E04NI-Q1/4P](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779994076/Firmware_Asia_V4.30.410_251128_S3000692201.zip), [DS-E04NI-Q1/4P(SSD 1T)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779994076/Firmware_Asia_V4.30.410_251128_S3000692201.zip), [DS-E04NI-Q1/4P(SSD 2T)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779994076/Firmware_Asia_V4.30.410_251128_S3000692201.zip), [DS-E08NI-Q1](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779994076/Firmware_Asia_V4.30.410_251128_S3000692201.zip), [DS-E08NI-Q1(SSD 1T)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779994076/Firmware_Asia_V4.30.410_251128_S3000692201.zip), [DS-E08NI-Q1(SSD 2T)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779994076/Firmware_Asia_V4.30.410_251128_S3000692201.zip), [DS-E08NI-Q1/8P](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779994076/Firmware_Asia_V4.30.410_251128_S3000692201.zip), [DS-E08NI-Q1/8P(SSD 1T)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779994076/Firmware_Asia_V4.30.410_251128_S3000692201.zip) | 2025-11-28 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779994076/Firmware_Asia_V4.30.410_251128_S3000692201.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CeNVR_V4.30.410_251128_ReleaseNote.pdf) |

</details>


<details>
<summary><h2>DS-K1105EDB - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 1.0.2 | Applied to: [DS-K1105EDB](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779870290/Firmware__V2.1.0_251219_S3000692666.zip), [DS-K1105EDKB](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779870290/Firmware__V2.1.0_251219_S3000692666.zip), [DS-K1105EDKB-QR](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779870290/Firmware__V2.1.0_251219_S3000692666.zip), [DS-K1105EMB](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779870290/Firmware__V2.1.0_251219_S3000692666.zip), [DS-K1105EMKB](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779870290/Firmware__V2.1.0_251219_S3000692666.zip), [DS-K1105EMKB-QR](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779870290/Firmware__V2.1.0_251219_S3000692666.zip) | 2026-04-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779870290/Firmware__V2.1.0_251219_S3000692666.zip) | — |

</details>


<details>
<summary><h2>DS-K1T105AE - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 1.3.65 | Applied to: [DS-K1T105AE](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V1.3.65_260329_S3000711467.zip), [DS-K1T105AE(D-STD)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V1.3.65_260329_S3000711467.zip), [DS-K1T105AM](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V1.3.65_260329_S3000711467.zip), [DS-K1T105AM(D-STD)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V1.3.65_260329_S3000711467.zip), [DS-K1T201AEF](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V1.3.65_260329_S3000711467.zip) | 2026-03-29 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V1.3.65_260329_S3000711467.zip) | — |

</details>


<details>
<summary><h2>DS-K1T320EFWX - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 3.9.50 | Applied to: [DS-K1T320EFWX](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779758234/Firmware__V3.9.50_260130_S3000705230.zip), [DS-K1T320EFWX-B](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779758234/Firmware__V3.9.50_260130_S3000705230.zip), [DS-K1T320EFX](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779758234/Firmware__V3.9.50_260130_S3000705230.zip), [DS-K1T320EWX](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779758234/Firmware__V3.9.50_260130_S3000705230.zip), [DS-K1T320EX](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779758234/Firmware__V3.9.50_260130_S3000705230.zip), [DS-K1T320MFWX](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779758234/Firmware__V3.9.50_260130_S3000705230.zip), [DS-K1T320MFWX-B](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779758234/Firmware__V3.9.50_260130_S3000705230.zip), [DS-K1T320MFX](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779758234/Firmware__V3.9.50_260130_S3000705230.zip) | 2026-01-30 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779758234/Firmware__V3.9.50_260130_S3000705230.zip) | Fix bugs, enhance products quality to meet customers’ requirements. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202604/releasenote%5CDS-K1T320_Series_MinMoe_Terminal_V3.9.50_build260130_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-K1T321EFWX - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 3.9.50 | Applied to: [DS-K1T321EFWX](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779758234/Firmware__V3.9.50_260130_S3000705232.zip), [DS-K1T321EFWX-B](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779758234/Firmware__V3.9.50_260130_S3000705232.zip), [DS-K1T321EFX](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779758234/Firmware__V3.9.50_260130_S3000705232.zip), [DS-K1T321EWX](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779758234/Firmware__V3.9.50_260130_S3000705232.zip), [DS-K1T321EX](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779758234/Firmware__V3.9.50_260130_S3000705232.zip), [DS-K1T321MFWX](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779758234/Firmware__V3.9.50_260130_S3000705232.zip), [DS-K1T321MFWX-B](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779758234/Firmware__V3.9.50_260130_S3000705232.zip), [DS-K1T321MFX](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779758234/Firmware__V3.9.50_260130_S3000705232.zip) | 2026-01-30 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779758234/Firmware__V3.9.50_260130_S3000705232.zip) | improvement and will take effect automatically after the Date of Change. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202604/releasenote%5CDS-K1T321_Series_MinMoe_Terminal_V3.9.50_build260130_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-K1T341CM - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 3.3.200 | Applied to: [DS-K1T341CM](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779764110/Firmware__V3.3.200_260119_S3000711469.zip), [DS-K1T341CMF](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779764110/Firmware__V3.3.200_260119_S3000711469.zip), [DS-K1T341CMFW](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779764110/Firmware__V3.3.200_260119_S3000711469.zip), [DS-K1T341CMW](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779764110/Firmware__V3.3.200_260119_S3000711469.zip), [DS-KAS541](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779764110/Firmware__V3.3.200_260119_S3000711469.zip) | 2026-01-19 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779764110/Firmware__V3.3.200_260119_S3000711469.zip) | — |

</details>


<details>
<summary><h2>DS-K1T342DWX - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 4.48.40 | Applied to: [DS-K1T342DWX](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780732335/Firmware__V4.48.40_260522_S3000724280.zip), [DS-K1T342DWX-E1](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780732335/Firmware__V4.48.40_260522_S3000724280.zip), [DS-K1T342DX](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780732335/Firmware__V4.48.40_260522_S3000724280.zip), [DS-K1T342DX-E1](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780732335/Firmware__V4.48.40_260522_S3000724280.zip), [DS-K1T342EFWX](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780732335/Firmware__V4.48.40_260522_S3000724280.zip), [DS-K1T342EFWX-E1](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780732335/Firmware__V4.48.40_260522_S3000724280.zip), [DS-K1T342EWX](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780732335/Firmware__V4.48.40_260522_S3000724280.zip), [DS-K1T342EWX-E1](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780732335/Firmware__V4.48.40_260522_S3000724280.zip) | 2026-05-22 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780732335/Firmware__V4.48.40_260522_S3000724280.zip) | — |

</details>


<details>
<summary><h2>DS-K1T343EFWX - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 4.48.40 | Applied to: [DS-K1T343EFWX](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780732335/Firmware__V4.48.40_260522_S3000724280.zip), [DS-K1T343EFWX-B](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780732335/Firmware__V4.48.40_260522_S3000724280.zip), [DS-K1T343EWX](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780732335/Firmware__V4.48.40_260522_S3000724280.zip), [DS-K1T343MFWX](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780732335/Firmware__V4.48.40_260522_S3000724280.zip), [DS-K1T343MFWX-B](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780732335/Firmware__V4.48.40_260522_S3000724280.zip), [DS-K1T343MWX](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780732335/Firmware__V4.48.40_260522_S3000724280.zip) | 2026-05-22 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780732335/Firmware__V4.48.40_260522_S3000724280.zip) | — |

</details>


<details>
<summary><h2>DS-K1T343EFWX-B - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 4.48.40 | Applied to: [DS-K1T343EFWX-B](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780732335/Firmware__V4.48.40_260522_S3000724280.zip), [DS-K1T343MFWX-B](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780732335/Firmware__V4.48.40_260522_S3000724280.zip) | 2026-04-23 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780732335/Firmware__V4.48.40_260522_S3000724280.zip) | — |

</details>


<details>
<summary><h2>DS-K1T502DBFWX - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 1.20.0 | Applied to: [DS-K1T502DBFWX](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779994076/Firmware__V1.20.0_251204_S3000689789.zip), [DS-K1T502DBFWX-C](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779994076/Firmware__V1.20.0_251204_S3000689789.zip), [DS-K1T502DBWX](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779994076/Firmware__V1.20.0_251204_S3000689789.zip), [DS-K1T502DBWX-CQR](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779994076/Firmware__V1.20.0_251204_S3000689789.zip), [DS-K1T502DBWX-QR](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779994076/Firmware__V1.20.0_251204_S3000689789.zip) | 2025-12-04 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779994076/Firmware__V1.20.0_251204_S3000689789.zip) | Added 502POE model, added POE support, added lock 2 locally; · 502POE model supports dual -door control, supports authentication to open door 2, supports · intercom plus door 2 （reminder: only door1 support connecting security module, door2 not · supported）; · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CDS-K1T502_Series_Access_Control_Terminal_V1.20.0_build251204_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-K1T642EFW - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 3.7.80 | Applied to: [DS-K1T642EFW](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779870290/Firmware__V3.7.80_251218_S3000701506.zip) | 2025-12-18 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779870290/Firmware__V3.7.80_251218_S3000701506.zip) | — |

</details>


<details>
<summary><h2>DS-K1T670MFWX - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 4.48.20 | Applied to: [DS-K1T670MFWX](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780531020/Firmware__V4.48.20_260515_S3000722841.zip), [DS-K1T670MWX-QR](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780531020/Firmware__V4.48.20_260515_S3000722841.zip), [DS-K1T670MWX-WBQR](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780531020/Firmware__V4.48.20_260515_S3000722841.zip), [DS-K1T670MWX-WEQR](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780531020/Firmware__V4.48.20_260515_S3000722841.zip), [DS-K1T670MX](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780531020/Firmware__V4.48.20_260515_S3000722841.zip), [DS-K1T670MX-QR](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780531020/Firmware__V4.48.20_260515_S3000722841.zip), [DS-K1T670MX-WB](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780531020/Firmware__V4.48.20_260515_S3000722841.zip), [DS-K1T670MX-WE](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780531020/Firmware__V4.48.20_260515_S3000722841.zip) | 2026-04-27 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780531020/Firmware__V4.48.20_260515_S3000722841.zip) | — |

</details>


<details>
<summary><h2>DS-K1T673DBWFX - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 4.48.20 | Applied to: [DS-K1T673DBWFX](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780531020/Firmware__V4.48.20_260515_S3000722841.zip), [DS-K1T673DBWFX-QR](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780531020/Firmware__V4.48.20_260515_S3000722841.zip), [DS-K1T673DG1X-E1](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780531020/Firmware__V4.48.20_260515_S3000722841.zip), [DS-K1T673DGX-E1](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780531020/Firmware__V4.48.20_260515_S3000722841.zip), [DS-K1T673DWX](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780531020/Firmware__V4.48.20_260515_S3000722841.zip), [DS-K1T673DWX-E1](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780531020/Firmware__V4.48.20_260515_S3000722841.zip), [DS-K1T673DWX-PROE1](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780531020/Firmware__V4.48.20_260515_S3000722841.zip), [DS-K1T673DX](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780531020/Firmware__V4.48.20_260515_S3000722841.zip) | 2026-05-15 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780531020/Firmware__V4.48.20_260515_S3000722841.zip) | — |

</details>


<details>
<summary><h2>DS-K1T8003EF - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 1.4.21 | Applied to: [DS-K1T8003EF](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V1.4.21_260327_S3000711457.zip), [DS-K1T8003F](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V1.4.21_260327_S3000711457.zip) | 2026-03-27 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V1.4.21_260327_S3000711457.zip) | — |

</details>


<details>
<summary><h2>DS-K1T804AEF - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 1.4.21 | Applied to: [DS-K1T804AEF](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V1.4.21_260327_S3000711452.zip), [DS-K1T804AF](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V1.4.21_260327_S3000711452.zip), [DS-K1T804AMF](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V1.4.21_260327_S3000711452.zip), [DS-KAS261](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V1.4.21_260327_S3000711452.zip) | 2026-03-27 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V1.4.21_260327_S3000711452.zip) | — |

</details>


<details>
<summary><h2>DS-K1T807EBFWX-E1 - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 4.24.20 | Applied to: [DS-K1T807EBFWX-E1](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779758234/Firmware__V4.24.20_260209_S3000704686.zip), [DS-K1T807EBFWX-QRE1](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779758234/Firmware__V4.24.20_260209_S3000704686.zip), [DS-K1T807EBWX-QRE1](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779758234/Firmware__V4.24.20_260209_S3000704686.zip), [DS-K1T807EX-E1](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779758234/Firmware__V4.24.20_260209_S3000704686.zip), [DS-K1T807MBFWX-E1](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779758234/Firmware__V4.24.20_260209_S3000704686.zip), [DS-K1T807MBFWX-QRE1](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779758234/Firmware__V4.24.20_260209_S3000704686.zip), [DS-K1T807MBWX-QRE1](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779758234/Firmware__V4.24.20_260209_S3000704686.zip), [DS-K1T807MX-E1](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779758234/Firmware__V4.24.20_260209_S3000704686.zip) | 2026-02-09 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779758234/Firmware__V4.24.20_260209_S3000704686.zip) | — |

</details>


<details>
<summary><h2>DS-K2602T - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 1.1.3 | Applied to: [[DS-K2602T](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780043044/Firmware__V1.1.3_251120_S3000687367.zip)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780043044/Firmware__V1.1.3_251120_S3000687367.zip), DS-K2602T (MAIN BOARD), [DS-K2602TMAIN](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780043044/Firmware__V1.1.3_251120_S3000687367.zip) BOARD | 2025-11-20 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780043044/Firmware__V1.1.3_251120_S3000687367.zip) | — |

</details>


<details>
<summary><h2>DS-K3B220X - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 1.1.0 | Applied to: [DS-K3B220X](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779870290/Firmware__V1.1.0_260122_S3000699698.zip), [DS-K3B220X-R/M-DP65](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779870290/Firmware__V1.1.0_260122_S3000699698.zip), [DS-K3B220X-L/M-DP65](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779870290/Firmware__V1.1.0_260122_S3000699698.zip), [DS-K3B220X-L/M-DP75](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779870290/Firmware__V1.1.0_260122_S3000699698.zip), [DS-K3B220X-M/M-DP75](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779870290/Firmware__V1.1.0_260122_S3000699698.zip), [DS-K3B220X-R/M-DP75](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779870290/Firmware__V1.1.0_260122_S3000699698.zip), [DS-K3B220X-L/PG](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779870290/Firmware__V1.1.0_260122_S3000699698.zip), [DS-K3B220X-M/PG](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779870290/Firmware__V1.1.0_260122_S3000699698.zip) | 2025-12-19 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779870290/Firmware__V1.1.0_260122_S3000699698.zip) | — |

</details>


<details>
<summary><h2>DS-K3B501SX - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 2.0.6 | Applied to: [DS-K3B501SX](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780081037/Firmware__V2.0.6_251024_S3000687327.zip), [DS-K3B501SX-L/M-DP65](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780081037/Firmware__V2.0.6_251024_S3000687327.zip), [DS-K3B501SX-L/M-DP90](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780081037/Firmware__V2.0.6_251024_S3000687327.zip), [DS-K3B501SX-L/M-DP110](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780081037/Firmware__V2.0.6_251024_S3000687327.zip), [DS-K3B501SX-L/MPG-DP65](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780081037/Firmware__V2.0.6_251024_S3000687327.zip), [DS-K3B501SX-L/MPG-DP75](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780081037/Firmware__V2.0.6_251024_S3000687327.zip), [DS-K3B501SX-L/MPG-DP90](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780081037/Firmware__V2.0.6_251024_S3000687327.zip), [DS-K3B501SX-L/MPG-DP110](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780081037/Firmware__V2.0.6_251024_S3000687327.zip) | 2025-10-24 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780081037/Firmware__V2.0.6_251024_S3000687327.zip) | Add NFC log retrieval function to the card reader; · Disable button triggering for 700ms after swiping card to prevent accidental touch · Optimized Features · Optimize beep response for touch button · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CDS-K110X_Series_Card_Reader_V2.0.6_build251024_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-K3B530X - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 1.2.0 | Applied to: [DS-K3B530X](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780531020/Firmware__V1.2.0_251022_S3000681572.zip), [DS-K3B530X-M/MPG-DP65](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780531020/Firmware__V1.2.0_251022_S3000681572.zip), [DS-K3B530X-R/MPG-DP65](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780531020/Firmware__V1.2.0_251022_S3000681572.zip), [DS-K3B530X-M/MPG-DP90](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780531020/Firmware__V1.2.0_251022_S3000681572.zip), [DS-K3B530X-M/MPG-DP65-90](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780531020/Firmware__V1.2.0_251022_S3000681572.zip), [DS-K3B530X-M/M-DP65](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780531020/Firmware__V1.2.0_251022_S3000681572.zip), [DS-K3B530X-R/MPG-DP90](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780531020/Firmware__V1.2.0_251022_S3000681572.zip), [DS-K3B530X-R/M-DP65](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780531020/Firmware__V1.2.0_251022_S3000681572.zip) | 2025-10-22 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780531020/Firmware__V1.2.0_251022_S3000681572.zip) | — |

</details>


<details>
<summary><h2>DS-K3B631TX - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 1.1.0 | Applied to: [DS-K3B631TX](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779870290/Firmware__V1.1.0_260122_S3000699698.zip), [DS-K3B631TX-L/MPIQL-DP65](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779870290/Firmware__V1.1.0_260122_S3000699698.zip), [DS-K3B631TX-M/MPIQL-DP65](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779870290/Firmware__V1.1.0_260122_S3000699698.zip), [DS-K3B631TX-R/MPIQL-DP65](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779870290/Firmware__V1.1.0_260122_S3000699698.zip), [DS-K3B631TX-L/DPIQL](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779870290/Firmware__V1.1.0_260122_S3000699698.zip), [DS-K3B631TX-M/DPIQL](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779870290/Firmware__V1.1.0_260122_S3000699698.zip), [DS-K3B631TX-R/DPIQL](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779870290/Firmware__V1.1.0_260122_S3000699698.zip), [DS-K3B631TX-L/DPIL](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779870290/Firmware__V1.1.0_260122_S3000699698.zip) | 2026-01-19 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779870290/Firmware__V1.1.0_260122_S3000699698.zip) | — |

</details>


<details>
<summary><h2>DS-K3BC430LX - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 2.1.0 | Applied to: [DS-K3BC430LX](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779870290/Firmware__V2.1.0_251219_S3000692666.zip), [DS-K3BC430LX/868](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779870290/Firmware__V2.1.0_251219_S3000692666.zip) | 2025-12-19 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779870290/Firmware__V2.1.0_251219_S3000692666.zip) | — |

</details>


<details>
<summary><h2>DS-K3G200BX - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 1.0.0 | Applied to: [DS-K3G200BX](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780617965/Firmware__V1.0.0_260417_S3000718427.zip), [DS-K3G200BX-R/E-DM55](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780617965/Firmware__V1.0.0_260417_S3000718427.zip), [DS-K3G200BX-R/M-DM55](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780617965/Firmware__V1.0.0_260417_S3000718427.zip), [DS-K3G200BX-R/INE-OUTM-DM55](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780617965/Firmware__V1.0.0_260417_S3000718427.zip), [DS-K3G200BX-R/MQ-DM55](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780617965/Firmware__V1.0.0_260417_S3000718427.zip), [DS-K3G225X](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780617965/Firmware__V1.0.0_260417_S3000718427.zip), [DS-K3G225X-R/E-DM55](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780617965/Firmware__V1.0.0_260417_S3000718427.zip), [DS-K3G225X-R/M-DM55](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780617965/Firmware__V1.0.0_260417_S3000718427.zip) | 2025-12-15 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780617965/Firmware__V1.0.0_260417_S3000718427.zip) | — |

</details>


<details>
<summary><h2>DS-K3G200X - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 2.0.6 | Applied to: [DS-K3G200X](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780081037/Firmware__V2.0.6_251024_S3000687327.zip), [DS-K3G200X-R/M-DM55](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780081037/Firmware__V2.0.6_251024_S3000687327.zip), [DS-K3G200X-R/E-DM55](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780081037/Firmware__V2.0.6_251024_S3000687327.zip), [DS-K3G200X-R/D-DM55](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780081037/Firmware__V2.0.6_251024_S3000687327.zip), [DS-K3G200X-R/DM55](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780081037/Firmware__V2.0.6_251024_S3000687327.zip), [DS-K3G200X-R/MQ-DM55](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780081037/Firmware__V2.0.6_251024_S3000687327.zip), [DS-K3G200X-R/PG-DM55](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780081037/Firmware__V2.0.6_251024_S3000687327.zip), [DS-K3Y501SX](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780081037/Firmware__V2.0.6_251024_S3000687327.zip) | 2026-01-29 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780081037/Firmware__V2.0.6_251024_S3000687327.zip) | — |

</details>


<details>
<summary><h2>DS-K3G411CX - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 2.0.7 | Applied to: [DS-K3G411CX](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780732335/Firmware__V2.0.7_260401_S3000711496.zip), [DS-K3G411CX-R/MPA-DM55](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780732335/Firmware__V2.0.7_260401_S3000711496.zip), [DS-K3G411CX-R/M-DM55](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780732335/Firmware__V2.0.7_260401_S3000711496.zip), [DS-K3G411CX-R/MQ-DM55](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780732335/Firmware__V2.0.7_260401_S3000711496.zip), [DS-K3G501CX](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780732335/Firmware__V2.0.7_260401_S3000711496.zip), [DS-K3G501CX-R/MPA-DM55](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780732335/Firmware__V2.0.7_260401_S3000711496.zip), [DS-K3G501CX-R/M-DM55](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780732335/Firmware__V2.0.7_260401_S3000711496.zip), [DS-K3G501CX-R/MQ-DM55](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780732335/Firmware__V2.0.7_260401_S3000711496.zip) | 2026-04-01 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780732335/Firmware__V2.0.7_260401_S3000711496.zip) | — |

</details>


<details>
<summary><h2>DS-K3G501X - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 2.0.6 | Applied to: [DS-K3G501X](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780081037/Firmware__V2.6.0_231129_S3000543848.zip), [DS-K3G501X-R/M-DM55](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780081037/Firmware__V2.6.0_231129_S3000543848.zip), [DS-K3G501X-R/MPG-DM55](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780081037/Firmware__V2.6.0_231129_S3000543848.zip), [DS-K3G501X-R/MFPG-DM55](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780081037/Firmware__V2.6.0_231129_S3000543848.zip), [DS-K3G501X-R/MPG-DM55/868](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780081037/Firmware__V2.6.0_231129_S3000543848.zip), [DS-K3G501X-R/M-INPG-DM55](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780081037/Firmware__V2.6.0_231129_S3000543848.zip), [DS-K3G501X-R/E-DM55](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780081037/Firmware__V2.6.0_231129_S3000543848.zip), [DS-K3G501X-R/EPG-DM55](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780081037/Firmware__V2.6.0_231129_S3000543848.zip) | 2025-10-24 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780081037/Firmware__V2.6.0_231129_S3000543848.zip) | Add NFC log retrieval function to the card reader; · Disable button triggering for 700ms after swiping card to prevent accidental touch · Optimized Features · Optimize beep response for touch button · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CDS-K110X_Series_Card_Reader_V2.0.6_build251024_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-K3G530LX - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 4.0.0 | Applied to: [DS-K3G530LX](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780081037/Firmware__V4.0.0_251023_S3000681590.zip), [DS-K3G530LX-R/PG-DM55](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780081037/Firmware__V4.0.0_251023_S3000681590.zip), [DS-K3G530LX-R/DM55](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780081037/Firmware__V4.0.0_251023_S3000681590.zip), [DS-K3G530X](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780081037/Firmware__V4.0.0_251023_S3000681590.zip), [DS-K3G530X-R/MPG-DM55](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780081037/Firmware__V4.0.0_251023_S3000681590.zip), [DS-K3G530X-R/EPG-DM55](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780081037/Firmware__V4.0.0_251023_S3000681590.zip), [DS-K3G530X-R/M-DM55](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780081037/Firmware__V4.0.0_251023_S3000681590.zip), [DS-K3G530X-R/E-DM55](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780081037/Firmware__V4.0.0_251023_S3000681590.zip) | 2025-10-23 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780081037/Firmware__V4.0.0_251023_S3000681590.zip) | — |

</details>


<details>
<summary><h2>DS-K3G530X - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 3.3.0 | Applied to: [DS-K3G530X](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780081037/Firmware__V3.3.0_251027_S3000681148.zip), [DS-K3G530X-R/MPG-DM55](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780081037/Firmware__V3.3.0_251027_S3000681148.zip), [DS-K3G530X-R/EPG-DM55](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780081037/Firmware__V3.3.0_251027_S3000681148.zip), [DS-K3G530X-R/M-DM55](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780081037/Firmware__V3.3.0_251027_S3000681148.zip), [DS-K3G530X-R/E-DM55](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780081037/Firmware__V3.3.0_251027_S3000681148.zip), [DS-K3G530X-R/DPGQ-DM55](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780081037/Firmware__V3.3.0_251027_S3000681148.zip), [DS-K3G530X/MODULAR](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780081037/Firmware__V3.3.0_251027_S3000681148.zip), [DS-K3G530X-R/DM55](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780081037/Firmware__V3.3.0_251027_S3000681148.zip) | 2025-10-27 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780081037/Firmware__V3.3.0_251027_S3000681148.zip) | — |

</details>


<details>
<summary><h2>DS-K3GL606WX-WE - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 1.1.0 | Applied to: [DS-K3GL606WX-WE](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779870290/Firmware__V1.1.0_260122_S3000699698.zip) | 2026-01-22 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779870290/Firmware__V1.1.0_260122_S3000699698.zip) | — |

</details>


<details>
<summary><h2>DS-K3Y220LX - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 2.0.0 | Applied to: [DS-K3Y220LX](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779870290/Firmware__V2.0.0_251219_S3000692664.zip), [DS-K3Y220LX-L1/PG-DP55](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779870290/Firmware__V2.0.0_251219_S3000692664.zip), [DS-K3Y220LX-L1/DP55](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779870290/Firmware__V2.0.0_251219_S3000692664.zip), [DS-K3Y220LX-L2/PG-DP55](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779870290/Firmware__V2.0.0_251219_S3000692664.zip), [DS-K3Y220LX-M1/PG-DP55](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779870290/Firmware__V2.0.0_251219_S3000692664.zip), [DS-K3Y220LX-M1/DP55](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779870290/Firmware__V2.0.0_251219_S3000692664.zip), [DS-K3Y220LX-M2/PG-DP55](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779870290/Firmware__V2.0.0_251219_S3000692664.zip), [DS-K3Y220LX-M2/DP55](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779870290/Firmware__V2.0.0_251219_S3000692664.zip) | 2025-12-19 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779870290/Firmware__V2.0.0_251219_S3000692664.zip) | — |

</details>


<details>
<summary><h2>DS-K3Y411BX - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 2.7.1 | Applied to: [DS-K3Y411BX](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780043044/Firmware__V2.7.1_260521_S3000724470.zip), [DS-K3Y411BX-M/MPG-DP55](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780043044/Firmware__V2.7.1_260521_S3000724470.zip), [DS-K3Y411BX-R/MPG-DP55](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780043044/Firmware__V2.7.1_260521_S3000724470.zip) | 2026-05-21 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780043044/Firmware__V2.7.1_260521_S3000724470.zip) | — |

</details>


<details>
<summary><h2>DS-K6B411TX - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 1.0.0 | Applied to: [DS-K6B411TX](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780617965/Firmware__V1.0.0_260417_S3000718427.zip), [DS-K6B411TMX-L](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780617965/Firmware__V1.0.0_260417_S3000718427.zip), [DS-K6B411TEX-L](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780617965/Firmware__V1.0.0_260417_S3000718427.zip), [DS-K6B411TMX-M](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780617965/Firmware__V1.0.0_260417_S3000718427.zip), [DS-K6B411TEX-M](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780617965/Firmware__V1.0.0_260417_S3000718427.zip), [DS-K6B411TMX-R](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780617965/Firmware__V1.0.0_260417_S3000718427.zip), [DS-K6B411TEX-R](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780617965/Firmware__V1.0.0_260417_S3000718427.zip), [DS-K6B411TMQX-L](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780617965/Firmware__V1.0.0_260417_S3000718427.zip) | 2025-10-23 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780617965/Firmware__V1.0.0_260417_S3000718427.zip) | — |

</details>


<details>
<summary><h2>DS-K6BC402LX - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 2.2.0 | Applied to: [DS-K6BC402LX](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779764110/Firmware__V2.2.0_260114_S3000699468.zip), [DS-K6BC402LX-LR](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779764110/Firmware__V2.2.0_260114_S3000699468.zip), [DS-K6BC402LX-LR/PA](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779764110/Firmware__V2.2.0_260114_S3000699468.zip), [DS-K6BC402X-RS](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779764110/Firmware__V2.2.0_260114_S3000699468.zip), [[DS-K6BC402X-RS/M](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779764110/Firmware__V2.2.0_260114_S3000699468.zip)Q](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779764110/Firmware__V2.2.0_260114_S3000699468.zip), DS-K6BC402X-RS/M, [DS-K6BC402X-RS/E](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779764110/Firmware__V2.2.0_260114_S3000699468.zip) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779764110/Firmware__V2.2.0_260114_S3000699468.zip) | — |

</details>


<details>
<summary><h2>DS-K6BC402X-RS - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 3.4.0 | Applied to: [DS-K6BC402X-RS](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779764110/Firmware__V3.4.0_260113_S3000699384.zip), [[DS-K6BC402X-RS/M](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779764110/Firmware__V3.4.0_260113_S3000699384.zip)Q](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779764110/Firmware__V3.4.0_260113_S3000699384.zip), DS-K6BC402X-RS/M, [DS-K6BC402X-RS/E](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779764110/Firmware__V3.4.0_260113_S3000699384.zip) | 2026-01-13 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779764110/Firmware__V3.4.0_260113_S3000699384.zip) | — |

</details>


<details>
<summary><h2>DS-KD7000EY-ME2 - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 1.3.0 | Applied to: [DS-KD7000EY-ME2](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780081037/Firmware__V1.3.0_251210_S3000691986.zip), [DS-KD7003EY-IME2](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780081037/Firmware__V1.3.0_251210_S3000691986.zip), [DS-KD7003EY-IME2/ALUMINUM](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780081037/Firmware__V1.3.0_251210_S3000691986.zip), [DS-KD7003EY-S2](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780081037/Firmware__V1.3.0_251210_S3000691986.zip), [DS-KIS704EY](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780081037/Firmware__V1.3.0_251210_S3000691986.zip), [DS-KIS704EY/ALUMINUM](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780081037/Firmware__V1.3.0_251210_S3000691986.zip) | 2025-12-10 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780081037/Firmware__V1.3.0_251210_S3000691986.zip) | ⚠️ Beta firmware. Door station: · Fixed a rare issue where the elevator could not be called after a device restart · Optimized the web page UI and fixed some display issue · Optimized the M1 card encryption function · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5C2_Wire_HD_Video_Intercom_V1.3.0_build251210_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-KD8005-IME1 - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 3.10.0 | Applied to: [DS-KD8005-IME1](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779994076/Firmware__V3.10.0_251125_S3000687368.zip), [DS-KD8005-IME1/S](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779994076/Firmware__V3.10.0_251125_S3000687368.zip) | 2025-11-25 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779994076/Firmware__V3.10.0_251125_S3000687368.zip) | Main unit of modular door station with high 5 MP resolution camera · Flexible adjustment of 0/1/2 call buttons · Standard PoE power supply (IEEE 802.3af) · IP65, IK08 protection level · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CDS-KD8005_Main_Module_V3.10.0_build251125_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-KH6000-E1 - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 2.2.116 | Applied to: [DS-KH6000-E1](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780563030/Firmware__V2.2.116_260519_S3000724104.zip), [DS-KH6000-E1/WHITE](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780563030/Firmware__V2.2.116_260519_S3000724104.zip), [DS-KH6100-E1/WHITE](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780563030/Firmware__V2.2.116_260519_S3000724104.zip) | 2026-05-19 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780563030/Firmware__V2.2.116_260519_S3000724104.zip) | — |

</details>


<details>
<summary><h2>DS-KH6110-WE1 - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 2.2.116 | Applied to: [DS-KH6110-WE1](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780563030/Firmware__V2.2.116_260519_S3000724104.zip), [DS-KH6110-WE1/WHITE](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780563030/Firmware__V2.2.116_260519_S3000724104.zip), [DS-KIS606-P](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780563030/Firmware__V2.2.116_260519_S3000724104.zip) | 2026-04-27 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780563030/Firmware__V2.2.116_260519_S3000724104.zip) | — |

</details>


<details>
<summary><h2>DS-KH6320-LE1(B)/WHITE - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 2.2.114 | Applied to: [DS-KH6320-LE1(B)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780599961/Firmware__V2.2.114_260427_S3000724121.zip)/WHITE, [DS-KH6350-WTE1/WHITE](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780599961/Firmware__V2.2.114_260427_S3000724121.zip), [DS-KH6351-TE1](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780599961/Firmware__V2.2.114_260427_S3000724121.zip), [DS-KH6351-WTE1](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780599961/Firmware__V2.2.114_260427_S3000724121.zip), [DS-KIS605-P(C)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780599961/Firmware__V2.2.114_260427_S3000724121.zip), [DS-KIS607-S](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780599961/Firmware__V2.2.114_260427_S3000724121.zip), [DS-KIS608-P](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780599961/Firmware__V2.2.114_260427_S3000724121.zip), [DS-KIS610-P](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780599961/Firmware__V2.2.114_260427_S3000724121.zip) | 2026-04-27 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780599961/Firmware__V2.2.114_260427_S3000724121.zip) | — |

</details>


<details>
<summary><h2>DS-KH6320-TDE1 - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 2.2.114 | Applied to: [DS-KH6320-TDE1](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780599961/Firmware__V2.2.114_260427_S3000724105.zip), [DS-KH6320-TE1](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780599961/Firmware__V2.2.114_260427_S3000724105.zip), [DS-KH6320-WTDE1](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780599961/Firmware__V2.2.114_260427_S3000724105.zip), [DS-KH6320-WTE1](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780599961/Firmware__V2.2.114_260427_S3000724105.zip), [DS-KH6320Y-WTE2](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780599961/Firmware__V2.2.114_260427_S3000724105.zip), [DS-KH8350-TE1](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780599961/Firmware__V2.2.114_260427_S3000724105.zip), [DS-KH8350-WTE1](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780599961/Firmware__V2.2.114_260427_S3000724105.zip), [DS-KH8520-WTE1](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780599961/Firmware__V2.2.114_260427_S3000724105.zip) | 2026-04-27 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780599961/Firmware__V2.2.114_260427_S3000724105.zip) | — |

</details>


<details>
<summary><h2>DS-KH7300EY-WTPE2/WHITE - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 2.2.74 | Applied to: [DS-KH7300EY-WTPE2/WHITE](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780043044/Firmware__V2.2.74_251104_S3000687885.zip), [DS-KIS707EY](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780043044/Firmware__V2.2.74_251104_S3000687885.zip), [DS-KIS708EY](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780043044/Firmware__V2.2.74_251104_S3000687885.zip) | 2025-11-04 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780043044/Firmware__V2.2.74_251104_S3000687885.zip) | ⚠️ Beta firmware. Door station: · Fixed a rare issue where the elevator could not be called after a device restart · Optimized the web page UI and fixed some display issue · Optimized the M1 card encryption function · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5C2_Wire_HD_Video_Intercom_V1.3.0_build251210_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-KH8380-TE1 - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 2.2.114 | Applied to: [DS-KH8380-TE1](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780599961/Firmware__V2.2.114_260427_S3000724121.zip), [DS-KH8380-WTE1](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780599961/Firmware__V2.2.114_260427_S3000724121.zip), [DS-KH8380-WTE1/FLUSH](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780599961/Firmware__V2.2.114_260427_S3000724121.zip), [DS-KH8381-TE1](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780599961/Firmware__V2.2.114_260427_S3000724121.zip), [DS-KH8381-WTE1](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780599961/Firmware__V2.2.114_260427_S3000724121.zip), [DS-KH8381-WTE1/FLUSH](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780599961/Firmware__V2.2.114_260427_S3000724121.zip), [[DS-KIS613-S](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780599961/Firmware__V2.2.114_260427_S3000724121.zip)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780599961/Firmware__V2.2.114_260427_S3000724121.zip), DS-KIS613-S( | 2026-04-27 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780599961/Firmware__V2.2.114_260427_S3000724121.zip) | — |

</details>


<details>
<summary><h2>DS-KIS705EY - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 1.3.0 | Applied to: [DS-KIS705EY](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780081037/Firmware__V1.3.0_251210_S3000691986.zip), [DS-KIS705EY-2MONITORS](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780081037/Firmware__V1.3.0_251210_S3000691986.zip), [DS-KIS705EY/2MONITORS](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780081037/Firmware__V1.3.0_251210_S3000691986.zip), [DS-KIS706EY](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780081037/Firmware__V1.3.0_251210_S3000691986.zip), [DS-KIS707EY](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780081037/Firmware__V1.3.0_251210_S3000691986.zip), [DS-KIS708EY](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780081037/Firmware__V1.3.0_251210_S3000691986.zip), [DS-KV7023EY-IME2](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780081037/Firmware__V1.3.0_251210_S3000691986.zip), [DS-KV7413EY-IME2-1/2/4](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780081037/Firmware__V1.3.0_251210_S3000691986.zip) | 2025-12-10 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780081037/Firmware__V1.3.0_251210_S3000691986.zip) | ⚠️ Beta firmware. Door station: · Fixed a rare issue where the elevator could not be called after a device restart · Optimized the web page UI and fixed some display issue · Optimized the M1 card encryption function · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5C2_Wire_HD_Video_Intercom_V1.3.0_build251210_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-PA201P-16WB - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 1.2.0 | Applied to: [DS-PA201P-16WB](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780531020/Firmware__V1.2.0_251022_S3000681572.zip), [DS-PA201P-16WE](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780531020/Firmware__V1.2.0_251022_S3000681572.zip), [DS-PA201P-32WB](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780531020/Firmware__V1.2.0_251022_S3000681572.zip), [DS-PA201PG-16WB](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780531020/Firmware__V1.2.0_251022_S3000681572.zip), [DS-PA201PG-16WE](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780531020/Firmware__V1.2.0_251022_S3000681572.zip), [DS-PA201PG-32WB](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780531020/Firmware__V1.2.0_251022_S3000681572.zip), [DS-PA201PG-32WE](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780531020/Firmware__V1.2.0_251022_S3000681572.zip), [DS-PA201PG-KIT-16WE](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780531020/Firmware__V1.2.0_251022_S3000681572.zip) | 2025-11-21 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780531020/Firmware__V1.2.0_251022_S3000681572.zip) | — |

</details>


<details>
<summary><h2>DS-TDSB0G-FC/2KM - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.1.4 | Applied to: [DS-TDSB0G-FC/2KM](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780043044/Firmware__V5.1.4_251107_S3000686639.zip), [DS-TDSB0G-FK/120M](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780043044/Firmware__V5.1.4_251107_S3000686639.zip), [DS-TDSB0G-FK/500M](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780043044/Firmware__V5.1.4_251107_S3000686639.zip), [DS-TDSB0G-FK/60M](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780043044/Firmware__V5.1.4_251107_S3000686639.zip), [DS-TDSB0G-FX/1KM](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780043044/Firmware__V5.1.4_251107_S3000686639.zip) | 2025-11-07 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780043044/Firmware__V5.1.4_251107_S3000686639.zip) | — |

</details>


<details>
<summary><h2>DS-TP50-08H - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.12 | Applied to: [DS-TP50-08H](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780043044/Firmware__V5.5.12_251117_S3000685520.zip), [DS-TP50-08H/4T](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780043044/Firmware__V5.5.12_251117_S3000685520.zip) | 2025-11-17 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780043044/Firmware__V5.5.12_251117_S3000685520.zip) | — |

</details>


<details>
<summary><h2>DS-TP50-16R - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.14 | Applied to: [DS-TP50-16R](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780563030/Firmware__V5.5.14_260520_S3000723829.zip), [DS-TP50-16R/4T](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780563030/Firmware__V5.5.14_260520_S3000723829.zip) | 2026-05-20 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780563030/Firmware__V5.5.14_260520_S3000723829.zip) | — |

</details>


<details>
<summary><h2>DVR-104G-M1/T - DVR_V4 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 4.83.613 | Applied to: DVR-104G-M1/T | 2025-10-28 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780081037/Firmware_Asia_V4.83.613_251028_S3000681724.zip) | improve product performance, and will take effect automatically after upgrading from previous versions. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202511/releasenote%5CTurbo_HD_DVR_V4.83.613build251028_Release_Notes.pdf) |

</details>


<details>
<summary><h2>DVR-108G-M1 - DVR_V4 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 4.83.614 | Applied to: DVR-108G-M1, DVR-108G-M1(C), DVR-208G-M1, DVR-208G-M1(C) | 2025-12-10 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779994076/Firmware_Asia_V4.83.614_251210_S3000691920.zip) | Fix known issues Customer Impact and Recommended Action This new firmware upgrade is to improve product performance, and will take effect automatically after upgrading from previous versions. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CTurbo_HD_DVR_V4.83.614build251210_Release_Notes.pdf) |

</details>


<details>
<summary><h2>DVR-204G-M1 - DVR_V4 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 4.83.614 | Applied to: DVR-204G-M1, DVR-204G-M1(C) | 2025-12-10 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779994076/Firmware__V4.83.614_251210_S3000691913.zip) | Fix known issues Customer Impact and Recommended Action This new firmware upgrade is to improve product performance, and will take effect automatically after upgrading from previous versions. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CTurbo_HD_DVR_V4.83.614build251210_Release_Notes.pdf) |

</details>


<details>
<summary><h2>DVR-204G-M1/T - DVR_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 4.83.614 | Applied to: DVR-204G-M1/T | 2025-12-10 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779994076/Firmware_Asia_V4.83.614_251210_S3000691935.zip) | — |

</details>


<details>
<summary><h2>DVR-204Q-M1 - DVR_V4 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 4.84.011 | Applied to: DVR-204Q-M1, DVR-204Q-M1(C), DVR-204Q-M1(E), DVR-204Q-M1/T | 2025-12-17 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779907479/Firmware_Europe_V4.84.011_251217_S3000693333.zip) | Fix known defects to improve product stability. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202603/releasenote%5CTurbo_HD_DVR_V4.84.011build251217_Release_Notes.pdf) |

</details>


<details>
<summary><h2>DVR-204U-M1/T - DVR_V4 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 4.84.011 | Applied to: DVR-204U-M1/T, DVR-208Q-M1/T | 2025-12-17 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779907479/Firmware_Europe_V4.84.011_251217_S3000693333.zip) | Fix known defects to improve product stability. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202603/releasenote%5CTurbo_HD_DVR_V4.84.011build251217_Release_Notes.pdf) |

</details>


<details>
<summary><h2>DVR-208G-M1/T - DVR_V4 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 4.83.614 | Applied to: DVR-208G-M1/T | 2025-12-10 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779994076/Firmware_Asia_V4.83.614_251210_S3000691944.zip) | Fix known issues Customer Impact and Recommended Action This new firmware upgrade is to improve product performance, and will take effect automatically after upgrading from previous versions. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CTurbo_HD_DVR_V4.83.614build251210_Release_Notes.pdf) |

</details>


<details>
<summary><h2>DVR-208Q-M1 - DVR_V4 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 4.84.011 | Applied to: DVR-208Q-M1, DVR-208Q-M1(C), DVR-208Q-M1(E) | 2025-12-17 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779907479/Firmware_Europe_V4.84.011_251217_S3000693333.zip) | Fix known defects to improve product stability. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202603/releasenote%5CTurbo_HD_DVR_V4.84.011build251217_Release_Notes.pdf) |

</details>


<details>
<summary><h2>DVR-208U-M1/T - DVR_V4 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 4.84.011 | Applied to: DVR-208U-M1/T, DVR-216Q-M1, DVR-216Q-M1(F), DVR-216Q-M1/T, DVR-216U-M1/T | 2025-12-17 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779907479/Firmware_Europe_V4.84.011_251217_S3000693333.zip) | Fix known defects to improve product stability. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202603/releasenote%5CTurbo_HD_DVR_V4.84.011build251217_Release_Notes.pdf) |

</details>


<details>
<summary><h2>HM-TD1017-2/QW-HS121 - THERMAL_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.54 | Applied to: HM-TD1017-2/QW-HS121 | 2026-03-25 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779754560/Firmware__V5.5.54_260325_S3000710191.zip) | 1.1 Issues fixes： 1) Fixed known software issues. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202605/releasenote%5CGeneral_Firmware_Update_Release_notes.pdf) |

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
| 5.5.348 | Applied to: HM-TD1228-2/G1/T3A, HM-TD1228-3/G1/T3A, HM-TD1228-7/G1/T3A, HM-TD2628-10/G1/T3A, HM-TD2628-3/G1/T3A, HM-TD2628-7/G1/T3A, HM-TD2638-10/G1/T3Y | 2026-04-27 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779753206/Firmware__V5.5.348_260410_S3000714869.zip) | 1.1 Issues fixes： 1) Fixed known software issues. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202605/releasenote%5CGeneral_Firmware_Update_Release_notes.pdf) |

</details>


<details>
<summary><h2>HM-TD1228T-2/G1/T3A - THERMAL_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.348 | Applied to: HM-TD1228T-2/G1/T3A, HM-TD1228T-3/G1/T3A, HM-TD2168-5/G1/T3Y, HM-TD2168T-5/G1/T3Y, HM-TD2628T-3/G1/T3A, HM-TD2628T-7/G1/T3A, HM-TD2638-15/G1/T3Y, HM-TD2638-25/G1/T3Y | 2026-04-10 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779753206/Firmware__V5.5.348_260410_S3000714871.zip) | Perimeter Protection related： · Support Abnormal Action Detection function. · Allow the camera to detect special poses such as crawling, crouching, · climbing walls, bending over, and swinging arms. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202604/releasenote%5CThermal_Network_Fixed_Camera_V5.5.348_Release_Notes.pdf) |

</details>


<details>
<summary><h2>HM-TD2168-5/G0/T1Y - THERMAL_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.348 | Applied to: HM-TD2168-5/G0/T1Y, HM-TD2168T-5/G0/T1Y, HM-TD2638-10/G0/T1Y, HM-TD2638-15/G0/T1Y, HM-TD2638-25/G0/T1Y, HM-TD2638-35/G0/T1Y, HM-TD2638-4/G0/T1Y, HM-TD2638-8/G0/T1Y | 2026-04-10 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779753206/Firmware__V5.5.348_260410_S3000714869.zip) | Perimeter Protection related： · Support Abnormal Action Detection function. · Allow the camera to detect special poses such as crawling, crouching, · climbing walls, bending over, and swinging arms. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202604/releasenote%5CThermal_Network_Fixed_Camera_V5.5.348_Release_Notes.pdf) |

</details>


<details>
<summary><h2>HM-TD3028T-2/Q(B) - THERMAL_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.342 | Applied to: HM-TD3028T-2/Q(B), HM-TD3028T-3/Q(B) | 2026-04-16 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779522628/Firmware__V5.5.342_260416_S3000717610.zip) | 1.1 Issues fixes： 1) Fixed known software issues. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202605/releasenote%5CGeneral_Firmware_Update_Release_notes.pdf) |

</details>


<details>
<summary><h2>HM-TD5528T-10/W - THERMAL_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.141 | Applied to: HM-TD5528T-10/W, HM-TD5528T-15/W, HM-TD5537T-15/W, HM-TD5537T-25/W, HM-TD5537T-7/W, HM-TD5567T-15/W, HM-TD5567T-25/W, HM-TD5567T-7/W | 2026-04-16 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780531020/Firmware__V5.5.141_260416_S3000716151.zip) | 1.1 Issues fixes： 1) Fixed known software issues. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202605/releasenote%5CGeneral_Firmware_Update_Release_notes.pdf) |

</details>


<details>
<summary><h2>HM-TD63C8-100C4L/G0/T2Y - THERMAL_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.11 | Applied to: HM-TD63C8-100C4L/G0/T2Y, HM-TD63C8-75C4L/G0/T2Y, HM-TD81C8-150ZK4FL/G0/T2 | 2026-05-06 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780683636/Firmware__V5.7.11_260402_S3000713041.zip) | — |

</details>


<details>
<summary><h2>HM-TX2840-10/G0/T1 - THERMAL_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.506 | Applied to: HM-TX2840-10/G0/T1, HM-TX3840-10/G0/T1, HM-TX3840-15/G0/T1, HM-TX3840-25/G0/T1 | 2026-04-01 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780732335/Firmware__V5.5.506_260401_S3000716856.zip) | fixed camera models supporting Guanlan Large-scale. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202604/releasenote%5CThermal_TandemVu_Series_V5.5.506_Release_note.pdf) |

</details>


<details>
<summary><h2>HM-TX2840-10/G1/T3 - THERMAL_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.506 | Applied to: HM-TX2840-10/G1/T3, HM-TX3840-10/G1/T3, HM-TX3840-15/G1/T3, HM-TX3840-25/G1/T3 | 2026-04-01 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780732335/Firmware__V5.5.506_260401_S3000716856.zip) | 1.1 Issues fixes： 1) Fixed known software issues. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202605/releasenote%5CGeneral_Firmware_Update_Release_notes.pdf) |

</details>


<details>
<summary><h2>IDS-2CD5347G2/V-XS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.9.21 | Applied to: [IDS-2CD5347G2/V-XS](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779753206/Firmware__V5.9.21_260423_S3000719054.zip), [IDS-2CD5347G2/V-XS(2.8MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779753206/Firmware__V5.9.21_260423_S3000719054.zip), [IDS-2CD5347G2/V-XS(4MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779753206/Firmware__V5.9.21_260423_S3000719054.zip), [IDS-2CD5387G2/V-XS](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779753206/Firmware__V5.9.21_260423_S3000719054.zip), [IDS-2CD5387G2/V-XS(2.8MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779753206/Firmware__V5.9.21_260423_S3000719054.zip), [IDS-2CD5387G2/V-XS(4MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779753206/Firmware__V5.9.21_260423_S3000719054.zip), [IDS-2CD5A46G2/V-XZ(H)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779753206/Firmware__V5.9.21_260423_S3000719054.zip)S(Y), [IDS-2CD5A46G2/V-XZHSY(2.8-12MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779753206/Firmware__V5.9.21_260423_S3000719054.zip) | 2026-04-23 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779753206/Firmware__V5.9.21_260423_S3000719054.zip) | 1. Support AI Encoding of main stream in Smart Event VCA mode. 2. Modify Features NA · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202605/releasenote%5CDeepinViewX_Network_Camera_V5.9.21_Release_Note_--H9.pdf) |

</details>


<details>
<summary><h2>IDS-2CD70166G2-AP - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.9.23 | Applied to: [IDS-2CD70166G2-AP](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779216345/Firmware__V5.9.23_260407_S3000714059.zip), [IDS-2CD70166G2/E-IHSYR](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779216345/Firmware__V5.9.23_260407_S3000714059.zip), [IDS-2CD70166G2/E-IHSYR(3.8-16MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779216345/Firmware__V5.9.23_260407_S3000714059.zip), [IDS-2CD70166G2/E-IHSYR(11-40MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779216345/Firmware__V5.9.23_260407_S3000714059.zip), [IDS-2CD7046G2-AP](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779216345/Firmware__V5.9.23_260407_S3000714059.zip), [IDS-2CD7046G2/E-IHSYR](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779216345/Firmware__V5.9.23_260407_S3000714059.zip), [IDS-2CD7046G2/E-IHSYR(11-40MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779216345/Firmware__V5.9.23_260407_S3000714059.zip), [IDS-2CD7046G2/E-IHSYR(3.8-16MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779216345/Firmware__V5.9.23_260407_S3000714059.zip) | 2026-04-07 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779216345/Firmware__V5.9.23_260407_S3000714059.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202605/releasenote%5CDeepinView_Camera_V5.9.23_Release_Note.pdf) |

</details>


<details>
<summary><h2>IDS-2CD7026G0(-AP) - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.61 | Applied to: [IDS-2CD7026G0(-AP)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779388610/Firmware__V5.8.61_260327_S3000711542.zip), [IDS-2CD7026G0-AP(C)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779388610/Firmware__V5.8.61_260327_S3000711542.zip), [IDS-2CD7026G0/EP-IHSY](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779388610/Firmware__V5.8.61_260327_S3000711542.zip), [[IDS-2CD7026G0/EP-IHSY(3.8-16MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779388610/Firmware__V5.8.61_260327_S3000711542.zip)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779388610/Firmware__V5.8.61_260327_S3000711542.zip), [[IDS-2CD7026G0/EP-IHSY(11-40MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779388610/Firmware__V5.8.61_260327_S3000711542.zip)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779388610/Firmware__V5.8.61_260327_S3000711542.zip), IDS-2CD7026G0/EP-IHSY(3.8-16MM)(C)O-STD, IDS-2CD7026G0/EP-IHSY(11-40MM)(C), [IDS-2CD7046G0/E-IHSY(/F11)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779388610/Firmware__V5.8.61_260327_S3000711542.zip)(R) | 2026-03-27 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779388610/Firmware__V5.8.61_260327_S3000711542.zip) | 1. ANPR algorithm updates: · 1) Fix the issue that manual capture of motorcycle license plates reports "unknown". · 2) Optimization for Belgian and Hungarian license plates recognition · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202605/releasenote%5CDeepinView_Camera_V5.8.61_Release_Note.pdf) |

</details>


<details>
<summary><h2>IDS-2CD7046G0-H-AP - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.9.1 | Applied to: [IDS-2CD7046G0-H-AP](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780683636/Firmware__V5.9.14_260401_S3000712572.zip) | 2026-04-02 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780683636/Firmware__V5.9.14_260401_S3000712572.zip) |  Improved functionality Fix some known bugs and improve system stability. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202605/releasenote%5CG7-V5.9.1_Release_Note.pdf) |

</details>


<details>
<summary><h2>IDS-2CD7046G0/H-AP - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.9.1 | Applied to: [IDS-2CD7046G0/H-AP](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780683636/Firmware__V5.9.14_260401_S3000712572.zip), [IDS-2CD7086G0/H-AP](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780683636/Firmware__V5.9.14_260401_S3000712572.zip), [IDS-2CD70C5G0/H-AP](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780683636/Firmware__V5.9.14_260401_S3000712572.zip), [IDS-2CD7146G0/H-IZ(H)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780683636/Firmware__V5.9.14_260401_S3000712572.zip)S(Y), [IDS-2CD7146G0/H-IZS(2.8-12MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780683636/Firmware__V5.9.14_260401_S3000712572.zip), [IDS-2CD7146G0/H-IZS(8-32MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780683636/Firmware__V5.9.14_260401_S3000712572.zip), [IDS-2CD7146G0/H-IZHSY(8-32MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780683636/Firmware__V5.9.14_260401_S3000712572.zip), [IDS-2CD7146G0/H-IZHSY(2.8-12MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780683636/Firmware__V5.9.14_260401_S3000712572.zip) | 2026-04-02 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780683636/Firmware__V5.9.14_260401_S3000712572.zip) |  Improved functionality Fix some known bugs and improve system stability. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202605/releasenote%5CG7-V5.9.1_Release_Note.pdf) |

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
| 5.9.1 | Applied to: [IDS-2CD7086G0-H-AP](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780683636/Firmware__V5.9.14_260401_S3000712572.zip) | 2026-04-02 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780683636/Firmware__V5.9.14_260401_S3000712572.zip) |  Improved functionality Fix some known bugs and improve system stability. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202605/releasenote%5CG7-V5.9.1_Release_Note.pdf) |

</details>


<details>
<summary><h2>IDS-2CD70C5G0-H-AP - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.9.1 | Applied to: [IDS-2CD70C5G0-H-AP](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780683636/Firmware__V5.9.14_260401_S3000712572.zip) | 2026-04-02 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780683636/Firmware__V5.9.14_260401_S3000712572.zip) |  Improved functionality Fix some known bugs and improve system stability. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202605/releasenote%5CG7-V5.9.1_Release_Note.pdf) |

</details>


<details>
<summary><h2>IDS-2CD7146G0-H-IZ-H-S-Y- - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.9.1 | Applied to: [IDS-2CD7146G0-H-IZ-H-S-Y-](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780683636/Firmware__V5.9.14_260401_S3000712572.zip) | 2026-04-02 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780683636/Firmware__V5.9.14_260401_S3000712572.zip) |  Improved functionality Fix some known bugs and improve system stability. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202605/releasenote%5CG7-V5.9.1_Release_Note.pdf) |

</details>


<details>
<summary><h2>IDS-2CD7186G0-H-IZ-H-S-Y- - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.9.1 | Applied to: [IDS-2CD7186G0-H-IZ-H-S-Y-](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780683636/Firmware__V5.9.14_260401_S3000712572.zip) | 2026-04-02 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780683636/Firmware__V5.9.14_260401_S3000712572.zip) |  Improved functionality Fix some known bugs and improve system stability. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202605/releasenote%5CG7-V5.9.1_Release_Note.pdf) |

</details>


<details>
<summary><h2>IDS-2CD71C5G0-H-IZ-H-S-Y- - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.9.1 | Applied to: [IDS-2CD71C5G0-H-IZ-H-S-Y-](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780683636/Firmware__V5.9.14_260401_S3000712572.zip) | 2026-04-02 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780683636/Firmware__V5.9.14_260401_S3000712572.zip) |  Improved functionality Fix some known bugs and improve system stability. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202605/releasenote%5CG7-V5.9.1_Release_Note.pdf) |

</details>


<details>
<summary><h2>IDS-2CD7347G0-XS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.2 | Applied to: [IDS-2CD7347G0-XS](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.8.20_260330_S3000711486.zip), [IDS-2CD7347G0-XS(2.8MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.8.20_260330_S3000711486.zip), [IDS-2CD7347G0-XS(4MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.8.20_260330_S3000711486.zip), [IDS-2CD7387G0-XS](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.8.20_260330_S3000711486.zip), [IDS-2CD7387G0-XS(2.8MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.8.20_260330_S3000711486.zip), [IDS-2CD7387G0-XS(4MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.8.20_260330_S3000711486.zip), [IDS-2CD7D47G0-XS](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.8.20_260330_S3000711486.zip), [IDS-2CD7D47G0-XS(2.8MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.8.20_260330_S3000711486.zip) | 2026-04-04 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.8.20_260330_S3000711486.zip) | NA 2. Modify Features Fix some known bugs and improve system stability. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202605/releasenote%5CNetwork_Camera_V5.8.2_Release_Note_--G5.pdf) |

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
| 5.9.1 | Applied to: [IDS-2CD7A46G0-H-IZHS-Y-](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780683636/Firmware__V5.9.14_260401_S3000712572.zip) | 2026-04-02 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780683636/Firmware__V5.9.14_260401_S3000712572.zip) |  Improved functionality Fix some known bugs and improve system stability. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202605/releasenote%5CG7-V5.9.1_Release_Note.pdf) |

</details>


<details>
<summary><h2>IDS-2CD7A46G2/V-XZHS(Y) - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.0 | Applied to: [IDS-2CD7A46G2/V-XZHS(Y)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780649800/Firmware__V5.8.0_260402_S3000713014.zip), [IDS-2CD7A46G2/V-XZHSY(2.8-12MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780649800/Firmware__V5.8.0_260402_S3000713014.zip), [IDS-2CD7A86G2/V-XZHS(Y)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780649800/Firmware__V5.8.0_260402_S3000713014.zip), [IDS-2CD7A86G2/V-XZHSY(2.8-12MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780649800/Firmware__V5.8.0_260402_S3000713014.zip) | 2026-04-02 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780649800/Firmware__V5.8.0_260402_S3000713014.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202605/releasenote%5C5.8.0_Release_Note.pdf) |

</details>


<details>
<summary><h2>IDS-2CD7A86G0-H-IZHS-Y- - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.9.1 | Applied to: [IDS-2CD7A86G0-H-IZHS-Y-](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780683636/Firmware__V5.9.14_260401_S3000712572.zip) | 2026-04-02 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780683636/Firmware__V5.9.14_260401_S3000712572.zip) |  Improved functionality Fix some known bugs and improve system stability. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202605/releasenote%5CG7-V5.9.1_Release_Note.pdf) |

</details>


<details>
<summary><h2>IDS-2CD7A86G0-H-IZHSY - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.9.1 | Applied to: [IDS-2CD7A86G0-H-IZHSY](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780683636/Firmware__V5.9.14_260401_S3000712572.zip) | 2026-04-02 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780683636/Firmware__V5.9.14_260401_S3000712572.zip) |  Improved functionality Fix some known bugs and improve system stability. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202605/releasenote%5CG7-V5.9.1_Release_Note.pdf) |

</details>


<details>
<summary><h2>IDS-2CD7AC5G0-H-IZHS-Y- - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.9.1 | Applied to: [IDS-2CD7AC5G0-H-IZHS-Y-](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780683636/Firmware__V5.9.14_260401_S3000712572.zip) | 2026-04-02 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780683636/Firmware__V5.9.14_260401_S3000712572.zip) |  Improved functionality Fix some known bugs and improve system stability. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202605/releasenote%5CG7-V5.9.1_Release_Note.pdf) |

</details>


<details>
<summary><h2>IDS-2CD8447G0/B-RS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.1 | Applied to: [IDS-2CD8447G0/B-RS](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.8.1_260330_S3000711487.zip), [IDS-2CD8447G0/B-RS(2.8MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.8.1_260330_S3000711487.zip), [IDS-2CD8447G0/B-RS(4MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.8.1_260330_S3000711487.zip) | 2026-03-30 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.8.1_260330_S3000711487.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202605/releasenote%5CNetwork_Camera_V5.8.1_Release_Note_--H9.pdf) |

</details>


<details>
<summary><h2>IDS-2CD8A46G0-IZ/UH - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.3 | Applied to: [IDS-2CD8A46G0-IZ/UH](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.3_260330_S3000712763.zip), [IDS-2CD8A46G0-IZ/UH(2.8-12MM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.3_260330_S3000712763.zip) | 2026-03-30 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.3_260330_S3000712763.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202605/releasenote%5CNetwork_Camera-V5.8.3_Release_Note-G5.pdf) |

</details>


<details>
<summary><h2>IDS-2CD8A46G2-XZHS(Y) - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.9.11 | Applied to: [IDS-2CD8A46G2-XZHS(Y)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.9.11_260330_S3000712752.zip), [IDS-2CD8A46G2-XZHS(0832/4)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.9.11_260330_S3000712752.zip), [IDS-2CD8A46G2-XZHSY(0832/4)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.9.11_260330_S3000712752.zip), [IDS-2CD8A86G2-XZHS(Y)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.9.11_260330_S3000712752.zip), [IDS-2CD8A86G2-XZHS(1050/4)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.9.11_260330_S3000712752.zip), [IDS-2CD8A86G2-XZHSY(1050/4)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.9.11_260330_S3000712752.zip) | 2026-03-30 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.9.11_260330_S3000712752.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202605/releasenote%5CH11_5.9.11_Release_Note.pdf) |

</details>


<details>
<summary><h2>IDS-2CD8A48G2-XZHS(Y) - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.9.22 | Applied to: [IDS-2CD8A48G2-XZHS(Y)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.9.22_260330_S3000711500.zip), [IDS-2CD8A48G2-XZHSY(1545/4)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.9.22_260330_S3000711500.zip), [IDS-2CD8A48G2-XZHS(1545/4)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.9.22_260330_S3000711500.zip) | 2026-03-30 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.9.22_260330_S3000711500.zip) | GPS function optimization · Fix some known bugs and improve system stability. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202605/releasenote%5CNetwork_Camera_V5.9.22_Release_Note_--H9.pdf) |

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
| 5.10.0 | Applied to: [IDS-2CD8V446G0/X2-XZHS(Y)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779753206/Firmware__V5.10.0_260423_S3000718071.zip), [IDS-2CD8V446G0/X2-XZHSY(1050/1050)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779753206/Firmware__V5.10.0_260423_S3000718071.zip)/O-STD, [IDS-2CD8V447G0E/X2-XZS](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779753206/Firmware__V5.10.0_260423_S3000718071.zip), [IDS-2CD8V447G0E/X2-XZS(4-6/4-6)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779753206/Firmware__V5.10.0_260423_S3000718071.zip), [IDS-2CD8V447G0E/X2-XZS(6-9/6-9)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779753206/Firmware__V5.10.0_260423_S3000718071.zip), [IDS-2CD8V886G0/X2-XZHS(Y)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779753206/Firmware__V5.10.0_260423_S3000718071.zip), [IDS-2CD8V886G0/X2-XZHSY(1050/1050)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779753206/Firmware__V5.10.0_260423_S3000718071.zip)/O-STD | 2026-04-23 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779753206/Firmware__V5.10.0_260423_S3000718071.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202605/releasenote%5CDeepinView_Dual-Lens_Omni_Camera_V5.10.0_Release_Note.pdf) |

</details>


<details>
<summary><h2>IDS-6708NXI-M1/X - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.04.051 | Applied to: [IDS-6708NXI-M1/X](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779870290/Firmware__V5.04.051_251218_S3000694433.zip), [IDS-6708NXI-M1/X(1×4T)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779870290/Firmware__V5.04.051_251218_S3000694433.zip), [IDS-6716NXI-M1/X](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779870290/Firmware__V5.04.051_251218_S3000694433.zip), [IDS-6716NXI-M1/X(1×8T)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779870290/Firmware__V5.04.051_251218_S3000694433.zip), [IDS-7608NXI-M2/8P/X](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779870290/Firmware__V5.04.051_251218_S3000694433.zip), [IDS-7608NXI-M2/X](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779870290/Firmware__V5.04.051_251218_S3000694433.zip), [IDS-7616NXI-M2/16P/X](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779870290/Firmware__V5.04.051_251218_S3000694433.zip), [IDS-7616NXI-M2/X](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779870290/Firmware__V5.04.051_251218_S3000694433.zip) | 2025-12-18 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779870290/Firmware__V5.04.051_251218_S3000694433.zip) | Modified functions · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5C5.04.051_build251218_ReleaseNotes.pdf) |

</details>


<details>
<summary><h2>IDS-7104HQHI-M1/S - DVR_V4 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 4.84.011 | Applied to: [IDS-7104HQHI-M1/S](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779907479/Firmware_Europe_V4.84.011_251217_S3000693333.zip), [IDS-7104HQHI-M1/S(C)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779907479/Firmware_Europe_V4.84.011_251217_S3000693333.zip), [IDS-7104HQHI-M1/S(E)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779907479/Firmware_Europe_V4.84.011_251217_S3000693333.zip), [IDS-7104HQHI-M1/T](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779907479/Firmware_Europe_V4.84.011_251217_S3000693333.zip), [IDS-7204HQHI-M1/E](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779907479/Firmware_Europe_V4.84.011_251217_S3000693333.zip), [IDS-7204HQHI-M1/E(E)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779907479/Firmware_Europe_V4.84.011_251217_S3000693333.zip), [IDS-7204HQHI-M1/T](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779907479/Firmware_Europe_V4.84.011_251217_S3000693333.zip) | 2025-12-17 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779907479/Firmware_Europe_V4.84.011_251217_S3000693333.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202410/releasenote%5CTurbo_HD_DVR_V4.75.013_build_240919_Release_Notes.pdf) |

</details>


<details>
<summary><h2>IDS-7108HQHI-M1/S - DVR_V4 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 4.84.011 | Applied to: [IDS-7108HQHI-M1/S](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779907479/Firmware_Europe_V4.84.011_251217_S3000693333.zip), [IDS-7108HQHI-M1/S(C)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779907479/Firmware_Europe_V4.84.011_251217_S3000693333.zip), [IDS-7108HQHI-M1/S(E)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779907479/Firmware_Europe_V4.84.011_251217_S3000693333.zip), [IDS-7208HQHI-M1/E](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779907479/Firmware_Europe_V4.84.011_251217_S3000693333.zip), [IDS-7208HQHI-M1/E(E)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779907479/Firmware_Europe_V4.84.011_251217_S3000693333.zip) | 2025-12-17 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779907479/Firmware_Europe_V4.84.011_251217_S3000693333.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202407/1719874945624/releasenote%5CTurbo_HD_DVR_V4.75.011_build_240620_Release_Notes.pdf) |

</details>


<details>
<summary><h2>IDS-7108HQHI-M1/T - DVR_V4 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 4.84.011 | Applied to: [IDS-7108HQHI-M1/T](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779907479/Firmware_Asia_V4.84.011_251217_S3000693357.zip), [IDS-7204HUHI-M1/T](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779907479/Firmware_Asia_V4.84.011_251217_S3000693357.zip), [IDS-7208HQHI-M1/T](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779907479/Firmware_Asia_V4.84.011_251217_S3000693357.zip) | 2025-12-17 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779907479/Firmware_Asia_V4.84.011_251217_S3000693357.zip) | Fix known defects to improve product stability. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202603/releasenote%5CTurbo_HD_DVR_V4.84.011build251217_Release_Notes.pdf) |

</details>


<details>
<summary><h2>IDS-7116HQHI-M1/S - DVR_V4 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 4.84.011 | Applied to: [IDS-7116HQHI-M1/S](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779907479/Firmware_Europe_V4.84.011_251217_S3000693414.zip), [IDS-7116HQHI-M1/S(E)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779907479/Firmware_Europe_V4.84.011_251217_S3000693414.zip), [IDS-7116HQHI-M1/S(F)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779907479/Firmware_Europe_V4.84.011_251217_S3000693414.zip), [IDS-7116HQHI-M1/T](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779907479/Firmware_Europe_V4.84.011_251217_S3000693414.zip), [IDS-7208HUHI-M1/T](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779907479/Firmware_Europe_V4.84.011_251217_S3000693414.zip), [IDS-7216HQHI-M1/E](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779907479/Firmware_Europe_V4.84.011_251217_S3000693414.zip), [IDS-7216HQHI-M1/E(F)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779907479/Firmware_Europe_V4.84.011_251217_S3000693414.zip), [IDS-7216HQHI-M1/T](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779907479/Firmware_Europe_V4.84.011_251217_S3000693414.zip) | 2025-12-17 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779907479/Firmware_Europe_V4.84.011_251217_S3000693414.zip) | improve product performance, and will take effect automatically after upgrading from previous versions. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202510/releasenote%5CTurbo_HD_DVR_V4.83.803build250903_Release_Notes.pdf) |

</details>


<details>
<summary><h2>IDS-7204HQHI-M1/XT - DVR_V4 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 4.84.011 | Applied to: [IDS-7204HQHI-M1/XT](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779907479/Firmware_Asia_V4.84.011_251217_S3000693376.zip) | 2025-12-17 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779907479/Firmware_Asia_V4.84.011_251217_S3000693376.zip) | Fix known defects to improve product stability. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202603/releasenote%5CTurbo_HD_DVR_V4.84.011build251217_Release_Notes.pdf) |

</details>


<details>
<summary><h2>IDS-7204HTHI-M1/XT - DVR_V4 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 4.84.011 | Applied to: [IDS-7204HTHI-M1/XT](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779907479/Firmware_Asia_V4.84.011_251217_S3000693370.zip), [IDS-7204HTHI-M2/XT](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779907479/Firmware_Asia_V4.84.011_251217_S3000693370.zip), [IDS-7208HTHI-M2/XT](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779907479/Firmware_Asia_V4.84.011_251217_S3000693370.zip), [IDS-7208HUHI-M1/XT](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779907479/Firmware_Asia_V4.84.011_251217_S3000693370.zip), [IDS-7208HUHI-M2/PXT](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779907479/Firmware_Asia_V4.84.011_251217_S3000693370.zip), [IDS-7208HUHI-M2/XT](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779907479/Firmware_Asia_V4.84.011_251217_S3000693370.zip), [IDS-7216HQHI-M1/XT](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779907479/Firmware_Asia_V4.84.011_251217_S3000693370.zip), [IDS-7216HQHI-M2/XT](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779907479/Firmware_Asia_V4.84.011_251217_S3000693370.zip) | 2025-12-17 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779907479/Firmware_Asia_V4.84.011_251217_S3000693370.zip) | Fix known defects to improve product stability. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202603/releasenote%5CTurbo_HD_DVR_V4.84.011build251217_Release_Notes.pdf) |

</details>


<details>
<summary><h2>IDS-7204HUHI-M1/PXT - DVR_V4 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 4.84.011 | Applied to: [IDS-7204HUHI-M1/PXT](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779907479/Firmware_Europe_V4.84.011_251217_S3000693403.zip), [IDS-7204HUHI-M1/XT](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779907479/Firmware_Europe_V4.84.011_251217_S3000693403.zip), [IDS-7204HUHI-M2/XT](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779907479/Firmware_Europe_V4.84.011_251217_S3000693403.zip), [IDS-7208HQHI-M1/XT](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779907479/Firmware_Europe_V4.84.011_251217_S3000693403.zip), [IDS-7208HQHI-M2/XT](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779907479/Firmware_Europe_V4.84.011_251217_S3000693403.zip) | 2025-12-17 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779907479/Firmware_Europe_V4.84.011_251217_S3000693403.zip) | Fix known defects to improve product stability. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202603/releasenote%5CTurbo_HD_DVR_V4.84.011build251217_Release_Notes.pdf) |

</details>


<details>
<summary><h2>IDS-TCC446-HI - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.3.0 | Applied to: [IDS-TCC446-HI](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780563030/Firmware__V5.3.0_260506_S3000720247.zip), [IDS-TCC446-HI/23](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780563030/Firmware__V5.3.0_260506_S3000720247.zip) | 2026-05-06 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780563030/Firmware__V5.3.0_260506_S3000720247.zip) | — |

</details>


<details>
<summary><h2>IDS-TCD403-BI - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.0 | Applied to: [IDS-TCD403-BI](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780599961/Firmware__V5.5.0_260420_S3000720736.zip), [IDS-TCD403-BI(G)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780599961/Firmware__V5.5.0_260420_S3000720736.zip)/POE/0832 | 2026-04-20 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780599961/Firmware__V5.5.0_260420_S3000720736.zip) | — |

</details>


<details>
<summary><h2>IDS-TCM403-B - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.0 | Applied to: [IDS-TCM403-B](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780599961/Firmware__V5.5.0_260420_S3000720758.zip), [[[IDS-TCM403-B(G)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780599961/Firmware__V5.5.0_260420_S3000720758.zip)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780599961/Firmware__V5.5.0_260420_S3000720758.zip)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780599961/Firmware__V5.5.0_260420_S3000720758.zip)/POE/0832, IDS-TCM403-B(G)/POE/2812, IDS-TCM403-B(G)/POE/1050, [IDS-TCM403-BI](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780599961/Firmware__V5.5.0_260420_S3000720758.zip), [[[IDS-TCM403-BI(G)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780599961/Firmware__V5.5.0_260420_S3000720758.zip)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780599961/Firmware__V5.5.0_260420_S3000720758.zip)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780599961/Firmware__V5.5.0_260420_S3000720758.zip)/G/POE/0832, IDS-TCM403-BI(G)/Y/G/POE/0832, IDS-TCM403-BI(G)/POE/0832 | 2026-04-20 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780599961/Firmware__V5.5.0_260420_S3000720758.zip) | — |

</details>


<details>
<summary><h2>IDS-TCS900-HI - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.4.0 | Applied to: [IDS-TCS900-HI](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780081037/Firmware__V5.4.0_251023_S3000680319.zip), [IDS-TCS900-HI/1140/H1(AF)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780081037/Firmware__V5.4.0_251023_S3000680319.zip)(24V), [IDS-TCS907-HIR](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780081037/Firmware__V5.4.0_251023_S3000680319.zip) | 2025-10-23 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780081037/Firmware__V5.4.0_251023_S3000680319.zip) | — |

</details>


<details>
<summary><h2>IDS-TCV500-HE - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.0 | Applied to: [IDS-TCV500-HE](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780599961/Firmware__V5.5.0_260420_S3000720739.zip), [IDS-TCV500-HE/1140/H1(AF)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780599961/Firmware__V5.5.0_260420_S3000720739.zip), [IDS-TCV500-HI](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780599961/Firmware__V5.5.0_260420_S3000720739.zip), [[IDS-TCV500-HI/1140/H1(AF)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780599961/Firmware__V5.5.0_260420_S3000720739.zip)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780599961/Firmware__V5.5.0_260420_S3000720739.zip)(24V), IDS-TCV500-HI/1140/H1(AF), [IDS-TCV507-HER](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780599961/Firmware__V5.5.0_260420_S3000720739.zip), [IDS-TCV507-HER/150M/1140(AF)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780599961/Firmware__V5.5.0_260420_S3000720739.zip), [IDS-TCV507-HIR](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780599961/Firmware__V5.5.0_260420_S3000720739.zip) | 2026-04-20 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780599961/Firmware__V5.5.0_260420_S3000720739.zip) | — |

</details>


<details>
<summary><h2>IDS-TCV900-HE - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.0 | Applied to: [IDS-TCV900-HE](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780599961/Firmware__V5.5.0_260420_S3000720727.zip), [IDS-TCV900-HE/1140/H1(AF)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780599961/Firmware__V5.5.0_260420_S3000720727.zip), [IDS-TCV900-HE/25/H1](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780599961/Firmware__V5.5.0_260420_S3000720727.zip), [IDS-TCV900-HI](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780599961/Firmware__V5.5.0_260420_S3000720727.zip), [IDS-TCV900-HI/1140/H1(AF)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780599961/Firmware__V5.5.0_260420_S3000720727.zip), [IDS-TCV900-HI/25/H1](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780599961/Firmware__V5.5.0_260420_S3000720727.zip), [IDS-TCV900-HI/25/H1(24V)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780599961/Firmware__V5.5.0_260420_S3000720727.zip), [IDS-TCV907-HER](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780599961/Firmware__V5.5.0_260420_S3000720727.zip) | 2026-04-20 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780599961/Firmware__V5.5.0_260420_S3000720727.zip) | — |

</details>


<details>
<summary><h2>IDS-TCVC00-HE - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.0 | Applied to: [IDS-TCVC00-HE](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780599961/Firmware__V5.5.0_260420_S3000720742.zip), [IDS-TCVC00-HE/1140/H1(AF)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780599961/Firmware__V5.5.0_260420_S3000720742.zip), [IDS-TCVC00-HI](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780599961/Firmware__V5.5.0_260420_S3000720742.zip), [IDS-TCVC00-HI/1140/H1(AF)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780599961/Firmware__V5.5.0_260420_S3000720742.zip), [IDS-TCVC00-HI/1140(AF)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780599961/Firmware__V5.5.0_260420_S3000720742.zip), [IDS-TCVC07-HER](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780599961/Firmware__V5.5.0_260420_S3000720742.zip), [IDS-TCVC07-HER/1140(AF)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780599961/Firmware__V5.5.0_260420_S3000720742.zip), [IDS-TCVC07-HIR](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780599961/Firmware__V5.5.0_260420_S3000720742.zip) | 2026-04-20 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780599961/Firmware__V5.5.0_260420_S3000720742.zip) | — |

</details>


<details>
<summary><h2>IDS-TCVK00-HE - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.0 | Applied to: [IDS-TCVK00-HE](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780599961/Firmware__V5.5.0_260420_S3000720731.zip), [IDS-TCVK00-HE/1140/H1(AF)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780599961/Firmware__V5.5.0_260420_S3000720731.zip), [IDS-TCVK00-HI](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780599961/Firmware__V5.5.0_260420_S3000720731.zip), [IDS-TCVK00-HI/1140(AF)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780599961/Firmware__V5.5.0_260420_S3000720731.zip), [IDS-TCVK00-HI/1140/H1(AF)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780599961/Firmware__V5.5.0_260420_S3000720731.zip), [IDS-TCVK07-HER](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780599961/Firmware__V5.5.0_260420_S3000720731.zip), [IDS-TCVK07-HER/1140(AF)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780599961/Firmware__V5.5.0_260420_S3000720731.zip), [IDS-TCVK07-HER/150M/1140(AF)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780599961/Firmware__V5.5.0_260420_S3000720731.zip) | 2026-04-20 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780599961/Firmware__V5.5.0_260420_S3000720731.zip) | — |

</details>


<details>
<summary><h2>IDS-TVJ860-GIR - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.6 | Applied to: [IDS-TVJ860-GIR](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780043044/Firmware__V5.5.6_251107_S3000707557.zip), [IDS-TVJ870-Z/E/WZ(SYSCOM)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780043044/Firmware__V5.5.6_251107_S3000707557.zip) | 2025-11-07 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780043044/Firmware__V5.5.6_251107_S3000707557.zip) | — |

</details>


<details>
<summary><h2>IK-4142TH-MH/P - IPC_E3S (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.25 | Applied to: IK-4142TH-MH/P, [DS-J142I](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.7.25_260401_S3000715096.zip), [DS-J142I/IK-4142TH-MH/P(D)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.7.25_260401_S3000715096.zip), IPC-B129H, IPC-B129H(2.8MM)(C)(HILOOKSTD), IPC-B129H(4MM)(C)(HILOOKSTD), IPC-B140H(-M), IPC-B140H(2.8MM)(HILOOKSTD) | 2026-04-01 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.7.25_260401_S3000715096.zip) | Mic, support the Third Stream of 720P 1fps, HLC, Line Crossing Detection, Intrusion Detection; · Support reset password via E-mail on SADP , iVMS4200 and Hik-Connect, set the reserved · E-mail address when active camera; · External · [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202312/releasenote%5CIPC_E3S_5.5.84_Release_Note--External.pdf) |

</details>


<details>
<summary><h2>IKS-2042BH-PH/W - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.23 | Applied to: IKS-2042BH-PH/W, [DS-J142I](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780649800/Firmware__V5.8.23_260403_S3000712854.zip), IKS-2042BPH-PH/W, IKS-2042BTH-PH/W, IPC-CFW02(/EU), IPC-CFW02(2.8MM)(HILOOKSTD)/EU, IPC-CFW02(4MM)(HILOOKSTD)/EU | 2026-04-03 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780649800/Firmware__V5.8.23_260403_S3000712854.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202509/releasenote%5CNVS_V4.32.205_250811__V4.32.401_250811_ReleaseNotes.pdf) |

</details>


<details>
<summary><h2>IKS-2044BPH-PH/W - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.23 | Applied to: IKS-2044BPH-PH/W, [DS-J142I](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780649800/Firmware__V5.8.23_260403_S3000712854.zip), IKS-2044BTH-PH/W, IPC-CFW04(/EU), IPC-CFW04(2.8MM)(HILOOKSTD)/EU, IPC-CFW04(4MM)(HILOOKSTD)/EU | 2026-04-03 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780649800/Firmware__V5.8.23_260403_S3000712854.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202509/releasenote%5CNVS_V4.32.205_250811__V4.32.401_250811_ReleaseNotes.pdf) |

</details>


<details>
<summary><h2>IPC-B120HA - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.41 | Applied to: IPC-B120HA, IPC-B120HA(2.8MM)(HILOOKSTD), IPC-B120HA(4MM)(HILOOKSTD), IPC-B120HA-LU, IPC-B120HA-LU(2.8MM)(HILOOKSTD), IPC-B120HA-LU(4MM)(HILOOKSTD), IPC-B129HA, IPC-B129HA(2.8MM)(HILOOKSTD) | 2026-04-01 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.8.41_260401_S3000712568.zip) | Fixed some bugs to enhance system stability. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202604/releasenote%5CNetwork_Camera-V5.8.41_SP1_Release_Note-E9.pdf) |

</details>


<details>
<summary><h2>IPC-B120HA-LUF/SL - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.41 | Applied to: IPC-B120HA-LUF/SL, IPC-B120HA-LUF/SL(2.8MM)(HILOOKSTD), IPC-B120HA-LUF/SL(4MM)(HILOOKSTD), IPC-B129HA-LU, IPC-B129HA-LU(2.8MM)(HILOOKSTD), IPC-B129HA-LU(4MM)(HILOOKSTD), IPC-B129HA-LUF/S(L)(RB), IPC-B129HA-LUF/SRB(2.8MM)(HILOOKSTD) | 2026-04-01 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.8.41_260401_S3000712568.zip) | Fixed some bugs to enhance system stability. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202604/releasenote%5CNetwork_Camera-V5.8.41_260401_Release_Note-E9.pdf) |

</details>


<details>
<summary><h2>IPC-B120HAA-LU(F)(/SX) - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.9.15 | Applied to: IPC-B120HAA-LU(F)(/SX), IPC-B120HAA-LU(2.8MM)(HILOOKSTD), IPC-B120HAA-LU(4MM)(HILOOKSTD), IPC-B140HAA-LU(F)(/SX), IPC-B140HAA-LU(2.8MM)(HILOOKSTD), IPC-B140HAA-LU(4MM)(HILOOKSTD), IPC-B420HAA-LU(F)(/SX), IPC-B420HAA-LU(2.8MM)(HILOOKSTD) | 2026-05-08 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780563030/Firmware__V5.9.15_260508_S3000721710.zip) | Animal detection is newly supported, with detection targets including large animals (horses, sheep, · cattle, etc.), small animals (cats, dogs), and poultry (birds). By default, it is not selected and needs to · be manually enabled. It supports SMART events such as intrusion detection. · The 1XX3 and 3XX1G3(E) series products are newly added. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202606/releasenote%5CNetwork_Camera-V5.9.15_260508_Release_IPCE_E_E15.pdf) |

</details>


<details>
<summary><h2>IPC-B129HAA-LU(F)(/SL)(/SRB) - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.9.14 | Applied to: IPC-B129HAA-LU(F)(/SL)(/SRB), IPC-B129HAA-LU(2.8MM)(HILOOKSTD), IPC-B129HAA-LU(4MM)(HILOOKSTD), IPC-B129HAA-LUF/SL(2.8MM)(HILOOKSTD), IPC-B129HAA-LUF/SL(4MM)(HILOOKSTD), IPC-B129HAA-LUF/SRB(2.8MM)(HILOOKSTD), IPC-B129HAA-LUF/SRB(4MM)(HILOOKSTD), IPC-B149HAA-LU(F)(/SL)(/SRB) | 2026-04-01 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780683636/Firmware__V5.9.14_260401_S3000712572.zip) | — |

</details>


<details>
<summary><h2>IPC-B140HA - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.41 | Applied to: IPC-B140HA, IPC-B140HA(2.8MM)(HILOOKSTD), IPC-B140HA(4MM)(HILOOKSTD), IPC-B140HA-LU, IPC-B140HA-LU(2.8MM)(HILOOKSTD), IPC-B140HA-LU(4MM)(HILOOKSTD), IPC-B149HA, IPC-B149HA(2.8MM)(HILOOKSTD) | 2026-04-01 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.8.41_260401_S3000712569.zip) | 1. Fixed some bugs to enhance system stability. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202604/releasenote%5CNetwork_Camera-V5.8.41_SP1_Release_Note-E10.pdf) |

</details>


<details>
<summary><h2>IPC-B140HA-LUF/SL - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.41 | Applied to: IPC-B140HA-LUF/SL, IPC-B140HA-LUF/SL(2.8MM)(HILOOKSTD), IPC-B140HA-LUF/SL(4MM)(HILOOKSTD), IPC-B140HAP-LUF/SL, IPC-B140HAP-LUF/SL(2.8MM)(HILOOKSTD), IPC-B140HAP-LUF/SL(4MM)(HILOOKSTD), IPC-B149HA-LU, IPC-B149HA-LU(2.8MM)(HILOOKSTD) | 2026-04-01 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.8.41_260401_S3000712568.zip) | 1. Fixed some bugs to enhance system stability. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202604/releasenote%5CNetwork_Camera-V5.8.41_SP1_Release_Note-E10.pdf) |

</details>


<details>
<summary><h2>IPC-B160HA-LU - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.41 | Applied to: IPC-B160HA-LU, IPC-B160HA-LU(2.8MM)(HILOOKSTD), IPC-B160HA-LU(4MM)(HILOOKSTD), IPC-B160HA-LUF/SL, IPC-B160HA-LUF/SL(2.8MM)(HILOOKSTD), IPC-B160HA-LUF/SL(4MM)(HILOOKSTD), IPC-B160HAP-LUF/SL, IPC-B160HAP-LUF/SL(2.8MM)(HILOOKSTD) | 2026-04-01 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.8.41_260401_S3000712568.zip) | 1. Fixed some bugs to enhance system stability. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202604/releasenote%5CNetwork_Camera-V5.8.41_SP1_Release_Note-G6.pdf) |

</details>


<details>
<summary><h2>IPC-B460HAD-LUF/S(L)(RB) - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.12 | Applied to: IPC-B460HAD-LUF/S(L)(RB), IPC-B460HAD-LUF/SL(2.8MM)(HILOOKSTD), IPC-B460HAD-LUF/SRB(2.8MM)(HILOOKSTD), IPC-B469HAD-LUF/S(L)(RB), IPC-B469HAD-LUF/SRB(2.8MM)(HILOOKSTD), IPC-B469HAD-LUF/SL(2.8MM)(HILOOKSTD), IPC-B480HAD-LUF/S(L)(RB), IPC-B480HAD-LUF/SL(2MM)(HILOOKSTD) | 2026-04-16 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780617965/Firmware__V5.8.12_260407_S3000714560.zip) | some bugs to enhance system stability. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202605/releasenote%5CNetwork_Camera-V5.8.12_260416_Release_IPCE_P_E11.pdf) |

</details>


<details>
<summary><h2>IPC-B640H-Z - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.89 | Applied to: IPC-B640H-Z, IPC-B640H-Z(2.8-12MM)(HILOOKSTD), IPC-B640H-V(2.8-12MM)(HILOOKSTD), IPC-B640H-Z(2.8-12MM)(C)(HILOOKSTD), IPC-D640H-Z, IPC-D640H-Z(2.8-12MM)(HILOOKSTD), IPC-D640H-Z(2.8-12MM)(C)(HILOOKSTD), IPC-D650H-Z | 2026-04-01 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.7.25_260401_S3000715096.zip) | Improved Features · After the device is upgraded to V5.5.89 version, it cannot be upgraded back to a version lower · than V5.5.89. · [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202312/releasenote%5CNetwork_Camera_V5.5.89_Release_Note_--G0.pdf) |

</details>


<details>
<summary><h2>IPC-CFW06-P - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.10 | Applied to: IPC-CFW06-P, IPC-CFW06-P(2.8MM)(HILOOKSTD)/EU | 2026-03-30 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.10_260330_S3000712749.zip) | — |

</details>


<details>
<summary><h2>ISD-CA6040S-C - UNKNOWN (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.0 | Applied to: ISD-CA6040S-C, ISD-CA6040S-C(220V), ISD-CA6040S-C(110V), ISD-CA6040S-H, ISD-CA6040S-H(220V), ISD-CA6040S-H(110V), ISD-CA6040S-H(BS), ISD-CA6040S-H(BS)(220V) | 2026-04-07 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780649800/Firmware__V5.8.0_260402_S3000712887.zip) | — |
| 5.7.210 | Applied to: ISD-CA6040S-C, ISD-CA6040S-C(220V), ISD-CA6040S-C(110V), ISD-CA6040S-H, ISD-CA6040S-H(220V), ISD-CA6040S-H(110V), ISD-CA6040S-H(BS), ISD-CA6040S-H(BS)(220V) | 2026-04-02 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780683636/Firmware__V5.7.210_260402_S3000713546.zip) | — |

</details>


<details>
<summary><h2>ISD-SMG318L - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 1.2.8 | Applied to: ISD-SMG318L, ISD-SMG133L, ISD-SMG333L, ISD-SMG572L, ISD-SMG572LC-I | 2026-05-09 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779750762/Firmware__V1.2.8_260509_S3000723501.zip) | — |

</details>


<details>
<summary><h2>ISD-SMG924L-H(C) - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 1.2.0 | Applied to: ISD-SMG924L-H(C) | 2026-03-20 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780531020/Firmware__V1.2.0_251022_S3000681572.zip) | — |

</details>


<details>
<summary><h2>NVR-104MH-K - NVR_V4 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 4.84.101 | Applied to: NVR-104MH-K, HL-NVR-104MH-K, NVR-104MH-K/4P, HL-NVR-104MH-K/4P, NVR-108MH-K, HL-NVR-108MH-K, NVR-108MH-K/8P, HL-NVR-108MH-K/8P | 2025-12-12 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779956347/Firmware__V4.84.101_251212_S3000693705.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CEUI_NVR_V4.84.101_251212_ReleaseNote.pdf) |

</details>


<details>
<summary><h2>NVR-104MH-Q/W - NVR_V4 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 4.85.001 | Applied to: NVR-104MH-Q/W, NVR-108MH-Q/W | 2025-12-11 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779956347/Firmware__V4.85.001_251211_S3000693151.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CEUI_NVR_V4.85.001_251211_ReleaseNote.pdf) |

</details>


<details>
<summary><h2>PTZ-N2204I-DE3 - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.9.5 | Applied to: PTZ-N2204I-DE3, PTZ-N2204I-DE3(HILOOKSTD), PTZ-N2204I-DE3(HILOOKSTD)(G), PTZ-N2404I-DE3, PTZ-N2404I-DE3(HILOOKSTD)(G), PTZ-N4215-DE3, PTZ-N4215-DE3(HILOOKSTD), PTZ-N4215-DE3(HILOOKSTD)(J) | 2026-04-16 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780649800/Firmware__V5.9.51_260403_S3000712992.zip) | 1. Algorithm optimization and updates. 2. Fix some bugs. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202507/releasenote%5CRelease_Note.pdf) |

</details>


<details>
<summary><h2>PTZ-N2404I-DE3 - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.11 | Applied to: PTZ-N2404I-DE3, PTZ-N2404I-DE3(HILOOKSTD)(F), PTZ-N2404I-DE3(HILOOKSTD)(G), PTZ-N4215-DE3, PTZ-N4215-DE3(HILOOKSTD), PTZ-N4215-DE3(HILOOKSTD)(C), PTZ-N4215-DE3(HILOOKSTD)(J), PTZ-N4215I-DE | 2026-04-02 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780683636/Firmware__V5.7.11_260402_S3000713041.zip) | Algorithm optimization and updates. 2. Fix some bugs. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202604/releasenote%5CV5.9.5_260416_Release_Note.pdf) |

</details>


<details>
<summary><h2>PTZ-N2C200C-D/4G - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.11 | Applied to: PTZ-N2C200C-D/4G, PTZ-N2C200C-D/4G(2.8MM)(HILOOKSTD)/EU, PTZ-N2C200C-D/4G(4MM)(HILOOKSTD)/EU | 2026-04-09 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780599961/Firmware__V5.8.110_260421_S3000718008.zip) | some bugs to enhance system stability. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202605/releasenote%5CNetwork_Camera-V5.8.11_260409Release_IPDE_E9.pdf) |

</details>


<details>
<summary><h2>PTZ-N2C600M-DE - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.1 | Applied to: PTZ-N2C600M-DE, PTZ-N2C600M-DE(2.8MM)(HILOOKSTD), PTZ-N2C600M-DE(4MM)(HILOOKSTD) | 2026-03-26 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.8.1_260330_S3000711487.zip) | some bugs to enhance system stability. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202605/releasenote%5CNetwork_Camera-V5.8.1_260326_Release_Note.pdf) |

</details>


<details>
<summary><h2>PTZ-N2D200M-DE/12 - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.4 | Applied to: PTZ-N2D200M-DE/12, PTZ-N2D200M-DE/12(2.8/8MM)(HILOOKSTD), PTZ-N2D400M-DE/14, PTZ-N2D400M-DE/14(2.8/8MM)(HILOOKSTD) | 2026-03-25 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1780769282/Firmware__V5.8.41_260401_S3000712568.zip) | — |

</details>


<details>
<summary><h2>PTZ-N4215I-DE - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.30 | Applied to: PTZ-N4215I-DE, PTZ-N4215I-DE(HILOOKSTD)(F), PTZ-N4215I-DE(HILOOKSTD)(H), PTZ-N4215I-DE(HILOOKSTD)(J), PTZ-N4225I-DE, PTZ-N4225I-DE(HILOOKSTD)(E), PTZ-N4225I-DE(HILOOKSTD)(F), PTZ-N4225I-DE(HILOOKSTD)(H) | 2026-03-28 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.30_260328_S3000711533.zip) | Algorithm optimization and updates. 2. Fix some bugs. · [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202604/releasenote%5CV5.9.5_260416_Release_Note.pdf) |

</details>


<details>
<summary><h2>THC-B120-C - THERMAL_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 1.10.03 | Applied to: THC-B120-C, THC-B120-C(2.8MM)(HILOOK STD), THC-B120-C(3.6MM)(HILOOK STD), THC-B120-PC, THC-B120-PC(2.8MM)(HILOOK STD) | 2025-12-11 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779956347/Firmware__V1.10.03_251211_S3000692842.zip) | — |

</details>


<details>
<summary><h2>THC-B123-M - THERMAL_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 1.09.01 | Applied to: THC-B123-M, THC-B123-M(2.8MM)(HILOOK STD), THC-B123-M(3.6MM)(HILOOK STD), THC-B223-M, THC-B223-M(2.8MM)(HILOOK STD), THC-B223-M(3.6MM)(HILOOK STD), THC-B223-M(6MM)(HILOOK STD), THC-T123-M | 2026-01-07 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/download/1779782863/Firmware__V1.09.01_260107_S3000700979.zip) | — |

</details>
