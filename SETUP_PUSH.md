# Quick Push Setup

Everything is ready to push! You just need to authenticate once.

## Option 1: Personal Access Token (Easiest)

1. Create a token: https://github.com/settings/tokens/new

   - Name: `hikvision-fw-archive`
   - Expiration: No expiration (or your choice)
   - Scopes: Check `repo` (full control of private repositories)
   - Click "Generate token"
   - **Copy the token immediately** (you won't see it again!)

2. Run this command (replace YOUR_TOKEN with your actual token):

```bash
cd "/Users/josiahclark/Library/Mobile Documents/com~apple~CloudDocs/Coding and development/hikvision-fw-archive"
git remote set-url origin https://YOUR_TOKEN@github.com/JoeyGE0/hikvision-fw-archive.git
git push -u origin main
```

## Option 2: SSH Key (More Secure)

1. Generate SSH key:

```bash
ssh-keygen -t ed25519 -C "your_email@example.com"
# Press Enter for default location
# Press Enter for no passphrase (or set one)
```

2. Copy public key:

```bash
cat ~/.ssh/id_ed25519.pub
```

3. Add to GitHub:

   - Go to: https://github.com/settings/keys
   - Click "New SSH key"
   - Paste the key
   - Click "Add SSH key"

4. Push:

```bash
cd "/Users/josiahclark/Library/Mobile Documents/com~apple~CloudDocs/Coding and development/hikvision-fw-archive"
git remote set-url origin git@github.com:JoeyGE0/hikvision-fw-archive.git
git push -u origin main
```

## Option 3: GitHub Desktop

1. Open GitHub Desktop
2. File > Add Local Repository
3. Choose the `hikvision-fw-archive` folder
4. Click "Publish repository"

## Current Status

✅ All files committed locally (2 commits)
✅ Remote configured: https://github.com/JoeyGE0/hikvision-fw-archive.git
✅ Ready to push!

Just authenticate using one of the methods above and you're done!
