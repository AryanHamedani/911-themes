# Carrera for btop

Porsche 911 Heritage Cockpit (`Carrera v2.0.0`) theme for [btop](https://github.com/aristocratos/btop) — Basalt Alcantara (`#15171a`), Chalk (`#d6d2c7`), GT Silver (`#9599a2`), and Carmine Red (`#e1656c`).

## Files

- `carrera.theme` — Standalone copy of `omarchy-carrera-theme/btop.theme` defining all 42 `theme[...]` keys.

### Derived Hex Notes

- Box borders (`cpu_box`, `mem_box`, `net_box`, `proc_box`) use `#454954` and `div_line` uses `#31353f`, matching `omarchy-carrera-theme/btop.theme`.

## Installation

1. Copy `carrera.theme` to `~/.config/btop/themes/carrera.theme`:

   ```bash
   mkdir -p ~/.config/btop/themes
   cp carrera.theme ~/.config/btop/themes/carrera.theme
   ```

2. Enable it manually in `~/.config/btop/btop.conf` (this repository does not modify your active config):

   ```ini
   color_theme = "carrera"
   ```

## Verification

```bash
grep -E '^theme\[[a-z_]+\]="#[0-9a-fA-F]{6}"$' carrera.theme | wc -l
```

## License

[MIT](../LICENSE) — Copyright (c) 2026 Aryan Hamedani.

Not affiliated with or endorsed by Porsche AG. Porsche, 911 and Carrera are trademarks of Porsche AG.
