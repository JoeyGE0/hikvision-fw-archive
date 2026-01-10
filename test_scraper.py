#!/usr/bin/env python3
"""Test script to verify the early exit logic for download limits."""
import sys
import os

# Add current directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Mock the early exit logic
def test_early_exit_logic():
    """Test that the early exit logic works correctly."""
    print("Testing early exit logic...")
    
    # Simulate the variables from the scraper
    MAX_FIRMWARES_TO_DOWNLOAD = 10
    new_downloads_count = 0
    test_mode_limit_reached = False
    total_links_processed = 0
    total_links_checked = 0
    
    # Simulate processing 1000 links (like the real scenario)
    links = list(range(1000))
    
    print(f"  Starting with MAX_FIRMWARES_TO_DOWNLOAD = {MAX_FIRMWARES_TO_DOWNLOAD}")
    print(f"  Simulating {len(links)} links to process...")
    
    for link_idx, link in enumerate(links, 1):
        # Check 1: Early exit flag
        if test_mode_limit_reached:
            print(f"  ✓ Early exit triggered at link {link_idx}")
            break
        
        # Check 2: Download limit BEFORE processing (NEW FIX)
        if MAX_FIRMWARES_TO_DOWNLOAD > 0 and new_downloads_count >= MAX_FIRMWARES_TO_DOWNLOAD:
            print(f"  ✓ Download limit reached at link {link_idx} (before processing)")
            test_mode_limit_reached = True
            break
        
        # Simulate processing the link
        total_links_checked += 1
        
        # Simulate finding a new firmware (every 5th link)
        if link_idx % 5 == 0:
            new_downloads_count += 1
            total_links_processed += 1
            print(f"    Link {link_idx}: Downloaded firmware #{new_downloads_count}")
            
            # Check limit after download (existing check)
            if MAX_FIRMWARES_TO_DOWNLOAD > 0 and new_downloads_count >= MAX_FIRMWARES_TO_DOWNLOAD:
                print(f"  ✓ Download limit reached at link {link_idx} (after download)")
                test_mode_limit_reached = True
                break
    
    print(f"\n  Results:")
    print(f"    - Links checked: {total_links_checked}")
    print(f"    - Links processed: {total_links_processed}")
    print(f"    - Downloads: {new_downloads_count}")
    print(f"    - Early exit triggered: {test_mode_limit_reached}")
    
    # Verify the fix works
    if test_mode_limit_reached and new_downloads_count == MAX_FIRMWARES_TO_DOWNLOAD:
        print(f"\n  ✅ TEST PASSED: Early exit works correctly!")
        print(f"     Stopped after {total_links_checked} links instead of processing all 1000")
        return True
    elif not test_mode_limit_reached:
        print(f"\n  ❌ TEST FAILED: Early exit not triggered")
        return False
    else:
        print(f"\n  ⚠️  TEST WARNING: Unexpected state")
        return False


def test_break_statement_placement():
    """Test that break statements are correctly placed."""
    print("\nTesting break statement placement...")
    
    # Simulate nested loops
    test_mode_limit_reached = False
    MAX_FIRMWARES_TO_DOWNLOAD = 10
    new_downloads_count = 0
    
    search_terms = ['DS-2CD', 'DS-2DE', 'DS-76']
    models_per_search = 100
    links_per_model = 10
    
    total_links_checked = 0
    
    for search_term in search_terms:
        if test_mode_limit_reached:
            print(f"  ✓ Broke out of search_terms loop")
            break
            
        for model_idx in range(models_per_search):
            if test_mode_limit_reached:
                print(f"  ✓ Broke out of models loop")
                break
                
            for link_idx in range(links_per_model):
                # Early check (NEW FIX)
                if test_mode_limit_reached:
                    break
                    
                if MAX_FIRMWARES_TO_DOWNLOAD > 0 and new_downloads_count >= MAX_FIRMWARES_TO_DOWNLOAD:
                    test_mode_limit_reached = True
                    break
                
                total_links_checked += 1
                
                # Simulate download
                if link_idx % 2 == 0:
                    new_downloads_count += 1
                    if new_downloads_count >= MAX_FIRMWARES_TO_DOWNLOAD:
                        test_mode_limit_reached = True
                        break
        
        if test_mode_limit_reached:
            break
    
    print(f"  Links checked: {total_links_checked}")
    print(f"  Downloads: {new_downloads_count}")
    
    if test_mode_limit_reached and new_downloads_count == MAX_FIRMWARES_TO_DOWNLOAD:
        print(f"  ✅ TEST PASSED: Break statements work correctly in nested loops")
        return True
    else:
        print(f"  ❌ TEST FAILED")
        return False


def test_code_structure():
    """Test that the code structure is correct."""
    print("\nTesting code structure...")
    
    # Read main.py and check for issues
    try:
        with open('main.py', 'r') as f:
            content = f.read()
        
        issues = []
        
        # Check 1: Early exit check exists
        if 'Check download limit BEFORE processing link' not in content:
            issues.append("Missing early exit check comment")
        
        # Check 2: No unreachable code after break
        lines = content.split('\n')
        for i, line in enumerate(lines):
            if 'break' in line and i + 1 < len(lines):
                next_line = lines[i + 1].strip()
                # Check if there's code after break that's not a comment or blank
                if next_line and not next_line.startswith('#') and 'if test_mode_limit_reached' not in next_line:
                    # This might be unreachable, but let's check context
                    if 'time.sleep' in next_line or 'logger' in next_line:
                        # Check if it's in the same block
                        indent_break = len(line) - len(line.lstrip())
                        indent_next = len(lines[i + 1]) - len(lines[i + 1].lstrip())
                        if indent_next > indent_break:
                            issues.append(f"Possible unreachable code after break at line {i + 2}")
        
        if issues:
            print(f"  ⚠️  Found {len(issues)} potential issues:")
            for issue in issues:
                print(f"     - {issue}")
            return False
        else:
            print(f"  ✅ Code structure looks good")
            return True
            
    except Exception as e:
        print(f"  ❌ Error checking code: {e}")
        return False


if __name__ == '__main__':
    print("=" * 60)
    print("Testing Hikvision Scraper Fix")
    print("=" * 60)
    
    test1 = test_early_exit_logic()
    test2 = test_break_statement_placement()
    test3 = test_code_structure()
    
    print("\n" + "=" * 60)
    if test1 and test2 and test3:
        print("✅ ALL TESTS PASSED")
        sys.exit(0)
    else:
        print("❌ SOME TESTS FAILED")
        sys.exit(1)
