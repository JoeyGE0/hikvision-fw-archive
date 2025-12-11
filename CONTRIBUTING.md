# Contributing to Hikvision Firmware Archive

Thank you for your interest in contributing! Here's how you can help:

## Reporting Missing Firmwares

If you know of a firmware that's not in the archive:

1. Check if it's already listed in `missing.txt`
2. If not, add it to `missing.txt` with format:
   ```
   Model Name - Hardware Version - Firmware Version - Date (if known)
   ```
3. Open an issue or discussion with details

## Adding Firmwares Manually

If you have a firmware download link:

1. Fork the repository
2. Use the `add` command:
   ```bash
   python main.py add <url> --model "DS-2CD2XXX" --hw-version "IPC_XXX" --version "5.7.0" --date "2023-01-01" --changes "Bug fixes" --notes "Official release"
   ```
3. Generate updated README:
   ```bash
   python release.py
   ```
4. Submit a pull request

## Improving the Scraper

The scraper in `main.py` needs to be adapted to Hikvision's actual website structure. To help:

1. Inspect Hikvision's download center HTML structure
2. Update the `extract_firmware_info()` method in `main.py`
3. Update the `scrape_firmwares()` method to navigate their site
4. Test and submit a PR

## Code Style

- Follow PEP 8
- Use type hints where possible
- Add docstrings to functions
- Keep functions focused and small

## Questions?

Open a discussion or issue if you have questions!
