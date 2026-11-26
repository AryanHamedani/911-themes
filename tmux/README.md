# 911 for tmux

A dark, glare-free [tmux](https://github.com/tmux/tmux) theme inspired by the **Porsche 911 (`992.2`) Precision Night Cockpit**: **Race-Tex Chrome** (`#131519`) status bar, **Guards Red** (`#bf3b3e`) session badge with `#f4f3ef` ink (`4.84:1` AA), **Vanadium Grey** (`#1d2026`) active window tab, and **Guards/Carmine Red** (`#e55c5a`) active pane borders.

Calibrated in OKLCH for long daily sessions and verified to WCAG AA contrast targets.

## Files Included

- `911.conf` — Complete tmux styling covering status bar, session/mode indicators, active/last/activity/bell window tabs, pane borders and display-panes overlays, messages, command prompt, copy-mode selection/match/current-match/mark highlights, 24-hour clock mode, and rounded popups/menus.

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
