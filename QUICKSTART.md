# Quick Start Guide

## Setup

1. **Clone the repository:**

   ```bash
   git clone https://github.com/YOUR_USERNAME/hikvision-fw-archive.git
   cd hikvision-fw-archive
   ```

2. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Make scripts executable (optional):**
   ```bash
   chmod +x main.py release.py
   ```

## Basic Usage

### Scraping Firmwares

**Note:** The scraper needs to be customized for Hikvision's actual website structure. Currently it's a skeleton that you'll need to adapt.

```bash
python main.py scrape
```

This will:

- Fetch firmware data from Hikvision's download center
- Update `devices.json` and `firmwares_live.json`
- Save the data

### Manually Adding a Firmware

```bash
python main.py add "https://example.com/firmware.zip" \
  --model "DS-2CD2XXX" \
  --hw-version "IPC_XXX" \
  --version "5.7.0" \
  --date "2023-01-01" \
  --changes "Bug fixes and improvements" \
  --notes "Official release"
```

### Generating README

```bash
python release.py
```

This generates the `README.md` file from the JSON data files.

## Customizing the Scraper

The scraper in `main.py` needs to be adapted to Hikvision's website. Here's what you need to do:

1. **Inspect Hikvision's download center:**

   - Visit https://www.hikvision.com/en/support/download/firmware/
   - Use browser dev tools to inspect the HTML structure
   - Note how firmware information is displayed

2. **Update `extract_firmware_info()` method:**

   - This method should extract firmware data from HTML elements
   - You'll need to find the correct CSS selectors or XPath expressions

3. **Update `scrape_firmwares()` method:**
   - Implement navigation through product categories
   - Handle pagination if needed
   - Extract firmware links and metadata

## Example: Adding Firmware Data Structure

The JSON structure for firmwares looks like this:

```json
{
  "DS-2CD2XXX_IPC_XXX_5.7.0": {
    "device_id": 100001,
    "model": "DS-2CD2XXX",
    "hardware_version": "IPC_XXX",
    "version": "5.7.0",
    "date": "2023-01-01",
    "download_url": "https://example.com/firmware.zip",
    "changes": "Bug fixes and improvements",
    "notes": "Official release",
    "is_beta": false,
    "source": "live"
  }
}
```

## Testing

Test the scraper locally before setting up automation:

```bash
# Test scraping (will fail until you customize it)
python main.py scrape

# Test manual add
python main.py add "https://example.com/test.zip" --model "TEST" --hw-version "TEST" --version "1.0.0"

# Generate README to see results
python release.py
```

## Next Steps

1. Customize the scraper for Hikvision's website structure
2. Test locally
3. Push to GitHub
4. GitHub Actions will run automatically twice daily
5. Monitor and improve based on results
