# Carrera for Cliamp

Porsche 911 Heritage Cockpit (`Carrera v2.0.0`) theme for [Cliamp](https://github.com/bjarneo/cliamp) — Basalt Alcantara (`#15171a`), Chalk (`#d6d2c7`), GT Silver (`#9599a2`), and Carmine Red (`#e1656c`).

## Files

- `carrera.toml` — Flat TOML theme defining `bg`, `accent`, `bright_fg`, `fg`, `green`, `yellow`, and `red` as `#RRGGBB` values.

## Installation

1. Copy `carrera.toml` to `~/.config/cliamp/themes/carrera.toml`:

   ```bash
   mkdir -p ~/.config/cliamp/themes
   cp carrera.toml ~/.config/cliamp/themes/carrera.toml
   ```

2. Enable it manually in `~/.config/cliamp/config.toml` (this repository does not modify your active config):

   ```toml
   theme = "carrera"
   ```

## Verification

```bash
python3 -c 'import tomllib, re; d=tomllib.load(open("carrera.toml","rb")); assert all(k in d for k in ("bg","accent","bright_fg","fg","green","yellow","red")) and all(re.fullmatch(r"#[0-9a-fA-F]{6}", v) for v in d.values())'
```

## License

[MIT](../LICENSE) — Copyright (c) 2026 Aryan Hamedani.

Not affiliated with or endorsed by Porsche AG. Porsche, 911 and Carrera are trademarks of Porsche AG.
