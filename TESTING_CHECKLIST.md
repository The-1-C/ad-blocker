# Testing Checklist - Ad Blocker v2.0

## Pre-Installation ✅

- [ ] All files present (manifest.json, popup.html, popup.js, background.js, content.js)
- [ ] No syntax errors in JavaScript files
- [ ] Rules JSON files are valid JSON
- [ ] manifest.json passes Chrome validation

## Installation ✅

- [ ] Extract zip to folder
- [ ] Open chrome://extensions/
- [ ] Enable Developer mode
- [ ] Load unpacked → select folder
- [ ] Extension appears in toolbar
- [ ] No installation errors

## Initial Popup Test ✅

- [ ] Popup opens when clicking extension icon
- [ ] Popup shows without errors
- [ ] Toggle switch is visible
- [ ] Status text displays (Active/Disabled)
- [ ] Statistics section visible
- [ ] All buttons visible (Whitelist, Reset, Auto-Update)
- [ ] Blocking level dropdown works

## Blocking Functionality ✅

### Test 1: Toggle On/Off
- [ ] Toggle ON → status shows "Active" (green)
- [ ] Toggle OFF → status shows "Disabled" (yellow)
- [ ] Toggling updates storage
- [ ] Can toggle repeatedly without errors

### Test 2: Blocking Levels
- [ ] Switch to "Standard" → applies ruleset_standard
- [ ] Switch to "Aggressive" → applies both rulesets
- [ ] Switch to "Custom" → applies ruleset_1
- [ ] Dropdown changes persist
- [ ] No console errors on switch

### Test 3: Ad Blocking Works
Visit these sites (known to have ads):
- [ ] YouTube.com → blocks ads
- [ ] Reddit.com → blocks tracking
- [ ] News site → blocks banners
- [ ] Check each with Standard and Aggressive modes

## Statistics ✅

- [ ] "Blocked Today" displays number
- [ ] "Blocked This Tab" displays number
- [ ] "Total Blocked" displays number
- [ ] Numbers increase when visiting ad-heavy sites
- [ ] "Reset Stats" button clears counters
- [ ] Counters persist after popup close
- [ ] Reset only affects "Blocked Today" (optional: and tab counters)

## Whitelisting ✅

### Test 1: Whitelist Site
- [ ] Open popup on any website
- [ ] Click "Whitelist This Site"
- [ ] Button text changes to "Remove from Whitelist"
- [ ] Button color changes (becomes reddish)
- [ ] Site name appears in whitelist list
- [ ] Blocking disabled on that site

### Test 2: Remove from Whitelist
- [ ] Click remove button (×) next to domain
- [ ] Site removed from list
- [ ] Button changes back to "Whitelist This Site"
- [ ] Color returns to normal
- [ ] Blocking re-enabled on that site

### Test 3: Multiple Sites
- [ ] Whitelist 3-5 different sites
- [ ] All appear in list
- [ ] Each can be removed independently
- [ ] Whitelist persists across sessions

## Storage ✅

- [ ] Settings saved to chrome.storage.local
- [ ] Stats persisted when popup closes
- [ ] Whitelist persisted when popup closes
- [ ] Settings survive extension reload
- [ ] Clear Chrome cache doesn't delete settings

## Content Script (Cosmetic Filtering) ✅

- [ ] Content script injects on every page
- [ ] Ad containers hidden via CSS
- [ ] No console errors on pages
- [ ] Works with Standard and Aggressive modes
- [ ] Dynamically added ads get hidden

## Service Worker ✅

- [ ] Service Worker registers without errors
- [ ] No errors in DevTools (chrome://extensions → Service Worker)
- [ ] Message handling works (popup ↔ background)
- [ ] Tab cleanup works (closed tabs removed from stats)
- [ ] No memory leaks

## Error Handling ✅

- [ ] Toggle errors gracefully
- [ ] Invalid domains don't crash extension
- [ ] Network errors handled
- [ ] Storage quota exceeded handled
- [ ] Malformed storage data doesn't crash

## Performance ✅

- [ ] Popup opens in <500ms
- [ ] No lag when toggling
- [ ] Page loading not slowed down
- [ ] CPU usage minimal (<5%)
- [ ] Memory usage stable (5-10MB)

## Cross-Site Testing ✅

Test on variety of sites:

### Ad-Heavy Sites
- [ ] YouTube (pre-roll ads)
- [ ] Reddit (sponsored posts)
- [ ] Medium (tracking)
- [ ] News sites (banners)

### Corporate Sites
- [ ] Amazon (ads)
- [ ] Google (ads)
- [ ] Microsoft (tracking)

### Content Sites
- [ ] Wikipedia (minimal ads)
- [ ] GitHub (no ads)
- [ ] Stack Overflow

## Edge Cases ✅

- [ ] Whitelist then toggle OFF → blocking still off
- [ ] Whitelist then toggle ON → blocking applied to non-whitelisted
- [ ] Open multiple popup instances → all in sync
- [ ] Extension disabled then enabled → works again
- [ ] Multiple tabs open → per-tab stats work
- [ ] Close tab → stats cleaned up
- [ ] Aggressive then Standard → works both ways

## Browser Compatibility ✅

- [ ] Chrome latest version
- [ ] Chrome stable build
- [ ] No warnings in DevTools
- [ ] No deprecated API usage

## Documentation ✅

- [ ] README.md is complete
- [ ] QUICKSTART.md covers basics
- [ ] IMPLEMENTATION_SUMMARY.md has technical details
- [ ] All code is commented
- [ ] No broken links in docs

## GitHub ✅

- [ ] Code pushed to GitHub
- [ ] Commit history clean
- [ ] .gitignore working
- [ ] Zip file created
- [ ] README visible on GitHub page

## Final Quality Check ✅

**User Experience:**
- [ ] Intuitive UI
- [ ] Clear feedback (enable/disable, counts)
- [ ] Fast performance
- [ ] No unexpected behavior

**Code Quality:**
- [ ] No console errors
- [ ] No memory leaks
- [ ] Proper error handling
- [ ] Clean code structure

**Features:**
- [ ] Blocking works reliably
- [ ] Stats accurate
- [ ] Whitelisting works
- [ ] UI responsive

## Performance Baseline

| Metric | Target | Actual |
|--------|--------|--------|
| Popup load time | <500ms | __ |
| Memory usage | <15MB | __ |
| CPU usage | <5% idle | __ |
| Toggle latency | <100ms | __ |

## Known Issues (if any)

- Issue: ___________
  Status: ___________
  Workaround: ___________

## Sign Off

- [ ] All tests passed
- [ ] No critical issues
- [ ] Ready for release
- [ ] User feedback: ___________

**Tested By:** ___________  
**Date:** ___________  
**Version:** 2.0

---

## Quick Test Script (Manual)

```javascript
// Run in console on any page to verify blocking:

// 1. Check if background service worker is active
console.log('Checking extension...');

// 2. Check storage
chrome.storage.local.get(null, (result) => {
  console.log('Storage:', result);
});

// 3. Check if content script is running
console.log('Content script loaded: ', window.__adBlockerActive !== undefined);

// 4. Report results
setTimeout(() => {
  alert('Check console for results. Extension is working if no errors appear.');
}, 1000);
```

## Automated Test Ideas (Future)

- Selenium tests for popup interactions
- Unit tests for rule parsing
- Integration tests for blocking
- Performance benchmarks
