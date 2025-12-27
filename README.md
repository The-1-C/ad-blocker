# Simple Ad Blocker Extension (v2.0)

A powerful, privacy-first Chrome extension that blocks ads and trackers using declarative rules and cosmetic filtering.

## Features

✨ **Core Blocking**
- Blocks ads via Declarative Net Request API (privacy-preserving)
- Cosmetic filtering (hides ad containers and elements)
- Multiple blocking levels (Standard / Aggressive / Custom)
- Whitelisting for specific sites

📊 **Statistics & Monitoring**
- Real-time block counter (today / current tab / total)
- Privacy-preserved analytics
- Auto-resets daily

🚀 **Advanced Features**
- Auto-updates rules from EasyList daily
- Multiple rule sets (standard + aggressive)
- Supports 100+ ad networks and trackers
- Lightweight & fast (no cloud syncing)

## Installation

1. Open Chrome and go to `chrome://extensions/`
2. Enable **Developer mode** (top right)
3. Click **Load unpacked**
4. Select this folder

## Usage

### Main Features

**Blocking Levels:**
- **Standard**: Fast & efficient (covers 100+ common ad networks)
- **Aggressive**: Thorough (blocks tracking scripts, analytics, and more)
- **Custom**: Use rules.json (original rules)

**Whitelisting:**
- Click "Whitelist This Site" to disable blocking on current domain
- Remove from list anytime

**Reset Stats:**
- Click "Reset Stats" to clear today's block count

**Auto-Update Rules:**
- Click "Auto-Update Rules" to fetch latest rules from EasyList

### Statistics

- **Blocked Today**: Resets at midnight
- **Blocked This Tab**: Current page only
- **Total Blocked**: All-time count

## Configuration

### Manual Rule Updates

Update rules manually using Python scripts:

```bash
# Update from filter lists (requires requests library)
pip install requests
python update_rules.py

# Generate custom rules from EasyList
python generate_rules.py
```

This will:
1. Fetch latest EasyList and uBlock Origin lists
2. Parse rules into DNR format
3. Save to `rules-standard.json` and `rules-aggressive.json`

### Whitelisting

Whitelisted domains are stored in `chrome.storage.local` and won't have blocking applied.

### Custom Blocking

Edit `rules.json` to add custom rules in DNR format:

```json
{
  "id": 999,
  "priority": 1,
  "action": { "type": "block" },
  "condition": {
    "urlFilter": "example-ads.com",
    "domainType": "thirdParty",
    "resourceTypes": ["script", "image", "xmlhttprequest", "sub_frame"]
  }
}
```

## How It Works

### Network Requests
The extension uses Chrome's **Declarative Net Request API**, which blocks requests directly without seeing the data. This means:
- No history tracking
- No cross-site tracking
- Completely private
- Faster than traditional content-script blocking

### Cosmetic Filtering
A content script injects CSS rules to hide ad containers on the page, covering ads that slip through network blocking.

### Rule Sources

The extension includes rules from:
- [EasyList](https://easylist.to/) - Community-maintained ad list
- [EasyPrivacy](https://easylist.to/) - Privacy-focused rules
- [uBlock Origin](https://github.com/uBlockOrigin/uAssets) - Comprehensive filters
- Custom domain list maintained in rules files

## File Structure

```
ad-blocker/
├── manifest.json           # Extension config & permissions
├── popup.html             # UI popup
├── popup.js               # Popup logic
├── background.js          # Service worker (stats tracking)
├── content.js             # Content script (cosmetic filtering)
├── rules.json             # Custom rules (deprecated, use standard)
├── rules-standard.json    # Standard rules (~100 domains)
├── rules-aggressive.json  # Aggressive rules (~300+ domains)
├── generate_rules.py      # Script to generate rules from filter lists
├── update_rules.py        # Auto-update script
└── _metadata/             # Logs and metadata
```

## Performance

- **Memory**: ~5-10 MB (mostly storage)
- **CPU**: Negligible (DNR processes at browser level)
- **Network**: No external requests (only on manual update)

## Privacy

- No data is collected or sent
- No login required
- No analytics (optional future feature)
- Rules are processed locally in-browser

## Troubleshooting

**Extension not blocking ads?**
1. Check status in popup (should show "Active")
2. Make sure blocking level is set to Standard or Aggressive
3. Check whitelist (site may be whitelisted)
4. Reload the page to apply changes
5. Try clearing storage: Settings → Advanced → Clear browsing data

**Popup not showing block counts?**
1. Reload the extension (chrome://extensions)
2. Make sure tab permission is enabled
3. Check browser console for errors (F12)

**Performance issues?**
1. Switch to Standard blocking level (faster)
2. Remove custom rules from rules.json if using Custom level
3. Check for malformed rules (must be valid JSON)

## Updates

The extension automatically checks for rule updates daily. You can also:
- Click "Auto-Update Rules" button in popup
- Manually run: `python update_rules.py`

## Contributing

To improve rules:
1. Find blocking issues on websites
2. Add rules to `rules.json`
3. Test on the problematic site
4. Submit improvements

## License

MIT License - Feel free to use and modify

## Resources

- [Chrome Declarative Net Request API](https://developer.chrome.com/docs/extensions/reference/declarativeNetRequest/)
- [EasyList](https://easylist.to/)
- [uBlock Origin Filters](https://github.com/uBlockOrigin/uAssets)
- [Adblock Plus Syntax](https://adblockplus.org/en/filters)

---

**Version 2.0** - Full rewrite with stats, whitelisting, and advanced filtering
