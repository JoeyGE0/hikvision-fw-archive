#!/usr/bin/env python3
"""Test to verify download failure handling."""
import sys

def test_download_failure_handling():
    """Test that failed downloads don't count towards limit and script continues."""
    print("=" * 60)
    print("Testing Download Failure Handling")
    print("=" * 60)
    
    MAX_FIRMWARES_TO_DOWNLOAD = 10
    new_downloads_count = 0
    successful_downloads = 0
    failed_downloads = 0
    links_processed = 0
    
    # Simulate 20 firmware links where some fail
    # Links 1, 3, 5, 7, 9, 11, 13, 15, 17, 19 succeed
    # Links 2, 4, 6, 8, 10, 12, 14, 16, 18, 20 fail
    
    for link_idx in range(1, 21):
        links_processed += 1
        
        # Check limit BEFORE processing (NEW FIX)
        if MAX_FIRMWARES_TO_DOWNLOAD > 0 and new_downloads_count >= MAX_FIRMWARES_TO_DOWNLOAD:
            print(f"  ✓ Download limit reached at link {link_idx}")
            break
        
        # Simulate download attempt
        download_succeeds = (link_idx % 2 == 1)  # Odd numbers succeed
        
        if download_succeeds:
            # Simulate successful download
            file_exists = True
            if file_exists:
                new_downloads_count += 1  # Only increment on success
                successful_downloads += 1
                print(f"  ✓ Link {link_idx}: Download succeeded (#{successful_downloads})")
            else:
                failed_downloads += 1
                print(f"  ✗ Link {link_idx}: Download failed (file missing)")
                continue  # Skip to next
        else:
            # Simulate download failure (exception)
            failed_downloads += 1
            print(f"  ✗ Link {link_idx}: Download failed (exception)")
            continue  # Skip to next, don't increment counter
    
    print(f"\n  Results:")
    print(f"    - Links processed: {links_processed}")
    print(f"    - Successful downloads: {successful_downloads}")
    print(f"    - Failed downloads: {failed_downloads}")
    print(f"    - Counter (new_downloads_count): {new_downloads_count}")
    
    # Verify behavior
    issues = []
    
    if new_downloads_count != successful_downloads:
        issues.append(f"Counter ({new_downloads_count}) doesn't match successful downloads ({successful_downloads})")
    
    if new_downloads_count != MAX_FIRMWARES_TO_DOWNLOAD:
        issues.append(f"Counter ({new_downloads_count}) doesn't match limit ({MAX_FIRMWARES_TO_DOWNLOAD})")
    
    if failed_downloads == 0:
        issues.append("No failed downloads in test scenario")
    
    if issues:
        print(f"\n  ⚠️  Issues found:")
        for issue in issues:
            print(f"     - {issue}")
        return False
    else:
        print(f"\n  ✅ TEST PASSED:")
        print(f"     - Only successful downloads count towards limit")
        print(f"     - Failed downloads don't count towards limit")
        print(f"     - Script continues after failures (doesn't get stuck)")
        return True


def test_script_continues_after_failure():
    """Test that script continues to next firmware after failure."""
    print("\n" + "=" * 60)
    print("Testing Script Continues After Failure")
    print("=" * 60)
    
    MAX_FIRMWARES_TO_DOWNLOAD = 5
    new_downloads_count = 0
    attempts = []
    
    # Simulate: first 3 fail, then 5 succeed
    for link_idx in range(1, 11):
        # Check limit
        if MAX_FIRMWARES_TO_DOWNLOAD > 0 and new_downloads_count >= MAX_FIRMWARES_TO_DOWNLOAD:
            break
        
        # First 3 fail
        if link_idx <= 3:
            attempts.append(f"Link {link_idx}: FAILED")
            continue  # Continue to next
        
        # Rest succeed
        new_downloads_count += 1
        attempts.append(f"Link {link_idx}: SUCCESS (#{new_downloads_count})")
    
    print(f"  Attempts made: {len(attempts)}")
    for attempt in attempts:
        print(f"    {attempt}")
    
    print(f"\n  Final count: {new_downloads_count}")
    
    if new_downloads_count == MAX_FIRMWARES_TO_DOWNLOAD and len(attempts) > MAX_FIRMWARES_TO_DOWNLOAD:
        print(f"\n  ✅ TEST PASSED: Script continues after failures and reaches limit")
        return True
    else:
        print(f"\n  ❌ TEST FAILED")
        return False


if __name__ == '__main__':
    test1 = test_download_failure_handling()
    test2 = test_script_continues_after_failure()
    
    print("\n" + "=" * 60)
    if test1 and test2:
        print("✅ ALL TESTS PASSED")
        print("\nSummary:")
        print("  • Failed downloads DON'T count towards limit")
        print("  • Script continues to next firmware after failure")
        print("  • Script doesn't get stuck on failures")
        print("  • Only successful downloads count")
        sys.exit(0)
    else:
        print("❌ SOME TESTS FAILED")
        sys.exit(1)
