# Carrera for Starship

A dark, glare-free [Starship](https://starship.rs) prompt theme inspired by the Porsche 911 Heritage Cockpit on a night drive: **Basalt Alcantara** (`#15171a`) surfaces, warm **Chalk (`Kreide`)** (`#d6d2c7`) dial numerals, and a disciplined spark of **Carmine Red** (`#e1656c`).

Calibrated in OKLCH for long daily sessions and tuned to WCAG AA / APCA contrast targets.

## Files Included

- `carrera.toml` — Complete standalone Starship configuration defining `[palettes.carrera]`, `palette = "carrera"`, and styled prompt modules.

## Manual Install

### Option A: Use as your Starship config

1. Back up your existing configuration, then copy `carrera.toml` to `~/.config/starship.toml`:

   ```sh
   cp -n ~/.config/starship.toml ~/.config/starship.toml.bak 2>/dev/null || true
   cp carrera.toml ~/.config/starship.toml
   ```

   Or test it temporarily via `STARSHIP_CONFIG` without modifying `~/.config/starship.toml`:

   ```sh
   STARSHIP_CONFIG=/path/to/carrera.toml starship print-config
   ```

### Option B: Add the palette to an existing config

Copy `palette = "carrera"` (near the top of `~/.config/starship.toml`) and the `[palettes.carrera]` table from `carrera.toml` into your existing Starship configuration, then reference tokens such as `accent`, `blue`, `green`, `yellow`, `orange`, `cyan`, `red`, or `muted` in your module `style` fields.

Palette reference: [`../colors.toml`](../colors.toml).

---

Not affiliated with or endorsed by Porsche AG. Porsche, 911 and Carrera are trademarks of Porsche AG.

License: [MIT](../LICENSE)
