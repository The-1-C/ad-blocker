
import json

file_path = 'c:/Users/Kaden/Desktop/Projects/ad-blocker/rules.json'

with open(file_path, 'r') as f:
    current_rules = json.load(f)

# Find the highest ID used
max_id = 0
for rule in current_rules:
    if rule['id'] > max_id:
        max_id = rule['id']

start_id = max_id + 1

new_domains = [
    "cdn.adsgravity.io",
    "adroll.com",
    "adsrvr.org",
    "bluekai.com",
    "exelator.com",
    "quantserve.com",
    "scorecardresearch.com",
    "zedo.com",
    "advertising.com",
    "adtechus.com",
    "smartadserver.com",
    "spotxchange.com",
    "adcolony.com",
    "unityads.unity3d.com",
    "vungle.com",
    "applovin.com",
    "chartboost.com",
    "inmobi.com",
    "ironsrc.com",
    "tapjoy.com",
    "startapp.com"
]

current_id = start_id

for domain in new_domains:
    # Check if already exists to avoid duplicates
    exists = False
    for rule in current_rules:
        if rule['condition']['urlFilter'] == domain:
            exists = True
            break
    
    if not exists:
        rule = {
            "id": current_id,
            "priority": 1,
            "action": {"type": "block"},
            "condition": {
                "urlFilter": domain,
                "domainType": "thirdParty",
                "resourceTypes": ["script", "image", "xmlhttprequest", "sub_frame"]
            }
        }
        current_rules.append(rule)
        current_id += 1

with open(file_path, 'w') as f:
    json.dump(current_rules, f, indent=2)

print(f"Added {current_id - start_id} new rules.")
