# Carrera for Atuin

A dark, glare-free [Atuin](https://atuin.sh) shell history theme inspired by the Porsche 911 Heritage Cockpit on a night drive: **Basalt Alcantara** (`#15171a`) surfaces, warm **Chalk (`Kreide`)** (`#d6d2c7`) dial numerals, and a disciplined spark of **Carmine Red** (`#e1656c`).

Calibrated in OKLCH for long daily sessions and tuned to WCAG AA / APCA contrast targets.

## Files Included

- `carrera.toml` — Atuin theme file defining `[theme] name = "carrera"` and all 15 PascalCase `[colors]` tokens.

## Manual Install

1. Copy `carrera.toml` to your Atuin themes directory (or `$ATUIN_THEME_DIR`):

   ```sh
   mkdir -p ~/.config/atuin/themes
   cp carrera.toml ~/.config/atuin/themes/carrera.toml
   ```

2. Select the theme in `~/.config/atuin/config.toml`:

   ```toml
   [theme]
   name = "carrera"
   ```

Palette reference: [`../colors.toml`](../colors.toml).

---

Not affiliated with or endorsed by Porsche AG. Porsche, 911 and Carrera are trademarks of Porsche AG.

License: [MIT](../LICENSE)
