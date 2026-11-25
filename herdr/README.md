# Carrera for Herdr

A dark, glare-free [Herdr](https://github.com/herdr-sh/herdr) multiplexer theme inspired by the Porsche 911 Heritage Cockpit on a night drive: **Basalt Alcantara** (`#15171a`) surfaces, warm **Chalk (`Kreide`)** (`#d6d2c7`) dial numerals, and a disciplined spark of **Carmine Red** (`#e1656c`).

Calibrated in OKLCH for long daily sessions and tuned to WCAG AA / APCA contrast targets.

## Files Included

- `carrera.toml` — Herdr `[theme]`, `[theme.custom]` (all 19 custom color tokens), and `[ui]` accent configuration.

## Manual Install

Herdr reads a single configuration file (`~/.config/herdr/config.toml`) and does not currently support external file `include` directives.

1. Merge the `[theme]`, `[theme.custom]`, and `[ui]` sections from `carrera.toml` into `~/.config/herdr/config.toml` (replacing any existing `[theme]` / `[theme.custom]` / `[ui].accent` entries).
2. Verify the configuration without launching Herdr:

   ```sh
   HERDR_CONFIG_PATH=~/.config/herdr/config.toml herdr config check
   ```

Palette reference: [`../colors.toml`](../colors.toml).

---

Not affiliated with or endorsed by Porsche AG. Porsche, 911 and Carrera are trademarks of Porsche AG.

License: [MIT](../LICENSE)
