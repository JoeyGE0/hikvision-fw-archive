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
**Last Run:** 2026-01-24 05:20:35 UTC  
**Firmwares Found:** 100  
**New Firmwares:** 10  
**Test Mode:** Disabled



---

## Firmware List

Below is the complete list of archived firmwares, organized by device model and hardware version.

**Total: 100**



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
| 1.1.2 | Applied to: [AE-DC2015-B1](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V1.1.2_200914_S3000337767.zip) | 2020-09-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V1.1.2_200914_S3000337767.zip) |  |
| 1.0.8 | Applied to: [AE-DC2015-B1](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V1.0.8_250703_S3000666382.zip) | 2020-03-20 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V1.0.8_250703_S3000666382.zip) |  |
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
| 1.0.8 | Applied to: [AE-DC8312-C6S(GPS)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V1.0.8_250703_S3000666382.zip) | 2025-07-03 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V1.0.8_250703_S3000666382.zip) |  |

</details>


<details>
<summary><h2>AE-DC8322-G2PRO - UNKNOWN (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 1.1.7 | Applied to: [AE-DC8322-G2PRO(HK)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V1.1.7_230919_S3000526629.zip)(GPS) | 2023-09-19 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V1.1.7_230919_S3000526629.zip) |  |
| 1.1.4 | Applied to: [AE-DC8322-G2PRO(HK)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V1.1.4_220725_S3000443106.zip)(GPS) | 2022-07-25 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V1.1.4_220725_S3000443106.zip) |  |

</details>


<details>
<summary><h2>AE-DI2032-G40 - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
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
<summary><h2>AE-DI5052-G40 - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 4.7.4 | Applied to: [AE-DI5052-G40](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V4.7.4_251117_S3000685762.zip) PRO(EU) | 2025-11-17 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V4.7.4_251117_S3000685762.zip) |  |

</details>


<details>
<summary><h2>AE-MD5043-SD - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.1 | Applied to: [AE-MD5043-SD/GLF(EU-STD)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.10_241205_S3000618834.zip) | 2024-11-21 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.10_241205_S3000618834.zip) |  |

</details>


<details>
<summary><h2>AE-MH0408 - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.1 | Applied to: [AE-MH0408(1T)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.10_241205_S3000618834.zip)(RJ45) | 2024-11-21 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.10_241205_S3000618834.zip) |  |

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
| 5.7.23 | Applied to: [DS-2CD1023G0-IUF(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_241008_S3000605524.zip)(C) | 2024-12-11 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_241008_S3000605524.zip) |  |

</details>


<details>
<summary><h2>DS-2CD1023G0E-I - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD1023G0E-I(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_241008_S3000605524.zip) | 2024-12-11 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_241008_S3000605524.zip) |  |
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
| 5.8.10 | Applied to: [DS-2CD1023G2-LIUF(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.10_241205_S3000618834.zip) | 2024-12-05 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.10_241205_S3000618834.zip) |  |

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
| 5.8.10 | Applied to: [DS-2CD1027G2-LUF(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.10_241205_S3000618834.zip) | 2024-12-05 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.10_241205_S3000618834.zip) |  |

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
| 5.9.12 | Applied to: [DS-2CD1027G3-LIUF(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.9.12_250919_S3000675616.zip) | 2025-09-19 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.9.12_250919_S3000675616.zip) |  |
| 5.9.11 | Applied to: [DS-2CD1027G3-LIUF(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.9.11_250822_S3000669952.zip) | 2025-08-22 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.9.11_250822_S3000669952.zip) |  |

</details>


<details>
<summary><h2>DS-2CD1043G0-I - IPC_E7S (3 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD1043G0-IUF(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_241008_S3000605524.zip)(B) | 2024-12-11 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_241008_S3000605524.zip) |  |
| 5.5.820 | Applied to: [DS-2CD1043G0-IUF(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.820_231109_S3000539580.zip)(B) | 2023-11-09 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.820_231109_S3000539580.zip) |  |
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
| 5.8.10 | Applied to: [DS-2CD1043G2-LIUF(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.10_241205_S3000618834.zip) | 2025-07-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.10_241205_S3000618834.zip) |  |

</details>


<details>
<summary><h2>DS-2CD1043G2-LIUF - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.10 | Applied to: [DS-2CD1043G2-LIUF/SL(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.10_241205_S3000618834.zip) | 2025-07-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.10_241205_S3000618834.zip) |  |

</details>


<details>
<summary><h2>DS-2CD1047G2-L - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.10 | Applied to: [DS-2CD1047G2-LUF(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.10_241205_S3000618834.zip) | 2025-07-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.10_241205_S3000618834.zip) |  |

</details>


<details>
<summary><h2>DS-2CD1047G2H-LIU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.10 | Applied to: [DS-2CD1047G2H-LIU(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.10_241205_S3000618834.zip)(BLACK) | 2025-07-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.10_241205_S3000618834.zip) |  |

</details>


<details>
<summary><h2>DS-2CD1047G2H-LIUF - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.10 | Applied to: [DS-2CD1047G2H-LIUF/SRB(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.10_241205_S3000618834.zip) | 2025-07-14 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.10_241205_S3000618834.zip) |  |

</details>


<details>
<summary><h2>DS-2CD1047G3-LIU - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.9.12 | Applied to: [DS-2CD1047G3-LIUF(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.9.12_250919_S3000675616.zip) | 2025-09-19 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.9.12_250919_S3000675616.zip) |  |
| 5.9.11 | Applied to: [DS-2CD1047G3-LIUF(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.9.11_250822_S3000669952.zip) | 2025-08-22 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.9.11_250822_S3000669952.zip) |  |

</details>


<details>
<summary><h2>DS-2CD1047G3H-LIU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.21 | Applied to: [DS-2CD1047G3H-LIU/SRB(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.21_250714_S3000661481.zip) | 2025-11-17 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.21_250714_S3000661481.zip) |  |

</details>


<details>
<summary><h2>DS-2CD1053G0-I - IPC_G0 (3 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD1053G0-I(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_241008_S3000605524.zip) | 2024-10-08 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_241008_S3000605524.zip) |  |
| 5.5.800 | Applied to: [DS-2CD1053G0-I(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/af64952b-34be-46d9-94b8-3bf76fb5a5f4.zip) | 2021-08-16 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/af64952b-34be-46d9-94b8-3bf76fb5a5f4.zip) |  |
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
| 5.9.12 | Applied to: [DS-2CD1067G3-LIUF/SRB(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.9.12_250919_S3000675616.zip) | 2025-09-19 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.9.12_250919_S3000675616.zip) |  |
| 5.9.11 | Applied to: [DS-2CD1067G3-LIUF/SRB(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.9.11_250822_S3000669952.zip) | 2025-08-22 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.9.11_250822_S3000669952.zip) |  |

</details>


<details>
<summary><h2>DS-2CD1083G0-I - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD1083G0-I(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_241008_S3000605524.zip)(C) | 2024-10-08 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_241008_S3000605524.zip) |  |

</details>


<details>
<summary><h2>DS-2CD1083G0-IUF - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD1083G0-IUF(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_241008_S3000605524.zip)(C) | 2024-10-08 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_241008_S3000605524.zip) |  |

</details>


<details>
<summary><h2>DS-2CD1123G0-IUF - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD1123G0-IUF(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_241211_S3000620671.zip)(C) | 2024-12-11 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_241211_S3000620671.zip) |  |

</details>


<details>
<summary><h2>DS-2CD1123G0E-I - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD1123G0E-I(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_241211_S3000620671.zip) | 2024-12-11 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.7.23_241211_S3000620671.zip) |  |
| 5.5.84 | Applied to: [DS-2CD1123G0E-I(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/c3afe62f-4071-4e50-a292-ded015321289.zip) | 2021-01-04 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/c3afe62f-4071-4e50-a292-ded015321289.zip) |  |

</details>


<details>
<summary><h2>DS-2CD1123G2-LIU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.10 | Applied to: [DS-2CD1123G2-LIUF(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.10_241205_S3000618834.zip) | 2024-12-05 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.10_241205_S3000618834.zip) |  |

</details>


<details>
<summary><h2>DS-2CD1127G2-L - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.10 | Applied to: [DS-2CD1127G2-LUF(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.10_241205_S3000618834.zip) | 2024-12-05 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.8.10_241205_S3000618834.zip) |  |

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
| 5.9.12 | Applied to: [DS-2CD1127G3-LIUF(2.8mm)](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.9.12_250919_S3000675616.zip) | 2025-09-19 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.9.12_250919_S3000675616.zip) |  |

</details>


<details>
<summary><h2>DS-2TD5537T-7 - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.49 | Applied to: [DS-2TD5537T-7/W](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.49_220822_S3000450133.zip) | 2022-08-22 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware__V5.5.49_220822_S3000450133.zip) |  |

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
<summary><h2>IDS-E08HQHI-B - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 4.75.013 | Applied to: [iDS-E08HQHI-B](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware_Asia_V4.75.013_240919_S3000600889.zip) | 2024-09-19 | [📥 Download](https://github.com/JoeyGE0/hikvision-fw-archive/releases/latest/download/Firmware_Asia_V4.75.013_240919_S3000600889.zip) |  |

</details>
