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
**Last Run:** 2026-03-08 21:47:04 UTC  
**Firmwares Found:** 951  
**New Firmwares:** 10  
**Test Mode:** Disabled



---

## Firmware List

Below is the complete list of archived firmwares, organized by device model and hardware version.

**Total: 951**



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
<summary><h2>DS-2CD1047G3H-LIU - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD1047G3H-LIUF(2.8mm)](https://assets.hikvision.com/prd/normal/all/files/202602/Firmware__V5.8.30_251210_S3000691347.zip) | 2025-12-10 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202602/Firmware__V5.8.30_251210_S3000691347.zip) |  |
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
<summary><h2>DS-2CD1147G3H-LIU - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD1147G3H-LIUF(2.8mm)](https://assets.hikvision.com/prd/normal/all/files/202602/Firmware__V5.8.30_251210_S3000691347.zip) | 2025-12-10 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202602/Firmware__V5.8.30_251210_S3000691347.zip) |  |
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
<summary><h2>DS-2CD1347G3H-LIU - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD1347G3H-LIU/SRB(2.8mm)](https://assets.hikvision.com/prd/normal/all/files/202602/Firmware__V5.8.30_251210_S3000691347.zip) | 2025-12-10 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202602/Firmware__V5.8.30_251210_S3000691347.zip) |  |
| 5.8.21 | Applied to: [DS-2CD1347G3H-LIU(2.8mm)](https://assets.hikvision.com/prd/normal/all/files/202512/Firmware__V5.8.21_251117_S3000687895.zip) | 2025-11-17 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202512/Firmware__V5.8.21_251117_S3000687895.zip) |  |

</details>


<details>
<summary><h2>DS-2CD1353G0-I - IPC_G0 (3 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD1353G0-I(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202410/Firmware__V5.7.23_241008_S3000605524.zip)(C) | 2024-10-08 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202410/Firmware__V5.7.23_241008_S3000605524.zip) |  |
| 5.5.800 | Applied to: [DS-2CD1353G0-I(2.8mm)](https://assets.hikvision.com/prd/public/all/files/af64952b-34be-46d9-94b8-3bf76fb5a5f4.zip) | 2021-08-16 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/af64952b-34be-46d9-94b8-3bf76fb5a5f4.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202312/releasenote%5CNetwork_Camera_V5.5.89_Release_Note_--G0.pdf) |
| 5.5.89 | Applied to: [DS-2CD1353G0-I(2.8mm)](https://assets.hikvision.com/prd/public/all/files/87acab3e-5d46-45cd-88c4-87b51139b600.zip) | 2021-04-29 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/87acab3e-5d46-45cd-88c4-87b51139b600.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202312/releasenote%5CNetwork_Camera_V5.5.89_Release_Note_--G0.pdf) |

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
<summary><h2>DS-2CD1B47G3H-LIU - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD1B47G3H-LIUF/SRB(2.8mm)](https://assets.hikvision.com/prd/normal/all/files/202602/Firmware__V5.8.30_251210_S3000691347.zip) | 2025-12-10 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202602/Firmware__V5.8.30_251210_S3000691347.zip) |  |
| 5.8.21 | Applied to: [DS-2CD1B47G3H-LIU(2.8mm)](https://assets.hikvision.com/prd/normal/all/files/202512/Firmware__V5.8.21_251117_S3000687895.zip) | 2025-11-17 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202512/Firmware__V5.8.21_251117_S3000687895.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.8.21_SP1_251117_Release_Note-H13U.pdf) |

</details>


<details>
<summary><h2>DS-2CD1B67G3-LIU - IPC_G0 (3 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.9.13 | Applied to: [DS-2CD1B67G3-LIU/LSL(2.8mm)](https://assets.hikvision.com/prd/normal/all/files/202512/Firmware__V5.9.13_251124_S3000688200.zip) | 2025-11-24 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202512/Firmware__V5.9.13_251124_S3000688200.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.9.13_251124_Release_Note-IPCE_E_E15.pdf) |
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
<summary><h2>DS-2CD1T47G3H-LIU - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD1T47G3H-LIU/SL(2.8mm)](https://assets.hikvision.com/prd/normal/all/files/202602/Firmware__V5.8.30_251210_S3000691347.zip) | 2025-12-10 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202602/Firmware__V5.8.30_251210_S3000691347.zip) |  |
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
<summary><h2>DS-2CD1T67G3-LIU - IPC_G0 (3 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.9.13 | Applied to: [DS-2CD1T67G3-LIU/LSL(2.8mm)](https://assets.hikvision.com/prd/normal/all/files/202512/Firmware__V5.9.13_251124_S3000688200.zip) | 2025-11-24 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202512/Firmware__V5.9.13_251124_S3000688200.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.9.13_251124_Release_Note-IPCE_E_E15.pdf) |
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
<summary><h2>DS-2CD2021G1-IDW - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.800 | Applied to: [DS-2CD2021G1-IDW1(2.8mm)](https://assets.hikvision.com/prd/public/all/files/2b726e56-901f-4e8d-9fd4-e9d67bc8e80a.zip) | 2021-06-28 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/2b726e56-901f-4e8d-9fd4-e9d67bc8e80a.zip) |  |

</details>


<details>
<summary><h2>DS-2CD2023G0-I - IPC_G1 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.6.821 | Applied to: [DS-2CD2023G0-I(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202309/Firmware__V5.6.821_230831_S3000525150.zip)(BLACK) | 2023-08-31 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202309/Firmware__V5.6.821_230831_S3000525150.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202401/releasenote%5CNetwork_Camera-V5.6.821_Release_Note-IPC_G1_230831.pdf) |

</details>


<details>
<summary><h2>DS-2CD2023G2-I - IPC_G0 (3 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.19 | Applied to: [DS-2CD2023G2-I(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202412/Firmware__V5.7.19_241207_S3000618481.zip)(D) | 2024-12-07 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202412/Firmware__V5.7.19_241207_S3000618481.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202507/releasenote%5CNetwork_Camera-V5.7.0_SP6_Release_Note-G6_I.pdf) |
| 5.7.0 | Applied to: [DS-2CD2023G2-I(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202411/Firmware__V5.7.0_241023_S3000609022.zip)(D) | 2024-10-23 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202411/Firmware__V5.7.0_241023_S3000609022.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202507/releasenote%5CNetwork_Camera-V5.7.0_SP6_Release_Note-G6_I.pdf) |
| 5.7.18 | Applied to: [DS-2CD2023G2-I(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202409/Firmware__V5.7.18_240826_S3000597013.zip)(D) | 2024-08-26 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202409/Firmware__V5.7.18_240826_S3000597013.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202507/releasenote%5CNetwork_Camera-V5.7.0_SP6_Release_Note-G6_I.pdf) |

</details>


<details>
<summary><h2>DS-2CD2023G2-LI - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.19 | Applied to: [DS-2CD2023G2-LI(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202412/Firmware__V5.7.19_241207_S3000618481.zip) | 2024-12-07 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202412/Firmware__V5.7.19_241207_S3000618481.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.19_241207_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2023G2-LI2U - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.19 | Applied to: [DS-2CD2023G2-LI2U/SL(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202412/Firmware__V5.7.19_241207_S3000618481.zip) | 2024-12-07 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202412/Firmware__V5.7.19_241207_S3000618481.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.19_241207_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2025FHWD-I - IPC_G1 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.6.821 | Applied to: [DS-2CD2025FHWD-I(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202309/Firmware__V5.6.821_230831_S3000525150.zip) | 2023-08-31 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202309/Firmware__V5.6.821_230831_S3000525150.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202401/releasenote%5CNetwork_Camera-V5.6.821_Release_Note-IPC_G1_230831.pdf) |

</details>


<details>
<summary><h2>DS-2CD2025FWD-I - IPC_G1 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.6.821 | Applied to: [DS-2CD2025FWD-I(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202309/Firmware__V5.6.821_230831_S3000525150.zip) | 2023-08-31 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202309/Firmware__V5.6.821_230831_S3000525150.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202401/releasenote%5CNetwork_Camera-V5.6.821_Release_Note-IPC_G1_230831.pdf) |

</details>


<details>
<summary><h2>DS-2CD2026G2-I - IPC_G0 (4 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.19 | Applied to: [DS-2CD2026G2-I(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202412/Firmware__V5.7.19_241207_S3000618481.zip) | 2024-12-07 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202412/Firmware__V5.7.19_241207_S3000618481.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202408/releasenote%5CNetwork_Camera-V5.5.820_Release_Note-G3.pdf) |
| 5.7.0 | Applied to: [DS-2CD2026G2-I(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202411/Firmware__V5.7.0_241023_S3000609022.zip) | 2024-10-23 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202411/Firmware__V5.7.0_241023_S3000609022.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202408/releasenote%5CNetwork_Camera-V5.5.820_Release_Note-G3.pdf) |
| 5.5.820 | Applied to: [DS-2CD2026G2-I(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202312/Firmware__V5.5.820_231108_S3000539625.zip) | 2023-11-08 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202312/Firmware__V5.5.820_231108_S3000539625.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202408/releasenote%5CNetwork_Camera-V5.5.820_Release_Note-G3.pdf) |
| 5.5.800 | Applied to: [DS-2CD2026G2-I(2.8mm)](https://assets.hikvision.com/prd/public/all/files/7ddcc773-b084-4adc-a9e1-08ed4b8252f4.zip) | 2021-10-09 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/7ddcc773-b084-4adc-a9e1-08ed4b8252f4.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202408/releasenote%5CNetwork_Camera-V5.5.820_Release_Note-G3.pdf) |

</details>


<details>
<summary><h2>DS-2CD2026G2-IU - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.19 | Applied to: [DS-2CD2026G2-IU/SL(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202412/Firmware__V5.7.19_241207_S3000618481.zip) | 2024-12-07 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202412/Firmware__V5.7.19_241207_S3000618481.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202408/releasenote%5CNetwork_Camera-V5.5.820_Release_Note-G3.pdf) |
| 5.5.820 | Applied to: [DS-2CD2026G2-IU/SL(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202312/Firmware__V5.5.820_231108_S3000539625.zip) | 2023-11-08 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202312/Firmware__V5.5.820_231108_S3000539625.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202408/releasenote%5CNetwork_Camera-V5.5.820_Release_Note-G3.pdf) |

</details>


<details>
<summary><h2>DS-2CD2027G2-L - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.19 | Applied to: [DS-2CD2027G2-LU(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202412/Firmware__V5.7.19_241207_S3000618481.zip) | 2024-12-07 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202412/Firmware__V5.7.19_241207_S3000618481.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202408/releasenote%5CNetwork_Camera-V5.5.820_Release_Note-G3.pdf) |
| 5.5.820 | Applied to: [DS-2CD2027G2-LU(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202312/Firmware__V5.5.820_231108_S3000539625.zip) | 2023-11-08 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202312/Firmware__V5.5.820_231108_S3000539625.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202408/releasenote%5CNetwork_Camera-V5.5.820_Release_Note-G3.pdf) |

</details>


<details>
<summary><h2>DS-2CD2041G1-IDW - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.89 | Applied to: [DS-2CD2041G1-IDW1(2.8mm)](https://assets.hikvision.com/prd/public/all/files/87acab3e-5d46-45cd-88c4-87b51139b600.zip) | 2021-04-29 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/87acab3e-5d46-45cd-88c4-87b51139b600.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202312/releasenote%5CNetwork_Camera_V5.5.89_Release_Note_--G0.pdf) |
| 5.5.82 | Applied to: [DS-2CD2041G1-IDW1(2.8mm)](https://assets.hikvision.com/prd/public/all/files/e8cbe4a1-a383-4ffa-a762-1891fa4b0901.zip) | 2019-01-30 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/e8cbe4a1-a383-4ffa-a762-1891fa4b0901.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202312/releasenote%5CNetwork_Camera_V5.5.89_Release_Note_--G0.pdf) |

</details>


<details>
<summary><h2>DS-2CD2043G0-I - IPC_G1 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.6.821 | Applied to: [DS-2CD2043G0-I(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202309/Firmware__V5.6.821_230831_S3000525150.zip) | 2023-08-31 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202309/Firmware__V5.6.821_230831_S3000525150.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202401/releasenote%5CNetwork_Camera-V5.6.821_Release_Note-IPC_G1_230831.pdf) |

</details>


<details>
<summary><h2>DS-2CD2043G2-I - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.19 | Applied to: [DS-2CD2043G2-I(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202412/Firmware__V5.7.19_241207_S3000618481.zip) | 2024-12-07 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202412/Firmware__V5.7.19_241207_S3000618481.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.19_241207_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2043G2-LI - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.19 | Applied to: [DS-2CD2043G2-LI(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202412/Firmware__V5.7.19_241207_S3000618481.zip) | 2024-12-07 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202412/Firmware__V5.7.19_241207_S3000618481.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.19_241207_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2043G2-LI2U - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.19 | Applied to: [DS-2CD2043G2-LI2U/SL(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202412/Firmware__V5.7.19_241207_S3000618481.zip) | 2024-12-07 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202412/Firmware__V5.7.19_241207_S3000618481.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.19_241207_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2043G2-LIZ - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.21 | Applied to: [DS-2CD2043G2-LIZY(2.8/4mm)](https://assets.hikvision.com/prd/normal/all/files/202512/Firmware__V5.8.21_251117_S3000687899.zip) | 2025-11-17 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202512/Firmware__V5.8.21_251117_S3000687899.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.8.21_SP1_251117_Release_Note-H13U.pdf) |

</details>


<details>
<summary><h2>DS-2CD2043G2-LIZ2UY - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.21 | Applied to: [DS-2CD2043G2-LIZ2UY/SL(2.8/4mm)](https://assets.hikvision.com/prd/normal/all/files/202512/Firmware__V5.8.21_251117_S3000687899.zip) | 2025-11-17 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202512/Firmware__V5.8.21_251117_S3000687899.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.8.21_SP1_251117_Release_Note-H13U.pdf) |

</details>


<details>
<summary><h2>DS-2CD2045FWD-I - IPC_G1 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.6.821 | Applied to: [DS-2CD2045FWD-I(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202309/Firmware__V5.6.821_230831_S3000525150.zip)(BLACK) | 2023-08-31 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202309/Firmware__V5.6.821_230831_S3000525150.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202401/releasenote%5CNetwork_Camera-V5.6.821_Release_Note-IPC_G1_230831.pdf) |
| 5.6.820 | Applied to: [DS-2CD2045FWD-I(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202301/Firmware__V5.6.820_220519_S3000430633.zip)(BLACK) | 2022-05-19 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202301/Firmware__V5.6.820_220519_S3000430633.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202401/releasenote%5CNetwork_Camera-V5.6.821_Release_Note-IPC_G1_230831.pdf) |

</details>


<details>
<summary><h2>DS-2CD2046G2-I - IPC_G0 (3 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.19 | Applied to: [DS-2CD2046G2-IU(6mm)](https://assets.hikvision.com/prd/public/all/files/202412/Firmware__V5.7.19_241207_S3000618481.zip)(C) | 2024-12-07 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202412/Firmware__V5.7.19_241207_S3000618481.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.19_241207_Release_Note.pdf) |
| 5.5.820 | Applied to: [DS-2CD2046G2-IU(6mm)](https://assets.hikvision.com/prd/public/all/files/202312/Firmware__V5.5.820_231108_S3000539625.zip)(C) | 2023-11-08 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202312/Firmware__V5.5.820_231108_S3000539625.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.19_241207_Release_Note.pdf) |
| 5.5.800 | Applied to: [DS-2CD2046G2-IU(6mm)](https://assets.hikvision.com/prd/public/all/files/7ddcc773-b084-4adc-a9e1-08ed4b8252f4.zip)(C) | 2021-10-09 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/7ddcc773-b084-4adc-a9e1-08ed4b8252f4.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.19_241207_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2046G2-IU - IPC_G0 (3 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.19 | Applied to: [DS-2CD2046G2-IU/SL(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202412/Firmware__V5.7.19_241207_S3000618481.zip) | 2024-12-07 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202412/Firmware__V5.7.19_241207_S3000618481.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/330c4c2c-5730-4877-a942-0be87cea67ca.pdf) |
| 5.5.820 | Applied to: [DS-2CD2046G2-IU/SL(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202312/Firmware__V5.5.820_231108_S3000539625.zip) | 2023-11-08 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202312/Firmware__V5.5.820_231108_S3000539625.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/330c4c2c-5730-4877-a942-0be87cea67ca.pdf) |
| 5.5.800 | Applied to: [DS-2CD2046G2-IU/SL(2.8mm)](https://assets.hikvision.com/prd/public/all/files/7ddcc773-b084-4adc-a9e1-08ed4b8252f4.zip) | 2021-10-09 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/7ddcc773-b084-4adc-a9e1-08ed4b8252f4.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/330c4c2c-5730-4877-a942-0be87cea67ca.pdf) |

</details>


<details>
<summary><h2>DS-2CD2046G2H-I - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.19 | Applied to: [DS-2CD2046G2H-IU(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202412/Firmware__V5.7.19_241207_S3000618481.zip)(eF) | 2024-12-07 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202412/Firmware__V5.7.19_241207_S3000618481.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.19_241207_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2046G2H-I2U - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.19 | Applied to: [DS-2CD2046G2H-I2U/SL(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202412/Firmware__V5.7.19_241207_S3000618481.zip)(eF) | 2024-12-07 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202412/Firmware__V5.7.19_241207_S3000618481.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.19_241207_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2046G3-IZ - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.21 | Applied to: [DS-2CD2046G3-IZ2UY(2.8/4mm)](https://assets.hikvision.com/prd/normal/all/files/202512/Firmware__V5.8.21_251117_S3000687899.zip) | 2025-11-17 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202512/Firmware__V5.8.21_251117_S3000687899.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.8.21_SP1_251117_Release_Note-H13U.pdf) |

</details>


<details>
<summary><h2>DS-2CD2046G3-IZ2UY - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.21 | Applied to: [DS-2CD2046G3-IZ2UY/SRB(2.8/4)](https://assets.hikvision.com/prd/normal/all/files/202512/Firmware__V5.8.21_251117_S3000687899.zip)O-STDBLACK | 2025-11-17 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202512/Firmware__V5.8.21_251117_S3000687899.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.8.21_SP1_251117_Release_Note-H13U.pdf) |

</details>


<details>
<summary><h2>DS-2CD2047G2-L - IPC_G0 (3 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.19 | Applied to: [DS-2CD2047G2-LU(6mm)](https://assets.hikvision.com/prd/public/all/files/202412/Firmware__V5.7.19_241207_S3000618481.zip)(C) | 2024-12-07 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202412/Firmware__V5.7.19_241207_S3000618481.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.19_241207_Release_Note.pdf) |
| 5.5.820 | Applied to: [DS-2CD2047G2-LU(6mm)](https://assets.hikvision.com/prd/public/all/files/202312/Firmware__V5.5.820_231108_S3000539625.zip)(C) | 2023-11-08 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202312/Firmware__V5.5.820_231108_S3000539625.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.19_241207_Release_Note.pdf) |
| 5.5.800 | Applied to: [DS-2CD2047G2-LU(6mm)](https://assets.hikvision.com/prd/public/all/files/7ddcc773-b084-4adc-a9e1-08ed4b8252f4.zip)(C) | 2021-10-09 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/7ddcc773-b084-4adc-a9e1-08ed4b8252f4.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.19_241207_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2047G2-LU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.19 | Applied to: [DS-2CD2047G2-LU/SL(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202412/Firmware__V5.7.19_241207_S3000618481.zip)(C) | 2024-12-07 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202412/Firmware__V5.7.19_241207_S3000618481.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.19_241207_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2047G2H-LIU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.19 | Applied to: [DS-2CD2047G2H-LI(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202412/Firmware__V5.7.19_241207_S3000618481.zip)(eF) | 2024-12-07 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202412/Firmware__V5.7.19_241207_S3000618481.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.19_241207_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2047G3-LI - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.21 | Applied to: [DS-2CD2047G3-LIY(2.8mm)](https://assets.hikvision.com/prd/normal/all/files/202512/Firmware__V5.8.21_251117_S3000687899.zip) | 2025-11-17 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202512/Firmware__V5.8.21_251117_S3000687899.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.8.21_SP1_251117_Release_Note-H13U.pdf) |

</details>


<details>
<summary><h2>DS-2CD2047G3-LI2UY - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.21 | Applied to: [DS-2CD2047G3-LI2UY/SL(2.8mm)](https://assets.hikvision.com/prd/normal/all/files/202512/Firmware__V5.8.21_251117_S3000687899.zip) | 2025-11-17 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202512/Firmware__V5.8.21_251117_S3000687899.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.8.21_SP1_251117_Release_Note-H13U.pdf) |

</details>


<details>
<summary><h2>DS-2CD2051G1-IDW - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.82 | Applied to: [DS-2CD2051G1-IDW1(2.8mm)](https://assets.hikvision.com/prd/public/all/files/e8cbe4a1-a383-4ffa-a762-1891fa4b0901.zip) | 2019-01-30 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/e8cbe4a1-a383-4ffa-a762-1891fa4b0901.zip) |  |

</details>


<details>
<summary><h2>DS-2CD2063G0-I - IPC_G1 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.6.821 | Applied to: [DS-2CD2063G0-I(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202309/Firmware__V5.6.821_230831_S3000525150.zip) | 2023-08-31 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202309/Firmware__V5.6.821_230831_S3000525150.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202401/releasenote%5CNetwork_Camera-V5.6.821_Release_Note-IPC_G1_230831.pdf) |

</details>


<details>
<summary><h2>DS-2CD2063G2-I - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.19 | Applied to: [DS-2CD2063G2-IU(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202412/Firmware__V5.7.19_241207_S3000618481.zip) | 2024-12-07 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202412/Firmware__V5.7.19_241207_S3000618481.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.19_241207_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2063G2-LI - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.19 | Applied to: [DS-2CD2063G2-LI(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202412/Firmware__V5.7.19_241207_S3000618481.zip) | 2024-12-07 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202412/Firmware__V5.7.19_241207_S3000618481.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.19_241207_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2063G2-LI2U - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.19 | Applied to: [DS-2CD2063G2-LI2U/SL(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202412/Firmware__V5.7.19_241207_S3000618481.zip) | 2024-12-07 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202412/Firmware__V5.7.19_241207_S3000618481.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.19_241207_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2065G1-I - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.6.820 | Applied to: [DS-2CD2065G1-I(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202301/Firmware__V5.6.820_220519_S3000430633.zip)(BLACK) | 2022-05-19 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202301/Firmware__V5.6.820_220519_S3000430633.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202301/Network%20Camera%20V5.6.820%20Release%20Note%20--G1.pdf) |

</details>


<details>
<summary><h2>DS-2CD2066G2-I - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.19 | Applied to: [DS-2CD2066G2-IU(6mm)](https://assets.hikvision.com/prd/public/all/files/202412/Firmware__V5.7.19_241207_S3000618481.zip)(C) | 2024-12-07 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202412/Firmware__V5.7.19_241207_S3000618481.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.19_241207_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2066G2-IU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.19 | Applied to: [DS-2CD2066G2-IU/SL(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202412/Firmware__V5.7.19_241207_S3000618481.zip)(C) | 2024-12-07 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202412/Firmware__V5.7.19_241207_S3000618481.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.19_241207_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2066G2H-I - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.19 | Applied to: [DS-2CD2066G2H-IU(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202412/Firmware__V5.7.19_241207_S3000618481.zip)(eF) | 2024-12-07 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202412/Firmware__V5.7.19_241207_S3000618481.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.19_241207_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2066G2H-I2U - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.19 | Applied to: [DS-2CD2066G2H-I2U/SL(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202412/Firmware__V5.7.19_241207_S3000618481.zip)/eFO-STDBLACK | 2024-12-07 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202412/Firmware__V5.7.19_241207_S3000618481.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.19_241207_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2067G2-L - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.19 | Applied to: [DS-2CD2067G2-LU(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202412/Firmware__V5.7.19_241207_S3000618481.zip)(C) | 2024-12-07 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202412/Firmware__V5.7.19_241207_S3000618481.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.19_241207_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2067G2H-LIU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.19 | Applied to: [DS-2CD2067G2H-LI(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202412/Firmware__V5.7.19_241207_S3000618481.zip)(eF) | 2024-12-07 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202412/Firmware__V5.7.19_241207_S3000618481.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.19_241207_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2067G3-LI - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD2067G3-LI2UY(2.8mm)](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691342.zip) | 2025-12-10 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691342.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD2067G3-LI2UY - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD2067G3-LI2UY/SL(2.8mm)](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691342.zip) | 2025-12-10 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691342.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD2083G0-I - IPC_G1 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.6.821 | Applied to: [DS-2CD2083G0-I(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202309/Firmware__V5.6.821_230831_S3000525150.zip) | 2023-08-31 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202309/Firmware__V5.6.821_230831_S3000525150.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202401/releasenote%5CNetwork_Camera-V5.6.821_Release_Note-IPC_G1_230831.pdf) |

</details>


<details>
<summary><h2>DS-2CD2083G2-I - IPC_G0 (3 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.6 | Applied to: [DS-2CD2083G2-I(6mm)](https://assets.hikvision.com/prd/normal/all/files/202602/Firmware__V5.7.6_260128_S3000701683.zip)(D) | 2026-01-28 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202602/Firmware__V5.7.6_260128_S3000701683.zip) |  |
| 5.7.5 | Applied to: [DS-2CD2083G2-I(2.8mm)](https://assets.hikvision.com/prd/normal/all/files/202508/Firmware__V5.7.5_250718_S3000663086.zip) | 2025-07-18 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202508/Firmware__V5.7.5_250718_S3000663086.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.19_241207_Release_Note.pdf) |
| 5.7.19 | Applied to: [DS-2CD2083G2-I(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202412/Firmware__V5.7.19_241207_S3000618481.zip) | 2024-12-07 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202412/Firmware__V5.7.19_241207_S3000618481.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.19_241207_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2083G2-LI - IPC_G0 (3 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.6 | Applied to: [DS-2CD2083G2-LI(2.8mm)](https://assets.hikvision.com/prd/normal/all/files/202602/Firmware__V5.7.6_260128_S3000701683.zip)(T) | 2026-01-28 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202602/Firmware__V5.7.6_260128_S3000701683.zip) |  |
| 5.7.19 | Applied to: [DS-2CD2083G2-LI(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202412/Firmware__V5.7.19_241207_S3000618481.zip) | 2024-12-07 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202412/Firmware__V5.7.19_241207_S3000618481.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.19_241207_Release_Note.pdf) |
| 5.7.5 | Applied to: [DS-2CD2083G2-LI(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202411/Firmware__V5.7.5_241103_S3000612864.zip) | 2024-11-03 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202411/Firmware__V5.7.5_241103_S3000612864.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.19_241207_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2083G2-LI2U - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.19 | Applied to: [DS-2CD2083G2-LI2U/SL(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202412/Firmware__V5.7.19_241207_S3000618481.zip) | 2024-12-07 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202412/Firmware__V5.7.19_241207_S3000618481.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.19_241207_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2085G1-I - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.6.820 | Applied to: [DS-2CD2085G1-I(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202301/Firmware__V5.6.820_220519_S3000430633.zip)(BLACK) | 2022-05-19 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202301/Firmware__V5.6.820_220519_S3000430633.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202301/Network%20Camera%20V5.6.820%20Release%20Note%20--G1.pdf) |
| 5.6.6 | Applied to: [DS-2CD2085G1-I(2.8mm)](https://assets.hikvision.com/prd/public/all/files/f18aceb7-b896-4c7d-ad2e-8f0d2a91bcc3.zip)(BLACK) | 2021-06-25 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/f18aceb7-b896-4c7d-ad2e-8f0d2a91bcc3.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202301/Network%20Camera%20V5.6.820%20Release%20Note%20--G1.pdf) |

</details>


<details>
<summary><h2>DS-2CD2086G2-I - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.19 | Applied to: [DS-2CD2086G2-I(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202412/Firmware__V5.7.19_241207_S3000618481.zip)(C) | 2024-12-07 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202412/Firmware__V5.7.19_241207_S3000618481.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.19_241207_Release_Note.pdf) |
| 5.5.820 | Applied to: [DS-2CD2086G2-I(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202312/Firmware__V5.5.820_231108_S3000539625.zip)(C) | 2023-11-08 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202312/Firmware__V5.5.820_231108_S3000539625.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.19_241207_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2086G2-IU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.19 | Applied to: [DS-2CD2086G2-IU/SL(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202412/Firmware__V5.7.19_241207_S3000618481.zip)(C) | 2024-12-07 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202412/Firmware__V5.7.19_241207_S3000618481.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.19_241207_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2086G2H-I - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.19 | Applied to: [DS-2CD2086G2H-I(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202412/Firmware__V5.7.19_241207_S3000618481.zip)(eF) | 2024-12-07 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202412/Firmware__V5.7.19_241207_S3000618481.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.19_241207_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2086G2H-I2U - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.19 | Applied to: [DS-2CD2086G2H-I2U/SL(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202412/Firmware__V5.7.19_241207_S3000618481.zip)(eF) | 2024-12-07 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202412/Firmware__V5.7.19_241207_S3000618481.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.19_241207_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2087G2-L - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.19 | Applied to: [DS-2CD2087G2-LU(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202412/Firmware__V5.7.19_241207_S3000618481.zip)(C) | 2024-12-07 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202412/Firmware__V5.7.19_241207_S3000618481.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.19_241207_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2087G2H-LI - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.19 | Applied to: [DS-2CD2087G2H-LI(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202412/Firmware__V5.7.19_241207_S3000618481.zip)(eF) | 2024-12-07 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202412/Firmware__V5.7.19_241207_S3000618481.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.19_241207_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2087G2H-LIU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.19 | Applied to: [DS-2CD2087G2H-LIU/SL(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202412/Firmware__V5.7.19_241207_S3000618481.zip)(eF) | 2024-12-07 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202412/Firmware__V5.7.19_241207_S3000618481.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.19_241207_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2087G3-LI - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD2087G3-LIY(2.8mm)](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691342.zip) | 2025-12-10 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691342.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD2087G3-LI2UY - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD2087G3-LI2UY/SL(2.8mm)](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691342.zip) | 2025-12-10 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691342.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD2121G0-I - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2121G0-IS(4mm)](https://assets.hikvision.com/prd/public/all/files/202505/Firmware__V5.7.23_241211_S3000620665.zip) | 2024-12-11 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202505/Firmware__V5.7.23_241211_S3000620665.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202507/releasenote%5CNetwork_Camera-V5.7.23_SP2_Release_Note-E8.pdf) |
| 5.5.800 | Applied to: [DS-2CD2121G0-IS(4mm)](https://assets.hikvision.com/prd/public/all/files/2b726e56-901f-4e8d-9fd4-e9d67bc8e80a.zip) | 2021-06-28 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/2b726e56-901f-4e8d-9fd4-e9d67bc8e80a.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202507/releasenote%5CNetwork_Camera-V5.7.23_SP2_Release_Note-E8.pdf) |

</details>


<details>
<summary><h2>DS-2CD2121G1-IDW - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.821 | Applied to: [DS-2CD2121G1-IDW1(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202312/Firmware__V5.5.821_231108_S3000539548.zip) | 2023-11-08 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202312/Firmware__V5.5.821_231108_S3000539548.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202404/1712790068455/releasenote%5CIPC_E6_5.5.821_Release_Note.pdf) |
| 5.5.800 | Applied to: [DS-2CD2121G1-IDW1(2.8mm)](https://assets.hikvision.com/prd/public/all/files/2b726e56-901f-4e8d-9fd4-e9d67bc8e80a.zip) | 2021-06-28 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/2b726e56-901f-4e8d-9fd4-e9d67bc8e80a.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202404/1712790068455/releasenote%5CIPC_E6_5.5.821_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2123G0-I - IPC_G1 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.6.821 | Applied to: [DS-2CD2123G0-IS(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202309/Firmware__V5.6.821_230831_S3000525150.zip)(BLACK) | 2023-08-31 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202309/Firmware__V5.6.821_230831_S3000525150.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202401/releasenote%5CNetwork_Camera-V5.6.821_Release_Note-IPC_G1_230831.pdf) |

</details>


<details>
<summary><h2>DS-2CD2123G0-IU - IPC_G1 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.6.821 | Applied to: [DS-2CD2123G0-IU(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202309/Firmware__V5.6.821_230831_S3000525150.zip) | 2023-08-31 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202309/Firmware__V5.6.821_230831_S3000525150.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202401/releasenote%5CNetwork_Camera-V5.6.821_Release_Note-IPC_G1_230831.pdf) |

</details>


<details>
<summary><h2>DS-2CD2123G2-I - IPC_G0 (3 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.19 | Applied to: [DS-2CD2123G2-I(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202412/Firmware__V5.7.19_241207_S3000618481.zip)(D)(BLACK) | 2024-12-07 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202412/Firmware__V5.7.19_241207_S3000618481.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202507/releasenote%5CNetwork_Camera-V5.7.0_SP6_Release_Note-G6_I.pdf) |
| 5.7.0 | Applied to: [DS-2CD2123G2-I(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202411/Firmware__V5.7.0_241023_S3000609022.zip)(D)(BLACK) | 2024-10-23 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202411/Firmware__V5.7.0_241023_S3000609022.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202507/releasenote%5CNetwork_Camera-V5.7.0_SP6_Release_Note-G6_I.pdf) |
| 5.7.18 | Applied to: [DS-2CD2123G2-I(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202409/Firmware__V5.7.18_240826_S3000597013.zip)(D)(BLACK) | 2024-08-26 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202409/Firmware__V5.7.18_240826_S3000597013.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202507/releasenote%5CNetwork_Camera-V5.7.0_SP6_Release_Note-G6_I.pdf) |

</details>


<details>
<summary><h2>DS-2CD2123G2-IU - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.19 | Applied to: [DS-2CD2123G2-IU(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202412/Firmware__V5.7.19_241207_S3000618481.zip)(D) | 2024-12-07 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202412/Firmware__V5.7.19_241207_S3000618481.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202507/releasenote%5CNetwork_Camera-V5.7.0_SP6_Release_Note-G6_I.pdf) |
| 5.7.0 | Applied to: [DS-2CD2123G2-IU(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202411/Firmware__V5.7.0_241023_S3000609022.zip)(D) | 2024-10-23 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202411/Firmware__V5.7.0_241023_S3000609022.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202507/releasenote%5CNetwork_Camera-V5.7.0_SP6_Release_Note-G6_I.pdf) |

</details>


<details>
<summary><h2>DS-2CD2123G2-LI - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.19 | Applied to: [DS-2CD2123G2-LI(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202412/Firmware__V5.7.19_241207_S3000618481.zip) | 2024-12-07 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202412/Firmware__V5.7.19_241207_S3000618481.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.19_241207_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2125FHWD-I - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.6.820 | Applied to: [DS-2CD2125FHWD-I(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202301/Firmware__V5.6.820_220519_S3000430633.zip) | 2022-05-19 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202301/Firmware__V5.6.820_220519_S3000430633.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202301/Network%20Camera%20V5.6.820%20Release%20Note%20--G1.pdf) |
| 5.6.6 | Applied to: [DS-2CD2125FHWD-I(2.8mm)](https://assets.hikvision.com/prd/public/all/files/f18aceb7-b896-4c7d-ad2e-8f0d2a91bcc3.zip) | 2021-06-25 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/f18aceb7-b896-4c7d-ad2e-8f0d2a91bcc3.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202301/Network%20Camera%20V5.6.820%20Release%20Note%20--G1.pdf) |

</details>


<details>
<summary><h2>DS-2CD2125FWD-I - IPC_G1 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.6.821 | Applied to: [DS-2CD2125FWD-IS(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202309/Firmware__V5.6.821_230831_S3000525150.zip) | 2023-08-31 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202309/Firmware__V5.6.821_230831_S3000525150.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202301/Network%20Camera%20V5.6.820%20Release%20Note%20--G1.pdf) |
| 5.6.820 | Applied to: [DS-2CD2125FWD-IS(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202301/Firmware__V5.6.820_220519_S3000430633.zip) | 2022-05-19 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202301/Firmware__V5.6.820_220519_S3000430633.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202301/Network%20Camera%20V5.6.820%20Release%20Note%20--G1.pdf) |

</details>


<details>
<summary><h2>DS-2CD2125G0-IMS - IPC_G1 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.6.821 | Applied to: [DS-2CD2125G0-IMS(4mm)](https://assets.hikvision.com/prd/public/all/files/202309/Firmware__V5.6.821_230831_S3000525150.zip) | 2023-08-31 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202309/Firmware__V5.6.821_230831_S3000525150.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202401/releasenote%5CNetwork_Camera-V5.6.821_Release_Note-IPC_G1_230831.pdf) |

</details>


<details>
<summary><h2>DS-2CD2126G2-I - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.19 | Applied to: [DS-2CD2126G2-ISU(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202412/Firmware__V5.7.19_241207_S3000618481.zip)(C) | 2024-12-07 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202412/Firmware__V5.7.19_241207_S3000618481.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.19_241207_Release_Note.pdf) |
| 5.7.0 | Applied to: [DS-2CD2126G2-ISU(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202411/Firmware__V5.7.0_241023_S3000609022.zip)(C) | 2024-10-23 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202411/Firmware__V5.7.0_241023_S3000609022.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.19_241207_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2126G2-IMS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.19 | Applied to: [DS-2CD2126G2-IMS(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202412/Firmware__V5.7.19_241207_S3000618481.zip) | 2024-12-07 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202412/Firmware__V5.7.19_241207_S3000618481.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.19_241207_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2141G1-IDW - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.89 | Applied to: [DS-2CD2141G1-IDW1(2.8mm)](https://assets.hikvision.com/prd/public/all/files/87acab3e-5d46-45cd-88c4-87b51139b600.zip)(T) | 2021-04-29 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/87acab3e-5d46-45cd-88c4-87b51139b600.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202312/releasenote%5CNetwork_Camera_V5.5.89_Release_Note_--G0.pdf) |
| 5.5.82 | Applied to: [DS-2CD2141G1-IDW1(2.8mm)](https://assets.hikvision.com/prd/public/all/files/e8cbe4a1-a383-4ffa-a762-1891fa4b0901.zip)(T) | 2019-01-30 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/e8cbe4a1-a383-4ffa-a762-1891fa4b0901.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202312/releasenote%5CNetwork_Camera_V5.5.89_Release_Note_--G0.pdf) |

</details>


<details>
<summary><h2>DS-2CD2143G0-I - IPC_G1 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.6.821 | Applied to: [DS-2CD2143G0-I(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202309/Firmware__V5.6.821_230831_S3000525150.zip)(BLACK) | 2023-08-31 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202309/Firmware__V5.6.821_230831_S3000525150.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202401/releasenote%5CNetwork_Camera-V5.6.821_Release_Note-IPC_G1_230831.pdf) |

</details>


<details>
<summary><h2>DS-2CD2143G0-IU - IPC_G1 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.6.821 | Applied to: [DS-2CD2143G0-IU(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202309/Firmware__V5.6.821_230831_S3000525150.zip) | 2023-08-31 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202309/Firmware__V5.6.821_230831_S3000525150.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202401/releasenote%5CNetwork_Camera-V5.6.821_Release_Note-IPC_G1_230831.pdf) |

</details>


<details>
<summary><h2>DS-2CD2143G2-I - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.19 | Applied to: [DS-2CD2143G2-I(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202412/Firmware__V5.7.19_241207_S3000618481.zip)(BLACK) | 2024-12-07 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202412/Firmware__V5.7.19_241207_S3000618481.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.19_241207_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2143G2-IU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.19 | Applied to: [DS-2CD2143G2-IU(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202412/Firmware__V5.7.19_241207_S3000618481.zip)(BLACK) | 2024-12-07 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202412/Firmware__V5.7.19_241207_S3000618481.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.19_241207_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2143G2-LI - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.19 | Applied to: [DS-2CD2143G2-LI(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202412/Firmware__V5.7.19_241207_S3000618481.zip) | 2024-12-07 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202412/Firmware__V5.7.19_241207_S3000618481.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.19_241207_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2145FWD-I - IPC_G1 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.6.821 | Applied to: [DS-2CD2145FWD-IS(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202309/Firmware__V5.6.821_230831_S3000525150.zip)(BLACK) | 2023-08-31 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202309/Firmware__V5.6.821_230831_S3000525150.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202401/releasenote%5CNetwork_Camera-V5.6.821_Release_Note-IPC_G1_230831.pdf) |

</details>


<details>
<summary><h2>DS-2CD2146G2-I - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.19 | Applied to: [DS-2CD2146G2-ISU(6mm)](https://assets.hikvision.com/prd/public/all/files/202412/Firmware__V5.7.19_241207_S3000618481.zip)(C) | 2024-12-07 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202412/Firmware__V5.7.19_241207_S3000618481.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.19_241207_Release_Note.pdf) |
| 5.5.800 | Applied to: [DS-2CD2146G2-ISU(6mm)](https://assets.hikvision.com/prd/public/all/files/7ddcc773-b084-4adc-a9e1-08ed4b8252f4.zip)(C) | 2021-10-09 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/7ddcc773-b084-4adc-a9e1-08ed4b8252f4.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.19_241207_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2146G2H-I - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.19 | Applied to: [DS-2CD2146G2H-I(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202412/Firmware__V5.7.19_241207_S3000618481.zip)(eF) | 2024-12-07 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202412/Firmware__V5.7.19_241207_S3000618481.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.19_241207_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2147G2 - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.19 | Applied to: [DS-2CD2147G2-SU(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202412/Firmware__V5.7.19_241207_S3000618481.zip) | 2024-12-07 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202412/Firmware__V5.7.19_241207_S3000618481.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202408/releasenote%5CNetwork_Camera-V5.5.820_Release_Note-G3.pdf) |
| 5.5.820 | Applied to: [DS-2CD2147G2-SU(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202312/Firmware__V5.5.820_231108_S3000539625.zip) | 2023-11-08 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202312/Firmware__V5.5.820_231108_S3000539625.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202408/releasenote%5CNetwork_Camera-V5.5.820_Release_Note-G3.pdf) |

</details>


<details>
<summary><h2>DS-2CD2147G2-L - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.19 | Applied to: [DS-2CD2147G2-LSU(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202412/Firmware__V5.7.19_241207_S3000618481.zip)(C) | 2024-12-07 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202412/Firmware__V5.7.19_241207_S3000618481.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.19_241207_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2147G2H-LI - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.19 | Applied to: [DS-2CD2147G2H-LI(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202412/Firmware__V5.7.19_241207_S3000618481.zip)(eF) | 2024-12-07 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202412/Firmware__V5.7.19_241207_S3000618481.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.19_241207_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2147G3-LI - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.21 | Applied to: [DS-2CD2147G3-LIY(2.8mm)](https://assets.hikvision.com/prd/normal/all/files/202512/Firmware__V5.8.21_251117_S3000687899.zip) | 2025-11-17 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202512/Firmware__V5.8.21_251117_S3000687899.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.8.21_SP1_251117_Release_Note-H13U.pdf) |

</details>


<details>
<summary><h2>DS-2CD2163G0-I - IPC_G1 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.6.821 | Applied to: [DS-2CD2163G0-I(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202309/Firmware__V5.6.821_230831_S3000525150.zip)(BLACK) | 2023-08-31 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202309/Firmware__V5.6.821_230831_S3000525150.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202401/releasenote%5CNetwork_Camera-V5.6.821_Release_Note-IPC_G1_230831.pdf) |

</details>


<details>
<summary><h2>DS-2CD2163G0-IU - IPC_G1 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.6.821 | Applied to: [DS-2CD2163G0-IU(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202309/Firmware__V5.6.821_230831_S3000525150.zip) | 2023-08-31 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202309/Firmware__V5.6.821_230831_S3000525150.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202401/releasenote%5CNetwork_Camera-V5.6.821_Release_Note-IPC_G1_230831.pdf) |

</details>


<details>
<summary><h2>DS-2CD2163G2-I - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.19 | Applied to: [DS-2CD2163G2-I(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202412/Firmware__V5.7.19_241207_S3000618481.zip) | 2024-12-07 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202412/Firmware__V5.7.19_241207_S3000618481.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.19_241207_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2163G2-IU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.19 | Applied to: [DS-2CD2163G2-IU(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202412/Firmware__V5.7.19_241207_S3000618481.zip) | 2024-12-07 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202412/Firmware__V5.7.19_241207_S3000618481.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.19_241207_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2163G2-LI - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.19 | Applied to: [DS-2CD2163G2-LI(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202412/Firmware__V5.7.19_241207_S3000618481.zip) | 2024-12-07 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202412/Firmware__V5.7.19_241207_S3000618481.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.19_241207_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2165G0-I - IPC_G1 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.6.821 | Applied to: [DS-2CD2165G0-I(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202309/Firmware__V5.6.821_230831_S3000525150.zip)(BLACK) | 2023-08-31 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202309/Firmware__V5.6.821_230831_S3000525150.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202401/releasenote%5CNetwork_Camera-V5.6.821_Release_Note-IPC_G1_230831.pdf) |

</details>


<details>
<summary><h2>DS-2CD2166G2-I - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.19 | Applied to: [DS-2CD2166G2-ISU(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202412/Firmware__V5.7.19_241207_S3000618481.zip)(C)(BLACK) | 2024-12-07 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202412/Firmware__V5.7.19_241207_S3000618481.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.19_241207_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2166G2H-I - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.19 | Applied to: [DS-2CD2166G2H-I(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202412/Firmware__V5.7.19_241207_S3000618481.zip)(eF) | 2024-12-07 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202412/Firmware__V5.7.19_241207_S3000618481.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.19_241207_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2167G2H-LI - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.19 | Applied to: [DS-2CD2167G2H-LI(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202412/Firmware__V5.7.19_241207_S3000618481.zip)(eF) | 2024-12-07 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202412/Firmware__V5.7.19_241207_S3000618481.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.19_241207_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2167G3-LI - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD2167G3-LIS2UY(2.8mm)](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691342.zip) | 2025-12-10 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691342.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD2183G0-I - IPC_G1 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.6.821 | Applied to: [DS-2CD2183G0-I(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202309/Firmware__V5.6.821_230831_S3000525150.zip)(BLACK) | 2023-08-31 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202309/Firmware__V5.6.821_230831_S3000525150.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202401/releasenote%5CNetwork_Camera-V5.6.821_Release_Note-IPC_G1_230831.pdf) |
| 5.6.820 | Applied to: [DS-2CD2183G0-I(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202301/Firmware__V5.6.820_220519_S3000430633.zip)(BLACK) | 2022-05-19 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202301/Firmware__V5.6.820_220519_S3000430633.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202401/releasenote%5CNetwork_Camera-V5.6.821_Release_Note-IPC_G1_230831.pdf) |

</details>


<details>
<summary><h2>DS-2CD2183G0-IU - IPC_G1 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.6.821 | Applied to: [DS-2CD2183G0-IU(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202309/Firmware__V5.6.821_230831_S3000525150.zip) | 2023-08-31 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202309/Firmware__V5.6.821_230831_S3000525150.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202401/releasenote%5CNetwork_Camera-V5.6.821_Release_Note-IPC_G1_230831.pdf) |

</details>


<details>
<summary><h2>DS-2CD2183G2-I - IPC_G0 (3 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.6 | Applied to: [DS-2CD2183G2-I(2.8mm)](https://assets.hikvision.com/prd/normal/all/files/202602/Firmware__V5.7.6_260128_S3000701683.zip)(D) | 2026-01-28 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202602/Firmware__V5.7.6_260128_S3000701683.zip) |  |
| 5.7.5 | Applied to: [DS-2CD2183G2-IS(2.8mm)](https://assets.hikvision.com/prd/normal/all/files/202508/Firmware__V5.7.5_250718_S3000663086.zip)(BLACK) | 2025-07-18 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202508/Firmware__V5.7.5_250718_S3000663086.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.19_241207_Release_Note.pdf) |
| 5.7.19 | Applied to: [DS-2CD2183G2-IS(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202412/Firmware__V5.7.19_241207_S3000618481.zip)(BLACK) | 2024-12-07 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202412/Firmware__V5.7.19_241207_S3000618481.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.19_241207_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2183G2-IU - IPC_G0 (3 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.6 | Applied to: [DS-2CD2183G2-IU(2.8mm)](https://assets.hikvision.com/prd/normal/all/files/202602/Firmware__V5.7.6_260128_S3000701683.zip)(D) | 2026-01-28 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202602/Firmware__V5.7.6_260128_S3000701683.zip) |  |
| 5.7.5 | Applied to: [DS-2CD2183G2-IU(2.8mm)](https://assets.hikvision.com/prd/normal/all/files/202508/Firmware__V5.7.5_250718_S3000663086.zip)(D) | 2025-07-18 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202508/Firmware__V5.7.5_250718_S3000663086.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202508/releasenote%5CNetwork_Camera-V5.7.5_250718_Release_Note-H8.pdf) |
| 5.7.19 | Applied to: [DS-2CD2183G2-IU(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202412/Firmware__V5.7.19_241207_S3000618481.zip)(D) | 2024-12-07 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202412/Firmware__V5.7.19_241207_S3000618481.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202508/releasenote%5CNetwork_Camera-V5.7.5_250718_Release_Note-H8.pdf) |

</details>


<details>
<summary><h2>DS-2CD2183G2-LI - IPC_G0 (3 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.6 | Applied to: [DS-2CD2183G2-LI(4mm)](https://assets.hikvision.com/prd/normal/all/files/202602/Firmware__V5.7.6_260128_S3000701683.zip)(T) | 2026-01-28 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202602/Firmware__V5.7.6_260128_S3000701683.zip) |  |
| 5.7.19 | Applied to: [DS-2CD2183G2-LI(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202412/Firmware__V5.7.19_241207_S3000618481.zip) | 2024-12-07 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202412/Firmware__V5.7.19_241207_S3000618481.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.19_241207_Release_Note.pdf) |
| 5.7.5 | Applied to: [DS-2CD2183G2-LI(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202411/Firmware__V5.7.5_241103_S3000612864.zip) | 2024-11-03 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202411/Firmware__V5.7.5_241103_S3000612864.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.19_241207_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2185FWD-I - IPC_G1 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.6.821 | Applied to: [DS-2CD2185FWD-I(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202309/Firmware__V5.6.821_230831_S3000525150.zip)(BLACK) | 2023-08-31 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202309/Firmware__V5.6.821_230831_S3000525150.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202401/releasenote%5CNetwork_Camera-V5.6.821_Release_Note-IPC_G1_230831.pdf) |

</details>


<details>
<summary><h2>DS-2CD2185G0-IMS - IPC_G1 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.6.821 | Applied to: [DS-2CD2185G0-IMS(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202309/Firmware__V5.6.821_230831_S3000525150.zip) | 2023-08-31 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202309/Firmware__V5.6.821_230831_S3000525150.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202401/releasenote%5CNetwork_Camera-V5.6.821_Release_Note-IPC_G1_230831.pdf) |

</details>


<details>
<summary><h2>DS-2CD2186G2-I - IPC_G0 (3 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.19 | Applied to: [DS-2CD2186G2-I(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202412/Firmware__V5.7.19_241207_S3000618481.zip) | 2024-12-07 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202412/Firmware__V5.7.19_241207_S3000618481.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202408/releasenote%5CNetwork_Camera-V5.5.820_Release_Note-G3.pdf) |
| 5.5.820 | Applied to: [DS-2CD2186G2-I(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202312/Firmware__V5.5.820_231108_S3000539625.zip) | 2023-11-08 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202312/Firmware__V5.5.820_231108_S3000539625.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202408/releasenote%5CNetwork_Camera-V5.5.820_Release_Note-G3.pdf) |
| 5.5.800 | Applied to: [DS-2CD2186G2-I(2.8mm)](https://assets.hikvision.com/prd/public/all/files/7ddcc773-b084-4adc-a9e1-08ed4b8252f4.zip) | 2021-10-09 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/7ddcc773-b084-4adc-a9e1-08ed4b8252f4.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202408/releasenote%5CNetwork_Camera-V5.5.820_Release_Note-G3.pdf) |

</details>


<details>
<summary><h2>DS-2CD2186G2H-I - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.19 | Applied to: [DS-2CD2186G2H-I(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202412/Firmware__V5.7.19_241207_S3000618481.zip)(eF) | 2024-12-07 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202412/Firmware__V5.7.19_241207_S3000618481.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.19_241207_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2187G2-L - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.19 | Applied to: [DS-2CD2187G2-L(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202412/Firmware__V5.7.19_241207_S3000618481.zip)(C) | 2024-12-07 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202412/Firmware__V5.7.19_241207_S3000618481.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.19_241207_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2187G2H-LI - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.19 | Applied to: [DS-2CD2187G2H-LI(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202412/Firmware__V5.7.19_241207_S3000618481.zip)(eF) | 2024-12-07 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202412/Firmware__V5.7.19_241207_S3000618481.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.19_241207_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2187G3-LI - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD2187G3-LIY(2.8mm)](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691342.zip) | 2025-12-10 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691342.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD23123G2-LI - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.2 | Applied to: [DS-2CD23123G2-LI2UY(2.8mm)](https://assets.hikvision.com/prd/normal/all/files/202511/Firmware__V5.8.2_251103_S3000682542.zip) | 2025-11-03 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202511/Firmware__V5.8.2_251103_S3000682542.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202511/releasenote%5CNetwork_Camera-V5.8.2_251103_Release_Note-IPCE_G9.pdf) |

</details>


<details>
<summary><h2>DS-2CD23123G2-LI2UY - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.2 | Applied to: [DS-2CD23123G2-LIS2UY/SL(2.8mm)](https://assets.hikvision.com/prd/normal/all/files/202511/Firmware__V5.8.2_251103_S3000682542.zip) | 2025-11-03 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202511/Firmware__V5.8.2_251103_S3000682542.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202511/releasenote%5CNetwork_Camera-V5.8.2_251103_Release_Note-IPCE_G9.pdf) |

</details>


<details>
<summary><h2>DS-2CD23126G3-I - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.2 | Applied to: [DS-2CD23126G3-I2UY(2.8mm)](https://assets.hikvision.com/prd/normal/all/files/202511/Firmware__V5.8.2_251103_S3000682542.zip)(eF) | 2025-11-03 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202511/Firmware__V5.8.2_251103_S3000682542.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202511/releasenote%5CNetwork_Camera-V5.8.2_251103_Release_Note-IPCE_G9.pdf) |

</details>


<details>
<summary><h2>DS-2CD23126G3-IS2UY - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.2 | Applied to: [DS-2CD23126G3-IS2UY/SRB(2.8mm)](https://assets.hikvision.com/prd/normal/all/files/202511/Firmware__V5.8.2_251103_S3000682542.zip)(eF)/O-STD | 2025-11-03 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202511/Firmware__V5.8.2_251103_S3000682542.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202511/releasenote%5CNetwork_Camera-V5.8.2_251103_Release_Note-IPCE_G9.pdf) |

</details>


<details>
<summary><h2>DS-2CD23166G3-I - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.2 | Applied to: [DS-2CD23166G3-IY(2.8mm)](https://assets.hikvision.com/prd/normal/all/files/202511/Firmware__V5.8.2_251103_S3000682542.zip)(eF) | 2025-11-03 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202511/Firmware__V5.8.2_251103_S3000682542.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202511/releasenote%5CNetwork_Camera-V5.8.2_251103_Release_Note-IPCE_G9.pdf) |

</details>


<details>
<summary><h2>DS-2CD23166G3-IS2UY - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.2 | Applied to: [DS-2CD23166G3-IS2UY/SRB(2.8mm)](https://assets.hikvision.com/prd/normal/all/files/202511/Firmware__V5.8.2_251103_S3000682542.zip)(eF)/O-STD | 2025-11-03 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202511/Firmware__V5.8.2_251103_S3000682542.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202511/releasenote%5CNetwork_Camera-V5.8.2_251103_Release_Note-IPCE_G9.pdf) |

</details>


<details>
<summary><h2>DS-2CD2323G0-I - IPC_G1 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.6.821 | Applied to: [DS-2CD2323G0-I(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202309/Firmware__V5.6.821_230831_S3000525150.zip)(BLACK) | 2023-08-31 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202309/Firmware__V5.6.821_230831_S3000525150.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202401/releasenote%5CNetwork_Camera-V5.6.821_Release_Note-IPC_G1_230831.pdf) |

</details>


<details>
<summary><h2>DS-2CD2323G2-I - IPC_G0 (3 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.19 | Applied to: [DS-2CD2323G2-I(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202412/Firmware__V5.7.19_241207_S3000618481.zip)(D) | 2024-12-07 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202412/Firmware__V5.7.19_241207_S3000618481.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202507/releasenote%5CNetwork_Camera-V5.7.0_SP6_Release_Note-G6_I.pdf) |
| 5.7.0 | Applied to: [DS-2CD2323G2-I(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202411/Firmware__V5.7.0_241023_S3000609022.zip)(D) | 2024-10-23 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202411/Firmware__V5.7.0_241023_S3000609022.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202507/releasenote%5CNetwork_Camera-V5.7.0_SP6_Release_Note-G6_I.pdf) |
| 5.7.18 | Applied to: [DS-2CD2323G2-I(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202409/Firmware__V5.7.18_240826_S3000597013.zip)(D) | 2024-08-26 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202409/Firmware__V5.7.18_240826_S3000597013.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202507/releasenote%5CNetwork_Camera-V5.7.0_SP6_Release_Note-G6_I.pdf) |

</details>


<details>
<summary><h2>DS-2CD2323G2-LI - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.19 | Applied to: [DS-2CD2323G2-LI(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202412/Firmware__V5.7.19_241207_S3000618481.zip) | 2024-12-07 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202412/Firmware__V5.7.19_241207_S3000618481.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.19_241207_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2323G2-LI2U - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.19 | Applied to: [DS-2CD2323G2-LI2U/SRB(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202412/Firmware__V5.7.19_241207_S3000618481.zip) | 2024-12-07 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202412/Firmware__V5.7.19_241207_S3000618481.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.19_241207_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2325FHWD-I - IPC_G1 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.6.821 | Applied to: [DS-2CD2325FHWD-I(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202309/Firmware__V5.6.821_230831_S3000525150.zip) | 2023-08-31 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202309/Firmware__V5.6.821_230831_S3000525150.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202401/releasenote%5CNetwork_Camera-V5.6.821_Release_Note-IPC_G1_230831.pdf) |

</details>


<details>
<summary><h2>DS-2CD2325FWD-I - IPC_G1 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.6.821 | Applied to: [DS-2CD2325FWD-I(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202309/Firmware__V5.6.821_230831_S3000525150.zip)(BLACK) | 2023-08-31 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202309/Firmware__V5.6.821_230831_S3000525150.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202401/releasenote%5CNetwork_Camera-V5.6.821_Release_Note-IPC_G1_230831.pdf) |

</details>


<details>
<summary><h2>DS-2CD2326G1-I - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.6.0 | Applied to: [DS-2CD2326G1-I/SL(2.8mm)](https://assets.hikvision.com/prd/public/all/files/18db80e0-2712-4496-8bd3-646f5014a59b.zip) | 2019-05-07 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/18db80e0-2712-4496-8bd3-646f5014a59b.zip) |  |

</details>


<details>
<summary><h2>DS-2CD2326G2-I - IPC_G0 (4 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.19 | Applied to: [DS-2CD2326G2-IU(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202412/Firmware__V5.7.19_241207_S3000618481.zip) | 2024-12-07 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202412/Firmware__V5.7.19_241207_S3000618481.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/330c4c2c-5730-4877-a942-0be87cea67ca.pdf) |
| 5.7.0 | Applied to: [DS-2CD2326G2-IU(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202411/Firmware__V5.7.0_241023_S3000609022.zip) | 2024-10-23 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202411/Firmware__V5.7.0_241023_S3000609022.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/330c4c2c-5730-4877-a942-0be87cea67ca.pdf) |
| 5.5.820 | Applied to: [DS-2CD2326G2-IU(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202205/IPC_G3_EN_STD_5.5.820_220520.zip) | 2022-05-20 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202205/IPC_G3_EN_STD_5.5.820_220520.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/330c4c2c-5730-4877-a942-0be87cea67ca.pdf) |
| 5.5.800 | Applied to: [DS-2CD2326G2-IU(2.8mm)](https://assets.hikvision.com/prd/public/all/files/7ddcc773-b084-4adc-a9e1-08ed4b8252f4.zip) | 2021-10-09 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/7ddcc773-b084-4adc-a9e1-08ed4b8252f4.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/330c4c2c-5730-4877-a942-0be87cea67ca.pdf) |

</details>


<details>
<summary><h2>DS-2CD2326G2-ISU - IPC_G0 (3 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.19 | Applied to: [DS-2CD2326G2-ISU/SL(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202412/Firmware__V5.7.19_241207_S3000618481.zip)(D) | 2024-12-07 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202412/Firmware__V5.7.19_241207_S3000618481.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202507/releasenote%5CNetwork_Camera-V5.7.0_SP6_Release_Note-G6_I.pdf) |
| 5.7.0 | Applied to: [DS-2CD2326G2-ISU/SL(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202411/Firmware__V5.7.0_241023_S3000609022.zip)(D) | 2024-10-23 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202411/Firmware__V5.7.0_241023_S3000609022.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202507/releasenote%5CNetwork_Camera-V5.7.0_SP6_Release_Note-G6_I.pdf) |
| 5.5.820 | Applied to: [DS-2CD2326G2-ISU/SL(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202312/Firmware__V5.5.820_231108_S3000539625.zip)(D) | 2023-11-08 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202312/Firmware__V5.5.820_231108_S3000539625.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202507/releasenote%5CNetwork_Camera-V5.7.0_SP6_Release_Note-G6_I.pdf) |

</details>


<details>
<summary><h2>DS-2CD2327G2-L - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.19 | Applied to: [DS-2CD2327G2-LU(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202412/Firmware__V5.7.19_241207_S3000618481.zip) | 2024-12-07 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202412/Firmware__V5.7.19_241207_S3000618481.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/330c4c2c-5730-4877-a942-0be87cea67ca.pdf) |
| 5.5.800 | Applied to: [DS-2CD2327G2-LU(2.8mm)](https://assets.hikvision.com/prd/public/all/files/7ddcc773-b084-4adc-a9e1-08ed4b8252f4.zip) | 2021-10-09 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/7ddcc773-b084-4adc-a9e1-08ed4b8252f4.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/330c4c2c-5730-4877-a942-0be87cea67ca.pdf) |

</details>


<details>
<summary><h2>DS-2CD2343G0-I - IPC_G1 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.6.821 | Applied to: [DS-2CD2343G0-I(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202309/Firmware__V5.6.821_230831_S3000525150.zip)(BLACK) | 2023-08-31 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202309/Firmware__V5.6.821_230831_S3000525150.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202401/releasenote%5CNetwork_Camera-V5.6.821_Release_Note-IPC_G1_230831.pdf) |

</details>


<details>
<summary><h2>DS-2CD2343G2-LI - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.19 | Applied to: [DS-2CD2343G2-LI(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202412/Firmware__V5.7.19_241207_S3000618481.zip) | 2024-12-07 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202412/Firmware__V5.7.19_241207_S3000618481.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.19_241207_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2343G2-LI2U - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.19 | Applied to: [DS-2CD2343G2-LI2U/SL(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202412/Firmware__V5.7.19_241207_S3000618481.zip) | 2024-12-07 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202412/Firmware__V5.7.19_241207_S3000618481.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.19_241207_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2343G2-LIZ - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.21 | Applied to: [DS-2CD2343G2-LIZ2UY(2.8/4mm)](https://assets.hikvision.com/prd/normal/all/files/202512/Firmware__V5.8.21_251117_S3000687899.zip) | 2025-11-17 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202512/Firmware__V5.8.21_251117_S3000687899.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.8.21_SP1_251117_Release_Note-H13U.pdf) |

</details>


<details>
<summary><h2>DS-2CD2343G2-LIZ2UY - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.21 | Applied to: [DS-2CD2343G2-LIZ2UY/SRB(2.8/4mm)](https://assets.hikvision.com/prd/normal/all/files/202512/Firmware__V5.8.21_251117_S3000687899.zip) | 2025-11-17 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202512/Firmware__V5.8.21_251117_S3000687899.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.8.21_SP1_251117_Release_Note-H13U.pdf) |

</details>


<details>
<summary><h2>DS-2CD2343G2D-LIZ2UY - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.11 | Applied to: [DS-2CD2343G2D-LIZ2UY/SL(2.8/4mm)](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.11_251216_S3000692172.zip) | 2025-12-16 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.11_251216_S3000692172.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.8.11_251216_Release_Note-IPCE_D_H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD2343G2P-LISU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.11 | Applied to: [DS-2CD2343G2P-LISU/SL(180°)](https://assets.hikvision.com/prd/normal/all/files/202511/Firmware__V5.8.11_251029_S3000683386.zip) | 2025-10-29 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202511/Firmware__V5.8.11_251029_S3000683386.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.8.11_SP1_251029_Release_Note-IPCE_P_E11.pdf) |

</details>


<details>
<summary><h2>DS-2CD2345FWD-I - IPC_G1 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.6.821 | Applied to: [DS-2CD2345FWD-I(4mm)](https://assets.hikvision.com/prd/public/all/files/202309/Firmware__V5.6.821_230831_S3000525150.zip)(BLACK) | 2023-08-31 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202309/Firmware__V5.6.821_230831_S3000525150.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202401/releasenote%5CNetwork_Camera-V5.6.821_Release_Note-IPC_G1_230831.pdf) |

</details>


<details>
<summary><h2>DS-2CD2345G0P-I - IPC_G1 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.6.821 | Applied to: [DS-2CD2345G0P-I(1.68mm)](https://assets.hikvision.com/prd/public/all/files/202309/Firmware__V5.6.821_230831_S3000525150.zip) | 2023-08-31 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202309/Firmware__V5.6.821_230831_S3000525150.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202401/releasenote%5CNetwork_Camera-V5.6.821_Release_Note-IPC_G1_230831.pdf) |

</details>


<details>
<summary><h2>DS-2CD2346G1-I - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.6.0 | Applied to: [DS-2CD2346G1-I/SL(4mm)](https://assets.hikvision.com/prd/public/all/files/18db80e0-2712-4496-8bd3-646f5014a59b.zip) | 2019-05-07 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/18db80e0-2712-4496-8bd3-646f5014a59b.zip) |  |

</details>


<details>
<summary><h2>DS-2CD2346G2-I - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.19 | Applied to: [DS-2CD2346G2-IU(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202412/Firmware__V5.7.19_241207_S3000618481.zip)(C)(BLACK) | 2024-12-07 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202412/Firmware__V5.7.19_241207_S3000618481.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.19_241207_Release_Note.pdf) |
| 5.5.800 | Applied to: [DS-2CD2346G2-IU(2.8mm)](https://assets.hikvision.com/prd/public/all/files/7ddcc773-b084-4adc-a9e1-08ed4b8252f4.zip)(C)(BLACK) | 2021-10-09 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/7ddcc773-b084-4adc-a9e1-08ed4b8252f4.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.19_241207_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2346G2-ISU - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.820 | Applied to: [DS-2CD2346G2-ISU/SL(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202312/Firmware__V5.5.820_231108_S3000539625.zip) | 2023-11-08 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202312/Firmware__V5.5.820_231108_S3000539625.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/330c4c2c-5730-4877-a942-0be87cea67ca.pdf) |
| 5.5.800 | Applied to: [DS-2CD2346G2-ISU/SL(2.8mm)](https://assets.hikvision.com/prd/public/all/files/7ddcc773-b084-4adc-a9e1-08ed4b8252f4.zip) | 2021-10-09 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/7ddcc773-b084-4adc-a9e1-08ed4b8252f4.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/330c4c2c-5730-4877-a942-0be87cea67ca.pdf) |

</details>


<details>
<summary><h2>DS-2CD2346G2H-I - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.19 | Applied to: [DS-2CD2346G2H-IU(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202412/Firmware__V5.7.19_241207_S3000618481.zip)(eF) | 2024-12-07 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202412/Firmware__V5.7.19_241207_S3000618481.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.19_241207_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2346G2H-IS2U - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.19 | Applied to: [DS-2CD2346G2H-IS2U/SRB(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202412/Firmware__V5.7.19_241207_S3000618481.zip)/eFO-STDBLK | 2024-12-07 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202412/Firmware__V5.7.19_241207_S3000618481.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.19_241207_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2346G3-IZ - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.21 | Applied to: [DS-2CD2346G3-IZY(2.8/4mm)](https://assets.hikvision.com/prd/normal/all/files/202512/Firmware__V5.8.21_251117_S3000687899.zip) | 2025-11-17 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202512/Firmware__V5.8.21_251117_S3000687899.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.8.21_SP1_251117_Release_Note-H13U.pdf) |

</details>


<details>
<summary><h2>DS-2CD2346G3-IZS2UY - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.21 | Applied to: [DS-2CD2346G3-IZS2UY/SRB(2.8/4mm)](https://assets.hikvision.com/prd/normal/all/files/202512/Firmware__V5.8.21_251117_S3000687899.zip) | 2025-11-17 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202512/Firmware__V5.8.21_251117_S3000687899.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.8.21_SP1_251117_Release_Note-H13U.pdf) |

</details>


<details>
<summary><h2>DS-2CD2346G3D-IZ2UY - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.11 | Applied to: [DS-2CD2346G3D-IZ2UY/SRB(2.8/4)](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.11_251216_S3000692172.zip)O-STDBLACK | 2025-12-16 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.11_251216_S3000692172.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.8.11_251216_Release_Note-IPCE_D_H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD2347G2-L - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.820 | Applied to: [DS-2CD2347G2-L(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202312/Firmware__V5.5.820_231108_S3000539625.zip) | 2023-11-08 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202312/Firmware__V5.5.820_231108_S3000539625.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202408/releasenote%5CNetwork_Camera-V5.5.820_Release_Note-G3.pdf) |
| 5.5.800 | Applied to: [DS-2CD2347G2-L(2.8mm)](https://assets.hikvision.com/prd/public/all/files/7ddcc773-b084-4adc-a9e1-08ed4b8252f4.zip) | 2021-10-09 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/7ddcc773-b084-4adc-a9e1-08ed4b8252f4.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202408/releasenote%5CNetwork_Camera-V5.5.820_Release_Note-G3.pdf) |

</details>


<details>
<summary><h2>DS-2CD2347G2-LSU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.19 | Applied to: [DS-2CD2347G2-LSU/SL/2](https://assets.hikvision.com/prd/public/all/files/202412/Firmware__V5.7.19_241207_S3000618481.zip).8mm/C/O-STD/BLACK | 2024-12-07 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202412/Firmware__V5.7.19_241207_S3000618481.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.19_241207_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2347G2H-LI - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.19 | Applied to: [DS-2CD2347G2H-LIU(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202412/Firmware__V5.7.19_241207_S3000618481.zip)(eF)/O-STD/BLACK | 2024-12-07 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202412/Firmware__V5.7.19_241207_S3000618481.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.19_241207_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2363G0-I - IPC_G1 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.6.821 | Applied to: [DS-2CD2363G0-I(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202309/Firmware__V5.6.821_230831_S3000525150.zip) | 2023-08-31 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202309/Firmware__V5.6.821_230831_S3000525150.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202401/releasenote%5CNetwork_Camera-V5.6.821_Release_Note-IPC_G1_230831.pdf) |

</details>


<details>
<summary><h2>DS-2CD2363G2P-LISU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.11 | Applied to: [DS-2CD2363G2P-LISU/SL(180°)](https://assets.hikvision.com/prd/normal/all/files/202511/Firmware__V5.8.11_251029_S3000683386.zip) | 2025-10-29 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202511/Firmware__V5.8.11_251029_S3000683386.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.8.11_SP1_251029_Release_Note-IPCE_P_E11.pdf) |

</details>


<details>
<summary><h2>DS-2CD2365G1-I - IPC_G1 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.6.821 | Applied to: [DS-2CD2365G1-I(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202309/Firmware__V5.6.821_230831_S3000525150.zip)(BLACK) | 2023-08-31 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202309/Firmware__V5.6.821_230831_S3000525150.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202401/releasenote%5CNetwork_Camera-V5.6.821_Release_Note-IPC_G1_230831.pdf) |

</details>


<details>
<summary><h2>DS-2CD2366G2P-ISU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.20 | Applied to: [DS-2CD2366G2P-ISU/SL(2.8mm)](https://assets.hikvision.com/prd/normal/all/files/202512/Firmware__V5.7.20_251125_S3000690065.zip)(C) | 2025-11-25 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202512/Firmware__V5.7.20_251125_S3000690065.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.20_251125_Release_Note-IPCE_P_G5.pdf) |

</details>


<details>
<summary><h2>DS-2CD2367G2P-LSU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.20 | Applied to: [DS-2CD2367G2P-LSU/SL(2.8mm)](https://assets.hikvision.com/prd/normal/all/files/202512/Firmware__V5.7.20_251125_S3000690065.zip)(C) | 2025-11-25 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202512/Firmware__V5.7.20_251125_S3000690065.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.20_251125_Release_Note-IPCE_P_G5.pdf) |

</details>


<details>
<summary><h2>DS-2CD2367G3-LI - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD2367G3-LI2UY(2.8mm)](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691342.zip) | 2025-12-10 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691342.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD2367G3-LIS2UY - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD2367G3-LIS2UY/SL(2.8mm)](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691342.zip) | 2025-12-10 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691342.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD2383G0-I - IPC_G1 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.6.821 | Applied to: [DS-2CD2383G0-I(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202309/Firmware__V5.6.821_230831_S3000525150.zip)(BLACK) | 2023-08-31 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202309/Firmware__V5.6.821_230831_S3000525150.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202401/releasenote%5CNetwork_Camera-V5.6.821_Release_Note-IPC_G1_230831.pdf) |

</details>


<details>
<summary><h2>DS-2CD2383G2-I - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.6 | Applied to: [DS-2CD2383G2-IU(2.8mm)](https://assets.hikvision.com/prd/normal/all/files/202602/Firmware__V5.7.6_260128_S3000701683.zip)(D)(BLACK) | 2026-01-28 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202602/Firmware__V5.7.6_260128_S3000701683.zip) |  |

</details>


<details>
<summary><h2>DS-2CD2383G2-LI - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.6 | Applied to: [DS-2CD2383G2-LI2U(2.8mm)](https://assets.hikvision.com/prd/normal/all/files/202602/Firmware__V5.7.6_260128_S3000701683.zip)(T) | 2026-01-28 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202602/Firmware__V5.7.6_260128_S3000701683.zip) |  |

</details>


<details>
<summary><h2>DS-2CD2383G2P-LISU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.11 | Applied to: [DS-2CD2383G2P-LISU/SL(180°)](https://assets.hikvision.com/prd/normal/all/files/202511/Firmware__V5.8.11_251029_S3000683386.zip) | 2025-10-29 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202511/Firmware__V5.8.11_251029_S3000683386.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.8.11_SP1_251029_Release_Note-IPCE_P_E11.pdf) |

</details>


<details>
<summary><h2>DS-2CD2385G1-I - IPC_G1 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.6.821 | Applied to: [DS-2CD2385G1-I(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202309/Firmware__V5.6.821_230831_S3000525150.zip) | 2023-08-31 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202309/Firmware__V5.6.821_230831_S3000525150.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202401/releasenote%5CNetwork_Camera-V5.6.821_Release_Note-IPC_G1_230831.pdf) |

</details>


<details>
<summary><h2>DS-2CD2386G2-I - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.820 | Applied to: [DS-2CD2386G2-I(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202312/Firmware__V5.5.820_231108_S3000539625.zip) | 2023-11-08 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202312/Firmware__V5.5.820_231108_S3000539625.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/330c4c2c-5730-4877-a942-0be87cea67ca.pdf) |
| 5.5.800 | Applied to: [DS-2CD2386G2-I(2.8mm)](https://assets.hikvision.com/prd/public/all/files/7ddcc773-b084-4adc-a9e1-08ed4b8252f4.zip) | 2021-10-09 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/7ddcc773-b084-4adc-a9e1-08ed4b8252f4.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/330c4c2c-5730-4877-a942-0be87cea67ca.pdf) |

</details>


<details>
<summary><h2>DS-2CD2386G2-ISU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.820 | Applied to: [DS-2CD2386G2-ISU/SL(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202312/Firmware__V5.5.820_231108_S3000539625.zip) | 2023-11-08 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202312/Firmware__V5.5.820_231108_S3000539625.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202408/releasenote%5CNetwork_Camera-V5.5.820_Release_Note-G3.pdf) |

</details>


<details>
<summary><h2>DS-2CD2387G2P-LSU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.20 | Applied to: [DS-2CD2387G2P-LSU/SL(4mm)](https://assets.hikvision.com/prd/normal/all/files/202512/Firmware__V5.7.20_251125_S3000690065.zip)(C)/O-STD/BLACK | 2025-11-25 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202512/Firmware__V5.7.20_251125_S3000690065.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.20_251125_Release_Note-IPCE_P_G5.pdf) |

</details>


<details>
<summary><h2>DS-2CD2387G3-LI - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD2387G3-LI2UY(2.8mm)](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691342.zip) | 2025-12-10 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691342.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD2387G3-LIS2UY - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD2387G3-LIS2UY/SL(2.8mm)](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691342.zip) | 2025-12-10 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691342.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD2421G0-I - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2421G0-I(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202505/Firmware__V5.7.23_241211_S3000620665.zip) | 2024-12-11 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202505/Firmware__V5.7.23_241211_S3000620665.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202404/1712790070190/releasenote%5CIPC_E6_5.5.821_Release_Note.pdf) |
| 5.5.821 | Applied to: [DS-2CD2421G0-I(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202312/Firmware__V5.5.821_231108_S3000539541.zip) | 2023-11-08 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202312/Firmware__V5.5.821_231108_S3000539541.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202404/1712790070190/releasenote%5CIPC_E6_5.5.821_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2423G0-I - IPC_G1 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.6.821 | Applied to: [DS-2CD2423G0-I(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202309/Firmware__V5.6.821_230831_S3000525150.zip) | 2023-08-31 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202309/Firmware__V5.6.821_230831_S3000525150.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202401/releasenote%5CNetwork_Camera-V5.6.821_Release_Note-IPC_G1_230831.pdf) |
| 5.5.83 | Applied to: [DS-2CD2423G0-I(2.8mm)](https://assets.hikvision.com/prd/public/all/files/52faab7e-03ae-4dee-9dbd-a67988b4b16b.zip) | 2019-02-21 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/52faab7e-03ae-4dee-9dbd-a67988b4b16b.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202401/releasenote%5CNetwork_Camera-V5.6.821_Release_Note-IPC_G1_230831.pdf) |

</details>


<details>
<summary><h2>DS-2CD2425FWD-I - IPC_G1 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.6.821 | Applied to: [DS-2CD2425FWD-I(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202309/Firmware__V5.6.821_230831_S3000525150.zip) | 2023-08-31 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202309/Firmware__V5.6.821_230831_S3000525150.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202401/releasenote%5CNetwork_Camera-V5.6.821_Release_Note-IPC_G1_230831.pdf) |

</details>


<details>
<summary><h2>DS-2CD2443G0-I - IPC_G1 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.6.821 | Applied to: [DS-2CD2443G0-I(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202309/Firmware__V5.6.821_230831_S3000525150.zip) | 2023-08-31 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202309/Firmware__V5.6.821_230831_S3000525150.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202401/releasenote%5CNetwork_Camera-V5.6.821_Release_Note-IPC_G1_230831.pdf) |
| 5.5.83 | Applied to: [DS-2CD2443G0-I(2.8mm)](https://assets.hikvision.com/prd/public/all/files/52faab7e-03ae-4dee-9dbd-a67988b4b16b.zip) | 2019-02-21 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/52faab7e-03ae-4dee-9dbd-a67988b4b16b.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202401/releasenote%5CNetwork_Camera-V5.6.821_Release_Note-IPC_G1_230831.pdf) |

</details>


<details>
<summary><h2>DS-2CD2455FWD-I - IPC_G1 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.6.821 | Applied to: [DS-2CD2455FWD-I(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202309/Firmware__V5.6.821_230831_S3000525150.zip) | 2023-08-31 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202309/Firmware__V5.6.821_230831_S3000525150.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202401/releasenote%5CNetwork_Camera-V5.6.821_Release_Note-IPC_G1_230831.pdf) |

</details>


<details>
<summary><h2>DS-2CD2463G0-I - IPC_G1 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.6.821 | Applied to: [DS-2CD2463G0-I(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202309/Firmware__V5.6.821_230831_S3000525150.zip) | 2023-08-31 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202309/Firmware__V5.6.821_230831_S3000525150.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202401/releasenote%5CNetwork_Camera-V5.6.821_Release_Note-IPC_G1_230831.pdf) |

</details>


<details>
<summary><h2>DS-2CD2523G0-I - IPC_G1 (3 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.6.821 | Applied to: [DS-2CD2523G0-I(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202309/Firmware__V5.6.821_230831_S3000525150.zip) | 2023-08-31 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202309/Firmware__V5.6.821_230831_S3000525150.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202401/releasenote%5CNetwork_Camera-V5.6.821_Release_Note-IPC_G1_230831.pdf) |
| 5.6.6 | Applied to: [DS-2CD2523G0-I(2.8mm)](https://assets.hikvision.com/prd/public/all/files/f18aceb7-b896-4c7d-ad2e-8f0d2a91bcc3.zip) | 2021-06-25 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/f18aceb7-b896-4c7d-ad2e-8f0d2a91bcc3.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202401/releasenote%5CNetwork_Camera-V5.6.821_Release_Note-IPC_G1_230831.pdf) |
| 5.6.2 | Applied to: [DS-2CD2523G0-I(2.8mm)](https://assets.hikvision.com/prd/public/all/files/f88f5389-fd05-44ea-9adc-874910511d97.zip) | 2019-07-01 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/f88f5389-fd05-44ea-9adc-874910511d97.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202401/releasenote%5CNetwork_Camera-V5.6.821_Release_Note-IPC_G1_230831.pdf) |

</details>


<details>
<summary><h2>DS-2CD2523G2-I - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.0 | Applied to: [DS-2CD2523G2-I(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202411/Firmware__V5.7.0_241023_S3000609022.zip)(D) | 2024-10-23 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202411/Firmware__V5.7.0_241023_S3000609022.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202507/releasenote%5CNetwork_Camera-V5.7.0_SP6_Release_Note-G6_I.pdf) |
| 5.7.18 | Applied to: [DS-2CD2523G2-I(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202409/Firmware__V5.7.18_240826_S3000597013.zip)(D) | 2024-08-26 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202409/Firmware__V5.7.18_240826_S3000597013.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202507/releasenote%5CNetwork_Camera-V5.7.0_SP6_Release_Note-G6_I.pdf) |

</details>


<details>
<summary><h2>DS-2CD2525FWD-I - IPC_G1 (3 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.6.821 | Applied to: [DS-2CD2525FWD-I(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202309/Firmware__V5.6.821_230831_S3000525150.zip) | 2023-08-31 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202309/Firmware__V5.6.821_230831_S3000525150.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202401/releasenote%5CNetwork_Camera-V5.6.821_Release_Note-IPC_G1_230831.pdf) |
| 5.6.6 | Applied to: [DS-2CD2525FWD-I(2.8mm)](https://assets.hikvision.com/prd/public/all/files/f18aceb7-b896-4c7d-ad2e-8f0d2a91bcc3.zip) | 2021-06-25 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/f18aceb7-b896-4c7d-ad2e-8f0d2a91bcc3.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202401/releasenote%5CNetwork_Camera-V5.6.821_Release_Note-IPC_G1_230831.pdf) |
| 5.6.2 | Applied to: [DS-2CD2525FWD-I(2.8mm)](https://assets.hikvision.com/prd/public/all/files/f88f5389-fd05-44ea-9adc-874910511d97.zip) | 2019-07-01 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/f88f5389-fd05-44ea-9adc-874910511d97.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202401/releasenote%5CNetwork_Camera-V5.6.821_Release_Note-IPC_G1_230831.pdf) |

</details>


<details>
<summary><h2>DS-2CD2526G2-IS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.0 | Applied to: [DS-2CD2526G2-I(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202411/Firmware__V5.7.0_241023_S3000609022.zip)(D) | 2024-10-23 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202411/Firmware__V5.7.0_241023_S3000609022.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202507/releasenote%5CNetwork_Camera-V5.7.0_SP6_Release_Note-G6_I.pdf) |

</details>


<details>
<summary><h2>DS-2CD2543G0-I - IPC_G1 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.6.821 | Applied to: [DS-2CD2543G0-I(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202309/Firmware__V5.6.821_230831_S3000525150.zip)(BLACK) | 2023-08-31 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202309/Firmware__V5.6.821_230831_S3000525150.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202401/releasenote%5CNetwork_Camera-V5.6.821_Release_Note-IPC_G1_230831.pdf) |
| 5.6.2 | Applied to: [DS-2CD2543G0-I(2.8mm)](https://assets.hikvision.com/prd/public/all/files/f88f5389-fd05-44ea-9adc-874910511d97.zip)(BLACK) | 2019-07-01 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/f88f5389-fd05-44ea-9adc-874910511d97.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202401/releasenote%5CNetwork_Camera-V5.6.821_Release_Note-IPC_G1_230831.pdf) |

</details>


<details>
<summary><h2>DS-2CD2545FWD-I - IPC_G1 (3 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.6.821 | Applied to: [DS-2CD2545FWD-IWS(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202309/Firmware__V5.6.821_230831_S3000525150.zip)(D) | 2023-08-31 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202309/Firmware__V5.6.821_230831_S3000525150.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202401/releasenote%5CNetwork_Camera-V5.6.821_Release_Note-IPC_G1_230831.pdf) |
| 5.6.6 | Applied to: [DS-2CD2545FWD-IWS(2.8mm)](https://assets.hikvision.com/prd/public/all/files/f18aceb7-b896-4c7d-ad2e-8f0d2a91bcc3.zip)(D) | 2021-06-25 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/f18aceb7-b896-4c7d-ad2e-8f0d2a91bcc3.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202401/releasenote%5CNetwork_Camera-V5.6.821_Release_Note-IPC_G1_230831.pdf) |
| 5.6.3 | Applied to: [DS-2CD2545FWD-IWS(2.8mm)](https://assets.hikvision.com/prd/public/all/files/fd283720-cf75-46b4-a8b9-aaa670def906.zip)(D) | 2019-09-23 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/fd283720-cf75-46b4-a8b9-aaa670def906.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202401/releasenote%5CNetwork_Camera-V5.6.821_Release_Note-IPC_G1_230831.pdf) |

</details>


<details>
<summary><h2>DS-2CD2546G2-IS - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.820 | Applied to: [DS-2CD2546G2-I(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202312/Firmware__V5.5.820_231108_S3000539625.zip) | 2023-11-08 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202312/Firmware__V5.5.820_231108_S3000539625.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/330c4c2c-5730-4877-a942-0be87cea67ca.pdf) |
| 5.5.800 | Applied to: [DS-2CD2546G2-I(2.8mm)](https://assets.hikvision.com/prd/public/all/files/7ddcc773-b084-4adc-a9e1-08ed4b8252f4.zip) | 2021-10-09 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/7ddcc773-b084-4adc-a9e1-08ed4b8252f4.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/330c4c2c-5730-4877-a942-0be87cea67ca.pdf) |

</details>


<details>
<summary><h2>DS-2CD2555FWD-I - IPC_G1 (3 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.6.821 | Applied to: [DS-2CD2555FWD-I(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202309/Firmware__V5.6.821_230831_S3000525150.zip) | 2023-08-31 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202309/Firmware__V5.6.821_230831_S3000525150.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202401/releasenote%5CNetwork_Camera-V5.6.821_Release_Note-IPC_G1_230831.pdf) |
| 5.6.6 | Applied to: [DS-2CD2555FWD-I(2.8mm)](https://assets.hikvision.com/prd/public/all/files/f18aceb7-b896-4c7d-ad2e-8f0d2a91bcc3.zip) | 2021-06-25 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/f18aceb7-b896-4c7d-ad2e-8f0d2a91bcc3.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202401/releasenote%5CNetwork_Camera-V5.6.821_Release_Note-IPC_G1_230831.pdf) |
| 5.6.2 | Applied to: [DS-2CD2555FWD-I(2.8mm)](https://assets.hikvision.com/prd/public/all/files/f88f5389-fd05-44ea-9adc-874910511d97.zip) | 2019-07-01 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/f88f5389-fd05-44ea-9adc-874910511d97.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202401/releasenote%5CNetwork_Camera-V5.6.821_Release_Note-IPC_G1_230831.pdf) |

</details>


<details>
<summary><h2>DS-2CD2563G0-I - IPC_G1 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.6.821 | Applied to: [DS-2CD2563G0-I(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202309/Firmware__V5.6.821_230831_S3000525150.zip) | 2023-08-31 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202309/Firmware__V5.6.821_230831_S3000525150.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202401/releasenote%5CNetwork_Camera-V5.6.821_Release_Note-IPC_G1_230831.pdf) |
| 5.6.2 | Applied to: [DS-2CD2563G0-I(2.8mm)](https://assets.hikvision.com/prd/public/all/files/f88f5389-fd05-44ea-9adc-874910511d97.zip) | 2019-07-01 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/f88f5389-fd05-44ea-9adc-874910511d97.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202401/releasenote%5CNetwork_Camera-V5.6.821_Release_Note-IPC_G1_230831.pdf) |

</details>


<details>
<summary><h2>DS-2CD26123G2-LIZS2U - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.2 | Applied to: [DS-2CD26123G2-LIZS2UY/SL(2.8-12mm)](https://assets.hikvision.com/prd/normal/all/files/202511/Firmware__V5.8.2_251103_S3000682542.zip)/O-STD | 2025-11-03 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202511/Firmware__V5.8.2_251103_S3000682542.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202511/releasenote%5CNetwork_Camera-V5.8.2_251103_Release_Note-IPCE_G9.pdf) |

</details>


<details>
<summary><h2>DS-2CD26123G2-LIZS2UY - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.2 | Applied to: [DS-2CD26123G2-LIZS2UY(2.8-12mm)](https://assets.hikvision.com/prd/normal/all/files/202511/Firmware__V5.8.2_251103_S3000682542.zip) | 2025-11-03 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202511/Firmware__V5.8.2_251103_S3000682542.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202511/releasenote%5CNetwork_Camera-V5.8.2_251103_Release_Note-IPCE_G9.pdf) |

</details>


<details>
<summary><h2>DS-2CD26126G3-IZS2UY - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.2 | Applied to: [DS-2CD26126G3-IZS2UY/SRB(2.8-12)](https://assets.hikvision.com/prd/normal/all/files/202511/Firmware__V5.8.2_251103_S3000682542.zip)eFO-STD | 2025-11-03 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202511/Firmware__V5.8.2_251103_S3000682542.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202511/releasenote%5CNetwork_Camera-V5.8.2_251103_Release_Note-IPCE_G9.pdf) |

</details>


<details>
<summary><h2>DS-2CD26126G3-IZSY - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.2 | Applied to: [DS-2CD26126G3-IZSY(2.8-12mm)](https://assets.hikvision.com/prd/normal/all/files/202511/Firmware__V5.8.2_251103_S3000682542.zip)(eF) | 2025-11-03 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202511/Firmware__V5.8.2_251103_S3000682542.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202511/releasenote%5CNetwork_Camera-V5.8.2_251103_Release_Note-IPCE_G9.pdf) |

</details>


<details>
<summary><h2>DS-2CD26166G3-IZS2UY - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.2 | Applied to: [DS-2CD26166G3-IZS2UY/SRB(2812)](https://assets.hikvision.com/prd/normal/all/files/202511/Firmware__V5.8.2_251103_S3000682542.zip)eFOSTDBLK | 2025-11-03 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202511/Firmware__V5.8.2_251103_S3000682542.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202511/releasenote%5CNetwork_Camera-V5.8.2_251103_Release_Note-IPCE_G9.pdf) |

</details>


<details>
<summary><h2>DS-2CD26166G3-IZSY - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.2 | Applied to: [DS-2CD26166G3-IZSY(2.8-12mm)](https://assets.hikvision.com/prd/normal/all/files/202511/Firmware__V5.8.2_251103_S3000682542.zip)(eF) | 2025-11-03 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202511/Firmware__V5.8.2_251103_S3000682542.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202511/releasenote%5CNetwork_Camera-V5.8.2_251103_Release_Note-IPCE_G9.pdf) |

</details>


<details>
<summary><h2>DS-2CD2621G0-I - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD2621G0-IZS(2.8-12mm)](https://assets.hikvision.com/prd/public/all/files/202505/Firmware__V5.7.23_241211_S3000620665.zip) | 2024-12-11 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202505/Firmware__V5.7.23_241211_S3000620665.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202507/releasenote%5CNetwork_Camera-V5.7.23_SP2_Release_Note-E8.pdf) |
| 5.5.800 | Applied to: [DS-2CD2621G0-IZS(2.8-12mm)](https://assets.hikvision.com/prd/public/all/files/2b726e56-901f-4e8d-9fd4-e9d67bc8e80a.zip) | 2021-06-28 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/2b726e56-901f-4e8d-9fd4-e9d67bc8e80a.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202507/releasenote%5CNetwork_Camera-V5.7.23_SP2_Release_Note-E8.pdf) |

</details>


<details>
<summary><h2>DS-2CD2623G1-IZ - IPC_G1 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.6.821 | Applied to: [DS-2CD2623G1-IZ(2.8-12mm)](https://assets.hikvision.com/prd/public/all/files/202309/Firmware__V5.6.821_230831_S3000525150.zip) | 2023-08-31 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202309/Firmware__V5.6.821_230831_S3000525150.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202401/releasenote%5CNetwork_Camera-V5.6.821_Release_Note-IPC_G1_230831.pdf) |

</details>


<details>
<summary><h2>DS-2CD2623G2-IZS - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.0 | Applied to: [DS-2CD2623G2-IZS(2.8-12mm)](https://assets.hikvision.com/prd/public/all/files/202411/Firmware__V5.7.0_241023_S3000609022.zip)(US Branch) | 2024-10-23 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202411/Firmware__V5.7.0_241023_S3000609022.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202312/releasenote%5CNetwork_Camera-V5.7.13_Release_Note-G5.pdf) |
| 5.7.13 | Applied to: [DS-2CD2623G2-IZS(2.8-12mm)](https://assets.hikvision.com/prd/public/all/files/202304/Firmware__V5.7.13_230403_S3000490228.zip)(US Branch) | 2023-04-03 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202304/Firmware__V5.7.13_230403_S3000490228.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202312/releasenote%5CNetwork_Camera-V5.7.13_Release_Note-G5.pdf) |

</details>


<details>
<summary><h2>DS-2CD2625FHWD-IZS - IPC_G1 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.6.821 | Applied to: [DS-2CD2625FHWD-IZS(2.8-12mm)](https://assets.hikvision.com/prd/public/all/files/202309/Firmware__V5.6.821_230831_S3000525150.zip) | 2023-08-31 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202309/Firmware__V5.6.821_230831_S3000525150.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202401/releasenote%5CNetwork_Camera-V5.6.821_Release_Note-IPC_G1_230831.pdf) |

</details>


<details>
<summary><h2>DS-2CD2625FWD-IZS - IPC_G1 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.6.821 | Applied to: [DS-2CD2625FWD-IZS(2.8-12mm)](https://assets.hikvision.com/prd/public/all/files/202309/Firmware__V5.6.821_230831_S3000525150.zip) | 2023-08-31 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202309/Firmware__V5.6.821_230831_S3000525150.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202401/releasenote%5CNetwork_Camera-V5.6.821_Release_Note-IPC_G1_230831.pdf) |

</details>


<details>
<summary><h2>DS-2CD2626G2-IZS - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.0 | Applied to: [DS-2CD2626G2-IZS(2.8-12mm)](https://assets.hikvision.com/prd/public/all/files/202411/Firmware__V5.7.0_241023_S3000609022.zip) | 2024-10-23 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202411/Firmware__V5.7.0_241023_S3000609022.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202408/releasenote%5CNetwork_Camera-V5.5.820_Release_Note-G3.pdf) |
| 5.5.820 | Applied to: [DS-2CD2626G2-IZS(2.8-12mm)](https://assets.hikvision.com/prd/public/all/files/202312/Firmware__V5.5.820_231108_S3000539625.zip) | 2023-11-08 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202312/Firmware__V5.5.820_231108_S3000539625.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202408/releasenote%5CNetwork_Camera-V5.5.820_Release_Note-G3.pdf) |

</details>


<details>
<summary><h2>DS-2CD2626G2-IZSU - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.0 | Applied to: [DS-2CD2626G2-IZSU/SL(2.8-12mm)](https://assets.hikvision.com/prd/public/all/files/202411/Firmware__V5.7.0_241023_S3000609022.zip) | 2024-10-23 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202411/Firmware__V5.7.0_241023_S3000609022.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202408/releasenote%5CNetwork_Camera-V5.5.820_Release_Note-G3.pdf) |
| 5.5.820 | Applied to: [DS-2CD2626G2-IZSU/SL(2.8-12mm)](https://assets.hikvision.com/prd/public/all/files/202312/Firmware__V5.5.820_231108_S3000539625.zip) | 2023-11-08 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202312/Firmware__V5.5.820_231108_S3000539625.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202408/releasenote%5CNetwork_Camera-V5.5.820_Release_Note-G3.pdf) |

</details>


<details>
<summary><h2>DS-2CD2626G2T-IZS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.0 | Applied to: [DS-2CD2626G2T-IZS(2.8-12mm)](https://assets.hikvision.com/prd/public/all/files/202411/Firmware__V5.7.0_241023_S3000609022.zip)(D) | 2024-10-23 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202411/Firmware__V5.7.0_241023_S3000609022.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202507/releasenote%5CNetwork_Camera-V5.7.0_SP6_Release_Note-G6_I.pdf) |

</details>


<details>
<summary><h2>DS-2CD2643G1-IZ - IPC_G1 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.6.821 | Applied to: [DS-2CD2643G1-IZS(2.8-12mm)](https://assets.hikvision.com/prd/public/all/files/202309/Firmware__V5.6.821_230831_S3000525150.zip) | 2023-08-31 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202309/Firmware__V5.6.821_230831_S3000525150.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202401/releasenote%5CNetwork_Camera-V5.6.821_Release_Note-IPC_G1_230831.pdf) |

</details>


<details>
<summary><h2>DS-2CD2645FWD-IZS - IPC_G1 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.6.821 | Applied to: [DS-2CD2645FWD-IZS/2](https://assets.hikvision.com/prd/public/all/files/202309/Firmware__V5.6.821_230831_S3000525150.zip).8-12mm/B/O-STD/BLACK | 2023-08-31 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202309/Firmware__V5.6.821_230831_S3000525150.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202401/releasenote%5CNetwork_Camera-V5.6.821_Release_Note-IPC_G1_230831.pdf) |

</details>


<details>
<summary><h2>DS-2CD2646G1-IZS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.6.0 | Applied to: [DS-2CD2646G1-IZS(2.8-12mm)](https://assets.hikvision.com/prd/public/all/files/18db80e0-2712-4496-8bd3-646f5014a59b.zip) | 2019-05-07 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/18db80e0-2712-4496-8bd3-646f5014a59b.zip) |  |

</details>


<details>
<summary><h2>DS-2CD2646G2-IZS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.820 | Applied to: [DS-2CD2646G2-IZS(2.8-12mm)](https://assets.hikvision.com/prd/public/all/files/202312/Firmware__V5.5.820_231108_S3000539625.zip) | 2023-11-08 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202312/Firmware__V5.5.820_231108_S3000539625.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202408/releasenote%5CNetwork_Camera-V5.5.820_Release_Note-G3.pdf) |

</details>


<details>
<summary><h2>DS-2CD2646G2-IZSU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.800 | Applied to: [DS-2CD2646G2-IZSU/SL(2.8-12mm)](https://assets.hikvision.com/prd/public/all/files/7ddcc773-b084-4adc-a9e1-08ed4b8252f4.zip) | 2021-10-09 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/7ddcc773-b084-4adc-a9e1-08ed4b8252f4.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/330c4c2c-5730-4877-a942-0be87cea67ca.pdf) |

</details>


<details>
<summary><h2>DS-2CD2663G1-IZ - IPC_G1 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.6.821 | Applied to: [DS-2CD2663G1-IZS(2.8-12mm)](https://assets.hikvision.com/prd/public/all/files/202309/Firmware__V5.6.821_230831_S3000525150.zip) | 2023-08-31 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202309/Firmware__V5.6.821_230831_S3000525150.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202401/releasenote%5CNetwork_Camera-V5.6.821_Release_Note-IPC_G1_230831.pdf) |

</details>


<details>
<summary><h2>DS-2CD2665G0-IZS - IPC_G1 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.6.821 | Applied to: [DS-2CD2665G0-IZS(2.8-12mm)](https://assets.hikvision.com/prd/public/all/files/202309/Firmware__V5.6.821_230831_S3000525150.zip) | 2023-08-31 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202309/Firmware__V5.6.821_230831_S3000525150.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202401/releasenote%5CNetwork_Camera-V5.6.821_Release_Note-IPC_G1_230831.pdf) |

</details>


<details>
<summary><h2>DS-2CD2667G3-LIZS2UY - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD2667G3-LIZS2UY/SL(2.8-12mm)](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691342.zip) | 2025-12-10 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691342.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD2667G3-LIZSY - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD2667G3-LIZSY(2.8-12mm)](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691342.zip)/O-STD/BLACK | 2025-12-10 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691342.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD2667G3T-LIZSY - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD2667G3T-LIZSY(2.8-12mm)](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691342.zip) | 2025-12-10 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691342.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD2683G1-IZ - IPC_G1 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.6.821 | Applied to: [DS-2CD2683G1-IZ(2.8-12mm)](https://assets.hikvision.com/prd/public/all/files/202309/Firmware__V5.6.821_230831_S3000525150.zip) | 2023-08-31 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202309/Firmware__V5.6.821_230831_S3000525150.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202401/releasenote%5CNetwork_Camera-V5.6.821_Release_Note-IPC_G1_230831.pdf) |

</details>


<details>
<summary><h2>DS-2CD2683G2-IZS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.6 | Applied to: [DS-2CD2683G2-IZS(2.8-12mm)](https://assets.hikvision.com/prd/normal/all/files/202602/Firmware__V5.7.6_260128_S3000701683.zip)(D) | 2026-01-28 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202602/Firmware__V5.7.6_260128_S3000701683.zip) |  |

</details>


<details>
<summary><h2>DS-2CD2683G2-LIZS2U - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.6 | Applied to: [DS-2CD2683G2-LIZS2U(2.8-12mm)](https://assets.hikvision.com/prd/normal/all/files/202602/Firmware__V5.7.6_260128_S3000701683.zip)(T) | 2026-01-28 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202602/Firmware__V5.7.6_260128_S3000701683.zip) |  |

</details>


<details>
<summary><h2>DS-2CD2685G0-IZS - IPC_G1 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.6.821 | Applied to: [DS-2CD2685G0-IZS(2.8-12mm)](https://assets.hikvision.com/prd/public/all/files/202309/Firmware__V5.6.821_230831_S3000525150.zip) | 2023-08-31 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202309/Firmware__V5.6.821_230831_S3000525150.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202401/releasenote%5CNetwork_Camera-V5.6.821_Release_Note-IPC_G1_230831.pdf) |

</details>


<details>
<summary><h2>DS-2CD2686G2-IZS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.820 | Applied to: [DS-2CD2686G2-IZS(2.8-12mm)](https://assets.hikvision.com/prd/public/all/files/202312/Firmware__V5.5.820_231108_S3000539625.zip) | 2023-11-08 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202312/Firmware__V5.5.820_231108_S3000539625.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202408/releasenote%5CNetwork_Camera-V5.5.820_Release_Note-G3.pdf) |

</details>


<details>
<summary><h2>DS-2CD2686G2-IZSU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.820 | Applied to: [DS-2CD2686G2-IZSU/SL(2.8-12mm)](https://assets.hikvision.com/prd/public/all/files/202312/Firmware__V5.5.820_231108_S3000539625.zip) | 2023-11-08 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202312/Firmware__V5.5.820_231108_S3000539625.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202408/releasenote%5CNetwork_Camera-V5.5.820_Release_Note-G3.pdf) |

</details>


<details>
<summary><h2>DS-2CD2687G3-LIZS2UY - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD2687G3-LIZS2UY/SRB(2.8-12mm)](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691342.zip)/O-STD | 2025-12-10 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691342.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD2687G3-LIZSY - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD2687G3-LIZSY(2.8-12mm)](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691342.zip) | 2025-12-10 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691342.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD2687G3T-LIZSY - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD2687G3T-LIZSY(2.8-12mm)](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691342.zip) | 2025-12-10 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691342.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD27123G2-LIZS2UY - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.2 | Applied to: [DS-2CD27123G2-LIZS2UY(2.8-12mm)](https://assets.hikvision.com/prd/normal/all/files/202511/Firmware__V5.8.2_251103_S3000682542.zip) | 2025-11-03 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202511/Firmware__V5.8.2_251103_S3000682542.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202511/releasenote%5CNetwork_Camera-V5.8.2_251103_Release_Note-IPCE_G9.pdf) |

</details>


<details>
<summary><h2>DS-2CD27126G3-IPTRZS2UY - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.2 | Applied to: [DS-2CD27126G3-IPTRZS2UY/SL(2.8-12)](https://assets.hikvision.com/prd/normal/all/files/202511/Firmware__V5.8.2_251103_S3000682542.zip)O-STD | 2025-11-03 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202511/Firmware__V5.8.2_251103_S3000682542.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202511/releasenote%5CNetwork_Camera-V5.8.2_251103_Release_Note-IPCE_G9.pdf) |

</details>


<details>
<summary><h2>DS-2CD27126G3-IPTRZSY - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.2 | Applied to: [DS-2CD27126G3-IPTRZSY(2.8-12mm)](https://assets.hikvision.com/prd/normal/all/files/202511/Firmware__V5.8.2_251103_S3000682542.zip) | 2025-11-03 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202511/Firmware__V5.8.2_251103_S3000682542.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202511/releasenote%5CNetwork_Camera-V5.8.2_251103_Release_Note-IPCE_G9.pdf) |

</details>


<details>
<summary><h2>DS-2CD27166G3-IPTRZS2UY - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.2 | Applied to: [DS-2CD27166G3-IPTRZS2UY/SL(2.8-12)](https://assets.hikvision.com/prd/normal/all/files/202511/Firmware__V5.8.2_251103_S3000682542.zip)O-STD | 2025-11-03 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202511/Firmware__V5.8.2_251103_S3000682542.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202511/releasenote%5CNetwork_Camera-V5.8.2_251103_Release_Note-IPCE_G9.pdf) |

</details>


<details>
<summary><h2>DS-2CD27166G3-IPTRZSY - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.2 | Applied to: [DS-2CD27166G3-IPTRZSY(2.8-12mm)](https://assets.hikvision.com/prd/normal/all/files/202511/Firmware__V5.8.2_251103_S3000682542.zip) | 2025-11-03 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202511/Firmware__V5.8.2_251103_S3000682542.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202511/releasenote%5CNetwork_Camera-V5.8.2_251103_Release_Note-IPCE_G9.pdf) |

</details>


<details>
<summary><h2>DS-2CD2721G0-I - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.800 | Applied to: [DS-2CD2721G0-I(2.8-12mm)](https://assets.hikvision.com/prd/public/all/files/2b726e56-901f-4e8d-9fd4-e9d67bc8e80a.zip) | 2021-06-28 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/2b726e56-901f-4e8d-9fd4-e9d67bc8e80a.zip) |  |

</details>


<details>
<summary><h2>DS-2CD2723G1-IZ - IPC_G1 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.6.821 | Applied to: [DS-2CD2723G1-IZ(2.8-12mm)](https://assets.hikvision.com/prd/public/all/files/202309/Firmware__V5.6.821_230831_S3000525150.zip) | 2023-08-31 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202309/Firmware__V5.6.821_230831_S3000525150.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202401/releasenote%5CNetwork_Camera-V5.6.821_Release_Note-IPC_G1_230831.pdf) |

</details>


<details>
<summary><h2>DS-2CD2723G2-IZS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.0 | Applied to: [DS-2CD2723G2-IZS(2.8-12mm)](https://assets.hikvision.com/prd/public/all/files/202411/Firmware__V5.7.0_241023_S3000609022.zip)(D) | 2024-10-23 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202411/Firmware__V5.7.0_241023_S3000609022.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202507/releasenote%5CNetwork_Camera-V5.7.0_SP6_Release_Note-G6_I.pdf) |

</details>


<details>
<summary><h2>DS-2CD2725FHWD-IZS - IPC_G1 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.6.821 | Applied to: [DS-2CD2725FHWD-IZS(2.8-12mm)](https://assets.hikvision.com/prd/public/all/files/202309/Firmware__V5.6.821_230831_S3000525150.zip) | 2023-08-31 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202309/Firmware__V5.6.821_230831_S3000525150.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202401/releasenote%5CNetwork_Camera-V5.6.821_Release_Note-IPC_G1_230831.pdf) |

</details>


<details>
<summary><h2>DS-2CD2725FWD-IZS - IPC_G1 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.6.821 | Applied to: [DS-2CD2725FWD-IZS(2.8-12mm)](https://assets.hikvision.com/prd/public/all/files/202309/Firmware__V5.6.821_230831_S3000525150.zip) | 2023-08-31 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202309/Firmware__V5.6.821_230831_S3000525150.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202401/releasenote%5CNetwork_Camera-V5.6.821_Release_Note-IPC_G1_230831.pdf) |

</details>


<details>
<summary><h2>DS-2CD2726G1-IZS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.6.0 | Applied to: [DS-2CD2726G1-IZS(2.8-12mm)](https://assets.hikvision.com/prd/public/all/files/18db80e0-2712-4496-8bd3-646f5014a59b.zip) | 2019-05-07 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/18db80e0-2712-4496-8bd3-646f5014a59b.zip) |  |

</details>


<details>
<summary><h2>DS-2CD2726G2-IZS - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.0 | Applied to: [DS-2CD2726G2-IZS(2.8-12mm)](https://assets.hikvision.com/prd/public/all/files/202411/Firmware__V5.7.0_241023_S3000609022.zip) | 2024-10-23 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202411/Firmware__V5.7.0_241023_S3000609022.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202408/releasenote%5CNetwork_Camera-V5.5.820_Release_Note-G3.pdf) |
| 5.5.820 | Applied to: [DS-2CD2726G2-IZS(2.8-12mm)](https://assets.hikvision.com/prd/public/all/files/202312/Firmware__V5.5.820_231108_S3000539625.zip) | 2023-11-08 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202312/Firmware__V5.5.820_231108_S3000539625.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202408/releasenote%5CNetwork_Camera-V5.5.820_Release_Note-G3.pdf) |

</details>


<details>
<summary><h2>DS-2CD2726G2T-IZS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.0 | Applied to: [DS-2CD2726G2T-IZS(2.8-12mm)](https://assets.hikvision.com/prd/public/all/files/202411/Firmware__V5.7.0_241023_S3000609022.zip)(D) | 2024-10-23 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202411/Firmware__V5.7.0_241023_S3000609022.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202507/releasenote%5CNetwork_Camera-V5.7.0_SP6_Release_Note-G6_I.pdf) |

</details>


<details>
<summary><h2>DS-2CD2743G1-IZ - IPC_G1 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.6.821 | Applied to: [DS-2CD2743G1-IZS(2.8-12mm)](https://assets.hikvision.com/prd/public/all/files/202309/Firmware__V5.6.821_230831_S3000525150.zip)(BLACK) | 2023-08-31 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202309/Firmware__V5.6.821_230831_S3000525150.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202401/releasenote%5CNetwork_Camera-V5.6.821_Release_Note-IPC_G1_230831.pdf) |

</details>


<details>
<summary><h2>DS-2CD2745FWD-IZS - IPC_G1 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.6.821 | Applied to: [DS-2CD2745FWD-IZS/2](https://assets.hikvision.com/prd/public/all/files/202309/Firmware__V5.6.821_230831_S3000525150.zip).8-12mm/B/O-STD/BLACK | 2023-08-31 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202309/Firmware__V5.6.821_230831_S3000525150.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202401/releasenote%5CNetwork_Camera-V5.6.821_Release_Note-IPC_G1_230831.pdf) |

</details>


<details>
<summary><h2>DS-2CD2746G1-IZS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.6.0 | Applied to: [DS-2CD2746G1-IZS(2.8-12mm)](https://assets.hikvision.com/prd/public/all/files/18db80e0-2712-4496-8bd3-646f5014a59b.zip) | 2019-05-07 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/18db80e0-2712-4496-8bd3-646f5014a59b.zip) |  |

</details>


<details>
<summary><h2>DS-2CD2746G2-IZS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.820 | Applied to: [DS-2CD2746G2-IZS(2.8-12mm)](https://assets.hikvision.com/prd/public/all/files/202312/Firmware__V5.5.820_231108_S3000539625.zip) | 2023-11-08 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202312/Firmware__V5.5.820_231108_S3000539625.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202408/releasenote%5CNetwork_Camera-V5.5.820_Release_Note-G3.pdf) |

</details>


<details>
<summary><h2>DS-2CD2763G1-IZ - IPC_G1 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.6.821 | Applied to: [DS-2CD2763G1-IZ(2.8-12mm)](https://assets.hikvision.com/prd/public/all/files/202309/Firmware__V5.6.821_230831_S3000525150.zip) | 2023-08-31 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202309/Firmware__V5.6.821_230831_S3000525150.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202401/releasenote%5CNetwork_Camera-V5.6.821_Release_Note-IPC_G1_230831.pdf) |

</details>


<details>
<summary><h2>DS-2CD2765G0-IZS - IPC_G1 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.6.821 | Applied to: [DS-2CD2765G0-IZS(2.8-12mm)](https://assets.hikvision.com/prd/public/all/files/202309/Firmware__V5.6.821_230831_S3000525150.zip) | 2023-08-31 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202309/Firmware__V5.6.821_230831_S3000525150.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202401/releasenote%5CNetwork_Camera-V5.6.821_Release_Note-IPC_G1_230831.pdf) |

</details>


<details>
<summary><h2>DS-2CD2766G3-IPTRZS2UY - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD2766G3-IPTRZS2UY/SL(2.8-12mm)](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691342.zip)O-STD | 2025-12-10 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691342.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD2766G3-IPTRZSY - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD2766G3-IPTRZSY(2.8-12mm)](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691342.zip) | 2025-12-10 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691342.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD2767G3T-LIZSY - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD2767G3T-LIZSY(2.8-12mm)](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691342.zip) | 2025-12-10 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691342.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD2783G1-IZ - IPC_G1 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.6.821 | Applied to: [DS-2CD2783G1-IZ(2.8-12mm)](https://assets.hikvision.com/prd/public/all/files/202309/Firmware__V5.6.821_230831_S3000525150.zip) | 2023-08-31 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202309/Firmware__V5.6.821_230831_S3000525150.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202401/releasenote%5CNetwork_Camera-V5.6.821_Release_Note-IPC_G1_230831.pdf) |

</details>


<details>
<summary><h2>DS-2CD2783G2-IZS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.6 | Applied to: [DS-2CD2783G2-IZS(2.8-12mm)](https://assets.hikvision.com/prd/normal/all/files/202602/Firmware__V5.7.6_260128_S3000701683.zip)(D) | 2026-01-28 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202602/Firmware__V5.7.6_260128_S3000701683.zip) |  |

</details>


<details>
<summary><h2>DS-2CD2783G2-LIZS2U - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.6 | Applied to: [DS-2CD2783G2-LIZS2U(2.8-12mm)](https://assets.hikvision.com/prd/normal/all/files/202602/Firmware__V5.7.6_260128_S3000701683.zip)(T) | 2026-01-28 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202602/Firmware__V5.7.6_260128_S3000701683.zip) |  |

</details>


<details>
<summary><h2>DS-2CD2785G0-IZS - IPC_G1 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.6.821 | Applied to: [DS-2CD2785G0-IZS(2.8-12mm)](https://assets.hikvision.com/prd/public/all/files/202309/Firmware__V5.6.821_230831_S3000525150.zip) | 2023-08-31 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202309/Firmware__V5.6.821_230831_S3000525150.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202401/releasenote%5CNetwork_Camera-V5.6.821_Release_Note-IPC_G1_230831.pdf) |

</details>


<details>
<summary><h2>DS-2CD2786G2-IZS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.820 | Applied to: [DS-2CD2786G2-IZS(2.8-12mm)](https://assets.hikvision.com/prd/public/all/files/202312/Firmware__V5.5.820_231108_S3000539625.zip) | 2023-11-08 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202312/Firmware__V5.5.820_231108_S3000539625.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202408/releasenote%5CNetwork_Camera-V5.5.820_Release_Note-G3.pdf) |

</details>


<details>
<summary><h2>DS-2CD2786G3-IPTRZS2UY - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD2786G3-IPTRZS2UY/SL(2.8-12mm)](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691342.zip)O-STD | 2025-12-10 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691342.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD2786G3-IPTRZSY - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD2786G3-IPTRZSY(2.8-12mm)](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691342.zip) | 2025-12-10 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691342.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD2787G3T-LIZSY - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD2787G3T-LIZSY(2.8-12mm)](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691342.zip) | 2025-12-10 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691342.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD2821G0 - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.800 | Applied to: [DS-2CD2821G0](https://assets.hikvision.com/prd/public/all/files/2b726e56-901f-4e8d-9fd4-e9d67bc8e80a.zip) | 2021-06-28 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/2b726e56-901f-4e8d-9fd4-e9d67bc8e80a.zip) |  |

</details>


<details>
<summary><h2>DS-2CD2935FWD-I - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.4.52 | Applied to: [DS-2CD2935FWD-I(1.16mm)](https://assets.hikvision.com/prd/public/all/files/7d4a69ad-ffac-4b30-a09d-66f19a538df0.zip) | 2020-04-16 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/7d4a69ad-ffac-4b30-a09d-66f19a538df0.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202312/releasenote%5CIPC_V5.4.52_G1__Release_Note--External.pdf) |

</details>


<details>
<summary><h2>DS-2CD2955FWD-I - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.4.52 | Applied to: [DS-2CD2955FWD-IS(1.05mm)](https://assets.hikvision.com/prd/public/all/files/7d4a69ad-ffac-4b30-a09d-66f19a538df0.zip) | 2020-04-16 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/7d4a69ad-ffac-4b30-a09d-66f19a538df0.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202312/releasenote%5CIPC_V5.4.52_G1__Release_Note--External.pdf) |

</details>


<details>
<summary><h2>DS-2CD2955G0-IS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.21 | Applied to: [DS-2CD2955G0-IS(1.05mm)](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.7.21_241211_S3000620660.zip) | 2024-12-11 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.7.21_241211_S3000620660.zip) |  |

</details>


<details>
<summary><h2>DS-2CD2D25G1-D - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.210 | Applied to: [DS-2CD2D25G1-D/NF(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202206/IPCG_E8_EN_STD_5.7.210_220615.zip) | 2022-06-15 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202206/IPCG_E8_EN_STD_5.7.210_220615.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202312/releasenote%5CIPC_V5.7.210_SP_Release_Note--EN.pdf) |

</details>


<details>
<summary><h2>DS-2CD2D45G1 - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.210 | Applied to: [DS-2CD2D45G1/M-D/NF(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202206/IPCG_E8_EN_STD_5.7.210_220615.zip) | 2022-06-15 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202206/IPCG_E8_EN_STD_5.7.210_220615.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202312/releasenote%5CIPC_V5.7.210_SP_Release_Note--EN.pdf) |

</details>


<details>
<summary><h2>DS-2CD2D45G2-U - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.23 | Applied to: [DS-2CD2D45G2-U(2.8mm)](https://assets.hikvision.com/prd/normal/all/files/202508/Firmware__V5.8.23_250716_S3000662537.zip) | 2025-07-16 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202508/Firmware__V5.8.23_250716_S3000662537.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CCovert_Camera_2Dxx_V5.8.23_250716_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD2H123G2-LIZS2UY - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.2 | Applied to: [DS-2CD2H123G2-LIZS2UY(2.8-12mm)](https://assets.hikvision.com/prd/normal/all/files/202511/Firmware__V5.8.2_251103_S3000682542.zip) | 2025-11-03 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202511/Firmware__V5.8.2_251103_S3000682542.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202511/releasenote%5CNetwork_Camera-V5.8.2_251103_Release_Note-IPCE_G9.pdf) |

</details>


<details>
<summary><h2>DS-2CD2H126G3-IZS2UY - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.2 | Applied to: [DS-2CD2H126G3-IZS2UY/SRB(2.8-12)](https://assets.hikvision.com/prd/normal/all/files/202511/Firmware__V5.8.2_251103_S3000682542.zip)eFO-STD | 2025-11-03 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202511/Firmware__V5.8.2_251103_S3000682542.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202511/releasenote%5CNetwork_Camera-V5.8.2_251103_Release_Note-IPCE_G9.pdf) |

</details>


<details>
<summary><h2>DS-2CD2H126G3-IZSY - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.2 | Applied to: [DS-2CD2H126G3-IZSY(2.8-12mm)](https://assets.hikvision.com/prd/normal/all/files/202511/Firmware__V5.8.2_251103_S3000682542.zip)(eF) | 2025-11-03 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202511/Firmware__V5.8.2_251103_S3000682542.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202511/releasenote%5CNetwork_Camera-V5.8.2_251103_Release_Note-IPCE_G9.pdf) |

</details>


<details>
<summary><h2>DS-2CD2H166G3-IZS2UY - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.2 | Applied to: [DS-2CD2H166G3-IZS2UY/SRB(2.8-12)](https://assets.hikvision.com/prd/normal/all/files/202511/Firmware__V5.8.2_251103_S3000682542.zip)eFO-STD | 2025-11-03 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202511/Firmware__V5.8.2_251103_S3000682542.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202511/releasenote%5CNetwork_Camera-V5.8.2_251103_Release_Note-IPCE_G9.pdf) |

</details>


<details>
<summary><h2>DS-2CD2H166G3-IZSY - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.2 | Applied to: [DS-2CD2H166G3-IZSY(2.8-12mm)](https://assets.hikvision.com/prd/normal/all/files/202511/Firmware__V5.8.2_251103_S3000682542.zip)(eF) | 2025-11-03 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202511/Firmware__V5.8.2_251103_S3000682542.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202511/releasenote%5CNetwork_Camera-V5.8.2_251103_Release_Note-IPCE_G9.pdf) |

</details>


<details>
<summary><h2>DS-2CD2H23G1-IZ - IPC_G1 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.6.821 | Applied to: [DS-2CD2H23G1-IZS(2.8-12mm)](https://assets.hikvision.com/prd/public/all/files/202309/Firmware__V5.6.821_230831_S3000525150.zip) | 2023-08-31 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202309/Firmware__V5.6.821_230831_S3000525150.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202401/releasenote%5CNetwork_Camera-V5.6.821_Release_Note-IPC_G1_230831.pdf) |

</details>


<details>
<summary><h2>DS-2CD2H25FHWD-IZS - IPC_G1 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.6.821 | Applied to: [DS-2CD2H25FHWD-IZS(2.8-12mm)](https://assets.hikvision.com/prd/public/all/files/202309/Firmware__V5.6.821_230831_S3000525150.zip) | 2023-08-31 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202309/Firmware__V5.6.821_230831_S3000525150.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202401/releasenote%5CNetwork_Camera-V5.6.821_Release_Note-IPC_G1_230831.pdf) |

</details>


<details>
<summary><h2>DS-2CD2H25FWD-IZS - IPC_G1 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.6.821 | Applied to: [DS-2CD2H25FWD-IZS(2.8-12mm)](https://assets.hikvision.com/prd/public/all/files/202309/Firmware__V5.6.821_230831_S3000525150.zip) | 2023-08-31 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202309/Firmware__V5.6.821_230831_S3000525150.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202401/releasenote%5CNetwork_Camera-V5.6.821_Release_Note-IPC_G1_230831.pdf) |

</details>


<details>
<summary><h2>DS-2CD2H26G2-IZS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.820 | Applied to: [DS-2CD2H26G2-IZS(2.8-12mm)](https://assets.hikvision.com/prd/public/all/files/202312/Firmware__V5.5.820_231108_S3000539625.zip) | 2023-11-08 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202312/Firmware__V5.5.820_231108_S3000539625.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202408/releasenote%5CNetwork_Camera-V5.5.820_Release_Note-G3.pdf) |

</details>


<details>
<summary><h2>DS-2CD2H43G1-IZ - IPC_G1 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.6.821 | Applied to: [DS-2CD2H43G1-IZ(2.8-12mm)](https://assets.hikvision.com/prd/public/all/files/202309/Firmware__V5.6.821_230831_S3000525150.zip) | 2023-08-31 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202309/Firmware__V5.6.821_230831_S3000525150.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202401/releasenote%5CNetwork_Camera-V5.6.821_Release_Note-IPC_G1_230831.pdf) |

</details>


<details>
<summary><h2>DS-2CD2H45FWD-IZS - IPC_G1 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.6.821 | Applied to: [DS-2CD2H45FWD-IZS(2.8-12mm)](https://assets.hikvision.com/prd/public/all/files/202309/Firmware__V5.6.821_230831_S3000525150.zip)(B) | 2023-08-31 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202309/Firmware__V5.6.821_230831_S3000525150.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202401/releasenote%5CNetwork_Camera-V5.6.821_Release_Note-IPC_G1_230831.pdf) |

</details>


<details>
<summary><h2>DS-2CD2H46G2-IZS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.800 | Applied to: [DS-2CD2H46G2-IZS(2.8-12mm)](https://assets.hikvision.com/prd/public/all/files/7ddcc773-b084-4adc-a9e1-08ed4b8252f4.zip) | 2021-10-09 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/7ddcc773-b084-4adc-a9e1-08ed4b8252f4.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/330c4c2c-5730-4877-a942-0be87cea67ca.pdf) |

</details>


<details>
<summary><h2>DS-2CD2H55FWD-IZS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.51 | Applied to: [DS-2CD2H55FWD-IZS(2.8-12mm)](https://assets.hikvision.com/prd/public/all/files/3e919f73-e198-45cf-aa44-a0652b9caf97.zip) | 2018-03-14 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/3e919f73-e198-45cf-aa44-a0652b9caf97.zip) |  |

</details>


<details>
<summary><h2>DS-2CD2H63G1-IZ - IPC_G1 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.6.821 | Applied to: [DS-2CD2H63G1-IZS(2.8-12mm)](https://assets.hikvision.com/prd/public/all/files/202309/Firmware__V5.6.821_230831_S3000525150.zip) | 2023-08-31 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202309/Firmware__V5.6.821_230831_S3000525150.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202401/releasenote%5CNetwork_Camera-V5.6.821_Release_Note-IPC_G1_230831.pdf) |

</details>


<details>
<summary><h2>DS-2CD2H67G3-LIZS2UY - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD2H67G3-LIZS2UY/SL(2.8-12mm)](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691342.zip) | 2025-12-10 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691342.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD2H67G3-LIZSY - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD2H67G3-LIZSY(2.8-12mm)](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691342.zip) | 2025-12-10 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691342.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD2H83G1-IZ - IPC_G1 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.6.821 | Applied to: [DS-2CD2H83G1-IZ(2.8-12mm)](https://assets.hikvision.com/prd/public/all/files/202309/Firmware__V5.6.821_230831_S3000525150.zip) | 2023-08-31 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202309/Firmware__V5.6.821_230831_S3000525150.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202401/releasenote%5CNetwork_Camera-V5.6.821_Release_Note-IPC_G1_230831.pdf) |

</details>


<details>
<summary><h2>DS-2CD2H85FWD-IZS - IPC_G1 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.6.821 | Applied to: [DS-2CD2H85FWD-IZS(2.8-12mm)](https://assets.hikvision.com/prd/public/all/files/202309/Firmware__V5.6.821_230831_S3000525150.zip) | 2023-08-31 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202309/Firmware__V5.6.821_230831_S3000525150.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202312/releasenote%5CNetwork_Camera_V5.6.6_Release_Note_--G1.pdf) |
| 5.6.6 | Applied to: [DS-2CD2H85FWD-IZS(2.8-12mm)](https://assets.hikvision.com/prd/public/all/files/f18aceb7-b896-4c7d-ad2e-8f0d2a91bcc3.zip) | 2021-06-25 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/f18aceb7-b896-4c7d-ad2e-8f0d2a91bcc3.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202312/releasenote%5CNetwork_Camera_V5.6.6_Release_Note_--G1.pdf) |

</details>


<details>
<summary><h2>DS-2CD2H86G2-IZS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.820 | Applied to: [DS-2CD2H86G2-IZS(2.8-12mm)](https://assets.hikvision.com/prd/public/all/files/202312/Firmware__V5.5.820_231108_S3000539625.zip) | 2023-11-08 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202312/Firmware__V5.5.820_231108_S3000539625.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202408/releasenote%5CNetwork_Camera-V5.5.820_Release_Note-G3.pdf) |

</details>


<details>
<summary><h2>DS-2CD2H87G3-LIZS2UY - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD2H87G3-LIZS2UY/SRB(2.8-12mm)](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691342.zip)/O-STD | 2025-12-10 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691342.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD2H87G3-LIZSY - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD2H87G3-LIZSY(2.8-12mm)](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691342.zip) | 2025-12-10 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691342.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD2T123G2-2LI - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.2 | Applied to: [DS-2CD2T123G2-2LI2UY(2.8mm)](https://assets.hikvision.com/prd/normal/all/files/202511/Firmware__V5.8.2_251103_S3000682542.zip) | 2025-11-03 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202511/Firmware__V5.8.2_251103_S3000682542.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202511/releasenote%5CNetwork_Camera-V5.8.2_251103_Release_Note-IPCE_G9.pdf) |

</details>


<details>
<summary><h2>DS-2CD2T123G2-LIS2U - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.2 | Applied to: [DS-2CD2T123G2-LIS2UY/SL(2.8mm)](https://assets.hikvision.com/prd/normal/all/files/202511/Firmware__V5.8.2_251103_S3000682542.zip) | 2025-11-03 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202511/Firmware__V5.8.2_251103_S3000682542.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202511/releasenote%5CNetwork_Camera-V5.8.2_251103_Release_Note-IPCE_G9.pdf) |

</details>


<details>
<summary><h2>DS-2CD2T126G3-2I - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.2 | Applied to: [DS-2CD2T126G3-2IY(2.8mm)](https://assets.hikvision.com/prd/normal/all/files/202511/Firmware__V5.8.2_251103_S3000682542.zip)(eF) | 2025-11-03 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202511/Firmware__V5.8.2_251103_S3000682542.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202511/releasenote%5CNetwork_Camera-V5.8.2_251103_Release_Note-IPCE_G9.pdf) |

</details>


<details>
<summary><h2>DS-2CD2T126G3-IS2UY - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.2 | Applied to: [DS-2CD2T126G3-IS2UY/SRB(2.8mm)](https://assets.hikvision.com/prd/normal/all/files/202511/Firmware__V5.8.2_251103_S3000682542.zip)(eF)/O-STD | 2025-11-03 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202511/Firmware__V5.8.2_251103_S3000682542.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202511/releasenote%5CNetwork_Camera-V5.8.2_251103_Release_Note-IPCE_G9.pdf) |

</details>


<details>
<summary><h2>DS-2CD2T166G3-2I - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.2 | Applied to: [DS-2CD2T166G3-2IY(2.8mm)](https://assets.hikvision.com/prd/normal/all/files/202511/Firmware__V5.8.2_251103_S3000682542.zip)(eF) | 2025-11-03 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202511/Firmware__V5.8.2_251103_S3000682542.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202511/releasenote%5CNetwork_Camera-V5.8.2_251103_Release_Note-IPCE_G9.pdf) |

</details>


<details>
<summary><h2>DS-2CD2T166G3-IS2UY - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.2 | Applied to: [DS-2CD2T166G3-IS2UY/SRB(2.8mm)](https://assets.hikvision.com/prd/normal/all/files/202511/Firmware__V5.8.2_251103_S3000682542.zip)(eF)/O-STD | 2025-11-03 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202511/Firmware__V5.8.2_251103_S3000682542.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202511/releasenote%5CNetwork_Camera-V5.8.2_251103_Release_Note-IPCE_G9.pdf) |

</details>


<details>
<summary><h2>DS-2CD2T21G0-I - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.800 | Applied to: [DS-2CD2T21G0-IS(4mm)](https://assets.hikvision.com/prd/public/all/files/2b726e56-901f-4e8d-9fd4-e9d67bc8e80a.zip) | 2021-06-28 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/2b726e56-901f-4e8d-9fd4-e9d67bc8e80a.zip) |  |

</details>


<details>
<summary><h2>DS-2CD2T23G0-I5 - IPC_G1 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.6.821 | Applied to: [DS-2CD2T23G0-I5(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202309/Firmware__V5.6.821_230831_S3000525150.zip) | 2023-08-31 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202309/Firmware__V5.6.821_230831_S3000525150.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202401/releasenote%5CNetwork_Camera-V5.6.821_Release_Note-IPC_G1_230831.pdf) |

</details>


<details>
<summary><h2>DS-2CD2T23G2-2I - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.0 | Applied to: [DS-2CD2T23G2-2I(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202411/Firmware__V5.7.0_241023_S3000609022.zip)(D) | 2024-10-23 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202411/Firmware__V5.7.0_241023_S3000609022.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202507/releasenote%5CNetwork_Camera-V5.7.0_SP6_Release_Note-G6_I.pdf) |
| 5.7.18 | Applied to: [DS-2CD2T23G2-2I(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202409/Firmware__V5.7.18_240826_S3000597013.zip)(D) | 2024-08-26 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202409/Firmware__V5.7.18_240826_S3000597013.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202507/releasenote%5CNetwork_Camera-V5.7.0_SP6_Release_Note-G6_I.pdf) |

</details>


<details>
<summary><h2>DS-2CD2T25FHWD-I5 - IPC_G1 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.6.821 | Applied to: [DS-2CD2T25FHWD-I8(4mm)](https://assets.hikvision.com/prd/public/all/files/202309/Firmware__V5.6.821_230831_S3000525150.zip) | 2023-08-31 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202309/Firmware__V5.6.821_230831_S3000525150.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202401/releasenote%5CNetwork_Camera-V5.6.821_Release_Note-IPC_G1_230831.pdf) |

</details>


<details>
<summary><h2>DS-2CD2T25FWD-I5 - IPC_G1 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.6.821 | Applied to: [DS-2CD2T25FWD-I8(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202309/Firmware__V5.6.821_230831_S3000525150.zip) | 2023-08-31 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202309/Firmware__V5.6.821_230831_S3000525150.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202401/releasenote%5CNetwork_Camera-V5.6.821_Release_Note-IPC_G1_230831.pdf) |

</details>


<details>
<summary><h2>DS-2CD2T26G1-2I - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.6.0 | Applied to: [DS-2CD2T26G1-4I(2.8mm)](https://assets.hikvision.com/prd/public/all/files/18db80e0-2712-4496-8bd3-646f5014a59b.zip) | 2019-05-07 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/18db80e0-2712-4496-8bd3-646f5014a59b.zip) |  |

</details>


<details>
<summary><h2>DS-2CD2T26G1-4I - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.6.0 | Applied to: [DS-2CD2T26G1-4I/SL(2.8mm)](https://assets.hikvision.com/prd/public/all/files/18db80e0-2712-4496-8bd3-646f5014a59b.zip) | 2019-05-07 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/18db80e0-2712-4496-8bd3-646f5014a59b.zip) |  |

</details>


<details>
<summary><h2>DS-2CD2T26G2-2I - IPC_G0 (3 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.0 | Applied to: [DS-2CD2T26G2-4I(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202411/Firmware__V5.7.0_241023_S3000609022.zip) | 2024-10-23 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202411/Firmware__V5.7.0_241023_S3000609022.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202408/releasenote%5CNetwork_Camera-V5.5.820_Release_Note-G3.pdf) |
| 5.5.820 | Applied to: [DS-2CD2T26G2-4I(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202312/Firmware__V5.5.820_231108_S3000539625.zip) | 2023-11-08 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202312/Firmware__V5.5.820_231108_S3000539625.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202408/releasenote%5CNetwork_Camera-V5.5.820_Release_Note-G3.pdf) |
| 5.5.800 | Applied to: [DS-2CD2T26G2-4I(2.8mm)](https://assets.hikvision.com/prd/public/all/files/7ddcc773-b084-4adc-a9e1-08ed4b8252f4.zip) | 2021-10-09 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/7ddcc773-b084-4adc-a9e1-08ed4b8252f4.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202408/releasenote%5CNetwork_Camera-V5.5.820_Release_Note-G3.pdf) |

</details>


<details>
<summary><h2>DS-2CD2T26G2-ISU - IPC_G0 (3 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.0 | Applied to: [DS-2CD2T26G2-ISU/SL(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202411/Firmware__V5.7.0_241023_S3000609022.zip) | 2024-10-23 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202411/Firmware__V5.7.0_241023_S3000609022.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/330c4c2c-5730-4877-a942-0be87cea67ca.pdf) |
| 5.5.820 | Applied to: [DS-2CD2T26G2-ISU/SL(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202312/Firmware__V5.5.820_231108_S3000539625.zip) | 2023-11-08 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202312/Firmware__V5.5.820_231108_S3000539625.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/330c4c2c-5730-4877-a942-0be87cea67ca.pdf) |
| 5.5.800 | Applied to: [DS-2CD2T26G2-ISU/SL(2.8mm)](https://assets.hikvision.com/prd/public/all/files/7ddcc773-b084-4adc-a9e1-08ed4b8252f4.zip) | 2021-10-09 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/7ddcc773-b084-4adc-a9e1-08ed4b8252f4.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/330c4c2c-5730-4877-a942-0be87cea67ca.pdf) |

</details>


<details>
<summary><h2>DS-2CD2T27G2-L - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.820 | Applied to: [DS-2CD2T27G2-L(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202312/Firmware__V5.5.820_231108_S3000539625.zip) | 2023-11-08 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202312/Firmware__V5.5.820_231108_S3000539625.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202408/releasenote%5CNetwork_Camera-V5.5.820_Release_Note-G3.pdf) |
| 5.5.800 | Applied to: [DS-2CD2T27G2-L(2.8mm)](https://assets.hikvision.com/prd/public/all/files/7ddcc773-b084-4adc-a9e1-08ed4b8252f4.zip) | 2021-10-09 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/7ddcc773-b084-4adc-a9e1-08ed4b8252f4.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202408/releasenote%5CNetwork_Camera-V5.5.820_Release_Note-G3.pdf) |

</details>


<details>
<summary><h2>DS-2CD2T43G0-I5 - IPC_G1 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.6.821 | Applied to: [DS-2CD2T43G0-I5(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202309/Firmware__V5.6.821_230831_S3000525150.zip) | 2023-08-31 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202309/Firmware__V5.6.821_230831_S3000525150.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202401/releasenote%5CNetwork_Camera-V5.6.821_Release_Note-IPC_G1_230831.pdf) |

</details>


<details>
<summary><h2>DS-2CD2T43G2P-LISU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.11 | Applied to: [DS-2CD2T43G2P-LISU/SL(180°)](https://assets.hikvision.com/prd/normal/all/files/202511/Firmware__V5.8.11_251029_S3000683386.zip) | 2025-10-29 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202511/Firmware__V5.8.11_251029_S3000683386.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.8.11_SP1_251029_Release_Note-IPCE_P_E11.pdf) |

</details>


<details>
<summary><h2>DS-2CD2T45FWD-I5 - IPC_G1 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.6.821 | Applied to: [DS-2CD2T45FWD-I8(4mm)](https://assets.hikvision.com/prd/public/all/files/202309/Firmware__V5.6.821_230831_S3000525150.zip)(BLACK) | 2023-08-31 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202309/Firmware__V5.6.821_230831_S3000525150.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202401/releasenote%5CNetwork_Camera-V5.6.821_Release_Note-IPC_G1_230831.pdf) |

</details>


<details>
<summary><h2>DS-2CD2T45G0P-I - IPC_G1 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.6.821 | Applied to: [DS-2CD2T45G0P-I(1.68mm)](https://assets.hikvision.com/prd/public/all/files/202309/Firmware__V5.6.821_230831_S3000525150.zip) | 2023-08-31 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202309/Firmware__V5.6.821_230831_S3000525150.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202401/releasenote%5CNetwork_Camera-V5.6.821_Release_Note-IPC_G1_230831.pdf) |

</details>


<details>
<summary><h2>DS-2CD2T46G1-4I - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.6.0 | Applied to: [DS-2CD2T46G1-4I/SL(2.8mm)](https://assets.hikvision.com/prd/public/all/files/18db80e0-2712-4496-8bd3-646f5014a59b.zip) | 2019-05-07 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/18db80e0-2712-4496-8bd3-646f5014a59b.zip) |  |

</details>


<details>
<summary><h2>DS-2CD2T46G2-2I - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.820 | Applied to: [DS-2CD2T46G2-2I(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202312/Firmware__V5.5.820_231108_S3000539625.zip) | 2023-11-08 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202312/Firmware__V5.5.820_231108_S3000539625.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/330c4c2c-5730-4877-a942-0be87cea67ca.pdf) |
| 5.5.800 | Applied to: [DS-2CD2T46G2-2I(2.8mm)](https://assets.hikvision.com/prd/public/all/files/7ddcc773-b084-4adc-a9e1-08ed4b8252f4.zip) | 2021-10-09 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/7ddcc773-b084-4adc-a9e1-08ed4b8252f4.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/330c4c2c-5730-4877-a942-0be87cea67ca.pdf) |

</details>


<details>
<summary><h2>DS-2CD2T46G2-ISU - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.820 | Applied to: [DS-2CD2T46G2-ISU/SL(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202312/Firmware__V5.5.820_231108_S3000539625.zip) | 2023-11-08 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202312/Firmware__V5.5.820_231108_S3000539625.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/330c4c2c-5730-4877-a942-0be87cea67ca.pdf) |
| 5.5.800 | Applied to: [DS-2CD2T46G2-ISU/SL(2.8mm)](https://assets.hikvision.com/prd/public/all/files/7ddcc773-b084-4adc-a9e1-08ed4b8252f4.zip) | 2021-10-09 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/7ddcc773-b084-4adc-a9e1-08ed4b8252f4.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/330c4c2c-5730-4877-a942-0be87cea67ca.pdf) |

</details>


<details>
<summary><h2>DS-2CD2T46G2P-ISU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.20 | Applied to: [DS-2CD2T46G2P-ISU/SL(2.8mm)](https://assets.hikvision.com/prd/normal/all/files/202512/Firmware__V5.7.20_251125_S3000690065.zip)(C) | 2025-11-25 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202512/Firmware__V5.7.20_251125_S3000690065.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.20_251125_Release_Note-IPCE_P_G5.pdf) |

</details>


<details>
<summary><h2>DS-2CD2T47G2-L - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.820 | Applied to: [DS-2CD2T47G2-L(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202312/Firmware__V5.5.820_231108_S3000539625.zip) | 2023-11-08 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202312/Firmware__V5.5.820_231108_S3000539625.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202408/releasenote%5CNetwork_Camera-V5.5.820_Release_Note-G3.pdf) |
| 5.5.800 | Applied to: [DS-2CD2T47G2-L(2.8mm)](https://assets.hikvision.com/prd/public/all/files/7ddcc773-b084-4adc-a9e1-08ed4b8252f4.zip) | 2021-10-09 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/7ddcc773-b084-4adc-a9e1-08ed4b8252f4.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202408/releasenote%5CNetwork_Camera-V5.5.820_Release_Note-G3.pdf) |

</details>


<details>
<summary><h2>DS-2CD2T63G0-I5 - IPC_G1 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.6.821 | Applied to: [DS-2CD2T63G0-I8(4mm)](https://assets.hikvision.com/prd/public/all/files/202309/Firmware__V5.6.821_230831_S3000525150.zip) | 2023-08-31 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202309/Firmware__V5.6.821_230831_S3000525150.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202401/releasenote%5CNetwork_Camera-V5.6.821_Release_Note-IPC_G1_230831.pdf) |

</details>


<details>
<summary><h2>DS-2CD2T63G2P-LISU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.11 | Applied to: [DS-2CD2T63G2P-LISU/SL(180°)](https://assets.hikvision.com/prd/normal/all/files/202511/Firmware__V5.8.11_251029_S3000683386.zip) | 2025-10-29 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202511/Firmware__V5.8.11_251029_S3000683386.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.8.11_SP1_251029_Release_Note-IPCE_P_E11.pdf) |

</details>


<details>
<summary><h2>DS-2CD2T65G1-I5 - IPC_G1 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.6.821 | Applied to: [DS-2CD2T65G1-I5(4mm)](https://assets.hikvision.com/prd/public/all/files/202309/Firmware__V5.6.821_230831_S3000525150.zip)(BLACK) | 2023-08-31 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202309/Firmware__V5.6.821_230831_S3000525150.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202401/releasenote%5CNetwork_Camera-V5.6.821_Release_Note-IPC_G1_230831.pdf) |

</details>


<details>
<summary><h2>DS-2CD2T66G2P-ISU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.20 | Applied to: [DS-2CD2T66G2P-ISU/SL(2.8mm)](https://assets.hikvision.com/prd/normal/all/files/202512/Firmware__V5.7.20_251125_S3000690065.zip)(C) | 2025-11-25 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202512/Firmware__V5.7.20_251125_S3000690065.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.20_251125_Release_Note-IPCE_P_G5.pdf) |

</details>


<details>
<summary><h2>DS-2CD2T67G2P-LSU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.20 | Applied to: [DS-2CD2T67G2P-LSU/SL(2.8mm)](https://assets.hikvision.com/prd/normal/all/files/202512/Firmware__V5.7.20_251125_S3000690065.zip)(C) | 2025-11-25 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202512/Firmware__V5.7.20_251125_S3000690065.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.20_251125_Release_Note-IPCE_P_G5.pdf) |

</details>


<details>
<summary><h2>DS-2CD2T67G3-LIS2UY - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD2T67G3-LIS2UY/SL(2.8mm)](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691342.zip) | 2025-12-10 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691342.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD2T67G3-LIY - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD2T67G3-LIY(2.8mm)](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691342.zip) | 2025-12-10 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691342.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD2T83G0-I5 - IPC_G1 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.6.821 | Applied to: [DS-2CD2T83G0-I5(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202309/Firmware__V5.6.821_230831_S3000525150.zip) | 2023-08-31 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202309/Firmware__V5.6.821_230831_S3000525150.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202401/releasenote%5CNetwork_Camera-V5.6.821_Release_Note-IPC_G1_230831.pdf) |

</details>


<details>
<summary><h2>DS-2CD2T83G2-2I - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.6 | Applied to: [DS-2CD2T83G2-2I(2.8mm)](https://assets.hikvision.com/prd/normal/all/files/202602/Firmware__V5.7.6_260128_S3000701683.zip)(D) | 2026-01-28 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202602/Firmware__V5.7.6_260128_S3000701683.zip) |  |

</details>


<details>
<summary><h2>DS-2CD2T83G2-2LI - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.6 | Applied to: [DS-2CD2T83G2-2LI2U(2.8mm)](https://assets.hikvision.com/prd/normal/all/files/202602/Firmware__V5.7.6_260128_S3000701683.zip)(T) | 2026-01-28 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202602/Firmware__V5.7.6_260128_S3000701683.zip) |  |

</details>


<details>
<summary><h2>DS-2CD2T83G2P-LISU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.11 | Applied to: [DS-2CD2T83G2P-LISU/SL(180°)](https://assets.hikvision.com/prd/normal/all/files/202511/Firmware__V5.8.11_251029_S3000683386.zip) | 2025-10-29 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202511/Firmware__V5.8.11_251029_S3000683386.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.8.11_SP1_251029_Release_Note-IPCE_P_E11.pdf) |

</details>


<details>
<summary><h2>DS-2CD2T85G1-I5 - IPC_G1 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.6.821 | Applied to: [DS-2CD2T85G1-I5(4mm)](https://assets.hikvision.com/prd/public/all/files/202309/Firmware__V5.6.821_230831_S3000525150.zip)(BLACK) | 2023-08-31 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202309/Firmware__V5.6.821_230831_S3000525150.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202401/releasenote%5CNetwork_Camera-V5.6.821_Release_Note-IPC_G1_230831.pdf) |

</details>


<details>
<summary><h2>DS-2CD2T86G2-ISU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.820 | Applied to: [DS-2CD2T86G2-ISU/SL(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202312/Firmware__V5.5.820_231108_S3000539625.zip) | 2023-11-08 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202312/Firmware__V5.5.820_231108_S3000539625.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202408/releasenote%5CNetwork_Camera-V5.5.820_Release_Note-G3.pdf) |

</details>


<details>
<summary><h2>DS-2CD2T87G2P-LSU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.20 | Applied to: [DS-2CD2T87G2P-LSU/SL(4mm)](https://assets.hikvision.com/prd/normal/all/files/202512/Firmware__V5.7.20_251125_S3000690065.zip)(C)/O-STD/BLACK | 2025-11-25 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202512/Firmware__V5.7.20_251125_S3000690065.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.20_251125_Release_Note-IPCE_P_G5.pdf) |

</details>


<details>
<summary><h2>DS-2CD2T87G3-LIS2UY - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD2T87G3-LIS2UY/SL(2.8mm)](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691342.zip)O-STD/BLACK | 2025-12-10 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691342.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD2T87G3-LIY - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD2T87G3-LIY(2.8mm)](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691342.zip) | 2025-12-10 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691342.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD30167G3-LIU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.2 | Applied to: [DS-2CD30167G3-LIUY(2.8mm)](https://assets.hikvision.com/prd/normal/all/files/202511/Firmware__V5.8.2_251103_S3000682562.zip) | 2025-11-03 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202511/Firmware__V5.8.2_251103_S3000682562.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202511/releasenote%5CNetwork_Camera-V5.8.2_251103_Release_Note-IPCE_H_G9.pdf) |

</details>


<details>
<summary><h2>DS-2CD3027G2-LS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.820 | Applied to: [DS-2CD3027G2-LS(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202312/Firmware__V5.5.820_231108_S3000539630.zip) | 2023-11-08 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202312/Firmware__V5.5.820_231108_S3000539630.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202403/releasenote%5CNetwork_Camera-V5.5.820_Release_Note-G3.pdf) |

</details>


<details>
<summary><h2>DS-2CD3046G2-IS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.55 | Applied to: [DS-2CD3046G2-IS(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202411/Firmware__V5.7.55_241108_S3000612871.zip)(H) | 2024-11-08 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202411/Firmware__V5.7.55_241108_S3000612871.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.55_SP3_241108_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD3046G2-IU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.55 | Applied to: [DS-2CD3046G2-IU/SL(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202411/Firmware__V5.7.55_241108_S3000612871.zip)(H) | 2024-11-08 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202411/Firmware__V5.7.55_241108_S3000612871.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.55_SP3_241108_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD3046G2H-LI - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.55 | Applied to: [DS-2CD3046G2H-LI(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202411/Firmware__V5.7.55_241108_S3000612871.zip) | 2024-11-08 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202411/Firmware__V5.7.55_241108_S3000612871.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.55_SP3_241108_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD3046G3-IU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD3046G3-IUY(2.8mm)](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691324.zip) | 2025-12-10 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691324.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD3046G3-LIU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD3046G3-LIU(2.8mm)](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691324.zip)(eF) | 2025-12-10 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691324.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD3047G2-LS - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.820 | Applied to: [DS-2CD3047G2-LS(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202312/Firmware__V5.5.820_231108_S3000539630.zip) | 2023-11-08 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202312/Firmware__V5.5.820_231108_S3000539630.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202403/releasenote%5CNetwork_Camera-V5.5.820_Release_Note-G3.pdf) |
| 5.5.800 | Applied to: [DS-2CD3047G2-LS(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202207/Firmware__V5.5.800_211009_S3000390724.zip) | 2021-10-09 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202207/Firmware__V5.5.800_211009_S3000390724.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202403/releasenote%5CNetwork_Camera-V5.5.820_Release_Note-G3.pdf) |

</details>


<details>
<summary><h2>DS-2CD3047G3-LIU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD3047G3-LIUY(2.8mm)](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691324.zip) | 2025-12-10 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691324.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD3066G2-IS - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.55 | Applied to: [DS-2CD3066G2-IS(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202411/Firmware__V5.7.55_241108_S3000612871.zip)(H) | 2024-11-08 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202411/Firmware__V5.7.55_241108_S3000612871.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.55_SP3_241108_Release_Note.pdf) |
| 5.7.51 | Applied to: [DS-2CD3066G2-IS(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202310/Firmware__V5.7.51_230829_S3000522021.zip)(H) | 2023-08-29 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202310/Firmware__V5.7.51_230829_S3000522021.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.55_SP3_241108_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD3066G2H-LI - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.55 | Applied to: [DS-2CD3066G2H-LIU(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202411/Firmware__V5.7.55_241108_S3000612871.zip)(eF) | 2024-11-08 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202411/Firmware__V5.7.55_241108_S3000612871.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.55_SP3_241108_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD3066G3-IU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD3066G3-IUY(2.8mm)](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691324.zip) | 2025-12-10 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691324.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD3066G3-LIU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD3066G3-LIUY(2.8mm)](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691324.zip)(eF) | 2025-12-10 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691324.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD3067G3-LIU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD3067G3-LIU(2.8mm)](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691324.zip) | 2025-12-10 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691324.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD3086G2H-LI - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.55 | Applied to: [DS-2CD3086G2H-LIU(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202411/Firmware__V5.7.55_241108_S3000612871.zip)(eF) | 2024-11-08 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202411/Firmware__V5.7.55_241108_S3000612871.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.55_SP3_241108_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD3086G3-IU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD3086G3-IUY(4mm)](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691324.zip) | 2025-12-10 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691324.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD3086G3-LIU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD3086G3-LIU(2.8mm)](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691324.zip)(eF) | 2025-12-10 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691324.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD3087G3-LIU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD3087G3-LIU(2.8mm)](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691324.zip) | 2025-12-10 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691324.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD30C7G3-LIU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.2 | Applied to: [DS-2CD30C7G3-LIUY(2.8mm)](https://assets.hikvision.com/prd/normal/all/files/202511/Firmware__V5.8.2_251103_S3000682562.zip)(BLACK) | 2025-11-03 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202511/Firmware__V5.8.2_251103_S3000682562.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202511/releasenote%5CNetwork_Camera-V5.8.2_251103_Release_Note-IPCE_H_G9.pdf) |

</details>


<details>
<summary><h2>DS-2CD3121G2E-LIU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.10 | Applied to: [DS-2CD3121G2E-LIU(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202412/Firmware__V5.8.10_241205_S3000618834.zip) | 2024-12-05 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202412/Firmware__V5.8.10_241205_S3000618834.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202507/releasenote%5CNetwork_Camera-V5.8.10_SP2_Release_Note-E9.pdf) |

</details>


<details>
<summary><h2>DS-2CD3125G0-IMS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.6.820 | Applied to: [DS-2CD3125G0-IMS(4mm)](https://assets.hikvision.com/prd/public/all/files/202301/Firmware__V5.6.820_220519_S3000430633.zip) | 2022-05-19 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202301/Firmware__V5.6.820_220519_S3000430633.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202301/Network%20Camera%20V5.6.820%20Release%20Note%20--G1.pdf) |

</details>


<details>
<summary><h2>DS-2CD3146G2-IMS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.55 | Applied to: [DS-2CD3146G2-IMS(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202411/Firmware__V5.7.55_241108_S3000612871.zip) | 2024-11-08 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202411/Firmware__V5.7.55_241108_S3000612871.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.55_SP3_241108_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD3146G2-IS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.55 | Applied to: [DS-2CD3146G2-IS(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202411/Firmware__V5.7.55_241108_S3000612871.zip)(H) | 2024-11-08 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202411/Firmware__V5.7.55_241108_S3000612871.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.55_SP3_241108_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD3146G2H-LIS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.55 | Applied to: [DS-2CD3146G2H-LIS(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202411/Firmware__V5.7.55_241108_S3000612871.zip) | 2024-11-08 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202411/Firmware__V5.7.55_241108_S3000612871.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.55_SP3_241108_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD3146G3-ISU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD3146G3-ISUY(2.8mm)](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691324.zip) | 2025-12-10 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691324.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD3146G3-LISU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD3146G3-LISUY(2.8mm)](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691324.zip)(eF) | 2025-12-10 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691324.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD3146G3-SU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD3146G3-SU(2mm)](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691324.zip) | 2025-12-10 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691324.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD3147G3-LISU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD3147G3-LISU(2.8mm)](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691324.zip) | 2025-12-10 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691324.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD3166G2-IS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.55 | Applied to: [DS-2CD3166G2-IS(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202411/Firmware__V5.7.55_241108_S3000612871.zip)(H) | 2024-11-08 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202411/Firmware__V5.7.55_241108_S3000612871.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.55_SP3_241108_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD3166G2H-LIS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.55 | Applied to: [DS-2CD3166G2H-LISU(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202411/Firmware__V5.7.55_241108_S3000612871.zip)(eF) | 2024-11-08 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202411/Firmware__V5.7.55_241108_S3000612871.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.55_SP3_241108_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD3166G3-ISU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD3166G3-ISUY(2.8mm)](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691324.zip) | 2025-12-10 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691324.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD3166G3-LISU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD3166G3-LISUY(2.8mm)](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691324.zip)(eF) | 2025-12-10 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691324.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD3167G3-LISU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD3167G3-LISU(2.8mm)](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691324.zip) | 2025-12-10 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691324.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD3185G0-IMS - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.6.6 | Applied to: [DS-2CD3185G0-IMS(2.8mm)](https://assets.hikvision.com/prd/public/all/files/f18aceb7-b896-4c7d-ad2e-8f0d2a91bcc3.zip) | 2021-06-25 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/f18aceb7-b896-4c7d-ad2e-8f0d2a91bcc3.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202312/releasenote%5C%E3%80%90Release_Note%E3%80%91Mobile_IPC_V5.6.2_190701.pdf) |
| 5.6.2 | Applied to: [DS-2CD3185G0-IMS(2.8mm)](https://assets.hikvision.com/prd/public/all/files/f88f5389-fd05-44ea-9adc-874910511d97.zip) | 2019-07-01 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/f88f5389-fd05-44ea-9adc-874910511d97.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202312/releasenote%5C%E3%80%90Release_Note%E3%80%91Mobile_IPC_V5.6.2_190701.pdf) |

</details>


<details>
<summary><h2>DS-2CD3186G2-IMS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.55 | Applied to: [DS-2CD3186G2-IMS(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202411/Firmware__V5.7.55_241108_S3000612871.zip) | 2024-11-08 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202411/Firmware__V5.7.55_241108_S3000612871.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.55_SP3_241108_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD3186G2-IS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.55 | Applied to: [DS-2CD3186G2-IS(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202411/Firmware__V5.7.55_241108_S3000612871.zip)(H) | 2024-11-08 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202411/Firmware__V5.7.55_241108_S3000612871.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.55_SP3_241108_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD3186G3-ISU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD3186G3-ISUY(4mm)](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691324.zip) | 2025-12-10 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691324.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD3186G3-LISU - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD3186G3-LISUY(2.8mm)](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691324.zip)(eF) | 2025-12-10 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691324.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |
| 5.8.11 | Applied to: [DS-2CD3186G3-LISUY(2.8mm)](https://assets.hikvision.com/prd/normal/all/files/202511/Firmware__V5.8.11_251022_S3000680465.zip)(eF) | 2025-10-22 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202511/Firmware__V5.8.11_251022_S3000680465.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD3187G3-LISU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD3187G3-LISU(2.8mm)](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691324.zip) | 2025-12-10 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691324.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD33167G3-LISU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.2 | Applied to: [DS-2CD33167G3-LISUY(2.8mm)](https://assets.hikvision.com/prd/normal/all/files/202511/Firmware__V5.8.2_251103_S3000682562.zip) | 2025-11-03 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202511/Firmware__V5.8.2_251103_S3000682562.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202511/releasenote%5CNetwork_Camera-V5.8.2_251103_Release_Note-IPCE_H_G9.pdf) |

</details>


<details>
<summary><h2>DS-2CD3327G2-LS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.820 | Applied to: [DS-2CD3327G2-LSU(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202312/Firmware__V5.5.820_231108_S3000539630.zip) | 2023-11-08 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202312/Firmware__V5.5.820_231108_S3000539630.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202403/releasenote%5CNetwork_Camera-V5.5.820_Release_Note-G3.pdf) |

</details>


<details>
<summary><h2>DS-2CD3343G2 - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.11 | Applied to: [DS-2CD3343G2/X2-LIZSUY/SL(2.8/4mm)](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.11_251216_S3000692172.zip)O-STD | 2025-12-16 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.11_251216_S3000692172.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.8.11_251216_Release_Note-IPCE_D_H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD3346G2-IS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.55 | Applied to: [DS-2CD3346G2-ISU(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202411/Firmware__V5.7.55_241108_S3000612871.zip)(H) | 2024-11-08 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202411/Firmware__V5.7.55_241108_S3000612871.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.55_SP3_241108_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD3346G2H-LIS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.55 | Applied to: [DS-2CD3346G2H-LIS(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202411/Firmware__V5.7.55_241108_S3000612871.zip) | 2024-11-08 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202411/Firmware__V5.7.55_241108_S3000612871.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.55_SP3_241108_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD3346G2H-LISU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.55 | Applied to: [DS-2CD3346G2H-LISU/SL(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202411/Firmware__V5.7.55_241108_S3000612871.zip) | 2024-11-08 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202411/Firmware__V5.7.55_241108_S3000612871.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.55_SP3_241108_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD3346G3-ISU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD3346G3-ISUY(2.8mm)](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691324.zip) | 2025-12-10 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691324.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD3346G3-LISU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD3346G3-LISUY(2.8mm)](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691324.zip)(eF) | 2025-12-10 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691324.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD3347G2-LS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.820 | Applied to: [DS-2CD3347G2-LSU(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202312/Firmware__V5.5.820_231108_S3000539630.zip) | 2023-11-08 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202312/Firmware__V5.5.820_231108_S3000539630.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202403/releasenote%5CNetwork_Camera-V5.5.820_Release_Note-G3.pdf) |

</details>


<details>
<summary><h2>DS-2CD3347G3-LISU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD3347G3-LISU(2.8mm)](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691324.zip) | 2025-12-10 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691324.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD3366G2H-LIS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.55 | Applied to: [DS-2CD3366G2H-LISU(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202411/Firmware__V5.7.55_241108_S3000612871.zip) | 2024-11-08 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202411/Firmware__V5.7.55_241108_S3000612871.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.55_SP3_241108_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD3366G3-ISU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD3366G3-ISUY(2.8mm)](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691324.zip) | 2025-12-10 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691324.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD3366G3-LISU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD3366G3-LISUY(2.8mm)](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691324.zip)(eF) | 2025-12-10 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691324.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD3367G3-LISU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD3367G3-LISUY(2.8mm)](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691324.zip) | 2025-12-10 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691324.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD3386G2-IS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.55 | Applied to: [DS-2CD3386G2-ISU(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202411/Firmware__V5.7.55_241108_S3000612871.zip)(H) | 2024-11-08 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202411/Firmware__V5.7.55_241108_S3000612871.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.55_SP3_241108_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD3386G2H-LIS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.55 | Applied to: [DS-2CD3386G2H-LISU(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202411/Firmware__V5.7.55_241108_S3000612871.zip) | 2024-11-08 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202411/Firmware__V5.7.55_241108_S3000612871.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.55_SP3_241108_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD3386G3-ISU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD3386G3-ISUY(4mm)](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691324.zip) | 2025-12-10 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691324.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD3386G3-LISU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD3386G3-LISUY(2.8mm)](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691324.zip)(eF) | 2025-12-10 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691324.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD3387G3-LISU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD3387G3-LISU(2.8mm)](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691324.zip) | 2025-12-10 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691324.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD33C7G3-LISU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.2 | Applied to: [DS-2CD33C7G3-LISUY(2.8mm)](https://assets.hikvision.com/prd/normal/all/files/202511/Firmware__V5.8.2_251103_S3000682562.zip) | 2025-11-03 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202511/Firmware__V5.8.2_251103_S3000682562.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202511/releasenote%5CNetwork_Camera-V5.8.2_251103_Release_Note-IPCE_H_G9.pdf) |

</details>


<details>
<summary><h2>DS-2CD3546G2-IS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.55 | Applied to: [DS-2CD3546G2-IS(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202411/Firmware__V5.7.55_241108_S3000612871.zip)(H) | 2024-11-08 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202411/Firmware__V5.7.55_241108_S3000612871.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.55_SP3_241108_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD3546G3-IS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD3546G3-ISY(2.8mm)](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691324.zip) | 2025-12-10 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691324.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD3566G2-IS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.55 | Applied to: [DS-2CD3566G2-IS(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202411/Firmware__V5.7.55_241108_S3000612871.zip)(H) | 2024-11-08 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202411/Firmware__V5.7.55_241108_S3000612871.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.55_SP3_241108_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD3566G3-IS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD3566G3-ISY(2.8mm)](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691324.zip) | 2025-12-10 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691324.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD3586G2-IS - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.19 | Applied to: [DS-2CD3586G2-IS(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202412/Firmware__V5.7.19_241207_S3000618493.zip)(H) | 2024-12-07 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202412/Firmware__V5.7.19_241207_S3000618493.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.55_SP3_241108_Release_Note.pdf) |
| 5.7.55 | Applied to: [DS-2CD3586G2-IS(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202411/Firmware__V5.7.55_241108_S3000612871.zip)(H) | 2024-11-08 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202411/Firmware__V5.7.55_241108_S3000612871.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.55_SP3_241108_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD3586G3-IS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD3586G3-ISY(4mm)](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691324.zip) | 2025-12-10 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691324.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD36167G3-LIZSU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.2 | Applied to: [DS-2CD36167G3-LIZSUY/SL(2.7-13.5mm)](https://assets.hikvision.com/prd/normal/all/files/202511/Firmware__V5.8.2_251103_S3000682562.zip)O-STD | 2025-11-03 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202511/Firmware__V5.8.2_251103_S3000682562.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202511/releasenote%5CNetwork_Camera-V5.8.2_251103_Release_Note-IPCE_H_G9.pdf) |

</details>


<details>
<summary><h2>DS-2CD36167G3T-LIZSU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.2 | Applied to: [DS-2CD36167G3T-LIZSUY(2.7-13.5mm)](https://assets.hikvision.com/prd/normal/all/files/202511/Firmware__V5.8.2_251103_S3000682562.zip) | 2025-11-03 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202511/Firmware__V5.8.2_251103_S3000682562.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202511/releasenote%5CNetwork_Camera-V5.8.2_251103_Release_Note-IPCE_H_G9.pdf) |

</details>


<details>
<summary><h2>DS-2CD3621G2-LIZS - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.10 | Applied to: [DS-2CD3621G2-LIZS(2.7-13.5mm)](https://assets.hikvision.com/prd/normal/all/files/202507/Firmware__V5.8.10_250714_S3000661509.zip) | 2025-07-14 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202507/Firmware__V5.8.10_250714_S3000661509.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202508/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-E10.pdf) |
| 5.7.12 | Applied to: [DS-2CD3621G2-LIZS(2.7-13.5mm)](https://assets.hikvision.com/prd/public/all/files/202307/Firmware__V5.7.12_230614_S3000507847.zip) | 2023-06-14 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202307/Firmware__V5.7.12_230614_S3000507847.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202508/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-E10.pdf) |

</details>


<details>
<summary><h2>DS-2CD3646G2-IZS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.55 | Applied to: [DS-2CD3646G2-IZS(2.7-13.5mm)](https://assets.hikvision.com/prd/public/all/files/202411/Firmware__V5.7.55_241108_S3000612871.zip)(H) | 2024-11-08 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202411/Firmware__V5.7.55_241108_S3000612871.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.55_SP3_241108_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD3646G2HT-LIZS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.55 | Applied to: [DS-2CD3646G2HT-LIZS(2.7-13.5mm)](https://assets.hikvision.com/prd/public/all/files/202411/Firmware__V5.7.55_241108_S3000612871.zip) | 2024-11-08 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202411/Firmware__V5.7.55_241108_S3000612871.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.55_SP3_241108_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD3646G2T-IZS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.55 | Applied to: [DS-2CD3646G2T-IZSY(2.7-13.5mm)](https://assets.hikvision.com/prd/public/all/files/202411/Firmware__V5.7.55_241108_S3000612871.zip)(H) | 2024-11-08 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202411/Firmware__V5.7.55_241108_S3000612871.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.55_SP3_241108_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD3646G2T-LIDZSU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.1 | Applied to: [DS-2CD3646G2T-LIDZSU/4G/SL(2.7-13.5)](https://assets.hikvision.com/prd/normal/all/files/202508/Firmware__V5.8.1_250807_S3000666035.zip)OSTD | 2025-08-07 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202508/Firmware__V5.8.1_250807_S3000666035.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202508/releasenote%5CNetwork_Camera-V5.8.1_250807_Release_Note-IPCE_HGL_G5.pdf) |

</details>


<details>
<summary><h2>DS-2CD3646G3-IZSU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD3646G3-IZSUY/SL(2.7-13.5mm)](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691324.zip) | 2025-12-10 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691324.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD3646G3-LIZSU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD3646G3-LIZSUY/SL(27135)](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691324.zip)eFOSTDBLACK | 2025-12-10 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691324.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD3646G3T-IZSU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD3646G3T-IZSUY(2.7-13.5mm)](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691324.zip) | 2025-12-10 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691324.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD3646G3T-LIZSU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD3646G3T-LIZSUY(27135)](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691324.zip)eFO-STD/BLACK | 2025-12-10 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691324.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD3647G3-LIZSU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD3647G3-LIZSUY/SL(27135)](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691324.zip)O-STD/BLACK | 2025-12-10 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691324.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD3647G3T-LIZSU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD3647G3T-LIZSUY(2.7-13.5mm)](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691324.zip) | 2025-12-10 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691324.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD3666G2-IZS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.55 | Applied to: [DS-2CD3666G2-IZS(7-35mm)](https://assets.hikvision.com/prd/public/all/files/202411/Firmware__V5.7.55_241108_S3000612871.zip)(H) | 2024-11-08 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202411/Firmware__V5.7.55_241108_S3000612871.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.55_SP3_241108_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD3666G2HT-LIZS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.55 | Applied to: [DS-2CD3666G2HT-LIZSY(2.7-13.5mm)](https://assets.hikvision.com/prd/public/all/files/202411/Firmware__V5.7.55_241108_S3000612871.zip) | 2024-11-08 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202411/Firmware__V5.7.55_241108_S3000612871.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.55_SP3_241108_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD3666G2T-IZS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.55 | Applied to: [DS-2CD3666G2T-IZSY(2.7-13.5mm)](https://assets.hikvision.com/prd/public/all/files/202411/Firmware__V5.7.55_241108_S3000612871.zip)(H) | 2024-11-08 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202411/Firmware__V5.7.55_241108_S3000612871.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.55_SP3_241108_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD3666G3-IZSU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD3666G3-IZSUY/SL(2.7-13.5mm)](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691324.zip) | 2025-12-10 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691324.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD3666G3-LIZSU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD3666G3-LIZSUY/SL(2.7-13.5mm)](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691324.zip)eFOSTD | 2025-12-10 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691324.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD3666G3T-IZSU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD3666G3T-IZSUY(2.7-13.5mm)](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691324.zip) | 2025-12-10 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691324.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD3666G3T-LIZSU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD3666G3T-LIZSUY(2.7-13.5mm)](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691324.zip)eF/O-STD | 2025-12-10 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691324.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD3667G3-LIZSU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD3667G3-LIZSUY/SL(2.7-13.5mm)](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691324.zip)O-STD | 2025-12-10 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691324.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD3667G3T-LIZSU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD3667G3T-LIZSUY(2.7-13.5mm)](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691324.zip) | 2025-12-10 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691324.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD3686G2-IZS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.55 | Applied to: [DS-2CD3686G2-IZS(2.7-13.5mm)](https://assets.hikvision.com/prd/public/all/files/202411/Firmware__V5.7.55_241108_S3000612871.zip)(H) | 2024-11-08 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202411/Firmware__V5.7.55_241108_S3000612871.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.55_SP3_241108_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD3686G2HT-LIZS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.55 | Applied to: [DS-2CD3686G2HT-LIZS(2.7-13.5mm)](https://assets.hikvision.com/prd/public/all/files/202411/Firmware__V5.7.55_241108_S3000612871.zip) | 2024-11-08 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202411/Firmware__V5.7.55_241108_S3000612871.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.55_SP3_241108_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD3686G2T-IZS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.55 | Applied to: [DS-2CD3686G2T-IZS(2.7-13.5mm)](https://assets.hikvision.com/prd/public/all/files/202411/Firmware__V5.7.55_241108_S3000612871.zip)(H) | 2024-11-08 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202411/Firmware__V5.7.55_241108_S3000612871.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.55_SP3_241108_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD3686G2T-LIDZSU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.1 | Applied to: [DS-2CD3686G2T-LIDZSU/4G/SL(2.7-13.5)](https://assets.hikvision.com/prd/normal/all/files/202508/Firmware__V5.8.1_250807_S3000666035.zip)OSTD | 2025-08-07 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202508/Firmware__V5.8.1_250807_S3000666035.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202508/releasenote%5CNetwork_Camera-V5.8.1_250807_Release_Note-IPCE_HGL_G5.pdf) |

</details>


<details>
<summary><h2>DS-2CD3686G3-IZSU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD3686G3-IZSUY/SL(2.7-13.5mm)](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691324.zip) | 2025-12-10 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691324.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD3686G3-LIZSU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD3686G3-LIZSUY/SL(27135)](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691324.zip)eFOSTDBLACK | 2025-12-10 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691324.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD3686G3T-IZSU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD3686G3T-IZSUY(2.7-13.5mm)](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691324.zip) | 2025-12-10 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691324.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD3686G3T-LIZSU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD3686G3T-LIZSUY(27135)](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691324.zip)eFO-STD/BLACK | 2025-12-10 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691324.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD3687G3-LIZSU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD3687G3-LIZSUY/SL(27135)](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691324.zip)O-STD/BLACK | 2025-12-10 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691324.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD3687G3T-LIZSU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD3687G3T-LIZSUY(2.7-13.5mm)](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691324.zip) | 2025-12-10 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691324.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD36C7G3-LIZSU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.2 | Applied to: [DS-2CD36C7G3-LIZSUY/SL(2.7-13.5mm)](https://assets.hikvision.com/prd/normal/all/files/202511/Firmware__V5.8.2_251103_S3000682562.zip)/O-STD | 2025-11-03 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202511/Firmware__V5.8.2_251103_S3000682562.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202511/releasenote%5CNetwork_Camera-V5.8.2_251103_Release_Note-IPCE_H_G9.pdf) |

</details>


<details>
<summary><h2>DS-2CD36C7G3T-LIZSU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.2 | Applied to: [DS-2CD36C7G3T-LIZSU(2.7-13.5mm)](https://assets.hikvision.com/prd/normal/all/files/202511/Firmware__V5.8.2_251103_S3000682562.zip) | 2025-11-03 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202511/Firmware__V5.8.2_251103_S3000682562.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202511/releasenote%5CNetwork_Camera-V5.8.2_251103_Release_Note-IPCE_H_G9.pdf) |

</details>


<details>
<summary><h2>DS-2CD37167G3T-LIZSU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.2 | Applied to: [DS-2CD37167G3T-LIZSUY(2.7-13.5mm)](https://assets.hikvision.com/prd/normal/all/files/202511/Firmware__V5.8.2_251103_S3000682562.zip) | 2025-11-03 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202511/Firmware__V5.8.2_251103_S3000682562.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202511/releasenote%5CNetwork_Camera-V5.8.2_251103_Release_Note-IPCE_H_G9.pdf) |

</details>


<details>
<summary><h2>DS-2CD3721G2-LIZS - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.10 | Applied to: [DS-2CD3721G2-LIZS(2.7-13.5mm)](https://assets.hikvision.com/prd/normal/all/files/202507/Firmware__V5.8.10_250714_S3000661509.zip) | 2025-07-14 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202507/Firmware__V5.8.10_250714_S3000661509.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202508/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-E10.pdf) |
| 5.7.12 | Applied to: [DS-2CD3721G2-LIZS(2.7-13.5mm)](https://assets.hikvision.com/prd/public/all/files/202307/Firmware__V5.7.12_230614_S3000507847.zip) | 2023-06-14 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202307/Firmware__V5.7.12_230614_S3000507847.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202508/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-E10.pdf) |

</details>


<details>
<summary><h2>DS-2CD3746G2-IZS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.55 | Applied to: [DS-2CD3746G2-IZS(7-35mm)](https://assets.hikvision.com/prd/public/all/files/202411/Firmware__V5.7.55_241108_S3000612871.zip)(H) | 2024-11-08 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202411/Firmware__V5.7.55_241108_S3000612871.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.55_SP3_241108_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD3746G2H-LIZSU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.55 | Applied to: [DS-2CD3746G2H-LIZSU/SLPTRZ(27135)](https://assets.hikvision.com/prd/public/all/files/202502/Firmware__V5.7.55_250211_S3000630839.zip)eFO-STD | 2025-02-11 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202502/Firmware__V5.7.55_250211_S3000630839.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202503/releasenote%5CNetwork_Camera-V5.7.55_SP4_Release_Note-G5_P.pdf) |

</details>


<details>
<summary><h2>DS-2CD3746G2HT-LIZS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.55 | Applied to: [DS-2CD3746G2HT-LIZSU(2.7-13.5mm)](https://assets.hikvision.com/prd/public/all/files/202411/Firmware__V5.7.55_241108_S3000612871.zip) | 2024-11-08 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202411/Firmware__V5.7.55_241108_S3000612871.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.55_SP3_241108_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD3746G2HT-LIZSU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.55 | Applied to: [DS-2CD3746G2HT-LIZSU(PTRZ)](https://assets.hikvision.com/prd/public/all/files/202502/Firmware__V5.7.55_250211_S3000630839.zip)(27135)eFO-STD | 2025-02-11 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202502/Firmware__V5.7.55_250211_S3000630839.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202503/releasenote%5CNetwork_Camera-V5.7.55_SP4_Release_Note-G5_P.pdf) |

</details>


<details>
<summary><h2>DS-2CD3746G2T-IZS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.55 | Applied to: [DS-2CD3746G2T-IZS(2.7-13.5mm)](https://assets.hikvision.com/prd/public/all/files/202411/Firmware__V5.7.55_241108_S3000612871.zip)(H) | 2024-11-08 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202411/Firmware__V5.7.55_241108_S3000612871.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.55_SP3_241108_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD3746G3T-IZSU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD3746G3T-IZSUY(2.7-13.5)](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691324.zip)O-STDBLACK | 2025-12-10 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691324.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD3746G3T-LIZSU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD3746G3T-LIZSUY(27135)](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691324.zip)eFO-STD/BLACK | 2025-12-10 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691324.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD3747G3-LIZSUY - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD3747G3-LIZSUY/SL(PTRZ)](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691324.zip)(27135)O-STD | 2025-12-10 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691324.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD3747G3T-LIZSU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD3747G3T-LIZSU(2.7-13.5mm)](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691324.zip) | 2025-12-10 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691324.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD3747G3T-LIZSUY - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD3747G3T-LIZSUY/SL(PTRZ)](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691324.zip)(27135)OSTD | 2025-12-10 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691324.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD3766G2-IZS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.55 | Applied to: [DS-2CD3766G2-IZS(7-35mm)](https://assets.hikvision.com/prd/public/all/files/202411/Firmware__V5.7.55_241108_S3000612871.zip)(H) | 2024-11-08 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202411/Firmware__V5.7.55_241108_S3000612871.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.55_SP3_241108_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD3766G2H-LIZSU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.55 | Applied to: [DS-2CD3766G2H-LIZSU(PTRZ)](https://assets.hikvision.com/prd/public/all/files/202502/Firmware__V5.7.55_250211_S3000630839.zip)(27135)eF/O-STD | 2025-02-11 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202502/Firmware__V5.7.55_250211_S3000630839.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202503/releasenote%5CNetwork_Camera-V5.7.55_SP4_Release_Note-G5_P.pdf) |

</details>


<details>
<summary><h2>DS-2CD3766G2HT-LIZS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.55 | Applied to: [DS-2CD3766G2HT-LIZSU(2.7-13.5mm)](https://assets.hikvision.com/prd/public/all/files/202411/Firmware__V5.7.55_241108_S3000612871.zip) | 2024-11-08 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202411/Firmware__V5.7.55_241108_S3000612871.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.55_SP3_241108_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD3766G2HT-LIZSU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.55 | Applied to: [DS-2CD3766G2HT-LIZSU(PTRZ)](https://assets.hikvision.com/prd/public/all/files/202502/Firmware__V5.7.55_250211_S3000630839.zip)(27135)eFO-STD | 2025-02-11 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202502/Firmware__V5.7.55_250211_S3000630839.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202503/releasenote%5CNetwork_Camera-V5.7.55_SP4_Release_Note-G5_P.pdf) |

</details>


<details>
<summary><h2>DS-2CD3766G2T-IZS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.55 | Applied to: [DS-2CD3766G2T-IZS(2.7-13.5mm)](https://assets.hikvision.com/prd/public/all/files/202411/Firmware__V5.7.55_241108_S3000612871.zip)(H) | 2024-11-08 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202411/Firmware__V5.7.55_241108_S3000612871.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.55_SP3_241108_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD3766G3T-IZSU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD3766G3T-IZSUY(2.7-13.5mm)](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691324.zip) | 2025-12-10 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691324.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD3766G3T-LIZSU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD3766G3T-LIZSU(2.7-13.5mm)](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691324.zip)(eF)O-STD | 2025-12-10 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691324.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD3767G3-LIZSUY - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD3767G3-LIZSUY/SL(PTRZ)](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691324.zip)(27135)O-STD | 2025-12-10 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691324.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD3767G3T-LIZSU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD3767G3T-LIZSU(2.7-13.5mm)](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691324.zip) | 2025-12-10 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691324.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD3767G3T-LIZSUY - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD3767G3T-LIZSUY/SL(PTRZ)](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691324.zip)(27135)OSTD | 2025-12-10 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691324.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD3786G2-IZS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.55 | Applied to: [DS-2CD3786G2-IZS(2.7-13.5mm)](https://assets.hikvision.com/prd/public/all/files/202411/Firmware__V5.7.55_241108_S3000612871.zip)(H) | 2024-11-08 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202411/Firmware__V5.7.55_241108_S3000612871.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.55_SP3_241108_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD3786G2H-LIZSU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.55 | Applied to: [DS-2CD3786G2H-LIZSU(PTRZ)](https://assets.hikvision.com/prd/public/all/files/202502/Firmware__V5.7.55_250211_S3000630839.zip)(27135)eF/O-STD | 2025-02-11 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202502/Firmware__V5.7.55_250211_S3000630839.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202503/releasenote%5CNetwork_Camera-V5.7.55_SP4_Release_Note-G5_P.pdf) |

</details>


<details>
<summary><h2>DS-2CD3786G2HT-LIZS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.55 | Applied to: [DS-2CD3786G2HT-LIZSU(2.7-13.5mm)](https://assets.hikvision.com/prd/public/all/files/202411/Firmware__V5.7.55_241108_S3000612871.zip) | 2024-11-08 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202411/Firmware__V5.7.55_241108_S3000612871.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.55_SP3_241108_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD3786G2HT-LIZSU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.55 | Applied to: [DS-2CD3786G2HT-LIZSU(PTRZ)](https://assets.hikvision.com/prd/public/all/files/202502/Firmware__V5.7.55_250211_S3000630839.zip)(27135)eFO-STD | 2025-02-11 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202502/Firmware__V5.7.55_250211_S3000630839.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202503/releasenote%5CNetwork_Camera-V5.7.55_SP4_Release_Note-G5_P.pdf) |

</details>


<details>
<summary><h2>DS-2CD3786G2T-IZS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.55 | Applied to: [DS-2CD3786G2T-IZS(2.7-13.5mm)](https://assets.hikvision.com/prd/public/all/files/202411/Firmware__V5.7.55_241108_S3000612871.zip)(H) | 2024-11-08 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202411/Firmware__V5.7.55_241108_S3000612871.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.55_SP3_241108_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD3786G3T-IZSU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD3786G3T-IZSUY(7-35mm)](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691324.zip) | 2025-12-10 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691324.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD3786G3T-LIZSU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD3786G3T-LIZSUY(2.7-13.5mm)](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691324.zip)eF/O-STD | 2025-12-10 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691324.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD3787G3-LIZSUY - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD3787G3-LIZSUY/SL(PTRZ)](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691324.zip)(27135)O-STD | 2025-12-10 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691324.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD3787G3T-LIZSU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD3787G3T-LIZSUY(2.7-13.5mm)](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691324.zip) | 2025-12-10 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691324.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD3787G3T-LIZSUY - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD3787G3T-LIZSUY/SL(PTRZ)](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691324.zip)(27135)OSTD | 2025-12-10 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691324.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD37C7G3T-LIZSU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.2 | Applied to: [DS-2CD37C7G3T-LIZSUY(2.7-13.5mm)](https://assets.hikvision.com/prd/normal/all/files/202511/Firmware__V5.8.2_251103_S3000682562.zip) | 2025-11-03 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202511/Firmware__V5.8.2_251103_S3000682562.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202511/releasenote%5CNetwork_Camera-V5.8.2_251103_Release_Note-IPCE_H_G9.pdf) |

</details>


<details>
<summary><h2>DS-2CD3843G0-AP - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2CD3843G0-AP](https://assets.hikvision.com/prd/public/all/files/202505/Firmware__V5.7.23_241211_S3000620665.zip) | 2024-12-11 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202505/Firmware__V5.7.23_241211_S3000620665.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202507/releasenote%5CNetwork_Camera-V5.7.23_SP2_Release_Note-E8.pdf) |

</details>


<details>
<summary><h2>DS-2CD3956G2-IS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.40 | Applied to: [DS-2CD3956G2-IS(1.05mm)](https://assets.hikvision.com/prd/public/all/files/202303/Firmware__V5.7.40_230218_S3000482515.zip) | 2023-02-18 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202303/Firmware__V5.7.40_230218_S3000482515.zip) |  |

</details>


<details>
<summary><h2>DS-2CD3A26G2T-IZS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.0 | Applied to: [DS-2CD3A26G2T-IZS(4.7-71mm)](https://assets.hikvision.com/prd/public/all/files/202308/Firmware__V5.7.0_230627_S3000512210.zip) | 2023-06-27 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202308/Firmware__V5.7.0_230627_S3000512210.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202408/releasenote%5CNetwork_Camera-V5.7.0_SP2_Release_Note-IPCE_LZ_H8_230627.pdf) |

</details>


<details>
<summary><h2>DS-2CD3A46G2T-IZHS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.0 | Applied to: [DS-2CD3A46G2T-IZHS(6-60mm)](https://assets.hikvision.com/prd/public/all/files/202411/Firmware__V5.8.0_241103_S3000612874.zip) | 2024-11-03 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202411/Firmware__V5.8.0_241103_S3000612874.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202511/releasenote%5CNetwork_Camera-V5.7.5_SP3_Release_Note-H8.pdf) |

</details>


<details>
<summary><h2>DS-2CD3B26G2T-IZHS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.55 | Applied to: [DS-2CD3B26G2T-IZHS(8-32mm)](https://assets.hikvision.com/prd/public/all/files/202411/Firmware__V5.7.55_241108_S3000612871.zip)(H) | 2024-11-08 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202411/Firmware__V5.7.55_241108_S3000612871.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.55_SP3_241108_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD3B46G2T-IZHS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.55 | Applied to: [DS-2CD3B46G2T-IZHSY(8-32mm)](https://assets.hikvision.com/prd/public/all/files/202411/Firmware__V5.7.55_241108_S3000612871.zip)(H) | 2024-11-08 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202411/Firmware__V5.7.55_241108_S3000612871.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.55_SP3_241108_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD3B86G2T-IZHS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.55 | Applied to: [DS-2CD3B86G2T-IZHSY(8-32mm)](https://assets.hikvision.com/prd/public/all/files/202411/Firmware__V5.7.55_241108_S3000612871.zip)(H) | 2024-11-08 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202411/Firmware__V5.7.55_241108_S3000612871.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.55_SP3_241108_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD3D46G2T-IZHSU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.55 | Applied to: [DS-2CD3D46G2T-IZHSUY(8-32mm)](https://assets.hikvision.com/prd/public/all/files/202411/Firmware__V5.7.55_241108_S3000612871.zip)(H) | 2024-11-08 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202411/Firmware__V5.7.55_241108_S3000612871.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.55_SP3_241108_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD3D86G2T-IZHSU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.55 | Applied to: [DS-2CD3D86G2T-IZHSUY(8-32mm)](https://assets.hikvision.com/prd/public/all/files/202411/Firmware__V5.7.55_241108_S3000612871.zip)(H) | 2024-11-08 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202411/Firmware__V5.7.55_241108_S3000612871.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.55_SP3_241108_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD3H167G3-LIZSU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.2 | Applied to: [DS-2CD3H167G3-LIZSUY(2.7-13.5mm)](https://assets.hikvision.com/prd/normal/all/files/202511/Firmware__V5.8.2_251103_S3000682562.zip) | 2025-11-03 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202511/Firmware__V5.8.2_251103_S3000682562.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202511/releasenote%5CNetwork_Camera-V5.8.2_251103_Release_Note-IPCE_H_G9.pdf) |

</details>


<details>
<summary><h2>DS-2CD3H46G3-LIZSU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD3H46G3-LIZSUY/SL(2.7-13.5)](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691324.zip)eFO-STD | 2025-12-10 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691324.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD3H47G3-LIZSUY - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD3H47G3-LIZSUY/SL(2.7-13.5)](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691324.zip)O-STDBLK | 2025-12-10 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691324.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD3H66G3-LIZSU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD3H66G3-LIZSUY/SL(2.7-13.5)](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691324.zip)eFO-STD | 2025-12-10 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691324.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD3H67G3-LIZSUY - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD3H67G3-LIZSUY/SL(2.7-13.5)](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691324.zip)O-STDBLK | 2025-12-10 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691324.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD3H86G3-LIZSU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD3H86G3-LIZSUY/SL(2.7-13.5)](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691324.zip)eFO-STD | 2025-12-10 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691324.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD3H87G3-LIZSUY - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD3H87G3-LIZSUY/SL(2.7-13.5)](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691324.zip)O-STDBLK | 2025-12-10 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691324.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD3HC7G3-LIZSU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.2 | Applied to: [DS-2CD3HC7G3-LIZSUY(2.7-13.5mm)](https://assets.hikvision.com/prd/normal/all/files/202511/Firmware__V5.8.2_251103_S3000682562.zip) | 2025-11-03 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202511/Firmware__V5.8.2_251103_S3000682562.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202511/releasenote%5CNetwork_Camera-V5.8.2_251103_Release_Note-IPCE_H_G9.pdf) |

</details>


<details>
<summary><h2>DS-2CD3T167G3-LISU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.2 | Applied to: [DS-2CD3T167G3-LISUY(2.8mm)](https://assets.hikvision.com/prd/normal/all/files/202511/Firmware__V5.8.2_251103_S3000682562.zip) | 2025-11-03 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202511/Firmware__V5.8.2_251103_S3000682562.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202511/releasenote%5CNetwork_Camera-V5.8.2_251103_Release_Note-IPCE_H_G9.pdf) |

</details>


<details>
<summary><h2>DS-2CD3T23G1-I - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.52 | Applied to: [DS-2CD3T23G1-I/4G(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202407/1720728513514/Firmware__V5.7.52_240705_S3000585755.zip) | 2024-07-05 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202407/1720728513514/Firmware__V5.7.52_240705_S3000585755.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202408/1722466890133/releasenote%5CG5_6_Series_Solar_5.7.52_Release_Note.pdf) |
| 5.7.51 | Applied to: [DS-2CD3T23G1-I/4G(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202403/Firmware__V5.7.51_240320_S3000563201.zip) | 2024-03-20 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202403/Firmware__V5.7.51_240320_S3000563201.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202408/1722466890133/releasenote%5CG5_6_Series_Solar_5.7.52_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD3T46G2-4IS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.55 | Applied to: [DS-2CD3T46G2-4ISY(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202411/Firmware__V5.7.55_241108_S3000612871.zip)(H) | 2024-11-08 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202411/Firmware__V5.7.55_241108_S3000612871.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.55_SP3_241108_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD3T46G2-ISU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.55 | Applied to: [DS-2CD3T46G2-ISU/SL(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202411/Firmware__V5.7.55_241108_S3000612871.zip)(H) | 2024-11-08 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202411/Firmware__V5.7.55_241108_S3000612871.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.55_SP3_241108_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD3T46G2-LIDSU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.1 | Applied to: [DS-2CD3T46G2-LIDSU/4G/SL(2.8mm)](https://assets.hikvision.com/prd/normal/all/files/202508/Firmware__V5.8.1_250807_S3000666035.zip) | 2025-08-07 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202508/Firmware__V5.8.1_250807_S3000666035.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202508/releasenote%5CNetwork_Camera-V5.8.1_250807_Release_Note-IPCE_HGL_G5.pdf) |

</details>


<details>
<summary><h2>DS-2CD3T46G2H-LIS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.55 | Applied to: [DS-2CD3T46G2H-LIS(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202411/Firmware__V5.7.55_241108_S3000612871.zip) | 2024-11-08 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202411/Firmware__V5.7.55_241108_S3000612871.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.55_SP3_241108_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD3T46G3-2ISU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD3T46G3-4ISUY(2.8mm)](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691324.zip) | 2025-12-10 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691324.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD3T46G3-ISU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD3T46G3-ISUY/SL(2.8mm)](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691324.zip) | 2025-12-10 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691324.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD3T46G3-LISU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD3T46G3-LISUY(2.8mm)](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691324.zip)(eF) | 2025-12-10 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691324.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD3T47G3-LISU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD3T47G3-LISUY(2.8mm)](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691324.zip) | 2025-12-10 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691324.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD3T66G2-4IS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.55 | Applied to: [DS-2CD3T66G2-4IS(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202411/Firmware__V5.7.55_241108_S3000612871.zip)(H) | 2024-11-08 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202411/Firmware__V5.7.55_241108_S3000612871.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.55_SP3_241108_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD3T66G2H-LIS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.55 | Applied to: [DS-2CD3T66G2H-LISU(4mm)](https://assets.hikvision.com/prd/public/all/files/202411/Firmware__V5.7.55_241108_S3000612871.zip) | 2024-11-08 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202411/Firmware__V5.7.55_241108_S3000612871.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.55_SP3_241108_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD3T66G3-2ISU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD3T66G3-4ISUY(2.8mm)](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691324.zip) | 2025-12-10 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691324.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD3T66G3-ISU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD3T66G3-ISUY/SL(2.8mm)](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691324.zip) | 2025-12-10 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691324.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD3T66G3-LISU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD3T66G3-LISUY(2.8mm)](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691324.zip)(eF) | 2025-12-10 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691324.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD3T67G3-LISU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD3T67G3-LISUY(2.8mm)](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691324.zip) | 2025-12-10 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691324.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD3T86G2-4IS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.55 | Applied to: [DS-2CD3T86G2-4ISY(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202411/Firmware__V5.7.55_241108_S3000612871.zip)(H) | 2024-11-08 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202411/Firmware__V5.7.55_241108_S3000612871.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.55_SP3_241108_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD3T86G2-LIDSU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.1 | Applied to: [DS-2CD3T86G2-LIDSU/4G/SL(2.8mm)](https://assets.hikvision.com/prd/normal/all/files/202508/Firmware__V5.8.1_250807_S3000666035.zip) | 2025-08-07 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202508/Firmware__V5.8.1_250807_S3000666035.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202508/releasenote%5CNetwork_Camera-V5.8.1_250807_Release_Note-IPCE_HGL_G5.pdf) |

</details>


<details>
<summary><h2>DS-2CD3T86G2H-LIS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.55 | Applied to: [DS-2CD3T86G2H-LISUY(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202411/Firmware__V5.7.55_241108_S3000612871.zip) | 2024-11-08 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202411/Firmware__V5.7.55_241108_S3000612871.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.55_SP3_241108_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD3T86G3-2ISU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD3T86G3-4ISUY(6mm)](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691324.zip) | 2025-12-10 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691324.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD3T86G3-ISU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD3T86G3-ISUY/SL(6mm)](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691324.zip) | 2025-12-10 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691324.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD3T86G3-LISU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD3T86G3-LISUY(2.8mm)](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691324.zip)(eF) | 2025-12-10 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691324.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD3T87G2P-LSU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.20 | Applied to: [DS-2CD3T87G2P-LSU/SL(4mm)](https://assets.hikvision.com/prd/normal/all/files/202512/Firmware__V5.7.20_251125_S3000690065.zip)(C) | 2025-11-25 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202512/Firmware__V5.7.20_251125_S3000690065.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.7.20_251125_Release_Note-IPCE_P_G5.pdf) |

</details>


<details>
<summary><h2>DS-2CD3T87G3-LISU - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.30 | Applied to: [DS-2CD3T87G3-LISUY(2.8mm)](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691324.zip) | 2025-12-10 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.30_251210_S3000691324.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |
| 5.8.10 | Applied to: [DS-2CD3T87G3-LISUY(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202505/Firmware__V5.8.10_250410_S3000646734.zip) | 2025-04-10 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202505/Firmware__V5.8.10_250410_S3000646734.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-H13.pdf) |

</details>


<details>
<summary><h2>DS-2CD3TC7G3-LISU - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.2 | Applied to: [DS-2CD3TC7G3-LISUY(4mm)](https://assets.hikvision.com/prd/normal/all/files/202511/Firmware__V5.8.2_251103_S3000682562.zip)(BLACK) | 2025-11-03 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202511/Firmware__V5.8.2_251103_S3000682562.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202511/releasenote%5CNetwork_Camera-V5.8.2_251103_Release_Note-IPCE_H_G9.pdf) |

</details>


<details>
<summary><h2>DS-2CD4A24FWD-IZ - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.84 | Applied to: [DS-2CD4A24FWD-IZ(4.7-94mm)](https://assets.hikvision.com/prd/public/all/files/d555f2de-098a-40f4-b417-e8db8a68a42a.zip)(T) | 2019-05-07 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/d555f2de-098a-40f4-b417-e8db8a68a42a.zip) |  |

</details>


<details>
<summary><h2>DS-2CD4A45G0-IZ - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.85 | Applied to: [DS-2CD4A45G0-IZHS(4.7-94mm)](https://assets.hikvision.com/prd/public/all/files/d3b888f5-d9e5-4f4a-8eac-251e4f17471c.zip)(B) | 2019-11-07 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/d3b888f5-d9e5-4f4a-8eac-251e4f17471c.zip) |  |

</details>


<details>
<summary><h2>DS-2CD4B26FWD-IZ - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.91 | Applied to: [DS-2CD4B26FWD-IZS(2.8-12mm)](https://assets.hikvision.com/prd/public/all/files/560e73e2-270f-4f2d-b248-d18f6e89e09e.zip) | 2021-04-29 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/560e73e2-270f-4f2d-b248-d18f6e89e09e.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202312/releasenote%5C%E3%80%90Release_Note%E3%80%91Mobile_IPC_V5.5.91_210429.pdf) |

</details>


<details>
<summary><h2>DS-2CD4B36FWD-IZ - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.91 | Applied to: [DS-2CD4B36FWD-IZS(2.8-12mm)](https://assets.hikvision.com/prd/public/all/files/560e73e2-270f-4f2d-b248-d18f6e89e09e.zip) | 2021-04-29 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/560e73e2-270f-4f2d-b248-d18f6e89e09e.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202312/releasenote%5C%E3%80%90Release_Note%E3%80%91Mobile_IPC_V5.5.91_210429.pdf) |

</details>


<details>
<summary><h2>DS-2CD4B45G0-IZS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.85 | Applied to: [DS-2CD4B45G0-IZS(4.7-65.8mm)](https://assets.hikvision.com/prd/public/all/files/d3b888f5-d9e5-4f4a-8eac-251e4f17471c.zip)(B) | 2019-11-07 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/d3b888f5-d9e5-4f4a-8eac-251e4f17471c.zip) |  |

</details>


<details>
<summary><h2>DS-2CD4D36FWD-IZ - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.91 | Applied to: [DS-2CD4D36FWD-IZS(2.8-12mm)](https://assets.hikvision.com/prd/public/all/files/560e73e2-270f-4f2d-b248-d18f6e89e09e.zip) | 2021-04-29 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/560e73e2-270f-4f2d-b248-d18f6e89e09e.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202312/releasenote%5C%E3%80%90Release_Note%E3%80%91Mobile_IPC_V5.5.91_210429.pdf) |

</details>


<details>
<summary><h2>DS-2CD6045G0 - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.2 | Applied to: [DS-2CD6045G0/SC-IZRS(2.8-12mm)](https://assets.hikvision.com/prd/public/all/files/202503/Firmware__V5.8.2_250222_S3000634155.zip) | 2025-02-22 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202503/Firmware__V5.8.2_250222_S3000634155.zip) |  |

</details>


<details>
<summary><h2>DS-2CD6085G0 - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.2 | Applied to: [DS-2CD6085G0/SC-IZRS(2.8-12mm)](https://assets.hikvision.com/prd/public/all/files/202503/Firmware__V5.8.2_250222_S3000634155.zip) | 2025-02-22 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202503/Firmware__V5.8.2_250222_S3000634155.zip) |  |

</details>


<details>
<summary><h2>DS-2CD6365G1-IVS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.3 | Applied to: [DS-2CD6365G1-IVS(1.16mm)](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.3_260112_S3000699425.zip) | 2026-01-12 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.3_260112_S3000699425.zip) |  |

</details>


<details>
<summary><h2>DS-2CD6365G1-S - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.3 | Applied to: [DS-2CD6365G1-S/RC(1.16mm)](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.3_260112_S3000699425.zip) | 2026-01-12 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.3_260112_S3000699425.zip) |  |

</details>


<details>
<summary><h2>DS-2CD63C5G1-IVS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.3 | Applied to: [DS-2CD63C5G1-IVS(1.29mm)](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.3_260112_S3000699425.zip) | 2026-01-12 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.3_260112_S3000699425.zip) |  |

</details>


<details>
<summary><h2>DS-2CD63C5G1-S - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.3 | Applied to: [DS-2CD63C5G1-S/RC(1.29mm)](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.3_260112_S3000699425.zip) | 2026-01-12 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.3_260112_S3000699425.zip) |  |

</details>


<details>
<summary><h2>DS-2CD6425G1-XX - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.210 | Applied to: [DS-2CD6425G1-10(3.7mm)](https://assets.hikvision.com/prd/public/all/files/202206/IPCG_E8_EN_STD_5.7.210_220615.zip)2m | 2022-06-15 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202206/IPCG_E8_EN_STD_5.7.210_220615.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202312/releasenote%5CIPC_V5.7.210_SP_Release_Note--EN.pdf) |

</details>


<details>
<summary><h2>DS-2CD6425G2-C1 - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.20 | Applied to: [DS-2CD6425G2-C1](https://assets.hikvision.com/prd/public/all/files/202305/Firmware__V5.8.20_230426_S3000496912.zip) | 2023-04-26 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202305/Firmware__V5.8.20_230426_S3000496912.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202312/releasenote%5CIPCG_OP_G5_V5.8.20_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD6425G2-C2 - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.20 | Applied to: [DS-2CD6425G2-C2](https://assets.hikvision.com/prd/public/all/files/202305/Firmware__V5.8.20_230426_S3000496912.zip) | 2023-04-26 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202305/Firmware__V5.8.20_230426_S3000496912.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202312/releasenote%5CIPCG_OP_G5_V5.8.20_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD6445G1-XX - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.210 | Applied to: [DS-2CD6445G1-30(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202206/IPCG_E8_EN_STD_5.7.210_220615.zip)2m | 2022-06-15 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202206/IPCG_E8_EN_STD_5.7.210_220615.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202312/releasenote%5CIPC_V5.7.210_SP_Release_Note--EN.pdf) |

</details>


<details>
<summary><h2>DS-2CD6445G2-C1 - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.20 | Applied to: [DS-2CD6445G2-C1/HDMI](https://assets.hikvision.com/prd/public/all/files/202305/Firmware__V5.8.20_230426_S3000496912.zip) | 2023-04-26 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202305/Firmware__V5.8.20_230426_S3000496912.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202312/releasenote%5CIPCG_OP_G5_V5.8.20_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD6825G0 - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.10 | Applied to: [DS-2CD6825G0/C-I(2mm)](https://assets.hikvision.com/prd/normal/all/files/202507/Firmware__V5.8.10_250624_S3000661598.zip)(B) | 2025-06-24 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202507/Firmware__V5.8.10_250624_S3000661598.zip) |  |

</details>


<details>
<summary><h2>DS-2CD6825G0 - IPC_V5 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.850 | Applied to: [DS-2CD6825G0/C-I(2mm)](https://assets.hikvision.com/prd/public/all/files/202205/IPCDC_H7_EN_STD_5.5.850_220421.zip) | 2022-04-21 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202205/IPCDC_H7_EN_STD_5.5.850_220421.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202207/IPC_V5.5.850_build_220421_Release%20Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD6924G0-IHS - IPC_G0 (3 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.1 | Applied to: [DS-2CD6924G0-IHS(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202406/1718399693233/Firmware__V5.7.1_240613_S3000580356.zip)(C) | 2024-06-13 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202406/1718399693233/Firmware__V5.7.1_240613_S3000580356.zip) |  |
| 5.7.0 | Applied to: [DS-2CD6924G0-IHS/NFC(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202402/Firmware__V5.7.0_240129_S3000555034.zip) | 2024-01-29 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202402/Firmware__V5.7.0_240129_S3000555034.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202312/releasenote%5CIPCP_H5_5.5.820_Release_Note.pdf) |
| 5.5.820 | Applied to: [DS-2CD6924G0-IHS/NFC(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202312/Firmware__V5.5.820_230717_S3000547672.zip) | 2023-07-17 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202312/Firmware__V5.5.820_230717_S3000547672.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202312/releasenote%5CIPCP_H5_5.5.820_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD6944G0-IHS - IPC_G0 (3 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.1 | Applied to: [DS-2CD6944G0-IHS(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202406/1718399693233/Firmware__V5.7.1_240613_S3000580356.zip)(C) | 2024-06-13 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202406/1718399693233/Firmware__V5.7.1_240613_S3000580356.zip) |  |
| 5.7.0 | Applied to: [DS-2CD6944G0-IHS(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202402/Firmware__V5.7.0_240129_S3000555034.zip) | 2024-01-29 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202402/Firmware__V5.7.0_240129_S3000555034.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202312/releasenote%5CIPCP_H5_5.5.820_Release_Note.pdf) |
| 5.5.820 | Applied to: [DS-2CD6944G0-IHS(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202312/Firmware__V5.5.820_230717_S3000547672.zip) | 2023-07-17 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202312/Firmware__V5.5.820_230717_S3000547672.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202312/releasenote%5CIPCP_H5_5.5.820_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD6951G2-IS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.11 | Applied to: [DS-2CD6951G2-IS(2mm)](https://assets.hikvision.com/prd/normal/all/files/202511/Firmware__V5.8.11_251114_S3000686926.zip) | 2025-11-14 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202511/Firmware__V5.8.11_251114_S3000686926.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CIPCG_PS_G5_Camera_V5.8.11_251114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD6984G0-IH - IPC_G0 (3 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.0 | Applied to: [DS-2CD6984G0-IHSAC/NFC(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202402/Firmware__V5.7.0_240129_S3000555034.zip) | 2024-01-29 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202402/Firmware__V5.7.0_240129_S3000555034.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202312/releasenote%5CIPCP_H5_5.5.820_Release_Note.pdf) |
| 5.5.820 | Applied to: [DS-2CD6984G0-IHSAC/NFC(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202312/Firmware__V5.5.820_230717_S3000547672.zip) | 2023-07-17 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202312/Firmware__V5.5.820_230717_S3000547672.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202312/releasenote%5CIPCP_H5_5.5.820_Release_Note.pdf) |
| 5.5.800 | Applied to: [DS-2CD6984G0-IHSAC/NFC(2.8mm)](https://assets.hikvision.com/prd/public/all/files/34fbba54-1d37-4561-bb64-efceb8d155cb.zip) | 2021-10-09 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/34fbba54-1d37-4561-bb64-efceb8d155cb.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202312/releasenote%5CIPCP_H5_5.5.820_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD6B55G0-PL - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.211 | Applied to: [DS-2CD6B55G0-PL/T1(4mm)](https://assets.hikvision.com/prd/normal/all/files/202509/Firmware__V5.7.211_250825_S3000670507.zip) | 2025-08-25 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202509/Firmware__V5.7.211_250825_S3000670507.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5C6B_Camera_V5.7.211_250825_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD6D24FWD-IZHS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.821 | Applied to: [DS-2CD6D24FWD-IZHS(2.8-12mm)](https://assets.hikvision.com/prd/public/all/files/202310/Firmware__V5.5.821_230830_S3000530199.zip)(B) | 2023-08-30 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202310/Firmware__V5.5.821_230830_S3000530199.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202310/releasenote%5CIPCMC_H3_V5.5.821_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD6D42G0-IS - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.21 | Applied to: [DS-2CD6D42G0-IS(2.8mm)](https://assets.hikvision.com/prd/normal/all/files/202509/Firmware__V5.8.21_250901_S3000672195.zip) | 2025-09-01 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202509/Firmware__V5.8.21_250901_S3000672195.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202508/releasenote%5CIPCG_PS_G5_Camera_V5.8.11_250730_Release_Note.pdf) |
| 5.8.11 | Applied to: [DS-2CD6D42G0-IS(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202309/Firmware__V5.8.11_230807_S3000526550.zip) | 2023-08-07 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202309/Firmware__V5.8.11_230807_S3000526550.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202508/releasenote%5CIPCG_PS_G5_Camera_V5.8.11_250730_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD6D42G2-IS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.9.0 | Applied to: [DS-2CD6D42G2-IS(2.8mm)](https://assets.hikvision.com/prd/normal/all/files/202508/Firmware__V5.9.0_250730_S3000665724.zip) | 2025-07-30 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202508/Firmware__V5.9.0_250730_S3000665724.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5C6_Series_Dual-Lens_Camera_V5.9.0_250730_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD6D44G1-IZS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.9.11 | Applied to: [DS-2CD6D44G1-IZS(2.8-8mm)](https://assets.hikvision.com/prd/public/all/files/202401/Firmware__V5.9.11_240123_S3000553978.zip) | 2024-01-23 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202401/Firmware__V5.9.11_240123_S3000553978.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202403/releasenote%5CG7_6D_V5.9.11_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD6D44G1H-IZS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.9.11 | Applied to: [DS-2CD6D44G1H-IZS(2.8-12mm)](https://assets.hikvision.com/prd/public/all/files/202401/Firmware__V5.9.11_240123_S3000553978.zip) | 2024-01-23 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202401/Firmware__V5.9.11_240123_S3000553978.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202403/releasenote%5CG7_6D_V5.9.11_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD6D52G0-IH - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.820 | Applied to: [DS-2CD6D52G0-IHS(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202207/IPC_H7_EN_STD_5.5.820_220609.zip) | 2022-06-09 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202207/IPC_H7_EN_STD_5.5.820_220609.zip) |  |

</details>


<details>
<summary><h2>DS-2CD6D54FWD- - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.801 | Applied to: [DS-2CD6D54FWD-IZHS(2.8-12mm)](https://assets.hikvision.com/prd/public/all/files/4c6ede40-0464-4a88-a0e4-f87cc45b37a2.zip) | 2021-09-27 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/4c6ede40-0464-4a88-a0e4-f87cc45b37a2.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202207/IPC%20V5.5.801%20build%20210927%20Release%20Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD6D54G1-IZ - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.801 | Applied to: [DS-2CD6D54G1-IZS(2.8-8mm)](https://assets.hikvision.com/prd/public/all/files/4c6ede40-0464-4a88-a0e4-f87cc45b37a2.zip) | 2021-09-27 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/4c6ede40-0464-4a88-a0e4-f87cc45b37a2.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202207/IPC%20V5.5.801%20build%20210927%20Release%20Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD6D54G1-IZS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.821 | Applied to: [DS-2CD6D54G1-IZS(2.8-8mm)](https://assets.hikvision.com/prd/public/all/files/202310/Firmware__V5.5.821_230830_S3000530199.zip)(B) | 2023-08-30 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202310/Firmware__V5.5.821_230830_S3000530199.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202310/releasenote%5CIPCMC_H3_V5.5.821_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD6D54G1-ZS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.801 | Applied to: [DS-2CD6D54G1-ZS/RC(2.8-8mm)](https://assets.hikvision.com/prd/public/all/files/4c6ede40-0464-4a88-a0e4-f87cc45b37a2.zip) | 2021-09-27 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/4c6ede40-0464-4a88-a0e4-f87cc45b37a2.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202207/IPC%20V5.5.801%20build%20210927%20Release%20Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD6D54G2-IZHS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.9.0 | Applied to: [DS-2CD6D54G2-IZHS(2.8-8mm)](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.9.0_251208_S3000690292.zip) | 2025-12-08 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.9.0_251208_S3000690292.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CPanoVu_Camera_6D5x_V5.9.0_251208_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD6D55G2-IZHS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.9.0 | Applied to: [DS-2CD6D55G2-IZHS(2.8-8mm/2mm)](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.9.0_251208_S3000690292.zip) | 2025-12-08 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.9.0_251208_S3000690292.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202601/releasenote%5CPanoVu_Camera_6D5x_V5.9.0_251208_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD6D82G0-IH - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.820 | Applied to: [DS-2CD6D82G0-IHS(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202207/IPC_H7_EN_STD_5.5.820_220609.zip) | 2022-06-09 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202207/IPC_H7_EN_STD_5.5.820_220609.zip) |  |

</details>


<details>
<summary><h2>DS-2CD6D82G2-IS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.9.0 | Applied to: [DS-2CD6D82G2-IS(2.8mm)](https://assets.hikvision.com/prd/normal/all/files/202508/Firmware__V5.9.0_250730_S3000665724.zip) | 2025-07-30 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202508/Firmware__V5.9.0_250730_S3000665724.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5C6_Series_Dual-Lens_Camera_V5.9.0_250730_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CD6F82G0-S - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.2 | Applied to: [DS-2CD6F82G0-S(4mm/8mm)](https://assets.hikvision.com/prd/public/all/files/202507/Firmware__V5.8.2_250709_S3000660429.zip) | 2025-07-09 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202507/Firmware__V5.8.2_250709_S3000660429.zip) |  |

</details>


<details>
<summary><h2>DS-2CD6F82G0-WS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.2 | Applied to: [DS-2CD6F82G0-WS(4mm/8mm)](https://assets.hikvision.com/prd/public/all/files/202507/Firmware__V5.8.2_250709_S3000660429.zip) | 2025-07-09 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202507/Firmware__V5.8.2_250709_S3000660429.zip) |  |

</details>


<details>
<summary><h2>DS-2CD6W65G1-IVS - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.3 | Applied to: [DS-2CD6W65G1-IVS(1.16mm)](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.3_260112_S3000699425.zip) | 2026-01-12 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.3_260112_S3000699425.zip) |  |

</details>


<details>
<summary><h2>DS-2CE11D0T-PIRLO - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 1.04.00 | Applied to: [DS-2CE11D0T-PIRLO(2.8mm)](https://assets.hikvision.com/prd/public/all/files/69abb770-f4dd-44cc-8019-2402c5b56195.zip) | 2019-12-02 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/69abb770-f4dd-44cc-8019-2402c5b56195.zip) |  |

</details>


<details>
<summary><h2>DS-2CE12D0T-PIRLO - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 1.04.00 | Applied to: [DS-2CE12D0T-PIRLO(2.8mm)](https://assets.hikvision.com/prd/public/all/files/69abb770-f4dd-44cc-8019-2402c5b56195.zip) | 2019-12-02 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/69abb770-f4dd-44cc-8019-2402c5b56195.zip) |  |

</details>


<details>
<summary><h2>DS-2CE16C0T-IRP - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 1.03.00 | Applied to: [DS-2CE16C0T-IRP(2.8mm)](https://assets.hikvision.com/prd/public/all/files/2d1e38da-635e-4597-9968-4849720b7602.zip)(B) | 2018-01-17 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/2d1e38da-635e-4597-9968-4849720b7602.zip) |  |

</details>


<details>
<summary><h2>DS-2CE16D0T-VFIR3F - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 1.09.00 | Applied to: [DS-2CE16D0T-VFIR3F(2.8-12mm)](https://assets.hikvision.com/prd/public/all/files/c07f4409-e9af-42b2-af68-4dd1a78afad4.zip) | 2021-12-02 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/c07f4409-e9af-42b2-af68-4dd1a78afad4.zip) |  |

</details>


<details>
<summary><h2>DS-2CE16H0T-ITF - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 1.03.02 | Applied to: [DS-2CE16H0T-ITF(2.8mm)](https://assets.hikvision.com/prd/public/all/files/431928a6-68c4-4c12-9768-f832b6d9ce30.zip) | 2020-08-26 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/431928a6-68c4-4c12-9768-f832b6d9ce30.zip) |  |

</details>


<details>
<summary><h2>DS-2CE56C0T-IRP - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 1.03.00 | Applied to: [DS-2CE56C0T-IRP(2.8mm)](https://assets.hikvision.com/prd/public/all/files/2d1e38da-635e-4597-9968-4849720b7602.zip)(B) | 2018-01-17 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/2d1e38da-635e-4597-9968-4849720b7602.zip) |  |

</details>


<details>
<summary><h2>DS-2CE56D0T-VFIR3E - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 1.05.01 | Applied to: [DS-2CE56D0T-VFIR3E(2.8-12mm)](https://assets.hikvision.com/prd/public/all/files/43fc2fab-1e87-4a88-b81f-807028b6c33c.zip) | 2020-03-23 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/43fc2fab-1e87-4a88-b81f-807028b6c33c.zip) |  |

</details>


<details>
<summary><h2>DS-2CE56D0T-VFIR3F - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 1.09.00 | Applied to: [DS-2CE56D0T-VFIR3F(2.8-12mm)](https://assets.hikvision.com/prd/public/all/files/70474c85-ca48-4d5d-bc63-6ff018ea610c.zip) | 2019-12-02 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/70474c85-ca48-4d5d-bc63-6ff018ea610c.zip) |  |

</details>


<details>
<summary><h2>DS-2CE56D0T-VFIRE - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 1.05.01 | Applied to: [DS-2CE56D0T-VFIRE(2.8-12mm)](https://assets.hikvision.com/prd/public/all/files/f5bbc2ed-315c-4413-a94c-5fd4fdda15de.zip) | 2020-03-23 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/f5bbc2ed-315c-4413-a94c-5fd4fdda15de.zip) |  |

</details>


<details>
<summary><h2>DS-2CE56D0T-VPIR3F - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 1.09.00 | Applied to: [DS-2CE56D0T-VPIR3F(2.8-12mm)](https://assets.hikvision.com/prd/public/all/files/70474c85-ca48-4d5d-bc63-6ff018ea610c.zip) | 2019-12-02 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/70474c85-ca48-4d5d-bc63-6ff018ea610c.zip) |  |

</details>


<details>
<summary><h2>DS-2CE71D0T-PIRLO - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 1.04.00 | Applied to: [DS-2CE71D0T-PIRLO(2.8mm)](https://assets.hikvision.com/prd/public/all/files/69abb770-f4dd-44cc-8019-2402c5b56195.zip) | 2019-12-02 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/69abb770-f4dd-44cc-8019-2402c5b56195.zip) |  |

</details>


<details>
<summary><h2>DS-2CFS04 - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.9.11 | Applied to: [DS-2CFS04/4G(4mm)](https://assets.hikvision.com/prd/normal/all/files/202511/Firmware__V5.9.11_251030_S3000682327.zip) | 2025-10-30 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202511/Firmware__V5.9.11_251030_S3000682327.zip) |  |

</details>


<details>
<summary><h2>DS-2CFW02 - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.22 | Applied to: [DS-2CFW02(2.8mm)](https://assets.hikvision.com/prd/normal/all/files/202507/Firmware__V5.8.22_250708_S3000661552.zip) | 2025-07-08 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202507/Firmware__V5.8.22_250708_S3000661552.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202508/releasenote%5CNetwork_Camera-V5.8.22_250708_Release_Note-E9.pdf) |

</details>


<details>
<summary><h2>DS-2CFW04 - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.22 | Applied to: [DS-2CFW04(2.8mm)](https://assets.hikvision.com/prd/normal/all/files/202507/Firmware__V5.8.22_250708_S3000661562.zip) | 2025-07-08 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202507/Firmware__V5.8.22_250708_S3000661562.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202508/releasenote%5CNetwork_Camera-V5.8.22_250708_Release_Note-E10.pdf) |

</details>


<details>
<summary><h2>DS-2CFW06-P - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.10 | Applied to: [DS-2CFW06-P(2.8mm)](https://assets.hikvision.com/prd/normal/all/files/202511/Firmware__V5.8.10_251029_S3000683391.zip) | 2025-10-29 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202511/Firmware__V5.8.10_251029_S3000683391.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.8.10_251029_Release_Note-IPCE_PW_E11.pdf) |

</details>


<details>
<summary><h2>DS-2CFWQ3 - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.100 | Applied to: [DS-2CFWQ3(2.8mm)](https://assets.hikvision.com/prd/normal/all/files/202508/Firmware__V5.8.100_250805_S3000666892.zip) | 2025-08-05 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202508/Firmware__V5.8.100_250805_S3000666892.zip) |  |

</details>


<details>
<summary><h2>DS-2CFWQ5 - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.100 | Applied to: [DS-2CFWQ5(2.8mm)](https://assets.hikvision.com/prd/normal/all/files/202508/Firmware__V5.8.100_250725_S3000664410.zip) | 2025-07-25 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202508/Firmware__V5.8.100_250725_S3000664410.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202509/releasenote%5CNetwork_Camera-V5.8.100_250725_Release_Note-E12.pdf) |

</details>


<details>
<summary><h2>DS-2CFWQ6-D - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.110 | Applied to: [DS-2CFWQ6-D(2.8+4mm)](https://assets.hikvision.com/prd/normal/all/files/202510/Firmware__V5.8.110_250725_S3000664408.zip) | 2025-07-25 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202510/Firmware__V5.8.110_250725_S3000664408.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202509/releasenote%5CNetwork_Camera-V5.8.100_250725_Release_Note-E12.pdf) |

</details>


<details>
<summary><h2>DS-2CV1021G0-IDW - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.821 | Applied to: [DS-2CV1021G0-IDW1(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202312/Firmware__V5.5.821_231108_S3000539545.zip)(D) | 2023-11-08 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202312/Firmware__V5.5.821_231108_S3000539545.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202404/1712790066963/releasenote%5CIPC_E6_5.5.821_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CV1023G2-LIDW - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.22 | Applied to: [DS-2CV1023G2-LIDWF(2.8mm)](https://assets.hikvision.com/prd/normal/all/files/202507/Firmware__V5.8.22_250708_S3000661552.zip)(B) | 2025-07-08 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202507/Firmware__V5.8.22_250708_S3000661552.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202508/releasenote%5CNetwork_Camera-V5.8.22_250708_Release_Note-E9.pdf) |

</details>


<details>
<summary><h2>DS-2CV1043G2-LIDW - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.22 | Applied to: [DS-2CV1043G2-LIDWF(2.8mm)](https://assets.hikvision.com/prd/normal/all/files/202507/Firmware__V5.8.22_250708_S3000661562.zip)(B) | 2025-07-08 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202507/Firmware__V5.8.22_250708_S3000661562.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202508/releasenote%5CNetwork_Camera-V5.8.22_250708_Release_Note-E10.pdf) |

</details>


<details>
<summary><h2>DS-2CV1F23G2-LIDWF - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.22 | Applied to: [DS-2CV1F23G2-LIDWF(2.8mm)](https://assets.hikvision.com/prd/normal/all/files/202507/Firmware__V5.8.22_250708_S3000661552.zip)(B) | 2025-07-08 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202507/Firmware__V5.8.22_250708_S3000661552.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202508/releasenote%5CNetwork_Camera-V5.8.22_250708_Release_Note-E9.pdf) |

</details>


<details>
<summary><h2>DS-2CV1F43G2-LIDWF - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.22 | Applied to: [DS-2CV1F43G2-LIDWF(2.8mm)](https://assets.hikvision.com/prd/normal/all/files/202507/Firmware__V5.8.22_250708_S3000661562.zip)(B) | 2025-07-08 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202507/Firmware__V5.8.22_250708_S3000661562.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202508/releasenote%5CNetwork_Camera-V5.8.22_250708_Release_Note-E10.pdf) |

</details>


<details>
<summary><h2>DS-2CV2021G2-IDW - UNKNOWN (3 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.24 | Applied to: [DS-2CV2021G2-IDW(2.8mm)](https://assets.hikvision.com/prd/normal/all/files/202509/Firmware__V5.7.24_250828_S3000671925.zip) | 2025-08-28 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202509/Firmware__V5.7.24_250828_S3000671925.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202404/1712790066963/releasenote%5CIPC_E6_5.5.821_Release_Note.pdf) |
| 5.5.821 | Applied to: [DS-2CV2021G2-IDW(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202312/Firmware__V5.5.821_231108_S3000539545.zip) | 2023-11-08 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202312/Firmware__V5.5.821_231108_S3000539545.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202404/1712790066963/releasenote%5CIPC_E6_5.5.821_Release_Note.pdf) |
| 5.5.803 | Applied to: [DS-2CV2021G2-IDW(2.8mm)](https://assets.hikvision.com/prd/public/all/files/e037f86a-4a71-43a9-9297-c597d9bca538.zip) | 2021-08-17 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/e037f86a-4a71-43a9-9297-c597d9bca538.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202404/1712790066963/releasenote%5CIPC_E6_5.5.821_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CV2026G0-IDW - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.820 | Applied to: [DS-2CV2026G0-IDW(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202312/Firmware__V5.5.820_231120_S3000541957.zip)(D) | 2023-11-20 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202312/Firmware__V5.5.820_231120_S3000541957.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202401/releasenote%5CNetwork_Camera-V5.5.820_Release_Note-G6.pdf) |

</details>


<details>
<summary><h2>DS-2CV2027G0-LDW - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.820 | Applied to: [DS-2CV2027G0-LDW(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202312/Firmware__V5.5.820_231120_S3000541957.zip) | 2023-11-20 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202312/Firmware__V5.5.820_231120_S3000541957.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202401/releasenote%5CNetwork_Camera-V5.5.820_Release_Note-G6.pdf) |

</details>


<details>
<summary><h2>DS-2CV2041G2-IDW - UNKNOWN (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.24 | Applied to: [DS-2CV2041G2-IDW(4mm)](https://assets.hikvision.com/prd/normal/all/files/202509/Firmware__V5.7.24_250828_S3000671925.zip)(D) | 2025-08-28 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202509/Firmware__V5.7.24_250828_S3000671925.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202401/releasenote%5CNetwork_Camera-V5.5.820_Release_Note-G6.pdf) |
| 5.5.820 | Applied to: [DS-2CV2041G2-IDW(4mm)](https://assets.hikvision.com/prd/public/all/files/202312/Firmware__V5.5.820_231120_S3000541958.zip)(D) | 2023-11-20 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202312/Firmware__V5.5.820_231120_S3000541958.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202401/releasenote%5CNetwork_Camera-V5.5.820_Release_Note-G6.pdf) |

</details>


<details>
<summary><h2>DS-2CV2046G0-IDW - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.820 | Applied to: [DS-2CV2046G0-IDW(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202312/Firmware__V5.5.820_231120_S3000541957.zip)(D) | 2023-11-20 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202312/Firmware__V5.5.820_231120_S3000541957.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202401/releasenote%5CNetwork_Camera-V5.5.820_Release_Note-G6.pdf) |

</details>


<details>
<summary><h2>DS-2CV2126G0-IDW - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.820 | Applied to: [DS-2CV2126G0-IDW(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202312/Firmware__V5.5.820_231120_S3000541957.zip) | 2023-11-20 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202312/Firmware__V5.5.820_231120_S3000541957.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202401/releasenote%5CNetwork_Camera-V5.5.820_Release_Note-G6.pdf) |

</details>


<details>
<summary><h2>DS-2CV2141G2-IDW - UNKNOWN (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.24 | Applied to: [DS-2CV2141G2-IDW(2.8mm)](https://assets.hikvision.com/prd/normal/all/files/202509/Firmware__V5.7.24_250828_S3000671925.zip) | 2025-08-28 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202509/Firmware__V5.7.24_250828_S3000671925.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202511/releasenote%5CNetwork_Camera-V5.7.24_SP1_Release_Note-E8.pdf) |
| 5.5.800 | Applied to: [DS-2CV2141G2-IDW(2.8mm)](https://assets.hikvision.com/prd/public/all/files/48db7f95-c2ae-44ae-9708-0a05fc35bb9f.zip) | 2021-08-16 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/48db7f95-c2ae-44ae-9708-0a05fc35bb9f.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202511/releasenote%5CNetwork_Camera-V5.7.24_SP1_Release_Note-E8.pdf) |

</details>


<details>
<summary><h2>DS-2CV2146G0-IDW - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.820 | Applied to: [DS-2CV2146G0-IDW(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202312/Firmware__V5.5.820_231120_S3000541957.zip) | 2023-11-20 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202312/Firmware__V5.5.820_231120_S3000541957.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202401/releasenote%5CNetwork_Camera-V5.5.820_Release_Note-G6.pdf) |

</details>


<details>
<summary><h2>DS-2CV2Q21FD-IW - UNKNOWN (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.5.821 | Applied to: [DS-2CV2Q21FD-IW(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202312/Firmware__V5.5.821_231108_S3000539548.zip) | 2023-11-08 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202312/Firmware__V5.5.821_231108_S3000539548.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202404/1712790068455/releasenote%5CIPC_E6_5.5.821_Release_Note.pdf) |
| 5.4.800 | Applied to: [DS-2CV2Q21FD-IW(2.8mm)](https://assets.hikvision.com/prd/public/all/files/6005351b-ceff-48af-bb0a-5e671137820c.zip) | 2021-10-20 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/6005351b-ceff-48af-bb0a-5e671137820c.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202404/1712790068455/releasenote%5CIPC_E6_5.5.821_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2CV2U32G1-IW - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.4.71 | Applied to: [DS-2CV2U32G1-IDW(1.68mm)](https://assets.hikvision.com/prd/public/all/files/202311/Firmware__V5.4.71_181129_S3000260066.zip) | 2018-11-29 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202311/Firmware__V5.4.71_181129_S3000260066.zip) |  |

</details>


<details>
<summary><h2>DS-2DB4223I-CX - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.7 | Applied to: [DS-2DB4223I-CX(T5/316L)](https://assets.hikvision.com/prd/public/all/files/202312/Firmware__V5.7.7_231117_S3000540108.zip) | 2023-11-17 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202312/Firmware__V5.7.7_231117_S3000540108.zip) |  |

</details>


<details>
<summary><h2>DS-2DB4236I-CWX - UNKNOWN (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.7 | Applied to: [DS-2DB4236I-CWX(T5/316L)](https://assets.hikvision.com/prd/public/all/files/202312/Firmware__V5.7.7_231117_S3000540108.zip) | 2023-11-17 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202312/Firmware__V5.7.7_231117_S3000540108.zip) |  |

</details>


<details>
<summary><h2>DS-2DE2A204IW-DE3 - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.30 | Applied to: [DS-2DE2A204IW-DE3/W(C0)](https://assets.hikvision.com/prd/normal/all/files/202509/Firmware__V5.7.30_250729_S3000670024.zip)(S6)(C) | 2025-07-29 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202509/Firmware__V5.7.30_250729_S3000670024.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202511/releasenote%5CV5.7.30_250729_Release_Note.pdf) |
| 5.7.11 | Applied to: [DS-2DE2A204IW-DE3(C0)](https://assets.hikvision.com/prd/public/all/files/202307/Firmware__V5.7.11_230612_S3000509332.zip)(S6)(C) | 2023-06-12 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202307/Firmware__V5.7.11_230612_S3000509332.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202312/releasenote%5CRelease_Note_E7_V5.7.11_230612.pdf) |

</details>


<details>
<summary><h2>DS-2DE2A204IWG1-E - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.9.2 | Applied to: [DS-2DE2A204IWG1-E/W](https://assets.hikvision.com/prd/normal/all/files/202603/Firmware__V5.9.2_260208_S3000703533.zip) | 2026-02-08 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202603/Firmware__V5.9.2_260208_S3000703533.zip) |  |
| 5.9.5 | Applied to: [DS-2DE2A204IWG1-E](https://assets.hikvision.com/prd/normal/all/files/202602/Firmware__V5.9.5_260129_S3000702016.zip) | 2026-01-29 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202602/Firmware__V5.9.5_260129_S3000702016.zip) |  |

</details>


<details>
<summary><h2>DS-2DE2A404IW-DE3 - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.30 | Applied to: [DS-2DE2A404IW-DE3/W(C0)](https://assets.hikvision.com/prd/normal/all/files/202509/Firmware__V5.7.30_250729_S3000670024.zip)(S6)(C) | 2025-07-29 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202509/Firmware__V5.7.30_250729_S3000670024.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202511/releasenote%5CV5.7.30_250729_Release_Note.pdf) |
| 5.7.11 | Applied to: [DS-2DE2A404IW-DE3(C0)](https://assets.hikvision.com/prd/public/all/files/202307/Firmware__V5.7.11_230612_S3000509332.zip)(S6)(C) | 2023-06-12 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202307/Firmware__V5.7.11_230612_S3000509332.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202312/releasenote%5CRelease_Note_E7_V5.7.11_230612.pdf) |

</details>


<details>
<summary><h2>DS-2DE2A404IWG1-E - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.9.2 | Applied to: [DS-2DE2A404IWG1-E/W](https://assets.hikvision.com/prd/normal/all/files/202603/Firmware__V5.9.2_260208_S3000703533.zip) | 2026-02-08 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202603/Firmware__V5.9.2_260208_S3000703533.zip) |  |
| 5.9.5 | Applied to: [DS-2DE2A404IWG1-E](https://assets.hikvision.com/prd/normal/all/files/202602/Firmware__V5.9.5_260129_S3000702016.zip) | 2026-01-29 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202602/Firmware__V5.9.5_260129_S3000702016.zip) |  |

</details>


<details>
<summary><h2>DS-2DE2A604IWG1-E - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.9.2 | Applied to: [DS-2DE2A604IWG1-E/W](https://assets.hikvision.com/prd/normal/all/files/202603/Firmware__V5.9.2_260208_S3000703533.zip) | 2026-02-08 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202603/Firmware__V5.9.2_260208_S3000703533.zip) |  |
| 5.9.5 | Applied to: [DS-2DE2A604IWG1-E](https://assets.hikvision.com/prd/normal/all/files/202602/Firmware__V5.9.5_260129_S3000702016.zip) | 2026-01-29 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202602/Firmware__V5.9.5_260129_S3000702016.zip) |  |

</details>


<details>
<summary><h2>DS-2DE2C200MW-DE - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.23 | Applied to: [DS-2DE2C200MW-DE(F0)](https://assets.hikvision.com/prd/public/all/files/202505/Firmware__V5.7.23_241211_S3000620671.zip)(S7) | 2024-12-11 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202505/Firmware__V5.7.23_241211_S3000620671.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202507/releasenote%5CNetwork_Camera-V5.7.23_SP2_Release_Note-E8.pdf) |

</details>


<details>
<summary><h2>DS-2DE2C200MWG - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.23 | Applied to: [DS-2DE2C200MWG/W(2.8mm)](https://assets.hikvision.com/prd/normal/all/files/202511/Firmware__V5.8.23_250820_S3000674313.zip) | 2025-08-20 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202511/Firmware__V5.8.23_250820_S3000674313.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.8.23_Release_Note-E9_E10.pdf) |

</details>


<details>
<summary><h2>DS-2DE2C200MWG-4G - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.34 | Applied to: [DS-2DE2C200MWG-4G(2.8mm)](https://assets.hikvision.com/prd/normal/all/files/202509/Firmware__V5.8.34_250908_S3000674318.zip) | 2025-09-08 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202509/Firmware__V5.8.34_250908_S3000674318.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202511/releasenote%5CNetwork_Camera-V5.8.34_Release_Note-E9_E10.pdf) |

</details>


<details>
<summary><h2>DS-2DE2C200MWG-E - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.21 | Applied to: [DS-2DE2C200MWG-E(2.8mm)](https://assets.hikvision.com/prd/normal/all/files/202507/Firmware__V5.8.21_250714_S3000661481.zip) | 2025-07-14 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202507/Firmware__V5.8.21_250714_S3000661481.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202508/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-E9.pdf) |

</details>


<details>
<summary><h2>DS-2DE2C200SCG-E - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.20 | Applied to: [DS-2DE2C200SCG-E(F0)](https://assets.hikvision.com/prd/public/all/files/202307/Firmware__V5.7.20_230630_S3000509422.zip) | 2023-06-30 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202307/Firmware__V5.7.20_230630_S3000509422.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202312/releasenote%5CNetwork_Camera-V5.7.20_SP4_Release_Note-E8.pdf) |

</details>


<details>
<summary><h2>DS-2DE2C400MW-DE - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.20 | Applied to: [DS-2DE2C400MW-DE(F0)](https://assets.hikvision.com/prd/public/all/files/202307/Firmware__V5.7.20_230630_S3000509422.zip)(S7) | 2023-06-30 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202307/Firmware__V5.7.20_230630_S3000509422.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202312/releasenote%5CNetwork_Camera-V5.7.20_SP4_Release_Note-E8.pdf) |

</details>


<details>
<summary><h2>DS-2DE2C400MWG - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.23 | Applied to: [DS-2DE2C400MWG/W(2.8mm)](https://assets.hikvision.com/prd/normal/all/files/202511/Firmware__V5.8.23_250820_S3000674333.zip) | 2025-08-20 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202511/Firmware__V5.8.23_250820_S3000674333.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CNetwork_Camera-V5.8.23_Release_Note-E9_E10.pdf) |

</details>


<details>
<summary><h2>DS-2DE2C400MWG-4G - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.34 | Applied to: [DS-2DE2C400MWG-4G(2.8mm)](https://assets.hikvision.com/prd/normal/all/files/202509/Firmware__V5.8.34_250908_S3000674302.zip) | 2025-09-08 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202509/Firmware__V5.8.34_250908_S3000674302.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202602/releasenote%5CNetwork_Camera-V5.8.34_250908_Release_Note-IPCE_GL_E10.pdf) |

</details>


<details>
<summary><h2>DS-2DE2C400MWG-E - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.10 | Applied to: [DS-2DE2C400MWG-E(2.8mm)](https://assets.hikvision.com/prd/normal/all/files/202507/Firmware__V5.8.10_250714_S3000661518.zip) | 2025-07-14 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202507/Firmware__V5.8.10_250714_S3000661518.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202508/releasenote%5CNetwork_Camera-V5.8.30_Release_Note-E10.pdf) |

</details>


<details>
<summary><h2>DS-2DE2C400SCG-E - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.20 | Applied to: [DS-2DE2C400SCG-E(F0)](https://assets.hikvision.com/prd/public/all/files/202307/Firmware__V5.7.20_230630_S3000509422.zip) | 2023-06-30 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202307/Firmware__V5.7.20_230630_S3000509422.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202312/releasenote%5CNetwork_Camera-V5.7.20_SP4_Release_Note-E8.pdf) |

</details>


<details>
<summary><h2>DS-2DE2C600MWG-E - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.1 | Applied to: [DS-2DE2C600MWG-E(2.8mm)](https://assets.hikvision.com/prd/public/all/files/202501/Firmware__V5.8.1_250114_S3000626327.zip) | 2025-01-14 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202501/Firmware__V5.8.1_250114_S3000626327.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202512/releasenote%5CV5.8.1_250114_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2DE3204W-DE - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.1 | Applied to: [DS-2DE3204W-DE(T5)](https://assets.hikvision.com/prd/public/all/files/202401/Firmware__V5.8.1_231108_S3000540195.zip) | 2023-11-08 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202401/Firmware__V5.8.1_231108_S3000540195.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202408/releasenote%5CIPDE_C_H8_V5.8.1_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2DE3A400BW-DE - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.0 | Applied to: [DS-2DE3A400BW-DE(F1)](https://assets.hikvision.com/prd/public/all/files/202401/Firmware__V5.8.0_231109_S3000541088.zip)(T5) | 2023-11-09 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202401/Firmware__V5.8.0_231109_S3000541088.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202408/releasenote%5CRelease_Note_IPDE_H8_5.8.0_231109.pdf) |

</details>


<details>
<summary><h2>DS-2DE3A404IW-DE - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.12 | Applied to: [DS-2DE3A404IW-DE(S6)](https://assets.hikvision.com/prd/public/all/files/202303/Firmware__V5.7.12_220907_S3000453567.zip) | 2022-09-07 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202303/Firmware__V5.7.12_220907_S3000453567.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202408/releasenote%5CIPDE_E7_V5.7.12_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2DE3A404IWG-E - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.0 | Applied to: [DS-2DE3A404IWG-E/W](https://assets.hikvision.com/prd/public/all/files/202401/Firmware__V5.8.0_231109_S3000541088.zip) | 2023-11-09 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202401/Firmware__V5.8.0_231109_S3000541088.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202408/releasenote%5CRelease_Note_IPDE_H8_5.8.0_231109.pdf) |

</details>


<details>
<summary><h2>DS-2DE4215IW-DE - IPC_G0 (4 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.12 | Applied to: [DS-2DE4215IW-DE(T5)](https://assets.hikvision.com/prd/normal/all/files/202510/Firmware__V5.8.12_250915_S3000675132.zip) | 2025-09-15 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202510/Firmware__V5.8.12_250915_S3000675132.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202510/releasenote%5CV5.8.12_250915_Release_Note.pdf) |
| 5.7.11 | Applied to: [DS-2DE4215IW-DE(S6)](https://assets.hikvision.com/prd/public/all/files/202209/Firmware__V5.7.11_220905_S3000452187.zip) | 2022-09-05 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202209/Firmware__V5.7.11_220905_S3000452187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202312/releasenote%5CV5.7.11_Release_Note--E7.pdf) |
| 5.5.800 | Applied to: [DS-2DE4215IW-DE(S5)](https://assets.hikvision.com/prd/public/all/files/54ad2899-2282-4f50-a330-d5675227d26f.zip) | 2021-06-28 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/54ad2899-2282-4f50-a330-d5675227d26f.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/4cdf7c64-e179-4c02-a3ae-ec999c2710e9.pdf) |
| 5.6.18 | Applied to: [DS-2DE4215IW-DE(E)](https://assets.hikvision.com/prd/public/all/files/2d8cfccf-08c0-4b96-8dd4-9396e1383825.zip) | 2021-04-28 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/2d8cfccf-08c0-4b96-8dd4-9396e1383825.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202507/releasenote%5CRelease_Note.pdf) |

</details>


<details>
<summary><h2>DS-2DE4215IWG-E - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.10 | Applied to: [DS-2DE4215IWG-E(B)](https://assets.hikvision.com/prd/public/all/files/202405/1716330077337/Firmware__V5.8.10_240403_S3000567042.zip) | 2024-04-03 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202405/1716330077337/Firmware__V5.8.10_240403_S3000567042.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202408/releasenote%5CIDPE_L_H8_V5.8.10_240403_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2DE4215IWG1-E - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.1 | Applied to: [DS-2DE4215IWG1-E](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.1_260115_S3000699374.zip) | 2026-01-15 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.1_260115_S3000699374.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202603/releasenote%5CV5.8.1_260115_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2DE4215W-DE - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.6.17 | Applied to: [DS-2DE4215W-DE(E)](https://assets.hikvision.com/prd/public/all/files/7e8b3eb3-ee90-4e13-a100-e57d971016f9.zip) | 2021-04-11 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/7e8b3eb3-ee90-4e13-a100-e57d971016f9.zip) |  |

</details>


<details>
<summary><h2>DS-2DE4225IW-DE - IPC_G0 (3 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.12 | Applied to: [DS-2DE4225IW-DE(T5)](https://assets.hikvision.com/prd/normal/all/files/202510/Firmware__V5.8.12_250915_S3000675132.zip) | 2025-09-15 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202510/Firmware__V5.8.12_250915_S3000675132.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202510/releasenote%5CV5.8.12_250915_Release_Note.pdf) |
| 5.7.11 | Applied to: [DS-2DE4225IW-DE(S6)](https://assets.hikvision.com/prd/public/all/files/202209/Firmware__V5.7.11_220905_S3000452187.zip) | 2022-09-05 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202209/Firmware__V5.7.11_220905_S3000452187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202312/releasenote%5CV5.7.11_Release_Note--E7.pdf) |
| 5.6.18 | Applied to: [DS-2DE4225IW-DE(E)](https://assets.hikvision.com/prd/public/all/files/2d8cfccf-08c0-4b96-8dd4-9396e1383825.zip) | 2021-04-28 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/2d8cfccf-08c0-4b96-8dd4-9396e1383825.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202507/releasenote%5CRelease_Note.pdf) |

</details>


<details>
<summary><h2>DS-2DE4225IWG-E - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.10 | Applied to: [DS-2DE4225IWG-E(B)](https://assets.hikvision.com/prd/public/all/files/202405/1716330077337/Firmware__V5.8.10_240403_S3000567042.zip) | 2024-04-03 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202405/1716330077337/Firmware__V5.8.10_240403_S3000567042.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202408/releasenote%5CIDPE_L_H8_V5.8.10_240403_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2DE4225IWG1-E - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.1 | Applied to: [DS-2DE4225IWG1-E](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.1_260115_S3000699374.zip) | 2026-01-15 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.1_260115_S3000699374.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202603/releasenote%5CV5.8.1_260115_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2DE4225W-DE - IPC_G0 (3 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.11 | Applied to: [DS-2DE4225W-DE(S6)](https://assets.hikvision.com/prd/public/all/files/202209/Firmware__V5.7.11_220905_S3000452187.zip) | 2022-09-05 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202209/Firmware__V5.7.11_220905_S3000452187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202312/releasenote%5CV5.7.11_Release_Note--E7.pdf) |
| 5.6.18 | Applied to: [DS-2DE4225W-DE(B)](https://assets.hikvision.com/prd/public/all/files/2d8cfccf-08c0-4b96-8dd4-9396e1383825.zip) | 2021-04-28 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/2d8cfccf-08c0-4b96-8dd4-9396e1383825.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202507/releasenote%5CRelease_Note.pdf) |
| 5.6.14 | Applied to: [DS-2DE4225W-DE(B)](https://assets.hikvision.com/prd/public/all/files/6d583cfc-1b98-4ee8-973c-2fad9724b521.zip) | 2019-08-26 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/6d583cfc-1b98-4ee8-973c-2fad9724b521.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202507/releasenote%5CRelease_Note.pdf) |

</details>


<details>
<summary><h2>DS-2DE4225W-DE3 - IPC_G0 (2 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.7.11 | Applied to: [DS-2DE4225W-DE3(S6)](https://assets.hikvision.com/prd/public/all/files/202209/Firmware__V5.7.11_220905_S3000452187.zip) | 2022-09-05 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202209/Firmware__V5.7.11_220905_S3000452187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202312/releasenote%5CV5.7.11_Release_Note--E7.pdf) |
| 5.6.18 | Applied to: [DS-2DE4225W-DE3(B)](https://assets.hikvision.com/prd/public/all/files/2d8cfccf-08c0-4b96-8dd4-9396e1383825.zip) | 2021-04-28 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/2d8cfccf-08c0-4b96-8dd4-9396e1383825.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202507/releasenote%5CRelease_Note.pdf) |

</details>


<details>
<summary><h2>DS-2DE4225WG-E3 - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.0 | Applied to: [DS-2DE4225WG-E3](https://assets.hikvision.com/prd/public/all/files/202401/Firmware__V5.8.0_231109_S3000541088.zip) | 2023-11-09 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202401/Firmware__V5.8.0_231109_S3000541088.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202408/releasenote%5CRelease_Note_IPDE_H8_5.8.0_231109.pdf) |

</details>


<details>
<summary><h2>DS-2DE4225WG1-E3 - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.1 | Applied to: [DS-2DE4225WG1-E3](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.1_260115_S3000699374.zip) | 2026-01-15 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.1_260115_S3000699374.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202603/releasenote%5CV5.8.1_260115_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2DE4415IW-DE - IPC_G0 (4 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.12 | Applied to: [DS-2DE4415IW-DE(T5)](https://assets.hikvision.com/prd/normal/all/files/202510/Firmware__V5.8.12_250915_S3000675132.zip) | 2025-09-15 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202510/Firmware__V5.8.12_250915_S3000675132.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202510/releasenote%5CV5.8.12_250915_Release_Note.pdf) |
| 5.7.11 | Applied to: [DS-2DE4415IW-DE(S6)](https://assets.hikvision.com/prd/public/all/files/202209/Firmware__V5.7.11_220905_S3000452187.zip) | 2022-09-05 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202209/Firmware__V5.7.11_220905_S3000452187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202312/releasenote%5CV5.7.11_Release_Note--E7.pdf) |
| 5.5.800 | Applied to: [DS-2DE4415IW-DE(S5)](https://assets.hikvision.com/prd/public/all/files/54ad2899-2282-4f50-a330-d5675227d26f.zip) | 2021-06-28 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/54ad2899-2282-4f50-a330-d5675227d26f.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/4cdf7c64-e179-4c02-a3ae-ec999c2710e9.pdf) |
| 5.6.18 | Applied to: [DS-2DE4415IW-DE(E)](https://assets.hikvision.com/prd/public/all/files/2d8cfccf-08c0-4b96-8dd4-9396e1383825.zip) | 2021-04-28 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/2d8cfccf-08c0-4b96-8dd4-9396e1383825.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202507/releasenote%5CRelease_Note.pdf) |

</details>


<details>
<summary><h2>DS-2DE4415IWG-E - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.10 | Applied to: [DS-2DE4415IWG-E(B)](https://assets.hikvision.com/prd/public/all/files/202405/1716330077337/Firmware__V5.8.10_240403_S3000567042.zip) | 2024-04-03 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202405/1716330077337/Firmware__V5.8.10_240403_S3000567042.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202408/releasenote%5CIDPE_L_H8_V5.8.10_240403_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2DE4415IWG1-E - IPC_G0 (1 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.1 | Applied to: [DS-2DE4415IWG1-E](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.1_260115_S3000699374.zip) | 2026-01-15 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202601/Firmware__V5.8.1_260115_S3000699374.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202603/releasenote%5CV5.8.1_260115_Release_Note.pdf) |

</details>


<details>
<summary><h2>DS-2DE4425IW-DE - IPC_G0 (4 firmwares)</h2></summary>

| Version | Supported Models | Date | Download | Notes |
| ------- | ---------------- | ---- | -------- | ----- |
| 5.8.12 | Applied to: [DS-2DE4425IW-DE(T5)](https://assets.hikvision.com/prd/normal/all/files/202510/Firmware__V5.8.12_250915_S3000675132.zip) | 2025-09-15 | [🔗 Link](https://assets.hikvision.com/prd/normal/all/files/202510/Firmware__V5.8.12_250915_S3000675132.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202510/releasenote%5CV5.8.12_250915_Release_Note.pdf) |
| 5.7.11 | Applied to: [DS-2DE4425IW-DE(S6)](https://assets.hikvision.com/prd/public/all/files/202209/Firmware__V5.7.11_220905_S3000452187.zip) | 2022-09-05 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/202209/Firmware__V5.7.11_220905_S3000452187.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/202312/releasenote%5CV5.7.11_Release_Note--E7.pdf) |
| 5.5.800 | Applied to: [DS-2DE4425IW-DE(S5)](https://assets.hikvision.com/prd/public/all/files/54ad2899-2282-4f50-a330-d5675227d26f.zip) | 2021-06-28 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/54ad2899-2282-4f50-a330-d5675227d26f.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/public/all/files/4cdf7c64-e179-4c02-a3ae-ec999c2710e9.pdf) |
| 5.6.18 | Applied to: [DS-2DE4425IW-DE(E)](https://assets.hikvision.com/prd/public/all/files/2d8cfccf-08c0-4b96-8dd4-9396e1383825.zip) | 2021-04-28 | [🔗 Link](https://assets.hikvision.com/prd/public/all/files/2d8cfccf-08c0-4b96-8dd4-9396e1383825.zip) | [📄 Release Notes](https://assets.hikvision.com/prd/normal/all/files/202507/releasenote%5CRelease_Note.pdf) |

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
