# Installation Guide - Ad Blocker v2.0

## Prerequisites

- Google Chrome (v88 or newer)
- Administrator access to your computer
- ~10 MB disk space

## Method 1: From ZIP File (Easiest)

### Step 1: Download the ZIP
1. Visit: https://github.com/The-1-C/ad-blocker/releases
2. Download `ad-blocker-v2.0.zip`
3. Save to Downloads folder

### Step 2: Extract ZIP
**Windows:**
1. Right-click `ad-blocker-v2.0.zip`
2. Select "Extract All..."
3. Choose location (Desktop or Documents)
4. Click "Extract"

**Mac:**
1. Double-click `ad-blocker-v2.0.zip`
2. Finder automatically extracts it
3. Move folder to preferred location

**Linux:**
```bash
unzip ad-blocker-v2.0.zip
# or
unzip -d ~/Downloads ad-blocker-v2.0.zip
```

### Step 3: Load in Chrome
1. **Open Chrome**
2. **Go to Extensions:**
   - Type in address bar: `chrome://extensions/`
   - Or: Menu (⋮) → More tools → Extensions

3. **Enable Developer Mode:**
   - Toggle switch in top-right corner
   - Should turn blue

4. **Load Unpacked:**
   - Click "Load unpacked" button
   - Navigate to extracted `ad-blocker` folder
   - Click "Open" or "Select"

5. **Verify Installation:**
   - Extension appears in toolbar
   - Extension icon visible
   - No error messages

## Method 2: From GitHub (For Developers)

### Prerequisites
- Git installed
- GitHub account (optional)

### Step 1: Clone Repository
```bash
# Clone the repo
git clone https://github.com/The-1-C/ad-blocker.git
cd ad-blocker

# Or download specific branch
git clone -b master https://github.com/The-1-C/ad-blocker.git
```

### Step 2: Install
Same as Step 3 above (Load in Chrome)

### Step 3: (Optional) Update Rules
```bash
# Install Python dependencies
pip install requests

# Update filter lists
python update_rules.py
```

## Method 3: From Source Files

If you downloaded individual files:

### Step 1: Create Folder
1. Create folder: `ad-blocker`
2. Create subfolders if needed:
   - `_metadata/` (for logs)

### Step 2: Add Files
Download and place in `ad-blocker` folder:
- `manifest.json` (required)
- `popup.html` (required)
- `popup.js` (required)
- `background.js` (required)
- `content.js` (required)
- `rules-standard.json` (recommended)
- `rules-aggressive.json` (recommended)
- `rules.json` (optional - custom rules)

### Step 3: Verify Structure
```
ad-blocker/
├── manifest.json
├── popup.html
├── popup.js
├── background.js
├── content.js
├── rules.json
├── rules-standard.json
├── rules-aggressive.json
└── _metadata/
```

### Step 4: Load in Chrome
Same as Method 1, Step 3

## Verification Steps

After installation, verify everything works:

### 1. Extension Appears
- [ ] Extension icon in toolbar (top right)
- [ ] Click icon → popup appears

### 2. Popup Works
- [ ] Popup loads without errors
- [ ] Toggle switch visible and clickable
- [ ] Status shows "Active" (green) or "Disabled" (yellow)
- [ ] Statistics visible (Blocked Today, etc.)

### 3. Blocking Works
- [ ] Toggle ON (should show "Active")
- [ ] Visit ad-heavy site (YouTube, Reddit, etc.)
- [ ] Some ads should be blocked
- [ ] Numbers in popup should increase

### 4. No Errors
- [ ] No red errors in chrome://extensions
- [ ] No errors in DevTools (F12 → Console)
- [ ] Service Worker shows "Activated and running"

## Troubleshooting

### "This file cannot be opened" (ZIP extraction)
**Solution:**
- Download 7-Zip: https://7-zip.org/
- Right-click ZIP → 7-Zip → Extract Here
- Or use Windows built-in: Right-click → Extract All

### "Load unpacked not visible"
**Solution:**
1. Make sure Developer mode is ON (toggle in top-right)
2. Should turn blue
3. Try refreshing the page (F5)

### "Extension won't load" or "Manifest error"
**Solutions:**
1. Check manifest.json is in correct folder
2. Make sure manifest.json is valid JSON (no syntax errors)
3. Try reloading: chrome://extensions → Reload button
4. Check console for detailed error (F12)

### "Popup shows blank screen"
**Solutions:**
1. Clear storage: Settings → Advanced → Clear browsing data
2. Unload extension and reload
3. Check popup.html and popup.js are in folder
4. Verify popup.js loads in DevTools

### "No ads are being blocked"
**Solutions:**
1. Check if toggle is ON (blue)
2. Try "Standard" blocking level
3. Try "Aggressive" level
4. Reload the page (Ctrl+R or Cmd+R)
5. Check if site is whitelisted
6. Try different website

### "Service Worker shows errors"
**Solutions:**
1. Click "Service Worker" link to see detailed errors
2. Reload extension from chrome://extensions
3. Check background.js for syntax errors
4. Clear extension storage and reload

### "Statistics not updating"
**Solutions:**
1. This is a Chrome limitation - not all blocks are reported
2. Visit ad-heavy sites to see more blocks
3. Try Aggressive mode (more blocks detected)
4. Stats only count certain request types

### "Can't update rules"
**Solutions:**
1. This requires Python and requests library
2. Install: `pip install requests`
3. Run: `python update_rules.py` in extension folder
4. Manual update via popup button requires internet

## Installation on Different Systems

### Windows 10/11
1. Right-click ZIP → Extract All
2. Go to chrome://extensions
3. Click Load unpacked
4. Select extracted folder
5. Done!

### macOS
1. Double-click ZIP (auto-extracts)
2. Go to chrome://extensions
3. Click Load unpacked
4. Select extracted folder
5. Done!

### Linux
```bash
# Extract
unzip ad-blocker-v2.0.zip

# Load in Chrome
# Go to chrome://extensions
# Click Load unpacked
# Select ~/ad-blocker folder
```

### Chrome OS
Chromebooks can't load unpacked extensions. Options:
1. Wait for official Chrome Web Store listing
2. Use a regular computer to set it up
3. Use remote desktop to another machine

## Uninstallation

### Remove Extension
1. Go to `chrome://extensions/`
2. Find "Ad Blocker"
3. Click "Remove" button
4. Confirm

### Cleanup
- Extension folder can be deleted
- Clear storage to remove stats/whitelist
- Settings in chrome://extensions will be cleared

## Update to New Version

### Method 1: Auto-Update (When Available)
- Chrome will auto-check Chrome Web Store
- Install automatically when available

### Method 2: Manual Update
1. Download new version ZIP
2. Extract to new folder
3. Go to chrome://extensions
4. Click reload on old version
5. Or remove old, load new version

### Preserve Settings
- Unload (don't remove) old version
- Load new version
- Settings should migrate automatically

## Getting Help

If you encounter issues:

1. **Check Documentation:**
   - README.md - Feature overview
   - QUICKSTART.md - Basic usage
   - TESTING_CHECKLIST.md - Verify installation

2. **Check GitHub Issues:**
   - https://github.com/The-1-C/ad-blocker/issues
   - Search for your problem
   - Create new issue if needed

3. **Debug Steps:**
   - Open DevTools (F12)
   - Check Console tab for errors
   - Check Service Worker logs
   - Check popup.js console

4. **Clear and Reset:**
   ```
   Settings → Advanced → Clear browsing data
   Check: Cookies and other site data
   Check: Cached images and files
   Time range: All time
   Click Clear data
   ```

5. **Reinstall:**
   1. Uninstall extension
   2. Delete extension folder
   3. Restart Chrome
   4. Download fresh copy
   5. Reinstall

## Next Steps

After installation:

1. **Read QUICKSTART.md** - Learn basic usage
2. **Visit ad-heavy site** - See blocking in action
3. **Whitelist trusted sites** - Add to exception list
4. **Check statistics** - See your impact
5. **Change blocking level** - Try Aggressive mode

## System Requirements

| Component | Requirement |
|-----------|------------|
| Browser | Chrome 88+ |
| RAM | 256 MB minimum |
| Disk Space | ~10 MB |
| Internet | Not required (blocking is local) |
| Admin Rights | Recommended for installation |

## Performance After Installation

Expected impact:
- **Speed**: No noticeable slowdown
- **Memory**: +5-10 MB
- **CPU**: <1% when idle
- **Battery**: Minimal impact (local blocking)

## Security Notes

- ✅ No installation of external programs
- ✅ No tracking of user activity
- ✅ No data sent to servers
- ✅ All processing happens locally
- ✅ Open source code (auditable)

---

**Installation Version**: 2.0  
**Last Updated**: 2025-12-26  
**Support**: https://github.com/The-1-C/ad-blocker
