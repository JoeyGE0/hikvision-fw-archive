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
    status = load_json('status.json')
    if not status:
        status = {
            'status': 'unknown',
            'last_run': 'Never',
            'firmwares_found': 0,
            'new_firmwares': 0,
            'test_mode': False,
            'errors': []
        }
    
    # Merge manual firmwares into live firmwares
    all_firmwares = {**firmwares_live, **firmwares_manual}
    
    # Group firmwares by device
    device_firmwares = defaultdict(list)
    device_info_map = {}  # Map device_id to device info (from devices.json or firmware data)
    
    for firmware_key, firmware_data in all_firmwares.items():
        device_id = firmware_data.get('device_id')
        if device_id:
            device_firmwares[device_id].append(firmware_data)
            # Store device info from firmware if not in devices.json
            if device_id not in device_info_map:
                device_info_map[device_id] = {
                    'model': firmware_data.get('model', 'Unknown'),
                    'hardware_version': firmware_data.get('hardware_version', '')
                }
    
    # Also add devices from devices.json
    for device_id, device_info in devices.items():
        device_id_int = int(device_id) if device_id.isdigit() else None
        if device_id_int and device_id_int not in device_info_map:
            device_info_map[device_id_int] = device_info
    
    # Load readme header
    readme_header = Path('readme_header.md').read_text(encoding='utf-8')
    
    # Generate status section
    status_text = status.get('status', 'unknown')
    last_run = status.get('last_run', 'Never')
    firmwares_found = status.get('firmwares_found', 0)
    new_firmwares = status.get('new_firmwares', 0)
    test_mode = status.get('test_mode', False)
    errors = status.get('errors', [])
    
    # Format status with emoji
    status_emoji = {
        'success': '✅',
        'error': '❌',
        'no_new_firmwares': '⚠️',
        'unknown': '❓'
    }.get(status_text, '❓')
    
    # Format last run time
    if last_run and last_run != 'Never':
        try:
            from datetime import datetime
            dt = datetime.fromisoformat(last_run.replace('Z', '+00:00'))
            last_run = dt.strftime('%Y-%m-%d %H:%M:%S UTC')
        except:
            pass
    
    # Format errors
    errors_text = ''
    if errors:
        errors_text = '\n\n**Recent Errors:**\n'
        for error in errors[-5:]:  # Show last 5 errors
            errors_text += f"- ⚠️ {error}\n"
    
    # Replace status placeholders
    readme_header = readme_header.replace('{{STATUS}}', f'{status_emoji} {status_text.upper()}')
    readme_header = readme_header.replace('{{LAST_RUN}}', last_run)
    readme_header = readme_header.replace('{{FIRMWARES_FOUND}}', str(firmwares_found))
    readme_header = readme_header.replace('{{NEW_FIRMWARES}}', str(new_firmwares))
    readme_header = readme_header.replace('{{TEST_MODE}}', '🧪 Enabled' if test_mode else 'Disabled')
    readme_header = readme_header.replace('{{ERRORS}}', errors_text)
    
    # Generate firmware list
    firmware_sections = []
    total_count = 0
    
    # Sort device IDs by model name
    sorted_device_ids = sorted(
        device_firmwares.keys(),
        key=lambda did: (
            device_info_map.get(did, {}).get('model', ''),
            device_info_map.get(did, {}).get('hardware_version', '')
        )
    )
    
    for device_id in sorted_device_ids:
        device_info = device_info_map.get(device_id, {})
        model = device_info.get('model', 'Unknown')
        hardware_version = device_info.get('hardware_version', '')
        
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
        
        # Create table with supported models column
        section += "| Version | Supported Models | Date | Download | Notes |\n"
        section += "| ------- | ---------------- | ---- | -------- | ----- |\n"
        
        for firmware in firmwares:
            version = firmware.get('version', '')
            date = firmware.get('date', '')
            changes = firmware.get('changes', '')
            notes = firmware.get('notes', '')
            download_url = firmware.get('download_url', '')
            filename = firmware.get('filename', '')
            supported_models = firmware.get('supported_models', [])
            is_beta = firmware.get('is_beta', False)
            
            # Format download link - prefer GitHub release if filename exists
            github_repo = "JoeyGE0/hikvision-fw-archive"
            if filename:
                # Link to latest release download (since makeLatest: true in workflow)
                firmware_download_url = f"https://github.com/{github_repo}/releases/latest/download/{filename}"
                download_link = f"[📥 Download]({firmware_download_url})"
            elif download_url:
                # Fallback to Hikvision URL
                firmware_download_url = download_url
                download_link = f"[🔗 Link]({download_url})"
            else:
                firmware_download_url = ""
                download_link = "—"
            
            # Format supported models - prefer "Applied to:" text if available
            # Make model names clickable links to the firmware download
            applied_to = firmware.get('applied_to', '')
            if applied_to and firmware_download_url:
                # Extract model names from "Applied to:" text and make them links
                # Pattern: "Applied to: DS-1200KI(B)" or "Applied to: DS-2CD2047G2-LU/SL(2.8mm)(C)"
                import re
                # Find all model patterns (DS-xxx, AE-xxx, IDS-xxx)
                model_pattern = r'(DS-[0-9A-Z-]+(?:[/-][A-Z0-9]+)*(?:\([^)]+\))?|AE-[0-9A-Z-]+(?:[/-][A-Z0-9]+)*(?:\([^)]+\))?|IDS-[0-9A-Z-]+(?:[/-][A-Z0-9]+)*(?:\([^)]+\))?)'
                models_found = re.findall(model_pattern, applied_to, re.IGNORECASE)
                
                if models_found:
                    # Replace each model name with a clickable link
                    models_text = applied_to
                    for model_name in models_found:
                        # Create link: [model_name](download_url)
                        linked_model = f"[{model_name}]({firmware_download_url})"
                        # Replace the model name with the linked version
                        models_text = models_text.replace(model_name, linked_model, 1)
                else:
                    # No models found, use text as-is
                    models_text = applied_to
            elif applied_to:
                # Have "Applied to:" text but no download URL yet
                models_text = applied_to
            elif supported_models and len(supported_models) > 0:
                # Show up to 3 models, then "and X more" if there are more
                if firmware_download_url:
                    # Make model names clickable
                    linked_models = [f"[{m}]({firmware_download_url})" for m in supported_models[:3]]
                    if len(supported_models) <= 3:
                        models_text = ', '.join(linked_models)
                    else:
                        models_text = ', '.join(linked_models) + f', and {len(supported_models) - 3} more'
                else:
                    if len(supported_models) <= 3:
                        models_text = ', '.join(supported_models)
                    else:
                        models_text = ', '.join(supported_models[:3]) + f', and {len(supported_models) - 3} more'
            else:
                # Fallback to primary model
                if firmware_download_url:
                    models_text = f"[{model}]({firmware_download_url})"
                else:
                    models_text = model
            
            # Format version
            version_link = version
            
            # Add beta warning
            if is_beta:
                notes = f"⚠️ Beta firmware. {notes}".strip()
            
            # Escape pipe characters in content
            changes = changes.replace('|', '\\|')
            notes = notes.replace('|', '\\|')
            models_text = models_text.replace('|', '\\|')
            
            section += f"| {version_link} | {models_text} | {date} | {download_link} | {notes} |\n"
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
