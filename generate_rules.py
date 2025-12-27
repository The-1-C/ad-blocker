#!/usr/bin/env python3
"""
Generate DNR rules from EasyList and other filter lists.
Fetches updated lists and converts them to Chrome Declarative Net Request format.
"""

import json
import requests
from urllib.parse import urlparse
from datetime import datetime

# URLs for various filter lists
FILTER_LISTS = {
    'easylist': 'https://easylist.to/easylist/easylist.txt',
    'easyprivacy': 'https://easylist.to/easylist/easyprivacy.txt',
    'ublock_ads': 'https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/filters.txt',
    'ublock_privacy': 'https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/privacy.txt',
}

# Known trackers and ad networks (fallback)
KNOWN_TRACKERS = [
    'doubleclick.net', 'googleadservices.com', 'googlesyndication.com',
    'analytics.google.com', 'google-analytics.com', 'pagead.googlesyndication.com',
    'ads.facebook.com', 'connect.facebook.net', 'pixel.facebook.com',
    'amazon-adsystem.com', 'media.net', 'ads.linkedin.com', 'ads.twitter.com',
    'analytics.twitter.com', 'bat.bing.com', 'taboola.com', 'outbrain.com',
    'criteo.com', 'scorecardresearch.com', 'hotjar.com', 'mouseflow.com',
    'fullstory.com', 'segment.com', 'mixpanel.com', 'amplitude.com',
    'drift.com', 'intercom.io', 'sentry.io', 'bugsnag.com',
    'googletagmanager.com', 'adservice.google.com', 'advertising.apple.com',
    'adcolony.com', 'unityads.unity3d.com', 'appodeal.com', 'openx.com',
    'pubmatic.com', 'onetag.com', 'districtm.io', 'synacor.com',
    'adn.inmobi.com', 'adform.net', 'bidswitch.net', 'c.amazon-adsystem.com'
]


def fetch_filter_list(url):
    """Fetch filter list from URL."""
    try:
        print(f"Fetching {url}...")
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.text.split('\n')
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return []


def extract_domains_from_adblock(lines):
    """Extract domains from Adblock filter syntax."""
    domains = set()

    for line in lines:
        line = line.strip()
        
        # Skip comments and empty lines
        if not line or line.startswith('!') or line.startswith('['):
            continue

        # Parse domain rules (simplified)
        # Format: ||example.com^ or ||example.com^$script,image
        if line.startswith('||'):
            # Extract domain
            domain = line[2:].split('^')[0].split('$')[0].strip()
            if domain and '/' not in domain:  # Only pure domains, not paths
                domains.add(domain)

        # Format: ^domain  (with pipe syntax)
        elif '||' in line:
            parts = line.split('||')
            for part in parts[1:]:
                domain = part.split('^')[0].split('/')[0].split('$')[0].strip()
                if domain:
                    domains.add(domain)

    return domains


def generate_dnr_rules(domains, start_id=1):
    """Convert domains to DNR rules."""
    rules = []
    rule_id = start_id

    for domain in sorted(domains):
        rule = {
            "id": rule_id,
            "priority": 1,
            "action": {"type": "block"},
            "condition": {
                "urlFilter": domain,
                "domainType": "thirdParty",
                "resourceTypes": ["script", "image", "xmlhttprequest", "sub_frame"]
            }
        }
        rules.append(rule)
        rule_id += 1

    return rules


def main():
    print("Generating ad-blocking rules from filter lists...")
    all_domains = set(KNOWN_TRACKERS)

    # Fetch from filter lists
    for name, url in FILTER_LISTS.items():
        print(f"\nProcessing {name}...")
        lines = fetch_filter_list(url)
        domains = extract_domains_from_adblock(lines)
        print(f"Found {len(domains)} domains from {name}")
        all_domains.update(domains)

    print(f"\nTotal unique domains: {len(all_domains)}")

    # Split into standard and aggressive rulesets
    # Standard: most common trackers
    standard_domains = list(all_domains)[:100]
    aggressive_domains = list(all_domains)

    # Generate rules
    standard_rules = generate_dnr_rules(standard_domains, start_id=1)
    aggressive_rules = generate_dnr_rules(aggressive_domains, start_id=len(standard_rules) + 1)

    # Save to files
    with open('rules-standard.json', 'w') as f:
        json.dump(standard_rules, f, indent=2)
    print(f"Saved {len(standard_rules)} rules to rules-standard.json")

    with open('rules-aggressive.json', 'w') as f:
        json.dump(aggressive_rules, f, indent=2)
    print(f"Saved {len(aggressive_rules)} rules to rules-aggressive.json")

    # Log timestamp
    with open('_metadata/rules_generated.txt', 'w') as f:
        f.write(f"Rules generated: {datetime.now().isoformat()}\n")
        f.write(f"Standard rules: {len(standard_rules)}\n")
        f.write(f"Aggressive rules: {len(aggressive_rules)}\n")
        f.write(f"Total unique domains: {len(all_domains)}\n")

    print(f"\nGeneration complete! {datetime.now().isoformat()}")


if __name__ == '__main__':
    main()
