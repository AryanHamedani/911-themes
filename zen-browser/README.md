# 911 (`992.2`) for Zen Browser

Precision Night Cockpit dark theme for Zen Browser (`userChrome.css` + `userContent.css`), aligned with [`../colors.toml`](../colors.toml).

## Coverage

- `userChrome.css`: Full Zen & Firefox LWT tokens, 4-plane cockpit surfaces (`#0a0b0d`, `#0c0e11`, `#0f1114`, `#131519`, `#141619`, `#1a1d23`, `#1d2026`), Guards Red focus & active tab indicator (`#e55c5a`), Smoked Carmine URL bar selection (`#261b1f`), AA badges (`#bf3b3e` / `#f4f3ef`), findbar, context menus, splitters, and scrollbars.
- `userContent.css`: Strictly scoped to `@-moz-document url-prefix("about:")` (New Tab, Preferences, Add-ons, `about:config`) so external websites remain untouched.

## Installation

1. Copy `userChrome.css` and `userContent.css` into your Zen profile's `chrome/` directory (`~/.config/zen/<profile>/chrome/`).
2. In `about:config`, set `toolkit.legacyUserProfileCustomizations.stylesheets` to `true` and restart Zen Browser.

---

Not affiliated with or endorsed by Porsche AG. Licensed under [MIT](../LICENSE).
