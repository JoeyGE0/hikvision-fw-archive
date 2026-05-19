# Hikvision Firmware Archive

An unofficial archive of Hikvision camera and NVR firmware files, maintained for historical reference and firmware rollback purposes.

- [About](#about)
- [Why This Exists](#why-this-exists)
- [How It Works](#how-it-works)
- [Using This Archive](#using-this-archive)
- [Important Warnings](#important-warnings)
- [Contributing](#contributing)
- [Firmware List](#firmware-list)

## About

This repository contains an automated collection of Hikvision firmware download links scraped from their official download center. Hikvision only displays the latest firmware for each device on their website, making it difficult to access older versions for rollback or troubleshooting purposes.

## Why This Exists

Hikvision's download center has a few limitations:

- **Only latest firmware shown**: Once a new firmware is released, older versions disappear from the official site
- **No version history**: There's no way to see what firmware versions existed for your device
- **Rollback difficulty**: If a new firmware causes issues, you can't easily downgrade without having saved the previous version
- **Hardware version confusion**: Matching firmware to your exact hardware version can be tricky
- **Scattered sources**: Firmware links are spread across different regional sites and support pages

This archive solves these problems by maintaining a searchable database of firmware versions with direct download links.

## How It Works

This archive is automatically updated twice daily (4:20 AM and PM UTC) by scraping Hikvision's download center. The scraper:

1. Searches for firmware files across Hikvision's product categories
2. Extracts model numbers, hardware versions, firmware versions, and release dates
3. Stores download links and metadata in JSON files
4. Generates this README with an organized firmware list
5. Creates GitHub releases when new firmwares are discovered

All data is stored in JSON format:

- `devices.json` - Device model and hardware version mappings
- `firmwares_live.json` - Firmwares scraped from Hikvision's website
- `firmwares_manual.json` - Manually added firmwares (betas, archived links, etc.)
- `firmware_info.json` - Additional metadata about firmware files

## Using This Archive

### Finding Firmware

1. **Search for your device model** (e.g., `DS-2CD2XXX`)
2. **Match your hardware version** - This is critical! Installing wrong firmware can brick your device
3. **Check the version and date** - Newer versions are listed first
4. **Click the download link** - Most links go directly to Hikvision's servers

### Device Model Format

Hikvision uses a consistent naming scheme:

- **DS-2CD** - IP Cameras (fixed)
- **DS-2DE** - PTZ Cameras
- **DS-76XX** - NVRs (various series)
- **DS-77XX** - NVRs (various series)
- **DS-86XX** - NVRs (various series)

### Hardware Versions

Hardware versions are critical for compatibility:

- Usually shown in device web interface under "Device Information"
- Format varies: `IPC_G0`, `IPC_XXX`, `NVR_XXX`, etc.
- Some devices show abbreviated versions (last few characters may be missing)
- **Always verify hardware version matches before flashing**

## Important Warnings

⚠️ **Read this before flashing firmware:**

1. **Hardware version must match** - Wrong firmware can permanently damage your device
2. **Beta firmwares are marked** - Use at your own risk, may be unstable
3. **Backup first** - Always backup your device configuration before updating
4. **Power stability** - Ensure stable power during firmware update (use UPS if possible)
5. **No warranty** - This is an unofficial archive, use at your own risk
6. **Regional differences** - Some firmwares may be region-specific
7. **Link validity** - Download links may expire or change without notice

### Firmware Installation Tips

- Use Hikvision's official tools (SADP, iVMS-4200) when possible
- Some devices require firmware files to be renamed (check device documentation)
- If firmware upload fails, try:
  - Renaming the file
  - Using TFTP recovery method
  - Contacting Hikvision support

## Contributing

Contributions are welcome! Here's how you can help:

### Reporting Missing Firmwares

If you know of a firmware that's not in this archive:

1. Check `missing.txt` - Add the model and version if not already listed
2. Open an issue with:
   - Device model and hardware version
   - Firmware version
   - Download link (if you have it)
   - Source (official site, support email, etc.)

### Adding Firmwares Manually

You can manually add firmwares using the command-line tool:

```bash
python main.py add "https://example.com/firmware.dav" \
  --model "DS-2CD2XXX" \
  --hw-version "IPC_G0" \
  --version "5.7.0" \
  --date "2023-01-15" \
  --changes "Bug fixes and stability improvements" \
  --notes "Official release from Hikvision support"
```

### Improving the Scraper

The scraper in `main.py` can always be improved:

- Better model/version detection
- Support for more product categories
- Handling edge cases and different page layouts
- Rate limiting and error handling improvements

### Editing Documentation

- **Don't edit `README.md` directly** - It's auto-generated
- Edit `readme_header.md` for changes to the header section
- The firmware list is generated automatically from JSON files

## Status

**Status:** ✅ SUCCESS  
**Last Run:** 2026-05-19 08:18:47 UTC  
**Scraper:** HTTP  
**Firmwares Found:** 1632  
**New Firmwares:** 65  
**Test Mode:** Disabled



---

## Firmware List

Below is the complete list of archived firmwares, organized by device model and hardware version.

**Total: 1632**



<details>
<summary><h2>AE-AC1130-A - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 3.6.1 | Applied to: [AE-AC1130-A/GA(V3.0)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V3.6.1_220818_S3000450312.zip)(LatinAmerica)/B | 2022-08-18 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V3.6.1_220818_S3000450312.zip) |  |

</details>


<details>
<summary><h2>AE-DC2015-B1 - UNKNOWN (6 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 1.1.5 | Applied to: [AE-DC2015-B1](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V1.1.5_220421_S3000442625.zip) | 2022-04-21 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V1.1.5_220421_S3000442625.zip) |  |
| 1.1.3 | Applied to: [AE-DC2015-B1](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V1.1.3_250304_S3000634438.zip) | 2021-11-16 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V1.1.3_250304_S3000634438.zip) |  |
| 1.1.4 | Applied to: [AE-DC2015-B1](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V1.1.4_220725_S3000443106.zip) | 2021-08-11 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V1.1.4_220725_S3000443106.zip) |  |
| 1.1.2 | Applied to: [AE-DC2015-B1](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V1.1.2_200828_S3000334190.zip) | 2020-09-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V1.1.2_200828_S3000334190.zip) |  |
| 1.0.8 | Applied to: [AE-DC2015-B1](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V1.0.8_200320_S3000313276.zip) | 2020-03-20 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V1.0.8_200320_S3000313276.zip) |  |
| 1.0.6 | Applied to: [AE-DC2015-B1](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V1.0.6_191031_S3000312642.zip) | 2019-10-31 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V1.0.6_191031_S3000312642.zip) |  |

</details>


<details>
<summary><h2>AE-DC2022-V200 - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 1.0.10 | Applied to: [AE-DC2022-V200(2CH)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V1.0.10_250902_S3000672017.zip) | 2025-09-02 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V1.0.10_250902_S3000672017.zip) |  |

</details>


<details>
<summary><h2>AE-DC2032-V300 - UNKNOWN (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 1.0.10 | Applied to: [AE-DC2032-V300(3CH)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V1.0.10_250902_S3000671476.zip) | 2025-09-02 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V1.0.10_250902_S3000671476.zip) |  |
| 1.0.3 | Applied to: [AE-DC2032-V300(3CH)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V1.0.3_250328_S3000641095.zip) | 2025-03-28 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V1.0.3_250328_S3000641095.zip) |  |

</details>


<details>
<summary><h2>AE-DC4328-K5 - UNKNOWN (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 1.0.7 | Applied to: [AE-DC4328-K5(2CH)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V1.0.7_230605_S3000521095.zip) | 2023-06-05 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V1.0.7_230605_S3000521095.zip) |  |
| 3.0.1 | Applied to: [AE-DC4328-K5(2CH)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V3.0.1_230306_S3000485364.zip) | 2023-04-10 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V3.0.1_230306_S3000485364.zip) |  |

</details>


<details>
<summary><h2>AE-DC5013-F6 - UNKNOWN (5 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 1.3.2 | Applied to: [AE-DC5013-F6](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V1.1.3_250304_S3000634438.zip) | 2022-04-20 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V1.1.3_250304_S3000634438.zip) |  |
| 1.3.0 | Applied to: [AE-DC5013-F6](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V1.3.0_210822_S3000384053.zip) | 2021-11-10 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V1.3.0_210822_S3000384053.zip) |  |
| 1.2.7 | Applied to: [AE-DC5013-F6](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/DashCam_AE_DC5013_F6_CN_STD_V1.2.7_build210409.zip) | 2021-04-09 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/DashCam_AE_DC5013_F6_CN_STD_V1.2.7_build210409.zip) |  |
| 1.2.5 | Applied to: [AE-DC5013-F6](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/DashCam_AE_DC5013_F6_CN_STD_V1.2.5_build200827.zip) | 2020-08-27 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/DashCam_AE_DC5013_F6_CN_STD_V1.2.5_build200827.zip) |  |
| 1.2.1 | Applied to: [AE-DC5013-F6](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/DashCam_AE_DC5013_F6_CN_STD_V1.2.1_build200703.zip) | 2020-07-03 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/DashCam_AE_DC5013_F6_CN_STD_V1.2.1_build200703.zip) |  |

</details>


<details>
<summary><h2>AE-DC5013-F6PRO - UNKNOWN (3 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 1.3.4 | Applied to: [AE-DC5013-F6PRO](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V1.3.4_S3000653240.zip) | 2023-09-19 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V1.3.4_S3000653240.zip) |  |
| 1.3.2 | Applied to: [AE-DC5013-F6PRO](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V1.1.3_250304_S3000634438.zip) | 2022-04-20 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V1.1.3_250304_S3000634438.zip) |  |
| 1.3.0 | Applied to: [AE-DC5013-F6PRO](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/DashCam_AE_DC5013_F6_CN_STD_V1.3.0_build210625.zip) | 2021-06-25 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/DashCam_AE_DC5013_F6_CN_STD_V1.3.0_build210625.zip) |  |

</details>


<details>
<summary><h2>AE-DC5113-F6S - UNKNOWN (5 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 1.3.2 | Applied to: [AE-DC5113-F6S](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V1.1.3_250304_S3000634438.zip) | 2022-09-28 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V1.1.3_250304_S3000634438.zip) |  |
| 1.3.0 | Applied to: [AE-DC5113-F6S](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V1.3.0_210822_S3000384053.zip) | 2021-08-22 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V1.3.0_210822_S3000384053.zip) |  |
| 1.2.8 | Applied to: [AE-DC5113-F6S](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V1.2.8_210513_S3000365428.zip) | 2021-05-13 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V1.2.8_210513_S3000365428.zip) |  |
| 1.2.6 | Applied to: [AE-DC5113-F6S](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V1.2.6_200820_S3000332869.zip) | 2020-08-20 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V1.2.6_200820_S3000332869.zip) |  |
| 1.2.3 | Applied to: [AE-DC5113-F6S](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V1.2.3_230605_S3000503831.zip) | 2020-05-25 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V1.2.3_230605_S3000503831.zip) |  |

</details>


<details>
<summary><h2>AE-DC5313-C6 - UNKNOWN (3 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 1.2.4 | Applied to: [AE-DC5313-C6](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V1.2.4_220629_S3000442951.zip) | 2022-12-09 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V1.2.4_220629_S3000442951.zip) |  |
| 1.1.6 | Applied to: [AE-DC5313-C6](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V1.1.6_220920_S3000456100.zip) | 2022-09-20 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V1.1.6_220920_S3000456100.zip) |  |
| 1.1.10 | Applied to: [AE-DC5313-C6](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/DashCam_AE_DC5313_C6_CN_STD_V1.1.10_build220223.zip) | 2022-02-23 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/DashCam_AE_DC5313_C6_CN_STD_V1.1.10_build220223.zip) |  |

</details>


<details>
<summary><h2>AE-DC5313-C6PRO - UNKNOWN (3 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 1.2.4 | Applied to: [AE-DC5313-C6PRO](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V1.2.4_220629_S3000442951.zip) | 2022-12-09 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V1.2.4_220629_S3000442951.zip) |  |
| 1.1.6 | Applied to: [AE-DC5313-C6PRO](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/DashCam_AE_DC5313_C6_EN_STD_V1.1.6_build211028.zip) | 2021-10-28 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/DashCam_AE_DC5313_C6_EN_STD_V1.1.6_build211028.zip) |  |
| 1.1.3 | Applied to: [AE-DC5313-C6PRO](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/DashCam_AE_DC5313_C6_CN_STD_V1.1.3_build201023.zip) | 2020-10-23 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/DashCam_AE_DC5313_C6_CN_STD_V1.1.3_build201023.zip) |  |

</details>


<details>
<summary><h2>AE-DC8012-C8 - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 1.2.3 | Applied to: [AE-DC8012-C8(2025)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V1.2.3_230605_S3000503831.zip)(2ch) | 2023-06-05 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V1.2.3_230605_S3000503831.zip) |  |

</details>


<details>
<summary><h2>AE-DC8222-C8PRO - UNKNOWN (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 1.1.7 | Applied to: [AE-DC8222-C8PRO(3.5K)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V1.1.7_230919_S3000526629.zip)(2024) | 2025-08-07 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V1.1.7_230919_S3000526629.zip) |  |
| 1.1.3 | Applied to: [AE-DC8222-C8PRO(3.5K)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V1.1.3_250304_S3000634438.zip)(2024) | 2025-03-04 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V1.1.3_250304_S3000634438.zip) |  |

</details>


<details>
<summary><h2>AE-DC8312-C6S - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 1.0.8 | Applied to: [AE-DC8312-C6S(GPS)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V1.0.8_200320_S3000313276.zip) | 2025-07-03 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V1.0.8_200320_S3000313276.zip) |  |

</details>


<details>
<summary><h2>AE-DC8322-G2PRO - UNKNOWN (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 1.1.7 | Applied to: [AE-DC8322-G2PRO(HK)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V1.1.7_230919_S3000526629.zip)(GPS) | 2023-09-19 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V1.1.7_230919_S3000526629.zip) |  |
| 1.1.4 | Applied to: [AE-DC8322-G2PRO(HK)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V1.1.4_220725_S3000443106.zip)(GPS) | 2022-07-25 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V1.1.4_220725_S3000443106.zip) |  |

</details>


<details>
<summary><h2>AE-DI2032-G40 - UNKNOWN (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 6.0.1 | Applied to: [AE-DI2032-G40(V2)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V6.0.1_260104_S3000696935.zip)(B)(US)(Integrated) | 2026-01-04 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V6.0.1_260104_S3000696935.zip) |  |
| 5.1.2 | Applied to: [AE-DI2032-G40(B)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.1.2_251024_S3000683492.zip)(EU) | 2025-01-02 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.1.2_251024_S3000683492.zip) |  |

</details>


<details>
<summary><h2>AE-DI5042-G4 - UNKNOWN (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 4.9.1 | Applied to: [AE-DI5042-G4(GPS+4G)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V4.9.1_240118_S3000552549.zip)(Lite) | 2024-01-18 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V4.9.1_240118_S3000552549.zip) |  |
| 4.4.3 | Applied to: [AE-DI5042-G4(GPS+4G)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/020a231f-6ff3-452b-be5e-24b24bfac6d5.zip)(Lite) | 2022-03-18 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/020a231f-6ff3-452b-be5e-24b24bfac6d5.zip) |  |

</details>


<details>
<summary><h2>AE-DI5052-G40 - UNKNOWN (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 4.7.5 | Applied to: [AE-DI5052-G40](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V4.7.5_260409_S3000716981.zip) PRO(EU) | 2026-04-09 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V4.7.5_260409_S3000716981.zip) |  |
| 4.7.4 | Applied to: [AE-DI5052-G40](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V4.7.4_251117_S3000685762.zip) PRO(EU) | 2025-11-17 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V4.7.4_251117_S3000685762.zip) |  |

</details>


<details>
<summary><h2>AE-MD5043-SD - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.1 | Applied to: [AE-MD5043-SD/GLF(EU-STD)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.12_260416_S3000716519.zip) | 2024-11-21 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.12_260416_S3000716519.zip) |  |

</details>


<details>
<summary><h2>AE-MH0408 - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.1 | Applied to: [AE-MH0408(1T)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.12_260416_S3000716519.zip)(RJ45) | 2024-11-21 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.12_260416_S3000716519.zip) |  |

</details>


<details>
<summary><h2>AE-VC1B1I-ISF - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 3.0.2 | Applied to: [AE-VC1B1I-ISF(RJ45)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V3.0.2_240613_S3000580999.zip)(6mm) | 2024-06-13 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V3.0.2_240613_S3000580999.zip) |  |

</details>


<details>
<summary><h2>AE-VC215I-ISF - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 3.0.2 | Applied to: [AE-VC215I-ISF(M12)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V3.0.2_230315_S3000488384.zip)(2.8mm) | 2023-03-15 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V3.0.2_230315_S3000488384.zip) |  |

</details>


<details>
<summary><h2>AE-VC3B2I-ISF - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 4.3.3 | Applied to: [AE-VC3B2I-ISF(RJ45)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V4.3.3_260311_S3000717251.zip)(6mm) | 2026-03-11 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V4.3.3_260311_S3000717251.zip) |  |

</details>


<details>
<summary><h2>AE-VC583I-ISF - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 3.0.1 | Applied to: [AE-VC583I-IS/P(H)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V3.0.1_230306_S3000485364.zip)(M12)(16mm) | 2023-03-06 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V3.0.1_230306_S3000485364.zip) |  |

</details>


<details>
<summary><h2>DS-1005KI - UNKNOWN (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 1.3.4 | Applied to: [DS-1005KI](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V1.3.4_S3000653240.zip) | 2020-25-06 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V1.3.4_S3000653240.zip) |  |
| 1.3.1 | Applied to: [DS-1005KI](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/4e0fc5d3-bfdf-4c83-8120-5498fed38183.zip) | 2017-10-12 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/4e0fc5d3-bfdf-4c83-8120-5498fed38183.zip) |  |

</details>


<details>
<summary><h2>DS-1006KI - UNKNOWN (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 2.0.0 | Applied to: [DS-1006KI](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V2.0.0_230822_S3000522028.zip) | 2023-08-22 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V2.0.0_230822_S3000522028.zip) |  |
| 1.2.4 | Applied to: [DS-1006KI](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V1.2.4_220629_S3000442951.zip) | 2022-06-29 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V1.2.4_220629_S3000442951.zip) |  |

</details>


<details>
<summary><h2>DS-1100KI - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.1.2 | Applied to: [DS-1100KI(C)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.1.2_251024_S3000683492.zip) | 2025-10-24 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.1.2_251024_S3000683492.zip) |  |

</details>


<details>
<summary><h2>DS-1105KI - UNKNOWN (3 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.1.2 | Applied to: [DS-1105KI](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.1.2_251024_S3000683489.zip) | 2025-10-24 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.1.2_251024_S3000683489.zip) |  |
| 4.6.0 | Applied to: [DS-1105KI](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V4.6.0_230704_S3000509505.zip) | 2023-07-04 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V4.6.0_230704_S3000509505.zip) |  |
| 1.1.0 | Applied to: [DS-1105KI](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V1.1.0_220914_S3000453160.zip) | 2022-09-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V1.1.0_220914_S3000453160.zip) |  |

</details>


<details>
<summary><h2>DS-1200KI - UNKNOWN (3 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 2.0.0 | Applied to: [DS-1200KI](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V2.0.0_230822_S3000522029.zip) | 2023-08-22 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V2.0.0_230822_S3000522029.zip) |  |
| 1.2.4 | Applied to: [DS-1200KI](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V1.2.4_220629_S3000442951.zip) | 2022-06-29 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V1.2.4_220629_S3000442951.zip) |  |
| 1.1.0 | Applied to: [DS-1200KI](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/7cea2f2f-1de8-4ac1-a6cf-06213036f752.zip) | 2017-08-25 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/7cea2f2f-1de8-4ac1-a6cf-06213036f752.zip) |  |

</details>


<details>
<summary><h2>DS-2CD1023G0-IUF - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD1023G0-IUF(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip)(C) | 2024-12-11 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) |  |

</details>


<details>
<summary><h2>DS-2CD1023G0E-I - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD1023G0E-I(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | 2024-12-11 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) |  |
| 5.5.84 | Applied to: [DS-2CD1023G0E-I(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/c3afe62f-4071-4e50-a292-ded015321289.zip) | 2021-01-04 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/c3afe62f-4071-4e50-a292-ded015321289.zip) |  |

</details>


<details>
<summary><h2>DS-2CD1023G2-LIDUF - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.34 | Applied to: [DS-2CD1023G2-LIDUF/4G/SL(2.8)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.34_250908_S3000674302.zip)OSTD/LA/FUS | 2025-09-08 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.34_250908_S3000674302.zip) |  |

</details>


<details>
<summary><h2>DS-2CD1023G2-LIU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.10 | Applied to: [DS-2CD1023G2-LIUF(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.100_260416_S3000716492.zip) | 2024-12-05 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.100_260416_S3000716492.zip) |  |

</details>


<details>
<summary><h2>DS-2CD1023G2-LIUF - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.21 | Applied to: [DS-2CD1023G2-LIUF/SL(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.21_250714_S3000661481.zip) | 2025-07-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.21_250714_S3000661481.zip) |  |

</details>


<details>
<summary><h2>DS-2CD1027G2-L - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.10 | Applied to: [DS-2CD1027G2-LUF(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.100_260416_S3000716492.zip) | 2024-12-05 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.100_260416_S3000716492.zip) |  |

</details>


<details>
<summary><h2>DS-2CD1027G2H-LIU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.21 | Applied to: [DS-2CD1027G2H-LIUF(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.21_250714_S3000661481.zip) | 2025-07-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.21_250714_S3000661481.zip) |  |

</details>


<details>
<summary><h2>DS-2CD1027G2H-LIUF - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.21 | Applied to: [DS-2CD1027G2H-LIUF/SRB(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.21_250714_S3000661481.zip) | 2025-07-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.21_250714_S3000661481.zip) |  |

</details>


<details>
<summary><h2>DS-2CD1027G3-LIU - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.9.12 | Applied to: [DS-2CD1027G3-LIUF(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.9.12_260407_S3000713711.zip) | 2025-09-19 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.9.12_260407_S3000713711.zip) |  |
| 5.9.11 | Applied to: [DS-2CD1027G3-LIUF(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.9.11_251030_S3000682327.zip) | 2025-08-22 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.9.11_251030_S3000682327.zip) |  |

</details>


<details>
<summary><h2>DS-2CD1043G0-I - IPC_E7S (3 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD1043G0-IUF(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip)(B) | 2024-12-11 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) |  |
| 5.5.820 | Applied to: [DS-2CD1043G0-IUF(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.820_260410_S3000715634.zip)(B) | 2023-11-09 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.820_260410_S3000715634.zip) |  |
| 5.5.88 | Applied to: [DS-2CD1043G0-IUF(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/01252820-85e5-4c30-ba88-1dd8b8e2d072.zip)(B) | 2020-06-10 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/01252820-85e5-4c30-ba88-1dd8b8e2d072.zip) |  |

</details>


<details>
<summary><h2>DS-2CD1043G2-LIDUF - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.34 | Applied to: [DS-2CD1043G2-LIDUF/4G/SL(2.8)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.34_250908_S3000674302.zip)OSTD/JP/FUS | 2025-09-08 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.34_250908_S3000674302.zip) |  |

</details>


<details>
<summary><h2>DS-2CD1043G2-LIU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.10 | Applied to: [DS-2CD1043G2-LIUF(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.100_260416_S3000716492.zip) | 2025-07-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.100_260416_S3000716492.zip) |  |

</details>


<details>
<summary><h2>DS-2CD1043G2-LIUF - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.41 | Applied to: [DS-2CD1043G2-LIUF/SL(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.41_260401_S3000712602.zip) | 2026-04-01 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.41_260401_S3000712602.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202604/releasenote%5CNetwork_Camera-V5.8.41_SP1_Release_Note-E10.pdf) |
| 5.8.10 | Applied to: [DS-2CD1043G2-LIUF/SL(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.100_260416_S3000716492.zip) | 2025-07-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.100_260416_S3000716492.zip) |  |

</details>


<details>
<summary><h2>DS-2CD1047G2-L - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.10 | Applied to: [DS-2CD1047G2-LUF(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.100_260416_S3000716492.zip) | 2025-07-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.100_260416_S3000716492.zip) |  |

</details>


<details>
<summary><h2>DS-2CD1047G2H-LIU - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.41 | Applied to: [DS-2CD1047G2H-LIU(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.41_260401_S3000712602.zip)(BLACK) | 2026-04-01 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.41_260401_S3000712602.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202604/releasenote%5CNetwork_Camera-V5.8.41_SP1_Release_Note-E10.pdf) |
| 5.8.10 | Applied to: [DS-2CD1047G2H-LIU(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.100_260416_S3000716492.zip)(BLACK) | 2025-07-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.100_260416_S3000716492.zip) |  |

</details>


<details>
<summary><h2>DS-2CD1047G2H-LIUF - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.41 | Applied to: [DS-2CD1047G2H-LIUF/SRB(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.41_260401_S3000712602.zip) | 2026-04-01 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.41_260401_S3000712602.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202604/releasenote%5CNetwork_Camera-V5.8.41_SP1_Release_Note-E10.pdf) |
| 5.8.10 | Applied to: [DS-2CD1047G2H-LIUF/SRB(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.100_260416_S3000716492.zip) | 2025-07-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.100_260416_S3000716492.zip) |  |

</details>


<details>
<summary><h2>DS-2CD1047G3-LIU - IPC_G0 (3 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.9.13 | Applied to: [DS-2CD1047G3-LIUF/SL(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.9.13_251124_S3000688200.zip) | 2025-11-24 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.9.13_251124_S3000688200.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202511/releasenote%5CNetwork_Camera-V5.9.12_250919_Release_Note-IPCE_E_E15.pdf) |
| 5.9.12 | Applied to: [DS-2CD1047G3-LIUF(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.9.12_260407_S3000713711.zip) | 2025-09-19 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.9.12_260407_S3000713711.zip) |  |
| 5.9.11 | Applied to: [DS-2CD1047G3-LIUF(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.9.11_251030_S3000682327.zip) | 2025-08-22 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.9.11_251030_S3000682327.zip) |  |

</details>


<details>
<summary><h2>DS-2CD1047G3H-LIU - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD1047G3H-LIUF(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | 2025-12-10 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) |  |
| 5.8.21 | Applied to: [DS-2CD1047G3H-LIU/SRB(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.21_250714_S3000661481.zip) | 2025-11-17 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.21_250714_S3000661481.zip) |  |

</details>


<details>
<summary><h2>DS-2CD1053G0-I - IPC_G0 (3 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD1053G0-I(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | 2024-10-08 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) |  |
| 5.5.800 | Applied to: [DS-2CD1053G0-I(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.800_211009_S3000390724.zip) | 2021-08-16 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.800_211009_S3000390724.zip) |  |
| 5.5.89 | Applied to: [DS-2CD1053G0-I(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/87acab3e-5d46-45cd-88c4-87b51139b600.zip) | 2021-04-29 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/87acab3e-5d46-45cd-88c4-87b51139b600.zip) |  |

</details>


<details>
<summary><h2>DS-2CD1067G2H-LIUF - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.21 | Applied to: [DS-2CD1067G2H-LIUF/SRB(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.21_250714_S3000661481.zip) | 2025-05-08 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.21_250714_S3000661481.zip) |  |

</details>


<details>
<summary><h2>DS-2CD1067G3-LIU - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.9.12 | Applied to: [DS-2CD1067G3-LIUF/SRB(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.9.12_260407_S3000713711.zip) | 2025-09-19 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.9.12_260407_S3000713711.zip) |  |
| 5.9.11 | Applied to: [DS-2CD1067G3-LIUF/SRB(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.9.11_251030_S3000682327.zip) | 2025-08-22 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.9.11_251030_S3000682327.zip) |  |

</details>


<details>
<summary><h2>DS-2CD1083G0-I - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD1083G0-I(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip)(C) | 2024-10-08 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) |  |

</details>


<details>
<summary><h2>DS-2CD1083G0-IUF - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD1083G0-IUF(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip)(C) | 2024-10-08 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) |  |

</details>


<details>
<summary><h2>DS-2CD1123G0-IUF - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD1123G0-IUF(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip)(C) | 2024-12-11 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) |  |

</details>


<details>
<summary><h2>DS-2CD1123G0E-I - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD1123G0E-I(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | 2024-12-11 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) |  |
| 5.5.84 | Applied to: [DS-2CD1123G0E-I(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/c3afe62f-4071-4e50-a292-ded015321289.zip) | 2021-01-04 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/c3afe62f-4071-4e50-a292-ded015321289.zip) |  |

</details>


<details>
<summary><h2>DS-2CD1123G2-LIU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.10 | Applied to: [DS-2CD1123G2-LIUF(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.100_260416_S3000716492.zip) | 2024-12-05 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.100_260416_S3000716492.zip) |  |

</details>


<details>
<summary><h2>DS-2CD1127G2-L - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.10 | Applied to: [DS-2CD1127G2-LUF(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.100_260416_S3000716492.zip) | 2024-12-05 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.100_260416_S3000716492.zip) |  |

</details>


<details>
<summary><h2>DS-2CD1127G2H-LIU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.21 | Applied to: [DS-2CD1127G2H-LIU(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.21_250714_S3000661481.zip) | 2025-07-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.21_250714_S3000661481.zip) |  |

</details>


<details>
<summary><h2>DS-2CD1127G3-LIU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.9.12 | Applied to: [DS-2CD1127G3-LIUF(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.9.12_260407_S3000713711.zip) | 2025-09-19 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.9.12_260407_S3000713711.zip) |  |

</details>


<details>
<summary><h2>DS-2CD1143G0-I - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD1143G0-I(4mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | 2024-12-11 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) |  |
| 5.5.88 | Applied to: [DS-2CD1143G0-I(4mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/01252820-85e5-4c30-ba88-1dd8b8e2d072.zip) | 2020-06-10 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/01252820-85e5-4c30-ba88-1dd8b8e2d072.zip) |  |

</details>


<details>
<summary><h2>DS-2CD1143G2-LIU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.10 | Applied to: [DS-2CD1143G2-LIUF(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.100_260416_S3000716492.zip) | 2025-07-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.100_260416_S3000716492.zip) |  |

</details>


<details>
<summary><h2>DS-2CD1147G2-L - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.10 | Applied to: [DS-2CD1147G2-L(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.100_260416_S3000716492.zip) | 2025-07-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.100_260416_S3000716492.zip) |  |

</details>


<details>
<summary><h2>DS-2CD1147G2H-LIU - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.41 | Applied to: [DS-2CD1147G2H-LIU(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.41_260401_S3000712602.zip)(BLACK) | 2026-04-01 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.41_260401_S3000712602.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202604/releasenote%5CNetwork_Camera-V5.8.41_SP1_Release_Note-E10.pdf) |
| 5.8.10 | Applied to: [DS-2CD1147G2H-LIU(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.100_260416_S3000716492.zip)(BLACK) | 2025-07-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.100_260416_S3000716492.zip) |  |

</details>


<details>
<summary><h2>DS-2CD1147G3-LIU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.9.12 | Applied to: [DS-2CD1147G3-LIUF(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.9.12_260407_S3000713711.zip) | 2025-09-19 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.9.12_260407_S3000713711.zip) |  |

</details>


<details>
<summary><h2>DS-2CD1147G3H-LIU - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD1147G3H-LIUF(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | 2025-12-10 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) |  |
| 5.8.21 | Applied to: [DS-2CD1147G3H-LIUF(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.21_250714_S3000661481.zip) | 2025-11-17 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.21_250714_S3000661481.zip) |  |

</details>


<details>
<summary><h2>DS-2CD1153G0-I - IPC_G0 (3 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD1153G0-I(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | 2024-10-08 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) |  |
| 5.5.800 | Applied to: [DS-2CD1153G0-I(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.800_211009_S3000390724.zip) | 2021-08-16 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.800_211009_S3000390724.zip) |  |
| 5.5.89 | Applied to: [DS-2CD1153G0-I(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/87acab3e-5d46-45cd-88c4-87b51139b600.zip) | 2021-04-29 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/87acab3e-5d46-45cd-88c4-87b51139b600.zip) |  |

</details>


<details>
<summary><h2>DS-2CD1167G3-LIU - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.9.12 | Applied to: [DS-2CD1167G3-LIUF(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.9.12_260407_S3000713711.zip) | 2025-09-19 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.9.12_260407_S3000713711.zip) |  |
| 5.9.11 | Applied to: [DS-2CD1167G3-LIUF(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.9.11_251030_S3000682327.zip) | 2025-08-22 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.9.11_251030_S3000682327.zip) |  |

</details>


<details>
<summary><h2>DS-2CD1183G0-I - IPC_G0 (3 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.19 | Applied to: [DS-2CD1183G0-I(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.19_241207_S3000618493.zip) | 2024-12-07 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.19_241207_S3000618493.zip) |  |
| 5.7.23 | Applied to: [DS-2CD1183G0-I(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | 2024-10-08 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) |  |
| 5.7.18 | Applied to: [DS-2CD1183G0-I(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.18_240826_S3000597013.zip) | 2024-08-26 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.18_240826_S3000597013.zip) |  |

</details>


<details>
<summary><h2>DS-2CD1183G0-IUF - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD1183G0-IUF(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | 2024-10-08 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) |  |
| 5.7.18 | Applied to: [DS-2CD1183G0-IUF(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.18_240826_S3000597013.zip) | 2024-08-26 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.18_240826_S3000597013.zip) |  |

</details>


<details>
<summary><h2>DS-2CD1323G0-IUF - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD1323G0-IUF(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip)(C) | 2024-12-11 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) |  |

</details>


<details>
<summary><h2>DS-2CD1323G0E-I - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD1323G0E-I(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | 2024-12-11 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) |  |
| 5.5.84 | Applied to: [DS-2CD1323G0E-I(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/c3afe62f-4071-4e50-a292-ded015321289.zip) | 2021-01-04 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/c3afe62f-4071-4e50-a292-ded015321289.zip) |  |

</details>


<details>
<summary><h2>DS-2CD1323G2-LIU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.10 | Applied to: [DS-2CD1323G2-LIUF(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.100_260416_S3000716492.zip) | 2024-12-05 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.100_260416_S3000716492.zip) |  |

</details>


<details>
<summary><h2>DS-2CD1323G2-LIUF - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.21 | Applied to: [DS-2CD1323G2-LIUF/SL(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.21_250714_S3000661481.zip) | 2025-07-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.21_250714_S3000661481.zip) |  |

</details>


<details>
<summary><h2>DS-2CD1327G2-L - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.10 | Applied to: [DS-2CD1327G2-LUF(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.100_260416_S3000716492.zip) | 2024-12-05 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.100_260416_S3000716492.zip) |  |

</details>


<details>
<summary><h2>DS-2CD1327G2H-LIU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.21 | Applied to: [DS-2CD1327G2H-LIUF(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.21_250714_S3000661481.zip) | 2025-07-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.21_250714_S3000661481.zip) |  |

</details>


<details>
<summary><h2>DS-2CD1327G2H-LIUF - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.21 | Applied to: [DS-2CD1327G2H-LIUF/SL(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.21_250714_S3000661481.zip) | 2025-07-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.21_250714_S3000661481.zip) |  |

</details>


<details>
<summary><h2>DS-2CD1327G3-LIU - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.9.12 | Applied to: [DS-2CD1327G3-LIUF/SRB(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.9.12_260407_S3000713711.zip) | 2025-09-19 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.9.12_260407_S3000713711.zip) |  |
| 5.9.11 | Applied to: [DS-2CD1327G3-LIUF/SRB(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.9.11_251030_S3000682327.zip) | 2025-08-22 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.9.11_251030_S3000682327.zip) |  |

</details>


<details>
<summary><h2>DS-2CD1343G0-I - IPC_E7S (3 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD1343G0-I(4mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | 2024-12-11 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) |  |
| 5.5.820 | Applied to: [DS-2CD1343G0-I(4mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.820_260410_S3000715634.zip) | 2023-11-09 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.820_260410_S3000715634.zip) |  |
| 5.5.88 | Applied to: [DS-2CD1343G0-I(4mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/01252820-85e5-4c30-ba88-1dd8b8e2d072.zip) | 2020-06-10 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/01252820-85e5-4c30-ba88-1dd8b8e2d072.zip) |  |

</details>


<details>
<summary><h2>DS-2CD1343G2-LIU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.10 | Applied to: [DS-2CD1343G2-LIU(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.100_260416_S3000716492.zip)(BLACK) | 2025-07-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.100_260416_S3000716492.zip) |  |

</details>


<details>
<summary><h2>DS-2CD1343G2-LIUF - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.41 | Applied to: [DS-2CD1343G2-LIUF/SL(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.41_260401_S3000712602.zip) | 2026-04-01 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.41_260401_S3000712602.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202604/releasenote%5CNetwork_Camera-V5.8.41_SP1_Release_Note-E10.pdf) |
| 5.8.10 | Applied to: [DS-2CD1343G2-LIUF/SL(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.100_260416_S3000716492.zip) | 2025-07-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.100_260416_S3000716492.zip) |  |

</details>


<details>
<summary><h2>DS-2CD1347G2-L - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.10 | Applied to: [DS-2CD1347G2-LUF(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.100_260416_S3000716492.zip) | 2025-07-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.100_260416_S3000716492.zip) |  |

</details>


<details>
<summary><h2>DS-2CD1347G2H-LIU - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.41 | Applied to: [DS-2CD1347G2H-LIU(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.41_260401_S3000712602.zip)(BLACK) | 2026-04-01 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.41_260401_S3000712602.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202604/releasenote%5CNetwork_Camera-V5.8.41_SP1_Release_Note-E10.pdf) |
| 5.8.10 | Applied to: [DS-2CD1347G2H-LIU(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.100_260416_S3000716492.zip) | 2025-07-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.100_260416_S3000716492.zip) |  |

</details>


<details>
<summary><h2>DS-2CD1347G2H-LIUF - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.41 | Applied to: [DS-2CD1347G2H-LIUF/SRB(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.41_260401_S3000712602.zip) | 2026-04-01 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.41_260401_S3000712602.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202604/releasenote%5CNetwork_Camera-V5.8.41_SP1_Release_Note-E10.pdf) |
| 5.8.10 | Applied to: [DS-2CD1347G2H-LIUF/SL(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.100_260416_S3000716492.zip) | 2025-07-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.100_260416_S3000716492.zip) |  |

</details>


<details>
<summary><h2>DS-2CD1347G3-LIU - IPC_G0 (3 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.9.13 | Applied to: [DS-2CD1347G3-LIUF/SL(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.9.13_251124_S3000688200.zip) | 2025-11-24 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.9.13_251124_S3000688200.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202511/releasenote%5CNetwork_Camera-V5.9.12_250919_Release_Note-IPCE_E_E15.pdf) |
| 5.9.12 | Applied to: [DS-2CD1347G3-LIUF/SL(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.9.12_260407_S3000713711.zip) | 2025-09-19 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.9.12_260407_S3000713711.zip) |  |
| 5.9.11 | Applied to: [DS-2CD1347G3-LIUF/SL(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.9.11_251030_S3000682327.zip) | 2025-08-22 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.9.11_251030_S3000682327.zip) |  |

</details>


<details>
<summary><h2>DS-2CD1347G3H-LIU - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD1347G3H-LIU/SRB(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | 2025-12-10 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) |  |
| 5.8.21 | Applied to: [DS-2CD1347G3H-LIU(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.21_250714_S3000661481.zip) | 2025-11-17 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.21_250714_S3000661481.zip) |  |

</details>


<details>
<summary><h2>DS-2CD1353G0-I - IPC_G0 (3 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD1353G0-I(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip)(C) | 2024-10-08 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) |  |
| 5.5.800 | Applied to: [DS-2CD1353G0-I(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.800_211009_S3000390724.zip) | 2021-08-16 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.800_211009_S3000390724.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202312/releasenote%5CNetwork_Camera_V5.5.89_Release_Note_--G0.pdf) |
| 5.5.89 | Applied to: [DS-2CD1353G0-I(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/87acab3e-5d46-45cd-88c4-87b51139b600.zip) | 2021-04-29 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/87acab3e-5d46-45cd-88c4-87b51139b600.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202312/releasenote%5CNetwork_Camera_V5.5.89_Release_Note_--G0.pdf) |

</details>


<details>
<summary><h2>DS-2CD1363G2P-LIUF - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.12 | Applied to: [DS-2CD1363G2P-LIUF/SRB(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.12_260416_S3000716519.zip) | 2026-04-16 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.12_260416_S3000716519.zip) |  |
| 5.8.11 | Applied to: [DS-2CD1363G2P-LIUF/SL(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.110_260421_S3000717992.zip) | 2025-10-29 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.110_260421_S3000717992.zip) |  |

</details>


<details>
<summary><h2>DS-2CD1363G2P-LIUF-S-L--RB- - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.12 | [DS-2CD1363G2P-LIUF-S-L--RB-](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.12_260416_S3000716513.zip) | 2026-04-16 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.12_260416_S3000716513.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202605/releasenote%5CNetwork_Camera-V5.8.12_260416_Release_IPCE_P_E11.pdf) |

</details>


<details>
<summary><h2>DS-2CD1367G2H-LIUF - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.21 | Applied to: [DS-2CD1367G2H-LIUF/SRB(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.21_250714_S3000661481.zip) | 2025-05-08 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.21_250714_S3000661481.zip) |  |

</details>


<details>
<summary><h2>DS-2CD1367G2HP-LIUF - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.12 | Applied to: [DS-2CD1367G2HP-LIUF/SRB(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.12_260416_S3000716519.zip) | 2026-04-16 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.12_260416_S3000716519.zip) |  |
| 5.8.11 | Applied to: [DS-2CD1367G2HP-LIUF/SL(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.110_260421_S3000717992.zip) | 2025-10-29 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.110_260421_S3000717992.zip) |  |

</details>


<details>
<summary><h2>DS-2CD1367G2HP-LIUF-S-L--RB- - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.12 | [DS-2CD1367G2HP-LIUF-S-L--RB-](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.12_260416_S3000716513.zip) | 2026-04-16 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.12_260416_S3000716513.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202605/releasenote%5CNetwork_Camera-V5.8.12_260416_Release_IPCE_P_E11.pdf) |

</details>


<details>
<summary><h2>DS-2CD1367G3-LIU - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.9.12 | Applied to: [DS-2CD1367G3-LIU/SRB(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.9.12_260407_S3000713711.zip) | 2025-09-19 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.9.12_260407_S3000713711.zip) |  |
| 5.9.11 | Applied to: [DS-2CD1367G3-LIU/SRB(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.9.11_251030_S3000682327.zip) | 2025-08-22 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.9.11_251030_S3000682327.zip) |  |

</details>


<details>
<summary><h2>DS-2CD1383G0-I - IPC_G0 (3 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.19 | Applied to: [DS-2CD1383G0-I(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.19_241207_S3000618493.zip) | 2024-12-07 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.19_241207_S3000618493.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.19_241207_Release_Note.pdf) |
| 5.7.23 | Applied to: [DS-2CD1383G0-I(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip)(C) | 2024-10-08 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) |  |
| 5.7.18 | Applied to: [DS-2CD1383G0-I(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.18_240826_S3000597013.zip) | 2024-08-26 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.18_240826_S3000597013.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.19_241207_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD1383G0-IUF - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD1383G0-IUF(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | 2024-10-08 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) |  |
| 5.7.18 | Applied to: [DS-2CD1383G0-IUF(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.18_240826_S3000597013.zip) | 2024-08-26 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.18_240826_S3000597013.zip) |  |

</details>


<details>
<summary><h2>DS-2CD1383G2P-LIUF - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.12 | Applied to: [DS-2CD1383G2P-LIUF/SRB(2mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.12_260416_S3000716519.zip) | 2026-04-16 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.12_260416_S3000716519.zip) |  |
| 5.8.11 | Applied to: [DS-2CD1383G2P-LIUF/SL(2mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.110_260421_S3000717992.zip) | 2025-10-29 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.110_260421_S3000717992.zip) |  |

</details>


<details>
<summary><h2>DS-2CD1383G2P-LIUF-S-L--RB- - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.12 | [DS-2CD1383G2P-LIUF-S-L--RB-](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.12_260416_S3000716513.zip) | 2026-04-16 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.12_260416_S3000716513.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202605/releasenote%5CNetwork_Camera-V5.8.12_260416_Release_IPCE_P_E11.pdf) |

</details>


<details>
<summary><h2>DS-2CD1623G0-I - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD1623G0-IZ(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | 2024-12-11 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) |  |
| 5.5.800 | Applied to: [DS-2CD1623G0-IZ(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.800_211009_S3000390724.zip) | 2021-06-28 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.800_211009_S3000390724.zip) |  |

</details>


<details>
<summary><h2>DS-2CD1623G2-IZ - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.10 | Applied to: [DS-2CD1623G2-IZ(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.100_260416_S3000716492.zip) | 2025-07-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.100_260416_S3000716492.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202508/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-E10.pdf) |

</details>


<details>
<summary><h2>DS-2CD1623G2-LIU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.21 | Applied to: [DS-2CD1B23G2-LIU(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.21_250714_S3000661481.zip) | 2025-07-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.21_250714_S3000661481.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202508/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-E9.pdf) |

</details>


<details>
<summary><h2>DS-2CD1623G2-LIZ - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.10 | Applied to: [DS-2CD1623G2-LIZSU(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.100_260416_S3000716492.zip) | 2025-07-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.100_260416_S3000716492.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202508/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-E10.pdf) |

</details>


<details>
<summary><h2>DS-2CD1627G2H-LIU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.21 | Applied to: [DS-2CD1B27G2H-LIUF(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.21_250714_S3000661481.zip) | 2025-07-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.21_250714_S3000661481.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202508/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-E9.pdf) |

</details>


<details>
<summary><h2>DS-2CD1643G0-I - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD1643G0-IZ(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | 2024-12-11 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202312/releasenote%5CNetwork_Camera_V5.5.89_Release_Note_--G0.pdf) |
| 5.5.89 | Applied to: [DS-2CD1643G0-IZ(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/87acab3e-5d46-45cd-88c4-87b51139b600.zip) | 2021-04-29 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/87acab3e-5d46-45cd-88c4-87b51139b600.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202312/releasenote%5CNetwork_Camera_V5.5.89_Release_Note_--G0.pdf) |

</details>


<details>
<summary><h2>DS-2CD1643G2-IZ - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.10 | Applied to: [DS-2CD1643G2-IZ(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.100_260416_S3000716492.zip) | 2025-07-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.100_260416_S3000716492.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202508/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-E10.pdf) |

</details>


<details>
<summary><h2>DS-2CD1643G2-LIU - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.41 | Applied to: [DS-2CD1B43G2-LIU(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.41_260401_S3000712602.zip) | 2026-04-01 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.41_260401_S3000712602.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202604/releasenote%5CNetwork_Camera-V5.8.41_SP1_Release_Note-E10.pdf) |
| 5.8.10 | Applied to: [DS-2CD1B43G2-LIU(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.100_260416_S3000716492.zip) | 2025-07-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.100_260416_S3000716492.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202508/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-E10.pdf) |

</details>


<details>
<summary><h2>DS-2CD1643G2-LIZ - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.10 | Applied to: [DS-2CD1643G2-LIZU(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.100_260416_S3000716492.zip) | 2025-07-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.100_260416_S3000716492.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202508/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-E10.pdf) |

</details>


<details>
<summary><h2>DS-2CD1647G2H-LIU - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.41 | Applied to: [DS-2CD1B47G2H-LIUF(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.41_260401_S3000712602.zip) | 2026-04-01 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.41_260401_S3000712602.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202604/releasenote%5CNetwork_Camera-V5.8.41_SP1_Release_Note-E10.pdf) |
| 5.8.10 | Applied to: [DS-2CD1B47G2H-LIUF(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.100_260416_S3000716492.zip) | 2025-07-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.100_260416_S3000716492.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202508/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-E10.pdf) |

</details>


<details>
<summary><h2>DS-2CD1653G0-I - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD1653G0-IZ(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip)(C) | 2024-10-08 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202507/releasenote%5CNetwork_Camera-V5.7.23_SP_Release_Note-E8.pdf) |

</details>


<details>
<summary><h2>DS-2CD1723G0-I - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD1723G0-I(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | 2024-12-11 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202507/releasenote%5CNetwork_Camera-V5.7.23_SP2_Release_Note-E8.pdf) |
| 5.5.800 | Applied to: [DS-2CD1723G0-I(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.800_211009_S3000390724.zip) | 2021-06-28 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.800_211009_S3000390724.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202507/releasenote%5CNetwork_Camera-V5.7.23_SP2_Release_Note-E8.pdf) |

</details>


<details>
<summary><h2>DS-2CD1723G2-IZ - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.10 | Applied to: [DS-2CD1723G2-IZS(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.100_260416_S3000716492.zip) | 2025-07-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.100_260416_S3000716492.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202508/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-E10.pdf) |

</details>


<details>
<summary><h2>DS-2CD1723G2-LIZ - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.10 | Applied to: [DS-2CD1723G2-LIZU(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.100_260416_S3000716492.zip) | 2025-07-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.100_260416_S3000716492.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202508/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-E10.pdf) |

</details>


<details>
<summary><h2>DS-2CD1743G0-I - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD1743G0-I(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | 2024-12-11 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202312/releasenote%5CNetwork_Camera_V5.5.89_Release_Note_--G0.pdf) |
| 5.5.89 | Applied to: [DS-2CD1743G0-I(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/87acab3e-5d46-45cd-88c4-87b51139b600.zip) | 2021-04-29 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/87acab3e-5d46-45cd-88c4-87b51139b600.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202312/releasenote%5CNetwork_Camera_V5.5.89_Release_Note_--G0.pdf) |

</details>


<details>
<summary><h2>DS-2CD1743G2-IZ - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.10 | Applied to: [DS-2CD1743G2-IZ(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.100_260416_S3000716492.zip) | 2025-07-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.100_260416_S3000716492.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202508/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-E10.pdf) |

</details>


<details>
<summary><h2>DS-2CD1743G2-LIZ - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.10 | Applied to: [DS-2CD1743G2-LIZU(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.100_260416_S3000716492.zip) | 2025-07-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.100_260416_S3000716492.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202508/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-E10.pdf) |

</details>


<details>
<summary><h2>DS-2CD1753G0-I - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD1753G0-IZ(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip)(C) | 2024-10-08 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202507/releasenote%5CNetwork_Camera-V5.7.23_SP_Release_Note-E8.pdf) |

</details>


<details>
<summary><h2>DS-2CD1A23G0-IZU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD1A23G0-IZU(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | 2024-10-08 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202507/releasenote%5CNetwork_Camera-V5.7.23_SP_Release_Note-E8.pdf) |

</details>


<details>
<summary><h2>DS-2CD1A43G0-IZU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD1A43G0-IZU(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | 2024-10-08 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202507/releasenote%5CNetwork_Camera-V5.7.23_SP_Release_Note-E8.pdf) |

</details>


<details>
<summary><h2>DS-2CD1B23G2-LIUF - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.21 | Applied to: [DS-2CD1B23G2-LIUF/SL(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.21_250714_S3000661481.zip) | 2025-07-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.21_250714_S3000661481.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202508/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-E9.pdf) |

</details>


<details>
<summary><h2>DS-2CD1B27G2H-LIUF - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.21 | Applied to: [DS-2CD1B27G2H-LIUF/SL(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.21_250714_S3000661481.zip) | 2025-07-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.21_250714_S3000661481.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202508/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-E9.pdf) |

</details>


<details>
<summary><h2>DS-2CD1B27G3-LIU - IPC_G0 (3 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.9.13 | Applied to: [DS-2CD1B27G3-LIUF/LSRB(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.9.13_251124_S3000688200.zip) | 2025-11-24 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.9.13_251124_S3000688200.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.9.13_251124_Release_Note-IPCE_E_E15.pdf) |
| 5.9.12 | Applied to: [DS-2CD1B27G3-LIU/SRB(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.9.12_260407_S3000713711.zip) | 2025-09-19 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.9.12_260407_S3000713711.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202511/releasenote%5CNetwork_Camera-V5.9.12_250919_Release_Note-IPCE_E_E15.pdf) |
| 5.9.11 | Applied to: [DS-2CD1B27G3-LIU/SRB(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.9.11_251030_S3000682327.zip) | 2025-08-22 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.9.11_251030_S3000682327.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202511/releasenote%5CNetwork_Camera-V5.9.12_250919_Release_Note-IPCE_E_E15.pdf) |

</details>


<details>
<summary><h2>DS-2CD1B43G2-LIUF - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.41 | Applied to: [DS-2CD1B43G2-LIUF/SL(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.41_260401_S3000712602.zip) | 2026-04-01 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.41_260401_S3000712602.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202604/releasenote%5CNetwork_Camera-V5.8.41_SP1_Release_Note-E10.pdf) |
| 5.8.10 | Applied to: [DS-2CD1B43G2-LIUF/SL(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.100_260416_S3000716492.zip) | 2025-07-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.100_260416_S3000716492.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202508/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-E10.pdf) |

</details>


<details>
<summary><h2>DS-2CD1B47G2H-LIUF - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.41 | Applied to: [DS-2CD1B47G2H-LIUF/SRB(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.41_260401_S3000712602.zip) | 2026-04-01 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.41_260401_S3000712602.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202604/releasenote%5CNetwork_Camera-V5.8.41_SP1_Release_Note-E10.pdf) |
| 5.8.10 | Applied to: [DS-2CD1B47G2H-LIUF/SL(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.100_260416_S3000716492.zip) | 2025-07-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.100_260416_S3000716492.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202508/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-E10.pdf) |

</details>


<details>
<summary><h2>DS-2CD1B47G3-LIU - IPC_G0 (3 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.9.13 | Applied to: [DS-2CD1B47G3-LIUF/LSL(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.9.13_251124_S3000688200.zip) | 2025-11-24 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.9.13_251124_S3000688200.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.9.13_251124_Release_Note-IPCE_E_E15.pdf) |
| 5.9.12 | Applied to: [DS-2CD1B47G3-LIUF/SRB(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.9.12_260407_S3000713711.zip) | 2025-09-19 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.9.12_260407_S3000713711.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202511/releasenote%5CNetwork_Camera-V5.9.12_250919_Release_Note-IPCE_E_E15.pdf) |
| 5.9.11 | Applied to: [DS-2CD1B47G3-LIUF/SRB(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.9.11_251030_S3000682327.zip) | 2025-08-22 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.9.11_251030_S3000682327.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202511/releasenote%5CNetwork_Camera-V5.9.12_250919_Release_Note-IPCE_E_E15.pdf) |

</details>


<details>
<summary><h2>DS-2CD1B47G3H-LIU - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD1B47G3H-LIUF/SRB(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | 2025-12-10 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) |  |
| 5.8.21 | Applied to: [DS-2CD1B47G3H-LIU(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.21_250714_S3000661481.zip) | 2025-11-17 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.21_250714_S3000661481.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.8.21_SP1_251117_Release_Note-H13U.pdf) |

</details>


<details>
<summary><h2>DS-2CD1B67G3-LIU - IPC_G0 (3 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.9.13 | Applied to: [DS-2CD1B67G3-LIU/LSL(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.9.13_251124_S3000688200.zip) | 2025-11-24 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.9.13_251124_S3000688200.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.9.13_251124_Release_Note-IPCE_E_E15.pdf) |
| 5.9.12 | Applied to: [DS-2CD1B67G3-LIUF/SRB(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.9.12_260407_S3000713711.zip) | 2025-09-19 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.9.12_260407_S3000713711.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202511/releasenote%5CNetwork_Camera-V5.9.12_250919_Release_Note-IPCE_E_E15.pdf) |
| 5.9.11 | Applied to: [DS-2CD1B67G3-LIUF/SRB(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.9.11_251030_S3000682327.zip) | 2025-08-22 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.9.11_251030_S3000682327.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202511/releasenote%5CNetwork_Camera-V5.9.12_250919_Release_Note-IPCE_E_E15.pdf) |

</details>


<details>
<summary><h2>DS-2CD1H23G2-IZ - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.10 | Applied to: [DS-2CD1H23G2-IZS(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.100_260416_S3000716492.zip) | 2025-07-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.100_260416_S3000716492.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202508/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-E10.pdf) |

</details>


<details>
<summary><h2>DS-2CD1H43G0-IZ - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD1H43G0-IZ(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip)(C) | 2024-12-11 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202507/releasenote%5CNetwork_Camera-V5.7.23_SP2_Release_Note-E8.pdf) |

</details>


<details>
<summary><h2>DS-2CD1H43G2-IZ - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.10 | Applied to: [DS-2CD1H43G2-IZS(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.100_260416_S3000716492.zip) | 2025-07-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.100_260416_S3000716492.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202508/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-E10.pdf) |

</details>


<details>
<summary><h2>DS-2CD1H53G0-IZ - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD1H53G0-IZ(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip)(C) | 2024-10-08 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202507/releasenote%5CNetwork_Camera-V5.7.23_SP_Release_Note-E8.pdf) |

</details>


<details>
<summary><h2>DS-2CD1P23G2-I - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.10 | Applied to: [DS-2CD1P23G2-IUF(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.100_260416_S3000716492.zip) | 2025-07-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.100_260416_S3000716492.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202508/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-E10.pdf) |

</details>


<details>
<summary><h2>DS-2CD1P27G2-L - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.10 | Applied to: [DS-2CD1P27G2-LUF(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.100_260416_S3000716492.zip) | 2025-07-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.100_260416_S3000716492.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202508/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-E10.pdf) |

</details>


<details>
<summary><h2>DS-2CD1P43G2-I - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.10 | Applied to: [DS-2CD1P43G2-I(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.100_260416_S3000716492.zip) | 2025-07-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.100_260416_S3000716492.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202508/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-E10.pdf) |

</details>


<details>
<summary><h2>DS-2CD1P47G2-L - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.10 | Applied to: [DS-2CD1P47G2-L(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.100_260416_S3000716492.zip) | 2025-07-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.100_260416_S3000716492.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202508/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-E10.pdf) |

</details>


<details>
<summary><h2>DS-2CD1T23G0-I - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD1T23G0-I(4mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip)(C) | 2024-10-08 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202507/releasenote%5CNetwork_Camera-V5.7.23_SP_Release_Note-E8.pdf) |

</details>


<details>
<summary><h2>DS-2CD1T23G2-LIU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.10 | Applied to: [DS-2CD1T23G2-LIUF(4mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.100_260416_S3000716492.zip) | 2024-12-05 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.100_260416_S3000716492.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202507/releasenote%5CNetwork_Camera-V5.8.10_SP2_Release_Note-E9.pdf) |

</details>


<details>
<summary><h2>DS-2CD1T23G2-LIUF - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.21 | Applied to: [DS-2CD1T23G2-LIUF/SL(4mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.21_250714_S3000661481.zip) | 2025-07-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.21_250714_S3000661481.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202508/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-E9.pdf) |

</details>


<details>
<summary><h2>DS-2CD1T27G2-L - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.10 | Applied to: [DS-2CD1T27G2-L(4mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.100_260416_S3000716492.zip) | 2024-12-05 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.100_260416_S3000716492.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202507/releasenote%5CNetwork_Camera-V5.8.10_SP2_Release_Note-E9.pdf) |

</details>


<details>
<summary><h2>DS-2CD1T27G2H-LIU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.21 | Applied to: [DS-2CD1T27G2H-LIU(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.21_250714_S3000661481.zip) | 2025-07-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.21_250714_S3000661481.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202508/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-E9.pdf) |

</details>


<details>
<summary><h2>DS-2CD1T27G2H-LIUF - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.21 | Applied to: [DS-2CD1T27G2H-LIUF/SL(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.21_250714_S3000661481.zip) | 2025-07-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.21_250714_S3000661481.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202508/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-E9.pdf) |

</details>


<details>
<summary><h2>DS-2CD1T27G3-LIU - IPC_G0 (3 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.9.13 | Applied to: [DS-2CD1T27G3-LIU/LSRB(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.9.13_251124_S3000688200.zip) | 2025-11-24 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.9.13_251124_S3000688200.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.9.13_251124_Release_Note-IPCE_E_E15.pdf) |
| 5.9.12 | Applied to: [DS-2CD1T27G3-LIU/SRB(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.9.12_260407_S3000713711.zip) | 2025-09-19 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.9.12_260407_S3000713711.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202511/releasenote%5CNetwork_Camera-V5.9.12_250919_Release_Note-IPCE_E_E15.pdf) |
| 5.9.11 | Applied to: [DS-2CD1T27G3-LIU/SRB(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.9.11_251030_S3000682327.zip) | 2025-08-22 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.9.11_251030_S3000682327.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202511/releasenote%5CNetwork_Camera-V5.9.12_250919_Release_Note-IPCE_E_E15.pdf) |

</details>


<details>
<summary><h2>DS-2CD1T43G0-I - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD1T43G0-I(4mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip)(C) | 2024-10-08 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202507/releasenote%5CNetwork_Camera-V5.7.23_SP_Release_Note-E8.pdf) |

</details>


<details>
<summary><h2>DS-2CD1T43G2-LIU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.10 | Applied to: [DS-2CD1T43G2-LIUF(4mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.100_260416_S3000716492.zip) | 2025-07-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.100_260416_S3000716492.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202508/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-E10.pdf) |

</details>


<details>
<summary><h2>DS-2CD1T43G2-LIUF - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.41 | Applied to: [DS-2CD1T43G2-LIUF/SL(4mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.41_260401_S3000712602.zip) | 2026-04-01 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.41_260401_S3000712602.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202604/releasenote%5CNetwork_Camera-V5.8.41_SP1_Release_Note-E10.pdf) |
| 5.8.10 | Applied to: [DS-2CD1T43G2-LIUF/SL(4mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.100_260416_S3000716492.zip) | 2025-07-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.100_260416_S3000716492.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202508/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-E10.pdf) |

</details>


<details>
<summary><h2>DS-2CD1T47G2-L - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.10 | Applied to: [DS-2CD1T47G2-LUF(4mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.100_260416_S3000716492.zip) | 2025-07-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.100_260416_S3000716492.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202508/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-E10.pdf) |

</details>


<details>
<summary><h2>DS-2CD1T47G2H-LIU - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.41 | Applied to: [DS-2CD1T47G2H-LIUF(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.41_260401_S3000712602.zip) | 2026-04-01 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.41_260401_S3000712602.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202604/releasenote%5CNetwork_Camera-V5.8.41_SP1_Release_Note-E10.pdf) |
| 5.8.10 | Applied to: [DS-2CD1T47G2H-LIU(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.100_260416_S3000716492.zip) | 2025-07-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.100_260416_S3000716492.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202508/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-E10.pdf) |

</details>


<details>
<summary><h2>DS-2CD1T47G2H-LIUF - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.41 | Applied to: [DS-2CD1T47G2H-LIUF/SL(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.41_260401_S3000712602.zip) | 2026-04-01 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.41_260401_S3000712602.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202604/releasenote%5CNetwork_Camera-V5.8.41_SP1_Release_Note-E10.pdf) |
| 5.8.10 | Applied to: [DS-2CD1T47G2H-LIUF/SRB(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.100_260416_S3000716492.zip) | 2025-07-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.100_260416_S3000716492.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202508/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-E10.pdf) |

</details>


<details>
<summary><h2>DS-2CD1T47G3-LIU - IPC_G0 (3 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.9.13 | Applied to: [DS-2CD1T47G3-LIUF/LSL(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.9.13_251124_S3000688200.zip) | 2025-11-24 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.9.13_251124_S3000688200.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.9.13_251124_Release_Note-IPCE_E_E15.pdf) |
| 5.9.12 | Applied to: [DS-2CD1T47G3-LIU/SRB(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.9.12_260407_S3000713711.zip) | 2025-09-19 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.9.12_260407_S3000713711.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202511/releasenote%5CNetwork_Camera-V5.9.12_250919_Release_Note-IPCE_E_E15.pdf) |
| 5.9.11 | Applied to: [DS-2CD1T47G3-LIU/SRB(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.9.11_251030_S3000682327.zip) | 2025-08-22 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.9.11_251030_S3000682327.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202511/releasenote%5CNetwork_Camera-V5.9.12_250919_Release_Note-IPCE_E_E15.pdf) |

</details>


<details>
<summary><h2>DS-2CD1T47G3H-LIU - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD1T47G3H-LIU/SL(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | 2025-12-10 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) |  |
| 5.8.21 | Applied to: [DS-2CD1T47G3H-LIU/SRB(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.21_250714_S3000661481.zip) | 2025-11-17 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.21_250714_S3000661481.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.8.21_SP1_251117_Release_Note-H13U.pdf) |

</details>


<details>
<summary><h2>DS-2CD1T63G2P-LIUF - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.12 | Applied to: [DS-2CD1T63G2P-LIUF/SRB(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.12_260416_S3000716519.zip) | 2026-04-16 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.12_260416_S3000716519.zip) |  |
| 5.8.11 | Applied to: [DS-2CD1T63G2P-LIUF/SL(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.110_260421_S3000717992.zip) | 2025-10-29 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.110_260421_S3000717992.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202511/releasenote%5CNetwork_Camera-V5.8.11_SP1_251029_Release_Note-IPCE_P_E11.pdf) |

</details>


<details>
<summary><h2>DS-2CD1T63G2P-LIUF-S-L--RB- - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.12 | [DS-2CD1T63G2P-LIUF-S-L--RB-](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.12_260416_S3000716513.zip) | 2026-04-16 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.12_260416_S3000716513.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202605/releasenote%5CNetwork_Camera-V5.8.12_260416_Release_IPCE_P_E11.pdf) |

</details>


<details>
<summary><h2>DS-2CD1T67G2H-LIUF - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.21 | Applied to: [DS-2CD1T67G2H-LIUF/SRB(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.21_250714_S3000661481.zip) | 2025-05-08 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.21_250714_S3000661481.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202507/releasenote%5CNetwork_Camera-V5.8.21_Release_Note-E12.pdf) |

</details>


<details>
<summary><h2>DS-2CD1T67G2HP-LIUF - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.12 | Applied to: [DS-2CD1T67G2HP-LIUF/SRB(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.12_260416_S3000716519.zip) | 2026-04-16 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.12_260416_S3000716519.zip) |  |
| 5.8.11 | Applied to: [DS-2CD1T67G2HP-LIUF/SRB(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.110_260421_S3000717992.zip) | 2025-10-29 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.110_260421_S3000717992.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202511/releasenote%5CNetwork_Camera-V5.8.11_SP1_251029_Release_Note-IPCE_P_E11.pdf) |

</details>


<details>
<summary><h2>DS-2CD1T67G2HP-LIUF-S-L--RB- - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.12 | [DS-2CD1T67G2HP-LIUF-S-L--RB-](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.12_260416_S3000716513.zip) | 2026-04-16 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.12_260416_S3000716513.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202605/releasenote%5CNetwork_Camera-V5.8.12_260416_Release_IPCE_P_E11.pdf) |

</details>


<details>
<summary><h2>DS-2CD1T67G3-LIU - IPC_G0 (3 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.9.13 | Applied to: [DS-2CD1T67G3-LIU/LSL(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.9.13_251124_S3000688200.zip) | 2025-11-24 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.9.13_251124_S3000688200.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.9.13_251124_Release_Note-IPCE_E_E15.pdf) |
| 5.9.12 | Applied to: [DS-2CD1T67G3-LIU/SRB(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.9.12_260407_S3000713711.zip) | 2025-09-19 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.9.12_260407_S3000713711.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202511/releasenote%5CNetwork_Camera-V5.9.12_250919_Release_Note-IPCE_E_E15.pdf) |
| 5.9.11 | Applied to: [DS-2CD1T67G3-LIU/SRB(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.9.11_251030_S3000682327.zip) | 2025-08-22 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.9.11_251030_S3000682327.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202511/releasenote%5CNetwork_Camera-V5.9.12_250919_Release_Note-IPCE_E_E15.pdf) |

</details>


<details>
<summary><h2>DS-2CD1T83G0-I - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD1T83G0-I(4mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip)(C) | 2024-10-08 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202507/releasenote%5CNetwork_Camera-V5.7.23_SP_Release_Note-E8.pdf) |

</details>


<details>
<summary><h2>DS-2CD1T83G2P-LIUF - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.12 | Applied to: [DS-2CD1T83G2P-LIUF/SRB(2mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.12_260416_S3000716519.zip) | 2026-04-16 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.12_260416_S3000716519.zip) |  |
| 5.8.11 | Applied to: [DS-2CD1T83G2P-LIUF/SL(2mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.110_260421_S3000717992.zip) | 2025-10-29 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.110_260421_S3000717992.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202511/releasenote%5CNetwork_Camera-V5.8.11_SP1_251029_Release_Note-IPCE_P_E11.pdf) |

</details>


<details>
<summary><h2>DS-2CD1T83G2P-LIUF-S-L--RB- - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.12 | [DS-2CD1T83G2P-LIUF-S-L--RB-](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.12_260416_S3000716513.zip) | 2026-04-16 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.12_260416_S3000716513.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202605/releasenote%5CNetwork_Camera-V5.8.12_260416_Release_IPCE_P_E11.pdf) |

</details>


<details>
<summary><h2>DS-2CD20123G2-LI - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.2 | Applied to: [DS-2CD20123G2-LIUY(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.23_260403_S3000712869.zip) | 2025-11-03 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.23_260403_S3000712869.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202511/releasenote%5CNetwork_Camera-V5.8.2_251103_Release_Note-IPCE_G9.pdf) |

</details>


<details>
<summary><h2>DS-2CD20123G2-LIUY - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.2 | Applied to: [DS-2CD20123G2-LIUY/SL(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.23_260403_S3000712869.zip) | 2025-11-03 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.23_260403_S3000712869.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202511/releasenote%5CNetwork_Camera-V5.8.2_251103_Release_Note-IPCE_G9.pdf) |

</details>


<details>
<summary><h2>DS-2CD20126G3-I - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.2 | Applied to: [DS-2CD20126G3-IY(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.23_260403_S3000712869.zip)(eF) | 2025-11-03 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.23_260403_S3000712869.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202511/releasenote%5CNetwork_Camera-V5.8.2_251103_Release_Note-IPCE_G9.pdf) |

</details>


<details>
<summary><h2>DS-2CD20126G3-IUY - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.3 | Applied to: [DS-2CD20126G3-IUY/SRB(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.3_260416_S3000716238.zip)eFO-STDBLACK | 2026-03-20 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.3_260416_S3000716238.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202604/releasenote%5CNetwork_Camera-V5.8.3_SP1_260320_Release_Note-IPCE_G9.pdf) |
| 5.8.2 | Applied to: [DS-2CD20126G3-IUY/SRB(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.23_260403_S3000712869.zip)eFO-STDBLACK | 2025-11-03 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.23_260403_S3000712869.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202511/releasenote%5CNetwork_Camera-V5.8.2_251103_Release_Note-IPCE_G9.pdf) |

</details>


<details>
<summary><h2>DS-2CD20166G3-I - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.2 | Applied to: [DS-2CD20166G3-IUY(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.23_260403_S3000712869.zip)(eF) | 2025-11-03 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.23_260403_S3000712869.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202511/releasenote%5CNetwork_Camera-V5.8.2_251103_Release_Note-IPCE_G9.pdf) |

</details>


<details>
<summary><h2>DS-2CD20166G3-IUY - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.2 | Applied to: [DS-2CD20166G3-IUY/SL(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.23_260403_S3000712869.zip)(eF) | 2025-11-03 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.23_260403_S3000712869.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202511/releasenote%5CNetwork_Camera-V5.8.2_251103_Release_Note-IPCE_G9.pdf) |

</details>


<details>
<summary><h2>DS-2CD2021G1-I - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2021G1-I(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip)(B) | 2024-12-11 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202507/releasenote%5CNetwork_Camera-V5.7.23_SP2_Release_Note-E8.pdf) |
| 5.5.800 | Applied to: [DS-2CD2021G1-I(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.800_211009_S3000390724.zip)(B) | 2021-06-28 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.800_211009_S3000390724.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202507/releasenote%5CNetwork_Camera-V5.7.23_SP2_Release_Note-E8.pdf) |

</details>


<details>
<summary><h2>DS-2CD2021G1-IDW - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.800 | Applied to: [DS-2CD2021G1-IDW1(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.800_211009_S3000390724.zip) | 2021-06-28 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.800_211009_S3000390724.zip) |  |

</details>


<details>
<summary><h2>DS-2CD2023G0-I - IPC_G1 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.6.821 | Applied to: [DS-2CD2023G0-I(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.6.821_230831_S3000525150.zip)(BLACK) | 2023-08-31 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.6.821_230831_S3000525150.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202401/releasenote%5CNetwork_Camera-V5.6.821_Release_Note-IPC_G1_230831.pdf) |

</details>


<details>
<summary><h2>DS-2CD2023G2-I - IPC_G0 (4 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2023G2-I(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip)(D) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202507/releasenote%5CNetwork_Camera-V5.7.0_SP6_Release_Note-G6_I.pdf) |
| 5.7.19 | Applied to: [DS-2CD2023G2-I(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.19_241207_S3000618493.zip)(D) | 2024-12-07 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.19_241207_S3000618493.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202507/releasenote%5CNetwork_Camera-V5.7.0_SP6_Release_Note-G6_I.pdf) |
| 5.7.0 | Applied to: [DS-2CD2023G2-I(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.0_240129_S3000555034.zip)(D) | 2024-10-23 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.0_240129_S3000555034.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202507/releasenote%5CNetwork_Camera-V5.7.0_SP6_Release_Note-G6_I.pdf) |
| 5.7.18 | Applied to: [DS-2CD2023G2-I(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.18_240826_S3000597013.zip)(D) | 2024-08-26 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.18_240826_S3000597013.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202507/releasenote%5CNetwork_Camera-V5.7.0_SP6_Release_Note-G6_I.pdf) |

</details>


<details>
<summary><h2>DS-2CD2023G2-IU - IPC_G0 (3 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2023G2-I(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip)(D) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202507/releasenote%5CNetwork_Camera-V5.7.0_SP6_Release_Note-G6_I.pdf) |
| 5.7.0 | Applied to: [DS-2CD2023G2-I(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.0_240129_S3000555034.zip)(D) | 2024-10-23 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.0_240129_S3000555034.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202507/releasenote%5CNetwork_Camera-V5.7.0_SP6_Release_Note-G6_I.pdf) |
| 5.7.18 | Applied to: [DS-2CD2023G2-I(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.18_240826_S3000597013.zip)(D) | 2024-08-26 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.18_240826_S3000597013.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202507/releasenote%5CNetwork_Camera-V5.7.0_SP6_Release_Note-G6_I.pdf) |

</details>


<details>
<summary><h2>DS-2CD2023G2-LI - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2023G2-LI(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |
| 5.7.19 | Applied to: [DS-2CD2023G2-LI(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.19_241207_S3000618493.zip) | 2024-12-07 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.19_241207_S3000618493.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.19_241207_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2023G2-LI2U - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2023G2-LI2U/SL(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |
| 5.7.19 | Applied to: [DS-2CD2023G2-LI2U/SL(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.19_241207_S3000618493.zip) | 2024-12-07 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.19_241207_S3000618493.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.19_241207_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2025FHWD-I - IPC_G1 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.6.821 | Applied to: [DS-2CD2025FHWD-I(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.6.821_230831_S3000525150.zip) | 2023-08-31 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.6.821_230831_S3000525150.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202401/releasenote%5CNetwork_Camera-V5.6.821_Release_Note-IPC_G1_230831.pdf) |

</details>


<details>
<summary><h2>DS-2CD2025FWD-I - IPC_G1 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.6.821 | Applied to: [DS-2CD2025FWD-I(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.6.821_230831_S3000525150.zip) | 2023-08-31 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.6.821_230831_S3000525150.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202401/releasenote%5CNetwork_Camera-V5.6.821_Release_Note-IPC_G1_230831.pdf) |

</details>


<details>
<summary><h2>DS-2CD2026G2-I - IPC_G0 (5 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2026G2-I(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202408/releasenote%5CNetwork_Camera-V5.5.820_Release_Note-G3.pdf) |
| 5.7.19 | Applied to: [DS-2CD2026G2-I(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.19_241207_S3000618493.zip) | 2024-12-07 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.19_241207_S3000618493.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202408/releasenote%5CNetwork_Camera-V5.5.820_Release_Note-G3.pdf) |
| 5.7.0 | Applied to: [DS-2CD2026G2-I(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.0_240129_S3000555034.zip) | 2024-10-23 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.0_240129_S3000555034.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202408/releasenote%5CNetwork_Camera-V5.5.820_Release_Note-G3.pdf) |
| 5.5.820 | Applied to: [DS-2CD2026G2-I(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.820_260410_S3000715634.zip) | 2023-11-08 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.820_260410_S3000715634.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202408/releasenote%5CNetwork_Camera-V5.5.820_Release_Note-G3.pdf) |
| 5.5.800 | Applied to: [DS-2CD2026G2-I(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.800_211009_S3000390724.zip) | 2021-10-09 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.800_211009_S3000390724.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202408/releasenote%5CNetwork_Camera-V5.5.820_Release_Note-G3.pdf) |

</details>


<details>
<summary><h2>DS-2CD2026G2-IU - IPC_G0 (3 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2026G2-IU/SL(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202408/releasenote%5CNetwork_Camera-V5.5.820_Release_Note-G3.pdf) |
| 5.7.19 | Applied to: [DS-2CD2026G2-IU/SL(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.19_241207_S3000618493.zip) | 2024-12-07 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.19_241207_S3000618493.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202408/releasenote%5CNetwork_Camera-V5.5.820_Release_Note-G3.pdf) |
| 5.5.820 | Applied to: [DS-2CD2026G2-IU/SL(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.820_260410_S3000715634.zip) | 2023-11-08 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.820_260410_S3000715634.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202408/releasenote%5CNetwork_Camera-V5.5.820_Release_Note-G3.pdf) |

</details>


<details>
<summary><h2>DS-2CD2027G2-L - IPC_G0 (3 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2027G2-LU(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202408/releasenote%5CNetwork_Camera-V5.5.820_Release_Note-G3.pdf) |
| 5.7.19 | Applied to: [DS-2CD2027G2-LU(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.19_241207_S3000618493.zip) | 2024-12-07 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.19_241207_S3000618493.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202408/releasenote%5CNetwork_Camera-V5.5.820_Release_Note-G3.pdf) |
| 5.5.820 | Applied to: [DS-2CD2027G2-LU(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.820_260410_S3000715634.zip) | 2023-11-08 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.820_260410_S3000715634.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202408/releasenote%5CNetwork_Camera-V5.5.820_Release_Note-G3.pdf) |

</details>


<details>
<summary><h2>DS-2CD2041G1-IDW - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.89 | Applied to: [DS-2CD2041G1-IDW1(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/87acab3e-5d46-45cd-88c4-87b51139b600.zip) | 2021-04-29 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/87acab3e-5d46-45cd-88c4-87b51139b600.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202312/releasenote%5CNetwork_Camera_V5.5.89_Release_Note_--G0.pdf) |
| 5.5.82 | Applied to: [DS-2CD2041G1-IDW1(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.820_260410_S3000715634.zip) | 2019-01-30 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.820_260410_S3000715634.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202312/releasenote%5CNetwork_Camera_V5.5.89_Release_Note_--G0.pdf) |

</details>


<details>
<summary><h2>DS-2CD2043G0-I - IPC_G1 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.6.821 | Applied to: [DS-2CD2043G0-I(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.6.821_230831_S3000525150.zip) | 2023-08-31 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.6.821_230831_S3000525150.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202401/releasenote%5CNetwork_Camera-V5.6.821_Release_Note-IPC_G1_230831.pdf) |

</details>


<details>
<summary><h2>DS-2CD2043G2-I - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2043G2-I(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |
| 5.7.19 | Applied to: [DS-2CD2043G2-I(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.19_241207_S3000618493.zip) | 2024-12-07 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.19_241207_S3000618493.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.19_241207_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2043G2-IU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2043G2-I(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2043G2-LI - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2043G2-LI(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |
| 5.7.19 | Applied to: [DS-2CD2043G2-LI(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.19_241207_S3000618493.zip) | 2024-12-07 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.19_241207_S3000618493.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.19_241207_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2043G2-LI2U - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2043G2-LI2U/SL(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |
| 5.7.19 | Applied to: [DS-2CD2043G2-LI2U/SL(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.19_241207_S3000618493.zip) | 2024-12-07 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.19_241207_S3000618493.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.19_241207_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2043G2-LIZ - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD2043G2-LIZY(2.8/4mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | 2025-12-10 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13U.pdf) |
| 5.8.21 | Applied to: [DS-2CD2043G2-LIZY(2.8/4mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.21_250714_S3000661481.zip) | 2025-11-17 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.21_250714_S3000661481.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.8.21_SP1_251117_Release_Note-H13U.pdf) |

</details>


<details>
<summary><h2>DS-2CD2043G2-LIZ2UY - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD2043G2-LIZ2UY/SRB(2.8/4mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | 2025-12-10 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13U.pdf) |
| 5.8.21 | Applied to: [DS-2CD2043G2-LIZ2UY/SL(2.8/4mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.21_250714_S3000661481.zip) | 2025-11-17 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.21_250714_S3000661481.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.8.21_SP1_251117_Release_Note-H13U.pdf) |

</details>


<details>
<summary><h2>DS-2CD2045FWD-I - IPC_G1 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.6.821 | Applied to: [DS-2CD2045FWD-I(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.6.821_230831_S3000525150.zip)(BLACK) | 2023-08-31 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.6.821_230831_S3000525150.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202401/releasenote%5CNetwork_Camera-V5.6.821_Release_Note-IPC_G1_230831.pdf) |
| 5.6.820 | Applied to: [DS-2CD2045FWD-I(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.6.820_220519_S3000430633.zip)(BLACK) | 2022-05-19 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.6.820_220519_S3000430633.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202401/releasenote%5CNetwork_Camera-V5.6.821_Release_Note-IPC_G1_230831.pdf) |

</details>


<details>
<summary><h2>DS-2CD2046G2-I - IPC_G0 (4 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2046G2-IU(6mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip)(C) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |
| 5.7.19 | Applied to: [DS-2CD2046G2-IU(6mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.19_241207_S3000618493.zip)(C) | 2024-12-07 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.19_241207_S3000618493.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.19_241207_Release_Note.pdf) |
| 5.5.820 | Applied to: [DS-2CD2046G2-IU(6mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.820_260410_S3000715634.zip)(C) | 2023-11-08 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.820_260410_S3000715634.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.19_241207_Release_Note.pdf) |
| 5.5.800 | Applied to: [DS-2CD2046G2-IU(6mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.800_211009_S3000390724.zip)(C) | 2021-10-09 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.800_211009_S3000390724.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.19_241207_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2046G2-IU - IPC_G0 (4 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2046G2-IU/SL(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/330c4c2c-5730-4877-a942-0be87cea67ca.pdf) |
| 5.7.19 | Applied to: [DS-2CD2046G2-IU/SL(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.19_241207_S3000618493.zip) | 2024-12-07 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.19_241207_S3000618493.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/330c4c2c-5730-4877-a942-0be87cea67ca.pdf) |
| 5.5.820 | Applied to: [DS-2CD2046G2-IU/SL(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.820_260410_S3000715634.zip) | 2023-11-08 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.820_260410_S3000715634.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/330c4c2c-5730-4877-a942-0be87cea67ca.pdf) |
| 5.5.800 | Applied to: [DS-2CD2046G2-IU/SL(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.800_211009_S3000390724.zip) | 2021-10-09 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.800_211009_S3000390724.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/330c4c2c-5730-4877-a942-0be87cea67ca.pdf) |

</details>


<details>
<summary><h2>DS-2CD2046G2H-I - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2046G2H-IU(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip)(eF) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |
| 5.7.19 | Applied to: [DS-2CD2046G2H-IU(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.19_241207_S3000618493.zip)(eF) | 2024-12-07 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.19_241207_S3000618493.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.19_241207_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2046G2H-I2U - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2046G2H-I2U/SL(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip)(eF) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |
| 5.7.19 | Applied to: [DS-2CD2046G2H-I2U/SL(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.19_241207_S3000618493.zip)(eF) | 2024-12-07 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.19_241207_S3000618493.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.19_241207_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2046G3-IZ - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD2046G3-IZY(2.8/4mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | 2025-12-10 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13U.pdf) |
| 5.8.21 | Applied to: [DS-2CD2046G3-IZ2UY(2.8/4mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.21_250714_S3000661481.zip) | 2025-11-17 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.21_250714_S3000661481.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.8.21_SP1_251117_Release_Note-H13U.pdf) |

</details>


<details>
<summary><h2>DS-2CD2046G3-IZ2UY - IPC_G0 (3 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.32 | Applied to: [DS-2CD2046G3-IZ2UY/SRB(2.8/4)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.32_260423_S3000719136.zip)O-STDBLACK | 2026-03-30 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.32_260423_S3000719136.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202604/releasenote%5CNetwork_Camera-V5.8.32_SP1_260330_Release_Note-H13U.pdf) |
| 5.8.30 | Applied to: [DS-2CD2046G3-IZ2UY/SRB(2.8/4)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip)O-STDBLACK | 2025-12-10 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13U.pdf) |
| 5.8.21 | Applied to: [DS-2CD2046G3-IZ2UY/SRB(2.8/4)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.21_250714_S3000661481.zip)O-STDBLACK | 2025-11-17 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.21_250714_S3000661481.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.8.21_SP1_251117_Release_Note-H13U.pdf) |

</details>


<details>
<summary><h2>DS-2CD2047G2-L - IPC_G0 (4 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2047G2-LU(6mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip)(C) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |
| 5.7.19 | Applied to: [DS-2CD2047G2-LU(6mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.19_241207_S3000618493.zip)(C) | 2024-12-07 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.19_241207_S3000618493.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.19_241207_Release_Note.pdf) |
| 5.5.820 | Applied to: [DS-2CD2047G2-LU(6mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.820_260410_S3000715634.zip)(C) | 2023-11-08 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.820_260410_S3000715634.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.19_241207_Release_Note.pdf) |
| 5.5.800 | Applied to: [DS-2CD2047G2-LU(6mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.800_211009_S3000390724.zip)(C) | 2021-10-09 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.800_211009_S3000390724.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.19_241207_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2047G2-LU - IPC_G0 (4 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2047G2-LU/SL(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip)(C) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |
| 5.7.19 | Applied to: [DS-2CD2047G2-LU/SL(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.19_241207_S3000618493.zip)(C) | 2024-12-07 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.19_241207_S3000618493.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.19_241207_Release_Note.pdf) |
| 5.5.820 | Applied to: [DS-2CD2047G2-LU(6mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.820_260410_S3000715634.zip)(C) | 2023-11-08 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.820_260410_S3000715634.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |
| 5.5.800 | Applied to: [DS-2CD2047G2-LU(6mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.800_211009_S3000390724.zip)(C) | 2021-10-09 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.800_211009_S3000390724.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2047G2H-LIU - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2047G2H-LI(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip)(eF) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |
| 5.7.19 | Applied to: [DS-2CD2047G2H-LI(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.19_241207_S3000618493.zip)(eF) | 2024-12-07 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.19_241207_S3000618493.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.19_241207_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2047G3-LI - IPC_G0 (3 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.32 | Applied to: [DS-2CD2047G3-LIY(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.32_260423_S3000719136.zip) | 2026-03-30 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.32_260423_S3000719136.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202604/releasenote%5CNetwork_Camera-V5.8.32_SP1_260330_Release_Note-H13U.pdf) |
| 5.8.30 | Applied to: [DS-2CD2047G3-LI2UY(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip)(BLACK) | 2025-12-10 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13U.pdf) |
| 5.8.21 | Applied to: [DS-2CD2047G3-LIY(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.21_250714_S3000661481.zip) | 2025-11-17 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.21_250714_S3000661481.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.8.21_SP1_251117_Release_Note-H13U.pdf) |

</details>


<details>
<summary><h2>DS-2CD2047G3-LI2UY - IPC_G0 (3 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.32 | Applied to: [DS-2CD2047G3-LI2UY/SL(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.32_260423_S3000719136.zip) | 2026-03-30 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.32_260423_S3000719136.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202604/releasenote%5CNetwork_Camera-V5.8.32_SP1_260330_Release_Note-H13U.pdf) |
| 5.8.30 | Applied to: [DS-2CD2047G3-LI2UY/SL(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | 2025-12-10 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13U.pdf) |
| 5.8.21 | Applied to: [DS-2CD2047G3-LI2UY/SL(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.21_250714_S3000661481.zip) | 2025-11-17 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.21_250714_S3000661481.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.8.21_SP1_251117_Release_Note-H13U.pdf) |

</details>


<details>
<summary><h2>DS-2CD2051G1-IDW - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.82 | Applied to: [DS-2CD2051G1-IDW1(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.820_260410_S3000715634.zip) | 2019-01-30 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.820_260410_S3000715634.zip) |  |

</details>


<details>
<summary><h2>DS-2CD2063G0-I - IPC_G1 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.6.821 | Applied to: [DS-2CD2063G0-I(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.6.821_230831_S3000525150.zip) | 2023-08-31 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.6.821_230831_S3000525150.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202401/releasenote%5CNetwork_Camera-V5.6.821_Release_Note-IPC_G1_230831.pdf) |

</details>


<details>
<summary><h2>DS-2CD2063G2-I - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2063G2-IU(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |
| 5.7.19 | Applied to: [DS-2CD2063G2-IU(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.19_241207_S3000618493.zip) | 2024-12-07 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.19_241207_S3000618493.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.19_241207_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2063G2-LI - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2063G2-LI(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |
| 5.7.19 | Applied to: [DS-2CD2063G2-LI(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.19_241207_S3000618493.zip) | 2024-12-07 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.19_241207_S3000618493.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.19_241207_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2063G2-LI2U - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2063G2-LI2U/SL(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |
| 5.7.19 | Applied to: [DS-2CD2063G2-LI2U/SL(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.19_241207_S3000618493.zip) | 2024-12-07 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.19_241207_S3000618493.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.19_241207_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2065G1-I - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.6.820 | Applied to: [DS-2CD2065G1-I(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.6.820_220519_S3000430633.zip)(BLACK) | 2022-05-19 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.6.820_220519_S3000430633.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202301/Network%20Camera%20V5.6.820%20Release%20Note%20--G1.pdf) |

</details>


<details>
<summary><h2>DS-2CD2066G2-I - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2066G2-IU(6mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip)(C) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |
| 5.7.19 | Applied to: [DS-2CD2066G2-IU(6mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.19_241207_S3000618493.zip)(C) | 2024-12-07 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.19_241207_S3000618493.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.19_241207_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2066G2-IU - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2066G2-IU/SL(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip)(C) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |
| 5.7.19 | Applied to: [DS-2CD2066G2-IU/SL(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.19_241207_S3000618493.zip)(C) | 2024-12-07 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.19_241207_S3000618493.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.19_241207_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2066G2H-I - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2066G2H-IU(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip)(eF) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |
| 5.7.19 | Applied to: [DS-2CD2066G2H-IU(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.19_241207_S3000618493.zip)(eF) | 2024-12-07 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.19_241207_S3000618493.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.19_241207_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2066G2H-I2U - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2066G2H-I2U/SL(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip)/eFO-STDBLACK | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |
| 5.7.19 | Applied to: [DS-2CD2066G2H-I2U/SL(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.19_241207_S3000618493.zip)/eFO-STDBLACK | 2024-12-07 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.19_241207_S3000618493.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.19_241207_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2067G2-L - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2067G2-LU(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip)(C) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |
| 5.7.19 | Applied to: [DS-2CD2067G2-LU(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.19_241207_S3000618493.zip)(C) | 2024-12-07 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.19_241207_S3000618493.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.19_241207_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2067G2H-LIU - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2067G2H-LI(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip)(eF) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |
| 5.7.19 | Applied to: [DS-2CD2067G2H-LI(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.19_241207_S3000618493.zip)(eF) | 2024-12-07 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.19_241207_S3000618493.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.19_241207_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2067G3-LI - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD2067G3-LI2UY(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | 2025-12-10 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD2067G3-LI2UY - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD2067G3-LI2UY/SL(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | 2025-12-10 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD2083G0-I - IPC_G1 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.6.821 | Applied to: [DS-2CD2083G0-I(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.6.821_230831_S3000525150.zip) | 2023-08-31 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.6.821_230831_S3000525150.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202401/releasenote%5CNetwork_Camera-V5.6.821_Release_Note-IPC_G1_230831.pdf) |

</details>


<details>
<summary><h2>DS-2CD2083G2-I - IPC_G0 (4 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.6 | Applied to: [DS-2CD2083G2-I(6mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.6_260128_S3000701683.zip)(D) | 2026-01-28 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.6_260128_S3000701683.zip) |  |
| 5.7.23 | Applied to: [DS-2CD2083G2-I(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |
| 5.7.5 | Applied to: [DS-2CD2083G2-I(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.55_241108_S3000612871.zip) | 2025-07-18 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.55_241108_S3000612871.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.19_241207_Release_Note.pdf) |
| 5.7.19 | Applied to: [DS-2CD2083G2-I(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.19_241207_S3000618493.zip) | 2024-12-07 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.19_241207_S3000618493.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.19_241207_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2083G2-IU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2083G2-I(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2083G2-LI - IPC_G0 (4 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.6 | Applied to: [DS-2CD2083G2-LI(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.6_260128_S3000701683.zip)(T) | 2026-01-28 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.6_260128_S3000701683.zip) |  |
| 5.7.23 | Applied to: [DS-2CD2083G2-LI(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |
| 5.7.19 | Applied to: [DS-2CD2083G2-LI(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.19_241207_S3000618493.zip) | 2024-12-07 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.19_241207_S3000618493.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.19_241207_Release_Note.pdf) |
| 5.7.5 | Applied to: [DS-2CD2083G2-LI(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.55_241108_S3000612871.zip) | 2024-11-03 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.55_241108_S3000612871.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.19_241207_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2083G2-LI2U - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2083G2-LI2U/SL(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |
| 5.7.19 | Applied to: [DS-2CD2083G2-LI2U/SL(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.19_241207_S3000618493.zip) | 2024-12-07 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.19_241207_S3000618493.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.19_241207_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2085G1-I - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.6.820 | Applied to: [DS-2CD2085G1-I(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.6.820_220519_S3000430633.zip)(BLACK) | 2022-05-19 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.6.820_220519_S3000430633.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202301/Network%20Camera%20V5.6.820%20Release%20Note%20--G1.pdf) |
| 5.6.6 | Applied to: [DS-2CD2085G1-I(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/f18aceb7-b896-4c7d-ad2e-8f0d2a91bcc3.zip)(BLACK) | 2021-06-25 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/f18aceb7-b896-4c7d-ad2e-8f0d2a91bcc3.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202301/Network%20Camera%20V5.6.820%20Release%20Note%20--G1.pdf) |

</details>


<details>
<summary><h2>DS-2CD2086G2-I - IPC_G0 (3 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2086G2-I(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip)(C) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |
| 5.7.19 | Applied to: [DS-2CD2086G2-I(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.19_241207_S3000618493.zip)(C) | 2024-12-07 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.19_241207_S3000618493.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.19_241207_Release_Note.pdf) |
| 5.5.820 | Applied to: [DS-2CD2086G2-I(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.820_260410_S3000715634.zip)(C) | 2023-11-08 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.820_260410_S3000715634.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.19_241207_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2086G2-IU - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2086G2-IU/SL(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip)(C) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |
| 5.7.19 | Applied to: [DS-2CD2086G2-IU/SL(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.19_241207_S3000618493.zip)(C) | 2024-12-07 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.19_241207_S3000618493.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.19_241207_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2086G2H-I - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2086G2H-I(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip)(eF) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |
| 5.7.19 | Applied to: [DS-2CD2086G2H-I(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.19_241207_S3000618493.zip)(eF) | 2024-12-07 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.19_241207_S3000618493.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.19_241207_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2086G2H-I2U - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2086G2H-I2U/SL(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip)(eF) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |
| 5.7.19 | Applied to: [DS-2CD2086G2H-I2U/SL(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.19_241207_S3000618493.zip)(eF) | 2024-12-07 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.19_241207_S3000618493.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.19_241207_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2087G2-L - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2087G2-LU(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip)(C) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |
| 5.7.19 | Applied to: [DS-2CD2087G2-LU(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.19_241207_S3000618493.zip)(C) | 2024-12-07 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.19_241207_S3000618493.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.19_241207_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2087G2H-LI - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2087G2H-LI(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip)(eF) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |
| 5.7.19 | Applied to: [DS-2CD2087G2H-LI(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.19_241207_S3000618493.zip)(eF) | 2024-12-07 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.19_241207_S3000618493.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.19_241207_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2087G2H-LIU - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2087G2H-LIU/SL(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip)(eF) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |
| 5.7.19 | Applied to: [DS-2CD2087G2H-LIU/SL(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.19_241207_S3000618493.zip)(eF) | 2024-12-07 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.19_241207_S3000618493.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.19_241207_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2087G3-LI - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.32 | Applied to: [DS-2CD2087G3-LI2UY(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.32_260423_S3000719136.zip)(BLACK) | 2026-03-30 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.32_260423_S3000719136.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202604/releasenote%5CNetwork_Camera-V5.8.32_SP1_260330_Release_Note-H13.pdf) |
| 5.8.30 | Applied to: [DS-2CD2087G3-LIY(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | 2025-12-10 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD2087G3-LI2UY - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD2087G3-LI2UY/SL(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | 2025-12-10 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD2121G0-I - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2121G0-IS(4mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | 2024-12-11 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202507/releasenote%5CNetwork_Camera-V5.7.23_SP2_Release_Note-E8.pdf) |
| 5.5.800 | Applied to: [DS-2CD2121G0-IS(4mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.800_211009_S3000390724.zip) | 2021-06-28 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.800_211009_S3000390724.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202507/releasenote%5CNetwork_Camera-V5.7.23_SP2_Release_Note-E8.pdf) |

</details>


<details>
<summary><h2>DS-2CD2121G1-IDW - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.821 | Applied to: [DS-2CD2121G1-IDW1(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.821_231108_S3000539548.zip) | 2023-11-08 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.821_231108_S3000539548.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202404/1712790068455/releasenote%5CIPC_E6_5.5.821_Release_Note.pdf) |
| 5.5.800 | Applied to: [DS-2CD2121G1-IDW1(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.800_211009_S3000390724.zip) | 2021-06-28 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.800_211009_S3000390724.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202404/1712790068455/releasenote%5CIPC_E6_5.5.821_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2123G0-I - IPC_G1 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.6.821 | Applied to: [DS-2CD2123G0-IS(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.6.821_230831_S3000525150.zip)(BLACK) | 2023-08-31 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.6.821_230831_S3000525150.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202401/releasenote%5CNetwork_Camera-V5.6.821_Release_Note-IPC_G1_230831.pdf) |

</details>


<details>
<summary><h2>DS-2CD2123G0-IU - IPC_G1 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.6.821 | Applied to: [DS-2CD2123G0-IU(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.6.821_230831_S3000525150.zip) | 2023-08-31 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.6.821_230831_S3000525150.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202401/releasenote%5CNetwork_Camera-V5.6.821_Release_Note-IPC_G1_230831.pdf) |

</details>


<details>
<summary><h2>DS-2CD2123G2-I - IPC_G0 (4 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2123G2-I(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip)(D)(BLACK) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202507/releasenote%5CNetwork_Camera-V5.7.0_SP6_Release_Note-G6_I.pdf) |
| 5.7.19 | Applied to: [DS-2CD2123G2-I(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.19_241207_S3000618493.zip)(D)(BLACK) | 2024-12-07 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.19_241207_S3000618493.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202507/releasenote%5CNetwork_Camera-V5.7.0_SP6_Release_Note-G6_I.pdf) |
| 5.7.0 | Applied to: [DS-2CD2123G2-I(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.0_240129_S3000555034.zip)(D)(BLACK) | 2024-10-23 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.0_240129_S3000555034.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202507/releasenote%5CNetwork_Camera-V5.7.0_SP6_Release_Note-G6_I.pdf) |
| 5.7.18 | Applied to: [DS-2CD2123G2-I(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.18_240826_S3000597013.zip)(D)(BLACK) | 2024-08-26 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.18_240826_S3000597013.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202507/releasenote%5CNetwork_Camera-V5.7.0_SP6_Release_Note-G6_I.pdf) |

</details>


<details>
<summary><h2>DS-2CD2123G2-IU - IPC_G0 (3 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2123G2-IU(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip)(D) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202507/releasenote%5CNetwork_Camera-V5.7.0_SP6_Release_Note-G6_I.pdf) |
| 5.7.19 | Applied to: [DS-2CD2123G2-IU(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.19_241207_S3000618493.zip)(D) | 2024-12-07 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.19_241207_S3000618493.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202507/releasenote%5CNetwork_Camera-V5.7.0_SP6_Release_Note-G6_I.pdf) |
| 5.7.0 | Applied to: [DS-2CD2123G2-IU(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.0_240129_S3000555034.zip)(D) | 2024-10-23 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.0_240129_S3000555034.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202507/releasenote%5CNetwork_Camera-V5.7.0_SP6_Release_Note-G6_I.pdf) |

</details>


<details>
<summary><h2>DS-2CD2123G2-LI - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2123G2-LI(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |
| 5.7.19 | Applied to: [DS-2CD2123G2-LI(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.19_241207_S3000618493.zip) | 2024-12-07 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.19_241207_S3000618493.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.19_241207_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2125FHWD-I - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.6.820 | Applied to: [DS-2CD2125FHWD-I(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.6.820_220519_S3000430633.zip) | 2022-05-19 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.6.820_220519_S3000430633.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202301/Network%20Camera%20V5.6.820%20Release%20Note%20--G1.pdf) |
| 5.6.6 | Applied to: [DS-2CD2125FHWD-I(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/f18aceb7-b896-4c7d-ad2e-8f0d2a91bcc3.zip) | 2021-06-25 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/f18aceb7-b896-4c7d-ad2e-8f0d2a91bcc3.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202301/Network%20Camera%20V5.6.820%20Release%20Note%20--G1.pdf) |

</details>


<details>
<summary><h2>DS-2CD2125FWD-I - IPC_G1 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.6.821 | Applied to: [DS-2CD2125FWD-IS(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.6.821_230831_S3000525150.zip) | 2023-08-31 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.6.821_230831_S3000525150.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202301/Network%20Camera%20V5.6.820%20Release%20Note%20--G1.pdf) |
| 5.6.820 | Applied to: [DS-2CD2125FWD-IS(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.6.820_220519_S3000430633.zip) | 2022-05-19 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.6.820_220519_S3000430633.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202301/Network%20Camera%20V5.6.820%20Release%20Note%20--G1.pdf) |

</details>


<details>
<summary><h2>DS-2CD2125G0-IMS - IPC_G1 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.6.821 | Applied to: [DS-2CD2125G0-IMS(4mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.6.821_230831_S3000525150.zip) | 2023-08-31 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.6.821_230831_S3000525150.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202401/releasenote%5CNetwork_Camera-V5.6.821_Release_Note-IPC_G1_230831.pdf) |

</details>


<details>
<summary><h2>DS-2CD2126G2-I - IPC_G0 (3 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2126G2-ISU(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip)(C) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |
| 5.7.19 | Applied to: [DS-2CD2126G2-ISU(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.19_241207_S3000618493.zip)(C) | 2024-12-07 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.19_241207_S3000618493.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.19_241207_Release_Note.pdf) |
| 5.7.0 | Applied to: [DS-2CD2126G2-ISU(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.0_240129_S3000555034.zip)(C) | 2024-10-23 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.0_240129_S3000555034.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.19_241207_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2126G2-IMS - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2126G2-IMS(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |
| 5.7.19 | Applied to: [DS-2CD2126G2-IMS(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.19_241207_S3000618493.zip) | 2024-12-07 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.19_241207_S3000618493.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.19_241207_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2141G1-IDW - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.89 | Applied to: [DS-2CD2141G1-IDW1(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/87acab3e-5d46-45cd-88c4-87b51139b600.zip)(T) | 2021-04-29 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/87acab3e-5d46-45cd-88c4-87b51139b600.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202312/releasenote%5CNetwork_Camera_V5.5.89_Release_Note_--G0.pdf) |
| 5.5.82 | Applied to: [DS-2CD2141G1-IDW1(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.820_260410_S3000715634.zip)(T) | 2019-01-30 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.820_260410_S3000715634.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202312/releasenote%5CNetwork_Camera_V5.5.89_Release_Note_--G0.pdf) |

</details>


<details>
<summary><h2>DS-2CD2143G0-I - IPC_G1 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.6.821 | Applied to: [DS-2CD2143G0-I(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.6.821_230831_S3000525150.zip)(BLACK) | 2023-08-31 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.6.821_230831_S3000525150.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202401/releasenote%5CNetwork_Camera-V5.6.821_Release_Note-IPC_G1_230831.pdf) |

</details>


<details>
<summary><h2>DS-2CD2143G0-IU - IPC_G1 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.6.821 | Applied to: [DS-2CD2143G0-IU(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.6.821_230831_S3000525150.zip) | 2023-08-31 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.6.821_230831_S3000525150.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202401/releasenote%5CNetwork_Camera-V5.6.821_Release_Note-IPC_G1_230831.pdf) |

</details>


<details>
<summary><h2>DS-2CD2143G2-I - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2143G2-I(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip)(BLACK) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |
| 5.7.19 | Applied to: [DS-2CD2143G2-I(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.19_241207_S3000618493.zip)(BLACK) | 2024-12-07 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.19_241207_S3000618493.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.19_241207_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2143G2-IU - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2143G2-IU(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip)(BLACK) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |
| 5.7.19 | Applied to: [DS-2CD2143G2-IU(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.19_241207_S3000618493.zip)(BLACK) | 2024-12-07 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.19_241207_S3000618493.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.19_241207_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2143G2-LI - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2143G2-LI(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |
| 5.7.19 | Applied to: [DS-2CD2143G2-LI(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.19_241207_S3000618493.zip) | 2024-12-07 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.19_241207_S3000618493.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.19_241207_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2143G2-LIPTRZ - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.32 | Applied to: [DS-2CD2143G2-LIPTRZY(2.8/4mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.32_260423_S3000719136.zip) | 2026-03-20 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.32_260423_S3000719136.zip) |  |
| 5.8.30 | Applied to: [DS-2CD2143G2-LIPTRZS2UY(2.8/4mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | 2025-12-10 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13U.pdf) |

</details>


<details>
<summary><h2>DS-2CD2145FWD-I - IPC_G1 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.6.821 | Applied to: [DS-2CD2145FWD-IS(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.6.821_230831_S3000525150.zip)(BLACK) | 2023-08-31 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.6.821_230831_S3000525150.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202401/releasenote%5CNetwork_Camera-V5.6.821_Release_Note-IPC_G1_230831.pdf) |

</details>


<details>
<summary><h2>DS-2CD2146G2-I - IPC_G0 (3 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2146G2-ISU(6mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip)(C) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |
| 5.7.19 | Applied to: [DS-2CD2146G2-ISU(6mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.19_241207_S3000618493.zip)(C) | 2024-12-07 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.19_241207_S3000618493.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.19_241207_Release_Note.pdf) |
| 5.5.800 | Applied to: [DS-2CD2146G2-ISU(6mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.800_211009_S3000390724.zip)(C) | 2021-10-09 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.800_211009_S3000390724.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.19_241207_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2146G2H-I - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2146G2H-I(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip)(eF) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |
| 5.7.19 | Applied to: [DS-2CD2146G2H-I(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.19_241207_S3000618493.zip)(eF) | 2024-12-07 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.19_241207_S3000618493.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.19_241207_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2146G3-IPTRZ - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD2146G3-IPTRZY(2.8/4mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip)(eF) | 2025-12-10 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13U.pdf) |

</details>


<details>
<summary><h2>DS-2CD2147G2 - IPC_G0 (3 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2147G2-SU(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202408/releasenote%5CNetwork_Camera-V5.5.820_Release_Note-G3.pdf) |
| 5.7.19 | Applied to: [DS-2CD2147G2-SU(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.19_241207_S3000618493.zip) | 2024-12-07 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.19_241207_S3000618493.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202408/releasenote%5CNetwork_Camera-V5.5.820_Release_Note-G3.pdf) |
| 5.5.820 | Applied to: [DS-2CD2147G2-SU(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.820_260410_S3000715634.zip) | 2023-11-08 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.820_260410_S3000715634.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202408/releasenote%5CNetwork_Camera-V5.5.820_Release_Note-G3.pdf) |

</details>


<details>
<summary><h2>DS-2CD2147G2-L - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2147G2-LSU(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip)(C) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |
| 5.7.19 | Applied to: [DS-2CD2147G2-LSU(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.19_241207_S3000618493.zip)(C) | 2024-12-07 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.19_241207_S3000618493.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.19_241207_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2147G2-LSU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2147G2-LSU(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip)(C) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2147G2H-LI - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2147G2H-LI(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip)(eF) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |
| 5.7.19 | Applied to: [DS-2CD2147G2H-LI(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.19_241207_S3000618493.zip)(eF) | 2024-12-07 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.19_241207_S3000618493.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.19_241207_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2147G3-LI - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.32 | Applied to: [DS-2CD2147G3-LIS2UY(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.32_260423_S3000719136.zip)(BLACK) | 2026-03-30 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.32_260423_S3000719136.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202604/releasenote%5CNetwork_Camera-V5.8.32_SP1_260330_Release_Note-H13U.pdf) |
| 5.8.21 | Applied to: [DS-2CD2147G3-LIY(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.21_250714_S3000661481.zip) | 2025-11-17 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.21_250714_S3000661481.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.8.21_SP1_251117_Release_Note-H13U.pdf) |

</details>


<details>
<summary><h2>DS-2CD2163G0-I - IPC_G1 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.6.821 | Applied to: [DS-2CD2163G0-I(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.6.821_230831_S3000525150.zip)(BLACK) | 2023-08-31 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.6.821_230831_S3000525150.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202401/releasenote%5CNetwork_Camera-V5.6.821_Release_Note-IPC_G1_230831.pdf) |

</details>


<details>
<summary><h2>DS-2CD2163G0-IU - IPC_G1 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.6.821 | Applied to: [DS-2CD2163G0-IU(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.6.821_230831_S3000525150.zip) | 2023-08-31 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.6.821_230831_S3000525150.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202401/releasenote%5CNetwork_Camera-V5.6.821_Release_Note-IPC_G1_230831.pdf) |

</details>


<details>
<summary><h2>DS-2CD2163G2-I - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2163G2-I(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |
| 5.7.19 | Applied to: [DS-2CD2163G2-I(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.19_241207_S3000618493.zip) | 2024-12-07 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.19_241207_S3000618493.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.19_241207_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2163G2-IU - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2163G2-IU(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |
| 5.7.19 | Applied to: [DS-2CD2163G2-IU(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.19_241207_S3000618493.zip) | 2024-12-07 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.19_241207_S3000618493.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.19_241207_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2163G2-LI - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2163G2-LI(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |
| 5.7.19 | Applied to: [DS-2CD2163G2-LI(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.19_241207_S3000618493.zip) | 2024-12-07 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.19_241207_S3000618493.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.19_241207_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2165G0-I - IPC_G1 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.6.821 | Applied to: [DS-2CD2165G0-I(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.6.821_230831_S3000525150.zip)(BLACK) | 2023-08-31 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.6.821_230831_S3000525150.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202401/releasenote%5CNetwork_Camera-V5.6.821_Release_Note-IPC_G1_230831.pdf) |

</details>


<details>
<summary><h2>DS-2CD2166G2-I - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2166G2-ISU(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip)(C)(BLACK) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |
| 5.7.19 | Applied to: [DS-2CD2166G2-ISU(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.19_241207_S3000618493.zip)(C)(BLACK) | 2024-12-07 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.19_241207_S3000618493.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.19_241207_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2166G2H-I - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2166G2H-I(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip)(eF) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |
| 5.7.19 | Applied to: [DS-2CD2166G2H-I(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.19_241207_S3000618493.zip)(eF) | 2024-12-07 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.19_241207_S3000618493.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.19_241207_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2167G2H-LI - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2167G2H-LI(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip)(eF) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |
| 5.7.19 | Applied to: [DS-2CD2167G2H-LI(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.19_241207_S3000618493.zip)(eF) | 2024-12-07 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.19_241207_S3000618493.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.19_241207_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2167G3-LI - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.32 | Applied to: [DS-2CD2167G3-LIS2UY(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.32_260423_S3000719136.zip) | 2026-03-30 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.32_260423_S3000719136.zip) |  |
| 5.8.30 | Applied to: [DS-2CD2167G3-LIS2UY(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | 2025-12-10 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD2183G0-I - IPC_G1 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.6.821 | Applied to: [DS-2CD2183G0-I(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.6.821_230831_S3000525150.zip)(BLACK) | 2023-08-31 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.6.821_230831_S3000525150.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202401/releasenote%5CNetwork_Camera-V5.6.821_Release_Note-IPC_G1_230831.pdf) |
| 5.6.820 | Applied to: [DS-2CD2183G0-I(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.6.820_220519_S3000430633.zip)(BLACK) | 2022-05-19 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.6.820_220519_S3000430633.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202401/releasenote%5CNetwork_Camera-V5.6.821_Release_Note-IPC_G1_230831.pdf) |

</details>


<details>
<summary><h2>DS-2CD2183G0-IU - IPC_G1 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.6.821 | Applied to: [DS-2CD2183G0-IU(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.6.821_230831_S3000525150.zip) | 2023-08-31 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.6.821_230831_S3000525150.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202401/releasenote%5CNetwork_Camera-V5.6.821_Release_Note-IPC_G1_230831.pdf) |

</details>


<details>
<summary><h2>DS-2CD2183G2-I - IPC_G0 (4 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.6 | Applied to: [DS-2CD2183G2-I(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.6_260128_S3000701683.zip)(D) | 2026-01-28 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.6_260128_S3000701683.zip) |  |
| 5.7.23 | Applied to: [DS-2CD2183G2-IS(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip)(BLACK) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |
| 5.7.5 | Applied to: [DS-2CD2183G2-IS(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.55_241108_S3000612871.zip)(BLACK) | 2025-07-18 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.55_241108_S3000612871.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.19_241207_Release_Note.pdf) |
| 5.7.19 | Applied to: [DS-2CD2183G2-IS(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.19_241207_S3000618493.zip)(BLACK) | 2024-12-07 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.19_241207_S3000618493.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.19_241207_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2183G2-IU - IPC_G0 (4 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.6 | Applied to: [DS-2CD2183G2-IU(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.6_260128_S3000701683.zip)(D) | 2026-01-28 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.6_260128_S3000701683.zip) |  |
| 5.7.23 | Applied to: [DS-2CD2183G2-IU(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip)(D) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |
| 5.7.5 | Applied to: [DS-2CD2183G2-IU(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.55_241108_S3000612871.zip)(D) | 2025-07-18 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.55_241108_S3000612871.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202508/releasenote%5CNetwork_Camera-V5.7.5_250718_Release_Note-H8.pdf) |
| 5.7.19 | Applied to: [DS-2CD2183G2-IU(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.19_241207_S3000618493.zip)(D) | 2024-12-07 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.19_241207_S3000618493.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202508/releasenote%5CNetwork_Camera-V5.7.5_250718_Release_Note-H8.pdf) |

</details>


<details>
<summary><h2>DS-2CD2183G2-LI - IPC_G0 (4 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.6 | Applied to: [DS-2CD2183G2-LI(4mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.6_260128_S3000701683.zip)(T) | 2026-01-28 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.6_260128_S3000701683.zip) |  |
| 5.7.23 | Applied to: [DS-2CD2183G2-LI(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |
| 5.7.19 | Applied to: [DS-2CD2183G2-LI(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.19_241207_S3000618493.zip) | 2024-12-07 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.19_241207_S3000618493.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.19_241207_Release_Note.pdf) |
| 5.7.5 | Applied to: [DS-2CD2183G2-LI(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.55_241108_S3000612871.zip) | 2024-11-03 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.55_241108_S3000612871.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.19_241207_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2185FWD-I - IPC_G1 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.6.821 | Applied to: [DS-2CD2185FWD-I(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.6.821_230831_S3000525150.zip)(BLACK) | 2023-08-31 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.6.821_230831_S3000525150.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202401/releasenote%5CNetwork_Camera-V5.6.821_Release_Note-IPC_G1_230831.pdf) |

</details>


<details>
<summary><h2>DS-2CD2185G0-IMS - IPC_G1 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.6.821 | Applied to: [DS-2CD2185G0-IMS(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.6.821_230831_S3000525150.zip) | 2023-08-31 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.6.821_230831_S3000525150.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202401/releasenote%5CNetwork_Camera-V5.6.821_Release_Note-IPC_G1_230831.pdf) |

</details>


<details>
<summary><h2>DS-2CD2186G2-I - IPC_G0 (4 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2186G2-I(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202408/releasenote%5CNetwork_Camera-V5.5.820_Release_Note-G3.pdf) |
| 5.7.19 | Applied to: [DS-2CD2186G2-I(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.19_241207_S3000618493.zip) | 2024-12-07 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.19_241207_S3000618493.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202408/releasenote%5CNetwork_Camera-V5.5.820_Release_Note-G3.pdf) |
| 5.5.820 | Applied to: [DS-2CD2186G2-I(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.820_260410_S3000715634.zip) | 2023-11-08 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.820_260410_S3000715634.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202408/releasenote%5CNetwork_Camera-V5.5.820_Release_Note-G3.pdf) |
| 5.5.800 | Applied to: [DS-2CD2186G2-I(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.800_211009_S3000390724.zip) | 2021-10-09 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.800_211009_S3000390724.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202408/releasenote%5CNetwork_Camera-V5.5.820_Release_Note-G3.pdf) |

</details>


<details>
<summary><h2>DS-2CD2186G2H-I - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2186G2H-I(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip)(eF) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |
| 5.7.19 | Applied to: [DS-2CD2186G2H-I(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.19_241207_S3000618493.zip)(eF) | 2024-12-07 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.19_241207_S3000618493.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.19_241207_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2187G2-L - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2187G2-L(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip)(C) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |
| 5.7.19 | Applied to: [DS-2CD2187G2-L(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.19_241207_S3000618493.zip)(C) | 2024-12-07 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.19_241207_S3000618493.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.19_241207_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2187G2-LSU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2187G2-LSU(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip)(C)(BLACK) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2187G2H-LI - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2187G2H-LI(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip)(eF) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |
| 5.7.19 | Applied to: [DS-2CD2187G2H-LI(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.19_241207_S3000618493.zip)(eF) | 2024-12-07 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.19_241207_S3000618493.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.19_241207_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2187G3-LI - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.32 | Applied to: [DS-2CD2187G3-LIS2UY(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.32_260423_S3000719136.zip)(BLACK) | 2026-03-30 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.32_260423_S3000719136.zip) |  |
| 5.8.30 | Applied to: [DS-2CD2187G3-LIY(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | 2025-12-10 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD23123G2-LI - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.2 | Applied to: [DS-2CD23123G2-LI2UY(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.23_260403_S3000712869.zip) | 2025-11-03 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.23_260403_S3000712869.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202511/releasenote%5CNetwork_Camera-V5.8.2_251103_Release_Note-IPCE_G9.pdf) |

</details>


<details>
<summary><h2>DS-2CD23123G2-LI2UY - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.3 | Applied to: [DS-2CD23123G2-LIS2UY/SRB(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.3_260416_S3000716238.zip) | 2026-03-20 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.3_260416_S3000716238.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202604/releasenote%5CNetwork_Camera-V5.8.3_SP1_260320_Release_Note-IPCE_G9.pdf) |
| 5.8.2 | Applied to: [DS-2CD23123G2-LIS2UY/SL(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.23_260403_S3000712869.zip) | 2025-11-03 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.23_260403_S3000712869.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202511/releasenote%5CNetwork_Camera-V5.8.2_251103_Release_Note-IPCE_G9.pdf) |

</details>


<details>
<summary><h2>DS-2CD23126G3-I - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.2 | Applied to: [DS-2CD23126G3-I2UY(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.23_260403_S3000712869.zip)(eF) | 2025-11-03 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.23_260403_S3000712869.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202511/releasenote%5CNetwork_Camera-V5.8.2_251103_Release_Note-IPCE_G9.pdf) |

</details>


<details>
<summary><h2>DS-2CD23126G3-IS2UY - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.3 | Applied to: [DS-2CD23126G3-IS2UY/SRB(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.3_260416_S3000716238.zip)(eF)/O-STD | 2026-03-20 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.3_260416_S3000716238.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202604/releasenote%5CNetwork_Camera-V5.8.3_SP1_260320_Release_Note-IPCE_G9.pdf) |
| 5.8.2 | Applied to: [DS-2CD23126G3-IS2UY/SRB(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.23_260403_S3000712869.zip)(eF)/O-STD | 2025-11-03 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.23_260403_S3000712869.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202511/releasenote%5CNetwork_Camera-V5.8.2_251103_Release_Note-IPCE_G9.pdf) |

</details>


<details>
<summary><h2>DS-2CD23127G3P-LIS2UY - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.110 | Applied to: [DS-2CD23127G3P-LIS2UY/SRB(180°)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.110_260421_S3000717992.zip) | 2026-04-21 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.110_260421_S3000717992.zip) |  |

</details>


<details>
<summary><h2>DS-2CD23127G3P-LIS2UY-S-L--RB- - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.110 | [DS-2CD23127G3P-LIS2UY-S-L--RB-](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.110_260421_S3000717992.zip) | 2026-04-21 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.110_260421_S3000717992.zip) |  |

</details>


<details>
<summary><h2>DS-2CD23166G3-I - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.2 | Applied to: [DS-2CD23166G3-IY(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.23_260403_S3000712869.zip)(eF) | 2025-11-03 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.23_260403_S3000712869.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202511/releasenote%5CNetwork_Camera-V5.8.2_251103_Release_Note-IPCE_G9.pdf) |

</details>


<details>
<summary><h2>DS-2CD23166G3-IS2UY - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.2 | Applied to: [DS-2CD23166G3-IS2UY/SRB(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.23_260403_S3000712869.zip)(eF)/O-STD | 2025-11-03 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.23_260403_S3000712869.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202511/releasenote%5CNetwork_Camera-V5.8.2_251103_Release_Note-IPCE_G9.pdf) |

</details>


<details>
<summary><h2>DS-2CD23167G3P-LIS2UY - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.110 | Applied to: [DS-2CD23167G3P-LIS2UY/SRB(180°)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.110_260421_S3000717992.zip) | 2026-04-21 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.110_260421_S3000717992.zip) |  |

</details>


<details>
<summary><h2>DS-2CD23167G3P-LIS2UY-S-L--RB- - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.110 | [DS-2CD23167G3P-LIS2UY-S-L--RB-](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.110_260421_S3000717992.zip) | 2026-04-21 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.110_260421_S3000717992.zip) |  |

</details>


<details>
<summary><h2>DS-2CD2323G0-I - IPC_G1 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.6.821 | Applied to: [DS-2CD2323G0-I(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.6.821_230831_S3000525150.zip)(BLACK) | 2023-08-31 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.6.821_230831_S3000525150.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202401/releasenote%5CNetwork_Camera-V5.6.821_Release_Note-IPC_G1_230831.pdf) |

</details>


<details>
<summary><h2>DS-2CD2323G2-I - IPC_G0 (4 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2323G2-I(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip)(D) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202507/releasenote%5CNetwork_Camera-V5.7.0_SP6_Release_Note-G6_I.pdf) |
| 5.7.19 | Applied to: [DS-2CD2323G2-I(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.19_241207_S3000618493.zip)(D) | 2024-12-07 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.19_241207_S3000618493.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202507/releasenote%5CNetwork_Camera-V5.7.0_SP6_Release_Note-G6_I.pdf) |
| 5.7.0 | Applied to: [DS-2CD2323G2-I(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.0_240129_S3000555034.zip)(D) | 2024-10-23 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.0_240129_S3000555034.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202507/releasenote%5CNetwork_Camera-V5.7.0_SP6_Release_Note-G6_I.pdf) |
| 5.7.18 | Applied to: [DS-2CD2323G2-I(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.18_240826_S3000597013.zip)(D) | 2024-08-26 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.18_240826_S3000597013.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202507/releasenote%5CNetwork_Camera-V5.7.0_SP6_Release_Note-G6_I.pdf) |

</details>


<details>
<summary><h2>DS-2CD2323G2-IU - IPC_G0 (3 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2323G2-I(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip)(D) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202507/releasenote%5CNetwork_Camera-V5.7.0_SP6_Release_Note-G6_I.pdf) |
| 5.7.0 | Applied to: [DS-2CD2323G2-I(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.0_240129_S3000555034.zip)(D) | 2024-10-23 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.0_240129_S3000555034.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202507/releasenote%5CNetwork_Camera-V5.7.0_SP6_Release_Note-G6_I.pdf) |
| 5.7.18 | Applied to: [DS-2CD2323G2-I(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.18_240826_S3000597013.zip)(D) | 2024-08-26 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.18_240826_S3000597013.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202507/releasenote%5CNetwork_Camera-V5.7.0_SP6_Release_Note-G6_I.pdf) |

</details>


<details>
<summary><h2>DS-2CD2323G2-LI - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2323G2-LI(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |
| 5.7.19 | Applied to: [DS-2CD2323G2-LI(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.19_241207_S3000618493.zip) | 2024-12-07 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.19_241207_S3000618493.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.19_241207_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2323G2-LI2U - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2323G2-LI2U/SRB(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |
| 5.7.19 | Applied to: [DS-2CD2323G2-LI2U/SRB(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.19_241207_S3000618493.zip) | 2024-12-07 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.19_241207_S3000618493.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.19_241207_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2325FHWD-I - IPC_G1 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.6.821 | Applied to: [DS-2CD2325FHWD-I(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.6.821_230831_S3000525150.zip) | 2023-08-31 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.6.821_230831_S3000525150.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202401/releasenote%5CNetwork_Camera-V5.6.821_Release_Note-IPC_G1_230831.pdf) |

</details>


<details>
<summary><h2>DS-2CD2325FWD-I - IPC_G1 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.6.821 | Applied to: [DS-2CD2325FWD-I(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.6.821_230831_S3000525150.zip)(BLACK) | 2023-08-31 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.6.821_230831_S3000525150.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202401/releasenote%5CNetwork_Camera-V5.6.821_Release_Note-IPC_G1_230831.pdf) |

</details>


<details>
<summary><h2>DS-2CD2326G1-I - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.6.0 | Applied to: [DS-2CD2326G1-I/SL(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/18db80e0-2712-4496-8bd3-646f5014a59b.zip) | 2019-05-07 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/18db80e0-2712-4496-8bd3-646f5014a59b.zip) |  |

</details>


<details>
<summary><h2>DS-2CD2326G2-I - IPC_G0 (5 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2326G2-IU(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/330c4c2c-5730-4877-a942-0be87cea67ca.pdf) |
| 5.7.19 | Applied to: [DS-2CD2326G2-IU(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.19_241207_S3000618493.zip) | 2024-12-07 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.19_241207_S3000618493.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/330c4c2c-5730-4877-a942-0be87cea67ca.pdf) |
| 5.7.0 | Applied to: [DS-2CD2326G2-IU(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.0_240129_S3000555034.zip) | 2024-10-23 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.0_240129_S3000555034.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/330c4c2c-5730-4877-a942-0be87cea67ca.pdf) |
| 5.5.820 | Applied to: [DS-2CD2326G2-IU(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.820_260410_S3000715634.zip) | 2022-05-20 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.820_260410_S3000715634.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/330c4c2c-5730-4877-a942-0be87cea67ca.pdf) |
| 5.5.800 | Applied to: [DS-2CD2326G2-IU(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.800_211009_S3000390724.zip) | 2021-10-09 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.800_211009_S3000390724.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/330c4c2c-5730-4877-a942-0be87cea67ca.pdf) |

</details>


<details>
<summary><h2>DS-2CD2326G2-ISU - IPC_G0 (4 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2326G2-ISU/SL(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip)(D) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202507/releasenote%5CNetwork_Camera-V5.7.0_SP6_Release_Note-G6_I.pdf) |
| 5.7.19 | Applied to: [DS-2CD2326G2-ISU/SL(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.19_241207_S3000618493.zip)(D) | 2024-12-07 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.19_241207_S3000618493.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202507/releasenote%5CNetwork_Camera-V5.7.0_SP6_Release_Note-G6_I.pdf) |
| 5.7.0 | Applied to: [DS-2CD2326G2-ISU/SL(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.0_240129_S3000555034.zip)(D) | 2024-10-23 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.0_240129_S3000555034.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202507/releasenote%5CNetwork_Camera-V5.7.0_SP6_Release_Note-G6_I.pdf) |
| 5.5.820 | Applied to: [DS-2CD2326G2-ISU/SL(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.820_260410_S3000715634.zip)(D) | 2023-11-08 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.820_260410_S3000715634.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202507/releasenote%5CNetwork_Camera-V5.7.0_SP6_Release_Note-G6_I.pdf) |

</details>


<details>
<summary><h2>DS-2CD2327G2-L - IPC_G0 (3 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2327G2-LU(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/330c4c2c-5730-4877-a942-0be87cea67ca.pdf) |
| 5.7.19 | Applied to: [DS-2CD2327G2-LU(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.19_241207_S3000618493.zip) | 2024-12-07 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.19_241207_S3000618493.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/330c4c2c-5730-4877-a942-0be87cea67ca.pdf) |
| 5.5.800 | Applied to: [DS-2CD2327G2-LU(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.800_211009_S3000390724.zip) | 2021-10-09 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.800_211009_S3000390724.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/330c4c2c-5730-4877-a942-0be87cea67ca.pdf) |

</details>


<details>
<summary><h2>DS-2CD2343G0-I - IPC_G1 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.6.821 | Applied to: [DS-2CD2343G0-I(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.6.821_230831_S3000525150.zip)(BLACK) | 2023-08-31 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.6.821_230831_S3000525150.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202401/releasenote%5CNetwork_Camera-V5.6.821_Release_Note-IPC_G1_230831.pdf) |

</details>


<details>
<summary><h2>DS-2CD2343G2-I - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2343G2-IU(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip)(BLACK) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2343G2-IU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2343G2-IU(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip)(BLACK) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2343G2-LI - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2343G2-LI(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |
| 5.7.19 | Applied to: [DS-2CD2343G2-LI(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.19_241207_S3000618493.zip) | 2024-12-07 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.19_241207_S3000618493.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.19_241207_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2343G2-LI2U - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2343G2-LI2U/SL(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |
| 5.7.19 | Applied to: [DS-2CD2343G2-LI2U/SL(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.19_241207_S3000618493.zip) | 2024-12-07 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.19_241207_S3000618493.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.19_241207_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2343G2-LIZ - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD2343G2-LIZY(2.8/4mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | 2025-12-10 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13U.pdf) |
| 5.8.21 | Applied to: [DS-2CD2343G2-LIZ2UY(2.8/4mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.21_250714_S3000661481.zip) | 2025-11-17 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.21_250714_S3000661481.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.8.21_SP1_251117_Release_Note-H13U.pdf) |

</details>


<details>
<summary><h2>DS-2CD2343G2-LIZ2UY - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD2343G2-LIZ2UY/SRB(2.8/4mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | 2025-12-10 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13U.pdf) |
| 5.8.21 | Applied to: [DS-2CD2343G2-LIZ2UY/SRB(2.8/4mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.21_250714_S3000661481.zip) | 2025-11-17 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.21_250714_S3000661481.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.8.21_SP1_251117_Release_Note-H13U.pdf) |

</details>


<details>
<summary><h2>DS-2CD2343G2D-LIZ2UY - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.11 | Applied to: [DS-2CD2343G2D-LIZ2UY/SL(2.8/4mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.110_260421_S3000717992.zip) | 2025-12-16 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.110_260421_S3000717992.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.8.11_251216_Release_Note-IPCE_D_H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD2343G2P-LISU - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.12 | Applied to: [DS-2CD2343G2P-LISU/SL(180°)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.12_260416_S3000716519.zip) | 2026-04-16 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.12_260416_S3000716519.zip) |  |
| 5.8.11 | Applied to: [DS-2CD2343G2P-LISU/SL(180°)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.110_260421_S3000717992.zip) | 2025-10-29 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.110_260421_S3000717992.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.8.11_SP1_251029_Release_Note-IPCE_P_E11.pdf) |

</details>


<details>
<summary><h2>DS-2CD2343G2P-LISU-S-L--RB- - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.12 | [DS-2CD2343G2P-LISU-S-L--RB-](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.12_260416_S3000716513.zip) | 2026-04-16 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.12_260416_S3000716513.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202605/releasenote%5CNetwork_Camera-V5.8.12_260416_Release_IPCE_P_E11.pdf) |

</details>


<details>
<summary><h2>DS-2CD2345FWD-I - IPC_G1 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.6.821 | Applied to: [DS-2CD2345FWD-I(4mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.6.821_230831_S3000525150.zip)(BLACK) | 2023-08-31 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.6.821_230831_S3000525150.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202401/releasenote%5CNetwork_Camera-V5.6.821_Release_Note-IPC_G1_230831.pdf) |

</details>


<details>
<summary><h2>DS-2CD2345G0P-I - IPC_G1 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.6.821 | Applied to: [DS-2CD2345G0P-I(1.68mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.6.821_230831_S3000525150.zip) | 2023-08-31 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.6.821_230831_S3000525150.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202401/releasenote%5CNetwork_Camera-V5.6.821_Release_Note-IPC_G1_230831.pdf) |

</details>


<details>
<summary><h2>DS-2CD2346G1-I - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.6.0 | Applied to: [DS-2CD2346G1-I/SL(4mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/18db80e0-2712-4496-8bd3-646f5014a59b.zip) | 2019-05-07 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/18db80e0-2712-4496-8bd3-646f5014a59b.zip) |  |

</details>


<details>
<summary><h2>DS-2CD2346G2-I - IPC_G0 (3 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2346G2-IU(6mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip)(C) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |
| 5.7.19 | Applied to: [DS-2CD2346G2-IU(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.19_241207_S3000618493.zip)(C)(BLACK) | 2024-12-07 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.19_241207_S3000618493.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.19_241207_Release_Note.pdf) |
| 5.5.800 | Applied to: [DS-2CD2346G2-IU(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.800_211009_S3000390724.zip)(C)(BLACK) | 2021-10-09 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.800_211009_S3000390724.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.19_241207_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2346G2-ISU - IPC_G0 (3 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2346G2-ISU/SL(6mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip)(C) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |
| 5.5.820 | Applied to: [DS-2CD2346G2-ISU/SL(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.820_260410_S3000715634.zip) | 2023-11-08 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.820_260410_S3000715634.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/330c4c2c-5730-4877-a942-0be87cea67ca.pdf) |
| 5.5.800 | Applied to: [DS-2CD2346G2-ISU/SL(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.800_211009_S3000390724.zip) | 2021-10-09 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.800_211009_S3000390724.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/330c4c2c-5730-4877-a942-0be87cea67ca.pdf) |

</details>


<details>
<summary><h2>DS-2CD2346G2H-I - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2346G2H-IU(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip)(eF) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |
| 5.7.19 | Applied to: [DS-2CD2346G2H-IU(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.19_241207_S3000618493.zip)(eF) | 2024-12-07 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.19_241207_S3000618493.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.19_241207_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2346G2H-IS2U - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2346G2H-IS2U/SRB(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip)/eFO-STDBLK | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |
| 5.7.19 | Applied to: [DS-2CD2346G2H-IS2U/SRB(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.19_241207_S3000618493.zip)/eFO-STDBLK | 2024-12-07 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.19_241207_S3000618493.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.19_241207_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2346G3-IZ - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD2346G3-IZY(2.8/4mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | 2025-12-10 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13U.pdf) |
| 5.8.21 | Applied to: [DS-2CD2346G3-IZY(2.8/4mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.21_250714_S3000661481.zip) | 2025-11-17 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.21_250714_S3000661481.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.8.21_SP1_251117_Release_Note-H13U.pdf) |

</details>


<details>
<summary><h2>DS-2CD2346G3-IZS2UY - IPC_G0 (3 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.32 | Applied to: [DS-2CD2346G3-IZS2UY/SRB(2.8/4mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.32_260423_S3000719136.zip) | 2026-03-30 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.32_260423_S3000719136.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202604/releasenote%5CNetwork_Camera-V5.8.32_SP1_260330_Release_Note-H13U.pdf) |
| 5.8.30 | Applied to: [DS-2CD2346G3-IZS2UY/SRB(2.8/4mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | 2025-12-10 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13U.pdf) |
| 5.8.21 | Applied to: [DS-2CD2346G3-IZS2UY/SRB(2.8/4mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.21_250714_S3000661481.zip) | 2025-11-17 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.21_250714_S3000661481.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.8.21_SP1_251117_Release_Note-H13U.pdf) |

</details>


<details>
<summary><h2>DS-2CD2346G3D-IZ2UY - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.11 | Applied to: [DS-2CD2346G3D-IZ2UY/SRB(2.8/4)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.110_260421_S3000717992.zip)O-STDBLACK | 2025-12-16 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.110_260421_S3000717992.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.8.11_251216_Release_Note-IPCE_D_H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD2347G2-L - IPC_G0 (3 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2347G2-L(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202408/releasenote%5CNetwork_Camera-V5.5.820_Release_Note-G3.pdf) |
| 5.5.820 | Applied to: [DS-2CD2347G2-L(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.820_260410_S3000715634.zip) | 2023-11-08 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.820_260410_S3000715634.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202408/releasenote%5CNetwork_Camera-V5.5.820_Release_Note-G3.pdf) |
| 5.5.800 | Applied to: [DS-2CD2347G2-L(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.800_211009_S3000390724.zip) | 2021-10-09 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.800_211009_S3000390724.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202408/releasenote%5CNetwork_Camera-V5.5.820_Release_Note-G3.pdf) |

</details>


<details>
<summary><h2>DS-2CD2347G2-LSU - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2347G2-LSU/SL(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip)(C) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |
| 5.7.19 | Applied to: [DS-2CD2347G2-LSU/SL/2](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.19_241207_S3000618493.zip).8mm/C/O-STD/BLACK | 2024-12-07 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.19_241207_S3000618493.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.19_241207_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2347G2-LU - IPC_G0 (3 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2347G2-L(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202408/releasenote%5CNetwork_Camera-V5.5.820_Release_Note-G3.pdf) |
| 5.5.820 | Applied to: [DS-2CD2347G2-L(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.820_260410_S3000715634.zip) | 2023-11-08 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.820_260410_S3000715634.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202408/releasenote%5CNetwork_Camera-V5.5.820_Release_Note-G3.pdf) |
| 5.5.800 | Applied to: [DS-2CD2347G2-L(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.800_211009_S3000390724.zip) | 2021-10-09 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.800_211009_S3000390724.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202408/releasenote%5CNetwork_Camera-V5.5.820_Release_Note-G3.pdf) |

</details>


<details>
<summary><h2>DS-2CD2347G2H-LI - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2347G2H-LI(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip)(eF) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |
| 5.7.19 | Applied to: [DS-2CD2347G2H-LIU(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.19_241207_S3000618493.zip)(eF)/O-STD/BLACK | 2024-12-07 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.19_241207_S3000618493.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.19_241207_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2347G2H-LISU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2347G2H-LISU/SL(2.8)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip)/eF/O-STD/BLK | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2347G3-LI - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.32 | Applied to: [DS-2CD2347G3-LI2UY(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.32_260423_S3000719136.zip) | 2026-03-30 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.32_260423_S3000719136.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202604/releasenote%5CNetwork_Camera-V5.8.32_SP1_260330_Release_Note-H13U.pdf) |

</details>


<details>
<summary><h2>DS-2CD2347G3-LIS2UY - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.32 | Applied to: [DS-2CD2347G3-LIS2UY/SRB(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.32_260423_S3000719136.zip) | 2026-03-30 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.32_260423_S3000719136.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202604/releasenote%5CNetwork_Camera-V5.8.32_SP1_260330_Release_Note-H13U.pdf) |
| 5.8.30 | Applied to: [DS-2CD2347G3-LIS2UY/SRB(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | 2025-12-10 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13U.pdf) |

</details>


<details>
<summary><h2>DS-2CD2347G3P-LIS2UY - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.100 | Applied to: [DS-2CD2347G3P-LIS2UY/SRB(180°)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.100_260416_S3000716492.zip) | 2026-03-25 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.100_260416_S3000716492.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202604/releasenote%5CNetwork_Camera-V5.8.100_260325_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2363G0-I - IPC_G1 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.6.821 | Applied to: [DS-2CD2363G0-I(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.6.821_230831_S3000525150.zip) | 2023-08-31 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.6.821_230831_S3000525150.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202401/releasenote%5CNetwork_Camera-V5.6.821_Release_Note-IPC_G1_230831.pdf) |

</details>


<details>
<summary><h2>DS-2CD2363G2-I - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2363G2-IU(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2363G2-LI - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2363G2-LI(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2363G2-LI2U - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2363G2-LI2U/SRB(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2363G2P-LISU - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.12 | Applied to: [DS-2CD2363G2P-LISU/SL(180°)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.12_260416_S3000716519.zip) | 2026-04-16 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.12_260416_S3000716519.zip) |  |
| 5.8.11 | Applied to: [DS-2CD2363G2P-LISU/SL(180°)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.110_260421_S3000717992.zip) | 2025-10-29 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.110_260421_S3000717992.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.8.11_SP1_251029_Release_Note-IPCE_P_E11.pdf) |

</details>


<details>
<summary><h2>DS-2CD2363G2P-LISU-S-L--RB- - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.12 | [DS-2CD2363G2P-LISU-S-L--RB-](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.12_260416_S3000716513.zip) | 2026-04-16 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.12_260416_S3000716513.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202605/releasenote%5CNetwork_Camera-V5.8.12_260416_Release_IPCE_P_E11.pdf) |

</details>


<details>
<summary><h2>DS-2CD2365G1-I - IPC_G1 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.6.821 | Applied to: [DS-2CD2365G1-I(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.6.821_230831_S3000525150.zip)(BLACK) | 2023-08-31 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.6.821_230831_S3000525150.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202401/releasenote%5CNetwork_Camera-V5.6.821_Release_Note-IPC_G1_230831.pdf) |

</details>


<details>
<summary><h2>DS-2CD2366G2-I - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2366G2-I(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip)(C) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2366G2-ISU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2366G2-ISU/SL(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip)/C/O-STD/BLACK | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2366G2H-I - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2366G2H-I(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip)(eF) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2366G2H-IS2U - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2366G2H-IS2U/SL(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip)(eF) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2366G2P-ISU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.20 | Applied to: [DS-2CD2366G2P-ISU/SL(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.20_230630_S3000509422.zip)(C) | 2025-11-25 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.20_230630_S3000509422.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.20_251125_Release_Note-IPCE_P_G5.pdf) |

</details>


<details>
<summary><h2>DS-2CD2367G2-L - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2367G2-LU(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip)(C) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2367G2H-LISU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2367G2H-LISU/SL(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip)(eF) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2367G2H-LIU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2367G2H-LIU(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip)(eF) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2367G2P-LSU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.20 | Applied to: [DS-2CD2367G2P-LSU/SL(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.20_230630_S3000509422.zip)(C) | 2025-11-25 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.20_230630_S3000509422.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.20_251125_Release_Note-IPCE_P_G5.pdf) |

</details>


<details>
<summary><h2>DS-2CD2367G3-LI - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD2367G3-LI2UY(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | 2025-12-10 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD2367G3-LIS2UY - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.32 | Applied to: [DS-2CD2367G3-LIS2UY/SL(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.32_260423_S3000719136.zip) | 2026-03-20 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.32_260423_S3000719136.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |
| 5.8.30 | Applied to: [DS-2CD2367G3-LIS2UY/SL(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | 2025-12-10 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD2367G3P-LIS2UY - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.100 | Applied to: [DS-2CD2367G3P-LIS2UY/SRB(180°)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.100_260416_S3000716492.zip) | 2026-03-25 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.100_260416_S3000716492.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202604/releasenote%5CNetwork_Camera-V5.8.100_260325_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2383G0-I - IPC_G1 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.6.821 | Applied to: [DS-2CD2383G0-I(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.6.821_230831_S3000525150.zip)(BLACK) | 2023-08-31 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.6.821_230831_S3000525150.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202401/releasenote%5CNetwork_Camera-V5.6.821_Release_Note-IPC_G1_230831.pdf) |

</details>


<details>
<summary><h2>DS-2CD2383G2-I - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.6 | Applied to: [DS-2CD2383G2-IU(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.6_260128_S3000701683.zip)(D)(BLACK) | 2026-01-28 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.6_260128_S3000701683.zip) |  |
| 5.7.23 | Applied to: [DS-2CD2383G2-I(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2383G2-IU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2383G2-I(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2383G2-LI - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.6 | Applied to: [DS-2CD2383G2-LI2U(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.6_260128_S3000701683.zip)(T) | 2026-01-28 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.6_260128_S3000701683.zip) |  |
| 5.7.23 | Applied to: [DS-2CD2383G2-LI(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2383G2-LI2U - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2383G2-LI2U/SL(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2383G2P-LISU - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.12 | Applied to: [DS-2CD2383G2P-LISU/SL(180°)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.12_260416_S3000716519.zip) | 2026-04-16 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.12_260416_S3000716519.zip) |  |
| 5.8.11 | Applied to: [DS-2CD2383G2P-LISU/SL(180°)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.110_260421_S3000717992.zip) | 2025-10-29 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.110_260421_S3000717992.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.8.11_SP1_251029_Release_Note-IPCE_P_E11.pdf) |

</details>


<details>
<summary><h2>DS-2CD2383G2P-LISU-S-L--RB- - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.12 | [DS-2CD2383G2P-LISU-S-L--RB-](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.12_260416_S3000716513.zip) | 2026-04-16 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.12_260416_S3000716513.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202605/releasenote%5CNetwork_Camera-V5.8.12_260416_Release_IPCE_P_E11.pdf) |

</details>


<details>
<summary><h2>DS-2CD2385G1-I - IPC_G1 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.6.821 | Applied to: [DS-2CD2385G1-I(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.6.821_230831_S3000525150.zip) | 2023-08-31 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.6.821_230831_S3000525150.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202401/releasenote%5CNetwork_Camera-V5.6.821_Release_Note-IPC_G1_230831.pdf) |

</details>


<details>
<summary><h2>DS-2CD2386G2-I - IPC_G0 (3 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2386G2-I(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/330c4c2c-5730-4877-a942-0be87cea67ca.pdf) |
| 5.5.820 | Applied to: [DS-2CD2386G2-I(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.820_260410_S3000715634.zip) | 2023-11-08 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.820_260410_S3000715634.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/330c4c2c-5730-4877-a942-0be87cea67ca.pdf) |
| 5.5.800 | Applied to: [DS-2CD2386G2-I(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.800_211009_S3000390724.zip) | 2021-10-09 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.800_211009_S3000390724.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/330c4c2c-5730-4877-a942-0be87cea67ca.pdf) |

</details>


<details>
<summary><h2>DS-2CD2386G2-ISU - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2386G2-ISU/SL(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202408/releasenote%5CNetwork_Camera-V5.5.820_Release_Note-G3.pdf) |
| 5.5.820 | Applied to: [DS-2CD2386G2-ISU/SL(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.820_260410_S3000715634.zip) | 2023-11-08 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.820_260410_S3000715634.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202408/releasenote%5CNetwork_Camera-V5.5.820_Release_Note-G3.pdf) |

</details>


<details>
<summary><h2>DS-2CD2386G2H-I - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2386G2H-IU(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip)(eF) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2386G2H-IS2U - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2386G2H-IS2U/SRB(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip)/eFO-STDBLK | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2387G2-L - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2387G2-LU(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip)(C) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2387G2-LSU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2387G2-LSU/SL(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip)(C) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2387G2-LU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2387G2-LU(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip)(C) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2387G2H-LI - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2387G2H-LI(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip)(eF) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2387G2H-LISU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2387G2H-LISU/SL(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip)(eF) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2387G2P-LSU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.20 | Applied to: [DS-2CD2387G2P-LSU/SL(4mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.20_230630_S3000509422.zip)(C)/O-STD/BLACK | 2025-11-25 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.20_230630_S3000509422.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.20_251125_Release_Note-IPCE_P_G5.pdf) |

</details>


<details>
<summary><h2>DS-2CD2387G3-LI - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.32 | Applied to: [DS-2CD2387G3-LI2UY(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.32_260423_S3000719136.zip) | 2026-03-30 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.32_260423_S3000719136.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202604/releasenote%5CNetwork_Camera-V5.8.32_SP1_260330_Release_Note-H13.pdf) |
| 5.8.30 | Applied to: [DS-2CD2387G3-LI2UY(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | 2025-12-10 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD2387G3-LIS2UY - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.32 | Applied to: [DS-2CD2387G3-LIS2UY/SL(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.32_260423_S3000719136.zip)O-STD/BLACK | 2026-03-30 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.32_260423_S3000719136.zip) |  |
| 5.8.30 | Applied to: [DS-2CD2387G3-LIS2UY/SL(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | 2025-12-10 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD2387G3P-LIS2UY - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.110 | Applied to: [DS-2CD2387G3P-LIS2UY/SRB(180°)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.110_260421_S3000717992.zip) | 2026-04-21 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.110_260421_S3000717992.zip) |  |

</details>


<details>
<summary><h2>DS-2CD2387G3P-LIS2UY-S-L--RB- - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.110 | [DS-2CD2387G3P-LIS2UY-S-L--RB-](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.110_260421_S3000717992.zip) | 2026-04-21 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.110_260421_S3000717992.zip) |  |

</details>


<details>
<summary><h2>DS-2CD2421G0-I - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2421G0-I(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | 2024-12-11 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202404/1712790070190/releasenote%5CIPC_E6_5.5.821_Release_Note.pdf) |
| 5.5.821 | Applied to: [DS-2CD2421G0-I(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.821_231108_S3000539548.zip) | 2023-11-08 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.821_231108_S3000539548.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202404/1712790070190/releasenote%5CIPC_E6_5.5.821_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2423G0-I - IPC_G1 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.6.821 | Applied to: [DS-2CD2423G0-I(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.6.821_230831_S3000525150.zip) | 2023-08-31 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.6.821_230831_S3000525150.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202401/releasenote%5CNetwork_Camera-V5.6.821_Release_Note-IPC_G1_230831.pdf) |
| 5.5.83 | Applied to: [DS-2CD2423G0-I(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/52faab7e-03ae-4dee-9dbd-a67988b4b16b.zip) | 2019-02-21 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/52faab7e-03ae-4dee-9dbd-a67988b4b16b.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202401/releasenote%5CNetwork_Camera-V5.6.821_Release_Note-IPC_G1_230831.pdf) |

</details>


<details>
<summary><h2>DS-2CD2423G2-I - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2423G2-I(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2425FWD-I - IPC_G1 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.6.821 | Applied to: [DS-2CD2425FWD-I(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.6.821_230831_S3000525150.zip) | 2023-08-31 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.6.821_230831_S3000525150.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202401/releasenote%5CNetwork_Camera-V5.6.821_Release_Note-IPC_G1_230831.pdf) |

</details>


<details>
<summary><h2>DS-2CD2426G2-I - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2426G2-I(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip)(C) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2443G0-I - IPC_G1 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.6.821 | Applied to: [DS-2CD2443G0-I(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.6.821_230831_S3000525150.zip) | 2023-08-31 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.6.821_230831_S3000525150.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202401/releasenote%5CNetwork_Camera-V5.6.821_Release_Note-IPC_G1_230831.pdf) |
| 5.5.83 | Applied to: [DS-2CD2443G0-I(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/52faab7e-03ae-4dee-9dbd-a67988b4b16b.zip) | 2019-02-21 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/52faab7e-03ae-4dee-9dbd-a67988b4b16b.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202401/releasenote%5CNetwork_Camera-V5.6.821_Release_Note-IPC_G1_230831.pdf) |

</details>


<details>
<summary><h2>DS-2CD2443G2-I - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2443G2-I(2mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2446G2-I - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2446G2-I(2mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip)(C) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2455FWD-I - IPC_G1 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.6.821 | Applied to: [DS-2CD2455FWD-I(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.6.821_230831_S3000525150.zip) | 2023-08-31 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.6.821_230831_S3000525150.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202401/releasenote%5CNetwork_Camera-V5.6.821_Release_Note-IPC_G1_230831.pdf) |

</details>


<details>
<summary><h2>DS-2CD2463G0-I - IPC_G1 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.6.821 | Applied to: [DS-2CD2463G0-I(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.6.821_230831_S3000525150.zip) | 2023-08-31 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.6.821_230831_S3000525150.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202401/releasenote%5CNetwork_Camera-V5.6.821_Release_Note-IPC_G1_230831.pdf) |

</details>


<details>
<summary><h2>DS-2CD2463G2-I - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2463G2-I(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2466G2-I - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2466G2-I(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip)(C) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2483G2-I - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2483G2-I(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2523G0-I - IPC_G1 (3 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.6.821 | Applied to: [DS-2CD2523G0-I(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.6.821_230831_S3000525150.zip) | 2023-08-31 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.6.821_230831_S3000525150.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202401/releasenote%5CNetwork_Camera-V5.6.821_Release_Note-IPC_G1_230831.pdf) |
| 5.6.6 | Applied to: [DS-2CD2523G0-I(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/f18aceb7-b896-4c7d-ad2e-8f0d2a91bcc3.zip) | 2021-06-25 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/f18aceb7-b896-4c7d-ad2e-8f0d2a91bcc3.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202401/releasenote%5CNetwork_Camera-V5.6.821_Release_Note-IPC_G1_230831.pdf) |
| 5.6.2 | Applied to: [DS-2CD2523G0-I(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/f88f5389-fd05-44ea-9adc-874910511d97.zip) | 2019-07-01 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/f88f5389-fd05-44ea-9adc-874910511d97.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202401/releasenote%5CNetwork_Camera-V5.6.821_Release_Note-IPC_G1_230831.pdf) |

</details>


<details>
<summary><h2>DS-2CD2523G2-I - IPC_G0 (3 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2523G2-I(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip)(D) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202507/releasenote%5CNetwork_Camera-V5.7.0_SP6_Release_Note-G6_I.pdf) |
| 5.7.0 | Applied to: [DS-2CD2523G2-I(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.0_240129_S3000555034.zip)(D) | 2024-10-23 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.0_240129_S3000555034.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202507/releasenote%5CNetwork_Camera-V5.7.0_SP6_Release_Note-G6_I.pdf) |
| 5.7.18 | Applied to: [DS-2CD2523G2-I(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.18_240826_S3000597013.zip)(D) | 2024-08-26 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.18_240826_S3000597013.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202507/releasenote%5CNetwork_Camera-V5.7.0_SP6_Release_Note-G6_I.pdf) |

</details>


<details>
<summary><h2>DS-2CD2523G2-IS - IPC_G0 (3 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2523G2-I(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip)(D) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202507/releasenote%5CNetwork_Camera-V5.7.0_SP6_Release_Note-G6_I.pdf) |
| 5.7.0 | Applied to: [DS-2CD2523G2-I(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.0_240129_S3000555034.zip)(D) | 2024-10-23 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.0_240129_S3000555034.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202507/releasenote%5CNetwork_Camera-V5.7.0_SP6_Release_Note-G6_I.pdf) |
| 5.7.18 | Applied to: [DS-2CD2523G2-I(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.18_240826_S3000597013.zip)(D) | 2024-08-26 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.18_240826_S3000597013.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202507/releasenote%5CNetwork_Camera-V5.7.0_SP6_Release_Note-G6_I.pdf) |

</details>


<details>
<summary><h2>DS-2CD2523G2-LI - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2523G2-LI2U(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2525FWD-I - IPC_G1 (3 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.6.821 | Applied to: [DS-2CD2525FWD-I(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.6.821_230831_S3000525150.zip) | 2023-08-31 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.6.821_230831_S3000525150.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202401/releasenote%5CNetwork_Camera-V5.6.821_Release_Note-IPC_G1_230831.pdf) |
| 5.6.6 | Applied to: [DS-2CD2525FWD-I(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/f18aceb7-b896-4c7d-ad2e-8f0d2a91bcc3.zip) | 2021-06-25 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/f18aceb7-b896-4c7d-ad2e-8f0d2a91bcc3.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202401/releasenote%5CNetwork_Camera-V5.6.821_Release_Note-IPC_G1_230831.pdf) |
| 5.6.2 | Applied to: [DS-2CD2525FWD-I(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/f88f5389-fd05-44ea-9adc-874910511d97.zip) | 2019-07-01 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/f88f5389-fd05-44ea-9adc-874910511d97.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202401/releasenote%5CNetwork_Camera-V5.6.821_Release_Note-IPC_G1_230831.pdf) |

</details>


<details>
<summary><h2>DS-2CD2526G2-IS - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2526G2-I(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip)(D) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202507/releasenote%5CNetwork_Camera-V5.7.0_SP6_Release_Note-G6_I.pdf) |
| 5.7.0 | Applied to: [DS-2CD2526G2-I(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.0_240129_S3000555034.zip)(D) | 2024-10-23 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.0_240129_S3000555034.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202507/releasenote%5CNetwork_Camera-V5.7.0_SP6_Release_Note-G6_I.pdf) |

</details>


<details>
<summary><h2>DS-2CD2543G0-I - IPC_G1 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.6.821 | Applied to: [DS-2CD2543G0-I(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.6.821_230831_S3000525150.zip)(BLACK) | 2023-08-31 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.6.821_230831_S3000525150.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202401/releasenote%5CNetwork_Camera-V5.6.821_Release_Note-IPC_G1_230831.pdf) |
| 5.6.2 | Applied to: [DS-2CD2543G0-I(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/f88f5389-fd05-44ea-9adc-874910511d97.zip)(BLACK) | 2019-07-01 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/f88f5389-fd05-44ea-9adc-874910511d97.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202401/releasenote%5CNetwork_Camera-V5.6.821_Release_Note-IPC_G1_230831.pdf) |

</details>


<details>
<summary><h2>DS-2CD2543G2-I - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2543G2-I(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2543G2-IWS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2543G2-I(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2543G2-LI - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2543G2-LI2U(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |
| 5.8.30 | Applied to: [DS-2CD2543G2-LIZS2UY(2.8/4mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip)/O-STDBLACK | 2025-12-10 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13U.pdf) |

</details>


<details>
<summary><h2>DS-2CD2545FWD-I - IPC_G1 (3 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.6.821 | Applied to: [DS-2CD2545FWD-IWS(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.6.821_230831_S3000525150.zip)(D) | 2023-08-31 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.6.821_230831_S3000525150.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202401/releasenote%5CNetwork_Camera-V5.6.821_Release_Note-IPC_G1_230831.pdf) |
| 5.6.6 | Applied to: [DS-2CD2545FWD-IWS(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/f18aceb7-b896-4c7d-ad2e-8f0d2a91bcc3.zip)(D) | 2021-06-25 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/f18aceb7-b896-4c7d-ad2e-8f0d2a91bcc3.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202401/releasenote%5CNetwork_Camera-V5.6.821_Release_Note-IPC_G1_230831.pdf) |
| 5.6.3 | Applied to: [DS-2CD2545FWD-IWS(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/fd283720-cf75-46b4-a8b9-aaa670def906.zip)(D) | 2019-09-23 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/fd283720-cf75-46b4-a8b9-aaa670def906.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202401/releasenote%5CNetwork_Camera-V5.6.821_Release_Note-IPC_G1_230831.pdf) |

</details>


<details>
<summary><h2>DS-2CD2546G2-IS - IPC_G0 (3 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2546G2-I(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/330c4c2c-5730-4877-a942-0be87cea67ca.pdf) |
| 5.5.820 | Applied to: [DS-2CD2546G2-I(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.820_260410_S3000715634.zip) | 2023-11-08 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.820_260410_S3000715634.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/330c4c2c-5730-4877-a942-0be87cea67ca.pdf) |
| 5.5.800 | Applied to: [DS-2CD2546G2-I(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.800_211009_S3000390724.zip) | 2021-10-09 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.800_211009_S3000390724.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/330c4c2c-5730-4877-a942-0be87cea67ca.pdf) |

</details>


<details>
<summary><h2>DS-2CD2546G3-I - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.32 | Applied to: [DS-2CD2546G3-IZ2UY(2.8/4mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.32_260423_S3000719136.zip) | 2026-03-30 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.32_260423_S3000719136.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202604/releasenote%5CNetwork_Camera-V5.8.32_SP1_260330_Release_Note-H13U.pdf) |
| 5.8.30 | Applied to: [DS-2CD2546G3-IZ2UY(2.8/4mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | 2025-12-10 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13U.pdf) |

</details>


<details>
<summary><h2>DS-2CD2547G2-LS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2547G2-LS(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip)(C)(BLACK) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2555FWD-I - IPC_G1 (3 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.6.821 | Applied to: [DS-2CD2555FWD-I(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.6.821_230831_S3000525150.zip) | 2023-08-31 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.6.821_230831_S3000525150.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202401/releasenote%5CNetwork_Camera-V5.6.821_Release_Note-IPC_G1_230831.pdf) |
| 5.6.6 | Applied to: [DS-2CD2555FWD-I(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/f18aceb7-b896-4c7d-ad2e-8f0d2a91bcc3.zip) | 2021-06-25 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/f18aceb7-b896-4c7d-ad2e-8f0d2a91bcc3.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202401/releasenote%5CNetwork_Camera-V5.6.821_Release_Note-IPC_G1_230831.pdf) |
| 5.6.2 | Applied to: [DS-2CD2555FWD-I(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/f88f5389-fd05-44ea-9adc-874910511d97.zip) | 2019-07-01 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/f88f5389-fd05-44ea-9adc-874910511d97.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202401/releasenote%5CNetwork_Camera-V5.6.821_Release_Note-IPC_G1_230831.pdf) |

</details>


<details>
<summary><h2>DS-2CD2563G0-I - IPC_G1 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.6.821 | Applied to: [DS-2CD2563G0-I(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.6.821_230831_S3000525150.zip) | 2023-08-31 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.6.821_230831_S3000525150.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202401/releasenote%5CNetwork_Camera-V5.6.821_Release_Note-IPC_G1_230831.pdf) |
| 5.6.2 | Applied to: [DS-2CD2563G0-I(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/f88f5389-fd05-44ea-9adc-874910511d97.zip) | 2019-07-01 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/f88f5389-fd05-44ea-9adc-874910511d97.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202401/releasenote%5CNetwork_Camera-V5.6.821_Release_Note-IPC_G1_230831.pdf) |

</details>


<details>
<summary><h2>DS-2CD2563G2-I - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2563G2-IS(4mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2563G2-LI - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2563G2-LI2U(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2566G2-I - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2566G2-IS(4mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip)(C) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2583G2-I - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2583G2-I(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2583G2-IS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2583G2-I(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2583G2-LI - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2583G2-LI2U(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2586G2-I - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2586G2-IS(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip)(C) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD26123G2-LIZS2U - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.2 | Applied to: [DS-2CD26123G2-LIZS2UY/SL(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.23_260403_S3000712869.zip)/O-STD | 2025-11-03 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.23_260403_S3000712869.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202511/releasenote%5CNetwork_Camera-V5.8.2_251103_Release_Note-IPCE_G9.pdf) |

</details>


<details>
<summary><h2>DS-2CD26123G2-LIZS2UY - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.2 | Applied to: [DS-2CD26123G2-LIZS2UY(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.23_260403_S3000712869.zip) | 2025-11-03 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.23_260403_S3000712869.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202511/releasenote%5CNetwork_Camera-V5.8.2_251103_Release_Note-IPCE_G9.pdf) |

</details>


<details>
<summary><h2>DS-2CD26126G3-IZS2UY - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.3 | Applied to: [DS-2CD26126G3-IZS2UY/SRB(2.8-12)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.3_260416_S3000716238.zip)eFO-STD | 2026-03-20 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.3_260416_S3000716238.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202604/releasenote%5CNetwork_Camera-V5.8.3_SP1_260320_Release_Note-IPCE_G9.pdf) |
| 5.8.2 | Applied to: [DS-2CD26126G3-IZS2UY/SRB(2.8-12)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.23_260403_S3000712869.zip)eFO-STD | 2025-11-03 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.23_260403_S3000712869.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202511/releasenote%5CNetwork_Camera-V5.8.2_251103_Release_Note-IPCE_G9.pdf) |

</details>


<details>
<summary><h2>DS-2CD26126G3-IZSY - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.2 | Applied to: [DS-2CD26126G3-IZSY(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.23_260403_S3000712869.zip)(eF) | 2025-11-03 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.23_260403_S3000712869.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202511/releasenote%5CNetwork_Camera-V5.8.2_251103_Release_Note-IPCE_G9.pdf) |

</details>


<details>
<summary><h2>DS-2CD26166G3-IZS2UY - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.2 | Applied to: [DS-2CD26166G3-IZS2UY/SRB(2812)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.23_260403_S3000712869.zip)eFOSTDBLK | 2025-11-03 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.23_260403_S3000712869.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202511/releasenote%5CNetwork_Camera-V5.8.2_251103_Release_Note-IPCE_G9.pdf) |

</details>


<details>
<summary><h2>DS-2CD26166G3-IZSY - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.2 | Applied to: [DS-2CD26166G3-IZSY(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.23_260403_S3000712869.zip)(eF) | 2025-11-03 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.23_260403_S3000712869.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202511/releasenote%5CNetwork_Camera-V5.8.2_251103_Release_Note-IPCE_G9.pdf) |

</details>


<details>
<summary><h2>DS-2CD2621G0-I - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2621G0-IZS(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | 2024-12-11 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202507/releasenote%5CNetwork_Camera-V5.7.23_SP2_Release_Note-E8.pdf) |
| 5.5.800 | Applied to: [DS-2CD2621G0-IZS(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.800_211009_S3000390724.zip) | 2021-06-28 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.800_211009_S3000390724.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202507/releasenote%5CNetwork_Camera-V5.7.23_SP2_Release_Note-E8.pdf) |

</details>


<details>
<summary><h2>DS-2CD2623G1-IZ - IPC_G1 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.6.821 | Applied to: [DS-2CD2623G1-IZ(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.6.821_230831_S3000525150.zip) | 2023-08-31 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.6.821_230831_S3000525150.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202401/releasenote%5CNetwork_Camera-V5.6.821_Release_Note-IPC_G1_230831.pdf) |

</details>


<details>
<summary><h2>DS-2CD2623G2-IZS - IPC_G0 (3 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2623G2-IZS(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |
| 5.7.0 | Applied to: [DS-2CD2623G2-IZS(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.0_240129_S3000555034.zip)(US Branch) | 2024-10-23 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.0_240129_S3000555034.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202312/releasenote%5CNetwork_Camera-V5.7.13_Release_Note-G5.pdf) |
| 5.7.13 | Applied to: [DS-2CD2623G2-IZS(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.13_230403_S3000490228.zip)(US Branch) | 2023-04-03 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.13_230403_S3000490228.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202312/releasenote%5CNetwork_Camera-V5.7.13_Release_Note-G5.pdf) |

</details>


<details>
<summary><h2>DS-2CD2623G2-LIZS2U - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2623G2-LIZS2U(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip)O-STD/BLACK | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2625FHWD-IZS - IPC_G1 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.6.821 | Applied to: [DS-2CD2625FHWD-IZS(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.6.821_230831_S3000525150.zip) | 2023-08-31 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.6.821_230831_S3000525150.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202401/releasenote%5CNetwork_Camera-V5.6.821_Release_Note-IPC_G1_230831.pdf) |

</details>


<details>
<summary><h2>DS-2CD2625FWD-IZS - IPC_G1 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.6.821 | Applied to: [DS-2CD2625FWD-IZS(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.6.821_230831_S3000525150.zip) | 2023-08-31 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.6.821_230831_S3000525150.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202401/releasenote%5CNetwork_Camera-V5.6.821_Release_Note-IPC_G1_230831.pdf) |

</details>


<details>
<summary><h2>DS-2CD2626G2-IZS - IPC_G0 (3 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2626G2-IZS(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip)(C) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |
| 5.7.0 | Applied to: [DS-2CD2626G2-IZS(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.0_240129_S3000555034.zip) | 2024-10-23 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.0_240129_S3000555034.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202408/releasenote%5CNetwork_Camera-V5.5.820_Release_Note-G3.pdf) |
| 5.5.820 | Applied to: [DS-2CD2626G2-IZS(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.820_260410_S3000715634.zip) | 2023-11-08 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.820_260410_S3000715634.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202408/releasenote%5CNetwork_Camera-V5.5.820_Release_Note-G3.pdf) |

</details>


<details>
<summary><h2>DS-2CD2626G2-IZSU - IPC_G0 (3 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2626G2-IZSU/SL(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202408/releasenote%5CNetwork_Camera-V5.5.820_Release_Note-G3.pdf) |
| 5.7.0 | Applied to: [DS-2CD2626G2-IZSU/SL(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.0_240129_S3000555034.zip) | 2024-10-23 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.0_240129_S3000555034.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202408/releasenote%5CNetwork_Camera-V5.5.820_Release_Note-G3.pdf) |
| 5.5.820 | Applied to: [DS-2CD2626G2-IZSU/SL(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.820_260410_S3000715634.zip) | 2023-11-08 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.820_260410_S3000715634.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202408/releasenote%5CNetwork_Camera-V5.5.820_Release_Note-G3.pdf) |

</details>


<details>
<summary><h2>DS-2CD2626G2T-IZS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.0 | Applied to: [DS-2CD2626G2T-IZS(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.0_240129_S3000555034.zip)(D) | 2024-10-23 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.0_240129_S3000555034.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202507/releasenote%5CNetwork_Camera-V5.7.0_SP6_Release_Note-G6_I.pdf) |

</details>


<details>
<summary><h2>DS-2CD2643G1-IZ - IPC_G1 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.6.821 | Applied to: [DS-2CD2643G1-IZS(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.6.821_230831_S3000525150.zip) | 2023-08-31 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.6.821_230831_S3000525150.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202401/releasenote%5CNetwork_Camera-V5.6.821_Release_Note-IPC_G1_230831.pdf) |

</details>


<details>
<summary><h2>DS-2CD2643G2-IZS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2643G2-IZS(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2643G2-LIZS2U - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2643G2-LIZS2U(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip)O-STD/BLACK | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2645FWD-IZS - IPC_G1 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.6.821 | Applied to: [DS-2CD2645FWD-IZS/2](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.6.821_230831_S3000525150.zip).8-12mm/B/O-STD/BLACK | 2023-08-31 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.6.821_230831_S3000525150.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202401/releasenote%5CNetwork_Camera-V5.6.821_Release_Note-IPC_G1_230831.pdf) |

</details>


<details>
<summary><h2>DS-2CD2646G1-IZS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.6.0 | Applied to: [DS-2CD2646G1-IZS(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/18db80e0-2712-4496-8bd3-646f5014a59b.zip) | 2019-05-07 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/18db80e0-2712-4496-8bd3-646f5014a59b.zip) |  |

</details>


<details>
<summary><h2>DS-2CD2646G2-IZS - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2646G2-IZS(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202408/releasenote%5CNetwork_Camera-V5.5.820_Release_Note-G3.pdf) |
| 5.5.820 | Applied to: [DS-2CD2646G2-IZS(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.820_260410_S3000715634.zip) | 2023-11-08 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.820_260410_S3000715634.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202408/releasenote%5CNetwork_Camera-V5.5.820_Release_Note-G3.pdf) |

</details>


<details>
<summary><h2>DS-2CD2646G2-IZSU - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2646G2-IZSU/SL(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/330c4c2c-5730-4877-a942-0be87cea67ca.pdf) |
| 5.5.800 | Applied to: [DS-2CD2646G2-IZSU/SL(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.800_211009_S3000390724.zip) | 2021-10-09 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.800_211009_S3000390724.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/330c4c2c-5730-4877-a942-0be87cea67ca.pdf) |

</details>


<details>
<summary><h2>DS-2CD2646G2H-IZS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2646G2H-IZS(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip)(eF) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2646G2H-IZS2U - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2646G2H-IZS2U/SRB(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip)eFO-STD | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2646G2HT-IZS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2646G2HT-IZS(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip)(eF) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2646G2HT-IZS2U - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2646G2HT-IZS2U/SL(2.8-12)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip)eFOSTDBLK | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2646G2T-IZS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2646G2T-IZS(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip)(C) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2646G2T-IZSY - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2646G2T-IZSY(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip)(C) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2647G2-LZS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2647G2-LZS(3.6-9mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip)(C) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2647G2T-LZS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2647G2T-LZS(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip)(C) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2647G3-LIZS2UY - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.32 | Applied to: [DS-2CD2647G3-LIZS2UY/SRB(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.32_260423_S3000719136.zip)/O-STD | 2026-04-23 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.32_260423_S3000719136.zip) |  |
| 5.8.30 | Applied to: [DS-2CD2647G3-LIZS2UY/SRB(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip)/O-STD | 2025-12-10 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13U.pdf) |

</details>


<details>
<summary><h2>DS-2CD2647G3-LIZS2UY-S-L--RB- - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.32 | [DS-2CD2647G3-LIZS2UY-S-L--RB-](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.32_260423_S3000719136.zip) | 2026-04-23 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.32_260423_S3000719136.zip) |  |

</details>


<details>
<summary><h2>DS-2CD2647G3-LIZSY - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.32 | Applied to: [DS-2CD2647G3-LIZSY(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.32_260423_S3000719136.zip) | 2026-04-23 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.32_260423_S3000719136.zip) |  |
| 5.8.30 | Applied to: [DS-2CD2647G3-LIZSY(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | 2025-12-10 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13U.pdf) |

</details>


<details>
<summary><h2>DS-2CD2647G3T-LIZSY - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.32 | Applied to: [DS-2CD2647G3T-LIZSY(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.32_260423_S3000719136.zip) | 2026-04-23 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.32_260423_S3000719136.zip) |  |
| 5.8.30 | Applied to: [DS-2CD2647G3T-LIZSY(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | 2025-12-10 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13U.pdf) |

</details>


<details>
<summary><h2>DS-2CD2663G1-IZ - IPC_G1 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.6.821 | Applied to: [DS-2CD2663G1-IZS(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.6.821_230831_S3000525150.zip) | 2023-08-31 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.6.821_230831_S3000525150.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202401/releasenote%5CNetwork_Camera-V5.6.821_Release_Note-IPC_G1_230831.pdf) |

</details>


<details>
<summary><h2>DS-2CD2663G2-IZS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2663G2-IZS(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2663G2-LIZS2U - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2663G2-LIZS2U(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2665G0-IZS - IPC_G1 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.6.821 | Applied to: [DS-2CD2665G0-IZS(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.6.821_230831_S3000525150.zip) | 2023-08-31 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.6.821_230831_S3000525150.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202401/releasenote%5CNetwork_Camera-V5.6.821_Release_Note-IPC_G1_230831.pdf) |

</details>


<details>
<summary><h2>DS-2CD2666G2-IZS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2666G2-IZS(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip)(C) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2666G2-IZSU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2666G2-IZSU/SL(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip)(C) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2666G2H-IZS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2666G2H-IZS(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip)(eF) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2666G2H-IZS2U - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2666G2H-IZS2U/SRB(2812)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip)eFO-STDBLK | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2666G2HT-IZS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2666G2HT-IZS(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip)(eF)O-STDBLK | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2666G2HT-IZS2U - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2666G2HT-IZS2U/SL(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip)eFO-STD | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2666G2T-IZS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2666G2T-IZS(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip)(C) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2667G2HT-LIZS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2667G2HT-LIZS(2.8-12)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip)/eF/O-STD/BLK | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2667G2T-LZS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2667G2T-LZS(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip)(C) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2667G3-LIZS2UY - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD2667G3-LIZS2UY/SL(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | 2025-12-10 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD2667G3-LIZSY - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD2667G3-LIZSY(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip)/O-STD/BLACK | 2025-12-10 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD2667G3T-LIZSY - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD2667G3T-LIZSY(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | 2025-12-10 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD2683G1-IZ - IPC_G1 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.6.821 | Applied to: [DS-2CD2683G1-IZ(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.6.821_230831_S3000525150.zip) | 2023-08-31 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.6.821_230831_S3000525150.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202401/releasenote%5CNetwork_Camera-V5.6.821_Release_Note-IPC_G1_230831.pdf) |

</details>


<details>
<summary><h2>DS-2CD2683G2-IZS - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.6 | Applied to: [DS-2CD2683G2-IZS(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.6_260128_S3000701683.zip)(D) | 2026-01-28 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.6_260128_S3000701683.zip) |  |
| 5.7.23 | Applied to: [DS-2CD2683G2-IZS(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip)(D) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2683G2-LIZS2U - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.6 | Applied to: [DS-2CD2683G2-LIZS2U(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.6_260128_S3000701683.zip)(T) | 2026-01-28 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.6_260128_S3000701683.zip) |  |
| 5.7.23 | Applied to: [DS-2CD2683G2-LIZS2U(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip)O-STD/BLACK | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2685G0-IZS - IPC_G1 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.6.821 | Applied to: [DS-2CD2685G0-IZS(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.6.821_230831_S3000525150.zip) | 2023-08-31 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.6.821_230831_S3000525150.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202401/releasenote%5CNetwork_Camera-V5.6.821_Release_Note-IPC_G1_230831.pdf) |

</details>


<details>
<summary><h2>DS-2CD2686G2-IZS - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2686G2-IZS(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202408/releasenote%5CNetwork_Camera-V5.5.820_Release_Note-G3.pdf) |
| 5.5.820 | Applied to: [DS-2CD2686G2-IZS(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.820_260410_S3000715634.zip) | 2023-11-08 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.820_260410_S3000715634.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202408/releasenote%5CNetwork_Camera-V5.5.820_Release_Note-G3.pdf) |

</details>


<details>
<summary><h2>DS-2CD2686G2-IZSU - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2686G2-IZSU/SL(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202408/releasenote%5CNetwork_Camera-V5.5.820_Release_Note-G3.pdf) |
| 5.5.820 | Applied to: [DS-2CD2686G2-IZSU/SL(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.820_260410_S3000715634.zip) | 2023-11-08 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.820_260410_S3000715634.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202408/releasenote%5CNetwork_Camera-V5.5.820_Release_Note-G3.pdf) |

</details>


<details>
<summary><h2>DS-2CD2686G2H-IZS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2686G2H-IZS(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip)eF/O-STDBLACK | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2686G2H-IZS2U - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2686G2H-IZS2U/SRB(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip)eFO-STD | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2686G2HT-IZS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2686G2HT-IZS(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip)(eF) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2686G2HT-IZS2U - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2686G2HT-IZS2U/SL(2.8-12)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip)eFOSTDBLK | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2686G2T-IZS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2686G2T-IZS(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip)(C) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2686G2T-IZSY - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2686G2T-IZSY(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip)(C) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2687G2T-LZS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2687G2T-LZS(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip)(C) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2687G3-LIZS2UY - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD2687G3-LIZS2UY/SRB(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip)/O-STD | 2025-12-10 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD2687G3-LIZSY - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.32 | Applied to: [DS-2CD2687G3-LIZSY(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.32_260423_S3000719136.zip) | 2026-03-30 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.32_260423_S3000719136.zip) |  |
| 5.8.30 | Applied to: [DS-2CD2687G3-LIZSY(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | 2025-12-10 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD2687G3T-LIZSY - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD2687G3T-LIZSY(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | 2025-12-10 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD27123G2-LIZS2UY - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.2 | Applied to: [DS-2CD27123G2-LIZS2UY(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.23_260403_S3000712869.zip) | 2025-11-03 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.23_260403_S3000712869.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202511/releasenote%5CNetwork_Camera-V5.8.2_251103_Release_Note-IPCE_G9.pdf) |

</details>


<details>
<summary><h2>DS-2CD27126G3-IPTRZS2UY - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.2 | Applied to: [DS-2CD27126G3-IPTRZS2UY/SL(2.8-12)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.23_260403_S3000712869.zip)O-STD | 2025-11-03 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.23_260403_S3000712869.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202511/releasenote%5CNetwork_Camera-V5.8.2_251103_Release_Note-IPCE_G9.pdf) |

</details>


<details>
<summary><h2>DS-2CD27126G3-IPTRZSY - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.2 | Applied to: [DS-2CD27126G3-IPTRZSY(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.23_260403_S3000712869.zip) | 2025-11-03 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.23_260403_S3000712869.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202511/releasenote%5CNetwork_Camera-V5.8.2_251103_Release_Note-IPCE_G9.pdf) |

</details>


<details>
<summary><h2>DS-2CD27166G3-IPTRZS2UY - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.2 | Applied to: [DS-2CD27166G3-IPTRZS2UY/SL(2.8-12)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.23_260403_S3000712869.zip)O-STD | 2025-11-03 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.23_260403_S3000712869.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202511/releasenote%5CNetwork_Camera-V5.8.2_251103_Release_Note-IPCE_G9.pdf) |

</details>


<details>
<summary><h2>DS-2CD27166G3-IPTRZSY - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.2 | Applied to: [DS-2CD27166G3-IPTRZSY(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.23_260403_S3000712869.zip) | 2025-11-03 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.23_260403_S3000712869.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202511/releasenote%5CNetwork_Camera-V5.8.2_251103_Release_Note-IPCE_G9.pdf) |

</details>


<details>
<summary><h2>DS-2CD2721G0-I - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.800 | Applied to: [DS-2CD2721G0-I(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.800_211009_S3000390724.zip) | 2021-06-28 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.800_211009_S3000390724.zip) |  |

</details>


<details>
<summary><h2>DS-2CD2723G1-IZ - IPC_G1 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.6.821 | Applied to: [DS-2CD2723G1-IZ(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.6.821_230831_S3000525150.zip) | 2023-08-31 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.6.821_230831_S3000525150.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202401/releasenote%5CNetwork_Camera-V5.6.821_Release_Note-IPC_G1_230831.pdf) |

</details>


<details>
<summary><h2>DS-2CD2723G2-IZS - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2723G2-IZS(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip)(D)O-STD/BLACK | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202507/releasenote%5CNetwork_Camera-V5.7.0_SP6_Release_Note-G6_I.pdf) |
| 5.7.0 | Applied to: [DS-2CD2723G2-IZS(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.0_240129_S3000555034.zip)(D) | 2024-10-23 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.0_240129_S3000555034.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202507/releasenote%5CNetwork_Camera-V5.7.0_SP6_Release_Note-G6_I.pdf) |

</details>


<details>
<summary><h2>DS-2CD2723G2-LIZS2U - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2723G2-LIZS2U(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip)O-STD/BLACK | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2725FHWD-IZS - IPC_G1 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.6.821 | Applied to: [DS-2CD2725FHWD-IZS(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.6.821_230831_S3000525150.zip) | 2023-08-31 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.6.821_230831_S3000525150.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202401/releasenote%5CNetwork_Camera-V5.6.821_Release_Note-IPC_G1_230831.pdf) |

</details>


<details>
<summary><h2>DS-2CD2725FWD-IZS - IPC_G1 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.6.821 | Applied to: [DS-2CD2725FWD-IZS(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.6.821_230831_S3000525150.zip) | 2023-08-31 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.6.821_230831_S3000525150.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202401/releasenote%5CNetwork_Camera-V5.6.821_Release_Note-IPC_G1_230831.pdf) |

</details>


<details>
<summary><h2>DS-2CD2726G1-IZS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.6.0 | Applied to: [DS-2CD2726G1-IZS(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/18db80e0-2712-4496-8bd3-646f5014a59b.zip) | 2019-05-07 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/18db80e0-2712-4496-8bd3-646f5014a59b.zip) |  |

</details>


<details>
<summary><h2>DS-2CD2726G2-IZS - IPC_G0 (3 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2726G2-IZS(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202408/releasenote%5CNetwork_Camera-V5.5.820_Release_Note-G3.pdf) |
| 5.7.0 | Applied to: [DS-2CD2726G2-IZS(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.0_240129_S3000555034.zip) | 2024-10-23 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.0_240129_S3000555034.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202408/releasenote%5CNetwork_Camera-V5.5.820_Release_Note-G3.pdf) |
| 5.5.820 | Applied to: [DS-2CD2726G2-IZS(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.820_260410_S3000715634.zip) | 2023-11-08 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.820_260410_S3000715634.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202408/releasenote%5CNetwork_Camera-V5.5.820_Release_Note-G3.pdf) |

</details>


<details>
<summary><h2>DS-2CD2726G2T-IZS - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2726G2T-IZS(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip)(D) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202507/releasenote%5CNetwork_Camera-V5.7.0_SP6_Release_Note-G6_I.pdf) |
| 5.7.0 | Applied to: [DS-2CD2726G2T-IZS(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.0_240129_S3000555034.zip)(D) | 2024-10-23 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.0_240129_S3000555034.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202507/releasenote%5CNetwork_Camera-V5.7.0_SP6_Release_Note-G6_I.pdf) |

</details>


<details>
<summary><h2>DS-2CD2743G1-IZ - IPC_G1 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.6.821 | Applied to: [DS-2CD2743G1-IZS(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.6.821_230831_S3000525150.zip)(BLACK) | 2023-08-31 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.6.821_230831_S3000525150.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202401/releasenote%5CNetwork_Camera-V5.6.821_Release_Note-IPC_G1_230831.pdf) |

</details>


<details>
<summary><h2>DS-2CD2743G2-IZS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2743G2-IZS(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2743G2-LIZS2U - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2743G2-LIZS2U(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip)O-STD/BLACK | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2745FWD-IZS - IPC_G1 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.6.821 | Applied to: [DS-2CD2745FWD-IZS/2](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.6.821_230831_S3000525150.zip).8-12mm/B/O-STD/BLACK | 2023-08-31 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.6.821_230831_S3000525150.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202401/releasenote%5CNetwork_Camera-V5.6.821_Release_Note-IPC_G1_230831.pdf) |

</details>


<details>
<summary><h2>DS-2CD2746G1-IZS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.6.0 | Applied to: [DS-2CD2746G1-IZS(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/18db80e0-2712-4496-8bd3-646f5014a59b.zip) | 2019-05-07 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/18db80e0-2712-4496-8bd3-646f5014a59b.zip) |  |

</details>


<details>
<summary><h2>DS-2CD2746G2-IZS - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2746G2-IZS(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip)(C) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |
| 5.5.820 | Applied to: [DS-2CD2746G2-IZS(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.820_260410_S3000715634.zip) | 2023-11-08 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.820_260410_S3000715634.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202408/releasenote%5CNetwork_Camera-V5.5.820_Release_Note-G3.pdf) |

</details>


<details>
<summary><h2>DS-2CD2746G2H-IPTRZS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2746G2H-IPTRZS(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2746G2H-IPTRZS2U - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2746G2H-IPTRZS2U/SL(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip)O-STD | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2746G2HT-IZS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2746G2HT-IZS(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip)(eF) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2746G2T-IZS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2746G2T-IZS(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip)(C) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2746G3-IPTRZS2UY - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.32 | Applied to: [DS-2CD2746G3-IPTRZS2UY/SRB(2.8-12)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.32_260423_S3000719136.zip)O-STD | 2026-04-23 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.32_260423_S3000719136.zip) |  |
| 5.8.30 | Applied to: [DS-2CD2746G3-IPTRZS2UY/SRB(2.8-12)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip)O-STD | 2025-12-10 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13U.pdf) |

</details>


<details>
<summary><h2>DS-2CD2746G3-IPTRZS2UY-S-L--RB- - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.32 | [DS-2CD2746G3-IPTRZS2UY-S-L--RB-](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.32_260423_S3000719136.zip) | 2026-04-23 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.32_260423_S3000719136.zip) |  |

</details>


<details>
<summary><h2>DS-2CD2746G3-IPTRZSY - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.32 | Applied to: [DS-2CD2746G3-IPTRZSY(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.32_260423_S3000719136.zip) | 2026-04-23 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.32_260423_S3000719136.zip) |  |
| 5.8.30 | Applied to: [DS-2CD2746G3-IPTRZSY(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | 2025-12-10 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13U.pdf) |

</details>


<details>
<summary><h2>DS-2CD2747G2-LZS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2747G2-LZS(3.6-9mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip)(C) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2747G2H-LIPTRZS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2747G2H-LIPTRZS(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip)OSTDBLACK | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2747G2H-LIPTRZS2U - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2747G2H-LIPTRZS2U/SL(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip)OSTD | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2747G2T-LZS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2747G2T-LZS(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip)(C) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2747G3-LIPTRZS2UY - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.32 | Applied to: [DS-2CD2747G3-LIPTRZS2UY/SL(2.8-12)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.32_260423_S3000719136.zip)O-STD | 2026-04-23 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.32_260423_S3000719136.zip) |  |

</details>


<details>
<summary><h2>DS-2CD2747G3-LIPTRZS2UY-S-L--RB- - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.32 | [DS-2CD2747G3-LIPTRZS2UY-S-L--RB-](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.32_260423_S3000719136.zip) | 2026-04-23 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.32_260423_S3000719136.zip) |  |

</details>


<details>
<summary><h2>DS-2CD2747G3-LIPTRZSY - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.32 | Applied to: [DS-2CD2747G3-LIPTRZSY(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.32_260423_S3000719136.zip) | 2026-04-23 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.32_260423_S3000719136.zip) |  |

</details>


<details>
<summary><h2>DS-2CD2747G3T-LIZSY - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.32 | Applied to: [DS-2CD2747G3T-LIZSY(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.32_260423_S3000719136.zip) | 2026-04-23 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.32_260423_S3000719136.zip) |  |
| 5.8.30 | Applied to: [DS-2CD2747G3T-LIZSY(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | 2025-12-10 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13U.pdf) |

</details>


<details>
<summary><h2>DS-2CD2763G1-IZ - IPC_G1 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.6.821 | Applied to: [DS-2CD2763G1-IZ(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.6.821_230831_S3000525150.zip) | 2023-08-31 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.6.821_230831_S3000525150.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202401/releasenote%5CNetwork_Camera-V5.6.821_Release_Note-IPC_G1_230831.pdf) |

</details>


<details>
<summary><h2>DS-2CD2763G2-IZS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2763G2-IZS(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2763G2-LIZS2U - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2763G2-LIZS2U(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2765G0-IZS - IPC_G1 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.6.821 | Applied to: [DS-2CD2765G0-IZS(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.6.821_230831_S3000525150.zip) | 2023-08-31 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.6.821_230831_S3000525150.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202401/releasenote%5CNetwork_Camera-V5.6.821_Release_Note-IPC_G1_230831.pdf) |

</details>


<details>
<summary><h2>DS-2CD2766G2-IZS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2766G2-IZS(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip)(C) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2766G2H-IPTRZS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2766G2H-IPTRZS(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2766G2H-IPTRZS2U - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2766G2H-IPTRZS2U/SL(2.8-12)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip)OSTDBLK | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2766G2HT-IZS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2766G2HT-IZS(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip)(eF) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2766G3-IPTRZS2UY - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD2766G3-IPTRZS2UY/SL(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip)O-STD | 2025-12-10 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD2766G3-IPTRZSY - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD2766G3-IPTRZSY(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | 2025-12-10 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD2767G2H-LIPTRZS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2767G2H-LIPTRZS(2.8-12)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip)O-STDBLACK | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2767G2H-LIPTRZS2U - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2767G2H-LIPTRZS2U/SL(2812)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip)OSTDBLK | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2767G2HT-LIZS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2767G2HT-LIZS(2.8-12)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip)/eF/O-STD/BLK | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2767G2T-LZS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2767G2T-LZS(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip)(C) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2767G3-LIPTRZS2UY - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.32 | Applied to: [DS-2CD2767G3-LIPTRZS2UY/SL(2.8-12)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.32_260423_S3000719136.zip)O-STD | 2026-03-30 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.32_260423_S3000719136.zip) |  |

</details>


<details>
<summary><h2>DS-2CD2767G3-LIPTRZSY - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.32 | Applied to: [DS-2CD2767G3-LIPTRZSY(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.32_260423_S3000719136.zip) | 2026-03-30 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.32_260423_S3000719136.zip) |  |

</details>


<details>
<summary><h2>DS-2CD2767G3T-LIZSY - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.32 | Applied to: [DS-2CD2767G3T-LIZSY(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.32_260423_S3000719136.zip) | 2026-03-30 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.32_260423_S3000719136.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202604/releasenote%5CNetwork_Camera-V5.8.32_SP1_260330_Release_Note-H13.pdf) |
| 5.8.30 | Applied to: [DS-2CD2767G3T-LIZSY(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | 2025-12-10 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD2783G1-IZ - IPC_G1 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.6.821 | Applied to: [DS-2CD2783G1-IZ(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.6.821_230831_S3000525150.zip) | 2023-08-31 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.6.821_230831_S3000525150.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202401/releasenote%5CNetwork_Camera-V5.6.821_Release_Note-IPC_G1_230831.pdf) |

</details>


<details>
<summary><h2>DS-2CD2783G2-IZS - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.6 | Applied to: [DS-2CD2783G2-IZS(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.6_260128_S3000701683.zip)(D) | 2026-01-28 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.6_260128_S3000701683.zip) |  |
| 5.7.23 | Applied to: [DS-2CD2783G2-IZS(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2783G2-LIZS2U - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.6 | Applied to: [DS-2CD2783G2-LIZS2U(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.6_260128_S3000701683.zip)(T) | 2026-01-28 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.6_260128_S3000701683.zip) |  |
| 5.7.23 | Applied to: [DS-2CD2783G2-LIZS2U(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip)(T) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2785G0-IZS - IPC_G1 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.6.821 | Applied to: [DS-2CD2785G0-IZS(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.6.821_230831_S3000525150.zip) | 2023-08-31 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.6.821_230831_S3000525150.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202401/releasenote%5CNetwork_Camera-V5.6.821_Release_Note-IPC_G1_230831.pdf) |

</details>


<details>
<summary><h2>DS-2CD2786G2-IZS - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2786G2-IZS(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202408/releasenote%5CNetwork_Camera-V5.5.820_Release_Note-G3.pdf) |
| 5.5.820 | Applied to: [DS-2CD2786G2-IZS(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.820_260410_S3000715634.zip) | 2023-11-08 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.820_260410_S3000715634.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202408/releasenote%5CNetwork_Camera-V5.5.820_Release_Note-G3.pdf) |

</details>


<details>
<summary><h2>DS-2CD2786G2H-IPTRZS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2786G2H-IPTRZS(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2786G2H-IPTRZS2U - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2786G2H-IPTRZS2U/SL(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip)O-STD | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2786G2HT-IZS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2786G2HT-IZS(2.8-12)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip)/eF/O-STD/BLK | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2786G3-IPTRZS2UY - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD2786G3-IPTRZS2UY/SL(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip)O-STD | 2025-12-10 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD2786G3-IPTRZSY - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD2786G3-IPTRZSY(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | 2025-12-10 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD2787G2H-LIPTRZS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2787G2H-LIPTRZS(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip)OSTDBLACK | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2787G2H-LIPTRZS2U - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2787G2H-LIPTRZS2U/SL(2812)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip)OSTDBLK | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2787G2HT-LIZS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2787G2HT-LIZS(2.8-12)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip)/eF/O-STD/BLK | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2787G2T-LZS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2787G2T-LZS(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip)(C) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2787G3-LIPTRZS2UY - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.32 | Applied to: [DS-2CD2787G3-LIPTRZS2UY/SL(2.8-12)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.32_260423_S3000719136.zip)O-STD | 2026-03-30 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.32_260423_S3000719136.zip) |  |

</details>


<details>
<summary><h2>DS-2CD2787G3-LIPTRZSY - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.32 | Applied to: [DS-2CD2787G3-LIPTRZSY(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.32_260423_S3000719136.zip) | 2026-03-30 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.32_260423_S3000719136.zip) |  |

</details>


<details>
<summary><h2>DS-2CD2787G3T-LIZSY - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD2787G3T-LIZSY(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | 2025-12-10 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD2821G0 - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.800 | Applied to: [DS-2CD2821G0](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.800_211009_S3000390724.zip) | 2021-06-28 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.800_211009_S3000390724.zip) |  |

</details>


<details>
<summary><h2>DS-2CD2935FWD-I - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.4.52 | Applied to: [DS-2CD2935FWD-I(1.16mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/7d4a69ad-ffac-4b30-a09d-66f19a538df0.zip) | 2020-04-16 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/7d4a69ad-ffac-4b30-a09d-66f19a538df0.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202312/releasenote%5CIPC_V5.4.52_G1__Release_Note--External.pdf) |

</details>


<details>
<summary><h2>DS-2CD2955FWD-I - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.4.52 | Applied to: [DS-2CD2955FWD-IS(1.05mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/7d4a69ad-ffac-4b30-a09d-66f19a538df0.zip) | 2020-04-16 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/7d4a69ad-ffac-4b30-a09d-66f19a538df0.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202312/releasenote%5CIPC_V5.4.52_G1__Release_Note--External.pdf) |

</details>


<details>
<summary><h2>DS-2CD2955G0-IS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.21 | Applied to: [DS-2CD2955G0-IS(1.05mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.211_250825_S3000670507.zip) | 2024-12-11 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.211_250825_S3000670507.zip) |  |

</details>


<details>
<summary><h2>DS-2CD2D25G1-D - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.210 | Applied to: [DS-2CD2D25G1-D/NF(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/IPCG_E8_EN_STD_5.7.210_220615.zip) | 2022-06-15 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/IPCG_E8_EN_STD_5.7.210_220615.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202312/releasenote%5CIPC_V5.7.210_SP_Release_Note--EN.pdf) |

</details>


<details>
<summary><h2>DS-2CD2D45G1 - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.210 | Applied to: [DS-2CD2D45G1/M-D/NF(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/IPCG_E8_EN_STD_5.7.210_220615.zip) | 2022-06-15 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/IPCG_E8_EN_STD_5.7.210_220615.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202312/releasenote%5CIPC_V5.7.210_SP_Release_Note--EN.pdf) |

</details>


<details>
<summary><h2>DS-2CD2D45G2-U - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.23 | Applied to: [DS-2CD2D45G2-U(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.23_260403_S3000712869.zip) | 2025-07-16 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.23_260403_S3000712869.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CCovert_Camera_2Dxx_V5.8.23_250716_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2E23G2-U - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2E23G2-U(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2E43G2-U - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2E43G2-U(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip)(BLACK) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2H123G2-LIZS2UY - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.2 | Applied to: [DS-2CD2H123G2-LIZS2UY(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.23_260403_S3000712869.zip) | 2025-11-03 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.23_260403_S3000712869.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202511/releasenote%5CNetwork_Camera-V5.8.2_251103_Release_Note-IPCE_G9.pdf) |

</details>


<details>
<summary><h2>DS-2CD2H126G3-IZS2UY - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.3 | Applied to: [DS-2CD2H126G3-IZS2UY/SRB(2.8-12)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.3_260416_S3000716238.zip)eFO-STD | 2026-03-20 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.3_260416_S3000716238.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202604/releasenote%5CNetwork_Camera-V5.8.3_SP1_260320_Release_Note-IPCE_G9.pdf) |
| 5.8.2 | Applied to: [DS-2CD2H126G3-IZS2UY/SRB(2.8-12)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.23_260403_S3000712869.zip)eFO-STD | 2025-11-03 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.23_260403_S3000712869.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202511/releasenote%5CNetwork_Camera-V5.8.2_251103_Release_Note-IPCE_G9.pdf) |

</details>


<details>
<summary><h2>DS-2CD2H126G3-IZSY - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.2 | Applied to: [DS-2CD2H126G3-IZSY(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.23_260403_S3000712869.zip)(eF) | 2025-11-03 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.23_260403_S3000712869.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202511/releasenote%5CNetwork_Camera-V5.8.2_251103_Release_Note-IPCE_G9.pdf) |

</details>


<details>
<summary><h2>DS-2CD2H166G3-IZS2UY - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.2 | Applied to: [DS-2CD2H166G3-IZS2UY/SRB(2.8-12)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.23_260403_S3000712869.zip)eFO-STD | 2025-11-03 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.23_260403_S3000712869.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202511/releasenote%5CNetwork_Camera-V5.8.2_251103_Release_Note-IPCE_G9.pdf) |

</details>


<details>
<summary><h2>DS-2CD2H166G3-IZSY - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.2 | Applied to: [DS-2CD2H166G3-IZSY(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.23_260403_S3000712869.zip)(eF) | 2025-11-03 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.23_260403_S3000712869.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202511/releasenote%5CNetwork_Camera-V5.8.2_251103_Release_Note-IPCE_G9.pdf) |

</details>


<details>
<summary><h2>DS-2CD2H23G1-IZ - IPC_G1 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.6.821 | Applied to: [DS-2CD2H23G1-IZS(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.6.821_230831_S3000525150.zip) | 2023-08-31 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.6.821_230831_S3000525150.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202401/releasenote%5CNetwork_Camera-V5.6.821_Release_Note-IPC_G1_230831.pdf) |

</details>


<details>
<summary><h2>DS-2CD2H23G2-IZS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2H23G2-IZS(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2H23G2-LIZS2U - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2H23G2-LIZS2U(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip)/O-STDBLACK | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2H25FHWD-IZS - IPC_G1 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.6.821 | Applied to: [DS-2CD2H25FHWD-IZS(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.6.821_230831_S3000525150.zip) | 2023-08-31 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.6.821_230831_S3000525150.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202401/releasenote%5CNetwork_Camera-V5.6.821_Release_Note-IPC_G1_230831.pdf) |

</details>


<details>
<summary><h2>DS-2CD2H25FWD-IZS - IPC_G1 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.6.821 | Applied to: [DS-2CD2H25FWD-IZS(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.6.821_230831_S3000525150.zip) | 2023-08-31 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.6.821_230831_S3000525150.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202401/releasenote%5CNetwork_Camera-V5.6.821_Release_Note-IPC_G1_230831.pdf) |

</details>


<details>
<summary><h2>DS-2CD2H26G2-IZS - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2H26G2-IZS(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202408/releasenote%5CNetwork_Camera-V5.5.820_Release_Note-G3.pdf) |
| 5.5.820 | Applied to: [DS-2CD2H26G2-IZS(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.820_260410_S3000715634.zip) | 2023-11-08 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.820_260410_S3000715634.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202408/releasenote%5CNetwork_Camera-V5.5.820_Release_Note-G3.pdf) |

</details>


<details>
<summary><h2>DS-2CD2H43G1-IZ - IPC_G1 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.6.821 | Applied to: [DS-2CD2H43G1-IZ(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.6.821_230831_S3000525150.zip) | 2023-08-31 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.6.821_230831_S3000525150.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202401/releasenote%5CNetwork_Camera-V5.6.821_Release_Note-IPC_G1_230831.pdf) |

</details>


<details>
<summary><h2>DS-2CD2H43G2-IZS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2H43G2-IZS(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2H43G2-LIZS2U - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2H43G2-LIZS2U(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip)/O-STDBLACK | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2H45FWD-IZS - IPC_G1 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.6.821 | Applied to: [DS-2CD2H45FWD-IZS(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.6.821_230831_S3000525150.zip)(B) | 2023-08-31 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.6.821_230831_S3000525150.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202401/releasenote%5CNetwork_Camera-V5.6.821_Release_Note-IPC_G1_230831.pdf) |

</details>


<details>
<summary><h2>DS-2CD2H46G2-IZS - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2H46G2-IZS(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/330c4c2c-5730-4877-a942-0be87cea67ca.pdf) |
| 5.5.800 | Applied to: [DS-2CD2H46G2-IZS(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.800_211009_S3000390724.zip) | 2021-10-09 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.800_211009_S3000390724.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/330c4c2c-5730-4877-a942-0be87cea67ca.pdf) |

</details>


<details>
<summary><h2>DS-2CD2H46G2H-IZS2UY - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2H46G2H-IZS2UY/SRB(2.8-12)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip)eFO-STD | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2H46G2H-IZSY - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2H46G2H-IZSY(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip)(eF) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2H47G3-LIZS2UY - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.32 | Applied to: [DS-2CD2H47G3-LIZS2UY/SRB(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.32_260423_S3000719136.zip)/O-STD | 2026-04-23 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.32_260423_S3000719136.zip) |  |
| 5.8.30 | Applied to: [DS-2CD2H47G3-LIZS2UY/SRB(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip)/O-STD | 2025-12-10 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13U.pdf) |

</details>


<details>
<summary><h2>DS-2CD2H47G3-LIZS2UY-S-L--RB- - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.32 | [DS-2CD2H47G3-LIZS2UY-S-L--RB-](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.32_260423_S3000719136.zip) | 2026-04-23 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.32_260423_S3000719136.zip) |  |

</details>


<details>
<summary><h2>DS-2CD2H47G3-LIZSY - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.32 | Applied to: [DS-2CD2H47G3-LIZSY(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.32_260423_S3000719136.zip) | 2026-04-23 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.32_260423_S3000719136.zip) |  |
| 5.8.30 | Applied to: [DS-2CD2H47G3-LIZSY(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | 2025-12-10 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13U.pdf) |

</details>


<details>
<summary><h2>DS-2CD2H55FWD-IZS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.51 | Applied to: [DS-2CD2H55FWD-IZS(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/3e919f73-e198-45cf-aa44-a0652b9caf97.zip) | 2018-03-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/3e919f73-e198-45cf-aa44-a0652b9caf97.zip) |  |

</details>


<details>
<summary><h2>DS-2CD2H63G1-IZ - IPC_G1 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.6.821 | Applied to: [DS-2CD2H63G1-IZS(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.6.821_230831_S3000525150.zip) | 2023-08-31 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.6.821_230831_S3000525150.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202401/releasenote%5CNetwork_Camera-V5.6.821_Release_Note-IPC_G1_230831.pdf) |

</details>


<details>
<summary><h2>DS-2CD2H63G2-IZS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2H63G2-IZS(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2H63G2-LIZS2U - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2H63G2-LIZS2U(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2H66G2-IZS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2H66G2-IZS(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip)(C) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2H66G2H-IZS2UY - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2H66G2H-IZS2UY/SRB(2.8-12)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip)eFO-STD | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2H66G2H-IZSY - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2H66G2H-IZSY(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip)(eF) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2H66G2T-IZS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2H66G2T-IZS(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip)(C) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2H67G3-LIZS2UY - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD2H67G3-LIZS2UY/SL(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | 2025-12-10 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD2H67G3-LIZSY - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD2H67G3-LIZSY(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | 2025-12-10 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD2H83G1-IZ - IPC_G1 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.6.821 | Applied to: [DS-2CD2H83G1-IZ(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.6.821_230831_S3000525150.zip) | 2023-08-31 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.6.821_230831_S3000525150.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202401/releasenote%5CNetwork_Camera-V5.6.821_Release_Note-IPC_G1_230831.pdf) |

</details>


<details>
<summary><h2>DS-2CD2H83G2-IZS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2H83G2-IZS(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2H83G2-LIZS2U - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2H83G2-LIZS2U(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2H85FWD-IZS - IPC_G1 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.6.821 | Applied to: [DS-2CD2H85FWD-IZS(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.6.821_230831_S3000525150.zip) | 2023-08-31 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.6.821_230831_S3000525150.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202312/releasenote%5CNetwork_Camera_V5.6.6_Release_Note_--G1.pdf) |
| 5.6.6 | Applied to: [DS-2CD2H85FWD-IZS(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/f18aceb7-b896-4c7d-ad2e-8f0d2a91bcc3.zip) | 2021-06-25 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/f18aceb7-b896-4c7d-ad2e-8f0d2a91bcc3.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202312/releasenote%5CNetwork_Camera_V5.6.6_Release_Note_--G1.pdf) |

</details>


<details>
<summary><h2>DS-2CD2H86G2-IZS - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2H86G2-IZS(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202408/releasenote%5CNetwork_Camera-V5.5.820_Release_Note-G3.pdf) |
| 5.5.820 | Applied to: [DS-2CD2H86G2-IZS(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.820_260410_S3000715634.zip) | 2023-11-08 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.820_260410_S3000715634.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202408/releasenote%5CNetwork_Camera-V5.5.820_Release_Note-G3.pdf) |

</details>


<details>
<summary><h2>DS-2CD2H86G2H-IZS2UY - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2H86G2H-IZS2UY/SRB(2.8-12)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip)eFO-STD | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2H86G2H-IZSY - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2H86G2H-IZSY(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip)(eF) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2H86G2T-IZS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2H86G2T-IZS(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip)(C) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2H87G3-LIZS2UY - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.32 | Applied to: [DS-2CD2H87G3-LIZS2UY/SRB(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.32_260423_S3000719136.zip)/O-STD | 2026-03-30 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.32_260423_S3000719136.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202604/releasenote%5CNetwork_Camera-V5.8.32_SP1_260330_Release_Note-H13.pdf) |
| 5.8.30 | Applied to: [DS-2CD2H87G3-LIZS2UY/SRB(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip)/O-STD | 2025-12-10 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD2H87G3-LIZSY - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD2H87G3-LIZSY(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | 2025-12-10 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD2T123G2-2LI - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.2 | Applied to: [DS-2CD2T123G2-2LI2UY(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.23_260403_S3000712869.zip) | 2025-11-03 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.23_260403_S3000712869.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202511/releasenote%5CNetwork_Camera-V5.8.2_251103_Release_Note-IPCE_G9.pdf) |

</details>


<details>
<summary><h2>DS-2CD2T123G2-LIS2U - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.2 | Applied to: [DS-2CD2T123G2-LIS2UY/SL(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.23_260403_S3000712869.zip) | 2025-11-03 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.23_260403_S3000712869.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202511/releasenote%5CNetwork_Camera-V5.8.2_251103_Release_Note-IPCE_G9.pdf) |

</details>


<details>
<summary><h2>DS-2CD2T126G3-2I - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.2 | Applied to: [DS-2CD2T126G3-2IY(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.23_260403_S3000712869.zip)(eF) | 2025-11-03 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.23_260403_S3000712869.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202511/releasenote%5CNetwork_Camera-V5.8.2_251103_Release_Note-IPCE_G9.pdf) |

</details>


<details>
<summary><h2>DS-2CD2T126G3-IS2UY - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.3 | Applied to: [DS-2CD2T126G3-IS2UY/SL(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.3_260416_S3000716238.zip)(eF) | 2026-03-20 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.3_260416_S3000716238.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202604/releasenote%5CNetwork_Camera-V5.8.3_SP1_260320_Release_Note-IPCE_G9.pdf) |
| 5.8.2 | Applied to: [DS-2CD2T126G3-IS2UY/SRB(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.23_260403_S3000712869.zip)(eF)/O-STD | 2025-11-03 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.23_260403_S3000712869.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202511/releasenote%5CNetwork_Camera-V5.8.2_251103_Release_Note-IPCE_G9.pdf) |

</details>


<details>
<summary><h2>DS-2CD2T127G3P-LIS2UY - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.110 | Applied to: [DS-2CD2T127G3P-LIS2UY/SRB(180°)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.110_260421_S3000717992.zip) | 2026-04-21 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.110_260421_S3000717992.zip) |  |

</details>


<details>
<summary><h2>DS-2CD2T127G3P-LIS2UY-S-L--RB- - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.110 | [DS-2CD2T127G3P-LIS2UY-S-L--RB-](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.110_260421_S3000717992.zip) | 2026-04-21 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.110_260421_S3000717992.zip) |  |

</details>


<details>
<summary><h2>DS-2CD2T166G3-2I - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.3 | Applied to: [DS-2CD2T166G3-2I2UY(6mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.3_260416_S3000716238.zip)(eF) | 2026-03-20 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.3_260416_S3000716238.zip) |  |
| 5.8.2 | Applied to: [DS-2CD2T166G3-2IY(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.23_260403_S3000712869.zip)(eF) | 2025-11-03 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.23_260403_S3000712869.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202511/releasenote%5CNetwork_Camera-V5.8.2_251103_Release_Note-IPCE_G9.pdf) |

</details>


<details>
<summary><h2>DS-2CD2T166G3-IS2UY - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.3 | Applied to: [DS-2CD2T166G3-IS2UY/SRB(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.3_260416_S3000716238.zip)(eF)/O-STD | 2026-03-20 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.3_260416_S3000716238.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202604/releasenote%5CNetwork_Camera-V5.8.3_SP1_260320_Release_Note-IPCE_G9.pdf) |
| 5.8.2 | Applied to: [DS-2CD2T166G3-IS2UY/SRB(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.23_260403_S3000712869.zip)(eF)/O-STD | 2025-11-03 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.23_260403_S3000712869.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202511/releasenote%5CNetwork_Camera-V5.8.2_251103_Release_Note-IPCE_G9.pdf) |

</details>


<details>
<summary><h2>DS-2CD2T167G3P-LIS2UY - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.110 | Applied to: [DS-2CD2T167G3P-LIS2UY/SL(180°)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.110_260421_S3000717992.zip) | 2026-04-21 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.110_260421_S3000717992.zip) |  |

</details>


<details>
<summary><h2>DS-2CD2T167G3P-LIS2UY-S-L--RB- - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.110 | [DS-2CD2T167G3P-LIS2UY-S-L--RB-](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.110_260421_S3000717992.zip) | 2026-04-21 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.110_260421_S3000717992.zip) |  |

</details>


<details>
<summary><h2>DS-2CD2T21G0-I - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.800 | Applied to: [DS-2CD2T21G0-IS(4mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.800_211009_S3000390724.zip) | 2021-06-28 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.800_211009_S3000390724.zip) |  |

</details>


<details>
<summary><h2>DS-2CD2T23G0-I5 - IPC_G1 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.6.821 | Applied to: [DS-2CD2T23G0-I5(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.6.821_230831_S3000525150.zip) | 2023-08-31 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.6.821_230831_S3000525150.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202401/releasenote%5CNetwork_Camera-V5.6.821_Release_Note-IPC_G1_230831.pdf) |

</details>


<details>
<summary><h2>DS-2CD2T23G2-2I - IPC_G0 (3 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2T23G2-2I(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip)(D) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202507/releasenote%5CNetwork_Camera-V5.7.0_SP6_Release_Note-G6_I.pdf) |
| 5.7.0 | Applied to: [DS-2CD2T23G2-2I(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.0_240129_S3000555034.zip)(D) | 2024-10-23 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.0_240129_S3000555034.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202507/releasenote%5CNetwork_Camera-V5.7.0_SP6_Release_Note-G6_I.pdf) |
| 5.7.18 | Applied to: [DS-2CD2T23G2-2I(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.18_240826_S3000597013.zip)(D) | 2024-08-26 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.18_240826_S3000597013.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202507/releasenote%5CNetwork_Camera-V5.7.0_SP6_Release_Note-G6_I.pdf) |

</details>


<details>
<summary><h2>DS-2CD2T23G2-2LI - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2T23G2-2LI(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2T23G2-LIS2U - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2T23G2-LIS2U/SRB(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2T25FHWD-I5 - IPC_G1 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.6.821 | Applied to: [DS-2CD2T25FHWD-I8(4mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.6.821_230831_S3000525150.zip) | 2023-08-31 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.6.821_230831_S3000525150.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202401/releasenote%5CNetwork_Camera-V5.6.821_Release_Note-IPC_G1_230831.pdf) |

</details>


<details>
<summary><h2>DS-2CD2T25FWD-I5 - IPC_G1 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.6.821 | Applied to: [DS-2CD2T25FWD-I8(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.6.821_230831_S3000525150.zip) | 2023-08-31 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.6.821_230831_S3000525150.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202401/releasenote%5CNetwork_Camera-V5.6.821_Release_Note-IPC_G1_230831.pdf) |

</details>


<details>
<summary><h2>DS-2CD2T26G1-2I - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.6.0 | Applied to: [DS-2CD2T26G1-4I(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/18db80e0-2712-4496-8bd3-646f5014a59b.zip) | 2019-05-07 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/18db80e0-2712-4496-8bd3-646f5014a59b.zip) |  |

</details>


<details>
<summary><h2>DS-2CD2T26G1-4I - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.6.0 | Applied to: [DS-2CD2T26G1-4I/SL(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/18db80e0-2712-4496-8bd3-646f5014a59b.zip) | 2019-05-07 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/18db80e0-2712-4496-8bd3-646f5014a59b.zip) |  |

</details>


<details>
<summary><h2>DS-2CD2T26G2-2I - IPC_G0 (4 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2T26G2-4I(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202408/releasenote%5CNetwork_Camera-V5.5.820_Release_Note-G3.pdf) |
| 5.7.0 | Applied to: [DS-2CD2T26G2-4I(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.0_240129_S3000555034.zip) | 2024-10-23 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.0_240129_S3000555034.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202408/releasenote%5CNetwork_Camera-V5.5.820_Release_Note-G3.pdf) |
| 5.5.820 | Applied to: [DS-2CD2T26G2-4I(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.820_260410_S3000715634.zip) | 2023-11-08 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.820_260410_S3000715634.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202408/releasenote%5CNetwork_Camera-V5.5.820_Release_Note-G3.pdf) |
| 5.5.800 | Applied to: [DS-2CD2T26G2-4I(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.800_211009_S3000390724.zip) | 2021-10-09 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.800_211009_S3000390724.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202408/releasenote%5CNetwork_Camera-V5.5.820_Release_Note-G3.pdf) |

</details>


<details>
<summary><h2>DS-2CD2T26G2-ISU - IPC_G0 (4 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2T26G2-ISU/SL(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/330c4c2c-5730-4877-a942-0be87cea67ca.pdf) |
| 5.7.0 | Applied to: [DS-2CD2T26G2-ISU/SL(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.0_240129_S3000555034.zip) | 2024-10-23 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.0_240129_S3000555034.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/330c4c2c-5730-4877-a942-0be87cea67ca.pdf) |
| 5.5.820 | Applied to: [DS-2CD2T26G2-ISU/SL(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.820_260410_S3000715634.zip) | 2023-11-08 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.820_260410_S3000715634.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/330c4c2c-5730-4877-a942-0be87cea67ca.pdf) |
| 5.5.800 | Applied to: [DS-2CD2T26G2-ISU/SL(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.800_211009_S3000390724.zip) | 2021-10-09 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.800_211009_S3000390724.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/330c4c2c-5730-4877-a942-0be87cea67ca.pdf) |

</details>


<details>
<summary><h2>DS-2CD2T27G2-L - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.820 | Applied to: [DS-2CD2T27G2-L(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.820_260410_S3000715634.zip) | 2023-11-08 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.820_260410_S3000715634.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202408/releasenote%5CNetwork_Camera-V5.5.820_Release_Note-G3.pdf) |
| 5.5.800 | Applied to: [DS-2CD2T27G2-L(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.800_211009_S3000390724.zip) | 2021-10-09 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.800_211009_S3000390724.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202408/releasenote%5CNetwork_Camera-V5.5.820_Release_Note-G3.pdf) |

</details>


<details>
<summary><h2>DS-2CD2T43G0-I5 - IPC_G1 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.6.821 | Applied to: [DS-2CD2T43G0-I5(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.6.821_230831_S3000525150.zip) | 2023-08-31 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.6.821_230831_S3000525150.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202401/releasenote%5CNetwork_Camera-V5.6.821_Release_Note-IPC_G1_230831.pdf) |

</details>


<details>
<summary><h2>DS-2CD2T43G2-2I - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2T43G2-2I(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2T43G2-2LI - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2T43G2-2LI(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2T43G2-2LIZ - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD2T43G2-4LIZY(2.8/4mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | 2025-12-10 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13U.pdf) |

</details>


<details>
<summary><h2>DS-2CD2T43G2-LIS2U - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2T43G2-LIS2U/SL(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2T43G2-LIZS2UY - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD2T43G2-LIZS2UY/SL(2.8/4mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | 2025-12-10 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13U.pdf) |

</details>


<details>
<summary><h2>DS-2CD2T43G2P-LISU - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.12 | Applied to: [DS-2CD2T43G2P-LISU/SL(180°)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.12_260416_S3000716519.zip) | 2026-04-16 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.12_260416_S3000716519.zip) |  |
| 5.8.11 | Applied to: [DS-2CD2T43G2P-LISU/SL(180°)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.110_260421_S3000717992.zip) | 2025-10-29 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.110_260421_S3000717992.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.8.11_SP1_251029_Release_Note-IPCE_P_E11.pdf) |

</details>


<details>
<summary><h2>DS-2CD2T43G2P-LISU-S-L--RB- - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.12 | [DS-2CD2T43G2P-LISU-S-L--RB-](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.12_260416_S3000716513.zip) | 2026-04-16 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.12_260416_S3000716513.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202605/releasenote%5CNetwork_Camera-V5.8.12_260416_Release_IPCE_P_E11.pdf) |

</details>


<details>
<summary><h2>DS-2CD2T45FWD-I5 - IPC_G1 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.6.821 | Applied to: [DS-2CD2T45FWD-I8(4mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.6.821_230831_S3000525150.zip)(BLACK) | 2023-08-31 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.6.821_230831_S3000525150.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202401/releasenote%5CNetwork_Camera-V5.6.821_Release_Note-IPC_G1_230831.pdf) |

</details>


<details>
<summary><h2>DS-2CD2T45G0P-I - IPC_G1 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.6.821 | Applied to: [DS-2CD2T45G0P-I(1.68mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.6.821_230831_S3000525150.zip) | 2023-08-31 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.6.821_230831_S3000525150.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202401/releasenote%5CNetwork_Camera-V5.6.821_Release_Note-IPC_G1_230831.pdf) |

</details>


<details>
<summary><h2>DS-2CD2T46G1-4I - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.6.0 | Applied to: [DS-2CD2T46G1-4I/SL(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/18db80e0-2712-4496-8bd3-646f5014a59b.zip) | 2019-05-07 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/18db80e0-2712-4496-8bd3-646f5014a59b.zip) |  |

</details>


<details>
<summary><h2>DS-2CD2T46G2-2I - IPC_G0 (3 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2T46G2-2I(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip)(C) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |
| 5.5.820 | Applied to: [DS-2CD2T46G2-2I(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.820_260410_S3000715634.zip) | 2023-11-08 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.820_260410_S3000715634.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/330c4c2c-5730-4877-a942-0be87cea67ca.pdf) |
| 5.5.800 | Applied to: [DS-2CD2T46G2-2I(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.800_211009_S3000390724.zip) | 2021-10-09 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.800_211009_S3000390724.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/330c4c2c-5730-4877-a942-0be87cea67ca.pdf) |

</details>


<details>
<summary><h2>DS-2CD2T46G2-ISU - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.820 | Applied to: [DS-2CD2T46G2-ISU/SL(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.820_260410_S3000715634.zip) | 2023-11-08 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.820_260410_S3000715634.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/330c4c2c-5730-4877-a942-0be87cea67ca.pdf) |
| 5.5.800 | Applied to: [DS-2CD2T46G2-ISU/SL(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.800_211009_S3000390724.zip) | 2021-10-09 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.800_211009_S3000390724.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/330c4c2c-5730-4877-a942-0be87cea67ca.pdf) |

</details>


<details>
<summary><h2>DS-2CD2T46G2H-2I - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2T46G2H-4I(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip)(eF) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2T46G2H-IS2U - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2T46G2H-IS2U/SL(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip)(eF) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2T46G2P-ISU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.20 | Applied to: [DS-2CD2T46G2P-ISU/SL(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.20_230630_S3000509422.zip)(C) | 2025-11-25 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.20_230630_S3000509422.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.20_251125_Release_Note-IPCE_P_G5.pdf) |

</details>


<details>
<summary><h2>DS-2CD2T46G3-2IZY - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD2T46G3-4IZY(2.8/4mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | 2025-12-10 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13U.pdf) |

</details>


<details>
<summary><h2>DS-2CD2T46G3-IZS2UY - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.32 | Applied to: [DS-2CD2T46G3-IZS2UY/SRB(2.8/4)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.32_260423_S3000719136.zip)O-STDBLACK | 2026-03-30 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.32_260423_S3000719136.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202604/releasenote%5CNetwork_Camera-V5.8.32_SP1_260330_Release_Note-H13U.pdf) |
| 5.8.30 | Applied to: [DS-2CD2T46G3-IZS2UY/SRB(2.8/4)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip)O-STDBLACK | 2025-12-10 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13U.pdf) |

</details>


<details>
<summary><h2>DS-2CD2T47G2-L - IPC_G0 (3 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2T47G2-L(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202408/releasenote%5CNetwork_Camera-V5.5.820_Release_Note-G3.pdf) |
| 5.5.820 | Applied to: [DS-2CD2T47G2-L(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.820_260410_S3000715634.zip) | 2023-11-08 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.820_260410_S3000715634.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202408/releasenote%5CNetwork_Camera-V5.5.820_Release_Note-G3.pdf) |
| 5.5.800 | Applied to: [DS-2CD2T47G2-L(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.800_211009_S3000390724.zip) | 2021-10-09 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.800_211009_S3000390724.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202408/releasenote%5CNetwork_Camera-V5.5.820_Release_Note-G3.pdf) |

</details>


<details>
<summary><h2>DS-2CD2T47G2-LSU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2T47G2-LSU/SL(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip)(C) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2T47G2H-LI - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2T47G2H-LI(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip)(eF) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2T47G2H-LISU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2T47G2H-LISU/SL(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip)(eF) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2T47G3-LIS2UY - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.32 | Applied to: [DS-2CD2T47G3-LIS2UY/SRB(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.32_260423_S3000719136.zip) | 2026-03-30 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.32_260423_S3000719136.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202604/releasenote%5CNetwork_Camera-V5.8.32_SP1_260330_Release_Note-H13U.pdf) |
| 5.8.30 | Applied to: [DS-2CD2T47G3-LIS2UY/SRB(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | 2025-12-10 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13U.pdf) |

</details>


<details>
<summary><h2>DS-2CD2T47G3-LIY - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.32 | Applied to: [DS-2CD2T47G3-LIY(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.32_260423_S3000719136.zip) | 2026-03-30 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.32_260423_S3000719136.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202604/releasenote%5CNetwork_Camera-V5.8.32_SP1_260330_Release_Note-H13U.pdf) |
| 5.8.30 | Applied to: [DS-2CD2T47G3-LIY(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | 2025-12-10 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13U.pdf) |

</details>


<details>
<summary><h2>DS-2CD2T47G3P-LIS2UY - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.100 | Applied to: [DS-2CD2T47G3P-LIS2UY/SL(180°)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.100_260416_S3000716492.zip) | 2026-03-25 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.100_260416_S3000716492.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202604/releasenote%5CNetwork_Camera-V5.8.100_260325_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2T63G0-I5 - IPC_G1 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.6.821 | Applied to: [DS-2CD2T63G0-I8(4mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.6.821_230831_S3000525150.zip) | 2023-08-31 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.6.821_230831_S3000525150.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202401/releasenote%5CNetwork_Camera-V5.6.821_Release_Note-IPC_G1_230831.pdf) |

</details>


<details>
<summary><h2>DS-2CD2T63G2-2I - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2T63G2-4I(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2T63G2-2LI - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2T63G2-2LI(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2T63G2-LIS2U - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2T63G2-LIS2U/SL(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2T63G2P-LISU - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.12 | Applied to: [DS-2CD2T63G2P-LISU/SL(180°)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.12_260416_S3000716519.zip) | 2026-04-16 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.12_260416_S3000716519.zip) |  |
| 5.8.11 | Applied to: [DS-2CD2T63G2P-LISU/SL(180°)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.110_260421_S3000717992.zip) | 2025-10-29 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.110_260421_S3000717992.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.8.11_SP1_251029_Release_Note-IPCE_P_E11.pdf) |

</details>


<details>
<summary><h2>DS-2CD2T63G2P-LISU-S-L--RB- - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.12 | [DS-2CD2T63G2P-LISU-S-L--RB-](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.12_260416_S3000716513.zip) | 2026-04-16 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.12_260416_S3000716513.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202605/releasenote%5CNetwork_Camera-V5.8.12_260416_Release_IPCE_P_E11.pdf) |

</details>


<details>
<summary><h2>DS-2CD2T65G1-I5 - IPC_G1 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.6.821 | Applied to: [DS-2CD2T65G1-I5(4mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.6.821_230831_S3000525150.zip)(BLACK) | 2023-08-31 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.6.821_230831_S3000525150.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202401/releasenote%5CNetwork_Camera-V5.6.821_Release_Note-IPC_G1_230831.pdf) |

</details>


<details>
<summary><h2>DS-2CD2T66G2-2I - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2T66G2-4I(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip)(C) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2T66G2-ISU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2T66G2-ISU/SL(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip)(C) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2T66G2H-2I - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2T66G2H-2I(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip)(eF) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2T66G2H-IS2U - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2T66G2H-IS2U/SL(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip)eFO-STDBLACK | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2T66G2P-ISU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.20 | Applied to: [DS-2CD2T66G2P-ISU/SL(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.20_230630_S3000509422.zip)(C) | 2025-11-25 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.20_230630_S3000509422.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.20_251125_Release_Note-IPCE_P_G5.pdf) |

</details>


<details>
<summary><h2>DS-2CD2T67G2-L - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2T67G2-L(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip)(C) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2T67G2H-LI - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2T67G2H-LI(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip)(eF) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2T67G2H-LISU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2T67G2H-LISU/SL(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip)(eF) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2T67G2P-LSU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.20 | Applied to: [DS-2CD2T67G2P-LSU/SL(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.20_230630_S3000509422.zip)(C) | 2025-11-25 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.20_230630_S3000509422.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.20_251125_Release_Note-IPCE_P_G5.pdf) |

</details>


<details>
<summary><h2>DS-2CD2T67G3-LIS2UY - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD2T67G3-LIS2UY/SL(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | 2025-12-10 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD2T67G3-LIY - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD2T67G3-LIY(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | 2025-12-10 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD2T67G3P-LIS2UY - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.100 | Applied to: [DS-2CD2T67G3P-LIS2UY/SL(180°)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.100_260416_S3000716492.zip) | 2026-03-25 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.100_260416_S3000716492.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202604/releasenote%5CNetwork_Camera-V5.8.100_260325_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2T83G0-I5 - IPC_G1 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.6.821 | Applied to: [DS-2CD2T83G0-I5(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.6.821_230831_S3000525150.zip) | 2023-08-31 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.6.821_230831_S3000525150.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202401/releasenote%5CNetwork_Camera-V5.6.821_Release_Note-IPC_G1_230831.pdf) |

</details>


<details>
<summary><h2>DS-2CD2T83G2-2I - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.6 | Applied to: [DS-2CD2T83G2-2I(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.6_260128_S3000701683.zip)(D) | 2026-01-28 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.6_260128_S3000701683.zip) |  |
| 5.7.23 | Applied to: [DS-2CD2T83G2-4I(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2T83G2-2LI - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.6 | Applied to: [DS-2CD2T83G2-2LI2U(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.6_260128_S3000701683.zip)(T) | 2026-01-28 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.6_260128_S3000701683.zip) |  |
| 5.7.23 | Applied to: [DS-2CD2T83G2-2LI2U(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2T83G2-LIS2U - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2T83G2-LIS2U/SL(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2T83G2P-LISU - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.12 | Applied to: [DS-2CD2T83G2P-LISU/SL(180°)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.12_260416_S3000716519.zip) | 2026-04-16 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.12_260416_S3000716519.zip) |  |
| 5.8.11 | Applied to: [DS-2CD2T83G2P-LISU/SL(180°)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.110_260421_S3000717992.zip) | 2025-10-29 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.110_260421_S3000717992.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.8.11_SP1_251029_Release_Note-IPCE_P_E11.pdf) |

</details>


<details>
<summary><h2>DS-2CD2T83G2P-LISU-S-L--RB- - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.12 | [DS-2CD2T83G2P-LISU-S-L--RB-](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.12_260416_S3000716513.zip) | 2026-04-16 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.12_260416_S3000716513.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202605/releasenote%5CNetwork_Camera-V5.8.12_260416_Release_IPCE_P_E11.pdf) |

</details>


<details>
<summary><h2>DS-2CD2T85G1-I5 - IPC_G1 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.6.821 | Applied to: [DS-2CD2T85G1-I5(4mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.6.821_230831_S3000525150.zip)(BLACK) | 2023-08-31 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.6.821_230831_S3000525150.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202401/releasenote%5CNetwork_Camera-V5.6.821_Release_Note-IPC_G1_230831.pdf) |

</details>


<details>
<summary><h2>DS-2CD2T86G2-2I - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2T86G2-2I(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip)(C)(BLACK) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2T86G2-4IY - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2T86G2-4IY(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip)(C) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2T86G2-ISU - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2T86G2-ISU/SL(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip)(C) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |
| 5.5.820 | Applied to: [DS-2CD2T86G2-ISU/SL(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.820_260410_S3000715634.zip) | 2023-11-08 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.820_260410_S3000715634.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202408/releasenote%5CNetwork_Camera-V5.5.820_Release_Note-G3.pdf) |

</details>


<details>
<summary><h2>DS-2CD2T86G2H-2I - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2T86G2H-2I(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip)(eF) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2T86G2H-IS2U - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2T86G2H-IS2U/SRB(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip)(eF) | 2026-03-20 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2T87G2-L - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2T87G2-L(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip)(C)(BLACK) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2T87G2-LSU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2T87G2-LSU/SL(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip)(C) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2T87G2H-LI - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2T87G2H-LI(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip)(eF) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2T87G2H-LISU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2T87G2H-LISU/SL(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip)(eF) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2T87G2P-LSU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.20 | Applied to: [DS-2CD2T87G2P-LSU/SL(4mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.20_230630_S3000509422.zip)(C)/O-STD/BLACK | 2025-11-25 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.20_230630_S3000509422.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.20_251125_Release_Note-IPCE_P_G5.pdf) |

</details>


<details>
<summary><h2>DS-2CD2T87G3-LIS2UY - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.32 | Applied to: [DS-2CD2T87G3-LIS2UY/SRB(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.32_260423_S3000719136.zip) | 2026-03-30 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.32_260423_S3000719136.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202604/releasenote%5CNetwork_Camera-V5.8.32_SP1_260330_Release_Note-H13.pdf) |
| 5.8.30 | Applied to: [DS-2CD2T87G3-LIS2UY/SL(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip)O-STD/BLACK | 2025-12-10 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD2T87G3-LIY - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.32 | Applied to: [DS-2CD2T87G3-LIY(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.32_260423_S3000719136.zip)(BLACK) | 2026-03-30 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.32_260423_S3000719136.zip) |  |
| 5.8.30 | Applied to: [DS-2CD2T87G3-LIY(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | 2025-12-10 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD2T87G3P-LIS2UY - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.110 | Applied to: [DS-2CD2T87G3P-LIS2UY/SRB(180°)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.110_260421_S3000717992.zip) | 2026-04-21 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.110_260421_S3000717992.zip) |  |

</details>


<details>
<summary><h2>DS-2CD2T87G3P-LIS2UY-S-L--RB- - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.110 | [DS-2CD2T87G3P-LIS2UY-S-L--RB-](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.110_260421_S3000717992.zip) | 2026-04-21 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.110_260421_S3000717992.zip) |  |

</details>


<details>
<summary><h2>DS-2CD30167G3-LIU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.2 | Applied to: [DS-2CD30167G3-LIUY(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.23_260403_S3000712869.zip) | 2025-11-03 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.23_260403_S3000712869.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202511/releasenote%5CNetwork_Camera-V5.8.2_251103_Release_Note-IPCE_H_G9.pdf) |

</details>


<details>
<summary><h2>DS-2CD3023G2-IU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD3023G2-IU(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip)(B) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD3023G2-LIU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD3023G2-LIU(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD3027G2-LS - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.820 | Applied to: [DS-2CD3027G2-LS(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.820_260410_S3000715634.zip) | 2023-11-08 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.820_260410_S3000715634.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202403/releasenote%5CNetwork_Camera-V5.5.820_Release_Note-G3.pdf) |
| 5.5.800 | Applied to: [DS-2CD3027G2-LS(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.800_211009_S3000390724.zip) | 2021-10-09 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.800_211009_S3000390724.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202403/releasenote%5CNetwork_Camera-V5.5.820_Release_Note-G3.pdf) |

</details>


<details>
<summary><h2>DS-2CD3043G2-IU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD3043G2-IU(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip)(B) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD3043G2-LIU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD3043G2-LIU(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD3046G2-IS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.55 | Applied to: [DS-2CD3046G2-IS(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.55_241108_S3000612871.zip)(H) | 2024-11-08 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.55_241108_S3000612871.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.55_SP3_241108_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD3046G2-IU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.55 | Applied to: [DS-2CD3046G2-IU/SL(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.55_241108_S3000612871.zip)(H) | 2024-11-08 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.55_241108_S3000612871.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.55_SP3_241108_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD3046G2H-LI - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.55 | Applied to: [DS-2CD3046G2H-LI(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.55_241108_S3000612871.zip) | 2024-11-08 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.55_241108_S3000612871.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.55_SP3_241108_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD3046G3-IU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD3046G3-IUY(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | 2025-12-10 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD3046G3-LIU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD3046G3-LIU(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip)(eF) | 2025-12-10 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD3047G2-LS - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.820 | Applied to: [DS-2CD3047G2-LS(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.820_260410_S3000715634.zip) | 2023-11-08 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.820_260410_S3000715634.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202403/releasenote%5CNetwork_Camera-V5.5.820_Release_Note-G3.pdf) |
| 5.5.800 | Applied to: [DS-2CD3047G2-LS(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.800_211009_S3000390724.zip) | 2021-10-09 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.800_211009_S3000390724.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202403/releasenote%5CNetwork_Camera-V5.5.820_Release_Note-G3.pdf) |

</details>


<details>
<summary><h2>DS-2CD3047G3-LIU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD3047G3-LIUY(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | 2025-12-10 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD3063G2-IU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD3063G2-IU(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD3063G2-LIU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD3063G2-LIU(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD3066G2-IS - IPC_G0 (3 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.2 | Applied to: [DS-2CD3066G2-IS(6mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.23_260403_S3000712869.zip)(H)(eF) | 2025-12-24 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.23_260403_S3000712869.zip) |  |
| 5.7.55 | Applied to: [DS-2CD3066G2-IS(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.55_241108_S3000612871.zip)(H) | 2024-11-08 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.55_241108_S3000612871.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.55_SP3_241108_Release_Note.pdf) |
| 5.7.51 | Applied to: [DS-2CD3066G2-IS(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.51_240320_S3000563201.zip)(H) | 2023-08-29 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.51_240320_S3000563201.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.55_SP3_241108_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD3066G2H-LI - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.55 | Applied to: [DS-2CD3066G2H-LIU(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.55_241108_S3000612871.zip)(eF) | 2024-11-08 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.55_241108_S3000612871.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.55_SP3_241108_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD3066G3-IU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD3066G3-IUY(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | 2025-12-10 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD3066G3-LIU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD3066G3-LIUY(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip)(eF) | 2025-12-10 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD3067G3-LIU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD3067G3-LIU(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | 2025-12-10 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD3083G2-LIU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD3083G2-LIU(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD3086G2H-LI - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.55 | Applied to: [DS-2CD3086G2H-LIU(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.55_241108_S3000612871.zip)(eF) | 2024-11-08 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.55_241108_S3000612871.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.55_SP3_241108_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD3086G3-IU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD3086G3-IUY(4mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | 2025-12-10 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD3086G3-LIU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD3086G3-LIU(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip)(eF) | 2025-12-10 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD3087G3-LIU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD3087G3-LIU(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | 2025-12-10 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD30C7G3-LIU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.2 | Applied to: [DS-2CD30C7G3-LIUY(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.23_260403_S3000712869.zip)(BLACK) | 2025-11-03 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.23_260403_S3000712869.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202511/releasenote%5CNetwork_Camera-V5.8.2_251103_Release_Note-IPCE_H_G9.pdf) |

</details>


<details>
<summary><h2>DS-2CD3121G2E-LIU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.10 | Applied to: [DS-2CD3121G2E-LIU(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.100_260416_S3000716492.zip) | 2024-12-05 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.100_260416_S3000716492.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202507/releasenote%5CNetwork_Camera-V5.8.10_SP2_Release_Note-E9.pdf) |

</details>


<details>
<summary><h2>DS-2CD3123G2-I - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD3123G2-ISU(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip)(B) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD3123G2-LISU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD3123G2-LISU(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD3125G0-IMS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.6.820 | Applied to: [DS-2CD3125G0-IMS(4mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.6.820_220519_S3000430633.zip) | 2022-05-19 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.6.820_220519_S3000430633.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202301/Network%20Camera%20V5.6.820%20Release%20Note%20--G1.pdf) |

</details>


<details>
<summary><h2>DS-2CD3143G2-LISU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD3143G2-LISU(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD3143G2-LISUY - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD3143G2-LIY(PTRZ)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip)(2.8/4mm) | 2025-12-10 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13U.pdf) |

</details>


<details>
<summary><h2>DS-2CD3146G2-IMS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.55 | Applied to: [DS-2CD3146G2-IMS(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.55_241108_S3000612871.zip) | 2024-11-08 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.55_241108_S3000612871.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.55_SP3_241108_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD3146G2-IS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.55 | Applied to: [DS-2CD3146G2-IS(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.55_241108_S3000612871.zip)(H) | 2024-11-08 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.55_241108_S3000612871.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.55_SP3_241108_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD3146G2H-LIS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.55 | Applied to: [DS-2CD3146G2H-LIS(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.55_241108_S3000612871.zip) | 2024-11-08 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.55_241108_S3000612871.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.55_SP3_241108_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD3146G3-ISU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD3146G3-ISUY(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | 2025-12-10 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD3146G3-LISU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD3146G3-LISUY(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip)(eF) | 2025-12-10 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD3146G3-SU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD3146G3-SU(2mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | 2025-12-10 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD3147G3-LISU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD3147G3-LISU(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | 2025-12-10 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD3163G2-I - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD3163G2-ISU(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip)(B) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD3163G2-LISU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD3163G2-LISU(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD3166G2-IS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.55 | Applied to: [DS-2CD3166G2-IS(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.55_241108_S3000612871.zip)(H) | 2024-11-08 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.55_241108_S3000612871.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.55_SP3_241108_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD3166G2H-LIS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.55 | Applied to: [DS-2CD3166G2H-LISU(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.55_241108_S3000612871.zip)(eF) | 2024-11-08 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.55_241108_S3000612871.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.55_SP3_241108_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD3166G3-ISU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD3166G3-ISUY(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | 2025-12-10 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD3166G3-LISU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD3166G3-LISUY(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip)(eF) | 2025-12-10 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD3167G3-LISU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD3167G3-LISU(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | 2025-12-10 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD3183G2-LISU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD3183G2-LISU(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD3185G0-IMS - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.6.6 | Applied to: [DS-2CD3185G0-IMS(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/f18aceb7-b896-4c7d-ad2e-8f0d2a91bcc3.zip) | 2021-06-25 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/f18aceb7-b896-4c7d-ad2e-8f0d2a91bcc3.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202312/releasenote%5C%E3%80%90Release_Note%E3%80%91Mobile_IPC_V5.6.2_190701.pdf) |
| 5.6.2 | Applied to: [DS-2CD3185G0-IMS(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/f88f5389-fd05-44ea-9adc-874910511d97.zip) | 2019-07-01 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/f88f5389-fd05-44ea-9adc-874910511d97.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202312/releasenote%5C%E3%80%90Release_Note%E3%80%91Mobile_IPC_V5.6.2_190701.pdf) |

</details>


<details>
<summary><h2>DS-2CD3186G2-IMS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.55 | Applied to: [DS-2CD3186G2-IMS(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.55_241108_S3000612871.zip) | 2024-11-08 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.55_241108_S3000612871.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.55_SP3_241108_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD3186G2-IS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.55 | Applied to: [DS-2CD3186G2-IS(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.55_241108_S3000612871.zip)(H) | 2024-11-08 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.55_241108_S3000612871.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.55_SP3_241108_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD3186G3-ISU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD3186G3-ISUY(4mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | 2025-12-10 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD3186G3-LISU - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD3186G3-LISUY(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip)(eF) | 2025-12-10 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |
| 5.8.11 | Applied to: [DS-2CD3186G3-LISUY(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.110_260421_S3000717992.zip)(eF) | 2025-10-22 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.110_260421_S3000717992.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD3187G3-LISU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD3187G3-LISU(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | 2025-12-10 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD33167G3-LISU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.2 | Applied to: [DS-2CD33167G3-LISUY(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.23_260403_S3000712869.zip) | 2025-11-03 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.23_260403_S3000712869.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202511/releasenote%5CNetwork_Camera-V5.8.2_251103_Release_Note-IPCE_H_G9.pdf) |

</details>


<details>
<summary><h2>DS-2CD3323G2-IU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD3323G2-IU(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD3323G2-LISU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD3323G2-LISU(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD3323G2-LIU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD3323G2-LIU/SL(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD3327G2-LS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.820 | Applied to: [DS-2CD3327G2-LSU(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.820_260410_S3000715634.zip) | 2023-11-08 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.820_260410_S3000715634.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202403/releasenote%5CNetwork_Camera-V5.5.820_Release_Note-G3.pdf) |

</details>


<details>
<summary><h2>DS-2CD3343G2 - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.11 | Applied to: [DS-2CD3343G2/X2-LIZSUY/SL(2.8/4mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.110_260421_S3000717992.zip)O-STD | 2025-12-16 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.110_260421_S3000717992.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.8.11_251216_Release_Note-IPCE_D_H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD3343G2-IU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD3343G2-IU(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD3343G2-LISU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD3343G2-LISU(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD3343G2-LIU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD3343G2-LIU/SL(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD3346G2-IS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.55 | Applied to: [DS-2CD3346G2-ISU(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.55_241108_S3000612871.zip)(H) | 2024-11-08 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.55_241108_S3000612871.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.55_SP3_241108_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD3346G2H-LIS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.55 | Applied to: [DS-2CD3346G2H-LIS(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.55_241108_S3000612871.zip) | 2024-11-08 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.55_241108_S3000612871.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.55_SP3_241108_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD3346G2H-LISU - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.2 | Applied to: [DS-2CD3346G2H-LISU/SL(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.23_260403_S3000712869.zip) | 2025-12-24 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.23_260403_S3000712869.zip) |  |
| 5.7.55 | Applied to: [DS-2CD3346G2H-LISU/SL(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.55_241108_S3000612871.zip) | 2024-11-08 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.55_241108_S3000612871.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.55_SP3_241108_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD3346G3-ISU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD3346G3-ISUY(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | 2025-12-10 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD3346G3-LISU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD3346G3-LISUY(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip)(eF) | 2025-12-10 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD3347G2-LS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.820 | Applied to: [DS-2CD3347G2-LSU(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.820_260410_S3000715634.zip) | 2023-11-08 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.820_260410_S3000715634.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202403/releasenote%5CNetwork_Camera-V5.5.820_Release_Note-G3.pdf) |

</details>


<details>
<summary><h2>DS-2CD3347G3-LISU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD3347G3-LISU(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | 2025-12-10 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD3363G2-IU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD3363G2-IU(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD3363G2-LISU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD3363G2-LISU(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD3363G2-LIU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD3363G2-LIU/SL(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD3366G2H-LIS - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.2 | Applied to: [DS-2CD3366G2H-LISU(4mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.23_260403_S3000712869.zip) | 2025-12-24 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.23_260403_S3000712869.zip) |  |
| 5.7.55 | Applied to: [DS-2CD3366G2H-LISU(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.55_241108_S3000612871.zip) | 2024-11-08 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.55_241108_S3000612871.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.55_SP3_241108_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD3366G3-ISU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD3366G3-ISUY(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | 2025-12-10 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD3366G3-LISU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD3366G3-LISUY(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip)(eF) | 2025-12-10 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD3367G3-LISU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD3367G3-LISUY(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | 2025-12-10 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD3383G2-LISU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD3383G2-LISU(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD3383G2-LIU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD3383G2-LIU/SL(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD3386G2-IS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.55 | Applied to: [DS-2CD3386G2-ISU(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.55_241108_S3000612871.zip)(H) | 2024-11-08 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.55_241108_S3000612871.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.55_SP3_241108_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD3386G2H-LIS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.55 | Applied to: [DS-2CD3386G2H-LISU(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.55_241108_S3000612871.zip) | 2024-11-08 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.55_241108_S3000612871.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.55_SP3_241108_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD3386G3-ISU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD3386G3-ISUY(4mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | 2025-12-10 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD3386G3-LISU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD3386G3-LISUY(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip)(eF) | 2025-12-10 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD3387G3-LISU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD3387G3-LISU(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | 2025-12-10 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD33C7G3-LISU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.2 | Applied to: [DS-2CD33C7G3-LISUY(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.23_260403_S3000712869.zip) | 2025-11-03 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.23_260403_S3000712869.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202511/releasenote%5CNetwork_Camera-V5.8.2_251103_Release_Note-IPCE_H_G9.pdf) |

</details>


<details>
<summary><h2>DS-2CD3523G2-IS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD3523G2-IS(4mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD3523G2-LIS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD3523G2-LIS(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD3543G2-IS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD3543G2-IS(4mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD3543G2-LIS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD3543G2-LIS(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD3546G2-IS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.55 | Applied to: [DS-2CD3546G2-IS(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.55_241108_S3000612871.zip)(H) | 2024-11-08 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.55_241108_S3000612871.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.55_SP3_241108_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD3546G3-IS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD3546G3-ISY(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | 2025-12-10 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD3563G2-IS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD3563G2-IS(4mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD3563G2-LIS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD3563G2-LIS(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD3566G2-IS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.55 | Applied to: [DS-2CD3566G2-IS(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.55_241108_S3000612871.zip)(H) | 2024-11-08 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.55_241108_S3000612871.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.55_SP3_241108_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD3566G3-IS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD3566G3-ISY(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | 2025-12-10 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD3583G2-LIS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD3583G2-LIS(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD3586G2-IS - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.19 | Applied to: [DS-2CD3586G2-IS(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.19_241207_S3000618493.zip)(H) | 2024-12-07 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.19_241207_S3000618493.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.55_SP3_241108_Release_Note.pdf) |
| 5.7.55 | Applied to: [DS-2CD3586G2-IS(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.55_241108_S3000612871.zip)(H) | 2024-11-08 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.55_241108_S3000612871.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.55_SP3_241108_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD3586G3-IS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD3586G3-ISY(4mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | 2025-12-10 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD36167G3-LIZSU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.2 | Applied to: [DS-2CD36167G3-LIZSUY/SL(2.7-13.5mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.23_260403_S3000712869.zip)O-STD | 2025-11-03 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.23_260403_S3000712869.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202511/releasenote%5CNetwork_Camera-V5.8.2_251103_Release_Note-IPCE_H_G9.pdf) |

</details>


<details>
<summary><h2>DS-2CD36167G3T-LIZSU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.2 | Applied to: [DS-2CD36167G3T-LIZSUY(2.7-13.5mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.23_260403_S3000712869.zip) | 2025-11-03 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.23_260403_S3000712869.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202511/releasenote%5CNetwork_Camera-V5.8.2_251103_Release_Note-IPCE_H_G9.pdf) |

</details>


<details>
<summary><h2>DS-2CD3621G2-LIZS - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.10 | Applied to: [DS-2CD3621G2-LIZS(2.7-13.5mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.100_260416_S3000716492.zip) | 2025-07-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.100_260416_S3000716492.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202508/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-E10.pdf) |
| 5.7.12 | Applied to: [DS-2CD3621G2-LIZS(2.7-13.5mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.12_220907_S3000453567.zip) | 2023-06-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.12_220907_S3000453567.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202508/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-E10.pdf) |

</details>


<details>
<summary><h2>DS-2CD3623G2-IZS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD3623G2-IZS(2.7-13.5mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD3623G2-LIZSU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD3623G2-LIZSU(2.7-13.5mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD3643G2-IZS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD3643G2-IZS(2.7-13.5mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD3643G2-LIZSU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD3643G2-LIZSU(2.7-13.5mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD3646G2-IZS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.55 | Applied to: [DS-2CD3646G2-IZS(2.7-13.5mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.55_241108_S3000612871.zip)(H) | 2024-11-08 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.55_241108_S3000612871.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.55_SP3_241108_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD3646G2HT-LIZS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.55 | Applied to: [DS-2CD3646G2HT-LIZS(2.7-13.5mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.55_241108_S3000612871.zip) | 2024-11-08 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.55_241108_S3000612871.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.55_SP3_241108_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD3646G2T-IZS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.55 | Applied to: [DS-2CD3646G2T-IZSY(2.7-13.5mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.55_241108_S3000612871.zip)(H) | 2024-11-08 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.55_241108_S3000612871.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.55_SP3_241108_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD3646G2T-LIDZSU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.1 | Applied to: [DS-2CD3646G2T-LIDZSU/4G/SL(2.7-13.5)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.12_260416_S3000716519.zip)OSTD | 2025-08-07 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.12_260416_S3000716519.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202508/releasenote%5CNetwork_Camera-V5.8.1_250807_Release_Note-IPCE_HGL_G5.pdf) |

</details>


<details>
<summary><h2>DS-2CD3646G3-IZSU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD3646G3-IZSUY/SL(2.7-13.5mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | 2025-12-10 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD3646G3-LIZSU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD3646G3-LIZSUY/SL(27135)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip)eFOSTDBLACK | 2025-12-10 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD3646G3T-IZSU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD3646G3T-IZSUY(2.7-13.5mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | 2025-12-10 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD3646G3T-LIZSU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD3646G3T-LIZSUY(27135)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip)eFO-STD/BLACK | 2025-12-10 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD3647G3-LIZSU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD3647G3-LIZSUY/SL(27135)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip)O-STD/BLACK | 2025-12-10 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD3647G3T-LIZSU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD3647G3T-LIZSUY(2.7-13.5mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | 2025-12-10 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD3663G2-IZS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD3663G2-IZS(2.7-13.5mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD3663G2-LIZSU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD3663G2-LIZSU(2.7-13.5mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD3666G2-IZS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.55 | Applied to: [DS-2CD3666G2-IZS(7-35mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.55_241108_S3000612871.zip)(H) | 2024-11-08 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.55_241108_S3000612871.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.55_SP3_241108_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD3666G2HT-LIZS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.55 | Applied to: [DS-2CD3666G2HT-LIZSY(2.7-13.5mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.55_241108_S3000612871.zip) | 2024-11-08 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.55_241108_S3000612871.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.55_SP3_241108_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD3666G2T-IZS - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.2 | Applied to: [DS-2CD3666G2T-IZSY(7-35mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.23_260403_S3000712869.zip)(H)(eF) | 2025-12-24 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.23_260403_S3000712869.zip) |  |
| 5.7.55 | Applied to: [DS-2CD3666G2T-IZSY(2.7-13.5mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.55_241108_S3000612871.zip)(H) | 2024-11-08 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.55_241108_S3000612871.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.55_SP3_241108_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD3666G3-IZSU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD3666G3-IZSUY/SL(2.7-13.5mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | 2025-12-10 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD3666G3-LIZSU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD3666G3-LIZSUY/SL(2.7-13.5mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip)eFOSTD | 2025-12-10 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD3666G3T-IZSU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD3666G3T-IZSUY(2.7-13.5mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | 2025-12-10 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD3666G3T-LIZSU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD3666G3T-LIZSUY(2.7-13.5mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip)eF/O-STD | 2025-12-10 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD3667G3-LIZSU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD3667G3-LIZSUY/SL(2.7-13.5mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip)O-STD | 2025-12-10 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD3667G3T-LIZSU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD3667G3T-LIZSUY(2.7-13.5mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | 2025-12-10 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD3683G2-IZSU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD3683G2-IZSU(2.7-13.5mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip)(B) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD3683G2-LIZSU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD3683G2-LIZSU(2.7-13.5mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD3686G2-IZS - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.2 | Applied to: [DS-2CD3686G2-IZS(7-35mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.23_260403_S3000712869.zip)(H)(eF) | 2025-12-24 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.23_260403_S3000712869.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.55_SP3_241108_Release_Note.pdf) |
| 5.7.55 | Applied to: [DS-2CD3686G2-IZS(2.7-13.5mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.55_241108_S3000612871.zip)(H) | 2024-11-08 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.55_241108_S3000612871.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.55_SP3_241108_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD3686G2HT-LIZS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.55 | Applied to: [DS-2CD3686G2HT-LIZS(2.7-13.5mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.55_241108_S3000612871.zip) | 2024-11-08 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.55_241108_S3000612871.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.55_SP3_241108_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD3686G2T-IZS - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.2 | Applied to: [DS-2CD3686G2T-IZS(7-35mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.23_260403_S3000712869.zip)(H)(eF) | 2025-12-24 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.23_260403_S3000712869.zip) |  |
| 5.7.55 | Applied to: [DS-2CD3686G2T-IZS(2.7-13.5mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.55_241108_S3000612871.zip)(H) | 2024-11-08 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.55_241108_S3000612871.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.55_SP3_241108_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD3686G2T-LIDZSU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.1 | Applied to: [DS-2CD3686G2T-LIDZSU/4G/SL(2.7-13.5)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.12_260416_S3000716519.zip)OSTD | 2025-08-07 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.12_260416_S3000716519.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202508/releasenote%5CNetwork_Camera-V5.8.1_250807_Release_Note-IPCE_HGL_G5.pdf) |

</details>


<details>
<summary><h2>DS-2CD3686G3-IZSU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD3686G3-IZSUY/SL(2.7-13.5mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | 2025-12-10 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD3686G3-LIZSU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD3686G3-LIZSUY/SL(27135)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip)eFOSTDBLACK | 2025-12-10 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD3686G3T-IZSU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD3686G3T-IZSUY(2.7-13.5mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | 2025-12-10 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD3686G3T-LIZSU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD3686G3T-LIZSUY(27135)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip)eFO-STD/BLACK | 2025-12-10 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD3687G3-LIZSU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD3687G3-LIZSUY/SL(27135)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip)O-STD/BLACK | 2025-12-10 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD3687G3T-LIZSU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD3687G3T-LIZSUY(2.7-13.5mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | 2025-12-10 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD36C7G3-LIZSU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.2 | Applied to: [DS-2CD36C7G3-LIZSUY/SL(2.7-13.5mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.23_260403_S3000712869.zip)/O-STD | 2025-11-03 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.23_260403_S3000712869.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202511/releasenote%5CNetwork_Camera-V5.8.2_251103_Release_Note-IPCE_H_G9.pdf) |

</details>


<details>
<summary><h2>DS-2CD36C7G3T-LIZSU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.2 | Applied to: [DS-2CD36C7G3T-LIZSU(2.7-13.5mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.23_260403_S3000712869.zip) | 2025-11-03 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.23_260403_S3000712869.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202511/releasenote%5CNetwork_Camera-V5.8.2_251103_Release_Note-IPCE_H_G9.pdf) |

</details>


<details>
<summary><h2>DS-2CD37167G3T-LIZSU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.2 | Applied to: [DS-2CD37167G3T-LIZSUY(2.7-13.5mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.23_260403_S3000712869.zip) | 2025-11-03 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.23_260403_S3000712869.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202511/releasenote%5CNetwork_Camera-V5.8.2_251103_Release_Note-IPCE_H_G9.pdf) |

</details>


<details>
<summary><h2>DS-2CD3721G2-LIZS - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.10 | Applied to: [DS-2CD3721G2-LIZS(2.7-13.5mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.100_260416_S3000716492.zip) | 2025-07-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.100_260416_S3000716492.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202508/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-E10.pdf) |
| 5.7.12 | Applied to: [DS-2CD3721G2-LIZS(2.7-13.5mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.12_220907_S3000453567.zip) | 2023-06-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.12_220907_S3000453567.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202508/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-E10.pdf) |

</details>


<details>
<summary><h2>DS-2CD3723G2-IZSU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD3723G2-IZSU(2.7-13.5mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip)(B) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD3723G2-LIZSU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD3723G2-LIZSU(2.7-13.5mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD3743G2-IZSU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD3743G2-IZSU(2.7-13.5mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip)(B) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD3743G2-LIZSU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD3743G2-LIZSU(2.7-13.5mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD3746G2-IZS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.55 | Applied to: [DS-2CD3746G2-IZS(7-35mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.55_241108_S3000612871.zip)(H) | 2024-11-08 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.55_241108_S3000612871.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.55_SP3_241108_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD3746G2H-LIZSU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.55 | Applied to: [DS-2CD3746G2H-LIZSU/SLPTRZ(27135)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.55_241108_S3000612871.zip)eFO-STD | 2025-02-11 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.55_241108_S3000612871.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202503/releasenote%5CNetwork_Camera-V5.7.55_SP4_Release_Note-G5_P.pdf) |

</details>


<details>
<summary><h2>DS-2CD3746G2HT-LIZS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.55 | Applied to: [DS-2CD3746G2HT-LIZSU(2.7-13.5mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.55_241108_S3000612871.zip) | 2024-11-08 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.55_241108_S3000612871.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.55_SP3_241108_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD3746G2HT-LIZSU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.55 | Applied to: [DS-2CD3746G2HT-LIZSU(PTRZ)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.55_241108_S3000612871.zip)(27135)eFO-STD | 2025-02-11 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.55_241108_S3000612871.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202503/releasenote%5CNetwork_Camera-V5.7.55_SP4_Release_Note-G5_P.pdf) |

</details>


<details>
<summary><h2>DS-2CD3746G2T-IZS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.55 | Applied to: [DS-2CD3746G2T-IZS(2.7-13.5mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.55_241108_S3000612871.zip)(H) | 2024-11-08 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.55_241108_S3000612871.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.55_SP3_241108_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD3746G3T-IZSU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD3746G3T-IZSUY(2.7-13.5)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip)O-STDBLACK | 2025-12-10 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD3746G3T-LIZSU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD3746G3T-LIZSUY(27135)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip)eFO-STD/BLACK | 2025-12-10 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD3747G3-LIZSUY - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD3747G3-LIZSUY/SL(PTRZ)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip)(27135)O-STD | 2025-12-10 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD3747G3T-LIZSU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD3747G3T-LIZSU(2.7-13.5mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | 2025-12-10 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD3747G3T-LIZSUY - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD3747G3T-LIZSUY/SL(PTRZ)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip)(27135)OSTD | 2025-12-10 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD3763G2-IZSU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD3763G2-IZSU(2.7-13.5mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip)(B) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD3763G2-LIZSU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD3763G2-LIZSU(2.7-13.5mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD3766G2-IZS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.55 | Applied to: [DS-2CD3766G2-IZS(7-35mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.55_241108_S3000612871.zip)(H) | 2024-11-08 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.55_241108_S3000612871.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.55_SP3_241108_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD3766G2H-LIZSU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.55 | Applied to: [DS-2CD3766G2H-LIZSU(PTRZ)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.55_241108_S3000612871.zip)(27135)eF/O-STD | 2025-02-11 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.55_241108_S3000612871.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202503/releasenote%5CNetwork_Camera-V5.7.55_SP4_Release_Note-G5_P.pdf) |

</details>


<details>
<summary><h2>DS-2CD3766G2HT-LIZS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.55 | Applied to: [DS-2CD3766G2HT-LIZSU(2.7-13.5mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.55_241108_S3000612871.zip) | 2024-11-08 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.55_241108_S3000612871.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.55_SP3_241108_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD3766G2HT-LIZSU - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.2 | Applied to: [DS-2CD3766G2HT-LIZSU/SLPTRZ(27135)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.23_260403_S3000712869.zip)eFOSTD | 2025-12-24 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.23_260403_S3000712869.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202503/releasenote%5CNetwork_Camera-V5.7.55_SP4_Release_Note-G5_P.pdf) |
| 5.7.55 | Applied to: [DS-2CD3766G2HT-LIZSU(PTRZ)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.55_241108_S3000612871.zip)(27135)eFO-STD | 2025-02-11 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.55_241108_S3000612871.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202503/releasenote%5CNetwork_Camera-V5.7.55_SP4_Release_Note-G5_P.pdf) |

</details>


<details>
<summary><h2>DS-2CD3766G2T-IZS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.55 | Applied to: [DS-2CD3766G2T-IZS(2.7-13.5mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.55_241108_S3000612871.zip)(H) | 2024-11-08 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.55_241108_S3000612871.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.55_SP3_241108_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD3766G3T-IZSU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD3766G3T-IZSUY(2.7-13.5mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | 2025-12-10 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD3766G3T-LIZSU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD3766G3T-LIZSU(2.7-13.5mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip)(eF)O-STD | 2025-12-10 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD3767G3-LIZSUY - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD3767G3-LIZSUY/SL(PTRZ)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip)(27135)O-STD | 2025-12-10 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD3767G3T-LIZSU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD3767G3T-LIZSU(2.7-13.5mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | 2025-12-10 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD3767G3T-LIZSUY - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD3767G3T-LIZSUY/SL(PTRZ)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip)(27135)OSTD | 2025-12-10 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD3783G2-IZSU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD3783G2-IZSU(2.7-13.5mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip)(B) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD3783G2-LIZSU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD3783G2-LIZSU(2.7-13.5mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD3786G2-IZS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.55 | Applied to: [DS-2CD3786G2-IZS(2.7-13.5mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.55_241108_S3000612871.zip)(H) | 2024-11-08 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.55_241108_S3000612871.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.55_SP3_241108_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD3786G2H-LIZSU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.55 | Applied to: [DS-2CD3786G2H-LIZSU(PTRZ)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.55_241108_S3000612871.zip)(27135)eF/O-STD | 2025-02-11 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.55_241108_S3000612871.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202503/releasenote%5CNetwork_Camera-V5.7.55_SP4_Release_Note-G5_P.pdf) |

</details>


<details>
<summary><h2>DS-2CD3786G2HT-LIZS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.55 | Applied to: [DS-2CD3786G2HT-LIZSU(2.7-13.5mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.55_241108_S3000612871.zip) | 2024-11-08 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.55_241108_S3000612871.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.55_SP3_241108_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD3786G2HT-LIZSU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.55 | Applied to: [DS-2CD3786G2HT-LIZSU(PTRZ)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.55_241108_S3000612871.zip)(27135)eFO-STD | 2025-02-11 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.55_241108_S3000612871.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202503/releasenote%5CNetwork_Camera-V5.7.55_SP4_Release_Note-G5_P.pdf) |

</details>


<details>
<summary><h2>DS-2CD3786G2T-IZS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.55 | Applied to: [DS-2CD3786G2T-IZS(2.7-13.5mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.55_241108_S3000612871.zip)(H) | 2024-11-08 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.55_241108_S3000612871.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.55_SP3_241108_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD3786G3T-IZSU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD3786G3T-IZSUY(7-35mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | 2025-12-10 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD3786G3T-LIZSU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD3786G3T-LIZSUY(2.7-13.5mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip)eF/O-STD | 2025-12-10 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD3787G3-LIZSUY - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD3787G3-LIZSUY/SL(PTRZ)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip)(27135)O-STD | 2025-12-10 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD3787G3T-LIZSU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD3787G3T-LIZSUY(2.7-13.5mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | 2025-12-10 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD3787G3T-LIZSUY - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD3787G3T-LIZSUY/SL(PTRZ)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip)(27135)OSTD | 2025-12-10 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD37C7G3T-LIZSU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.2 | Applied to: [DS-2CD37C7G3T-LIZSUY(2.7-13.5mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.23_260403_S3000712869.zip) | 2025-11-03 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.23_260403_S3000712869.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202511/releasenote%5CNetwork_Camera-V5.8.2_251103_Release_Note-IPCE_H_G9.pdf) |

</details>


<details>
<summary><h2>DS-2CD3843G0-AP - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD3843G0-AP](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | 2024-12-11 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202507/releasenote%5CNetwork_Camera-V5.7.23_SP2_Release_Note-E8.pdf) |

</details>


<details>
<summary><h2>DS-2CD3843G2-AP - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD3843G2-AP](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD3956G2-IS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.40 | Applied to: [DS-2CD3956G2-IS(1.05mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.40_230218_S3000482515.zip) | 2023-02-18 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.40_230218_S3000482515.zip) |  |

</details>


<details>
<summary><h2>DS-2CD3A26G2T-IZS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.0 | Applied to: [DS-2CD3A26G2T-IZS(4.7-71mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.0_240129_S3000555034.zip) | 2023-06-27 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.0_240129_S3000555034.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202408/releasenote%5CNetwork_Camera-V5.7.0_SP2_Release_Note-IPCE_LZ_H8_230627.pdf) |

</details>


<details>
<summary><h2>DS-2CD3A46G2T-IZHS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.0 | Applied to: [DS-2CD3A46G2T-IZHS(6-60mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.0_231109_S3000541088.zip) | 2024-11-03 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.0_231109_S3000541088.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202511/releasenote%5CNetwork_Camera-V5.7.5_SP3_Release_Note-H8.pdf) |

</details>


<details>
<summary><h2>DS-2CD3B26G2T-IZHS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.55 | Applied to: [DS-2CD3B26G2T-IZHS(8-32mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.55_241108_S3000612871.zip)(H) | 2024-11-08 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.55_241108_S3000612871.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.55_SP3_241108_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD3B46G2T-IZHS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.55 | Applied to: [DS-2CD3B46G2T-IZHSY(8-32mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.55_241108_S3000612871.zip)(H) | 2024-11-08 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.55_241108_S3000612871.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.55_SP3_241108_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD3B86G2T-IZHS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.55 | Applied to: [DS-2CD3B86G2T-IZHSY(8-32mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.55_241108_S3000612871.zip)(H) | 2024-11-08 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.55_241108_S3000612871.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.55_SP3_241108_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD3D46G2T-IZHSU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.55 | Applied to: [DS-2CD3D46G2T-IZHSUY(8-32mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.55_241108_S3000612871.zip)(H) | 2024-11-08 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.55_241108_S3000612871.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.55_SP3_241108_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD3D86G2T-IZHSU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.55 | Applied to: [DS-2CD3D86G2T-IZHSUY(8-32mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.55_241108_S3000612871.zip)(H) | 2024-11-08 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.55_241108_S3000612871.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.55_SP3_241108_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD3H167G3-LIZSU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.2 | Applied to: [DS-2CD3H167G3-LIZSUY(2.7-13.5mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.23_260403_S3000712869.zip) | 2025-11-03 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.23_260403_S3000712869.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202511/releasenote%5CNetwork_Camera-V5.8.2_251103_Release_Note-IPCE_H_G9.pdf) |

</details>


<details>
<summary><h2>DS-2CD3H23G2-LIZSU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD3H23G2-LIZSU(2.7-13.5mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD3H43G2-LIZSU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD3H43G2-LIZSU(2.7-13.5mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | 2026-03-20 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) |  |

</details>


<details>
<summary><h2>DS-2CD3H46G3-LIZSU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD3H46G3-LIZSUY/SL(2.7-13.5)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip)eFO-STD | 2025-12-10 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD3H47G3-LIZSUY - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD3H47G3-LIZSUY/SL(2.7-13.5)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip)O-STDBLK | 2025-12-10 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD3H63G2-LIZSU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD3H63G2-LIZSU(2.7-13.5mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | 2026-03-20 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) |  |

</details>


<details>
<summary><h2>DS-2CD3H66G3-LIZSU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD3H66G3-LIZSUY/SL(2.7-13.5)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip)eFO-STD | 2025-12-10 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD3H67G3-LIZSUY - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD3H67G3-LIZSUY/SL(2.7-13.5)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip)O-STDBLK | 2025-12-10 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD3H83G2-LIZSU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD3H83G2-LIZSU(2.7-13.5mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD3H86G3-LIZSU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD3H86G3-LIZSUY/SL(2.7-13.5)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip)eFO-STD | 2025-12-10 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD3H87G3-LIZSUY - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD3H87G3-LIZSUY/SL(2.7-13.5)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip)O-STDBLK | 2025-12-10 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD3HC7G3-LIZSU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.2 | Applied to: [DS-2CD3HC7G3-LIZSUY(2.7-13.5mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.23_260403_S3000712869.zip) | 2025-11-03 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.23_260403_S3000712869.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202511/releasenote%5CNetwork_Camera-V5.8.2_251103_Release_Note-IPCE_H_G9.pdf) |

</details>


<details>
<summary><h2>DS-2CD3T167G3-LISU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.2 | Applied to: [DS-2CD3T167G3-LISUY(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.23_260403_S3000712869.zip) | 2025-11-03 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.23_260403_S3000712869.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202511/releasenote%5CNetwork_Camera-V5.8.2_251103_Release_Note-IPCE_H_G9.pdf) |

</details>


<details>
<summary><h2>DS-2CD3T23G1-I - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.52 | Applied to: [DS-2CD3T23G1-I/4G(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.52_240705_S3000585755.zip) | 2024-07-05 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.52_240705_S3000585755.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202408/1722466890133/releasenote%5CG5_6_Series_Solar_5.7.52_Release_Note.pdf) |
| 5.7.51 | Applied to: [DS-2CD3T23G1-I/4G(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.51_240320_S3000563201.zip) | 2024-03-20 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.51_240320_S3000563201.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202408/1722466890133/releasenote%5CG5_6_Series_Solar_5.7.52_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD3T23G2-2IS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD3T23G2-2ISU(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip)(B) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD3T23G2-2LISU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD3T23G2-2LISU(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD3T23G2-LISU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD3T23G2-LISU/SL(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD3T43G2-2IS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD3T43G2-2IS(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD3T43G2-2LISU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD3T43G2-2LISU(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD3T43G2-LISU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD3T43G2-LISU/SL(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD3T46G2-4IS - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.2 | Applied to: [DS-2CD3T46G2-4ISY(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.23_260403_S3000712869.zip)(H) | 2025-12-24 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.23_260403_S3000712869.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.55_SP3_241108_Release_Note.pdf) |
| 5.7.55 | Applied to: [DS-2CD3T46G2-4ISY(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.55_241108_S3000612871.zip)(H) | 2024-11-08 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.55_241108_S3000612871.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.55_SP3_241108_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD3T46G2-ISU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.55 | Applied to: [DS-2CD3T46G2-ISU/SL(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.55_241108_S3000612871.zip)(H) | 2024-11-08 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.55_241108_S3000612871.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.55_SP3_241108_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD3T46G2-LIDSU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.1 | Applied to: [DS-2CD3T46G2-LIDSU/4G/SL(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.12_260416_S3000716519.zip) | 2025-08-07 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.12_260416_S3000716519.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202508/releasenote%5CNetwork_Camera-V5.8.1_250807_Release_Note-IPCE_HGL_G5.pdf) |

</details>


<details>
<summary><h2>DS-2CD3T46G2H-LIS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.55 | Applied to: [DS-2CD3T46G2H-LIS(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.55_241108_S3000612871.zip) | 2024-11-08 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.55_241108_S3000612871.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.55_SP3_241108_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD3T46G3-2ISU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD3T46G3-4ISUY(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | 2025-12-10 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD3T46G3-ISU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD3T46G3-ISUY/SL(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | 2025-12-10 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD3T46G3-LISU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD3T46G3-LISUY(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip)(eF) | 2025-12-10 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD3T47G3-LISU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD3T47G3-LISUY(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | 2025-12-10 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD3T63G2-2IS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD3T63G2-2ISU(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip)(B) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD3T63G2-2LISU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD3T63G2-2LISU(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD3T63G2-LISU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD3T63G2-LISU/SL(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD3T66G2-4IS - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.2 | Applied to: [DS-2CD3T66G2-4IS(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.23_260403_S3000712869.zip)(H)(eF) | 2025-12-24 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.23_260403_S3000712869.zip) |  |
| 5.7.55 | Applied to: [DS-2CD3T66G2-4IS(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.55_241108_S3000612871.zip)(H) | 2024-11-08 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.55_241108_S3000612871.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.55_SP3_241108_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD3T66G2H-LIS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.55 | Applied to: [DS-2CD3T66G2H-LISU(4mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.55_241108_S3000612871.zip) | 2024-11-08 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.55_241108_S3000612871.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.55_SP3_241108_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD3T66G3-2ISU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD3T66G3-4ISUY(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | 2025-12-10 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD3T66G3-ISU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD3T66G3-ISUY/SL(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | 2025-12-10 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD3T66G3-LISU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD3T66G3-LISUY(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip)(eF) | 2025-12-10 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD3T67G3-LISU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD3T67G3-LISUY(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | 2025-12-10 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD3T83G2-2LISU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD3T83G2-2LISU(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD3T83G2-LISU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD3T83G2-LISU/SL(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | 2026-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.7.23_260114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD3T86G2-4IS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.55 | Applied to: [DS-2CD3T86G2-4ISY(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.55_241108_S3000612871.zip)(H) | 2024-11-08 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.55_241108_S3000612871.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.55_SP3_241108_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD3T86G2-LIDSU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.1 | Applied to: [DS-2CD3T86G2-LIDSU/4G/SL(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.12_260416_S3000716519.zip) | 2025-08-07 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.12_260416_S3000716519.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202508/releasenote%5CNetwork_Camera-V5.8.1_250807_Release_Note-IPCE_HGL_G5.pdf) |

</details>


<details>
<summary><h2>DS-2CD3T86G2H-LIS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.55 | Applied to: [DS-2CD3T86G2H-LISUY(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.55_241108_S3000612871.zip) | 2024-11-08 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.55_241108_S3000612871.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.55_SP3_241108_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD3T86G3-2ISU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD3T86G3-4ISUY(6mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | 2025-12-10 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD3T86G3-ISU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD3T86G3-ISUY/SL(6mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | 2025-12-10 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD3T86G3-LISU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD3T86G3-LISUY(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip)(eF) | 2025-12-10 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD3T87G2P-LSU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.20 | Applied to: [DS-2CD3T87G2P-LSU/SL(4mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.20_230630_S3000509422.zip)(C) | 2025-11-25 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.20_230630_S3000509422.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.20_251125_Release_Note-IPCE_P_G5.pdf) |

</details>


<details>
<summary><h2>DS-2CD3T87G3-LISU - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD3T87G3-LISUY(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | 2025-12-10 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.30_251210_S3000691330.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |
| 5.8.10 | Applied to: [DS-2CD3T87G3-LISUY(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.100_260416_S3000716492.zip) | 2025-04-10 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.100_260416_S3000716492.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD3TC7G3-LISU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.2 | Applied to: [DS-2CD3TC7G3-LISUY(4mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.23_260403_S3000712869.zip)(BLACK) | 2025-11-03 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.23_260403_S3000712869.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202511/releasenote%5CNetwork_Camera-V5.8.2_251103_Release_Note-IPCE_H_G9.pdf) |

</details>


<details>
<summary><h2>DS-2CD4A24FWD-IZ - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.84 | Applied to: [DS-2CD4A24FWD-IZ(4.7-94mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/d555f2de-098a-40f4-b417-e8db8a68a42a.zip)(T) | 2019-05-07 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/d555f2de-098a-40f4-b417-e8db8a68a42a.zip) |  |

</details>


<details>
<summary><h2>DS-2CD4A45G0-IZ - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.85 | Applied to: [DS-2CD4A45G0-IZHS(4.7-94mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/IPCDC_H7_EN_STD_5.5.850_220421.zip)(B) | 2019-11-07 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/IPCDC_H7_EN_STD_5.5.850_220421.zip) |  |

</details>


<details>
<summary><h2>DS-2CD4B26FWD-IZ - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.91 | Applied to: [DS-2CD4B26FWD-IZS(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/560e73e2-270f-4f2d-b248-d18f6e89e09e.zip) | 2021-04-29 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/560e73e2-270f-4f2d-b248-d18f6e89e09e.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202312/releasenote%5C%E3%80%90Release_Note%E3%80%91Mobile_IPC_V5.5.91_210429.pdf) |

</details>


<details>
<summary><h2>DS-2CD4B36FWD-IZ - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.91 | Applied to: [DS-2CD4B36FWD-IZS(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/560e73e2-270f-4f2d-b248-d18f6e89e09e.zip) | 2021-04-29 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/560e73e2-270f-4f2d-b248-d18f6e89e09e.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202312/releasenote%5C%E3%80%90Release_Note%E3%80%91Mobile_IPC_V5.5.91_210429.pdf) |

</details>


<details>
<summary><h2>DS-2CD4B45G0-IZS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.85 | Applied to: [DS-2CD4B45G0-IZS(4.7-65.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/IPCDC_H7_EN_STD_5.5.850_220421.zip)(B) | 2019-11-07 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/IPCDC_H7_EN_STD_5.5.850_220421.zip) |  |

</details>


<details>
<summary><h2>DS-2CD4D36FWD-IZ - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.91 | Applied to: [DS-2CD4D36FWD-IZS(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/560e73e2-270f-4f2d-b248-d18f6e89e09e.zip) | 2021-04-29 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/560e73e2-270f-4f2d-b248-d18f6e89e09e.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202312/releasenote%5C%E3%80%90Release_Note%E3%80%91Mobile_IPC_V5.5.91_210429.pdf) |

</details>


<details>
<summary><h2>DS-2CD6045G0 - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.6 | Applied to: [DS-2CD6045G0/SC-IZRS(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.6_260203_S3000702384.zip) | 2026-02-03 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.6_260203_S3000702384.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202603/releasenote%5CCyclonic_Dust-Resistant_Camera_V5.8.6_260203_Release_Note.pdf) |
| 5.8.2 | Applied to: [DS-2CD6045G0/SC-IZRS(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.23_260403_S3000712869.zip) | 2025-02-22 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.23_260403_S3000712869.zip) |  |

</details>


<details>
<summary><h2>DS-2CD6085G0 - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.6 | Applied to: [DS-2CD6085G0/SC-IZRS(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.6_260203_S3000702384.zip) | 2026-02-03 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.6_260203_S3000702384.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202603/releasenote%5CCyclonic_Dust-Resistant_Camera_V5.8.6_260203_Release_Note.pdf) |
| 5.8.2 | Applied to: [DS-2CD6085G0/SC-IZRS(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.23_260403_S3000712869.zip) | 2025-02-22 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.23_260403_S3000712869.zip) |  |

</details>


<details>
<summary><h2>DS-2CD6365G1-IVS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.3 | Applied to: [DS-2CD6365G1-IVS(1.16mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.3_260416_S3000716238.zip) | 2026-01-12 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.3_260416_S3000716238.zip) |  |

</details>


<details>
<summary><h2>DS-2CD6365G1-S - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.3 | Applied to: [DS-2CD6365G1-S/RC(1.16mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.3_260416_S3000716238.zip) | 2026-01-12 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.3_260416_S3000716238.zip) |  |

</details>


<details>
<summary><h2>DS-2CD63C5G1-IVS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.3 | Applied to: [DS-2CD63C5G1-IVS(1.29mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.3_260416_S3000716238.zip) | 2026-01-12 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.3_260416_S3000716238.zip) |  |

</details>


<details>
<summary><h2>DS-2CD63C5G1-S - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.3 | Applied to: [DS-2CD63C5G1-S/RC(1.29mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.3_260416_S3000716238.zip) | 2026-01-12 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.3_260416_S3000716238.zip) |  |

</details>


<details>
<summary><h2>DS-2CD6425G1-XX - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.210 | Applied to: [DS-2CD6425G1-10(3.7mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/IPCG_E8_EN_STD_5.7.210_220615.zip)2m | 2022-06-15 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/IPCG_E8_EN_STD_5.7.210_220615.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202312/releasenote%5CIPC_V5.7.210_SP_Release_Note--EN.pdf) |

</details>


<details>
<summary><h2>DS-2CD6425G2-C1 - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.20 | Applied to: [DS-2CD6425G2-C1](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.20_230426_S3000496912.zip) | 2023-04-26 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.20_230426_S3000496912.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202312/releasenote%5CIPCG_OP_G5_V5.8.20_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD6425G2-C2 - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.20 | Applied to: [DS-2CD6425G2-C2](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.20_230426_S3000496912.zip) | 2023-04-26 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.20_230426_S3000496912.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202312/releasenote%5CIPCG_OP_G5_V5.8.20_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD6445G1-XX - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.210 | Applied to: [DS-2CD6445G1-30(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/IPCG_E8_EN_STD_5.7.210_220615.zip)2m | 2022-06-15 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/IPCG_E8_EN_STD_5.7.210_220615.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202312/releasenote%5CIPC_V5.7.210_SP_Release_Note--EN.pdf) |

</details>


<details>
<summary><h2>DS-2CD6445G2-C1 - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.20 | Applied to: [DS-2CD6445G2-C1/HDMI](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.20_230426_S3000496912.zip) | 2023-04-26 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.20_230426_S3000496912.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202312/releasenote%5CIPCG_OP_G5_V5.8.20_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD6825G0 - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.10 | Applied to: [DS-2CD6825G0/C-I(2mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.100_260416_S3000716492.zip)(B) | 2025-06-24 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.100_260416_S3000716492.zip) |  |

</details>


<details>
<summary><h2>DS-2CD6825G0 - IPC_V5 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.850 | Applied to: [DS-2CD6825G0/C-I(2mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/IPCDC_H7_EN_STD_5.5.850_220421.zip) | 2022-04-21 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/IPCDC_H7_EN_STD_5.5.850_220421.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202207/IPC_V5.5.850_build_220421_Release%20Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD6924G0-IHS - IPC_G0 (3 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.1 | Applied to: [DS-2CD6924G0-IHS(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.11_260413_S3000716685.zip)(C) | 2024-06-13 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.11_260413_S3000716685.zip) |  |
| 5.7.0 | Applied to: [DS-2CD6924G0-IHS/NFC(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.0_240129_S3000555034.zip) | 2024-01-29 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.0_240129_S3000555034.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202312/releasenote%5CIPCP_H5_5.5.820_Release_Note.pdf) |
| 5.5.820 | Applied to: [DS-2CD6924G0-IHS/NFC(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.820_260410_S3000715634.zip) | 2023-07-17 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.820_260410_S3000715634.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202312/releasenote%5CIPCP_H5_5.5.820_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD6944G0-IHS - IPC_G0 (3 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.1 | Applied to: [DS-2CD6944G0-IHS(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.11_260413_S3000716685.zip)(C) | 2024-06-13 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.11_260413_S3000716685.zip) |  |
| 5.7.0 | Applied to: [DS-2CD6944G0-IHS(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.0_240129_S3000555034.zip) | 2024-01-29 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.0_240129_S3000555034.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202312/releasenote%5CIPCP_H5_5.5.820_Release_Note.pdf) |
| 5.5.820 | Applied to: [DS-2CD6944G0-IHS(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.820_260410_S3000715634.zip) | 2023-07-17 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.820_260410_S3000715634.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202312/releasenote%5CIPCP_H5_5.5.820_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD6951G2-IS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.11 | Applied to: [DS-2CD6951G2-IS(2mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.110_260421_S3000717992.zip) | 2025-11-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.110_260421_S3000717992.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CIPCG_PS_G5_Camera_V5.8.11_251114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD6984G0-IH - IPC_G0 (3 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.0 | Applied to: [DS-2CD6984G0-IHSAC/NFC(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.0_240129_S3000555034.zip) | 2024-01-29 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.0_240129_S3000555034.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202312/releasenote%5CIPCP_H5_5.5.820_Release_Note.pdf) |
| 5.5.820 | Applied to: [DS-2CD6984G0-IHSAC/NFC(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.820_260410_S3000715634.zip) | 2023-07-17 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.820_260410_S3000715634.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202312/releasenote%5CIPCP_H5_5.5.820_Release_Note.pdf) |
| 5.5.800 | Applied to: [DS-2CD6984G0-IHSAC/NFC(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.800_211009_S3000390724.zip) | 2021-10-09 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.800_211009_S3000390724.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202312/releasenote%5CIPCP_H5_5.5.820_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD6984G0-IHS - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.0 | Applied to: [DS-2CD6984G0-IHS/NFC(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.0_240129_S3000555034.zip) | 2024-01-29 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.0_240129_S3000555034.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/b28e00a3-3d4d-405a-94e7-c3f287c0b839.pdf) |
| 5.5.800 | Applied to: [DS-2CD6984G0-IHS/NFC(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.800_211009_S3000390724.zip) | 2021-10-09 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.800_211009_S3000390724.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/b28e00a3-3d4d-405a-94e7-c3f287c0b839.pdf) |

</details>


<details>
<summary><h2>DS-2CD6B35G0-PLW - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.12 | Applied to: [DS-2CD6B35G0-PLW(4mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.12_260416_S3000716519.zip) | 2026-04-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.12_260416_S3000716519.zip) |  |

</details>


<details>
<summary><h2>DS-2CD6B55G0-PL - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.211 | Applied to: [DS-2CD6B55G0-PL/T1(4mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.211_250825_S3000670507.zip) | 2025-08-25 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.211_250825_S3000670507.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5C6B_Camera_V5.7.211_250825_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD6D24FWD-IZHS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.821 | Applied to: [DS-2CD6D24FWD-IZHS(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.821_231108_S3000539548.zip)(B) | 2023-08-30 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.821_231108_S3000539548.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202310/releasenote%5CIPCMC_H3_V5.5.821_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD6D42G0-IS - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.21 | Applied to: [DS-2CD6D42G0-IS(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.21_250714_S3000661481.zip) | 2025-09-01 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.21_250714_S3000661481.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202508/releasenote%5CIPCG_PS_G5_Camera_V5.8.11_250730_Release_Note.pdf) |
| 5.8.11 | Applied to: [DS-2CD6D42G0-IS(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.110_260421_S3000717992.zip) | 2023-08-07 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.110_260421_S3000717992.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202508/releasenote%5CIPCG_PS_G5_Camera_V5.8.11_250730_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD6D42G2-IS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.9.0 | Applied to: [DS-2CD6D42G2-IS(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.9.0_250730_S3000665724.zip) | 2025-07-30 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.9.0_250730_S3000665724.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5C6_Series_Dual-Lens_Camera_V5.9.0_250730_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD6D44G1-IZS - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.9.12 | Applied to: [DS-2CD6D44G1-IZS(2.8-8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.9.12_260407_S3000713711.zip) | 2026-04-07 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.9.12_260407_S3000713711.zip) |  |
| 5.9.11 | Applied to: [DS-2CD6D44G1-IZS(2.8-8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.9.11_251030_S3000682327.zip) | 2024-01-23 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.9.11_251030_S3000682327.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202403/releasenote%5CG7_6D_V5.9.11_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD6D44G1H-IZS - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.9.12 | Applied to: [DS-2CD6D44G1H-IZS(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.9.12_260407_S3000713711.zip) | 2026-04-07 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.9.12_260407_S3000713711.zip) |  |
| 5.9.11 | Applied to: [DS-2CD6D44G1H-IZS(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.9.11_251030_S3000682327.zip) | 2024-01-23 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.9.11_251030_S3000682327.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202403/releasenote%5CG7_6D_V5.9.11_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD6D52G0-IH - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.820 | Applied to: [DS-2CD6D52G0-IHS(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.820_260410_S3000715634.zip) | 2022-06-09 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.820_260410_S3000715634.zip) |  |

</details>


<details>
<summary><h2>DS-2CD6D52G0-IH-S- - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.820 | [DS-2CD6D52G0-IH-S-](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.820_260410_S3000715634.zip) | 2026-04-10 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.820_260410_S3000715634.zip) |  |

</details>


<details>
<summary><h2>DS-2CD6D52G0-IHS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.820 | Applied to: [DS-2CD6D52G0-IHS(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.820_260410_S3000715634.zip) | 2026-04-10 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.820_260410_S3000715634.zip) |  |

</details>


<details>
<summary><h2>DS-2CD6D54FWD- - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.801 | Applied to: [DS-2CD6D54FWD-IZHS(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/4c6ede40-0464-4a88-a0e4-f87cc45b37a2.zip) | 2021-09-27 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/4c6ede40-0464-4a88-a0e4-f87cc45b37a2.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202207/IPC%20V5.5.801%20build%20210927%20Release%20Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD6D54G1-IZ - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.801 | Applied to: [DS-2CD6D54G1-IZS(2.8-8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/4c6ede40-0464-4a88-a0e4-f87cc45b37a2.zip) | 2021-09-27 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/4c6ede40-0464-4a88-a0e4-f87cc45b37a2.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202207/IPC%20V5.5.801%20build%20210927%20Release%20Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD6D54G1-IZS - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.821 | Applied to: [DS-2CD6D54G1-IZS(2.8-8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.821_231108_S3000539548.zip)(B) | 2023-08-30 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.821_231108_S3000539548.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202310/releasenote%5CIPCMC_H3_V5.5.821_Release_Note.pdf) |
| 5.5.801 | Applied to: [DS-2CD6D54G1-IZS(2.8-8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/4c6ede40-0464-4a88-a0e4-f87cc45b37a2.zip) | 2021-09-27 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/4c6ede40-0464-4a88-a0e4-f87cc45b37a2.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202207/IPC%20V5.5.801%20build%20210927%20Release%20Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD6D54G1-ZS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.801 | Applied to: [DS-2CD6D54G1-ZS/RC(2.8-8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/4c6ede40-0464-4a88-a0e4-f87cc45b37a2.zip) | 2021-09-27 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/4c6ede40-0464-4a88-a0e4-f87cc45b37a2.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202207/IPC%20V5.5.801%20build%20210927%20Release%20Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD6D54G2-IZHS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.9.0 | Applied to: [DS-2CD6D54G2-IZHS(2.8-8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.9.0_251208_S3000690292.zip) | 2025-12-08 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.9.0_251208_S3000690292.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CPanoVu_Camera_6D5x_V5.9.0_251208_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD6D55G2-IZHS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.9.0 | Applied to: [DS-2CD6D55G2-IZHS(2.8-8mm/2mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.9.0_251208_S3000690292.zip) | 2025-12-08 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.9.0_251208_S3000690292.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CPanoVu_Camera_6D5x_V5.9.0_251208_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD6D82G0-IH - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.820 | Applied to: [DS-2CD6D82G0-IHS(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.820_260410_S3000715634.zip) | 2022-06-09 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.820_260410_S3000715634.zip) |  |

</details>


<details>
<summary><h2>DS-2CD6D82G0-IH-S- - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.820 | [DS-2CD6D82G0-IH-S-](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.820_260410_S3000715634.zip) | 2026-04-10 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.820_260410_S3000715634.zip) |  |

</details>


<details>
<summary><h2>DS-2CD6D82G0-IHS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.820 | Applied to: [DS-2CD6D82G0-IHS(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.820_260410_S3000715634.zip) | 2026-04-10 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.820_260410_S3000715634.zip) |  |

</details>


<details>
<summary><h2>DS-2CD6D82G2-IS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.9.0 | Applied to: [DS-2CD6D82G2-IS(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.9.0_250730_S3000665724.zip) | 2025-07-30 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.9.0_250730_S3000665724.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5C6_Series_Dual-Lens_Camera_V5.9.0_250730_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD6F82G0-S - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.2 | Applied to: [DS-2CD6F82G0-S(4mm/8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.23_260403_S3000712869.zip) | 2025-07-09 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.23_260403_S3000712869.zip) |  |

</details>


<details>
<summary><h2>DS-2CD6F82G0-WS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.2 | Applied to: [DS-2CD6F82G0-WS(4mm/8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.23_260403_S3000712869.zip) | 2025-07-09 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.23_260403_S3000712869.zip) |  |

</details>


<details>
<summary><h2>DS-2CD6W65G1-IVS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.3 | Applied to: [DS-2CD6W65G1-IVS(1.16mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.3_260416_S3000716238.zip) | 2026-01-12 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.3_260416_S3000716238.zip) |  |

</details>


<details>
<summary><h2>DS-2CE11D0T-PIRLO - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 1.04.00 | Applied to: [DS-2CE11D0T-PIRLO(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/69abb770-f4dd-44cc-8019-2402c5b56195.zip) | 2019-12-02 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/69abb770-f4dd-44cc-8019-2402c5b56195.zip) |  |

</details>


<details>
<summary><h2>DS-2CE12D0T-PIRLO - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 1.04.00 | Applied to: [DS-2CE12D0T-PIRLO(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/69abb770-f4dd-44cc-8019-2402c5b56195.zip) | 2019-12-02 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/69abb770-f4dd-44cc-8019-2402c5b56195.zip) |  |

</details>


<details>
<summary><h2>DS-2CE16C0T-IRP - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 1.03.00 | Applied to: [DS-2CE16C0T-IRP(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/2d1e38da-635e-4597-9968-4849720b7602.zip)(B) | 2018-01-17 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/2d1e38da-635e-4597-9968-4849720b7602.zip) |  |

</details>


<details>
<summary><h2>DS-2CE16D0T-VFIR3F - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 1.09.00 | Applied to: [DS-2CE16D0T-VFIR3F(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/c07f4409-e9af-42b2-af68-4dd1a78afad4.zip) | 2021-12-02 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/c07f4409-e9af-42b2-af68-4dd1a78afad4.zip) |  |

</details>


<details>
<summary><h2>DS-2CE16H0T-ITF - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 1.03.02 | Applied to: [DS-2CE16H0T-ITF(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/431928a6-68c4-4c12-9768-f832b6d9ce30.zip) | 2020-08-26 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/431928a6-68c4-4c12-9768-f832b6d9ce30.zip) |  |

</details>


<details>
<summary><h2>DS-2CE56C0T-IRP - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 1.03.00 | Applied to: [DS-2CE56C0T-IRP(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/2d1e38da-635e-4597-9968-4849720b7602.zip)(B) | 2018-01-17 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/2d1e38da-635e-4597-9968-4849720b7602.zip) |  |

</details>


<details>
<summary><h2>DS-2CE56D0T-VFIR3E - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 1.05.01 | Applied to: [DS-2CE56D0T-VFIR3E(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/43fc2fab-1e87-4a88-b81f-807028b6c33c.zip) | 2020-03-23 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/43fc2fab-1e87-4a88-b81f-807028b6c33c.zip) |  |

</details>


<details>
<summary><h2>DS-2CE56D0T-VFIR3F - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 1.09.00 | Applied to: [DS-2CE56D0T-VFIR3F(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/70474c85-ca48-4d5d-bc63-6ff018ea610c.zip) | 2019-12-02 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/70474c85-ca48-4d5d-bc63-6ff018ea610c.zip) |  |

</details>


<details>
<summary><h2>DS-2CE56D0T-VFIRE - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 1.05.01 | Applied to: [DS-2CE56D0T-VFIRE(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/f5bbc2ed-315c-4413-a94c-5fd4fdda15de.zip) | 2020-03-23 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/f5bbc2ed-315c-4413-a94c-5fd4fdda15de.zip) |  |

</details>


<details>
<summary><h2>DS-2CE56D0T-VPIR3F - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 1.09.00 | Applied to: [DS-2CE56D0T-VPIR3F(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/70474c85-ca48-4d5d-bc63-6ff018ea610c.zip) | 2019-12-02 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/70474c85-ca48-4d5d-bc63-6ff018ea610c.zip) |  |

</details>


<details>
<summary><h2>DS-2CE71D0T-PIRLO - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 1.04.00 | Applied to: [DS-2CE71D0T-PIRLO(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/69abb770-f4dd-44cc-8019-2402c5b56195.zip) | 2019-12-02 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/69abb770-f4dd-44cc-8019-2402c5b56195.zip) |  |

</details>


<details>
<summary><h2>DS-2CFS04 - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.9.11 | Applied to: [DS-2CFS04/4G(4mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.9.11_251030_S3000682327.zip) | 2025-10-30 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.9.11_251030_S3000682327.zip) |  |

</details>


<details>
<summary><h2>DS-2CFW02 - UNKNOWN (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.23 | Applied to: [DS-2CFW02(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.23_260403_S3000712869.zip) | 2026-04-03 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.23_260403_S3000712869.zip) |  |
| 5.8.22 | Applied to: [DS-2CFW02(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.22_250708_S3000661562.zip) | 2025-07-08 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.22_250708_S3000661562.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202508/releasenote%5CNetwork_Camera-V5.8.22_250708_Release_Note-E9.pdf) |

</details>


<details>
<summary><h2>DS-2CFW04 - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.22 | Applied to: [DS-2CFW04(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.22_250708_S3000661562.zip) | 2025-07-08 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.22_250708_S3000661562.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202508/releasenote%5CNetwork_Camera-V5.8.22_250708_Release_Note-E10.pdf) |

</details>


<details>
<summary><h2>DS-2CFW06-P - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.10 | Applied to: [DS-2CFW06-P(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.100_260416_S3000716492.zip) | 2025-10-29 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.100_260416_S3000716492.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.8.10_251029_Release_Note-IPCE_PW_E11.pdf) |

</details>


<details>
<summary><h2>DS-2CFWQ3 - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.100 | Applied to: [DS-2CFWQ3(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.100_260416_S3000716492.zip) | 2025-08-05 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.100_260416_S3000716492.zip) |  |

</details>


<details>
<summary><h2>DS-2CFWQ5 - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.100 | Applied to: [DS-2CFWQ5(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.100_260416_S3000716492.zip) | 2025-07-25 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.100_260416_S3000716492.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202509/releasenote%5CNetwork_Camera-V5.8.100_250725_Release_Note-E12.pdf) |

</details>


<details>
<summary><h2>DS-2CFWQ6-D - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.110 | Applied to: [DS-2CFWQ6-D(2.8+4mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.110_260421_S3000717992.zip) | 2025-07-25 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.110_260421_S3000717992.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202509/releasenote%5CNetwork_Camera-V5.8.100_250725_Release_Note-E12.pdf) |

</details>


<details>
<summary><h2>DS-2CV1021G0-IDW - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.821 | Applied to: [DS-2CV1021G0-IDW1(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.821_231108_S3000539548.zip)(D) | 2023-11-08 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.821_231108_S3000539548.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202404/1712790066963/releasenote%5CIPC_E6_5.5.821_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CV1023G2-LIDW - UNKNOWN (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.23 | Applied to: [DS-2CV1023G2-LIDWF(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.23_260403_S3000712869.zip)(B) | 2026-04-03 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.23_260403_S3000712869.zip) |  |
| 5.8.22 | Applied to: [DS-2CV1023G2-LIDWF(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.22_250708_S3000661562.zip)(B) | 2025-07-08 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.22_250708_S3000661562.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202508/releasenote%5CNetwork_Camera-V5.8.22_250708_Release_Note-E9.pdf) |

</details>


<details>
<summary><h2>DS-2CV1043G2-LIDW - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.22 | Applied to: [DS-2CV1043G2-LIDWF(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.22_250708_S3000661562.zip)(B) | 2025-07-08 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.22_250708_S3000661562.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202508/releasenote%5CNetwork_Camera-V5.8.22_250708_Release_Note-E10.pdf) |

</details>


<details>
<summary><h2>DS-2CV1F23G2-LIDWF - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.22 | Applied to: [DS-2CV1F23G2-LIDWF(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.22_250708_S3000661562.zip)(B) | 2025-07-08 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.22_250708_S3000661562.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202508/releasenote%5CNetwork_Camera-V5.8.22_250708_Release_Note-E9.pdf) |

</details>


<details>
<summary><h2>DS-2CV1F43G2-LIDWF - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.22 | Applied to: [DS-2CV1F43G2-LIDWF(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.22_250708_S3000661562.zip)(B) | 2025-07-08 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.22_250708_S3000661562.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202508/releasenote%5CNetwork_Camera-V5.8.22_250708_Release_Note-E10.pdf) |

</details>


<details>
<summary><h2>DS-2CV2021G2-IDW - UNKNOWN (3 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.24 | Applied to: [DS-2CV2021G2-IDW(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.24_250828_S3000671925.zip) | 2025-08-28 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.24_250828_S3000671925.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202404/1712790066963/releasenote%5CIPC_E6_5.5.821_Release_Note.pdf) |
| 5.5.821 | Applied to: [DS-2CV2021G2-IDW(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.821_231108_S3000539548.zip) | 2023-11-08 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.821_231108_S3000539548.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202404/1712790066963/releasenote%5CIPC_E6_5.5.821_Release_Note.pdf) |
| 5.5.803 | Applied to: [DS-2CV2021G2-IDW(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/e037f86a-4a71-43a9-9297-c597d9bca538.zip) | 2021-08-17 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/e037f86a-4a71-43a9-9297-c597d9bca538.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202404/1712790066963/releasenote%5CIPC_E6_5.5.821_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CV2026G0-IDW - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.820 | Applied to: [DS-2CV2026G0-IDW(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.820_260410_S3000715634.zip)(D) | 2023-11-20 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.820_260410_S3000715634.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202401/releasenote%5CNetwork_Camera-V5.5.820_Release_Note-G6.pdf) |

</details>


<details>
<summary><h2>DS-2CV2027G0-LDW - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.820 | Applied to: [DS-2CV2027G0-LDW(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.820_260410_S3000715634.zip) | 2023-11-20 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.820_260410_S3000715634.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202401/releasenote%5CNetwork_Camera-V5.5.820_Release_Note-G6.pdf) |

</details>


<details>
<summary><h2>DS-2CV2041G2-IDW - UNKNOWN (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.24 | Applied to: [DS-2CV2041G2-IDW(4mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.24_250828_S3000671925.zip)(D) | 2025-08-28 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.24_250828_S3000671925.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202401/releasenote%5CNetwork_Camera-V5.5.820_Release_Note-G6.pdf) |
| 5.5.820 | Applied to: [DS-2CV2041G2-IDW(4mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.820_260410_S3000715634.zip)(D) | 2023-11-20 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.820_260410_S3000715634.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202401/releasenote%5CNetwork_Camera-V5.5.820_Release_Note-G6.pdf) |

</details>


<details>
<summary><h2>DS-2CV2046G0-IDW - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.820 | Applied to: [DS-2CV2046G0-IDW(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.820_260410_S3000715634.zip)(D) | 2023-11-20 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.820_260410_S3000715634.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202401/releasenote%5CNetwork_Camera-V5.5.820_Release_Note-G6.pdf) |

</details>


<details>
<summary><h2>DS-2CV2126G0-IDW - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.820 | Applied to: [DS-2CV2126G0-IDW(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.820_260410_S3000715634.zip) | 2023-11-20 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.820_260410_S3000715634.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202401/releasenote%5CNetwork_Camera-V5.5.820_Release_Note-G6.pdf) |

</details>


<details>
<summary><h2>DS-2CV2141G2-IDW - UNKNOWN (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.24 | Applied to: [DS-2CV2141G2-IDW(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.24_250828_S3000671925.zip) | 2025-08-28 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.24_250828_S3000671925.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202511/releasenote%5CNetwork_Camera-V5.7.24_SP1_Release_Note-E8.pdf) |
| 5.5.800 | Applied to: [DS-2CV2141G2-IDW(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.800_211009_S3000390724.zip) | 2021-08-16 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.800_211009_S3000390724.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202511/releasenote%5CNetwork_Camera-V5.7.24_SP1_Release_Note-E8.pdf) |

</details>


<details>
<summary><h2>DS-2CV2146G0-IDW - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.820 | Applied to: [DS-2CV2146G0-IDW(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.820_260410_S3000715634.zip) | 2023-11-20 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.820_260410_S3000715634.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202401/releasenote%5CNetwork_Camera-V5.5.820_Release_Note-G6.pdf) |

</details>


<details>
<summary><h2>DS-2CV2Q21FD-IW - UNKNOWN (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.821 | Applied to: [DS-2CV2Q21FD-IW(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.821_231108_S3000539548.zip) | 2023-11-08 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.821_231108_S3000539548.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202404/1712790068455/releasenote%5CIPC_E6_5.5.821_Release_Note.pdf) |
| 5.4.800 | Applied to: [DS-2CV2Q21FD-IW(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/6005351b-ceff-48af-bb0a-5e671137820c.zip) | 2021-10-20 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/6005351b-ceff-48af-bb0a-5e671137820c.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202404/1712790068455/releasenote%5CIPC_E6_5.5.821_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CV2U32G1-IW - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.4.71 | Applied to: [DS-2CV2U32G1-IDW(1.68mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.4.71_181129_S3000260066.zip) | 2018-11-29 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.4.71_181129_S3000260066.zip) |  |

</details>


<details>
<summary><h2>DS-2DB4223I-CX - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.7 | Applied to: [DS-2DB4223I-CX(T5/316L)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.7_260410_S3000716682.zip) | 2023-11-17 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.7_260410_S3000716682.zip) |  |

</details>


<details>
<summary><h2>DS-2DB4236I-CWX - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.7 | Applied to: [DS-2DB4236I-CWX(T5/316L)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.7_260410_S3000716682.zip) | 2023-11-17 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.7_260410_S3000716682.zip) |  |

</details>


<details>
<summary><h2>DS-2DE2A204IW-DE3 - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.30 | Applied to: [DS-2DE2A204IW-DE3/W(C0)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.30_250729_S3000670024.zip)(S6)(C) | 2025-07-29 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.30_250729_S3000670024.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202511/releasenote%5CV5.7.30_250729_Release_Note.pdf) |
| 5.7.11 | Applied to: [DS-2DE2A204IW-DE3(C0)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.11_260413_S3000716685.zip)(S6)(C) | 2023-06-12 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.11_260413_S3000716685.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202312/releasenote%5CRelease_Note_E7_V5.7.11_230612.pdf) |

</details>


<details>
<summary><h2>DS-2DE2A204IWG1-E - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.9.2 | Applied to: [DS-2DE2A204IWG1-E/W](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.9.2_260416_S3000716258.zip) | 2026-02-08 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.9.2_260416_S3000716258.zip) |  |
| 5.9.5 | Applied to: [DS-2DE2A204IWG1-E](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.9.5_260416_S3000716247.zip) | 2026-01-29 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.9.5_260416_S3000716247.zip) |  |

</details>


<details>
<summary><h2>DS-2DE2A204IWG1-E-W - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.9.2 | [DS-2DE2A204IWG1-E-W](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.9.2_260416_S3000716258.zip) | 2026-04-16 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.9.2_260416_S3000716258.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202604/releasenote%5CV5.9.2_260416_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2DE2A404IW-DE3 - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.30 | Applied to: [DS-2DE2A404IW-DE3/W(C0)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.30_250729_S3000670024.zip)(S6)(C) | 2025-07-29 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.30_250729_S3000670024.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202511/releasenote%5CV5.7.30_250729_Release_Note.pdf) |
| 5.7.11 | Applied to: [DS-2DE2A404IW-DE3(C0)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.11_260413_S3000716685.zip)(S6)(C) | 2023-06-12 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.11_260413_S3000716685.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202312/releasenote%5CRelease_Note_E7_V5.7.11_230612.pdf) |

</details>


<details>
<summary><h2>DS-2DE2A404IWG1-E - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.9.2 | Applied to: [DS-2DE2A404IWG1-E/W](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.9.2_260416_S3000716258.zip) | 2026-02-08 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.9.2_260416_S3000716258.zip) |  |
| 5.9.5 | Applied to: [DS-2DE2A404IWG1-E](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.9.5_260416_S3000716247.zip) | 2026-01-29 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.9.5_260416_S3000716247.zip) |  |

</details>


<details>
<summary><h2>DS-2DE2A404IWG1-E-W - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.9.2 | [DS-2DE2A404IWG1-E-W](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.9.2_260416_S3000716258.zip) | 2026-04-16 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.9.2_260416_S3000716258.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202604/releasenote%5CV5.9.2_260416_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2DE2A604IWG1-E - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.9.2 | Applied to: [DS-2DE2A604IWG1-E/W](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.9.2_260416_S3000716258.zip) | 2026-02-08 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.9.2_260416_S3000716258.zip) |  |
| 5.9.5 | Applied to: [DS-2DE2A604IWG1-E](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.9.5_260416_S3000716247.zip) | 2026-01-29 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.9.5_260416_S3000716247.zip) |  |

</details>


<details>
<summary><h2>DS-2DE2A604IWG1-E-W - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.9.2 | [DS-2DE2A604IWG1-E-W](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.9.2_260416_S3000716258.zip) | 2026-04-16 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.9.2_260416_S3000716258.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202604/releasenote%5CV5.9.2_260416_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2DE2C200MW-DE - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2DE2C200MW-DE(F0)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip)(S7) | 2024-12-11 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_260114_S3000702187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202507/releasenote%5CNetwork_Camera-V5.7.23_SP2_Release_Note-E8.pdf) |

</details>


<details>
<summary><h2>DS-2DE2C200MWG - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.23 | Applied to: [DS-2DE2C200MWG/W(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.23_260403_S3000712869.zip) | 2025-08-20 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.23_260403_S3000712869.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.8.23_Release_Note-E9_E10.pdf) |

</details>


<details>
<summary><h2>DS-2DE2C200MWG-4G - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.34 | Applied to: [DS-2DE2C200MWG-4G(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.34_250908_S3000674302.zip) | 2025-09-08 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.34_250908_S3000674302.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202511/releasenote%5CNetwork_Camera-V5.8.34_Release_Note-E9_E10.pdf) |

</details>


<details>
<summary><h2>DS-2DE2C200MWG-E - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.21 | Applied to: [DS-2DE2C200MWG-E(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.21_250714_S3000661481.zip) | 2025-07-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.21_250714_S3000661481.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202508/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-E9.pdf) |

</details>


<details>
<summary><h2>DS-2DE2C200SCG-E - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.20 | Applied to: [DS-2DE2C200SCG-E(F0)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.20_230630_S3000509422.zip) | 2023-06-30 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.20_230630_S3000509422.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202312/releasenote%5CNetwork_Camera-V5.7.20_SP4_Release_Note-E8.pdf) |

</details>


<details>
<summary><h2>DS-2DE2C400MW-DE - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.20 | Applied to: [DS-2DE2C400MW-DE(F0)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.20_230630_S3000509422.zip)(S7) | 2023-06-30 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.20_230630_S3000509422.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202312/releasenote%5CNetwork_Camera-V5.7.20_SP4_Release_Note-E8.pdf) |

</details>


<details>
<summary><h2>DS-2DE2C400MWG - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.23 | Applied to: [DS-2DE2C400MWG/W(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.23_260403_S3000712869.zip) | 2025-08-20 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.23_260403_S3000712869.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.8.23_Release_Note-E9_E10.pdf) |

</details>


<details>
<summary><h2>DS-2DE2C400MWG-4G - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.34 | Applied to: [DS-2DE2C400MWG-4G(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.34_250908_S3000674302.zip) | 2025-09-08 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.34_250908_S3000674302.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.8.34_250908_Release_Note-IPCE_GL_E10.pdf) |

</details>


<details>
<summary><h2>DS-2DE2C400MWG-E - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.10 | Applied to: [DS-2DE2C400MWG-E(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.100_260416_S3000716492.zip) | 2025-07-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.100_260416_S3000716492.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202508/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-E10.pdf) |

</details>


<details>
<summary><h2>DS-2DE2C400SCG-E - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.20 | Applied to: [DS-2DE2C400SCG-E(F0)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.20_230630_S3000509422.zip) | 2023-06-30 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.20_230630_S3000509422.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202312/releasenote%5CNetwork_Camera-V5.7.20_SP4_Release_Note-E8.pdf) |

</details>


<details>
<summary><h2>DS-2DE2C600MWG-E - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.1 | Applied to: [DS-2DE2C600MWG-E(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.12_260416_S3000716519.zip) | 2025-01-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.12_260416_S3000716519.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CV5.8.1_250114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2DE3204W-DE - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.1 | Applied to: [DS-2DE3204W-DE(T5)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.12_260416_S3000716519.zip) | 2023-11-08 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.12_260416_S3000716519.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202408/releasenote%5CIPDE_C_H8_V5.8.1_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2DE3A400BW-DE - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.0 | Applied to: [DS-2DE3A400BW-DE(F1)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.0_231109_S3000541088.zip)(T5) | 2023-11-09 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.0_231109_S3000541088.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202408/releasenote%5CRelease_Note_IPDE_H8_5.8.0_231109.pdf) |

</details>


<details>
<summary><h2>DS-2DE3A404IW-DE - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.12 | Applied to: [DS-2DE3A404IW-DE(S6)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.12_220907_S3000453567.zip) | 2022-09-07 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.12_220907_S3000453567.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202408/releasenote%5CIPDE_E7_V5.7.12_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2DE3A404IWG-E - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.0 | Applied to: [DS-2DE3A404IWG-E/W](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.0_231109_S3000541088.zip) | 2023-11-09 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.0_231109_S3000541088.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202408/releasenote%5CRelease_Note_IPDE_H8_5.8.0_231109.pdf) |

</details>


<details>
<summary><h2>DS-2DE4215IW-DE - IPC_G0 (4 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.12 | Applied to: [DS-2DE4215IW-DE(T5)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.12_260416_S3000716519.zip) | 2025-09-15 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.12_260416_S3000716519.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202510/releasenote%5CV5.8.12_250915_Release_Note.pdf) |
| 5.7.11 | Applied to: [DS-2DE4215IW-DE(S6)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.11_260413_S3000716685.zip) | 2022-09-05 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.11_260413_S3000716685.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202312/releasenote%5CV5.7.11_Release_Note--E7.pdf) |
| 5.5.800 | Applied to: [DS-2DE4215IW-DE(S5)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.800_211009_S3000390724.zip) | 2021-06-28 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.800_211009_S3000390724.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/4cdf7c64-e179-4c02-a3ae-ec999c2710e9.pdf) |
| 5.6.18 | Applied to: [DS-2DE4215IW-DE(E)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/2d8cfccf-08c0-4b96-8dd4-9396e1383825.zip) | 2021-04-28 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/2d8cfccf-08c0-4b96-8dd4-9396e1383825.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202507/releasenote%5CRelease_Note.pdf) |

</details>


<details>
<summary><h2>DS-2DE4215IWG-E - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.10 | Applied to: [DS-2DE4215IWG-E(B)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.100_260416_S3000716492.zip) | 2024-04-03 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.100_260416_S3000716492.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202408/releasenote%5CIDPE_L_H8_V5.8.10_240403_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2DE4215IWG1-E - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.1 | Applied to: [DS-2DE4215IWG1-E](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.12_260416_S3000716519.zip) | 2026-01-15 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.12_260416_S3000716519.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202603/releasenote%5CV5.8.1_260115_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2DE4215W-DE - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.6.17 | Applied to: [DS-2DE4215W-DE(E)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/7e8b3eb3-ee90-4e13-a100-e57d971016f9.zip) | 2021-04-11 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/7e8b3eb3-ee90-4e13-a100-e57d971016f9.zip) |  |

</details>


<details>
<summary><h2>DS-2DE4225IW-DE - IPC_G0 (3 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.12 | Applied to: [DS-2DE4225IW-DE(T5)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.12_260416_S3000716519.zip) | 2025-09-15 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.12_260416_S3000716519.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202510/releasenote%5CV5.8.12_250915_Release_Note.pdf) |
| 5.7.11 | Applied to: [DS-2DE4225IW-DE(S6)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.11_260413_S3000716685.zip) | 2022-09-05 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.11_260413_S3000716685.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202312/releasenote%5CV5.7.11_Release_Note--E7.pdf) |
| 5.6.18 | Applied to: [DS-2DE4225IW-DE(E)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/2d8cfccf-08c0-4b96-8dd4-9396e1383825.zip) | 2021-04-28 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/2d8cfccf-08c0-4b96-8dd4-9396e1383825.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202507/releasenote%5CRelease_Note.pdf) |

</details>


<details>
<summary><h2>DS-2DE4225IWG-E - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.10 | Applied to: [DS-2DE4225IWG-E(B)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.100_260416_S3000716492.zip) | 2024-04-03 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.100_260416_S3000716492.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202408/releasenote%5CIDPE_L_H8_V5.8.10_240403_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2DE4225IWG1-E - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.1 | Applied to: [DS-2DE4225IWG1-E](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.12_260416_S3000716519.zip) | 2026-01-15 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.12_260416_S3000716519.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202603/releasenote%5CV5.8.1_260115_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2DE4225W-DE - IPC_G0 (3 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.11 | Applied to: [DS-2DE4225W-DE(S6)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.11_260413_S3000716685.zip) | 2022-09-05 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.11_260413_S3000716685.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202312/releasenote%5CV5.7.11_Release_Note--E7.pdf) |
| 5.6.18 | Applied to: [DS-2DE4225W-DE(B)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/2d8cfccf-08c0-4b96-8dd4-9396e1383825.zip) | 2021-04-28 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/2d8cfccf-08c0-4b96-8dd4-9396e1383825.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202507/releasenote%5CRelease_Note.pdf) |
| 5.6.14 | Applied to: [DS-2DE4225W-DE(B)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/6d583cfc-1b98-4ee8-973c-2fad9724b521.zip) | 2019-08-26 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/6d583cfc-1b98-4ee8-973c-2fad9724b521.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202507/releasenote%5CRelease_Note.pdf) |

</details>


<details>
<summary><h2>DS-2DE4225W-DE3 - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.11 | Applied to: [DS-2DE4225W-DE3(S6)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.11_260413_S3000716685.zip) | 2022-09-05 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.11_260413_S3000716685.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202312/releasenote%5CV5.7.11_Release_Note--E7.pdf) |
| 5.6.18 | Applied to: [DS-2DE4225W-DE3(B)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/2d8cfccf-08c0-4b96-8dd4-9396e1383825.zip) | 2021-04-28 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/2d8cfccf-08c0-4b96-8dd4-9396e1383825.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202507/releasenote%5CRelease_Note.pdf) |

</details>


<details>
<summary><h2>DS-2DE4225WG-E3 - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.0 | Applied to: [DS-2DE4225WG-E3](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.0_231109_S3000541088.zip) | 2023-11-09 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.0_231109_S3000541088.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202408/releasenote%5CRelease_Note_IPDE_H8_5.8.0_231109.pdf) |

</details>


<details>
<summary><h2>DS-2DE4225WG1-E3 - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.1 | Applied to: [DS-2DE4225WG1-E3](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.12_260416_S3000716519.zip) | 2026-01-15 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.12_260416_S3000716519.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202603/releasenote%5CV5.8.1_260115_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2DE4415IW-DE - IPC_G0 (4 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.12 | Applied to: [DS-2DE4415IW-DE(T5)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.12_260416_S3000716519.zip) | 2025-09-15 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.12_260416_S3000716519.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202510/releasenote%5CV5.8.12_250915_Release_Note.pdf) |
| 5.7.11 | Applied to: [DS-2DE4415IW-DE(S6)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.11_260413_S3000716685.zip) | 2022-09-05 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.11_260413_S3000716685.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202312/releasenote%5CV5.7.11_Release_Note--E7.pdf) |
| 5.5.800 | Applied to: [DS-2DE4415IW-DE(S5)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.800_211009_S3000390724.zip) | 2021-06-28 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.800_211009_S3000390724.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/4cdf7c64-e179-4c02-a3ae-ec999c2710e9.pdf) |
| 5.6.18 | Applied to: [DS-2DE4415IW-DE(E)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/2d8cfccf-08c0-4b96-8dd4-9396e1383825.zip) | 2021-04-28 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/2d8cfccf-08c0-4b96-8dd4-9396e1383825.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202507/releasenote%5CRelease_Note.pdf) |

</details>


<details>
<summary><h2>DS-2DE4415IWG-E - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.10 | Applied to: [DS-2DE4415IWG-E(B)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.100_260416_S3000716492.zip) | 2024-04-03 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.100_260416_S3000716492.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202408/releasenote%5CIDPE_L_H8_V5.8.10_240403_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2DE4415IWG1-E - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.1 | Applied to: [DS-2DE4415IWG1-E](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.12_260416_S3000716519.zip) | 2026-01-15 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.12_260416_S3000716519.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202603/releasenote%5CV5.8.1_260115_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2DE4425IW-DE - IPC_G0 (4 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.12 | Applied to: [DS-2DE4425IW-DE(T5)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.12_260416_S3000716519.zip) | 2025-09-15 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.12_260416_S3000716519.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202510/releasenote%5CV5.8.12_250915_Release_Note.pdf) |
| 5.7.11 | Applied to: [DS-2DE4425IW-DE(S6)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.11_260413_S3000716685.zip) | 2022-09-05 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.11_260413_S3000716685.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202312/releasenote%5CV5.7.11_Release_Note--E7.pdf) |
| 5.5.800 | Applied to: [DS-2DE4425IW-DE(S5)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.800_211009_S3000390724.zip) | 2021-06-28 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.800_211009_S3000390724.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/4cdf7c64-e179-4c02-a3ae-ec999c2710e9.pdf) |
| 5.6.18 | Applied to: [DS-2DE4425IW-DE(E)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/2d8cfccf-08c0-4b96-8dd4-9396e1383825.zip) | 2021-04-28 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/2d8cfccf-08c0-4b96-8dd4-9396e1383825.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202507/releasenote%5CRelease_Note.pdf) |

</details>


<details>
<summary><h2>DS-2DE4425IWG-E - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.10 | Applied to: [DS-2DE4425IWG-E(B)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.100_260416_S3000716492.zip) | 2024-04-03 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.100_260416_S3000716492.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202408/releasenote%5CIDPE_L_H8_V5.8.10_240403_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2DE4425IWG1-E - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.1 | Applied to: [DS-2DE4425IWG1-E](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.12_260416_S3000716519.zip) | 2026-01-15 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.12_260416_S3000716519.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202603/releasenote%5CV5.8.1_260115_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2DE4425W-DE - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.11 | Applied to: [DS-2DE4425W-DE(S6)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.11_260413_S3000716685.zip) | 2022-09-05 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.11_260413_S3000716685.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202312/releasenote%5CV5.7.11_Release_Note--E7.pdf) |
| 5.6.18 | Applied to: [DS-2DE4425W-DE(E)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/2d8cfccf-08c0-4b96-8dd4-9396e1383825.zip) | 2021-04-28 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/2d8cfccf-08c0-4b96-8dd4-9396e1383825.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202507/releasenote%5CRelease_Note.pdf) |

</details>


<details>
<summary><h2>DS-2DE4425W-DE3 - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.11 | Applied to: [DS-2DE4425W-DE3(S6)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.11_260413_S3000716685.zip) | 2022-09-05 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.11_260413_S3000716685.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202312/releasenote%5CV5.7.11_Release_Note--E7.pdf) |

</details>


<details>
<summary><h2>DS-2DE4425WG1-E3 - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.1 | Applied to: [DS-2DE4425WG1-E3](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.12_260416_S3000716519.zip) | 2026-01-15 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.12_260416_S3000716519.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202603/releasenote%5CV5.8.1_260115_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2DE4825IWG1-E - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.1 | Applied to: [DS-2DE4825IWG1-E](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.12_260416_S3000716519.zip) | 2026-01-15 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.12_260416_S3000716519.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202603/releasenote%5CV5.8.1_260115_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2DE4A204IW-DE - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.6.18 | Applied to: [DS-2DE4A204IW-DE(2.8-12mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/1d3851bc-8d3e-4383-82cf-35c9dd35805d.zip) | 2021-06-22 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/1d3851bc-8d3e-4383-82cf-35c9dd35805d.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202507/releasenote%5CRelease_Note.pdf) |

</details>


<details>
<summary><h2>DS-2DE4A225IW-DE - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.11 | Applied to: [DS-2DE4A225IW-DE(S6)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.11_260413_S3000716685.zip) | 2023-06-12 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.11_260413_S3000716685.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202312/releasenote%5CRelease_Note_E7_V5.7.11_230612.pdf) |
| 5.6.18 | Applied to: [DS-2DE4A225IW-DE(B)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/1d3851bc-8d3e-4383-82cf-35c9dd35805d.zip) | 2021-06-22 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/1d3851bc-8d3e-4383-82cf-35c9dd35805d.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202507/releasenote%5CRelease_Note.pdf) |

</details>


<details>
<summary><h2>DS-2DE4A225IWG-E - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.0 | Applied to: [DS-2DE4A225IWG-E](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.0_231109_S3000541088.zip) | 2023-11-09 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.0_231109_S3000541088.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202408/releasenote%5CRelease_Note_IPDE_H8_5.8.0_231109.pdf) |

</details>


<details>
<summary><h2>DS-2DE4A225IWG1-E - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.1 | Applied to: [DS-2DE4A225IWG1-E](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.12_260416_S3000716519.zip) | 2026-01-15 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.12_260416_S3000716519.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202603/releasenote%5CV5.8.1_260115_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2DE4A425IW-DE - IPC_G0 (3 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.11 | Applied to: [DS-2DE4A425IW-DE(S6)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.11_260413_S3000716685.zip) | 2023-06-12 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.11_260413_S3000716685.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202312/releasenote%5CRelease_Note_E7_V5.7.11_230612.pdf) |
| 5.6.18 | Applied to: [DS-2DE4A425IW-DE](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/1d3851bc-8d3e-4383-82cf-35c9dd35805d.zip) | 2021-06-22 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/1d3851bc-8d3e-4383-82cf-35c9dd35805d.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202507/releasenote%5CRelease_Note.pdf) |
| 5.6.14 | Applied to: [DS-2DE4A425IW-DE](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/6d583cfc-1b98-4ee8-973c-2fad9724b521.zip) | 2019-08-26 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/6d583cfc-1b98-4ee8-973c-2fad9724b521.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202507/releasenote%5CRelease_Note.pdf) |

</details>


<details>
<summary><h2>DS-2DE4A425IWG1-E - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.1 | Applied to: [DS-2DE4A425IWG1-E](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.12_260416_S3000716519.zip) | 2026-01-15 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.12_260416_S3000716519.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202603/releasenote%5CV5.8.1_260115_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2DE5225IW-AE - IPC_G0 (4 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.11 | Applied to: [DS-2DE5225IW-AE(S6)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.11_260413_S3000716685.zip) | 2023-06-12 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.11_260413_S3000716685.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202312/releasenote%5CRelease_Note_E7_V5.7.11_230612.pdf) |
| 5.5.800 | Applied to: [DS-2DE5225IW-AE(S5)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.800_211009_S3000390724.zip) | 2021-06-28 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.800_211009_S3000390724.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/4cdf7c64-e179-4c02-a3ae-ec999c2710e9.pdf) |
| 5.6.18 | Applied to: [DS-2DE5225IW-AE(C)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/2d8cfccf-08c0-4b96-8dd4-9396e1383825.zip) | 2021-04-28 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/2d8cfccf-08c0-4b96-8dd4-9396e1383825.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202507/releasenote%5CRelease_Note.pdf) |
| 5.6.14 | Applied to: [DS-2DE5225IW-AE(C)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/6d583cfc-1b98-4ee8-973c-2fad9724b521.zip) | 2019-08-26 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/6d583cfc-1b98-4ee8-973c-2fad9724b521.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202507/releasenote%5CRelease_Note.pdf) |

</details>


<details>
<summary><h2>DS-2DE5225W-AE - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.12 | Applied to: [DS-2DE5225W-AE(T5)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.12_260416_S3000716519.zip) | 2025-09-15 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.12_260416_S3000716519.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202510/releasenote%5CV5.8.12_250915_Release_Note.pdf) |
| 5.6.14 | Applied to: [DS-2DE5225W-AE](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/6d583cfc-1b98-4ee8-973c-2fad9724b521.zip) | 2019-08-26 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/6d583cfc-1b98-4ee8-973c-2fad9724b521.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202507/releasenote%5CRelease_Note.pdf) |

</details>


<details>
<summary><h2>DS-2DE5225W-AE3 - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.12 | Applied to: [DS-2DE5225W-AE3(T5)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.12_260416_S3000716519.zip) | 2025-09-15 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.12_260416_S3000716519.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202510/releasenote%5CV5.8.12_250915_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2DE5232IW-AE - IPC_G0 (3 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.11 | Applied to: [DS-2DE5232IW-AE(S6)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.11_260413_S3000716685.zip) | 2023-06-12 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.11_260413_S3000716685.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202312/releasenote%5CRelease_Note_E7_V5.7.11_230612.pdf) |
| 5.5.820 | Applied to: [DS-2DE5232IW-AE(S5)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.820_260410_S3000715634.zip) | 2022-05-25 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.820_260410_S3000715634.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202312/releasenote%5CPTZ_V5.5.820_Release_Note.pdf) |
| 5.6.18 | Applied to: [DS-2DE5232IW-AE(E)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/2d8cfccf-08c0-4b96-8dd4-9396e1383825.zip) | 2021-04-28 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/2d8cfccf-08c0-4b96-8dd4-9396e1383825.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202507/releasenote%5CRelease_Note.pdf) |

</details>


<details>
<summary><h2>DS-2DE5232W-AE - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.11 | Applied to: [DS-2DE5232W-AE(S6)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.11_260413_S3000716685.zip) | 2023-06-12 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.11_260413_S3000716685.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202312/releasenote%5CRelease_Note_E7_V5.7.11_230612.pdf) |
| 5.6.18 | Applied to: [DS-2DE5232W-AE(E)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/2d8cfccf-08c0-4b96-8dd4-9396e1383825.zip) | 2021-04-28 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/2d8cfccf-08c0-4b96-8dd4-9396e1383825.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202507/releasenote%5CRelease_Note.pdf) |

</details>


<details>
<summary><h2>DS-2DE5232W-AE3 - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.12 | Applied to: [DS-2DE5232W-AE3(T5)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.12_260416_S3000716519.zip) | 2025-09-15 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.12_260416_S3000716519.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202510/releasenote%5CV5.8.12_250915_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2DE5330W-AE - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.6.14 | Applied to: [DS-2DE5330W-AE(B)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/6d583cfc-1b98-4ee8-973c-2fad9724b521.zip) | 2019-08-26 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/6d583cfc-1b98-4ee8-973c-2fad9724b521.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202507/releasenote%5CRelease_Note.pdf) |

</details>


<details>
<summary><h2>DS-2DE5330W-AE3 - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.6.14 | Applied to: [DS-2DE5330W-AE3](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/6d583cfc-1b98-4ee8-973c-2fad9724b521.zip) | 2019-08-26 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/6d583cfc-1b98-4ee8-973c-2fad9724b521.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202507/releasenote%5CRelease_Note.pdf) |

</details>


<details>
<summary><h2>DS-2DE5425IW-AE - IPC_G0 (4 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.12 | Applied to: [DS-2DE5425IW-AE(T5)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.12_260416_S3000716519.zip) | 2025-09-15 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.12_260416_S3000716519.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202510/releasenote%5CV5.8.12_250915_Release_Note.pdf) |
| 5.7.11 | Applied to: [DS-2DE5425IW-AE(S6)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.11_260413_S3000716685.zip) | 2023-06-12 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.11_260413_S3000716685.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202312/releasenote%5CRelease_Note_E7_V5.7.11_230612.pdf) |
| 5.5.800 | Applied to: [DS-2DE5425IW-AE(S5)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.800_211009_S3000390724.zip) | 2021-06-28 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.800_211009_S3000390724.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/4cdf7c64-e179-4c02-a3ae-ec999c2710e9.pdf) |
| 5.6.14 | Applied to: [DS-2DE5425IW-AE(C)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/6d583cfc-1b98-4ee8-973c-2fad9724b521.zip) | 2019-08-26 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/6d583cfc-1b98-4ee8-973c-2fad9724b521.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202507/releasenote%5CRelease_Note.pdf) |

</details>


<details>
<summary><h2>DS-2DE5425IWG-E - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.10 | Applied to: [DS-2DE5425IWG-E(B)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.100_260416_S3000716492.zip) | 2024-04-03 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.100_260416_S3000716492.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202408/releasenote%5CIDPE_L_H8_V5.8.10_240403_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2DE5425IWG1-E - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.1 | Applied to: [DS-2DE5425IWG1-E](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.12_260416_S3000716519.zip) | 2026-01-15 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.12_260416_S3000716519.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202603/releasenote%5CV5.8.1_260115_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2DE5425WG1-E - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.1 | Applied to: [DS-2DE5425WG1-E](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.12_260416_S3000716519.zip) | 2026-01-15 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.12_260416_S3000716519.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202603/releasenote%5CV5.8.1_260115_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2DE5432IW-AE - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.820 | Applied to: [DS-2DE5432IW-AE(S5)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.820_260410_S3000715634.zip) | 2022-05-25 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.820_260410_S3000715634.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202312/releasenote%5CPTZ_V5.5.820_Release_Note.pdf) |
| 5.6.14 | Applied to: [DS-2DE5432IW-AE(B)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/4ab6dd7a-1bbb-4423-afb6-0c529edc5bd2.zip) | 2019-12-04 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/4ab6dd7a-1bbb-4423-afb6-0c529edc5bd2.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202507/releasenote%5CRelease_Note.pdf) |

</details>


<details>
<summary><h2>DS-2DE5432IWG-E - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.10 | Applied to: [DS-2DE5432IWG-E(B)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.100_260416_S3000716492.zip) | 2024-04-03 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.100_260416_S3000716492.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202408/releasenote%5CIDPE_L_H8_V5.8.10_240403_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2DE5432IWG1-E - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.1 | Applied to: [DS-2DE5432IWG1-E](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.12_260416_S3000716519.zip) | 2026-01-15 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.12_260416_S3000716519.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202603/releasenote%5CV5.8.1_260115_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2DE5432WG1-E - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.1 | Applied to: [DS-2DE5432WG1-E](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.12_260416_S3000716519.zip) | 2026-01-15 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.12_260416_S3000716519.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202603/releasenote%5CV5.8.1_260115_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2DE7225IW-AE - IPC_G0 (3 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.11 | Applied to: [DS-2DE7225IW-AE(S6)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.11_260413_S3000716685.zip) | 2022-09-05 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.11_260413_S3000716685.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202312/releasenote%5CV5.7.11_Release_Note--E7.pdf) |
| 5.5.800 | Applied to: [DS-2DE7225IW-AE(S5)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.800_211009_S3000390724.zip) | 2021-06-28 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.800_211009_S3000390724.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/4cdf7c64-e179-4c02-a3ae-ec999c2710e9.pdf) |
| 5.6.18 | Applied to: [DS-2DE7225IW-AE(B)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/2d8cfccf-08c0-4b96-8dd4-9396e1383825.zip) | 2021-04-28 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/2d8cfccf-08c0-4b96-8dd4-9396e1383825.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202507/releasenote%5CRelease_Note.pdf) |

</details>


<details>
<summary><h2>DS-2DE7232IW-AE - IPC_G0 (3 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.800 | Applied to: [DS-2DE7232IW-AE(S5)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.800_211009_S3000390724.zip) | 2021-06-28 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.800_211009_S3000390724.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/4cdf7c64-e179-4c02-a3ae-ec999c2710e9.pdf) |
| 5.6.18 | Applied to: [DS-2DE7232IW-AE](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/2d8cfccf-08c0-4b96-8dd4-9396e1383825.zip) | 2021-04-28 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/2d8cfccf-08c0-4b96-8dd4-9396e1383825.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202312/releasenote%5CPTZ_Camera_V5.6.0_Release_Note_--R7.pdf) |
| 5.6.0 | Applied to: [DS-2DE7232IW-AE](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/10aa0b1e-cc23-4cbd-8165-f40e222950e7.zip) | 2019-01-28 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/10aa0b1e-cc23-4cbd-8165-f40e222950e7.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202312/releasenote%5CPTZ_Camera_V5.6.0_Release_Note_--R7.pdf) |

</details>


<details>
<summary><h2>DS-2DE7425IW-AE - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.6.18 | Applied to: [DS-2DE7425IW-AE(B)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/2d8cfccf-08c0-4b96-8dd4-9396e1383825.zip) | 2021-04-28 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/2d8cfccf-08c0-4b96-8dd4-9396e1383825.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202507/releasenote%5CRelease_Note.pdf) |

</details>


<details>
<summary><h2>DS-2DE7A225IWG-EB-SL - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.13 | [DS-2DE7A225IWG-EB-SL](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.13_260422_S3000719553.zip) | 2026-04-22 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.13_260422_S3000719553.zip) |  |

</details>


<details>
<summary><h2>DS-2DE7A232IWG-EB-SL - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.13 | [DS-2DE7A232IWG-EB-SL](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.13_260422_S3000719553.zip) | 2026-04-22 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.13_260422_S3000719553.zip) |  |

</details>


<details>
<summary><h2>DS-2DF4220-DX-S6-316L- - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.11 | [DS-2DF4220-DX-S6-316L-](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.11_260413_S3000716685.zip) | 2026-04-13 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.11_260413_S3000716685.zip) |  |

</details>


<details>
<summary><h2>DS-2DF4220-DX-S6-316L--C- - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.11 | [DS-2DF4220-DX-S6-316L--C-](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.11_260413_S3000716685.zip) | 2026-04-13 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.11_260413_S3000716685.zip) |  |

</details>


<details>
<summary><h2>DS-2DF4420-DX-304--E- - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.9.3 | [DS-2DF4420-DX-304--E-](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.9.3_260417_S3000717323.zip) | 2026-04-17 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.9.3_260417_S3000717323.zip) |  |

</details>


<details>
<summary><h2>DS-2DF4420-DX-316L--E- - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.9.3 | [DS-2DF4420-DX-316L--E-](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.9.3_260417_S3000717323.zip) | 2026-04-17 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.9.3_260417_S3000717323.zip) |  |

</details>


<details>
<summary><h2>DS-2DF4420-DX-S6--C--304- - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.11 | [DS-2DF4420-DX-S6--C--304-](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.11_260413_S3000716685.zip) | 2026-04-13 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.11_260413_S3000716685.zip) |  |

</details>


<details>
<summary><h2>DS-2DF4420-DX-S6-316L--C- - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.11 | [DS-2DF4420-DX-S6-316L--C-](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.11_260413_S3000716685.zip) | 2026-04-13 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.11_260413_S3000716685.zip) |  |

</details>


<details>
<summary><h2>DS-2DF4420WG-XEY - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.11 | [DS-2DF4420WG-XEY](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.11_260413_S3000716685.zip) | 2026-04-13 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.11_260413_S3000716685.zip) |  |

</details>


<details>
<summary><h2>DS-2DF4420WG-XEY-ADC--E- - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.9.3 | [DS-2DF4420WG-XEY-ADC--E-](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.9.3_260417_S3000717323.zip) | 2026-04-17 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.9.3_260417_S3000717323.zip) |  |

</details>


<details>
<summary><h2>DS-2DF6223-CX-T5-316L- - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.7 | [DS-2DF6223-CX-T5-316L-](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.7_260410_S3000716682.zip) | 2026-04-10 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.7_260410_S3000716682.zip) |  |

</details>


<details>
<summary><h2>DS-2DF6231-CX-T5-316L- - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.7 | [DS-2DF6231-CX-T5-316L-](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.7_260410_S3000716682.zip) | 2026-04-10 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.7_260410_S3000716682.zip) |  |

</details>


<details>
<summary><h2>DS-2DF6C431-CX-T5-316L- - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.7 | [DS-2DF6C431-CX-T5-316L-](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.7_260410_S3000716682.zip) | 2026-04-10 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.7_260410_S3000716682.zip) |  |

</details>


<details>
<summary><h2>DS-2DF8432IWG-CXF-316L- - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.7 | [DS-2DF8432IWG-CXF-316L-](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.7_260410_S3000716682.zip) | 2026-04-10 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.7_260410_S3000716682.zip) |  |

</details>


<details>
<summary><h2>DS-2ST4C420MWG-E-14-PA- - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.9.62 | [DS-2ST4C420MWG-E-14-PA-](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.9.62_260416_S3000716213.zip) | 2026-04-16 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.9.62_260416_S3000716213.zip) |  |

</details>


<details>
<summary><h2>DS-2TD1217-2-QA - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.338 | [DS-2TD1217-2-QA](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.338_260413_S3000716448.zip) | 2026-04-13 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.338_260413_S3000716448.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202605/releasenote%5CGeneral_Firmware_Update_Release_notes.pdf) |

</details>


<details>
<summary><h2>DS-2TD1217-3-QA - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.338 | [DS-2TD1217-3-QA](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.338_260413_S3000716448.zip) | 2026-04-13 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.338_260413_S3000716448.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202605/releasenote%5CGeneral_Firmware_Update_Release_notes.pdf) |

</details>


<details>
<summary><h2>DS-2TD1217-6-QA - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.338 | [DS-2TD1217-6-QA](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.338_260413_S3000716448.zip) | 2026-04-13 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.338_260413_S3000716448.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202605/releasenote%5CGeneral_Firmware_Update_Release_notes.pdf) |

</details>


<details>
<summary><h2>DS-2TD1228-2-QA - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.338 | [DS-2TD1228-2-QA](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.338_260413_S3000716448.zip) | 2026-04-13 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.338_260413_S3000716448.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202605/releasenote%5CGeneral_Firmware_Update_Release_notes.pdf) |

</details>


<details>
<summary><h2>DS-2TD1228-3-QA - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.338 | [DS-2TD1228-3-QA](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.338_260413_S3000716448.zip) | 2026-04-13 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.338_260413_S3000716448.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202605/releasenote%5CGeneral_Firmware_Update_Release_notes.pdf) |

</details>


<details>
<summary><h2>DS-2TD1228-7-QA - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.338 | [DS-2TD1228-7-QA](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.338_260413_S3000716448.zip) | 2026-04-13 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.338_260413_S3000716448.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202605/releasenote%5CGeneral_Firmware_Update_Release_notes.pdf) |

</details>


<details>
<summary><h2>DS-2TD1228T-2-QA - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.338 | [DS-2TD1228T-2-QA](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.338_260413_S3000716448.zip) | 2026-04-13 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.338_260413_S3000716448.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202605/releasenote%5CGeneral_Firmware_Update_Release_notes.pdf) |

</details>


<details>
<summary><h2>DS-2TD1228T-2-QA-B- - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.338 | [DS-2TD1228T-2-QA-B-](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.338_260413_S3000716448.zip) | 2026-04-13 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.338_260413_S3000716448.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202605/releasenote%5CGeneral_Firmware_Update_Release_notes.pdf) |

</details>


<details>
<summary><h2>DS-2TD1228T-3-QA - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.338 | [DS-2TD1228T-3-QA](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.338_260413_S3000716448.zip) | 2026-04-13 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.338_260413_S3000716448.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202605/releasenote%5CGeneral_Firmware_Update_Release_notes.pdf) |

</details>


<details>
<summary><h2>DS-2TD1228T-3-QA-B- - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.338 | [DS-2TD1228T-3-QA-B-](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.338_260413_S3000716448.zip) | 2026-04-13 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.338_260413_S3000716448.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202605/releasenote%5CGeneral_Firmware_Update_Release_notes.pdf) |

</details>


<details>
<summary><h2>DS-2TD2137T-4-QY0 - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.338 | [DS-2TD2137T-4-QY0](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.338_260413_S3000716448.zip) | 2026-04-13 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.338_260413_S3000716448.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202605/releasenote%5CGeneral_Firmware_Update_Release_notes.pdf) |

</details>


<details>
<summary><h2>DS-2TD2137T-7-QY0 - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.338 | [DS-2TD2137T-7-QY0](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.338_260413_S3000716448.zip) | 2026-04-13 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.338_260413_S3000716448.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202605/releasenote%5CGeneral_Firmware_Update_Release_notes.pdf) |

</details>


<details>
<summary><h2>DS-2TD2138-10-QY - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.338 | [DS-2TD2138-10-QY](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.338_260413_S3000716448.zip) | 2026-04-13 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.338_260413_S3000716448.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202605/releasenote%5CGeneral_Firmware_Update_Release_notes.pdf) |

</details>


<details>
<summary><h2>DS-2TD2138-13-QY - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.338 | [DS-2TD2138-13-QY](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.338_260413_S3000716448.zip) | 2026-04-13 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.338_260413_S3000716448.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202605/releasenote%5CGeneral_Firmware_Update_Release_notes.pdf) |

</details>


<details>
<summary><h2>DS-2TD2138-15-QY - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.338 | [DS-2TD2138-15-QY](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.338_260413_S3000716448.zip) | 2026-04-13 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.338_260413_S3000716448.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202605/releasenote%5CGeneral_Firmware_Update_Release_notes.pdf) |

</details>


<details>
<summary><h2>DS-2TD2138-25-QY - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.338 | [DS-2TD2138-25-QY](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.338_260413_S3000716448.zip) | 2026-04-13 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.338_260413_S3000716448.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202605/releasenote%5CGeneral_Firmware_Update_Release_notes.pdf) |

</details>


<details>
<summary><h2>DS-2TD2138-35-QY - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.338 | [DS-2TD2138-35-QY](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.338_260413_S3000716448.zip) | 2026-04-13 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.338_260413_S3000716448.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202605/releasenote%5CGeneral_Firmware_Update_Release_notes.pdf) |

</details>


<details>
<summary><h2>DS-2TD2138-4-QY - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.338 | [DS-2TD2138-4-QY](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.338_260413_S3000716448.zip) | 2026-04-13 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.338_260413_S3000716448.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202605/releasenote%5CGeneral_Firmware_Update_Release_notes.pdf) |

</details>


<details>
<summary><h2>DS-2TD2138-7-QY - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.338 | [DS-2TD2138-7-QY](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.338_260413_S3000716448.zip) | 2026-04-13 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.338_260413_S3000716448.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202605/releasenote%5CGeneral_Firmware_Update_Release_notes.pdf) |

</details>


<details>
<summary><h2>DS-2TD2608-1-QA - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.338 | [DS-2TD2608-1-QA](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.338_260413_S3000716448.zip) | 2026-04-13 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.338_260413_S3000716448.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202605/releasenote%5CGeneral_Firmware_Update_Release_notes.pdf) |

</details>


<details>
<summary><h2>DS-2TD2608-2-QA - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.338 | [DS-2TD2608-2-QA](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.338_260413_S3000716448.zip) | 2026-04-13 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.338_260413_S3000716448.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202605/releasenote%5CGeneral_Firmware_Update_Release_notes.pdf) |

</details>


<details>
<summary><h2>DS-2TD2617-10-QA - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.338 | [DS-2TD2617-10-QA](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.338_260413_S3000716448.zip) | 2026-04-13 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.338_260413_S3000716448.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202605/releasenote%5CGeneral_Firmware_Update_Release_notes.pdf) |

</details>


<details>
<summary><h2>DS-2TD2617-3-QA - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.338 | [DS-2TD2617-3-QA](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.338_260413_S3000716448.zip) | 2026-04-13 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.338_260413_S3000716448.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202605/releasenote%5CGeneral_Firmware_Update_Release_notes.pdf) |

</details>


<details>
<summary><h2>DS-2TD2617-6-QA - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.338 | [DS-2TD2617-6-QA](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.338_260413_S3000716448.zip) | 2026-04-13 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.338_260413_S3000716448.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202605/releasenote%5CGeneral_Firmware_Update_Release_notes.pdf) |

</details>


<details>
<summary><h2>DS-2TD2628-10-QA - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.338 | [DS-2TD2628-10-QA](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.338_260413_S3000716448.zip) | 2026-04-13 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.338_260413_S3000716448.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202605/releasenote%5CGeneral_Firmware_Update_Release_notes.pdf) |

</details>


<details>
<summary><h2>DS-2TD2628-10-QA-GLT - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.118 | [DS-2TD2628-10-QA-GLT](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.118_260410_S3000715525.zip) | 2026-04-10 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.118_260410_S3000715525.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202605/releasenote%5CGeneral_Firmware_Update_Release_notes.pdf) |

</details>


<details>
<summary><h2>DS-2TD2628-3-QA - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.338 | [DS-2TD2628-3-QA](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.338_260413_S3000716448.zip) | 2026-04-13 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.338_260413_S3000716448.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202605/releasenote%5CGeneral_Firmware_Update_Release_notes.pdf) |

</details>


<details>
<summary><h2>DS-2TD2628-7-QA - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.338 | [DS-2TD2628-7-QA](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.338_260413_S3000716448.zip) | 2026-04-13 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.338_260413_S3000716448.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202605/releasenote%5CGeneral_Firmware_Update_Release_notes.pdf) |

</details>


<details>
<summary><h2>DS-2TD2628T-3-QA - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.338 | [DS-2TD2628T-3-QA](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.338_260413_S3000716448.zip) | 2026-04-13 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.338_260413_S3000716448.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202605/releasenote%5CGeneral_Firmware_Update_Release_notes.pdf) |

</details>


<details>
<summary><h2>DS-2TD2628T-7-QA - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.338 | [DS-2TD2628T-7-QA](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.338_260413_S3000716448.zip) | 2026-04-13 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.338_260413_S3000716448.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202605/releasenote%5CGeneral_Firmware_Update_Release_notes.pdf) |

</details>


<details>
<summary><h2>DS-2TD2637-10-QY - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.338 | [DS-2TD2637-10-QY](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.338_260413_S3000716448.zip) | 2026-04-13 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.338_260413_S3000716448.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202605/releasenote%5CGeneral_Firmware_Update_Release_notes.pdf) |

</details>


<details>
<summary><h2>DS-2TD2637-25-QY - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.338 | [DS-2TD2637-25-QY](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.338_260413_S3000716448.zip) | 2026-04-13 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.338_260413_S3000716448.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202605/releasenote%5CGeneral_Firmware_Update_Release_notes.pdf) |

</details>


<details>
<summary><h2>DS-2TD2637-35-QY-B- - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.338 | [DS-2TD2637-35-QY-B-](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.338_260413_S3000716448.zip) | 2026-04-13 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.338_260413_S3000716448.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202605/releasenote%5CGeneral_Firmware_Update_Release_notes.pdf) |

</details>


<details>
<summary><h2>DS-2TD2637-7-QY - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.338 | [DS-2TD2637-7-QY](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.338_260413_S3000716448.zip) | 2026-04-13 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.338_260413_S3000716448.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202605/releasenote%5CGeneral_Firmware_Update_Release_notes.pdf) |

</details>


<details>
<summary><h2>DS-2TD2637T-10-QY - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.338 | [DS-2TD2637T-10-QY](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.338_260413_S3000716448.zip) | 2026-04-13 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.338_260413_S3000716448.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202605/releasenote%5CGeneral_Firmware_Update_Release_notes.pdf) |

</details>


<details>
<summary><h2>DS-2TD2637T-15-QY - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.338 | [DS-2TD2637T-15-QY](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.338_260413_S3000716448.zip) | 2026-04-13 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.338_260413_S3000716448.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202605/releasenote%5CGeneral_Firmware_Update_Release_notes.pdf) |

</details>


<details>
<summary><h2>DS-2TD2637T-7-QY - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.338 | [DS-2TD2637T-7-QY](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.338_260413_S3000716448.zip) | 2026-04-13 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.338_260413_S3000716448.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202605/releasenote%5CGeneral_Firmware_Update_Release_notes.pdf) |

</details>


<details>
<summary><h2>DS-2TD5537T-7 - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.49 | Applied to: [DS-2TD5537T-7/W](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.49_220822_S3000450133.zip) | 2022-08-22 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.49_220822_S3000450133.zip) |  |

</details>


<details>
<summary><h2>DS-2TX3742-10A-Q - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.338 | [DS-2TX3742-10A-Q](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.338_260413_S3000716448.zip) | 2026-04-13 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.338_260413_S3000716448.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202605/releasenote%5CGeneral_Firmware_Update_Release_notes.pdf) |

</details>


<details>
<summary><h2>DS-2TX3742-10P-Q - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.338 | [DS-2TX3742-10P-Q](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.338_260413_S3000716448.zip) | 2026-04-13 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.338_260413_S3000716448.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202605/releasenote%5CGeneral_Firmware_Update_Release_notes.pdf) |

</details>


<details>
<summary><h2>DS-2TX3742-25A-Q - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.338 | [DS-2TX3742-25A-Q](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.338_260413_S3000716448.zip) | 2026-04-13 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.338_260413_S3000716448.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202605/releasenote%5CGeneral_Firmware_Update_Release_notes.pdf) |

</details>


<details>
<summary><h2>DS-2TX3742-25P-Q - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.338 | [DS-2TX3742-25P-Q](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.338_260413_S3000716448.zip) | 2026-04-13 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.338_260413_S3000716448.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202605/releasenote%5CGeneral_Firmware_Update_Release_notes.pdf) |

</details>


<details>
<summary><h2>DS-2TX3742-35A-Q - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.338 | [DS-2TX3742-35A-Q](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.338_260413_S3000716448.zip) | 2026-04-13 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.338_260413_S3000716448.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202605/releasenote%5CGeneral_Firmware_Update_Release_notes.pdf) |

</details>


<details>
<summary><h2>DS-2TX3742-35P-Q - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.338 | [DS-2TX3742-35P-Q](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.338_260413_S3000716448.zip) | 2026-04-13 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.338_260413_S3000716448.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202605/releasenote%5CGeneral_Firmware_Update_Release_notes.pdf) |

</details>


<details>
<summary><h2>DS-2XC6046G0-LIS-316L- - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.3 | [DS-2XC6046G0-LIS-316L-](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.3_260416_S3000716238.zip) | 2026-04-16 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.3_260416_S3000716238.zip) |  |

</details>


<details>
<summary><h2>DS-3WR18X - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 1.7.100 | [DS-3WR18X](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V1.7.100_260429_S3000720515.zip) | 2026-04-29 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V1.7.100_260429_S3000720515.zip) |  |

</details>


<details>
<summary><h2>DS-3WR30X - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 1.7.100 | [DS-3WR30X](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V1.7.100_260429_S3000720515.zip) | 2026-04-29 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V1.7.100_260429_S3000720515.zip) |  |

</details>


<details>
<summary><h2>DS-3WR30X-V - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 1.7.100 | [DS-3WR30X-V](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V1.7.100_260429_S3000720515.zip) | 2026-04-29 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V1.7.100_260429_S3000720515.zip) |  |

</details>


<details>
<summary><h2>DS-3WRM18X-1 - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 1.7.100 | [DS-3WRM18X-1](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V1.7.100_260429_S3000720515.zip) | 2026-04-29 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V1.7.100_260429_S3000720515.zip) |  |

</details>


<details>
<summary><h2>DS-3WRM18X-2 - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 1.7.100 | [DS-3WRM18X-2](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V1.7.100_260429_S3000720515.zip) | 2026-04-29 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V1.7.100_260429_S3000720515.zip) |  |

</details>


<details>
<summary><h2>DS-3WRM18X-3 - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 1.7.100 | [DS-3WRM18X-3](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V1.7.100_260429_S3000720515.zip) | 2026-04-29 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V1.7.100_260429_S3000720515.zip) |  |

</details>


<details>
<summary><h2>DS-3WRM30X-1 - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 1.7.100 | [DS-3WRM30X-1](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V1.7.100_260429_S3000720515.zip) | 2026-04-29 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V1.7.100_260429_S3000720515.zip) |  |

</details>


<details>
<summary><h2>DS-3WRM30X-2 - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 1.7.100 | [DS-3WRM30X-2](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V1.7.100_260429_S3000720515.zip) | 2026-04-29 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V1.7.100_260429_S3000720515.zip) |  |

</details>


<details>
<summary><h2>DS-3WRM30X-3 - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 1.7.100 | [DS-3WRM30X-3](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V1.7.100_260429_S3000720515.zip) | 2026-04-29 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V1.7.100_260429_S3000720515.zip) |  |

</details>


<details>
<summary><h2>DS-7104NI-S2-WX - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 4.32.406 | [DS-7104NI-S2-WX](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V4.32.406_260427_S3000720971.zip) | 2026-04-27 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V4.32.406_260427_S3000720971.zip) |  |

</details>


<details>
<summary><h2>DS-7232HGHI-M2-T-2K - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 4.84.100 | [DS-7232HGHI-M2-T-2K](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware_Europe_V4.84.100_260425_S3000719711.zip) | 2026-04-25 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware_Europe_V4.84.100_260425_S3000719711.zip) |  |

</details>


<details>
<summary><h2>DS-C80N-01HI - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 1.2.0 | [DS-C80N-01HI](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V1.2.0_260423_S3000720433.zip) | 2026-04-23 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V1.2.0_260423_S3000720433.zip) |  |

</details>


<details>
<summary><h2>DS-C80N-01HI-4K - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 1.2.0 | [DS-C80N-01HI-4K](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V1.2.0_260423_S3000720433.zip) | 2026-04-23 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V1.2.0_260423_S3000720433.zip) |  |

</details>


<details>
<summary><h2>DS-C80N-01HO - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 1.2.0 | [DS-C80N-01HO](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V1.2.0_260423_S3000720433.zip) | 2026-04-23 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V1.2.0_260423_S3000720433.zip) |  |

</details>


<details>
<summary><h2>DS-C80N-01HO-4K - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 1.2.0 | [DS-C80N-01HO-4K](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V1.2.0_260423_S3000720433.zip) | 2026-04-23 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V1.2.0_260423_S3000720433.zip) |  |

</details>


<details>
<summary><h2>DS-J142I - UNKNOWN (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 4.32.406 | [DS-J142I](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V4.32.406_260427_S3000720971.zip) | 2026-04-27 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V4.32.406_260427_S3000720971.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202605/releasenote%5CNetwork_Camera-V5.8.23_SP1_Release_Note-E9_E10.pdf) |
| 5.8.100 | [DS-J142I](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.100_260416_S3000716492.zip) | 2026-04-16 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.100_260416_S3000716492.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202605/releasenote%5CNetwork_Camera-V5.8.23_SP1_Release_Note-E9_E10.pdf) |

</details>


<details>
<summary><h2>DS-K1105EDB - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 1.0.2 | [DS-K1105EDB](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V1.0.2_260414_S3000716047.zip) | 2026-04-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V1.0.2_260414_S3000716047.zip) |  |

</details>


<details>
<summary><h2>DS-K1105EDKB - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 1.0.2 | [DS-K1105EDKB](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V1.0.2_260414_S3000716047.zip) | 2026-04-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V1.0.2_260414_S3000716047.zip) |  |

</details>


<details>
<summary><h2>DS-K1105EDKB-QR - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 1.0.2 | [DS-K1105EDKB-QR](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V1.0.2_260414_S3000716047.zip) | 2026-04-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V1.0.2_260414_S3000716047.zip) |  |

</details>


<details>
<summary><h2>DS-K1105EMB - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 1.0.2 | [DS-K1105EMB](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V1.0.2_260414_S3000716047.zip) | 2026-04-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V1.0.2_260414_S3000716047.zip) |  |

</details>


<details>
<summary><h2>DS-K1105EMKB - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 1.0.2 | [DS-K1105EMKB](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V1.0.2_260414_S3000716047.zip) | 2026-04-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V1.0.2_260414_S3000716047.zip) |  |

</details>


<details>
<summary><h2>DS-K1105EMKB-QR - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 1.0.2 | [DS-K1105EMKB-QR](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V1.0.2_260414_S3000716047.zip) | 2026-04-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V1.0.2_260414_S3000716047.zip) |  |

</details>


<details>
<summary><h2>DS-K1T342DWX - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 4.48.0 | [DS-K1T342DWX](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V4.48.0_260417_S3000716679.zip) | 2026-04-17 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V4.48.0_260417_S3000716679.zip) |  |

</details>


<details>
<summary><h2>DS-K1T342DWX-E1 - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 4.48.0 | [DS-K1T342DWX-E1](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V4.48.0_260417_S3000716679.zip) | 2026-04-17 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V4.48.0_260417_S3000716679.zip) |  |

</details>


<details>
<summary><h2>DS-K1T342DX - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 4.48.0 | [DS-K1T342DX](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V4.48.0_260417_S3000716679.zip) | 2026-04-17 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V4.48.0_260417_S3000716679.zip) |  |

</details>


<details>
<summary><h2>DS-K1T342DX-E1 - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 4.48.0 | [DS-K1T342DX-E1](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V4.48.0_260417_S3000716679.zip) | 2026-04-17 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V4.48.0_260417_S3000716679.zip) |  |

</details>


<details>
<summary><h2>DS-K1T342EFWX - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 4.48.0 | [DS-K1T342EFWX](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V4.48.0_260417_S3000716679.zip) | 2026-04-17 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V4.48.0_260417_S3000716679.zip) |  |

</details>


<details>
<summary><h2>DS-K1T342EFWX-E1 - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 4.48.0 | [DS-K1T342EFWX-E1](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V4.48.0_260417_S3000716679.zip) | 2026-04-17 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V4.48.0_260417_S3000716679.zip) |  |

</details>


<details>
<summary><h2>DS-K1T342EWX - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 4.48.0 | [DS-K1T342EWX](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V4.48.0_260417_S3000716679.zip) | 2026-04-17 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V4.48.0_260417_S3000716679.zip) |  |

</details>


<details>
<summary><h2>DS-K1T342EWX-E1 - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 4.48.0 | [DS-K1T342EWX-E1](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V4.48.0_260417_S3000716679.zip) | 2026-04-17 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V4.48.0_260417_S3000716679.zip) |  |

</details>


<details>
<summary><h2>DS-K1T342EX - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 4.48.0 | [DS-K1T342EX](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V4.48.0_260417_S3000716679.zip) | 2026-04-17 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V4.48.0_260417_S3000716679.zip) |  |

</details>


<details>
<summary><h2>DS-K1T342EX-E1 - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 4.48.0 | [DS-K1T342EX-E1](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V4.48.0_260417_S3000716679.zip) | 2026-04-17 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V4.48.0_260417_S3000716679.zip) |  |

</details>


<details>
<summary><h2>DS-K1T342MFWX - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 4.48.0 | [DS-K1T342MFWX](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V4.48.0_260417_S3000716679.zip) | 2026-04-17 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V4.48.0_260417_S3000716679.zip) |  |

</details>


<details>
<summary><h2>DS-K1T342MFWX-E1 - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 4.48.0 | [DS-K1T342MFWX-E1](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V4.48.0_260417_S3000716679.zip) | 2026-04-17 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V4.48.0_260417_S3000716679.zip) |  |

</details>


<details>
<summary><h2>DS-K1T342MFX - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 4.48.0 | [DS-K1T342MFX](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V4.48.0_260417_S3000716679.zip) | 2026-04-17 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V4.48.0_260417_S3000716679.zip) |  |

</details>


<details>
<summary><h2>DS-K1T342MFX-E1 - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 4.48.0 | [DS-K1T342MFX-E1](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V4.48.0_260417_S3000716679.zip) | 2026-04-17 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V4.48.0_260417_S3000716679.zip) |  |

</details>


<details>
<summary><h2>DS-K1T342MWX - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 4.48.0 | [DS-K1T342MWX](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V4.48.0_260417_S3000716679.zip) | 2026-04-17 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V4.48.0_260417_S3000716679.zip) |  |

</details>


<details>
<summary><h2>DS-K1T342MWX-E1 - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 4.48.0 | [DS-K1T342MWX-E1](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V4.48.0_260417_S3000716679.zip) | 2026-04-17 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V4.48.0_260417_S3000716679.zip) |  |

</details>


<details>
<summary><h2>DS-K1T342MX - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 4.48.0 | [DS-K1T342MX](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V4.48.0_260417_S3000716679.zip) | 2026-04-17 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V4.48.0_260417_S3000716679.zip) |  |

</details>


<details>
<summary><h2>DS-K1T342MX-E1 - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 4.48.0 | [DS-K1T342MX-E1](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V4.48.0_260417_S3000716679.zip) | 2026-04-17 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V4.48.0_260417_S3000716679.zip) |  |

</details>


<details>
<summary><h2>DS-K1T343EFWX - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 4.48.0 | [DS-K1T343EFWX](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V4.48.0_260417_S3000716680.zip) | 2026-04-17 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V4.48.0_260417_S3000716680.zip) |  |

</details>


<details>
<summary><h2>DS-K1T343EWX - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 4.48.0 | [DS-K1T343EWX](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V4.48.0_260417_S3000716680.zip) | 2026-04-17 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V4.48.0_260417_S3000716680.zip) |  |

</details>


<details>
<summary><h2>DS-K1T343MFWX - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 4.48.0 | [DS-K1T343MFWX](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V4.48.0_260417_S3000716680.zip) | 2026-04-17 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V4.48.0_260417_S3000716680.zip) |  |

</details>


<details>
<summary><h2>DS-K1T343MWX - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 4.48.0 | [DS-K1T343MWX](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V4.48.0_260417_S3000716680.zip) | 2026-04-17 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V4.48.0_260417_S3000716680.zip) |  |

</details>


<details>
<summary><h2>DS-K1T670MFWX - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 4.48.20 | [DS-K1T670MFWX](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V4.48.20_260427_S3000719622.zip) | 2026-04-27 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V4.48.20_260427_S3000719622.zip) |  |

</details>


<details>
<summary><h2>DS-K1T670MWX-QR - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 4.48.20 | [DS-K1T670MWX-QR](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V4.48.20_260427_S3000719622.zip) | 2026-04-27 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V4.48.20_260427_S3000719622.zip) |  |

</details>


<details>
<summary><h2>DS-K1T670MWX-WBQR - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 4.48.20 | [DS-K1T670MWX-WBQR](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V4.48.20_260427_S3000719622.zip) | 2026-04-27 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V4.48.20_260427_S3000719622.zip) |  |

</details>


<details>
<summary><h2>DS-K1T670MWX-WEQR - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 4.48.20 | [DS-K1T670MWX-WEQR](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V4.48.20_260427_S3000719622.zip) | 2026-04-27 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V4.48.20_260427_S3000719622.zip) |  |

</details>


<details>
<summary><h2>DS-K1T670MX - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 4.48.20 | [DS-K1T670MX](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V4.48.20_260427_S3000719622.zip) | 2026-04-27 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V4.48.20_260427_S3000719622.zip) |  |

</details>


<details>
<summary><h2>DS-K1T670MX-QR - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 4.48.20 | [DS-K1T670MX-QR](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V4.48.20_260427_S3000719622.zip) | 2026-04-27 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V4.48.20_260427_S3000719622.zip) |  |

</details>


<details>
<summary><h2>DS-K1T670MX-WB - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 4.48.20 | [DS-K1T670MX-WB](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V4.48.20_260427_S3000719622.zip) | 2026-04-27 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V4.48.20_260427_S3000719622.zip) |  |

</details>


<details>
<summary><h2>DS-K1T670MX-WE - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 4.48.20 | [DS-K1T670MX-WE](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V4.48.20_260427_S3000719622.zip) | 2026-04-27 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V4.48.20_260427_S3000719622.zip) |  |

</details>


<details>
<summary><h2>DS-K3B411BX - UNKNOWN (3 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 2.0.5 | Applied to: [DS-K3B411BX-L/M](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V2.0.5_250922_S3000677823.zip) | 2025-09-22 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V2.0.5_250922_S3000677823.zip) |  |
| 2.4.0 | Applied to: [DS-K3B411BX-L/M](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V2.4.0_250106_S3000625394.zip) | 2025-01-06 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V2.4.0_250106_S3000625394.zip) |  |
| 1.0.0 | Applied to: [DS-K3B411BX-L/M](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V1.0.0_240523_S3000577702.zip) | 2024-05-23 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V1.0.0_240523_S3000577702.zip) |  |

</details>


<details>
<summary><h2>DS-KAS342 - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 4.48.0 | [DS-KAS342](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V4.48.0_260417_S3000716679.zip) | 2026-04-17 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V4.48.0_260417_S3000716679.zip) |  |

</details>


<details>
<summary><h2>IDS-2CD5347G2-V-XS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.9.21 | [IDS-2CD5347G2-V-XS](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.9.21_260423_S3000719054.zip) | 2026-04-23 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.9.21_260423_S3000719054.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202605/releasenote%5CDeepinViewX_Network_Camera_V5.9.21_Release_Note_--H9.pdf) |

</details>


<details>
<summary><h2>IDS-2CD5387G2-V-XS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.9.21 | [IDS-2CD5387G2-V-XS](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.9.21_260423_S3000719054.zip) | 2026-04-23 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.9.21_260423_S3000719054.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202605/releasenote%5CDeepinViewX_Network_Camera_V5.9.21_Release_Note_--H9.pdf) |

</details>


<details>
<summary><h2>IDS-2CD5A46G2-V-XZ-H-S-Y- - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.9.21 | [IDS-2CD5A46G2-V-XZ-H-S-Y-](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.9.21_260423_S3000719054.zip) | 2026-04-23 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.9.21_260423_S3000719054.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202605/releasenote%5CDeepinViewX_Network_Camera_V5.9.21_Release_Note_--H9.pdf) |

</details>


<details>
<summary><h2>IDS-2CD5A86G2-V-XZ-H-S-Y- - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.9.21 | [IDS-2CD5A86G2-V-XZ-H-S-Y-](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.9.21_260423_S3000719054.zip) | 2026-04-23 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.9.21_260423_S3000719054.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202605/releasenote%5CDeepinViewX_Network_Camera_V5.9.21_Release_Note_--H9.pdf) |

</details>


<details>
<summary><h2>IDS-2CD5D47G2-V-XS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.9.21 | [IDS-2CD5D47G2-V-XS](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.9.21_260423_S3000719054.zip) | 2026-04-23 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.9.21_260423_S3000719054.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202605/releasenote%5CDeepinViewX_Network_Camera_V5.9.21_Release_Note_--H9.pdf) |

</details>


<details>
<summary><h2>IDS-2CD5D87G2-V-XS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.9.21 | [IDS-2CD5D87G2-V-XS](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.9.21_260423_S3000719054.zip) | 2026-04-23 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.9.21_260423_S3000719054.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202605/releasenote%5CDeepinViewX_Network_Camera_V5.9.21_Release_Note_--H9.pdf) |

</details>


<details>
<summary><h2>IDS-2CD5T47G2-V-X-H-S-Y- - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.9.21 | [IDS-2CD5T47G2-V-X-H-S-Y-](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.9.21_260423_S3000719054.zip) | 2026-04-23 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.9.21_260423_S3000719054.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202605/releasenote%5CDeepinViewX_Network_Camera_V5.9.21_Release_Note_--H9.pdf) |

</details>


<details>
<summary><h2>IDS-2CD5T87G2-V-X-H-S-Y- - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.9.21 | [IDS-2CD5T87G2-V-X-H-S-Y-](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.9.21_260423_S3000719054.zip) | 2026-04-23 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.9.21_260423_S3000719054.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202605/releasenote%5CDeepinViewX_Network_Camera_V5.9.21_Release_Note_--H9.pdf) |

</details>


<details>
<summary><h2>IDS-2CD7A45G0-IZ-H-S-Y- - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.50 | [IDS-2CD7A45G0-IZ-H-S-Y-](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.50_260415_S3000716272.zip) | 2026-04-15 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.50_260415_S3000716272.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202605/releasenote%5CNetwork_Camera_V5.8.50_Release_Note_--H8.pdf) |

</details>


<details>
<summary><h2>IDS-2CD7A45G0-P-IZHS-Y- - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.50 | [IDS-2CD7A45G0-P-IZHS-Y-](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.50_260415_S3000716272.zip) | 2026-04-15 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.50_260415_S3000716272.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202605/releasenote%5CNetwork_Camera_V5.8.50_Release_Note_--H8.pdf) |

</details>


<details>
<summary><h2>IDS-2CD7T46G2-VX3-I-H-S-Y- - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.9.21 | [IDS-2CD7T46G2-VX3-I-H-S-Y-](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.9.21_260423_S3000719054.zip) | 2026-04-23 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.9.21_260423_S3000719054.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202605/releasenote%5CDeepinViewX_Network_Camera_V5.9.21_Release_Note_--H9.pdf) |

</details>


<details>
<summary><h2>IDS-2CD8V446G0-X2-XZHS-Y- - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.10.0 | [IDS-2CD8V446G0-X2-XZHS-Y-](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.10.0_260423_S3000718071.zip) | 2026-04-23 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.10.0_260423_S3000718071.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202605/releasenote%5CDeepinView_Dual-Lens_Omni_Camera_V5.10.0_Release_Note.pdf) |

</details>


<details>
<summary><h2>IDS-2CD8V447G0E-X2-XZS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.10.0 | [IDS-2CD8V447G0E-X2-XZS](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.10.0_260423_S3000718071.zip) | 2026-04-23 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.10.0_260423_S3000718071.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202605/releasenote%5CDeepinView_Dual-Lens_Omni_Camera_V5.10.0_Release_Note.pdf) |

</details>


<details>
<summary><h2>IDS-2CD8V886G0-X2-XZHS-Y- - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.10.0 | [IDS-2CD8V886G0-X2-XZHS-Y-](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.10.0_260423_S3000718071.zip) | 2026-04-23 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.10.0_260423_S3000718071.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202605/releasenote%5CDeepinView_Dual-Lens_Omni_Camera_V5.10.0_Release_Note.pdf) |

</details>


<details>
<summary><h2>IDS-E08HQHI-B - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 4.75.013 | Applied to: [iDS-E08HQHI-B](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware_Asia_V4.75.013_240919_S3000600889.zip) | 2024-09-19 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware_Asia_V4.75.013_240919_S3000600889.zip) |  |

</details>


<details>
<summary><h2>UNKNOWN - UNKNOWN (3 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.348 | [UNKNOWN](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.348_260427_S3000719140.zip) | 2026-04-27 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.348_260427_S3000719140.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202605/releasenote%5CGeneral_Firmware_Update_Release_notes.pdf) |
| 5.9.5 | [UNKNOWN](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.9.5_260416_S3000716247.zip) | 2026-04-16 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.9.5_260416_S3000716247.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202604/releasenote%5CV5.9.5_260416_Release_Note.pdf) |
| 5.5.61 | [UNKNOWN](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.61_260413_S3000715287.zip) | 2026-04-13 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.61_260413_S3000715287.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202605/releasenote%5CGeneral_Firmware_Update_Release_notes.pdf) |

</details>
