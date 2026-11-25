# Carrera for Fastfetch

Porsche 911 Heritage Cockpit (`Carrera v2.0.0`) theme for [Fastfetch](https://github.com/fastfetch-cli/fastfetch) — Basalt Alcantara (`#15171a`), Chalk (`#d6d2c7`), GT Silver (`#9599a2`), and Carmine Red (`#e1656c`).

## Files

- `carrera.jsonc` — Fastfetch JSONC color configuration (`logo.color`, `display.color`, `display.percent.color`, `display.bar.color`, `display.temp.color`) using exact `colors.toml` hex values (requires Fastfetch >= v2.42.0).

## Installation

1. Copy `carrera.jsonc` to `~/.config/fastfetch/carrera.jsonc`:

   ```bash
   mkdir -p ~/.config/fastfetch
   cp carrera.jsonc ~/.config/fastfetch/carrera.jsonc
   ```

2. Run with `fastfetch --config ~/.config/fastfetch/carrera.jsonc`, or merge the `logo` and `display` blocks manually into `~/.config/fastfetch/config.jsonc` (this repository does not modify your active config).

## Verification

```bash
fastfetch --config carrera.jsonc --logo none --structure Title:OS:CPU:Memory
```

## License

[MIT](../LICENSE) — Copyright (c) 2026 Aryan Hamedani.

Not affiliated with or endorsed by Porsche AG. Porsche, 911 and Carrera are trademarks of Porsche AG.
