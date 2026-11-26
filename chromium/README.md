# 911 (`992.2`) for Chromium

Precision Night Cockpit dark theme for Chromium, aligned with [`../colors.toml`](../colors.toml) and `omarchy-911-theme/chromium.theme`.

## Files

- `chromium.theme` — Omarchy RGB triplet (`20,22,25` = `#141619` Race-Tex Charcoal).
- `manifest.json` — Standalone Manifest V3 Chromium theme extension covering 30 chrome, tab, omnibox, control, and NTP color slots, calibrated `tints`, and `properties` following the 911 4-plane depth and 5-step foreground hierarchy:
  - **Surfaces**: `#0a0b0d` (unfocused incognito) -> `#0c0e11` (inactive/incognito frame) -> `#0f1114` (active frame & tab strip well) -> `#141619` (toolbar, active tab, NTP canvas) -> `#1a1d23` (omnibox & NTP header) -> `#1d2026` (button/control fills)
  - **Typography & Icons**: `#edede9` (active tab) -> `#dadad6` (toolbar, omnibox & NTP text) -> `#b4b7be` (bookmarks, toolbar icons & NTP section headers) -> `#9297a2` (inactive tabs) -> `#858a96` (unfocused inactive tabs)
  - **Links**: `#6fa2de` (Lugano Blue on NTP and NTP sections)

## Installation

1. Open `chrome://extensions` and enable **Developer mode**.
2. Click **Load unpacked** and select this `chromium/` directory.

> **Omarchy note**: Omarchy's active `911` theme already applies `chromium.theme` (`20,22,25`) automatically.

---

Not affiliated with or endorsed by Porsche AG. Licensed under [MIT](../LICENSE).
