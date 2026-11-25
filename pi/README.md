# Carrera for Pi Coding Agent

Porsche 911 Heritage Cockpit (`Carrera v2.0.0`) theme for [Pi Coding Agent](https://pi.dev/) — Basalt Alcantara (`#15171a`), Chalk (`#d6d2c7`), GT Silver (`#9599a2`), and Carmine Red (`#e1656c`).

## Files

- `carrera.json` — Pi theme (`$schema: "https://pi.dev/schemas/theme.schema.json"`, `appearance: "dark"`) with 31 `vars`, all 56 `ThemeJsonSchema` color tokens (51 required + 5 optional), and `export` backgrounds.

### Derived Hex Notes

Derived panel, selection, border, and muted/dim tokens in `vars` and `export` follow Omarchy's theme templates (`pi.json.tpl`) using linear sRGB `mix(start, end, amount)` over `colors.toml` v2.0.0 (`selectedBackground` `#42282c` 22%, `panel` `#212224` 6%, `panelAlt` `#282a2b` 10%, `panelPending`/`Success`/`Error` `#2d2024`/`#232a26`/`#2d2225` 12%, `border` `#4f4f4e` 30%, `borderMuted` `#3c3c3d` 20%, `mutedText` `#94928c` 34%, `dimText` `#72716d` 52%).

## Installation

1. Copy `carrera.json` to `~/.pi/agent/themes/carrera.json`:

   ```bash
   mkdir -p ~/.pi/agent/themes
   cp carrera.json ~/.pi/agent/themes/carrera.json
   ```

2. Select `carrera` via `/settings` inside Pi, or set it manually in `~/.pi/agent/settings.json` (this repository does not modify your active config):

   ```json
   {
     "theme": "carrera"
   }
   ```

## Verification

```bash
python3 -c 'import json; d=json.load(open("carrera.json")); assert d["name"]=="carrera" and d["appearance"]=="dark" and all(v in d["vars"] or v.startswith("#") for v in d["colors"].values())'
```

## License

[MIT](../LICENSE) — Copyright (c) 2026 Aryan Hamedani.

Not affiliated with or endorsed by Porsche AG. Porsche, 911 and Carrera are trademarks of Porsche AG.
