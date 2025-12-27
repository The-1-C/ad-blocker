// Content script for cosmetic filtering (hiding ad elements)

// Common ad-related selectors to hide
const AD_SELECTORS = [
  '.ad',
  '.ads',
  '.advertisement',
  '.advertising',
  '.advert',
  '[id*="ad-"]',
  '[id*="ads"]',
  '[id*="advert"]',
  '[id*="google_ads"]',
  '[class*="ad-"]',
  '[class*="ads-"]',
  '[class*="advert"]',
  '[class*="advertisement"]',
  '.banner-ad',
  '.ad-banner',
  '.ad-box',
  '.ad-container',
  '.ad-space',
  '.ad-unit',
  '.sponsored',
  '[data-ad-slot]',
  '[data-ad-format]',
  'ins.adsbygoogle'
];

// Hide ads on page load
function hideAds() {
  try {
    AD_SELECTORS.forEach(selector => {
      try {
        const elements = document.querySelectorAll(selector);
        elements.forEach(el => {
          // Only hide if it's likely an ad (has some size)
          if (el.offsetHeight > 20 && el.offsetWidth > 20) {
            el.style.display = 'none';
            // Report to background script
            chrome.runtime.sendMessage({
              action: 'trackBlock',
              url: window.location.href
            }).catch(() => {
              // Background not listening, that's okay
            });
          }
        });
      } catch (e) {
        // Invalid selector, skip
      }
    });
  } catch (e) {
    console.error('Ad hiding error:', e);
  }
}

// Run on page load
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', hideAds);
} else {
  hideAds();
}

// Watch for dynamically injected ads
try {
  const observer = new MutationObserver(() => {
    hideAds();
  });

  observer.observe(document.documentElement, {
    childList: true,
    subtree: true
  });
} catch (e) {
  console.error('MutationObserver error:', e);
}

// Override common ad APIs to prevent them from loading
try {
  window.googletag = window.googletag || {
    cmd: [],
    display: () => {},
    defineSlot: () => ({
      addService: () => ({}),
      setTargeting: () => ({})
    })
  };

  window.adsbygoogle = window.adsbygoogle || [];
} catch (e) {
  // Can't override, that's okay
}
