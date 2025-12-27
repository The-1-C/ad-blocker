document.addEventListener('DOMContentLoaded', async () => {
  const toggle = document.getElementById('toggle');
  const statusText = document.getElementById('status-text');
  const currentDomain = document.getElementById('current-domain');
  const levelSelect = document.getElementById('level-select');
  const whitelistBtn = document.getElementById('whitelist-btn');
  const resetStatsBtn = document.getElementById('reset-stats-btn');
  const autoUpdateBtn = document.getElementById('auto-update-btn');
  const whitelistList = document.getElementById('whitelist-list');
  const whitelistItems = document.getElementById('whitelist-items');
  const blocksToday = document.getElementById('blocks-today');
  const blocksTab = document.getElementById('blocks-tab');
  const blocksTotal = document.getElementById('blocks-total');
  const noteText = document.getElementById('note-text');

  // Get current tab
  const [tab] = await chrome.tabs.query({ active: true, currentWindow: true });
  const tabDomain = new URL(tab.url).hostname;
  currentDomain.textContent = tabDomain;

  // Load extension state
  chrome.storage.local.get(['enabled', 'level', 'whitelist', 'stats'], (result) => {
    const isEnabled = result.enabled !== false;
    const level = result.level || 'standard';
    const whitelist = result.whitelist || [];
    const stats = result.stats || { today: 0, tab: {}, total: 0 };

    // Update UI
    toggle.checked = isEnabled;
    levelSelect.value = level;
    updateStatusText(isEnabled);
    updateStats(stats, tab.id);
    renderWhitelist(whitelist);

    // Check if current domain is whitelisted
    const isWhitelisted = whitelist.includes(tabDomain);
    whitelistBtn.textContent = isWhitelisted ? 'Remove from Whitelist' : 'Whitelist This Site';
    whitelistBtn.style.backgroundColor = isWhitelisted ? 'rgba(255,107,107,0.3)' : 'rgba(255,255,255,0.1)';
  });

  // Toggle blocking
  toggle.addEventListener('change', async () => {
    const isEnabled = toggle.checked;
    chrome.storage.local.set({ enabled: isEnabled });

    if (isEnabled) {
      const level = levelSelect.value;
      await applyBlockingLevel(level);
    } else {
      await chrome.declarativeNetRequest.updateEnabledRulesets({
        disableRulesetIds: ['ruleset_1', 'ruleset_standard', 'ruleset_aggressive']
      });
    }

    updateStatusText(isEnabled);
    noteText.textContent = isEnabled ? 'Blocking ad networks in real-time...' : 'Ad blocking is OFF.';
  });

  // Change blocking level
  levelSelect.addEventListener('change', async () => {
    const level = levelSelect.value;
    chrome.storage.local.set({ level });

    if (toggle.checked) {
      await applyBlockingLevel(level);
    }
  });

  // Whitelist current site
  whitelistBtn.addEventListener('click', () => {
    chrome.storage.local.get(['whitelist'], (result) => {
      const whitelist = result.whitelist || [];
      const index = whitelist.indexOf(tabDomain);

      if (index > -1) {
        whitelist.splice(index, 1);
        whitelistBtn.textContent = 'Whitelist This Site';
        whitelistBtn.style.backgroundColor = 'rgba(255,255,255,0.1)';
      } else {
        whitelist.push(tabDomain);
        whitelistBtn.textContent = 'Remove from Whitelist';
        whitelistBtn.style.backgroundColor = 'rgba(255,107,107,0.3)';
      }

      chrome.storage.local.set({ whitelist });
      renderWhitelist(whitelist);
    });
  });

  // Reset stats
  resetStatsBtn.addEventListener('click', () => {
    chrome.storage.local.set({ 
      stats: { today: 0, tab: {}, total: 0 } 
    });
    updateStats({ today: 0, tab: {}, total: 0 }, tab.id);
  });

  // Auto-update rules (trigger background script)
  autoUpdateBtn.addEventListener('click', async () => {
    autoUpdateBtn.textContent = 'Updating...';
    autoUpdateBtn.disabled = true;

    chrome.runtime.sendMessage({ action: 'updateRules' }, (response) => {
      autoUpdateBtn.textContent = 'Auto-Update Rules';
      autoUpdateBtn.disabled = false;
      if (response && response.success) {
        noteText.textContent = 'Rules updated successfully!';
        setTimeout(() => {
          noteText.textContent = 'Blocking ad networks in real-time...';
        }, 3000);
      } else {
        noteText.textContent = 'Update failed. Try again later.';
      }
    });
  });

  // Listen for stats updates from background script
  chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
    if (request.action === 'updateStats') {
      updateStats(request.stats, tab.id);
    }
  });

  function updateStatusText(isEnabled) {
    statusText.textContent = isEnabled ? 'Active' : 'Disabled';
    statusText.className = `status-text ${isEnabled ? 'active' : 'disabled'}`;
  }

  function updateStats(stats, currentTabId) {
    blocksToday.textContent = stats.today || 0;
    blocksTotal.textContent = stats.total || 0;
    const tabBlocks = stats.tab && stats.tab[currentTabId] ? stats.tab[currentTabId] : 0;
    blocksTab.textContent = tabBlocks;
  }

  function renderWhitelist(whitelist) {
    whitelistItems.innerHTML = '';
    if (whitelist.length === 0) {
      whitelistList.style.display = 'none';
      return;
    }

    whitelistList.style.display = 'block';
    whitelist.forEach(domain => {
      const item = document.createElement('div');
      item.className = 'whitelist-item';
      item.innerHTML = `
        <span>${domain}</span>
        <button class="remove-btn" data-domain="${domain}">×</button>
      `;
      whitelistItems.appendChild(item);

      item.querySelector('.remove-btn').addEventListener('click', () => {
        const updatedWhitelist = whitelist.filter(d => d !== domain);
        chrome.storage.local.set({ whitelist: updatedWhitelist });
        renderWhitelist(updatedWhitelist);
      });
    });
  }

  async function applyBlockingLevel(level) {
    const rulesets = {
      standard: { enableRulesetIds: ['ruleset_standard'], disableRulesetIds: ['ruleset_aggressive', 'ruleset_1'] },
      aggressive: { enableRulesetIds: ['ruleset_standard', 'ruleset_aggressive'], disableRulesetIds: ['ruleset_1'] },
      custom: { enableRulesetIds: ['ruleset_1'], disableRulesetIds: ['ruleset_standard', 'ruleset_aggressive'] }
    };

    await chrome.declarativeNetRequest.updateEnabledRulesets(rulesets[level] || rulesets.standard);
  }
});
