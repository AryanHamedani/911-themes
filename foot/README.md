# 911 for foot

A dark, glare-free [foot](https://codeberg.org/dnkl/foot) terminal theme inspired by the **Porsche 911 (`992.2`) Precision Night Cockpit**: **Race-Tex Charcoal** (`#141619`) surfaces, **Ice Grey (Crayon)** (`#dadad6`) dial typography, and a disciplined spark of **Guards/Carmine Red** (`#e55c5a`).

Calibrated in OKLCH for long daily sessions and verified to WCAG AA contrast targets.

## Files Included

- `911.ini` — Complete `[colors-dark]` + `[csd]` INI theme covering foreground/background, selection, cursor, jump labels, scrollback indicator, search match/no-match badges, URL highlight, bell flash, normal/bright/dim ANSI 0–15, and client-side decorations.

## Manual Install

1. Copy `911.ini` to your foot themes directory:

   ```sh
   mkdir -p ~/.config/foot/themes
   cp 911.ini ~/.config/foot/themes/911.ini
   ```

2. Include it in `~/.config/foot/foot.ini` under `[main]`:

   ```ini
   [main]
   include=~/.config/foot/themes/911.ini
   ```

> On Omarchy with the active `911` theme, `~/.config/foot/foot.ini` already includes `~/.local/state/omarchy/current/theme/foot.ini`.

Palette reference: [`../colors.toml`](../colors.toml).

---

Not affiliated with or endorsed by Porsche AG. Porsche and 911 are trademarks of Porsche AG.

License: [MIT](../LICENSE)
