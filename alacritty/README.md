# Carrera for Alacritty

A dark, glare-free [Alacritty](https://alacritty.org) terminal theme inspired by the Porsche 911 Heritage Cockpit on a night drive: **Basalt Alcantara** (`#15171a`) surfaces, warm **Chalk (`Kreide`)** (`#d6d2c7`) dial numerals, and a disciplined spark of **Carmine Red** (`#e1656c`).

Calibrated in OKLCH for long daily sessions and tuned to WCAG AA / APCA contrast targets.

## Files Included

- `carrera.toml` — Complete `[colors.*]` TOML color theme.

## Cursor Note

By default, `carrera.toml` sets `[colors.cursor]` and `[colors.vi_mode_cursor]` to `#e1656c` (Carmine Red) with `#15171a` text, matching `colors.toml`. If you prefer the Chalk (`Kreide`) cursor rendered by Omarchy runtime templates, set `cursor = "#eae6dc"`.

## Manual Install

1. Copy `carrera.toml` to your Alacritty themes directory:

   ```sh
   mkdir -p ~/.config/alacritty/themes
   cp carrera.toml ~/.config/alacritty/themes/carrera.toml
   ```

2. Import it in `~/.config/alacritty/alacritty.toml`:

   ```toml
   [general]
   import = ["~/.config/alacritty/themes/carrera.toml"]
   ```

Palette reference: [`../colors.toml`](../colors.toml).

---

Not affiliated with or endorsed by Porsche AG. Porsche, 911 and Carrera are trademarks of Porsche AG.

License: [MIT](../LICENSE)
