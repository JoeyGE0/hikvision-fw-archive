#!/usr/bin/env python3
"""Automatically add workflow file to GitHub via browser automation."""
from playwright.sync_api import sync_playwright
import time
import os

workflow_path = '.github/workflows/update.yml'
if not os.path.exists(workflow_path):
    print("❌ Workflow file not found!")
    exit(1)

workflow_content = open(workflow_path).read()
print(f"✅ Loaded workflow file")

print("\n🚀 Opening browser to add workflow file to GitHub...")
print("Please login to GitHub if prompted, then wait...")

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    
    try:
        url = "https://github.com/JoeyGE0/hikvision-fw-archive/new/main/.github/workflows"
        print(f"\n📍 Going to: {url}")
        page.goto(url, timeout=60000)
        time.sleep(8)  # Wait for page load and potential login
        
        # Fill filename
        print("📝 Filling filename...")
        page.fill('input[type="text"]', 'update.yml')
        time.sleep(1)
        
        # Fill content - click editor first
        print("📝 Filling content...")
        page.click('textarea, .monaco-editor, .CodeMirror')
        time.sleep(1)
        page.keyboard.press('Control+A')
        page.keyboard.type(workflow_content)
        time.sleep(2)
        
        # Commit
        print("💾 Committing...")
        page.click('button:has-text("Commit"), button[type="submit"]')
        time.sleep(10)
        
        print("\n✅✅✅ WORKFLOW FILE ADDED! GitHub Actions will run automatically!")
        
    except Exception as e:
        print(f"\n❌ Error: {e}")
        print("\nPlease manually add the file at:")
        print("https://github.com/JoeyGE0/hikvision-fw-archive/new/main/.github/workflows")
    
    finally:
        time.sleep(3)
        browser.close()
