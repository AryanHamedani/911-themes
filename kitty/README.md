# 911 for Kitty

A dark, glare-free [Kitty](https://sw.kovidgoyal.net/kitty/) terminal theme inspired by the **Porsche 911 (`992.2`) Precision Night Cockpit**: **Race-Tex Charcoal** (`#141619`) surfaces, **Ice Grey (Crayon)** (`#dadad6`) dial typography, and a disciplined spark of **Guards/Carmine Red** (`#e55c5a`).

Calibrated in OKLCH for 8-hour daily engineering sessions and verified to WCAG AA contrast targets across every surface and badge.

## Files Included

- [`911.conf`](911.conf) — Complete Kitty color theme covering foreground/background, selection, cursor, URL highlight, Smoked Carmine visual bell, active/inactive/bell split borders, Wayland/macOS titlebar, 4-plane tab bar (with AA Guards Red active tab badge), AA/AAA marks 1–3, and all 16 ANSI colors.

## Design Highlights

- **Cockpit Surface Hierarchy**: Deep diffuser margin (`#0a0b0d`) → Deep carbon tab bar well (`#0c0e11`) → Race-Tex chrome titlebar & inactive tabs (`#131519`) → Race-Tex Charcoal terminal canvas (`#141619`) → Slate Grey Neo selection (`#292d36`) & Smoked Carmine visual bell (`#261b1f`).
- **Guards Red Discipline**: Active split border (`#e55c5a`), standalone cursor needle (`#e55c5a` with `#0a0b0d` ink, `5.63:1` AA), and filled active tab badge (`#bf3b3e` with `#f4f3ef` ink, `4.84:1` AA). Inactive tabs use GT Silver in shadow (`#9297a2` on `#131519`, `6.24:1` AA).
- **Accessible Marks 1–3**: Deep diffuser ink (`#0a0b0d`) on Lugano Blue (`#6fa2de`, `7.41:1` AAA), PCCB Racing Gold (`#e0be66`, `10.99:1` AAA), and Ultraviolet (`#b488cc`, `6.88:1` AA).

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

> **Omarchy note**: On Omarchy with the active `911` theme, `~/.config/kitty/kitty.conf` already includes `~/.local/state/omarchy/current/theme/kitty.conf` (which maps `cursor` to `bright_foreground` `#edede9` at runtime). Standalone `911.conf` uses the canonical `#e55c5a` Guards/Carmine Red cursor needle.

Palette reference: [`../colors.toml`](../colors.toml).

---

Not affiliated with or endorsed by Porsche AG. Porsche and 911 are trademarks of Porsche AG.

License: [MIT](../LICENSE)
