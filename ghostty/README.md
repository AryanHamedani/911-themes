# 911 for Ghostty

A dark, glare-free [Ghostty](https://ghostty.org) terminal theme inspired by the **Porsche 911 (`992.2`) Precision Night Cockpit**: **Race-Tex Charcoal** (`#141619`) surfaces, **Ice Grey (Crayon)** (`#dadad6`) dial typography, and a disciplined spark of **Guards/Carmine Red** (`#e55c5a`).

Calibrated in OKLCH for long daily sessions and verified to WCAG AA contrast targets.

## Files Included

- `911` — Complete Ghostty theme covering background/foreground, cursor, selection, split divider, unfocused split fill, search match/selected-match highlights, and all 16 ANSI palette entries.

## Manual Install

1. Copy `911` to your Ghostty themes directory:

   ```sh
   mkdir -p ~/.config/ghostty/themes
   cp 911 ~/.config/ghostty/themes/911
   ```

2. Enable it in `~/.config/ghostty/config`:

   ```ini
   theme = 911
   ```

> On Omarchy with the active `911` theme, `~/.config/ghostty/config` already includes `~/.local/state/omarchy/current/theme/ghostty.conf`.

Palette reference: [`../colors.toml`](../colors.toml).

---

Not affiliated with or endorsed by Porsche AG. Porsche and 911 are trademarks of Porsche AG.

License: [MIT](../LICENSE)
