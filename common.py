"""Common utilities for Hikvision firmware archive."""
import json
import os
import re
from datetime import datetime
from typing import Any, Dict, List, Optional


def load_json(filepath: str) -> Dict[str, Any]:
    """Load JSON file, return empty dict if file doesn't exist."""
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {}


def save_json(filepath: str, data: Dict[str, Any]) -> None:
    """Save data to JSON file."""
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def merge_dicts(base: Dict[str, Any], new: Dict[str, Any]) -> Dict[str, Any]:
    """Merge new dict into base dict, preserving existing keys."""
    result = base.copy()
    for key, value in new.items():
        if key not in result:
            result[key] = value
        elif isinstance(value, dict) and isinstance(result[key], dict):
            result[key] = merge_dicts(result[key], value)
        elif isinstance(value, list) and isinstance(result[key], list):
            # Merge lists, avoiding duplicates
            existing_ids = {item.get('id') for item in result[key] if isinstance(item, dict) and 'id' in item}
            for item in value:
                if isinstance(item, dict) and item.get('id') not in existing_ids:
                    result[key].append(item)
    return result


def parse_version(version_str: str) -> tuple:
    """Parse Hikvision version string into tuple for comparison.
    
    Handles various Hikvision version formats:
    - "V5.7.0" -> (5, 7, 0)
    - "5.7.0" -> (5, 7, 0)
    - "5.7.0 build 220123" -> (5, 7, 0)
    - "V5.7.0_220123" -> (5, 7, 0)
    """
    try:
        # Remove 'V' prefix, build info, and date suffixes
        version_str = version_str.upper().replace('V', '').strip()
        # Remove build date suffixes (e.g., "_220123" or " build 220123")
        version_str = re.sub(r'[\s_]build[\s_]\d+', '', version_str)
        version_str = re.sub(r'_\d{6,8}$', '', version_str)
        # Split by dots
        parts = version_str.split('.')
        return tuple(int(part) for part in parts)
    except (ValueError, AttributeError):
        return (0, 0, 0)


def format_date(date_str: str) -> str:
    """Format date string to YYYY-MM-DD format.
    
    Handles Hikvision date formats:
    - YYYY-MM-DD (standard)
    - YYMMDD (common in filenames, e.g., 220123 -> 2022-01-23)
    - YYYYMMDD (e.g., 20220123 -> 2022-01-23)
    - Various slash formats
    """
    if not date_str:
        return ''
    
    try:
        # Handle YYMMDD format (common in Hikvision filenames)
        if len(date_str) == 6 and date_str.isdigit():
            year = '20' + date_str[:2]
            month = date_str[2:4]
            day = date_str[4:6]
            return f"{year}-{month}-{day}"
        
        # Handle YYYYMMDD format
        if len(date_str) == 8 and date_str.isdigit():
            year = date_str[:4]
            month = date_str[4:6]
            day = date_str[6:8]
            return f"{year}-{month}-{day}"
        
        # Try various date formats
        for fmt in ['%Y-%m-%d', '%Y/%m/%d', '%d/%m/%Y', '%m/%d/%Y', '%Y%m%d', '%d-%m-%Y']:
            try:
                dt = datetime.strptime(date_str, fmt)
                return dt.strftime('%Y-%m-%d')
            except ValueError:
                continue
        return date_str
    except Exception:
        return date_str


def get_device_id(devices: Dict[str, Any], model: str, hardware_version: str) -> Optional[int]:
    """Get device ID from devices.json for given model and hardware version."""
    for device_id, device_info in devices.items():
        if (device_info.get('model') == model and 
            device_info.get('hardware_version') == hardware_version):
            return int(device_id)
    return None


def create_device_id(devices: Dict[str, Any], model: str, hardware_version: str) -> int:
    """Create a new device ID for model and hardware version."""
    # Find the highest existing ID
    max_id = 0
    for device_id in devices.keys():
        try:
            max_id = max(max_id, int(device_id))
        except ValueError:
            continue
    
    # Start from 100000 for new devices
    new_id = max(100000, max_id + 1)
    devices[str(new_id)] = {
        'model': model,
        'hardware_version': hardware_version
    }
    return new_id


def normalize_model_name(model: str) -> str:
    """Normalize model name for consistent storage."""
    # Remove extra spaces, standardize formatting
    return ' '.join(model.split())


def is_beta_firmware(version: str, notes: str = '') -> bool:
    """Check if firmware is beta based on version string or notes."""
    version_lower = version.lower()
    notes_lower = notes.lower()
    beta_indicators = ['beta', 'test', 'alpha', 'rc', 'preview']
    return any(indicator in version_lower or indicator in notes_lower 
               for indicator in beta_indicators)
