#!/bin/bash
# Push script for Hikvision firmware archive
cd "$(dirname "$0")"

echo "Pushing to GitHub..."
git push -u origin main

if [ $? -ne 0 ]; then
    echo ""
    echo "Push failed. You may need to authenticate."
    echo ""
    echo "Option 1: Use Personal Access Token"
    echo "  1. Create token at: https://github.com/settings/tokens"
    echo "  2. Run: git remote set-url origin https://YOUR_TOKEN@github.com/JoeyGE0/hikvision-fw-archive.git"
    echo "  3. Run this script again"
    echo ""
    echo "Option 2: Use SSH"
    echo "  1. Generate SSH key: ssh-keygen -t ed25519 -C 'your_email@example.com'"
    echo "  2. Add to GitHub: https://github.com/settings/keys"
    echo "  3. Run this script again"
    echo ""
    echo "Option 3: Use GitHub Desktop or other GUI tool"
fi
