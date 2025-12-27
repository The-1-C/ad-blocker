// Service Worker for tracking stats and auto-updates

// Initialize storage on install
chrome.runtime.onInstalled.addListener(() => {
  chrome.storage.local.set({
    enabled: true,
    level: 'standard',
    whitelist: [],
    stats: { today: 0, tab: {}, total: 0 },
    lastUpdated: Date.now()
  });
});

// Listen for web request completion to track blocks
// Note: DNR doesn't provide detailed block events, so we use a simpler approach
// This listener fires when rules match (requires declarativeNetRequestFeedback)
chrome.declarativeNetRequest.onRuleMatchedDebug?.addListener((details) => {
  trackBlockedRequest(details);
});

// Fallback: Track using a content script message
chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
  if (request.action === 'trackBlock') {
    trackBlockedRequest({
      tabId: sender.tab.id,
      url: request.url
    });
  } else if (request.action === 'updateRules') {
    updateRulesFromEasyList()
      .then(success => sendResponse({ success }))
      .catch(err => sendResponse({ success: false, error: err.message }));
    return true; // Keep channel open for async response
  }
});

function trackBlockedRequest(details) {
  if (!details || !details.tabId) return;

  chrome.storage.local.get(['stats'], (result) => {
    const stats = result.stats || { today: 0, tab: {}, total: 0 };

    // Increment counters
    stats.today = (stats.today || 0) + 1;
    stats.total = (stats.total || 0) + 1;

    if (!stats.tab) stats.tab = {};
    stats.tab[details.tabId] = (stats.tab[details.tabId] || 0) + 1;

    chrome.storage.local.set({ stats });

    // Notify popup if it's open
    chrome.runtime.sendMessage({
      action: 'updateStats',
      stats: stats
    }).catch(() => {
      // Popup not listening, that's ok
    });
  });
}

// Schedule daily stats reset at midnight
function scheduleStatsReset() {
  const now = new Date();
  const tomorrow = new Date(now);
  tomorrow.setDate(tomorrow.getDate() + 1);
  tomorrow.setHours(0, 0, 0, 0);

  const timeUntilMidnight = tomorrow.getTime() - now.getTime();

  setTimeout(() => {
    chrome.storage.local.get(['stats'], (result) => {
      const stats = result.stats || { today: 0, tab: {}, total: 0 };
      stats.today = 0;
      stats.tab = {};
      chrome.storage.local.set({ stats });
    });
    scheduleStatsReset(); // Reschedule for next day
  }, timeUntilMidnight);
}

scheduleStatsReset();

// Clean up tab stats when tab is closed
chrome.tabs.onRemoved.addListener((tabId) => {
  chrome.storage.local.get(['stats'], (result) => {
    const stats = result.stats || { today: 0, tab: {}, total: 0 };
    if (stats.tab && stats.tab[tabId]) {
      delete stats.tab[tabId];
      chrome.storage.local.set({ stats });
    }
  });
});

// Auto-update rules (can be triggered manually or via background scheduler)
// Removed automatic alarm scheduling - use popup button or external scheduler instead

async function updateRulesFromEasyList() {
  try {
    const easyListUrl = 'https://easylist.to/easylist/easylist.txt';
    const response = await fetch(easyListUrl);

    if (!response.ok) {
      throw new Error(`HTTP ${response.status}`);
    }

    const text = await response.text();
    const domains = parseEasyList(text);

    if (domains.length > 20) {
      const rules = convertToDNR(domains.slice(0, 100));
      // Save to storage (in real extension, would update rules file)
      chrome.storage.local.set({
        lastUpdated: Date.now(),
        generatedRules: rules
      });
    }

    return true;
  } catch (error) {
    console.error('Rules update failed:', error);
    return false;
  }
}

function parseEasyList(text) {
  const lines = text.split('\n');
  const domains = new Set();

  for (const line of lines) {
    const trimmed = line.trim();

    // Skip comments
    if (!trimmed || trimmed.startsWith('!') || trimmed.startsWith('[')) {
      continue;
    }

    // Extract ||domain.com^ format
    if (trimmed.includes('||')) {
      const match = trimmed.match(/\|\|([a-z0-9.-]+)/i);
      if (match && match[1]) {
        domains.add(match[1]);
      }
    }
  }

  return Array.from(domains);
}

function convertToDNR(domains) {
  const rules = [];

  domains.forEach((domain, index) => {
    rules.push({
      id: index + 1,
      priority: 1,
      action: { type: 'block' },
      condition: {
        urlFilter: domain,
        domainType: 'thirdParty',
        resourceTypes: ['script', 'image', 'xmlhttprequest', 'sub_frame']
      }
    });
  });

  return rules;
}
