# Quick Start Guide

Get started with the Hikvision Firmware Archive in minutes.

## Installation

### Prerequisites

- Python 3.11 or higher
- pip (Python package manager)

### Setup Steps

1. **Clone the repository**:

   ```bash
   git clone https://github.com/JoeyGE0/hikvision-fw-archive.git
   cd hikvision-fw-archive
   ```

2. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

   This installs:

   - `requests` - HTTP library for web scraping
   - `beautifulsoup4` - HTML parsing
   - `lxml` - Fast XML/HTML parser
   - `python-dateutil` - Date parsing utilities

3. **Verify installation**:
   ```bash
   python main.py --help
   ```

## Basic Usage

### Scraping Firmwares

Run the scraper to fetch firmwares from Hikvision's website:

```bash
python main.py scrape
```

This will:

- Fetch firmware data from Hikvision's download center
- Extract model numbers, versions, and download links
- Update `devices.json` and `firmwares_live.json`
- Save all data to JSON files

**Note**: The scraper may take several minutes depending on how many products it finds.

### Manually Adding a Firmware

If you have a firmware download link, add it manually:

```bash
python main.py add "https://www.hikvision.com/download/firmware.dav" \
  --model "DS-2CD2XXX" \
  --hw-version "IPC_G0" \
  --version "5.7.0" \
  --date "2023-01-15" \
  --changes "Bug fixes and improvements" \
  --notes "Official release"
```

The tool will try to auto-detect model and version from the filename if you don't provide them.

### Generating the README

Generate the README file from JSON data:

```bash
python release.py
```

This creates `README.md` with an organized list of all firmwares.

## Understanding Hikvision Firmware

### Model Numbers

Hikvision uses consistent naming:

- **DS-2CD** - IP Cameras (fixed dome/bullet)
- **DS-2DE** - PTZ Cameras
- **DS-76XX** - NVRs (various series)
- **DS-77XX** - NVRs (various series)

### Hardware Versions

Critical for compatibility! Examples:

- `IPC_G0` - Generic IP Camera hardware
- `IPC_BXX` - Specific camera hardware version
- `NVR_XXX` - NVR hardware version

Find your hardware version in the device web interface under "Device Information" or "System Information".

### Firmware Versions

Format: `X.Y.Z` (e.g., `5.7.0`)

- Major version (5) - Major feature updates
- Minor version (7) - Feature additions
- Patch version (0) - Bug fixes

### Filename Patterns

Hikvision firmware files often follow patterns:

- `digicap.dav` - Generic name (model in metadata)
- `DS-2CD2XXX_5.7.0_220123.dav` - Model_Version_Date
- `IPC_XXX_5.7.0_220123.dav` - Hardware_Version_Date

## Customizing the Scraper

The scraper searches for firmwares by model prefixes. You can modify `scrape_firmwares()` in `main.py` to:

1. **Add more model prefixes**:

   ```python
   common_prefixes = [
       'DS-2CD',  # IP Cameras
       'DS-2DE',  # PTZ Cameras
       'DS-76',   # NVRs
       'YOUR-PREFIX',  # Add your own
   ]
   ```

2. **Adjust search patterns**: Modify `extract_model_from_filename()` and `extract_version_from_filename()` to handle different filename formats.

3. **Add rate limiting**: The scraper already includes delays, but you can adjust them:
   ```python
   time.sleep(2)  # Increase delay between requests
   ```

## Troubleshooting

### Scraper Finds No Firmwares

- **Check internet connection**: The scraper needs to access Hikvision's website
- **Verify website structure**: Hikvision may have changed their site layout
- **Check logs**: Look for error messages in the output
- **Try manual addition**: Use `python main.py add` for specific firmwares

### Invalid JSON Errors

If JSON files become corrupted:

1. Check file syntax with a JSON validator
2. Restore from git history: `git checkout devices.json`
3. Re-run scraper to regenerate data

### Missing Dependencies

If you get import errors:

```bash
pip install --upgrade -r requirements.txt
```

### Firmware Detection Issues

The scraper tries to auto-detect model/version from filenames. If it fails:

- Manually add firmwares with `--model` and `--version` flags
- Improve detection patterns in `extract_model_from_filename()` and `extract_version_from_filename()`

## Next Steps

- **Contribute**: See [CONTRIBUTING.md](CONTRIBUTING.md) for how to help
- **Report Issues**: Open an issue if you find problems
- **Improve Scraper**: Help make the scraper more robust
- **Add Firmwares**: Share firmware links you find

## Resources

- [Hikvision Official Download Center](https://www.hikvision.com/en/support/download/firmware/)
- [Hikvision Support](https://www.hikvision.com/en/support/)
- [SADP Tool](https://www.hikvision.com/en/support/download/tools/) - Device discovery and firmware upload tool
