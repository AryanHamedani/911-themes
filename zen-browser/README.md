# 911 (`992.2`) for Zen Browser

Precision Night Cockpit dark theme for Zen Browser (`userChrome.css` + `userContent.css`), crafted with a 4-plane surface hierarchy and aligned strictly with [`../colors.toml`](../colors.toml).

## Coverage

- `userChrome.css`:
  - Full Zen (`1.24.x`) & Firefox LWT/Proton design tokens across the 4-plane cockpit hierarchy (`#0a0b0d` diffuser shadow, `#0c0e11`/`#0f1114` recessed chrome & compact-mode drawer, `#141619`/`#131519` canvas & Race-Tex toolbars, `#1a1d23`/`#1d2026` Vanadium elevated popovers/URL bar, `#261b1f`/`#292d36` Smoked Carmine & Slate selection).
  - Vertical tabs, pending/unloaded tab dimming, multiselected tabs, pinned tabs separator, Essentials tiles, and Zen Folders (including folder search popup & overflow badges).
  - Workspace switcher & current workspace header with Guards Red (`#e55c5a`) active indicators.
  - Floating & docked URL bar with Guards Red focus ring, semantic HTTPS/chromeUI security icons, search-mode AA pill (`#bf3b3e`/`#f4f3ef`), and Smoked Carmine autocomplete selection.
  - Split-view splitters, active pane outline, dropzone, and Zen Glance overlay.
  - Compact Mode floating sidebar drawer, sidebar media controls card, status pill, findbar (including not-found state), context menus, downloads/extensions popups, and thin scrollbars with `prefers-reduced-motion` support.
- `userContent.css`:
  - Strictly scoped via `@-moz-document` to internal `about:*` pages (`about:newtab`, `about:home`, `about:blank`, `about:preferences`, `about:addons`, `about:config`, `about:privatebrowsing`) so external websites are never modified or broken.

## Installation

1. Copy `userChrome.css` and `userContent.css` into your Zen profile's `chrome/` directory (`~/.config/zen/<profile>/chrome/`).
2. In `about:config`, set `toolkit.legacyUserProfileCustomizations.stylesheets` to `true` and restart Zen Browser.

---

Not affiliated with or endorsed by Porsche AG. Licensed under [MIT](../LICENSE).
