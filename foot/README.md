# 911 for foot

A dark, glare-free [foot](https://codeberg.org/dnkl/foot) terminal theme inspired by the **Porsche 911 (`992.2`) Precision Night Cockpit**: **Race-Tex Charcoal** (`#141619`) surfaces, **Ice Grey (Crayon)** (`#dadad6`) dial typography, and a disciplined spark of **Guards/Carmine Red** (`#e55c5a`).

Calibrated in OKLCH for long daily sessions and verified to WCAG AA contrast targets.

## Files Included

- `911.ini` — Complete `[colors-dark]` (`RRGGBB`, no `#`) + `[csd]` (`AARRGGBB`, opaque `ff` prefix per `man 5 foot.ini`) INI theme covering foreground/background, selection, cursor, WCAG AA jump labels (`#bf3b3e`/`#f4f3ef`), muted scrollback indicator (`#363b47`/`#f4f3ef`), search match (`#5b5134`/`#edede9`) and no-match (`#bf3b3e`/`#f4f3ef`) badges, Lugano Blue URL highlights, restrained Guards Red bell flash (`0.25` alpha), full `regular0..7` / `bright0..7` / `dim0..7` palettes, and cockpit-matched client-side decorations.

## Cursor Note

- **Standalone (`911.ini`)**: Uses `cursor=0a0b0d e55c5a` (deep diffuser shadow ink on Guards/Carmine Red needle, `5.63:1` AA) per the standalone 911 suite policy.
- **Omarchy runtime**: When managed by Omarchy's active `911` theme, `/usr/bin/omarchy-theme-color` maps `cursor` to `bright_foreground` (`#edede9`), rendering `cursor=141619 edede9` in `~/.local/state/omarchy/current/theme/foot.ini`.

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
