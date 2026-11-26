# 911 for Kitty

A dark, glare-free [Kitty](https://sw.kovidgoyal.net/kitty/) terminal theme inspired by the **Porsche 911 (`992.2`) Precision Night Cockpit**: **Race-Tex Charcoal** (`#141619`) surfaces, **Ice Grey (Crayon)** (`#dadad6`) dial typography, and a disciplined spark of **Guards/Carmine Red** (`#e55c5a`).

Calibrated in OKLCH for long daily sessions and verified to WCAG AA contrast targets.

## Files Included

- `911.conf` — Complete Kitty color theme covering foreground/background, selection, cursor, URL highlight, visual bell, active/inactive/bell split borders, Wayland/macOS titlebar, tab bar (with AA Guards Red active tab badge), marks 1–3, and all 16 ANSI colors.

## Manual Install

1. Copy `911.conf` to your Kitty themes directory:

   ```sh
   mkdir -p ~/.config/kitty/themes
   cp 911.conf ~/.config/kitty/themes/911.conf
   ```

2. Include it in `~/.config/kitty/kitty.conf`:

   ```conf
   include themes/911.conf
   ```

> On Omarchy with the active `911` theme, `~/.config/kitty/kitty.conf` already includes `~/.local/state/omarchy/current/theme/kitty.conf`.

Palette reference: [`../colors.toml`](../colors.toml).

---

Not affiliated with or endorsed by Porsche AG. Porsche and 911 are trademarks of Porsche AG.

License: [MIT](../LICENSE)
