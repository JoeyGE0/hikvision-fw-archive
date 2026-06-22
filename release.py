#!/usr/bin/env python3
"""Generate README and create releases for Hikvision firmware archive."""
from __future__ import annotations

import json
import logging
import re
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional

from common import (
    HIKVISION_MODEL_PATTERN,
    load_json,
    normalize_product_model,
    parse_version,
    save_json,
)

GITHUB_REPO = 'JoeyGE0/hikvision-fw-archive'
ARCHIVE_RELEASES_URL = f'https://github.com/{GITHUB_REPO}/releases'
LICENSE_URL = 'https://www.hikvision.com/en/policies/materials-license-agreement/'

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
    scraper_mode = status.get('scraper_mode', 'http')
    catalog_fetch = status.get('catalog_fetch', 'unknown')
    catalog_entries = status.get('catalog_entries', 0)
    errors = status.get('errors', [])
    
    # Format status with emoji
    status_emoji = {
        'success': '✅',
        'error': '❌',
        'no_new_firmwares': '⚠️',
        'running': '🔄',
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
    readme_header = readme_header.replace('{{SCRAPER_MODE}}', scraper_mode.upper())
    readme_header = readme_header.replace('{{CATALOG_FETCH}}', str(catalog_fetch))
    readme_header = readme_header.replace('{{CATALOG_ENTRIES}}', str(catalog_entries))
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
        
        # Create collapsible section using HTML details/summary for better organization
        # This allows thousands of firmwares to be organized in dropdowns
        section = f"\n<details>\n<summary><h2>{model}"
        if hardware_version:
            section += f" - {hardware_version}"
        section += f" ({len(firmwares)} firmwares)</h2></summary>\n\n"
        
        # Create table with supported models column
        section += "| Version | Supported Models | Date | Download | Notes |\n"
        section += "| ------- | ---------------- | ---- | -------- | ----- |\n"
        
        for firmware in firmwares:
            version = firmware.get('version', '')
            date = firmware.get('date', '')
            download_url = firmware.get('download_url', '')
            filename = firmware.get('filename', '')
            supported_models = firmware.get('supported_models', [])
            is_beta = firmware.get('is_beta', False)
            
            # Format download link - prefer download_url from JSON (stable) over building latest URL
            github_repo = "JoeyGE0/hikvision-fw-archive"
            if download_url:
                # Use the download_url from JSON (should be stable release URL or Hikvision URL)
                firmware_download_url = download_url
                # Check if it's a GitHub release URL to determine link style
                if 'github.com' in download_url and '/releases/download/' in download_url:
                    download_link = f"[📥 Download]({firmware_download_url})"
                elif 'github.com' in download_url:
                    # Fallback for any other GitHub URL format
                    download_link = f"[📥 Download]({firmware_download_url})"
                else:
                    # Hikvision or other external URL
                    download_link = f"[🔗 Link]({firmware_download_url})"
            elif filename:
                # No download_url but have filename - build latest URL as last resort
                firmware_download_url = f"https://github.com/{github_repo}/releases/latest/download/{filename}"
                download_link = f"[📥 Download]({firmware_download_url})"
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
            
            # Notes column: short changes summary + optional PDF link
            notes_display = format_firmware_notes_summary(firmware)
            
            # Add beta warning
            if is_beta:
                notes_display = f"⚠️ Beta firmware. {notes_display}".strip()
            if not notes_display:
                notes_display = '—'
            
            # Escape pipe characters in content
            notes_display = notes_display.replace('|', '\\|')
            models_text = models_text.replace('|', '\\|')
            
            section += f"| {version_link} | {models_text} | {date} | {download_link} | {notes_display} |\n"
            total_count += 1
        
        # Close the details tag
        section += "\n</details>\n"
        
        firmware_sections.append(section)
    
    # Combine header and firmware list
    readme_content = readme_header.replace('Total: 0', f'Total: {total_count}')
    readme_content += '\n\n' + '\n'.join(firmware_sections)
    
    return readme_content


def github_release_page_url(download_url: str | None) -> str | None:
    """Map /releases/download/{tag}/file.zip to the release page for that tag."""
    url = (download_url or '').strip()
    match = re.search(rf'github\.com/{re.escape(GITHUB_REPO)}/releases/download/([^/]+)/', url)
    if match:
        return f'https://github.com/{GITHUB_REPO}/releases/tag/{match.group(1)}'
    return None


def index_models_for_firmware(firmware: Dict[str, Any]) -> List[str]:
    """Return normalized model keys that should resolve to this firmware row.

    Only ``model`` and models parsed from ``applied_to`` are indexed. The catalog
    ``supported_models`` list is often broader than the release-note ``applied_to``
    line and has caused wrong packages (e.g. DS-2CD1383G2 on a DS-2CD1063G2 build).
    """
    models: List[str] = []
    seen: set[str] = set()
    applied_models: set[str] = set()

    def add(raw: str) -> None:
        key = normalize_product_model(raw)
        if not key or key == 'UNKNOWN' or key in seen:
            return
        seen.add(key)
        models.append(key)

    applied_to = firmware.get('applied_to', '') or ''
    for match in re.findall(HIKVISION_MODEL_PATTERN, applied_to, re.IGNORECASE):
        applied_models.add(normalize_product_model(match))

    add(firmware.get('model', ''))
    for match in applied_models:
        add(match)

    # Fallback when Hikvision omits applied_to (manual rows, legacy scrapes).
    if not applied_models:
        for supported in firmware.get('supported_models') or []:
            add(str(supported))

    return models


def ha_firmware_record(firmware: Dict[str, Any]) -> Dict[str, Any]:
    """Shape one archive row for Home Assistant / API consumers."""
    download_url = (firmware.get('download_url') or '').strip()
    notes = (firmware.get('notes') or '').strip()
    changes = (firmware.get('changes') or '').strip()
    release_page = github_release_page_url(download_url) or ARCHIVE_RELEASES_URL
    return {
        'model': firmware.get('model', ''),
        'hardware_version': (firmware.get('hardware_version') or 'UNKNOWN').strip(),
        'version': firmware.get('version', ''),
        'date': firmware.get('date', ''),
        'filename': firmware.get('filename', ''),
        'download_url': download_url,
        'applied_to': firmware.get('applied_to', ''),
        'changes': changes,
        'notes': notes,
        'notes_pdf_url': notes if notes.startswith('http') else '',
        'release_page_url': release_page,
        'license_url': LICENSE_URL,
        'archive_url': f'https://github.com/{GITHUB_REPO}',
    }


def generate_firmware_index() -> Dict[str, Any]:
    """Build model → best firmware metadata index for integrations (e.g. Home Assistant)."""
    firmwares_live = load_json('firmwares_live.json')
    firmwares_manual = load_json('firmwares_manual.json')
    all_firmwares = {**firmwares_live, **firmwares_manual}

    # model -> list of HA records (one per archive row that references the model)
    by_model: Dict[str, List[Dict[str, Any]]] = defaultdict(list)
    for firmware in all_firmwares.values():
        if not isinstance(firmware, dict):
            continue
        if not firmware.get('version') or not firmware.get('download_url'):
            continue
        record = ha_firmware_record(firmware)
        for model_key in index_models_for_firmware(firmware):
            by_model[model_key].append(record)

    models_index: Dict[str, Any] = {}
    for model_key, records in by_model.items():
        records.sort(key=lambda r: parse_version(r.get('version', '0')), reverse=True)
        by_hw: Dict[str, List[Dict[str, Any]]] = defaultdict(list)
        for record in records:
            hw = (record.get('hardware_version') or 'UNKNOWN').upper()
            by_hw[hw].append(record)
        hw_latest = {
            hw: sorted(rows, key=lambda r: parse_version(r.get('version', '0')), reverse=True)[0]
            for hw, rows in by_hw.items()
        }
        models_index[model_key] = {
            'latest': records[0],
            'by_hardware_version': hw_latest,
            'all_versions': records,
        }

    return {
        'schema_version': 1,
        'generated_at': datetime.now(timezone.utc).isoformat(),
        'archive_releases_url': ARCHIVE_RELEASES_URL,
        'license_url': LICENSE_URL,
        'models': models_index,
    }


def format_firmware_notes_summary(firmware: Dict) -> str:
    """Short changes text plus optional release-note PDF link (matches README Notes column)."""
    changes = (firmware.get('changes') or '').strip()
    notes = (firmware.get('notes') or '').strip()
    parts: List[str] = []
    if changes:
        parts.append(changes)
    if notes.startswith('http'):
        parts.append(f'[📄 Release Notes]({notes})')
    return ' · '.join(parts)


def generate_release_body(firmware_files: List[str]) -> str:
    """Generate release body with device info and download links.
    
    Args:
        firmware_files: List of firmware filenames in this release
        
    Returns:
        Markdown formatted release body
    """
    firmwares_live = load_json('firmwares_live.json')
    firmwares_manual = load_json('firmwares_manual.json')
    all_firmwares = {**firmwares_live, **firmwares_manual}
    
    # Find firmwares that match the uploaded files
    release_firmwares = []
    for filename in firmware_files:
        for key, fw in all_firmwares.items():
            if fw.get('filename') == filename:
                release_firmwares.append(fw)
                break
    
    if not release_firmwares:
        return "Automated firmware archive update.\n\nNew firmwares may have been added. Check the README for details."
    
    # Build release body
    body = "## Firmware Updates\n\n"
    body += "This release includes the following firmware files:\n\n"
    
    github_repo = "JoeyGE0/hikvision-fw-archive"
    license_url = "https://www.hikvision.com/en/policies/materials-license-agreement/"
    
    for fw in release_firmwares:
        model = fw.get('model', 'Unknown')
        version = fw.get('version', '')
        date = fw.get('date', '')
        filename = fw.get('filename', '')
        applied_to = fw.get('applied_to', '')
        supported_models = fw.get('supported_models', [])
        
        # Format device info
        if applied_to:
            device_info = applied_to
        elif supported_models:
            device_info = ', '.join(supported_models[:5])
            if len(supported_models) > 5:
                device_info += f', and {len(supported_models) - 5} more'
        else:
            device_info = model
        
        # Prefer stable tag URL from JSON (latest/download 404s when file is on an older release)
        stored_url = (fw.get('download_url') or '').strip()
        if stored_url and '/releases/download/' in stored_url and '/latest/download/' not in stored_url:
            download_url = stored_url
        elif filename:
            download_url = f"https://github.com/{github_repo}/releases/latest/download/{filename}"
        else:
            download_url = ''
        if download_url:
            download_link = f"[📥 Download {filename or 'firmware'}]({download_url})"
        else:
            download_link = "Link not available"
        
        notes_summary = format_firmware_notes_summary(fw)

        body += f"### {model} - v{version}\n\n"
        body += f"- **Supported Devices:** {device_info}\n"
        if date:
            body += f"- **Release Date:** {date}\n"
        body += f"- **Download:** {download_link}\n"
        if notes_summary:
            body += f"- **Changes:** {notes_summary}\n"
        body += "\n"
    
    body += f"---\n\n"
    body += f"⚠️ **Important:** By downloading and using these firmware files, you agree to be bound by the [Hikvision Materials License Agreement]({license_url}).\n\n"
    body += "Please read the agreement before downloading or using any firmware files."
    
    return body


def main():
    """Generate README and integration index files."""
    logger.info("Generating README...")
    readme_content = generate_readme()

    output_file = Path('README.md')
    output_file.write_text(readme_content, encoding='utf-8')
    logger.info(f"README generated: {output_file}")

    logger.info("Generating firmware_index.json for integrations...")
    index = generate_firmware_index()
    save_json('firmware_index.json', index)
    logger.info(
        "firmware_index.json generated (%s models)",
        len(index.get('models', {})),
    )

    # Count total firmwares
    firmwares_live = load_json('firmwares_live.json')
    firmwares_manual = load_json('firmwares_manual.json')
    total = len(firmwares_live) + len(firmwares_manual)
    logger.info(f"Total firmwares: {total}")


if __name__ == '__main__':
    main()
