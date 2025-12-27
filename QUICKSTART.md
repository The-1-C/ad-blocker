# Ad Blocker v2.0 - Quick Start Guide

## 🚀 Installation (2 minutes)

### Step 1: Download
- Download `ad-blocker-v2.0.zip` from the releases page
- Extract it to any folder

### Step 2: Load in Chrome
1. Open Chrome
2. Go to `chrome://extensions/`
3. Enable **Developer mode** (toggle in top right)
4. Click **Load unpacked**
5. Select the extracted `ad-blocker` folder
6. Done! ✅

### Step 3: Verify It's Working
1. Click the extension icon (should be in toolbar)
2. You should see the popup with:
   - Toggle switch (should show "Active")
   - Statistics (Blocked Today: 0, etc.)
   - Blocking level selector
   - Whitelist button

## 📋 Features at a Glance

| Feature | What It Does |
|---------|-------------|
| **Toggle On/Off** | Enable or disable all blocking |
| **Blocking Levels** | Standard (fast) → Aggressive (thorough) |
| **Block Counter** | See how many ads were blocked |
| **Whitelist** | Disable blocking on specific sites |
| **Reset Stats** | Clear today's block count |
| **Auto-Update** | Fetch latest ad rules |

## 🎮 How to Use

### Block Ads
1. Extension is active by default
2. Toggle OFF to disable on current page
3. Reload the page to see changes
4. Visit any website - ads should be blocked

### Whitelist a Site
1. Click extension popup
2. Click "Whitelist This Site"
3. Button changes to "Remove from Whitelist"
4. Site will no longer be blocked
5. Click again to remove from whitelist

### Change Blocking Level
1. Click extension popup
2. Select from dropdown:
   - **Standard**: Fast (100 domains)
   - **Aggressive**: Thorough (300+ domains)
   - **Custom**: Use rules.json
3. Page reloads automatically

### Check Statistics
The popup shows:
- **Blocked Today**: Resets at midnight
- **Blocked This Tab**: Current page only
- **Total Blocked**: All-time count

### Reset Stats
Click "Reset Stats" button to clear counters.

## 🔍 Troubleshooting

**Popup not showing?**
- Right-click extension icon → "Show in toolbar"
- Reload the extension from chrome://extensions

**Ads still showing?**
- Make sure toggle is ON (blue)
- Check if site is whitelisted
- Try "Standard" blocking level
- Reload the page
- Try "Aggressive" level

**Stats showing 0?**
- Stats only count blocked requests
- Not all blocked requests are detected (Chrome limitation)
- Try visiting more sites
- Reload pages to trigger blocks

**Extension has errors?**
- Go to chrome://extensions
- Click "Errors" under your extension
- Reload the extension (circular arrow)
- Check Service Worker logs

## 📊 What Gets Blocked

### Standard Ruleset (~100 domains)
- Google: DoubleClick, GoogleAds, Analytics
- Facebook: Ads, Pixel, Tracking
- Amazon: AdSystem
- Twitter/LinkedIn: Ads
- Taboola/Outbrain: Content discovery ads
- Criteo, Hotjar, etc.

### Aggressive Ruleset (~300+ domains)
Everything above PLUS:
- All analytics services (Mixpanel, Segment, Amplitude)
- Error tracking (Sentry, Bugsnag)
- Session recording (FullStory, Hotjar Pro)
- Survey tools (Qualaroo)
- Email tracking
- Social media trackers

## ⚙️ Advanced (Optional)

### Update Rules Manually
```bash
pip install requests
python update_rules.py
```
This fetches latest rules from EasyList and uBlock Origin.

### Add Custom Rules
Edit `rules.json` with new domains:
```json
{
  "id": 999,
  "priority": 1,
  "action": { "type": "block" },
  "condition": {
    "urlFilter": "ads.example.com",
    "domainType": "thirdParty",
    "resourceTypes": ["script", "image", "xmlhttprequest", "sub_frame"]
  }
}
```

### How It Works
- **Network Blocking**: Chrome blocks requests directly (private)
- **Cosmetic Filtering**: Content script hides ad elements
- **Stats Tracking**: Background service worker counts blocks

## 🔒 Privacy & Security

✅ 100% Private
- No data sent anywhere
- No analytics
- No accounts required
- Everything stays on your device

✅ Secure
- Only uses official Chrome APIs
- No malware or tracking
- Code is open source (GitHub)
- Can be audited anytime

## 📞 Support

**Common Issues:**

1. **Extension won't load** → manifest.json invalid
   - Try reloading at chrome://extensions

2. **Popup is blank** → Storage issue
   - Clear: Settings → Advanced → Clear browsing data
   - Reload extension

3. **Still seeing ads** → Needs aggressive mode
   - Try "Aggressive" blocking level
   - Some ads need cosmetic filtering

## 📚 Full Documentation

See `README.md` for:
- Complete feature list
- File structure
- Configuration options
- Advanced customization
- Development guide

See `IMPLEMENTATION_SUMMARY.md` for:
- Technical details
- What's new in v2.0
- Architecture overview

## 🐛 Report Issues

Found a bug? Want a feature?
1. Go to GitHub: https://github.com/The-1-C/ad-blocker
2. Click "Issues" tab
3. Click "New Issue"
4. Describe the problem with details

## 🎉 You're All Set!

The extension is now active and blocking ads. Enjoy your faster, cleaner web!

**Tips:**
- Try "Aggressive" mode for best results
- Whitelist sites that break with blocking
- Check stats to see your impact
- Visit high-ad sites to see savings

---

**Version**: 2.0  
**Last Updated**: 2025-12-26  
**License**: MIT (free & open source)
