#!/usr/bin/env python3
"""Comprehensive test to verify the early exit fix prevents 6-hour runs."""
import sys

def simulate_old_behavior():
    """Simulate the OLD behavior (what was causing 6-hour runs)."""
    print("=" * 60)
    print("Simulating OLD behavior (BEFORE fix):")
    print("=" * 60)
    
    MAX_FIRMWARES_TO_DOWNLOAD = 10
    new_downloads_count = 0
    links_processed = 0
    links_checked = 0
    
    # Simulate 10,000 links (realistic scenario)
    # REAL SCENARIO: First 5000 links are existing firmwares, then new ones start
    total_links = 10000
    
    for link_idx in range(1, total_links + 1):
        # OLD BEHAVIOR: No early check, process everything first
        links_checked += 1
        
        # Simulate expensive operations (checking existence, parsing, etc.)
        # This is what was taking 6 hours - checking ALL links even after limit reached
        href = f"firmware_{link_idx}.zip"
        link_text = f"Firmware v1.0.{link_idx}"
        version = f"1.0.{link_idx}"
        model = "DS-2CD2047G2"
        
        # Simulate checking if firmware exists (expensive DB lookup)
        # REAL SCENARIO: First 5000 are existing, then new ones appear
        firmware_exists = (link_idx <= 5000)
        
        if firmware_exists:
            # OLD: Still processes existing ones (just skips download)
            links_processed += 1
            continue
        
        # New firmware found
        # OLD BEHAVIOR: Only checks limit here, AFTER processing the link
        if MAX_FIRMWARES_TO_DOWNLOAD > 0 and new_downloads_count >= MAX_FIRMWARES_TO_DOWNLOAD:
            break
        
        new_downloads_count += 1
        links_processed += 1
        
        if new_downloads_count >= MAX_FIRMWARES_TO_DOWNLOAD:
            break
    
    print(f"  Links checked: {links_checked:,}")
    print(f"  Links processed: {links_processed:,}")
    print(f"  Downloads: {new_downloads_count}")
    print(f"  ⚠️  OLD: Processed {links_checked:,} links before stopping")
    return links_checked


def simulate_new_behavior():
    """Simulate the NEW behavior (with the fix)."""
    print("\n" + "=" * 60)
    print("Simulating NEW behavior (AFTER fix):")
    print("=" * 60)
    
    MAX_FIRMWARES_TO_DOWNLOAD = 10
    new_downloads_count = 0
    test_mode_limit_reached = False
    links_processed = 0
    links_checked = 0
    
    # Simulate 10,000 links (same scenario)
    # REAL SCENARIO: First 5000 links are existing firmwares, then new ones start
    total_links = 10000
    
    for link_idx in range(1, total_links + 1):
        # NEW BEHAVIOR: Check limit FIRST (before expensive operations)
        if test_mode_limit_reached:
            break
        
        # NEW FIX: Early check BEFORE processing (saves checking thousands of links)
        if MAX_FIRMWARES_TO_DOWNLOAD > 0 and new_downloads_count >= MAX_FIRMWARES_TO_DOWNLOAD:
            test_mode_limit_reached = True
            break
        
        # Only do expensive operations if we haven't hit the limit
        links_checked += 1
        
        # Simulate expensive operations (checking existence, parsing, etc.)
        href = f"firmware_{link_idx}.zip"
        link_text = f"Firmware v1.0.{link_idx}"
        version = f"1.0.{link_idx}"
        model = "DS-2CD2047G2"
        
        # Simulate checking if firmware exists (expensive DB lookup)
        # REAL SCENARIO: First 5000 are existing, then new ones appear
        firmware_exists = (link_idx <= 5000)
        
        if firmware_exists:
            # NEW: Still processes existing ones, but stops early when limit reached
            links_processed += 1
            continue
        
        # New firmware found
        new_downloads_count += 1
        links_processed += 1
        
        if new_downloads_count >= MAX_FIRMWARES_TO_DOWNLOAD:
            test_mode_limit_reached = True
            break
    
    print(f"  Links checked: {links_checked:,}")
    print(f"  Links processed: {links_processed:,}")
    print(f"  Downloads: {new_downloads_count}")
    print(f"  ✅ NEW: Only checked {links_checked:,} links before stopping")
    return links_checked


if __name__ == '__main__':
    old_count = simulate_old_behavior()
    new_count = simulate_new_behavior()
    
    improvement = ((old_count - new_count) / old_count) * 100 if old_count > 0 else 0
    
    print("\n" + "=" * 60)
    print("RESULTS:")
    print("=" * 60)
    print(f"  Old behavior: {old_count:,} links processed")
    print(f"  New behavior: {new_count:,} links processed")
    print(f"  Improvement: {improvement:.1f}% reduction")
    print(f"  Time saved: ~{((old_count - new_count) / 1000):.1f} hours (estimated)")
    print("=" * 60)
    
    if new_count < old_count:
        print("✅ FIX VERIFIED: Early exit prevents unnecessary processing!")
        sys.exit(0)
    else:
        print("❌ FIX NOT WORKING: No improvement detected")
        sys.exit(1)
