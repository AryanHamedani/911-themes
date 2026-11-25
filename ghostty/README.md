# Carrera for Ghostty

A dark, glare-free [Ghostty](https://ghostty.org) terminal theme inspired by the Porsche 911 Heritage Cockpit on a night drive: **Basalt Alcantara** (`#15171a`) surfaces, warm **Chalk (`Kreide`)** (`#d6d2c7`) dial numerals, and a disciplined spark of **Carmine Red** (`#e1656c`).

Calibrated in OKLCH for long daily sessions and tuned to WCAG AA / APCA contrast targets.

## Files Included

- `carrera` — Standalone Ghostty theme file (no extension).

## Cursor Note

By default, `carrera` sets `cursor-color = #e1656c` and `cursor-text = #15171a` (Carmine Red cursor, matching `colors.toml`). If you prefer the Chalk (`Kreide`) cursor rendered by Omarchy runtime templates, set `cursor-color = #eae6dc`.

## Manual Install

1. Copy `carrera` to your Ghostty themes directory:

   ```sh
   mkdir -p ~/.config/ghostty/themes
   cp carrera ~/.config/ghostty/themes/carrera
   ```

2. Reference it in `~/.config/ghostty/config`:

   ```ini
   theme = carrera
   ```

   Or load it directly as an optional config file:

   ```ini
   config-file = ?"~/.config/ghostty/themes/carrera"
   ```

3. Validate the theme file:

   ```sh
   ghostty +validate-config --config-file=~/.config/ghostty/themes/carrera
   ```

Palette reference: [`../colors.toml`](../colors.toml).

---

Not affiliated with or endorsed by Porsche AG. Porsche, 911 and Carrera are trademarks of Porsche AG.

License: [MIT](../LICENSE)
