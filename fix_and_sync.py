#!/usr/bin/env python3
"""Fix and sync firmware data - run this to fix all existing data."""
import logging
from pathlib import Path

from common import load_json, save_json
from main import HikvisionScraper

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def main():
    """Fix and sync all firmware data."""
    logger.info("=" * 60)
    logger.info("Fixing and syncing firmware data...")
    logger.info("=" * 60)
    
    scraper = HikvisionScraper()
    
    # Step 1: Sync firmware directory with JSON
    logger.info("\n📦 Step 1: Syncing firmware directory with JSON...")
    scraper.sync_firmwares_directory()
    
    # Step 2: Clean up failed downloads
    logger.info("\n🧹 Step 2: Cleaning up failed downloads...")
    scraper.cleanup_failed_downloads()
    
    # Step 3: Clean up empty devices
    logger.info("\n🧹 Step 3: Cleaning up empty devices...")
    scraper.cleanup_empty_devices()
    
    # Step 4: Save everything
    logger.info("\n💾 Step 4: Saving data...")
    scraper.save()
    
    # Step 5: Show summary
    logger.info("\n" + "=" * 60)
    logger.info("📊 Summary:")
    logger.info(f"  • Total devices: {len(scraper.devices)}")
    logger.info(f"  • Total firmwares: {len(scraper.firmwares_live)}")
    
    # Count firmwares with files
    firmware_dir = Path('firmwares')
    firmware_files_count = 0
    if firmware_dir.exists():
        for ext in ['.zip', '.dav', '.pak', '.bin']:
            firmware_files_count += len(list(firmware_dir.glob(f'*{ext}')))
    
    logger.info(f"  • Firmware files in directory: {firmware_files_count}")
    logger.info("=" * 60)
    logger.info("✅ Fix and sync complete!")

if __name__ == '__main__':
    main()
