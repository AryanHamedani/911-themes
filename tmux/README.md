# Carrera for tmux

A dark, glare-free [tmux](https://github.com/tmux/tmux) theme inspired by the Porsche 911 Heritage Cockpit on a night drive: **Basalt Alcantara** (`#15171a` / `#101215`) instrument wells, warm **Chalk (`Kreide`)** (`#d6d2c7`) dial numerals, and a disciplined spark of **Carmine Red** (`#e1656c`).

Calibrated in OKLCH for long daily sessions and tuned to WCAG AA / APCA contrast targets.

## Files Included

- `carrera.conf` — Standalone tmux 24-bit RGB theme snippet covering status bar, window tabs, pane borders, copy mode, popups, menus, and clock mode.

## Manual Install

1. Copy `carrera.conf` to your tmux themes directory:

   ```sh
   mkdir -p ~/.config/tmux/themes
   cp carrera.conf ~/.config/tmux/themes/carrera.conf
   ```

2. Ensure truecolor (RGB) is enabled and source the theme in `~/.config/tmux/tmux.conf`:

   ```tmux
   set -g default-terminal "tmux-256color"
   set -ag terminal-overrides ",*:RGB"

   source-file ~/.config/tmux/themes/carrera.conf
   ```

3. Reload tmux when you are ready:

   ```sh
   tmux source-file ~/.config/tmux/tmux.conf
   ```

Palette reference: [`../colors.toml`](../colors.toml).

---

Not affiliated with or endorsed by Porsche AG. Porsche, 911 and Carrera are trademarks of Porsche AG.

License: [MIT](../LICENSE)
