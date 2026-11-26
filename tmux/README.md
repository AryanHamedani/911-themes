# 911 for tmux

A dark, glare-free [tmux](https://github.com/tmux/tmux) theme inspired by the **Porsche 911 (`992.2`) Precision Night Cockpit**: **Race-Tex Chrome** (`#131519`) status bar, **Guards Red** (`#bf3b3e` / `#f4f3ef`, `4.84:1` AA) state-reactive session badge, **Smoked Carmine** (`#261b1f`) active window tab with a **Guards Red** (`#e55c5a`) focus needle, and **Vanadium Elevated** (`#1a1d23`) rounded popups and menus.

Calibrated in OKLCH for 8-hour daily sessions and verified to WCAG AA (`>= 4.5:1`) across every readable foreground/background pair.

## Files Included

- `911.conf` — Complete tmux (`3.8`) styling covering:
  - **Status bar & session badge**: Race-Tex Chrome (`#131519`) bar with a Guards Red (`#bf3b3e`/`#f4f3ef`) session badge that shifts to PCCB Racing Gold (`#e0be66`/`#0a0b0d`) on `client_prefix` and Lava Orange (`#e89158`/`#0a0b0d`) in copy-mode, plus quiet telemetry and active-only `COPY`, `PREFIX`, `SYNC`, and `ZOOM` pills.
  - **Window tabs**: Calm muted inactive tabs (`#858a96`), brushed-silver last-visited tab (`#b4b7be`), Smoked Carmine (`#261b1f`) active tab with Guards Red `▎` needle and Glacier Cyan `Z` zoom indicator, and distinct activity (`#282721`/`#e0be66`) and bell (`#2a2124`/`#f48583`) states.
  - **Panes & overlays**: Single-line precision split borders (`#434854` inactive, `#e55c5a` active, `colour` half-border indicator), pre-styled `pane-border-format` (with `pane-border-status` off by default), and AA `display-panes` overlays.
  - **Messages & command prompt**: Vanadium elevated (`#1a1d23`) prompt bar with Guards Red / Racing Gold prompt cursors (`prompt-cursor-colour`, `prompt-command-cursor-colour`).
  - **Copy mode**: Slate Grey Neo selection (`#292d36`/`#edede9`), canonical search matches (`#5b5134`/`#edede9`), Guards Red current match (`#bf3b3e`/`#f4f3ef`), Smoked Carmine mark line (`#261b1f`/`#e89158`), muted-badge position pill (`#363b47`/`#f4f3ef`), Vanadium cursorline (`#1d2026`), and gutter line-number styling.
  - **Popups, menus & clock**: Rounded popups and menus on `#1a1d23` with `#2f3440` hairline borders and Smoked Carmine (`#261b1f`/`#edede9`) selected item, plus 24-hour Guards Red clock mode.

## Manual Install

1. Copy `911.conf` to `~/.config/tmux/911.conf`:

   ```sh
   mkdir -p ~/.config/tmux
   cp 911.conf ~/.config/tmux/911.conf
   ```

2. Source it from `~/.config/tmux/tmux.conf`:

   ```tmux
   source-file ~/.config/tmux/911.conf
   ```

Palette reference: [`../colors.toml`](../colors.toml).

---

Not affiliated with or endorsed by Porsche AG. Porsche and 911 are trademarks of Porsche AG.

License: [MIT](../LICENSE)
