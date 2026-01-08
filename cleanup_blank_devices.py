#!/usr/bin/env python3
"""Clean up blank devices with no firmware files."""
import json
from pathlib import Path
from common import load_json, save_json

def cleanup_blank_devices():
    """Remove devices and firmwares that have no actual files."""
    devices = load_json('devices.json')
    firmwares_live = load_json('firmwares_live.json')
    firmwares_manual = load_json('firmwares_manual.json')
    
    # Get all firmware files that exist
    firmware_dir = Path('firmwares')
    existing_files = set()
    if firmware_dir.exists():
        for file in firmware_dir.glob('*'):
            if file.is_file() and file.suffix in ['.zip', '.dav', '.bin', '.pak']:
                existing_files.add(file.name)
    
    print(f"Found {len(existing_files)} firmware files on disk")
    
    # Group firmwares by device_id
    device_firmwares = {}
    for key, fw in {**firmwares_live, **firmwares_manual}.items():
        device_id = fw.get('device_id')
        if device_id:
            if device_id not in device_firmwares:
                device_firmwares[device_id] = []
            device_firmwares[device_id].append((key, fw))
    
    # Find devices with no files
    devices_to_remove = []
    firmwares_to_remove = []
    
    for device_id, device_info in devices.items():
        device_id_int = int(device_id) if device_id.isdigit() else None
        if device_id_int:
            firmwares_for_device = device_firmwares.get(device_id_int, [])
            
            # Skip if device has no firmwares at all
            if not firmwares_for_device:
                devices_to_remove.append(device_id)
                continue
            
            # Check if any firmware has a filename that exists
            has_files = False
            for fw_key, fw in firmwares_for_device:
                filename = fw.get('filename', '')
                # Check if filename exists in files on disk
                if filename and filename in existing_files:
                    has_files = True
                    break
                # Also check if download_url suggests a real file (not just license agreement page)
                download_url = fw.get('download_url', '')
                if download_url and 'materials-license-agreement' not in download_url:
                    # Has a real download URL (even if file not on disk yet)
                    has_files = True
                    break
            
            if not has_files and len(firmwares_for_device) > 0:
                # Device has firmwares but none have actual files
                devices_to_remove.append(device_id)
                # Also remove all firmwares for this device
                for fw_key, fw in firmwares_for_device:
                    firmwares_to_remove.append(fw_key)
    
    # Remove devices
    for device_id in devices_to_remove:
        del devices[device_id]
        print(f"Removed device: {device_id}")
    
    # Remove firmwares
    for fw_key in firmwares_to_remove:
        if fw_key in firmwares_live:
            del firmwares_live[fw_key]
        if fw_key in firmwares_manual:
            del firmwares_manual[fw_key]
    
    print(f"\nRemoved {len(devices_to_remove)} devices and {len(firmwares_to_remove)} firmwares")
    
    # Save
    save_json('devices.json', devices)
    save_json('firmwares_live.json', firmwares_live)
    save_json('firmwares_manual.json', firmwares_manual)
    
    print("✅ Cleanup complete!")

if __name__ == '__main__':
    cleanup_blank_devices()
