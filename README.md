# Simple Ad Blocker Extension

A simple Chrome extension that blocks ads using the Declarative Net Request API.

## Installation

1. Open Chrome and navigate to `chrome://extensions/`.
2. Enable **Developer mode** in the top right corner.
3. Click **Load unpacked**.
4. Select this directory (`ad-blocker`).

## Features

- **Secure & Private**: Uses the privacy-preserving `declarativeNetRequest` API. No history tracking.
- **Lightweight**: Blocks requests to common ad servers (doubleclick, googleadservices, etc.).
- **Safe Defaults**: Only blocks third-party ad resources.

## Customization

You can add more blocking rules in `rules.json`.
