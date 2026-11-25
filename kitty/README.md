# Carrera for Kitty

A dark, glare-free [Kitty](https://sw.kovidgoyal.net/kitty/) terminal theme inspired by the Porsche 911 Heritage Cockpit on a night drive: **Basalt Alcantara** (`#15171a`) surfaces, warm **Chalk (`Kreide`)** (`#d6d2c7`) dial numerals, and a disciplined spark of **Carmine Red** (`#e1656c`).

Calibrated in OKLCH for long daily sessions and tuned to WCAG AA / APCA contrast targets.

## Files Included

- `carrera.conf` — Kitty color, cursor, tab bar, border, and 16-color ANSI palette definitions.

## Cursor Note

By default, `carrera.conf` sets `cursor #e1656c` and `cursor_text_color #15171a` (Carmine Red cursor, matching `colors.toml`). If you prefer the Chalk (`Kreide`) cursor rendered by Omarchy runtime templates, set `cursor #eae6dc`.

## Manual Install

1. Copy `carrera.conf` to your Kitty themes directory:

   ```sh
   mkdir -p ~/.config/kitty/themes
   cp carrera.conf ~/.config/kitty/themes/carrera.conf
   ```

2. Include it in `~/.config/kitty/kitty.conf`:

   ```conf
   include themes/carrera.conf
   ```

Palette reference: [`../colors.toml`](../colors.toml).

---

Not affiliated with or endorsed by Porsche AG. Porsche, 911 and Carrera are trademarks of Porsche AG.

License: [MIT](../LICENSE)
