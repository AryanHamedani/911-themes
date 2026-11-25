# Carrera for foot

A dark, glare-free [foot](https://codeberg.org/dnkl/foot) terminal theme inspired by the Porsche 911 Heritage Cockpit on a night drive: **Basalt Alcantara** (`#15171a`) surfaces, warm **Chalk (`Kreide`)** (`#d6d2c7`) dial numerals, and a disciplined spark of **Carmine Red** (`#e1656c`).

Calibrated in OKLCH for long daily sessions and tuned to WCAG AA / APCA contrast targets.

## Files Included

- `carrera.ini` — `[colors-dark]` palette definition using 6-digit hex values (without `#`, as required by `foot.ini(5)`).

## Cursor Note

By default, `carrera.ini` sets `cursor=15171a e1656c` (Carmine Red cursor with Basalt text, matching `colors.toml`). If you prefer the Chalk (`Kreide`) cursor rendered by Omarchy runtime templates, replace the `cursor` line with:

```ini
cursor=15171a eae6dc
```

## Manual Install

1. Copy `carrera.ini` to your foot themes directory:

   ```sh
   mkdir -p ~/.config/foot/themes
   cp carrera.ini ~/.config/foot/themes/carrera.ini
   ```

2. Add the include path under `[main]` in `~/.config/foot/foot.ini`:

   ```ini
   [main]
   include=~/.config/foot/themes/carrera.ini
   ```

3. Validate your configuration without applying it live:

   ```sh
   foot -c ~/.config/foot/foot.ini --check-config
   ```

Palette reference: [`../colors.toml`](../colors.toml).

---

Not affiliated with or endorsed by Porsche AG. Porsche, 911 and Carrera are trademarks of Porsche AG.

License: [MIT](../LICENSE)
