document.addEventListener('DOMContentLoaded', async () => {
  const toggle = document.getElementById('toggle');
  const statusText = document.getElementById('status-text');
  const noteText = document.getElementById('note-text');

  // 1. Initialize UI based on saved state
  chrome.storage.local.get(['enabled'], (result) => {
    // Default to true if 'enabled' is undefined
    const isEnabled = result.enabled !== false;
    updateUI(isEnabled);
  });

  // 2. Handle toggle changes
  toggle.addEventListener('change', async () => {
    const isEnabled = toggle.checked;

    // Save state
    chrome.storage.local.set({ enabled: isEnabled });

    // Update blocking rules
    if (isEnabled) {
      // Enable the static ruleset defined in manifest.json
      await chrome.declarativeNetRequest.updateEnabledRulesets({
        enableRulesetIds: ['ruleset_1']
      });
    } else {
      // Disable the static ruleset
      await chrome.declarativeNetRequest.updateEnabledRulesets({
        disableRulesetIds: ['ruleset_1']
      });
    }

    updateUI(isEnabled);
    
    // Optional: Reload current tab to apply changes immediately
    // chrome.tabs.reload(); 
  });

  function updateUI(isEnabled) {
    toggle.checked = isEnabled;
    if (isEnabled) {
      statusText.textContent = 'Active';
      statusText.className = 'status-text active';
      noteText.textContent = 'Ad blocking is ON. Refresh page to see changes.';
    } else {
      statusText.textContent = 'Disabled';
      statusText.className = 'status-text disabled';
      noteText.textContent = 'Ad blocking is OFF.';
    }
  }
});
