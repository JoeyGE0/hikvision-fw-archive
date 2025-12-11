# Hikvision Firmware Archive

A community-maintained archive of Hikvision camera and NVR firmware files.

## Why This Exists

Hikvision only shows the latest firmware version on their download center. Once a new version is released, older versions disappear. This makes it impossible to:

- Rollback to a previous firmware if a new one causes issues
- See firmware version history for your device
- Access beta or archived firmware versions
- Compare firmware versions

This archive maintains a searchable database of firmware versions with direct download links.

## How It Works

This repository is automatically updated by scraping Hikvision's download center. The scraper:

1. Searches for firmware files across Hikvision's product categories
2. Extracts model numbers, hardware versions, firmware versions, and release dates
3. Stores download links and metadata
4. Generates this README with an organized firmware list
5. Creates GitHub releases when new firmwares are discovered

## Finding Firmware

1. **Search for your device model** (e.g., `DS-2CD2043`)
2. **Match your hardware version** - Critical! Wrong firmware can damage your device
3. **Check version and date** - Newer versions listed first
4. **Click download link** - Most links go directly to Hikvision's servers

## Important Warnings

⚠️ **Before flashing firmware:**

- **Hardware version must match** - Check your device's web interface
- **Beta firmwares are marked** - Use at your own risk
- **Backup your configuration** - Always backup before updating
- **Stable power required** - Use UPS if possible during update
- **No warranty** - This is unofficial, use at your own risk

## Contributing

Found a missing firmware? Have a download link? 

- Open an issue with the model, hardware version, firmware version, and download link
- Or submit a PR adding it to `firmwares_manual.json`

## Firmware List

Total: 0

_Firmware list will appear here once scraping begins_
