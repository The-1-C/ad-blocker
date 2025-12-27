#!/usr/bin/env python3
"""
Automated script to periodically update rules from filter lists.
Run this as a scheduled task or cron job.

Usage:
    python update_rules.py
"""

import json
import requests
import logging
from datetime import datetime
from pathlib import Path

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('_metadata/update.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

EASYLIST_URL = 'https://easylist.to/easylist/easylist.txt'
UBLOCK_ADS_URL = 'https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/filters.txt'


def fetch_rules(url):
    """Fetch ad-blocking rules from URL."""
    try:
        logger.info(f"Fetching rules from {url}...")
        response = requests.get(url, timeout=15)
        response.raise_for_status()
        return response.text.split('\n')
    except Exception as e:
        logger.error(f"Failed to fetch {url}: {e}")
        return []


def parse_adblock_rules(lines):
    """Parse Adblock format rules and extract domains."""
    domains = set()

    for line in lines:
        line = line.strip()
        
        # Skip comments and metadata
        if not line or line.startswith('!') or line.startswith('['):
            continue

        # Extract ||domain.com^ format
        if '||' in line:
            parts = line.split('||')
            for part in parts[1:]:
                domain = part.split('^')[0].split('$')[0].split('/')[0].strip()
                if domain and '.' in domain and not any(c in domain for c in ['*', ':', '?']):
                    domains.add(domain)

        # Extract |http patterns
        elif line.startswith('|http'):
            try:
                # Simple extraction of domain from URL pattern
                domain = line.split('://')[1].split('/')[0].split('$')[0].strip()
                if domain and '.' in domain:
                    domains.add(domain)
            except:
                pass

    return domains


def generate_rules_json(domains, start_id=1):
    """Convert domains to DNR rule format."""
    rules = []
    
    for idx, domain in enumerate(sorted(domains), start=start_id):
        rule = {
            "id": idx,
            "priority": 1,
            "action": {"type": "block"},
            "condition": {
                "urlFilter": domain,
                "domainType": "thirdParty",
                "resourceTypes": ["script", "image", "xmlhttprequest", "sub_frame"]
            }
        }
        rules.append(rule)

    return rules


def save_rules(rules, filename):
    """Save rules to JSON file."""
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(rules, f, indent=2)
        logger.info(f"Saved {len(rules)} rules to {filename}")
        return True
    except Exception as e:
        logger.error(f"Failed to save {filename}: {e}")
        return False


def main():
    logger.info("=" * 60)
    logger.info("Starting rules update...")
    
    # Fetch rules from multiple sources
    all_domains = set()

    for url in [EASYLIST_URL, UBLOCK_ADS_URL]:
        lines = fetch_rules(url)
        if lines:
            domains = parse_adblock_rules(lines)
            logger.info(f"Found {len(domains)} domains from {url}")
            all_domains.update(domains)

    if not all_domains:
        logger.warning("No domains fetched! Using fallback rules...")
        # Fallback to common trackers
        all_domains = {
            'doubleclick.net', 'googleadservices.com', 'googlesyndication.com',
            'analytics.google.com', 'google-analytics.com', 'ads.facebook.com',
            'amazon-adsystem.com', 'media.net', 'ads.linkedin.com'
        }

    logger.info(f"Total unique domains: {len(all_domains)}")

    # Split into rule sets
    sorted_domains = sorted(list(all_domains))
    standard_domains = sorted_domains[:100]  # First 100 most common
    aggressive_domains = sorted_domains

    # Generate and save
    standard_rules = generate_rules_json(standard_domains, start_id=1)
    aggressive_rules = generate_rules_json(aggressive_domains, start_id=len(standard_rules) + 1)

    success = True
    success &= save_rules(standard_rules, 'rules-standard.json')
    success &= save_rules(aggressive_rules, 'rules-aggressive.json')

    # Update metadata
    if success:
        metadata = {
            'last_updated': datetime.now().isoformat(),
            'standard_rules_count': len(standard_rules),
            'aggressive_rules_count': len(aggressive_rules),
            'total_domains': len(all_domains),
            'sources': [EASYLIST_URL, UBLOCK_ADS_URL]
        }
        try:
            with open('_metadata/rules_metadata.json', 'w') as f:
                json.dump(metadata, f, indent=2)
            logger.info("Updated metadata")
        except Exception as e:
            logger.error(f"Failed to update metadata: {e}")

        logger.info("Rules update completed successfully!")
    else:
        logger.error("Rules update failed!")

    logger.info("=" * 60)


if __name__ == '__main__':
    main()
