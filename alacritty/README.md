# 911 for Alacritty

A dark, glare-free [Alacritty](https://alacritty.org) terminal theme inspired by the **Porsche 911 (`992.2`) Precision Night Cockpit**: **Race-Tex Charcoal** (`#141619`) surfaces, **Ice Grey (Crayon)** (`#dadad6`) dial typography, and a disciplined spark of **Guards/Carmine Red** (`#e55c5a`).

Calibrated in OKLCH for long daily sessions and verified to WCAG AA contrast targets.

## Files Included

- `911.toml` — Complete `[colors.*]` + `[bell]` TOML theme covering primary, cursor, vi-mode cursor, search matches, hints, line indicator, elevated Vanadium footer bar, selection, normal/bright/dim ANSI 0–15, `draw_bold_text_with_bright_colors = false`, and Smoked Carmine visual bell.

## Manual Install

1. Copy `911.toml` to your Alacritty themes directory:

   ```sh
   mkdir -p ~/.config/alacritty/themes
   cp 911.toml ~/.config/alacritty/themes/911.toml
   ```

2. Import it in `~/.config/alacritty/alacritty.toml`:

   ```toml
   [general]
   import = ["~/.config/alacritty/themes/911.toml"]
   ```

> On Omarchy with the active `911` theme, `~/.config/alacritty/alacritty.toml` already imports `~/.local/state/omarchy/current/theme/alacritty.toml`.

Palette reference: [`../colors.toml`](../colors.toml).

---

Not affiliated with or endorsed by Porsche AG. Porsche and 911 are trademarks of Porsche AG.

License: [MIT](../LICENSE)
