# Carrera for OpenCode

Porsche 911 Heritage Cockpit (`Carrera v2.0.0`) TUI theme for [OpenCode](https://opencode.ai/) — Basalt Alcantara (`#15171a`), Chalk (`#d6d2c7`), GT Silver (`#9599a2`), and Carmine Red (`#e1656c`).

## Files

- `carrera.json` — OpenCode V1 TUI theme (`$schema: "https://opencode.ai/theme.json"`) defining `defs` and all 52 `theme` tokens plus `thinkingOpacity: 0.6`.

### Derived Hex Notes

- `border` (`#31353f`) and `borderSubtle` (`#262930`) match `btop.theme` `div_line` and `colors.toml` `hyprland_inactive_border`.
- `diffAddBg` (`#222a23`) and `diffDelBg` (`#2d1e20`) use the shared `Carrera` opaque diff tints over `#15171a`.
- `diffAddNumBg` (`#1e2422`) and `diffDelNumBg` (`#251e21`) match the Omarchy 8% `green`/`red` over `#15171a` mix.

## Installation

1. Copy `carrera.json` to `~/.config/opencode/themes/carrera.json`:

   ```bash
   mkdir -p ~/.config/opencode/themes
   cp carrera.json ~/.config/opencode/themes/carrera.json
   ```

2. Enable it manually in `~/.config/opencode/opencode.json` (this repository does not modify your active config):

   ```json
   {
     "theme": "carrera"
   }
   ```

## Verification

```bash
python3 -c 'import json; d=json.load(open("carrera.json")); assert d["$schema"]=="https://opencode.ai/theme.json" and len(d["theme"])>=52'
```

## License

[MIT](../LICENSE) — Copyright (c) 2026 Aryan Hamedani.

Not affiliated with or endorsed by Porsche AG. Porsche, 911 and Carrera are trademarks of Porsche AG.
