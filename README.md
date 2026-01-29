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
**Last Run:** 2026-01-29 18:31:16 UTC  
**Firmwares Found:** 230  
**New Firmwares:** 10  
**Test Mode:** Disabled



---

## Firmware List

Below is the complete list of archived firmwares, organized by device model and hardware version.

**Total: 230**



<details>
<summary><h2>AE-AC1130-A - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 3.6.1 | Applied to: [AE-AC1130-A/GA(V3.0)](https://assets.hikvision.com/prd/public/all/files/202209/Firmware__V3.6.1_220818_S3000450312.zip)(LatinAmerica)/B | 2022-08-18 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202209/Firmware__V3.6.1_220818_S3000450312.zip) |  |

</details>


<details>
<summary><h2>AE-DC2015-B1 - UNKNOWN (6 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 1.1.5 | Applied to: [AE-DC2015-B1](https://assets.hikvision.com/prd/public/all/files/202209/Firmware__V1.1.5_220421_S3000442625.zip) | 2022-04-21 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202209/Firmware__V1.1.5_220421_S3000442625.zip) |  |
| 1.1.3 | Applied to: [AE-DC2015-B1](https://assets.hikvision.com/prd/public/all/files/202209/Firmware__V1.1.3_211116_S3000401023.zip) | 2021-11-16 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202209/Firmware__V1.1.3_211116_S3000401023.zip) |  |
| 1.1.4 | Applied to: [AE-DC2015-B1](https://assets.hikvision.com/prd/public/all/files/202209/Firmware__V1.1.4_210811_S3000384048.zip) | 2021-08-11 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202209/Firmware__V1.1.4_210811_S3000384048.zip) |  |
| 1.1.2 | Applied to: [AE-DC2015-B1](https://assets.hikvision.com/prd/public/all/files/202209/Firmware__V1.1.2_200914_S3000337767.zip) | 2020-09-14 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202209/Firmware__V1.1.2_200914_S3000337767.zip) |  |
| 1.0.8 | Applied to: [AE-DC2015-B1](https://assets.hikvision.com/prd/public/all/files/202209/Firmware__V1.0.8_200320_S3000313276.zip) | 2020-03-20 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202209/Firmware__V1.0.8_200320_S3000313276.zip) |  |
| 1.0.6 | Applied to: [AE-DC2015-B1](https://assets.hikvision.com/prd/public/all/files/202209/Firmware__V1.0.6_191031_S3000312642.zip) | 2019-10-31 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202209/Firmware__V1.0.6_191031_S3000312642.zip) |  |

</details>


<details>
<summary><h2>AE-DC2022-V200 - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 1.0.10 | Applied to: [AE-DC2022-V200(2CH)](https://assets.hikvision.com/prd/normal/all/files/202509/Firmware__V1.0.10_250902_S3000672017.zip) | 2025-09-02 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202509/Firmware__V1.0.10_250902_S3000672017.zip) |  |

</details>


<details>
<summary><h2>AE-DC2032-V300 - UNKNOWN (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 1.0.10 | Applied to: [AE-DC2032-V300(3CH)](https://assets.hikvision.com/prd/normal/all/files/202509/Firmware__V1.0.10_250902_S3000671476.zip) | 2025-09-02 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202509/Firmware__V1.0.10_250902_S3000671476.zip) |  |
| 1.0.3 | Applied to: [AE-DC2032-V300(3CH)](https://assets.hikvision.com/prd/public/all/files/202504/Firmware__V1.0.3_250328_S3000641095.zip) | 2025-03-28 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202504/Firmware__V1.0.3_250328_S3000641095.zip) |  |

</details>


<details>
<summary><h2>AE-DC4328-K5 - UNKNOWN (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 1.0.7 | Applied to: [AE-DC4328-K5(2CH)](https://assets.hikvision.com/prd/public/all/files/202308/Firmware__V1.0.7_230605_S3000521095.zip) | 2023-06-05 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202308/Firmware__V1.0.7_230605_S3000521095.zip) |  |
| 3.0.1 | Applied to: [AE-DC4328-K5(2CH)](https://assets.hikvision.com/prd/public/all/files/202401/Firmware__V3.0.1_230410_S3000550212.zip) | 2023-04-10 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202401/Firmware__V3.0.1_230410_S3000550212.zip) |  |

</details>


<details>
<summary><h2>AE-DC5013-F6 - UNKNOWN (5 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 1.3.2 | Applied to: [AE-DC5013-F6](https://assets.hikvision.com/prd/public/all/files/202209/Firmware__V1.3.2_220420_S3000442626.zip) | 2022-04-20 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202209/Firmware__V1.3.2_220420_S3000442626.zip) |  |
| 1.3.0 | Applied to: [AE-DC5013-F6](https://assets.hikvision.com/prd/public/all/files/202207/DashCam_AE_DC5013_F6_EN_STD_V1.3.0_build211110.zip) | 2021-11-10 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202207/DashCam_AE_DC5013_F6_EN_STD_V1.3.0_build211110.zip) |  |
| 1.2.7 | Applied to: [AE-DC5013-F6](https://assets.hikvision.com/prd/public/all/files/202207/DashCam_AE_DC5013_F6_CN_STD_V1.2.7_build210409.zip) | 2021-04-09 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202207/DashCam_AE_DC5013_F6_CN_STD_V1.2.7_build210409.zip) |  |
| 1.2.5 | Applied to: [AE-DC5013-F6](https://assets.hikvision.com/prd/public/all/files/202207/DashCam_AE_DC5013_F6_CN_STD_V1.2.5_build200827.zip) | 2020-08-27 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202207/DashCam_AE_DC5013_F6_CN_STD_V1.2.5_build200827.zip) |  |
| 1.2.1 | Applied to: [AE-DC5013-F6](https://assets.hikvision.com/prd/public/all/files/202207/DashCam_AE_DC5013_F6_CN_STD_V1.2.1_build200703.zip) | 2020-07-03 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202207/DashCam_AE_DC5013_F6_CN_STD_V1.2.1_build200703.zip) |  |

</details>


<details>
<summary><h2>AE-DC5013-F6PRO - UNKNOWN (3 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 1.3.4 | Applied to: [AE-DC5013-F6PRO](https://assets.hikvision.com/prd/public/all/files/202309/Firmware__V1.3.4_230919_S3000526631.zip) | 2023-09-19 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202309/Firmware__V1.3.4_230919_S3000526631.zip) |  |
| 1.3.2 | Applied to: [AE-DC5013-F6PRO](https://assets.hikvision.com/prd/public/all/files/202209/Firmware__V1.3.2_220420_S3000442626.zip) | 2022-04-20 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202209/Firmware__V1.3.2_220420_S3000442626.zip) |  |
| 1.3.0 | Applied to: [AE-DC5013-F6PRO](https://assets.hikvision.com/prd/public/all/files/202207/DashCam_AE_DC5013_F6_CN_STD_V1.3.0_build210625.zip) | 2021-06-25 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202207/DashCam_AE_DC5013_F6_CN_STD_V1.3.0_build210625.zip) |  |

</details>


<details>
<summary><h2>AE-DC5113-F6S - UNKNOWN (5 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 1.3.2 | Applied to: [AE-DC5113-F6S](https://assets.hikvision.com/prd/public/all/files/202210/Firmware__V1.3.2_220928_S3000456412.zip) | 2022-09-28 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202210/Firmware__V1.3.2_220928_S3000456412.zip) |  |
| 1.3.0 | Applied to: [AE-DC5113-F6S](https://assets.hikvision.com/prd/public/all/files/202209/Firmware__V1.3.0_210822_S3000384053.zip) | 2021-08-22 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202209/Firmware__V1.3.0_210822_S3000384053.zip) |  |
| 1.2.8 | Applied to: [AE-DC5113-F6S](https://assets.hikvision.com/prd/public/all/files/202209/Firmware__V1.2.8_210513_S3000365428.zip) | 2021-05-13 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202209/Firmware__V1.2.8_210513_S3000365428.zip) |  |
| 1.2.6 | Applied to: [AE-DC5113-F6S](https://assets.hikvision.com/prd/public/all/files/202209/Firmware__V1.2.6_200820_S3000332869.zip) | 2020-08-20 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202209/Firmware__V1.2.6_200820_S3000332869.zip) |  |
| 1.2.3 | Applied to: [AE-DC5113-F6S](https://assets.hikvision.com/prd/public/all/files/202209/Firmware__V1.2.3_200525_S3000320925.zip) | 2020-05-25 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202209/Firmware__V1.2.3_200525_S3000320925.zip) |  |

</details>


<details>
<summary><h2>AE-DC5313-C6 - UNKNOWN (3 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 1.2.4 | Applied to: [AE-DC5313-C6](https://assets.hikvision.com/prd/public/all/files/202301/Firmware__V1.2.4_221209_S3000475000.zip) | 2022-12-09 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202301/Firmware__V1.2.4_221209_S3000475000.zip) |  |
| 1.1.6 | Applied to: [AE-DC5313-C6](https://assets.hikvision.com/prd/public/all/files/202210/Firmware__V1.1.6_220920_S3000456100.zip) | 2022-09-20 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202210/Firmware__V1.1.6_220920_S3000456100.zip) |  |
| 1.1.10 | Applied to: [AE-DC5313-C6](https://assets.hikvision.com/prd/public/all/files/202207/DashCam_AE_DC5313_C6_CN_STD_V1.1.10_build220223.zip) | 2022-02-23 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202207/DashCam_AE_DC5313_C6_CN_STD_V1.1.10_build220223.zip) |  |

</details>


<details>
<summary><h2>AE-DC5313-C6PRO - UNKNOWN (3 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 1.2.4 | Applied to: [AE-DC5313-C6PRO](https://assets.hikvision.com/prd/public/all/files/202301/Firmware__V1.2.4_221209_S3000475000.zip) | 2022-12-09 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202301/Firmware__V1.2.4_221209_S3000475000.zip) |  |
| 1.1.6 | Applied to: [AE-DC5313-C6PRO](https://assets.hikvision.com/prd/public/all/files/202207/DashCam_AE_DC5313_C6_EN_STD_V1.1.6_build211028.zip) | 2021-10-28 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202207/DashCam_AE_DC5313_C6_EN_STD_V1.1.6_build211028.zip) |  |
| 1.1.3 | Applied to: [AE-DC5313-C6PRO](https://assets.hikvision.com/prd/public/all/files/202207/DashCam_AE_DC5313_C6_CN_STD_V1.1.3_build201023.zip) | 2020-10-23 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202207/DashCam_AE_DC5313_C6_CN_STD_V1.1.3_build201023.zip) |  |

</details>


<details>
<summary><h2>AE-DC8012-C8 - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 1.2.3 | Applied to: [AE-DC8012-C8(2025)](https://assets.hikvision.com/prd/public/all/files/202306/Firmware__V1.2.3_230605_S3000503831.zip)(2ch) | 2023-06-05 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202306/Firmware__V1.2.3_230605_S3000503831.zip) |  |

</details>


<details>
<summary><h2>AE-DC8222-C8PRO - UNKNOWN (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 1.1.7 | Applied to: [AE-DC8222-C8PRO(3.5K)](https://assets.hikvision.com/prd/normal/all/files/202508/Firmware__V1.1.7_250807_S3000666340.zip)(2024) | 2025-08-07 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202508/Firmware__V1.1.7_250807_S3000666340.zip) |  |
| 1.1.3 | Applied to: [AE-DC8222-C8PRO(3.5K)](https://assets.hikvision.com/prd/public/all/files/202503/Firmware__V1.1.3_250304_S3000634438.zip)(2024) | 2025-03-04 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202503/Firmware__V1.1.3_250304_S3000634438.zip) |  |

</details>


<details>
<summary><h2>AE-DC8312-C6S - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 1.0.8 | Applied to: [AE-DC8312-C6S(GPS)](https://assets.hikvision.com/prd/normal/all/files/202509/Firmware__V1.0.8_250703_S3000666382.zip) | 2025-07-03 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202509/Firmware__V1.0.8_250703_S3000666382.zip) |  |

</details>


<details>
<summary><h2>AE-DC8322-G2PRO - UNKNOWN (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 1.1.7 | Applied to: [AE-DC8322-G2PRO(HK)](https://assets.hikvision.com/prd/public/all/files/202309/Firmware__V1.1.7_230919_S3000526629.zip)(GPS) | 2023-09-19 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202309/Firmware__V1.1.7_230919_S3000526629.zip) |  |
| 1.1.4 | Applied to: [AE-DC8322-G2PRO(HK)](https://assets.hikvision.com/prd/public/all/files/202208/Firmware__V1.1.4_220725_S3000443106.zip)(GPS) | 2022-07-25 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202208/Firmware__V1.1.4_220725_S3000443106.zip) |  |

</details>


<details>
<summary><h2>AE-DI2032-G40 - UNKNOWN (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 6.0.1 | Applied to: [AE-DI2032-G40(V2)](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V6.0.1_260104_S3000696935.zip)(B)(US)(Integrated) | 2026-01-04 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V6.0.1_260104_S3000696935.zip) |  |
| 5.1.2 | Applied to: [AE-DI2032-G40(B)](https://assets.hikvision.com/prd/public/all/files/202501/Firmware__V5.1.2_250102_S3000625549.zip)(EU) | 2025-01-02 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202501/Firmware__V5.1.2_250102_S3000625549.zip) |  |

</details>


<details>
<summary><h2>AE-DI5042-G4 - UNKNOWN (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 4.9.1 | Applied to: [AE-DI5042-G4(GPS+4G)](https://assets.hikvision.com/prd/public/all/files/202401/Firmware__V4.9.1_240118_S3000552549.zip)(Lite) | 2024-01-18 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202401/Firmware__V4.9.1_240118_S3000552549.zip) |  |
| 4.4.3 | Applied to: [AE-DI5042-G4(GPS+4G)](https://assets.hikvision.com/prd/public/all/files/020a231f-6ff3-452b-be5e-24b24bfac6d5.zip)(Lite) | 2022-03-18 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/020a231f-6ff3-452b-be5e-24b24bfac6d5.zip) |  |

</details>


<details>
<summary><h2>AE-DI5052-G40 - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 4.7.4 | Applied to: [AE-DI5052-G40](https://assets.hikvision.com/prd/normal/all/files/202511/Firmware__V4.7.4_251117_S3000685762.zip) PRO(EU) | 2025-11-17 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202511/Firmware__V4.7.4_251117_S3000685762.zip) |  |

</details>


<details>
<summary><h2>AE-MD5043-SD - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.1 | Applied to: [AE-MD5043-SD/GLF(EU-STD)](https://assets.hikvision.com/prd/public/all/files/202412/Firmware__V5.8.1_241121_S3000622031.zip) | 2024-11-21 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202412/Firmware__V5.8.1_241121_S3000622031.zip) |  |

</details>


<details>
<summary><h2>AE-MH0408 - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.1 | Applied to: [AE-MH0408(1T)](https://assets.hikvision.com/prd/public/all/files/202412/Firmware__V5.8.1_241121_S3000622073.zip)(RJ45) | 2024-11-21 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202412/Firmware__V5.8.1_241121_S3000622073.zip) |  |

</details>


<details>
<summary><h2>AE-VC1B1I-ISF - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 3.0.2 | Applied to: [AE-VC1B1I-ISF(RJ45)](https://assets.hikvision.com/prd/public/all/files/202406/1718922865963/Firmware__V3.0.2_240613_S3000580999.zip)(6mm) | 2024-06-13 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202406/1718922865963/Firmware__V3.0.2_240613_S3000580999.zip) |  |

</details>


<details>
<summary><h2>AE-VC215I-ISF - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 3.0.2 | Applied to: [AE-VC215I-ISF(M12)](https://assets.hikvision.com/prd/public/all/files/202305/Firmware__V3.0.2_230315_S3000488384.zip)(2.8mm) | 2023-03-15 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202305/Firmware__V3.0.2_230315_S3000488384.zip) |  |

</details>


<details>
<summary><h2>AE-VC583I-ISF - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 3.0.1 | Applied to: [AE-VC583I-IS/P(H)](https://assets.hikvision.com/prd/public/all/files/202303/Firmware__V3.0.1_230306_S3000485364.zip)(M12)(16mm) | 2023-03-06 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202303/Firmware__V3.0.1_230306_S3000485364.zip) |  |

</details>


<details>
<summary><h2>DS-1005KI - UNKNOWN (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 1.3.4 | Applied to: [DS-1005KI](https://assets.hikvision.com/prd/public/all/files/202506/Firmware__V1.3.4_S3000653240.zip) | 2020-25-06 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202506/Firmware__V1.3.4_S3000653240.zip) |  |
| 1.3.1 | Applied to: [DS-1005KI](https://assets.hikvision.com/prd/public/all/files/4e0fc5d3-bfdf-4c83-8120-5498fed38183.zip) | 2017-10-12 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/4e0fc5d3-bfdf-4c83-8120-5498fed38183.zip) |  |

</details>


<details>
<summary><h2>DS-1006KI - UNKNOWN (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 2.0.0 | Applied to: [DS-1006KI](https://assets.hikvision.com/prd/public/all/files/202309/Firmware__V2.0.0_230822_S3000522028.zip) | 2023-08-22 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202309/Firmware__V2.0.0_230822_S3000522028.zip) |  |
| 1.2.4 | Applied to: [DS-1006KI](https://assets.hikvision.com/prd/public/all/files/202301/Firmware__V1.2.4_220629_S3000442948.zip) | 2022-06-29 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202301/Firmware__V1.2.4_220629_S3000442948.zip) |  |

</details>


<details>
<summary><h2>DS-1100KI - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.1.2 | Applied to: [DS-1100KI(C)](https://assets.hikvision.com/prd/normal/all/files/202511/Firmware__V5.1.2_251024_S3000683492.zip) | 2025-10-24 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202511/Firmware__V5.1.2_251024_S3000683492.zip) |  |

</details>


<details>
<summary><h2>DS-1105KI - UNKNOWN (3 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.1.2 | Applied to: [DS-1105KI](https://assets.hikvision.com/prd/normal/all/files/202511/Firmware__V5.1.2_251024_S3000683489.zip) | 2025-10-24 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202511/Firmware__V5.1.2_251024_S3000683489.zip) |  |
| 4.6.0 | Applied to: [DS-1105KI](https://assets.hikvision.com/prd/public/all/files/202307/Firmware__V4.6.0_230704_S3000509505.zip) | 2023-07-04 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202307/Firmware__V4.6.0_230704_S3000509505.zip) |  |
| 1.1.0 | Applied to: [DS-1105KI](https://assets.hikvision.com/prd/public/all/files/202209/Firmware__V1.1.0_220914_S3000453160.zip) | 2022-09-14 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202209/Firmware__V1.1.0_220914_S3000453160.zip) |  |

</details>


<details>
<summary><h2>DS-1200KI - UNKNOWN (3 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 2.0.0 | Applied to: [DS-1200KI](https://assets.hikvision.com/prd/public/all/files/202309/Firmware__V2.0.0_230822_S3000522029.zip) | 2023-08-22 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202309/Firmware__V2.0.0_230822_S3000522029.zip) |  |
| 1.2.4 | Applied to: [DS-1200KI](https://assets.hikvision.com/prd/public/all/files/202212/Firmware__V1.2.4_220629_S3000442951.zip) | 2022-06-29 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202212/Firmware__V1.2.4_220629_S3000442951.zip) |  |
| 1.1.0 | Applied to: [DS-1200KI](https://assets.hikvision.com/prd/public/all/files/7cea2f2f-1de8-4ac1-a6cf-06213036f752.zip) | 2017-08-25 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/7cea2f2f-1de8-4ac1-a6cf-06213036f752.zip) |  |

</details>


<details>
<summary><h2>DS-2CD1023G0-IUF - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD1023G0-IUF(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202505/Firmware__V5.7.23_241211_S3000620671.zip)(C) | 2024-12-11 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202505/Firmware__V5.7.23_241211_S3000620671.zip) |  |

</details>


<details>
<summary><h2>DS-2CD1023G0E-I - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD1023G0E-I(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202505/Firmware__V5.7.23_241211_S3000620671.zip) | 2024-12-11 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202505/Firmware__V5.7.23_241211_S3000620671.zip) |  |
| 5.5.84 | Applied to: [DS-2CD1023G0E-I(2.8mm)](https://assets.hikvision.com/prd/public/all/files/c3afe62f-4071-4e50-a292-ded015321289.zip) | 2021-01-04 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/c3afe62f-4071-4e50-a292-ded015321289.zip) |  |

</details>


<details>
<summary><h2>DS-2CD1023G2-LIDUF - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.34 | Applied to: [DS-2CD1023G2-LIDUF/4G/SL(2.8)](https://assets.hikvision.com/prd/normal/all/files/202509/Firmware__V5.8.34_250908_S3000674318.zip)OSTD/LA/FUS | 2025-09-08 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202509/Firmware__V5.8.34_250908_S3000674318.zip) |  |

</details>


<details>
<summary><h2>DS-2CD1023G2-LIU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.10 | Applied to: [DS-2CD1023G2-LIUF(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202412/Firmware__V5.8.10_241205_S3000618834.zip) | 2024-12-05 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202412/Firmware__V5.8.10_241205_S3000618834.zip) |  |

</details>


<details>
<summary><h2>DS-2CD1023G2-LIUF - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.21 | Applied to: [DS-2CD1023G2-LIUF/SL(2.8mm)](https://assets.hikvision.com/prd/normal/all/files/202507/Firmware__V5.8.21_250714_S3000661481.zip) | 2025-07-14 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202507/Firmware__V5.8.21_250714_S3000661481.zip) |  |

</details>


<details>
<summary><h2>DS-2CD1027G2-L - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.10 | Applied to: [DS-2CD1027G2-LUF(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202412/Firmware__V5.8.10_241205_S3000618834.zip) | 2024-12-05 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202412/Firmware__V5.8.10_241205_S3000618834.zip) |  |

</details>


<details>
<summary><h2>DS-2CD1027G2H-LIU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.21 | Applied to: [DS-2CD1027G2H-LIUF(2.8mm)](https://assets.hikvision.com/prd/normal/all/files/202507/Firmware__V5.8.21_250714_S3000661481.zip) | 2025-07-14 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202507/Firmware__V5.8.21_250714_S3000661481.zip) |  |

</details>


<details>
<summary><h2>DS-2CD1027G2H-LIUF - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.21 | Applied to: [DS-2CD1027G2H-LIUF/SRB(2.8mm)](https://assets.hikvision.com/prd/normal/all/files/202507/Firmware__V5.8.21_250714_S3000661481.zip) | 2025-07-14 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202507/Firmware__V5.8.21_250714_S3000661481.zip) |  |

</details>


<details>
<summary><h2>DS-2CD1027G3-LIU - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.9.12 | Applied to: [DS-2CD1027G3-LIUF(2.8mm)](https://assets.hikvision.com/prd/normal/all/files/202509/Firmware__V5.9.12_250919_S3000675616.zip) | 2025-09-19 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202509/Firmware__V5.9.12_250919_S3000675616.zip) |  |
| 5.9.11 | Applied to: [DS-2CD1027G3-LIUF(2.8mm)](https://assets.hikvision.com/prd/normal/all/files/202508/Firmware__V5.9.11_250822_S3000669952.zip) | 2025-08-22 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202508/Firmware__V5.9.11_250822_S3000669952.zip) |  |

</details>


<details>
<summary><h2>DS-2CD1043G0-I - IPC_E7S (3 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD1043G0-IUF(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202505/Firmware__V5.7.23_241211_S3000620671.zip)(B) | 2024-12-11 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202505/Firmware__V5.7.23_241211_S3000620671.zip) |  |
| 5.5.820 | Applied to: [DS-2CD1043G0-IUF(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202312/Firmware__V5.5.820_231109_S3000539580.zip)(B) | 2023-11-09 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202312/Firmware__V5.5.820_231109_S3000539580.zip) |  |
| 5.5.88 | Applied to: [DS-2CD1043G0-IUF(2.8mm)](https://assets.hikvision.com/prd/public/all/files/01252820-85e5-4c30-ba88-1dd8b8e2d072.zip)(B) | 2020-06-10 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/01252820-85e5-4c30-ba88-1dd8b8e2d072.zip) |  |

</details>


<details>
<summary><h2>DS-2CD1043G2-LIDUF - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.34 | Applied to: [DS-2CD1043G2-LIDUF/4G/SL(2.8)](https://assets.hikvision.com/prd/normal/all/files/202509/Firmware__V5.8.34_250908_S3000674302.zip)OSTD/JP/FUS | 2025-09-08 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202509/Firmware__V5.8.34_250908_S3000674302.zip) |  |

</details>


<details>
<summary><h2>DS-2CD1043G2-LIU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.10 | Applied to: [DS-2CD1043G2-LIUF(2.8mm)](https://assets.hikvision.com/prd/normal/all/files/202507/Firmware__V5.8.10_250714_S3000661509.zip) | 2025-07-14 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202507/Firmware__V5.8.10_250714_S3000661509.zip) |  |

</details>


<details>
<summary><h2>DS-2CD1043G2-LIUF - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.10 | Applied to: [DS-2CD1043G2-LIUF/SL(2.8mm)](https://assets.hikvision.com/prd/normal/all/files/202507/Firmware__V5.8.10_250714_S3000661518.zip) | 2025-07-14 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202507/Firmware__V5.8.10_250714_S3000661518.zip) |  |

</details>


<details>
<summary><h2>DS-2CD1047G2-L - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.10 | Applied to: [DS-2CD1047G2-LUF(2.8mm)](https://assets.hikvision.com/prd/normal/all/files/202507/Firmware__V5.8.10_250714_S3000661509.zip) | 2025-07-14 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202507/Firmware__V5.8.10_250714_S3000661509.zip) |  |

</details>


<details>
<summary><h2>DS-2CD1047G2H-LIU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.10 | Applied to: [DS-2CD1047G2H-LIU(2.8mm)](https://assets.hikvision.com/prd/normal/all/files/202507/Firmware__V5.8.10_250714_S3000661518.zip)(BLACK) | 2025-07-14 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202507/Firmware__V5.8.10_250714_S3000661518.zip) |  |

</details>


<details>
<summary><h2>DS-2CD1047G2H-LIUF - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.10 | Applied to: [DS-2CD1047G2H-LIUF/SRB(2.8mm)](https://assets.hikvision.com/prd/normal/all/files/202507/Firmware__V5.8.10_250714_S3000661518.zip) | 2025-07-14 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202507/Firmware__V5.8.10_250714_S3000661518.zip) |  |

</details>


<details>
<summary><h2>DS-2CD1047G3-LIU - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.9.12 | Applied to: [DS-2CD1047G3-LIUF(2.8mm)](https://assets.hikvision.com/prd/normal/all/files/202509/Firmware__V5.9.12_250919_S3000675616.zip) | 2025-09-19 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202509/Firmware__V5.9.12_250919_S3000675616.zip) |  |
| 5.9.11 | Applied to: [DS-2CD1047G3-LIUF(2.8mm)](https://assets.hikvision.com/prd/normal/all/files/202508/Firmware__V5.9.11_250822_S3000669952.zip) | 2025-08-22 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202508/Firmware__V5.9.11_250822_S3000669952.zip) |  |

</details>


<details>
<summary><h2>DS-2CD1047G3H-LIU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.21 | Applied to: [DS-2CD1047G3H-LIU/SRB(2.8mm)](https://assets.hikvision.com/prd/normal/all/files/202512/Firmware__V5.8.21_251117_S3000687895.zip) | 2025-11-17 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202512/Firmware__V5.8.21_251117_S3000687895.zip) |  |

</details>


<details>
<summary><h2>DS-2CD1053G0-I - IPC_G0 (3 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD1053G0-I(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202410/Firmware__V5.7.23_241008_S3000605524.zip) | 2024-10-08 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202410/Firmware__V5.7.23_241008_S3000605524.zip) |  |
| 5.5.800 | Applied to: [DS-2CD1053G0-I(2.8mm)](https://assets.hikvision.com/prd/public/all/files/af64952b-34be-46d9-94b8-3bf76fb5a5f4.zip) | 2021-08-16 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/af64952b-34be-46d9-94b8-3bf76fb5a5f4.zip) |  |
| 5.5.89 | Applied to: [DS-2CD1053G0-I(2.8mm)](https://assets.hikvision.com/prd/public/all/files/87acab3e-5d46-45cd-88c4-87b51139b600.zip) | 2021-04-29 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/87acab3e-5d46-45cd-88c4-87b51139b600.zip) |  |

</details>


<details>
<summary><h2>DS-2CD1067G2H-LIUF - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.21 | Applied to: [DS-2CD1067G2H-LIUF/SRB(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202505/Firmware__V5.8.21_250508_S3000647345.zip) | 2025-05-08 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202505/Firmware__V5.8.21_250508_S3000647345.zip) |  |

</details>


<details>
<summary><h2>DS-2CD1067G3-LIU - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.9.12 | Applied to: [DS-2CD1067G3-LIUF/SRB(2.8mm)](https://assets.hikvision.com/prd/normal/all/files/202509/Firmware__V5.9.12_250919_S3000675616.zip) | 2025-09-19 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202509/Firmware__V5.9.12_250919_S3000675616.zip) |  |
| 5.9.11 | Applied to: [DS-2CD1067G3-LIUF/SRB(2.8mm)](https://assets.hikvision.com/prd/normal/all/files/202508/Firmware__V5.9.11_250822_S3000669952.zip) | 2025-08-22 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202508/Firmware__V5.9.11_250822_S3000669952.zip) |  |

</details>


<details>
<summary><h2>DS-2CD1083G0-I - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD1083G0-I(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202410/Firmware__V5.7.23_241008_S3000605524.zip)(C) | 2024-10-08 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202410/Firmware__V5.7.23_241008_S3000605524.zip) |  |

</details>


<details>
<summary><h2>DS-2CD1083G0-IUF - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD1083G0-IUF(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202410/Firmware__V5.7.23_241008_S3000605524.zip)(C) | 2024-10-08 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202410/Firmware__V5.7.23_241008_S3000605524.zip) |  |

</details>


<details>
<summary><h2>DS-2CD1123G0-IUF - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD1123G0-IUF(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202505/Firmware__V5.7.23_241211_S3000620671.zip)(C) | 2024-12-11 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202505/Firmware__V5.7.23_241211_S3000620671.zip) |  |

</details>


<details>
<summary><h2>DS-2CD1123G0E-I - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD1123G0E-I(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202505/Firmware__V5.7.23_241211_S3000620671.zip) | 2024-12-11 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202505/Firmware__V5.7.23_241211_S3000620671.zip) |  |
| 5.5.84 | Applied to: [DS-2CD1123G0E-I(2.8mm)](https://assets.hikvision.com/prd/public/all/files/c3afe62f-4071-4e50-a292-ded015321289.zip) | 2021-01-04 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/c3afe62f-4071-4e50-a292-ded015321289.zip) |  |

</details>


<details>
<summary><h2>DS-2CD1123G2-LIU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.10 | Applied to: [DS-2CD1123G2-LIUF(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202412/Firmware__V5.8.10_241205_S3000618834.zip) | 2024-12-05 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202412/Firmware__V5.8.10_241205_S3000618834.zip) |  |

</details>


<details>
<summary><h2>DS-2CD1127G2-L - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.10 | Applied to: [DS-2CD1127G2-LUF(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202412/Firmware__V5.8.10_241205_S3000618834.zip) | 2024-12-05 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202412/Firmware__V5.8.10_241205_S3000618834.zip) |  |

</details>


<details>
<summary><h2>DS-2CD1127G2H-LIU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.21 | Applied to: [DS-2CD1127G2H-LIU(2.8mm)](https://assets.hikvision.com/prd/normal/all/files/202507/Firmware__V5.8.21_250714_S3000661481.zip) | 2025-07-14 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202507/Firmware__V5.8.21_250714_S3000661481.zip) |  |

</details>


<details>
<summary><h2>DS-2CD1127G3-LIU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.9.12 | Applied to: [DS-2CD1127G3-LIUF(2.8mm)](https://assets.hikvision.com/prd/normal/all/files/202509/Firmware__V5.9.12_250919_S3000675616.zip) | 2025-09-19 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202509/Firmware__V5.9.12_250919_S3000675616.zip) |  |

</details>


<details>
<summary><h2>DS-2CD1143G0-I - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD1143G0-I(4mm)](https://assets.hikvision.com/prd/public/all/files/202505/Firmware__V5.7.23_241211_S3000620671.zip) | 2024-12-11 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202505/Firmware__V5.7.23_241211_S3000620671.zip) |  |
| 5.5.88 | Applied to: [DS-2CD1143G0-I(4mm)](https://assets.hikvision.com/prd/public/all/files/01252820-85e5-4c30-ba88-1dd8b8e2d072.zip) | 2020-06-10 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/01252820-85e5-4c30-ba88-1dd8b8e2d072.zip) |  |

</details>


<details>
<summary><h2>DS-2CD1143G2-LIU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.10 | Applied to: [DS-2CD1143G2-LIUF(2.8mm)](https://assets.hikvision.com/prd/normal/all/files/202507/Firmware__V5.8.10_250714_S3000661509.zip) | 2025-07-14 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202507/Firmware__V5.8.10_250714_S3000661509.zip) |  |

</details>


<details>
<summary><h2>DS-2CD1147G2-L - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.10 | Applied to: [DS-2CD1147G2-L(2.8mm)](https://assets.hikvision.com/prd/normal/all/files/202507/Firmware__V5.8.10_250714_S3000661509.zip) | 2025-07-14 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202507/Firmware__V5.8.10_250714_S3000661509.zip) |  |

</details>


<details>
<summary><h2>DS-2CD1147G2H-LIU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.10 | Applied to: [DS-2CD1147G2H-LIU(2.8mm)](https://assets.hikvision.com/prd/normal/all/files/202507/Firmware__V5.8.10_250714_S3000661518.zip)(BLACK) | 2025-07-14 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202507/Firmware__V5.8.10_250714_S3000661518.zip) |  |

</details>


<details>
<summary><h2>DS-2CD1147G3-LIU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.9.12 | Applied to: [DS-2CD1147G3-LIUF(2.8mm)](https://assets.hikvision.com/prd/normal/all/files/202509/Firmware__V5.9.12_250919_S3000675616.zip) | 2025-09-19 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202509/Firmware__V5.9.12_250919_S3000675616.zip) |  |

</details>


<details>
<summary><h2>DS-2CD1147G3H-LIU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.21 | Applied to: [DS-2CD1147G3H-LIUF(2.8mm)](https://assets.hikvision.com/prd/normal/all/files/202512/Firmware__V5.8.21_251117_S3000687895.zip) | 2025-11-17 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202512/Firmware__V5.8.21_251117_S3000687895.zip) |  |

</details>


<details>
<summary><h2>DS-2CD1153G0-I - IPC_G0 (3 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD1153G0-I(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202410/Firmware__V5.7.23_241008_S3000605524.zip) | 2024-10-08 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202410/Firmware__V5.7.23_241008_S3000605524.zip) |  |
| 5.5.800 | Applied to: [DS-2CD1153G0-I(2.8mm)](https://assets.hikvision.com/prd/public/all/files/af64952b-34be-46d9-94b8-3bf76fb5a5f4.zip) | 2021-08-16 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/af64952b-34be-46d9-94b8-3bf76fb5a5f4.zip) |  |
| 5.5.89 | Applied to: [DS-2CD1153G0-I(2.8mm)](https://assets.hikvision.com/prd/public/all/files/87acab3e-5d46-45cd-88c4-87b51139b600.zip) | 2021-04-29 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/87acab3e-5d46-45cd-88c4-87b51139b600.zip) |  |

</details>


<details>
<summary><h2>DS-2CD1167G3-LIU - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.9.12 | Applied to: [DS-2CD1167G3-LIUF(2.8mm)](https://assets.hikvision.com/prd/normal/all/files/202509/Firmware__V5.9.12_250919_S3000675616.zip) | 2025-09-19 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202509/Firmware__V5.9.12_250919_S3000675616.zip) |  |
| 5.9.11 | Applied to: [DS-2CD1167G3-LIUF(2.8mm)](https://assets.hikvision.com/prd/normal/all/files/202508/Firmware__V5.9.11_250822_S3000669952.zip) | 2025-08-22 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202508/Firmware__V5.9.11_250822_S3000669952.zip) |  |

</details>


<details>
<summary><h2>DS-2CD1183G0-I - IPC_G0 (3 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.19 | Applied to: [DS-2CD1183G0-I(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202412/Firmware__V5.7.19_241207_S3000618481.zip) | 2024-12-07 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202412/Firmware__V5.7.19_241207_S3000618481.zip) |  |
| 5.7.23 | Applied to: [DS-2CD1183G0-I(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202410/Firmware__V5.7.23_241008_S3000605524.zip) | 2024-10-08 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202410/Firmware__V5.7.23_241008_S3000605524.zip) |  |
| 5.7.18 | Applied to: [DS-2CD1183G0-I(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202409/Firmware__V5.7.18_240826_S3000597013.zip) | 2024-08-26 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202409/Firmware__V5.7.18_240826_S3000597013.zip) |  |

</details>


<details>
<summary><h2>DS-2CD1183G0-IUF - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD1183G0-IUF(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202410/Firmware__V5.7.23_241008_S3000605524.zip) | 2024-10-08 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202410/Firmware__V5.7.23_241008_S3000605524.zip) |  |
| 5.7.18 | Applied to: [DS-2CD1183G0-IUF(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202409/Firmware__V5.7.18_240826_S3000597013.zip) | 2024-08-26 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202409/Firmware__V5.7.18_240826_S3000597013.zip) |  |

</details>


<details>
<summary><h2>DS-2CD1323G0-IUF - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD1323G0-IUF(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202505/Firmware__V5.7.23_241211_S3000620671.zip)(C) | 2024-12-11 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202505/Firmware__V5.7.23_241211_S3000620671.zip) |  |

</details>


<details>
<summary><h2>DS-2CD1323G0E-I - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD1323G0E-I(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202505/Firmware__V5.7.23_241211_S3000620671.zip) | 2024-12-11 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202505/Firmware__V5.7.23_241211_S3000620671.zip) |  |
| 5.5.84 | Applied to: [DS-2CD1323G0E-I(2.8mm)](https://assets.hikvision.com/prd/public/all/files/c3afe62f-4071-4e50-a292-ded015321289.zip) | 2021-01-04 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/c3afe62f-4071-4e50-a292-ded015321289.zip) |  |

</details>


<details>
<summary><h2>DS-2CD1323G2-LIU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.10 | Applied to: [DS-2CD1323G2-LIUF(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202412/Firmware__V5.8.10_241205_S3000618834.zip) | 2024-12-05 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202412/Firmware__V5.8.10_241205_S3000618834.zip) |  |

</details>


<details>
<summary><h2>DS-2CD1323G2-LIUF - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.21 | Applied to: [DS-2CD1323G2-LIUF/SL(2.8mm)](https://assets.hikvision.com/prd/normal/all/files/202507/Firmware__V5.8.21_250714_S3000661481.zip) | 2025-07-14 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202507/Firmware__V5.8.21_250714_S3000661481.zip) |  |

</details>


<details>
<summary><h2>DS-2CD1327G2-L - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.10 | Applied to: [DS-2CD1327G2-LUF(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202412/Firmware__V5.8.10_241205_S3000618834.zip) | 2024-12-05 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202412/Firmware__V5.8.10_241205_S3000618834.zip) |  |

</details>


<details>
<summary><h2>DS-2CD1327G2H-LIU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.21 | Applied to: [DS-2CD1327G2H-LIUF(2.8mm)](https://assets.hikvision.com/prd/normal/all/files/202507/Firmware__V5.8.21_250714_S3000661481.zip) | 2025-07-14 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202507/Firmware__V5.8.21_250714_S3000661481.zip) |  |

</details>


<details>
<summary><h2>DS-2CD1327G2H-LIUF - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.21 | Applied to: [DS-2CD1327G2H-LIUF/SL(2.8mm)](https://assets.hikvision.com/prd/normal/all/files/202507/Firmware__V5.8.21_250714_S3000661481.zip) | 2025-07-14 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202507/Firmware__V5.8.21_250714_S3000661481.zip) |  |

</details>


<details>
<summary><h2>DS-2CD1327G3-LIU - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.9.12 | Applied to: [DS-2CD1327G3-LIUF/SRB(2.8mm)](https://assets.hikvision.com/prd/normal/all/files/202509/Firmware__V5.9.12_250919_S3000675616.zip) | 2025-09-19 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202509/Firmware__V5.9.12_250919_S3000675616.zip) |  |
| 5.9.11 | Applied to: [DS-2CD1327G3-LIUF/SRB(2.8mm)](https://assets.hikvision.com/prd/normal/all/files/202508/Firmware__V5.9.11_250822_S3000669952.zip) | 2025-08-22 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202508/Firmware__V5.9.11_250822_S3000669952.zip) |  |

</details>


<details>
<summary><h2>DS-2CD1343G0-I - IPC_E7S (3 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD1343G0-I(4mm)](https://assets.hikvision.com/prd/public/all/files/202505/Firmware__V5.7.23_241211_S3000620671.zip) | 2024-12-11 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202505/Firmware__V5.7.23_241211_S3000620671.zip) |  |
| 5.5.820 | Applied to: [DS-2CD1343G0-I(4mm)](https://assets.hikvision.com/prd/public/all/files/202312/Firmware__V5.5.820_231109_S3000539580.zip) | 2023-11-09 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202312/Firmware__V5.5.820_231109_S3000539580.zip) |  |
| 5.5.88 | Applied to: [DS-2CD1343G0-I(4mm)](https://assets.hikvision.com/prd/public/all/files/01252820-85e5-4c30-ba88-1dd8b8e2d072.zip) | 2020-06-10 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/01252820-85e5-4c30-ba88-1dd8b8e2d072.zip) |  |

</details>


<details>
<summary><h2>DS-2CD1343G2-LIU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.10 | Applied to: [DS-2CD1343G2-LIU(2.8mm)](https://assets.hikvision.com/prd/normal/all/files/202507/Firmware__V5.8.10_250714_S3000661509.zip)(BLACK) | 2025-07-14 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202507/Firmware__V5.8.10_250714_S3000661509.zip) |  |

</details>


<details>
<summary><h2>DS-2CD1343G2-LIUF - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.10 | Applied to: [DS-2CD1343G2-LIUF/SL(2.8mm)](https://assets.hikvision.com/prd/normal/all/files/202507/Firmware__V5.8.10_250714_S3000661518.zip) | 2025-07-14 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202507/Firmware__V5.8.10_250714_S3000661518.zip) |  |

</details>


<details>
<summary><h2>DS-2CD1347G2-L - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.10 | Applied to: [DS-2CD1347G2-LUF(2.8mm)](https://assets.hikvision.com/prd/normal/all/files/202507/Firmware__V5.8.10_250714_S3000661509.zip) | 2025-07-14 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202507/Firmware__V5.8.10_250714_S3000661509.zip) |  |

</details>


<details>
<summary><h2>DS-2CD1347G2H-LIU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.10 | Applied to: [DS-2CD1347G2H-LIU(2.8mm)](https://assets.hikvision.com/prd/normal/all/files/202507/Firmware__V5.8.10_250714_S3000661518.zip) | 2025-07-14 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202507/Firmware__V5.8.10_250714_S3000661518.zip) |  |

</details>


<details>
<summary><h2>DS-2CD1347G2H-LIUF - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.10 | Applied to: [DS-2CD1347G2H-LIUF/SL(2.8mm)](https://assets.hikvision.com/prd/normal/all/files/202507/Firmware__V5.8.10_250714_S3000661518.zip) | 2025-07-14 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202507/Firmware__V5.8.10_250714_S3000661518.zip) |  |

</details>


<details>
<summary><h2>DS-2CD1347G3-LIU - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.9.12 | Applied to: [DS-2CD1347G3-LIUF/SL(2.8mm)](https://assets.hikvision.com/prd/normal/all/files/202509/Firmware__V5.9.12_250919_S3000675616.zip) | 2025-09-19 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202509/Firmware__V5.9.12_250919_S3000675616.zip) |  |
| 5.9.11 | Applied to: [DS-2CD1347G3-LIUF/SL(2.8mm)](https://assets.hikvision.com/prd/normal/all/files/202508/Firmware__V5.9.11_250822_S3000669952.zip) | 2025-08-22 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202508/Firmware__V5.9.11_250822_S3000669952.zip) |  |

</details>


<details>
<summary><h2>DS-2CD1347G3H-LIU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.21 | Applied to: [DS-2CD1347G3H-LIU(2.8mm)](https://assets.hikvision.com/prd/normal/all/files/202512/Firmware__V5.8.21_251117_S3000687895.zip) | 2025-11-17 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202512/Firmware__V5.8.21_251117_S3000687895.zip) |  |

</details>


<details>
<summary><h2>DS-2CD1353G0-I - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD1353G0-I(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202410/Firmware__V5.7.23_241008_S3000605524.zip)(C) | 2024-10-08 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202410/Firmware__V5.7.23_241008_S3000605524.zip) |  |

</details>


<details>
<summary><h2>DS-2CD1363G2P-LIUF - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.11 | Applied to: [DS-2CD1363G2P-LIUF/SL(2.8mm)](https://assets.hikvision.com/prd/normal/all/files/202511/Firmware__V5.8.11_251029_S3000683386.zip) | 2025-10-29 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202511/Firmware__V5.8.11_251029_S3000683386.zip) |  |

</details>


<details>
<summary><h2>DS-2CD1367G2H-LIUF - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.21 | Applied to: [DS-2CD1367G2H-LIUF/SRB(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202505/Firmware__V5.8.21_250508_S3000647345.zip) | 2025-05-08 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202505/Firmware__V5.8.21_250508_S3000647345.zip) |  |

</details>


<details>
<summary><h2>DS-2CD1367G2HP-LIUF - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.11 | Applied to: [DS-2CD1367G2HP-LIUF/SL(2.8mm)](https://assets.hikvision.com/prd/normal/all/files/202511/Firmware__V5.8.11_251029_S3000683386.zip) | 2025-10-29 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202511/Firmware__V5.8.11_251029_S3000683386.zip) |  |

</details>


<details>
<summary><h2>DS-2CD1367G3-LIU - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.9.12 | Applied to: [DS-2CD1367G3-LIU/SRB(2.8mm)](https://assets.hikvision.com/prd/normal/all/files/202509/Firmware__V5.9.12_250919_S3000675616.zip) | 2025-09-19 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202509/Firmware__V5.9.12_250919_S3000675616.zip) |  |
| 5.9.11 | Applied to: [DS-2CD1367G3-LIU/SRB(2.8mm)](https://assets.hikvision.com/prd/normal/all/files/202508/Firmware__V5.9.11_250822_S3000669952.zip) | 2025-08-22 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202508/Firmware__V5.9.11_250822_S3000669952.zip) |  |

</details>


<details>
<summary><h2>DS-2CD1383G0-I - IPC_G0 (3 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.19 | Applied to: [DS-2CD1383G0-I(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202412/Firmware__V5.7.19_241207_S3000618481.zip) | 2024-12-07 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202412/Firmware__V5.7.19_241207_S3000618481.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.19_241207_Release_Note.pdf) |
| 5.7.23 | Applied to: [DS-2CD1383G0-I(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202410/Firmware__V5.7.23_241008_S3000605524.zip)(C) | 2024-10-08 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202410/Firmware__V5.7.23_241008_S3000605524.zip) |  |
| 5.7.18 | Applied to: [DS-2CD1383G0-I(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202409/Firmware__V5.7.18_240826_S3000597013.zip) | 2024-08-26 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202409/Firmware__V5.7.18_240826_S3000597013.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.19_241207_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD1383G0-IUF - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD1383G0-IUF(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202410/Firmware__V5.7.23_241008_S3000605524.zip) | 2024-10-08 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202410/Firmware__V5.7.23_241008_S3000605524.zip) |  |
| 5.7.18 | Applied to: [DS-2CD1383G0-IUF(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202409/Firmware__V5.7.18_240826_S3000597013.zip) | 2024-08-26 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202409/Firmware__V5.7.18_240826_S3000597013.zip) |  |

</details>


<details>
<summary><h2>DS-2CD1383G2P-LIUF - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.11 | Applied to: [DS-2CD1383G2P-LIUF/SL(2mm)](https://assets.hikvision.com/prd/normal/all/files/202511/Firmware__V5.8.11_251029_S3000683386.zip) | 2025-10-29 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202511/Firmware__V5.8.11_251029_S3000683386.zip) |  |

</details>


<details>
<summary><h2>DS-2CD1623G0-I - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD1623G0-IZ(2.8-12mm)](https://assets.hikvision.com/prd/public/all/files/202505/Firmware__V5.7.23_241211_S3000620665.zip) | 2024-12-11 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202505/Firmware__V5.7.23_241211_S3000620665.zip) |  |
| 5.5.800 | Applied to: [DS-2CD1623G0-IZ(2.8-12mm)](https://assets.hikvision.com/prd/public/all/files/5d0fc94c-b0e2-48ab-9a55-9c49876b7081.zip) | 2021-06-28 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/5d0fc94c-b0e2-48ab-9a55-9c49876b7081.zip) |  |

</details>


<details>
<summary><h2>DS-2CD1623G2-IZ - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.10 | Applied to: [DS-2CD1623G2-IZ(2.8-12mm)](https://assets.hikvision.com/prd/normal/all/files/202507/Firmware__V5.8.10_250714_S3000661509.zip) | 2025-07-14 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202507/Firmware__V5.8.10_250714_S3000661509.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202508/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-E10.pdf) |

</details>


<details>
<summary><h2>DS-2CD1623G2-LIU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.21 | Applied to: [DS-2CD1B23G2-LIU(2.8mm)](https://assets.hikvision.com/prd/normal/all/files/202507/Firmware__V5.8.21_250714_S3000661481.zip) | 2025-07-14 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202507/Firmware__V5.8.21_250714_S3000661481.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202508/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-E9.pdf) |

</details>


<details>
<summary><h2>DS-2CD1623G2-LIZ - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.10 | Applied to: [DS-2CD1623G2-LIZSU(2.8-12mm)](https://assets.hikvision.com/prd/normal/all/files/202507/Firmware__V5.8.10_250714_S3000661509.zip) | 2025-07-14 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202507/Firmware__V5.8.10_250714_S3000661509.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202508/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-E10.pdf) |

</details>


<details>
<summary><h2>DS-2CD1627G2H-LIU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.21 | Applied to: [DS-2CD1B27G2H-LIUF(2.8mm)](https://assets.hikvision.com/prd/normal/all/files/202507/Firmware__V5.8.21_250714_S3000661481.zip) | 2025-07-14 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202507/Firmware__V5.8.21_250714_S3000661481.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202508/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-E9.pdf) |

</details>


<details>
<summary><h2>DS-2CD1643G0-I - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD1643G0-IZ(2.8-12mm)](https://assets.hikvision.com/prd/public/all/files/202505/Firmware__V5.7.23_241211_S3000620665.zip) | 2024-12-11 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202505/Firmware__V5.7.23_241211_S3000620665.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202312/releasenote%5CNetwork_Camera_V5.5.89_Release_Note_--G0.pdf) |
| 5.5.89 | Applied to: [DS-2CD1643G0-IZ(2.8-12mm)](https://assets.hikvision.com/prd/public/all/files/87acab3e-5d46-45cd-88c4-87b51139b600.zip) | 2021-04-29 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/87acab3e-5d46-45cd-88c4-87b51139b600.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202312/releasenote%5CNetwork_Camera_V5.5.89_Release_Note_--G0.pdf) |

</details>


<details>
<summary><h2>DS-2CD1643G2-IZ - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.10 | Applied to: [DS-2CD1643G2-IZ(2.8-12mm)](https://assets.hikvision.com/prd/normal/all/files/202507/Firmware__V5.8.10_250714_S3000661509.zip) | 2025-07-14 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202507/Firmware__V5.8.10_250714_S3000661509.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202508/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-E10.pdf) |

</details>


<details>
<summary><h2>DS-2CD1643G2-LIU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.10 | Applied to: [DS-2CD1B43G2-LIU(2.8mm)](https://assets.hikvision.com/prd/normal/all/files/202507/Firmware__V5.8.10_250714_S3000661518.zip) | 2025-07-14 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202507/Firmware__V5.8.10_250714_S3000661518.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202508/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-E10.pdf) |

</details>


<details>
<summary><h2>DS-2CD1643G2-LIZ - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.10 | Applied to: [DS-2CD1643G2-LIZU(2.8-12mm)](https://assets.hikvision.com/prd/normal/all/files/202507/Firmware__V5.8.10_250714_S3000661509.zip) | 2025-07-14 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202507/Firmware__V5.8.10_250714_S3000661509.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202508/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-E10.pdf) |

</details>


<details>
<summary><h2>DS-2CD1647G2H-LIU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.10 | Applied to: [DS-2CD1B47G2H-LIUF(2.8mm)](https://assets.hikvision.com/prd/normal/all/files/202507/Firmware__V5.8.10_250714_S3000661518.zip) | 2025-07-14 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202507/Firmware__V5.8.10_250714_S3000661518.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202508/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-E10.pdf) |

</details>


<details>
<summary><h2>DS-2CD1653G0-I - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD1653G0-IZ(2.8-12mm)](https://assets.hikvision.com/prd/public/all/files/202410/Firmware__V5.7.23_241008_S3000605507.zip)(C) | 2024-10-08 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202410/Firmware__V5.7.23_241008_S3000605507.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202507/releasenote%5CNetwork_Camera-V5.7.23_SP_Release_Note-E8.pdf) |

</details>


<details>
<summary><h2>DS-2CD1723G0-I - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD1723G0-I(2.8-12mm)](https://assets.hikvision.com/prd/public/all/files/202505/Firmware__V5.7.23_241211_S3000620665.zip) | 2024-12-11 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202505/Firmware__V5.7.23_241211_S3000620665.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202507/releasenote%5CNetwork_Camera-V5.7.23_SP2_Release_Note-E8.pdf) |
| 5.5.800 | Applied to: [DS-2CD1723G0-I(2.8-12mm)](https://assets.hikvision.com/prd/public/all/files/5d0fc94c-b0e2-48ab-9a55-9c49876b7081.zip) | 2021-06-28 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/5d0fc94c-b0e2-48ab-9a55-9c49876b7081.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202507/releasenote%5CNetwork_Camera-V5.7.23_SP2_Release_Note-E8.pdf) |

</details>


<details>
<summary><h2>DS-2CD1723G2-IZ - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.10 | Applied to: [DS-2CD1723G2-IZS(2.8-12mm)](https://assets.hikvision.com/prd/normal/all/files/202507/Firmware__V5.8.10_250714_S3000661509.zip) | 2025-07-14 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202507/Firmware__V5.8.10_250714_S3000661509.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202508/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-E10.pdf) |

</details>


<details>
<summary><h2>DS-2CD1723G2-LIZ - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.10 | Applied to: [DS-2CD1723G2-LIZU(2.8-12mm)](https://assets.hikvision.com/prd/normal/all/files/202507/Firmware__V5.8.10_250714_S3000661509.zip) | 2025-07-14 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202507/Firmware__V5.8.10_250714_S3000661509.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202508/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-E10.pdf) |

</details>


<details>
<summary><h2>DS-2CD1743G0-I - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD1743G0-I(2.8-12mm)](https://assets.hikvision.com/prd/public/all/files/202505/Firmware__V5.7.23_241211_S3000620665.zip) | 2024-12-11 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202505/Firmware__V5.7.23_241211_S3000620665.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202312/releasenote%5CNetwork_Camera_V5.5.89_Release_Note_--G0.pdf) |
| 5.5.89 | Applied to: [DS-2CD1743G0-I(2.8-12mm)](https://assets.hikvision.com/prd/public/all/files/87acab3e-5d46-45cd-88c4-87b51139b600.zip) | 2021-04-29 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/87acab3e-5d46-45cd-88c4-87b51139b600.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202312/releasenote%5CNetwork_Camera_V5.5.89_Release_Note_--G0.pdf) |

</details>


<details>
<summary><h2>DS-2CD1743G2-IZ - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.10 | Applied to: [DS-2CD1743G2-IZ(2.8-12mm)](https://assets.hikvision.com/prd/normal/all/files/202507/Firmware__V5.8.10_250714_S3000661509.zip) | 2025-07-14 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202507/Firmware__V5.8.10_250714_S3000661509.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202508/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-E10.pdf) |

</details>


<details>
<summary><h2>DS-2CD1743G2-LIZ - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.10 | Applied to: [DS-2CD1743G2-LIZU(2.8-12mm)](https://assets.hikvision.com/prd/normal/all/files/202507/Firmware__V5.8.10_250714_S3000661509.zip) | 2025-07-14 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202507/Firmware__V5.8.10_250714_S3000661509.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202508/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-E10.pdf) |

</details>


<details>
<summary><h2>DS-2CD1753G0-I - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD1753G0-IZ(2.8-12mm)](https://assets.hikvision.com/prd/public/all/files/202410/Firmware__V5.7.23_241008_S3000605507.zip)(C) | 2024-10-08 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202410/Firmware__V5.7.23_241008_S3000605507.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202507/releasenote%5CNetwork_Camera-V5.7.23_SP_Release_Note-E8.pdf) |

</details>


<details>
<summary><h2>DS-2CD1A23G0-IZU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD1A23G0-IZU(2.8-12mm)](https://assets.hikvision.com/prd/public/all/files/202410/Firmware__V5.7.23_241008_S3000605507.zip) | 2024-10-08 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202410/Firmware__V5.7.23_241008_S3000605507.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202507/releasenote%5CNetwork_Camera-V5.7.23_SP_Release_Note-E8.pdf) |

</details>


<details>
<summary><h2>DS-2CD1A43G0-IZU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD1A43G0-IZU(2.8-12mm)](https://assets.hikvision.com/prd/public/all/files/202410/Firmware__V5.7.23_241008_S3000605507.zip) | 2024-10-08 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202410/Firmware__V5.7.23_241008_S3000605507.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202507/releasenote%5CNetwork_Camera-V5.7.23_SP_Release_Note-E8.pdf) |

</details>


<details>
<summary><h2>DS-2CD1B23G2-LIUF - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.21 | Applied to: [DS-2CD1B23G2-LIUF/SL(2.8mm)](https://assets.hikvision.com/prd/normal/all/files/202507/Firmware__V5.8.21_250714_S3000661481.zip) | 2025-07-14 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202507/Firmware__V5.8.21_250714_S3000661481.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202508/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-E9.pdf) |

</details>


<details>
<summary><h2>DS-2CD1B27G2H-LIUF - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.21 | Applied to: [DS-2CD1B27G2H-LIUF/SL(2.8mm)](https://assets.hikvision.com/prd/normal/all/files/202507/Firmware__V5.8.21_250714_S3000661481.zip) | 2025-07-14 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202507/Firmware__V5.8.21_250714_S3000661481.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202508/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-E9.pdf) |

</details>


<details>
<summary><h2>DS-2CD1B27G3-LIU - IPC_G0 (3 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.9.13 | Applied to: [DS-2CD1B27G3-LIUF/LSRB(2.8mm)](https://assets.hikvision.com/prd/normal/all/files/202512/Firmware__V5.9.13_251124_S3000688200.zip) | 2025-11-24 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202512/Firmware__V5.9.13_251124_S3000688200.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.9.13_251124_Release_Note-IPCE_E_E15.pdf) |
| 5.9.12 | Applied to: [DS-2CD1B27G3-LIU/SRB(2.8mm)](https://assets.hikvision.com/prd/normal/all/files/202509/Firmware__V5.9.12_250919_S3000675616.zip) | 2025-09-19 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202509/Firmware__V5.9.12_250919_S3000675616.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202511/releasenote%5CNetwork_Camera-V5.9.12_250919_Release_Note-IPCE_E_E15.pdf) |
| 5.9.11 | Applied to: [DS-2CD1B27G3-LIU/SRB(2.8mm)](https://assets.hikvision.com/prd/normal/all/files/202508/Firmware__V5.9.11_250822_S3000669952.zip) | 2025-08-22 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202508/Firmware__V5.9.11_250822_S3000669952.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202511/releasenote%5CNetwork_Camera-V5.9.12_250919_Release_Note-IPCE_E_E15.pdf) |

</details>


<details>
<summary><h2>DS-2CD1B43G2-LIUF - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.10 | Applied to: [DS-2CD1B43G2-LIUF/SL(2.8mm)](https://assets.hikvision.com/prd/normal/all/files/202507/Firmware__V5.8.10_250714_S3000661518.zip) | 2025-07-14 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202507/Firmware__V5.8.10_250714_S3000661518.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202508/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-E10.pdf) |

</details>


<details>
<summary><h2>DS-2CD1B47G2H-LIUF - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.10 | Applied to: [DS-2CD1B47G2H-LIUF/SL(2.8mm)](https://assets.hikvision.com/prd/normal/all/files/202507/Firmware__V5.8.10_250714_S3000661518.zip) | 2025-07-14 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202507/Firmware__V5.8.10_250714_S3000661518.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202508/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-E10.pdf) |

</details>


<details>
<summary><h2>DS-2CD1B47G3-LIU - IPC_G0 (3 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.9.13 | Applied to: [DS-2CD1B47G3-LIUF/LSL(2.8mm)](https://assets.hikvision.com/prd/normal/all/files/202512/Firmware__V5.9.13_251124_S3000688200.zip) | 2025-11-24 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202512/Firmware__V5.9.13_251124_S3000688200.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.9.13_251124_Release_Note-IPCE_E_E15.pdf) |
| 5.9.12 | Applied to: [DS-2CD1B47G3-LIUF/SRB(2.8mm)](https://assets.hikvision.com/prd/normal/all/files/202509/Firmware__V5.9.12_250919_S3000675616.zip) | 2025-09-19 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202509/Firmware__V5.9.12_250919_S3000675616.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202511/releasenote%5CNetwork_Camera-V5.9.12_250919_Release_Note-IPCE_E_E15.pdf) |
| 5.9.11 | Applied to: [DS-2CD1B47G3-LIUF/SRB(2.8mm)](https://assets.hikvision.com/prd/normal/all/files/202508/Firmware__V5.9.11_250822_S3000669952.zip) | 2025-08-22 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202508/Firmware__V5.9.11_250822_S3000669952.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202511/releasenote%5CNetwork_Camera-V5.9.12_250919_Release_Note-IPCE_E_E15.pdf) |

</details>


<details>
<summary><h2>DS-2CD1B47G3H-LIU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.21 | Applied to: [DS-2CD1B47G3H-LIU(2.8mm)](https://assets.hikvision.com/prd/normal/all/files/202512/Firmware__V5.8.21_251117_S3000687895.zip) | 2025-11-17 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202512/Firmware__V5.8.21_251117_S3000687895.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.8.21_SP1_251117_Release_Note-H13U.pdf) |

</details>


<details>
<summary><h2>DS-2CD1B67G3-LIU - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.9.12 | Applied to: [DS-2CD1B67G3-LIUF/SRB(2.8mm)](https://assets.hikvision.com/prd/normal/all/files/202509/Firmware__V5.9.12_250919_S3000675616.zip) | 2025-09-19 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202509/Firmware__V5.9.12_250919_S3000675616.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202511/releasenote%5CNetwork_Camera-V5.9.12_250919_Release_Note-IPCE_E_E15.pdf) |
| 5.9.11 | Applied to: [DS-2CD1B67G3-LIUF/SRB(2.8mm)](https://assets.hikvision.com/prd/normal/all/files/202508/Firmware__V5.9.11_250822_S3000669952.zip) | 2025-08-22 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202508/Firmware__V5.9.11_250822_S3000669952.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202511/releasenote%5CNetwork_Camera-V5.9.12_250919_Release_Note-IPCE_E_E15.pdf) |

</details>


<details>
<summary><h2>DS-2CD1H23G2-IZ - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.10 | Applied to: [DS-2CD1H23G2-IZS(2.8-12mm)](https://assets.hikvision.com/prd/normal/all/files/202507/Firmware__V5.8.10_250714_S3000661509.zip) | 2025-07-14 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202507/Firmware__V5.8.10_250714_S3000661509.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202508/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-E10.pdf) |

</details>


<details>
<summary><h2>DS-2CD1H43G0-IZ - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD1H43G0-IZ(2.8-12mm)](https://assets.hikvision.com/prd/public/all/files/202505/Firmware__V5.7.23_241211_S3000620665.zip)(C) | 2024-12-11 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202505/Firmware__V5.7.23_241211_S3000620665.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202507/releasenote%5CNetwork_Camera-V5.7.23_SP2_Release_Note-E8.pdf) |

</details>


<details>
<summary><h2>DS-2CD1H43G2-IZ - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.10 | Applied to: [DS-2CD1H43G2-IZS(2.8-12mm)](https://assets.hikvision.com/prd/normal/all/files/202507/Firmware__V5.8.10_250714_S3000661509.zip) | 2025-07-14 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202507/Firmware__V5.8.10_250714_S3000661509.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202508/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-E10.pdf) |

</details>


<details>
<summary><h2>DS-2CD1H53G0-IZ - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD1H53G0-IZ(2.8-12mm)](https://assets.hikvision.com/prd/public/all/files/202410/Firmware__V5.7.23_241008_S3000605507.zip)(C) | 2024-10-08 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202410/Firmware__V5.7.23_241008_S3000605507.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202507/releasenote%5CNetwork_Camera-V5.7.23_SP_Release_Note-E8.pdf) |

</details>


<details>
<summary><h2>DS-2CD1P23G2-I - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.10 | Applied to: [DS-2CD1P23G2-IUF(2.8mm)](https://assets.hikvision.com/prd/normal/all/files/202507/Firmware__V5.8.10_250714_S3000661509.zip) | 2025-07-14 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202507/Firmware__V5.8.10_250714_S3000661509.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202508/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-E10.pdf) |

</details>


<details>
<summary><h2>DS-2CD1P27G2-L - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.10 | Applied to: [DS-2CD1P27G2-LUF(2.8mm)](https://assets.hikvision.com/prd/normal/all/files/202507/Firmware__V5.8.10_250714_S3000661509.zip) | 2025-07-14 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202507/Firmware__V5.8.10_250714_S3000661509.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202508/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-E10.pdf) |

</details>


<details>
<summary><h2>DS-2CD1P43G2-I - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.10 | Applied to: [DS-2CD1P43G2-I(2.8mm)](https://assets.hikvision.com/prd/normal/all/files/202507/Firmware__V5.8.10_250714_S3000661509.zip) | 2025-07-14 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202507/Firmware__V5.8.10_250714_S3000661509.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202508/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-E10.pdf) |

</details>


<details>
<summary><h2>DS-2CD1P47G2-L - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.10 | Applied to: [DS-2CD1P47G2-L(2.8mm)](https://assets.hikvision.com/prd/normal/all/files/202507/Firmware__V5.8.10_250714_S3000661509.zip) | 2025-07-14 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202507/Firmware__V5.8.10_250714_S3000661509.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202508/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-E10.pdf) |

</details>


<details>
<summary><h2>DS-2CD1T23G0-I - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD1T23G0-I(4mm)](https://assets.hikvision.com/prd/public/all/files/202410/Firmware__V5.7.23_241008_S3000605524.zip)(C) | 2024-10-08 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202410/Firmware__V5.7.23_241008_S3000605524.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202507/releasenote%5CNetwork_Camera-V5.7.23_SP_Release_Note-E8.pdf) |

</details>


<details>
<summary><h2>DS-2CD1T23G2-LIU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.10 | Applied to: [DS-2CD1T23G2-LIUF(4mm)](https://assets.hikvision.com/prd/public/all/files/202412/Firmware__V5.8.10_241205_S3000618834.zip) | 2024-12-05 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202412/Firmware__V5.8.10_241205_S3000618834.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202507/releasenote%5CNetwork_Camera-V5.8.10_SP2_Release_Note-E9.pdf) |

</details>


<details>
<summary><h2>DS-2CD1T23G2-LIUF - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.21 | Applied to: [DS-2CD1T23G2-LIUF/SL(4mm)](https://assets.hikvision.com/prd/normal/all/files/202507/Firmware__V5.8.21_250714_S3000661481.zip) | 2025-07-14 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202507/Firmware__V5.8.21_250714_S3000661481.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202508/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-E9.pdf) |

</details>


<details>
<summary><h2>DS-2CD1T27G2-L - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.10 | Applied to: [DS-2CD1T27G2-L(4mm)](https://assets.hikvision.com/prd/public/all/files/202412/Firmware__V5.8.10_241205_S3000618834.zip) | 2024-12-05 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202412/Firmware__V5.8.10_241205_S3000618834.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202507/releasenote%5CNetwork_Camera-V5.8.10_SP2_Release_Note-E9.pdf) |

</details>


<details>
<summary><h2>DS-2CD1T27G2H-LIU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.21 | Applied to: [DS-2CD1T27G2H-LIU(2.8mm)](https://assets.hikvision.com/prd/normal/all/files/202507/Firmware__V5.8.21_250714_S3000661481.zip) | 2025-07-14 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202507/Firmware__V5.8.21_250714_S3000661481.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202508/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-E9.pdf) |

</details>


<details>
<summary><h2>DS-2CD1T27G2H-LIUF - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.21 | Applied to: [DS-2CD1T27G2H-LIUF/SL(2.8mm)](https://assets.hikvision.com/prd/normal/all/files/202507/Firmware__V5.8.21_250714_S3000661481.zip) | 2025-07-14 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202507/Firmware__V5.8.21_250714_S3000661481.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202508/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-E9.pdf) |

</details>


<details>
<summary><h2>DS-2CD1T27G3-LIU - IPC_G0 (3 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.9.13 | Applied to: [DS-2CD1T27G3-LIU/LSRB(2.8mm)](https://assets.hikvision.com/prd/normal/all/files/202512/Firmware__V5.9.13_251124_S3000688200.zip) | 2025-11-24 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202512/Firmware__V5.9.13_251124_S3000688200.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.9.13_251124_Release_Note-IPCE_E_E15.pdf) |
| 5.9.12 | Applied to: [DS-2CD1T27G3-LIU/SRB(2.8mm)](https://assets.hikvision.com/prd/normal/all/files/202509/Firmware__V5.9.12_250919_S3000675616.zip) | 2025-09-19 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202509/Firmware__V5.9.12_250919_S3000675616.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202511/releasenote%5CNetwork_Camera-V5.9.12_250919_Release_Note-IPCE_E_E15.pdf) |
| 5.9.11 | Applied to: [DS-2CD1T27G3-LIU/SRB(2.8mm)](https://assets.hikvision.com/prd/normal/all/files/202508/Firmware__V5.9.11_250822_S3000669952.zip) | 2025-08-22 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202508/Firmware__V5.9.11_250822_S3000669952.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202511/releasenote%5CNetwork_Camera-V5.9.12_250919_Release_Note-IPCE_E_E15.pdf) |

</details>


<details>
<summary><h2>DS-2CD1T43G0-I - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD1T43G0-I(4mm)](https://assets.hikvision.com/prd/public/all/files/202410/Firmware__V5.7.23_241008_S3000605524.zip)(C) | 2024-10-08 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202410/Firmware__V5.7.23_241008_S3000605524.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202507/releasenote%5CNetwork_Camera-V5.7.23_SP_Release_Note-E8.pdf) |

</details>


<details>
<summary><h2>DS-2CD1T43G2-LIU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.10 | Applied to: [DS-2CD1T43G2-LIUF(4mm)](https://assets.hikvision.com/prd/normal/all/files/202507/Firmware__V5.8.10_250714_S3000661509.zip) | 2025-07-14 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202507/Firmware__V5.8.10_250714_S3000661509.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202508/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-E10.pdf) |

</details>


<details>
<summary><h2>DS-2CD1T43G2-LIUF - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.10 | Applied to: [DS-2CD1T43G2-LIUF/SL(4mm)](https://assets.hikvision.com/prd/normal/all/files/202507/Firmware__V5.8.10_250714_S3000661518.zip) | 2025-07-14 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202507/Firmware__V5.8.10_250714_S3000661518.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202508/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-E10.pdf) |

</details>


<details>
<summary><h2>DS-2CD1T47G2-L - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.10 | Applied to: [DS-2CD1T47G2-LUF(4mm)](https://assets.hikvision.com/prd/normal/all/files/202507/Firmware__V5.8.10_250714_S3000661509.zip) | 2025-07-14 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202507/Firmware__V5.8.10_250714_S3000661509.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202508/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-E10.pdf) |

</details>


<details>
<summary><h2>DS-2CD1T47G2H-LIU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.10 | Applied to: [DS-2CD1T47G2H-LIU(2.8mm)](https://assets.hikvision.com/prd/normal/all/files/202507/Firmware__V5.8.10_250714_S3000661518.zip) | 2025-07-14 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202507/Firmware__V5.8.10_250714_S3000661518.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202508/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-E10.pdf) |

</details>


<details>
<summary><h2>DS-2CD1T47G2H-LIUF - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.10 | Applied to: [DS-2CD1T47G2H-LIUF/SRB(2.8mm)](https://assets.hikvision.com/prd/normal/all/files/202507/Firmware__V5.8.10_250714_S3000661518.zip) | 2025-07-14 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202507/Firmware__V5.8.10_250714_S3000661518.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202508/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-E10.pdf) |

</details>


<details>
<summary><h2>DS-2CD1T47G3-LIU - IPC_G0 (3 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.9.13 | Applied to: [DS-2CD1T47G3-LIUF/LSL(2.8mm)](https://assets.hikvision.com/prd/normal/all/files/202512/Firmware__V5.9.13_251124_S3000688200.zip) | 2025-11-24 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202512/Firmware__V5.9.13_251124_S3000688200.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.9.13_251124_Release_Note-IPCE_E_E15.pdf) |
| 5.9.12 | Applied to: [DS-2CD1T47G3-LIU/SRB(2.8mm)](https://assets.hikvision.com/prd/normal/all/files/202509/Firmware__V5.9.12_250919_S3000675616.zip) | 2025-09-19 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202509/Firmware__V5.9.12_250919_S3000675616.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202511/releasenote%5CNetwork_Camera-V5.9.12_250919_Release_Note-IPCE_E_E15.pdf) |
| 5.9.11 | Applied to: [DS-2CD1T47G3-LIU/SRB(2.8mm)](https://assets.hikvision.com/prd/normal/all/files/202508/Firmware__V5.9.11_250822_S3000669952.zip) | 2025-08-22 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202508/Firmware__V5.9.11_250822_S3000669952.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202511/releasenote%5CNetwork_Camera-V5.9.12_250919_Release_Note-IPCE_E_E15.pdf) |

</details>


<details>
<summary><h2>DS-2CD1T47G3H-LIU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.21 | Applied to: [DS-2CD1T47G3H-LIU/SRB(2.8mm)](https://assets.hikvision.com/prd/normal/all/files/202512/Firmware__V5.8.21_251117_S3000687895.zip) | 2025-11-17 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202512/Firmware__V5.8.21_251117_S3000687895.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.8.21_SP1_251117_Release_Note-H13U.pdf) |

</details>


<details>
<summary><h2>DS-2CD1T63G2P-LIUF - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.11 | Applied to: [DS-2CD1T63G2P-LIUF/SL(2.8mm)](https://assets.hikvision.com/prd/normal/all/files/202511/Firmware__V5.8.11_251029_S3000683386.zip) | 2025-10-29 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202511/Firmware__V5.8.11_251029_S3000683386.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202511/releasenote%5CNetwork_Camera-V5.8.11_SP1_251029_Release_Note-IPCE_P_E11.pdf) |

</details>


<details>
<summary><h2>DS-2CD1T67G2H-LIUF - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.21 | Applied to: [DS-2CD1T67G2H-LIUF/SRB(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202505/Firmware__V5.8.21_250508_S3000647345.zip) | 2025-05-08 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202505/Firmware__V5.8.21_250508_S3000647345.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202507/releasenote%5CNetwork_Camera-V5.8.21_Release_Note-E12.pdf) |

</details>


<details>
<summary><h2>DS-2CD1T67G2HP-LIUF - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.11 | Applied to: [DS-2CD1T67G2HP-LIUF/SRB(2.8mm)](https://assets.hikvision.com/prd/normal/all/files/202511/Firmware__V5.8.11_251029_S3000683386.zip) | 2025-10-29 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202511/Firmware__V5.8.11_251029_S3000683386.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202511/releasenote%5CNetwork_Camera-V5.8.11_SP1_251029_Release_Note-IPCE_P_E11.pdf) |

</details>


<details>
<summary><h2>DS-2CD1T67G3-LIU - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.9.12 | Applied to: [DS-2CD1T67G3-LIU/SRB(2.8mm)](https://assets.hikvision.com/prd/normal/all/files/202509/Firmware__V5.9.12_250919_S3000675616.zip) | 2025-09-19 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202509/Firmware__V5.9.12_250919_S3000675616.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202511/releasenote%5CNetwork_Camera-V5.9.12_250919_Release_Note-IPCE_E_E15.pdf) |
| 5.9.11 | Applied to: [DS-2CD1T67G3-LIU/SRB(2.8mm)](https://assets.hikvision.com/prd/normal/all/files/202508/Firmware__V5.9.11_250822_S3000669952.zip) | 2025-08-22 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202508/Firmware__V5.9.11_250822_S3000669952.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202511/releasenote%5CNetwork_Camera-V5.9.12_250919_Release_Note-IPCE_E_E15.pdf) |

</details>


<details>
<summary><h2>DS-2CD1T83G0-I - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD1T83G0-I(4mm)](https://assets.hikvision.com/prd/public/all/files/202410/Firmware__V5.7.23_241008_S3000605524.zip)(C) | 2024-10-08 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202410/Firmware__V5.7.23_241008_S3000605524.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202507/releasenote%5CNetwork_Camera-V5.7.23_SP_Release_Note-E8.pdf) |

</details>


<details>
<summary><h2>DS-2CD1T83G2P-LIUF - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.11 | Applied to: [DS-2CD1T83G2P-LIUF/SL(2mm)](https://assets.hikvision.com/prd/normal/all/files/202511/Firmware__V5.8.11_251029_S3000683386.zip) | 2025-10-29 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202511/Firmware__V5.8.11_251029_S3000683386.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202511/releasenote%5CNetwork_Camera-V5.8.11_SP1_251029_Release_Note-IPCE_P_E11.pdf) |

</details>


<details>
<summary><h2>DS-2CD20123G2-LI - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.2 | Applied to: [DS-2CD20123G2-LIUY(2.8mm)](https://assets.hikvision.com/prd/normal/all/files/202511/Firmware__V5.8.2_251103_S3000682542.zip) | 2025-11-03 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202511/Firmware__V5.8.2_251103_S3000682542.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202511/releasenote%5CNetwork_Camera-V5.8.2_251103_Release_Note-IPCE_G9.pdf) |

</details>


<details>
<summary><h2>DS-2CD20123G2-LIUY - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.2 | Applied to: [DS-2CD20123G2-LIUY/SL(2.8mm)](https://assets.hikvision.com/prd/normal/all/files/202511/Firmware__V5.8.2_251103_S3000682542.zip) | 2025-11-03 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202511/Firmware__V5.8.2_251103_S3000682542.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202511/releasenote%5CNetwork_Camera-V5.8.2_251103_Release_Note-IPCE_G9.pdf) |

</details>


<details>
<summary><h2>DS-2CD20126G3-I - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.2 | Applied to: [DS-2CD20126G3-IY(2.8mm)](https://assets.hikvision.com/prd/normal/all/files/202511/Firmware__V5.8.2_251103_S3000682542.zip)(eF) | 2025-11-03 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202511/Firmware__V5.8.2_251103_S3000682542.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202511/releasenote%5CNetwork_Camera-V5.8.2_251103_Release_Note-IPCE_G9.pdf) |

</details>


<details>
<summary><h2>DS-2CD20126G3-IUY - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.2 | Applied to: [DS-2CD20126G3-IUY/SRB(2.8mm)](https://assets.hikvision.com/prd/normal/all/files/202511/Firmware__V5.8.2_251103_S3000682542.zip)eFO-STDBLACK | 2025-11-03 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202511/Firmware__V5.8.2_251103_S3000682542.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202511/releasenote%5CNetwork_Camera-V5.8.2_251103_Release_Note-IPCE_G9.pdf) |

</details>


<details>
<summary><h2>DS-2CD20166G3-I - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.2 | Applied to: [DS-2CD20166G3-IUY(2.8mm)](https://assets.hikvision.com/prd/normal/all/files/202511/Firmware__V5.8.2_251103_S3000682542.zip)(eF) | 2025-11-03 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202511/Firmware__V5.8.2_251103_S3000682542.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202511/releasenote%5CNetwork_Camera-V5.8.2_251103_Release_Note-IPCE_G9.pdf) |

</details>


<details>
<summary><h2>DS-2CD20166G3-IUY - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.2 | Applied to: [DS-2CD20166G3-IUY/SL(2.8mm)](https://assets.hikvision.com/prd/normal/all/files/202511/Firmware__V5.8.2_251103_S3000682542.zip)(eF) | 2025-11-03 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202511/Firmware__V5.8.2_251103_S3000682542.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202511/releasenote%5CNetwork_Camera-V5.8.2_251103_Release_Note-IPCE_G9.pdf) |

</details>


<details>
<summary><h2>DS-2CD2021G1-I - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2021G1-I(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202505/Firmware__V5.7.23_241211_S3000620665.zip)(B) | 2024-12-11 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202505/Firmware__V5.7.23_241211_S3000620665.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202507/releasenote%5CNetwork_Camera-V5.7.23_SP2_Release_Note-E8.pdf) |
| 5.5.800 | Applied to: [DS-2CD2021G1-I(2.8mm)](https://assets.hikvision.com/prd/public/all/files/2b726e56-901f-4e8d-9fd4-e9d67bc8e80a.zip)(B) | 2021-06-28 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/2b726e56-901f-4e8d-9fd4-e9d67bc8e80a.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202507/releasenote%5CNetwork_Camera-V5.7.23_SP2_Release_Note-E8.pdf) |

</details>


<details>
<summary><h2>DS-2TD5537T-7 - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.49 | Applied to: [DS-2TD5537T-7/W](https://assets.hikvision.com/prd/public/all/files/202211/Firmware__V5.5.49_220822_S3000450133.zip) | 2022-08-22 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202211/Firmware__V5.5.49_220822_S3000450133.zip) |  |

</details>


<details>
<summary><h2>DS-K3B411BX - UNKNOWN (3 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 2.0.5 | Applied to: [DS-K3B411BX-L/M](https://assets.hikvision.com/prd/normal/all/files/202510/Firmware__V2.0.5_250922_S3000677823.zip) | 2025-09-22 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202510/Firmware__V2.0.5_250922_S3000677823.zip) |  |
| 2.4.0 | Applied to: [DS-K3B411BX-L/M](https://assets.hikvision.com/prd/public/all/files/202502/Firmware__V2.4.0_250106_S3000625394.zip) | 2025-01-06 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202502/Firmware__V2.4.0_250106_S3000625394.zip) |  |
| 1.0.0 | Applied to: [DS-K3B411BX-L/M](https://assets.hikvision.com/prd/public/all/files/202406/1717709521275/Firmware__V1.0.0_240523_S3000577702.zip) | 2024-05-23 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202406/1717709521275/Firmware__V1.0.0_240523_S3000577702.zip) |  |

</details>


<details>
<summary><h2>IDS-E08HQHI-B - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 4.75.013 | Applied to: [iDS-E08HQHI-B](https://assets.hikvision.com/prd/public/all/files/202410/Firmware_Asia_V4.75.013_240919_S3000600889.zip) | 2024-09-19 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202410/Firmware_Asia_V4.75.013_240919_S3000600889.zip) |  |

</details>
