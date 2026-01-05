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

**Status:** ❌ ERROR  
**Last Run:** 2026-01-05 10:54:39 UTC  
**Firmwares Found:** 14  
**New Firmwares:** 2  
**Test Mode:** Disabled



**Recent Errors:**
- ⚠️ Search failed for DS-2DE: ElementHandle.fill: Element is not attached to the DOM
Call log:
    - fill("")
  - attempting fill action
    - waiting for element to be visible, enabled and editable

- ⚠️ Search failed for DS-76: ElementHandle.fill: Element is not attached to the DOM
Call log:
    - fill("")
  - attempting fill action
    - waiting for element to be visible, enabled and editable

- ⚠️ Search failed for DS-77: ElementHandle.fill: Element is not attached to the DOM
Call log:
    - fill("")
  - attempting fill action
    - waiting for element to be visible, enabled and editable

- ⚠️ Search failed for DS-2TD: ElementHandle.fill: Element is not attached to the DOM
Call log:
    - fill("")
  - attempting fill action
    - waiting for element to be visible, enabled and editable

- ⚠️ Search failed for AE-: ElementHandle.fill: Element is not attached to the DOM
Call log:
    - fill("")
  - attempting fill action
    - waiting for element to be visible, enabled and editable



---

## Firmware List

Below is the complete list of archived firmwares, organized by device model and hardware version.

**Total: 0**


