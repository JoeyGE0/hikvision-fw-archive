#!/usr/bin/env python3
"""Generate README and create releases for Hikvision firmware archive."""
import json
import logging
from collections import defaultdict
from datetime import datetime
from pathlib import Path
from typing import Dict, List

from common import load_json, parse_version

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def generate_readme() -> str:
    """Generate README content from JSON data."""
    devices = load_json('devices.json')
    firmwares_live = load_json('firmwares_live.json')
    firmwares_manual = load_json('firmwares_manual.json')
    firmware_info = load_json('firmware_info.json')
    
    # Merge manual firmwares into live firmwares
    all_firmwares = {**firmwares_live, **firmwares_manual}
    
    # Group firmwares by device
    device_firmwares = defaultdict(list)
    for firmware_key, firmware_data in all_firmwares.items():
        device_id = firmware_data.get('device_id')
        if device_id:
            device_firmwares[device_id].append(firmware_data)
    
    # Load readme header
    readme_header = Path('readme_header.md').read_text(encoding='utf-8')
    
    # Generate firmware list
    firmware_sections = []
    total_count = 0
    
    # Sort devices by model name
    sorted_devices = sorted(
        devices.items(),
        key=lambda x: (x[1].get('model', ''), x[1].get('hardware_version', ''))
    )
    
    for device_id, device_info in sorted_devices:
        model = device_info.get('model', 'Unknown')
        hardware_version = device_info.get('hardware_version', '')
        
        if device_id not in device_firmwares:
            continue
        
        firmwares = device_firmwares[device_id]
        
        # Sort firmwares by date (descending), then version (descending)
        firmwares.sort(
            key=lambda f: (
                f.get('date', ''),
                parse_version(f.get('version', ''))
            ),
            reverse=True
        )
        
        # Create section header
        section = f"\n## {model}"
        if hardware_version:
            section += f"\n\n### {hardware_version}"
        section += f"\n\nFirmwares for this hardware version: {len(firmwares)}\n\n"
        
        # Create table
        section += "| Version | Date | Changes | Notes |\n"
        section += "| ------- | ---- | ------- | ----- |\n"
        
        for firmware in firmwares:
            version = firmware.get('version', '')
            date = firmware.get('date', '')
            changes = firmware.get('changes', '')
            notes = firmware.get('notes', '')
            download_url = firmware.get('download_url', '')
            is_beta = firmware.get('is_beta', False)
            
            # Format version with link if URL exists
            if download_url:
                version_link = f"[{version}]({download_url})"
            else:
                version_link = version
            
            # Add beta warning
            if is_beta:
                notes = f"⚠️ Beta firmware. {notes}".strip()
            
            # Escape pipe characters in content
            changes = changes.replace('|', '\\|')
            notes = notes.replace('|', '\\|')
            
            section += f"| {version_link} | {date} | {changes} | {notes} |\n"
            total_count += 1
        
        firmware_sections.append(section)
    
    # Combine header and firmware list
    readme_content = readme_header.replace('Total: 0', f'Total: {total_count}')
    readme_content += '\n\n' + '\n'.join(firmware_sections)
    
    return readme_content


def main():
    """Generate README file."""
    logger.info("Generating README...")
    readme_content = generate_readme()
    
    output_file = Path('README.md')
    output_file.write_text(readme_content, encoding='utf-8')
    logger.info(f"README generated: {output_file}")
    
    # Count total firmwares
    firmwares_live = load_json('firmwares_live.json')
    firmwares_manual = load_json('firmwares_manual.json')
    total = len(firmwares_live) + len(firmwares_manual)
    logger.info(f"Total firmwares: {total}")


if __name__ == '__main__':
    main()
