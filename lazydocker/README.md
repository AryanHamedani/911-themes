# Carrera for Lazydocker

Porsche 911 Heritage Cockpit (`Carrera v2.0.0`) theme for [Lazydocker](https://github.com/jesseduffield/lazydocker) — Basalt Alcantara (`#15171a`), Chalk (`#d6d2c7`), GT Silver (`#9599a2`), and Carmine Red (`#e1656c`).

## Files

- `carrera.yml` — `gui.theme` configuration covering all 4 Lazydocker theme keys (`activeBorderColor`, `inactiveBorderColor`, `selectedLineBgColor`, `optionsTextColor`).

### Derived Hex Notes

- `inactiveBorderColor` uses `#31353f` (`btop.theme` `div_line`).

## Installation

Merge the `gui.theme` block from `carrera.yml` manually into `~/.config/lazydocker/config.yml` (this repository does not modify your active config).

## Verification

```bash
python3 -c 'import yaml; d=yaml.safe_load(open("carrera.yml")); assert set(d["gui"]["theme"])=={"activeBorderColor","inactiveBorderColor","selectedLineBgColor","optionsTextColor"}'
```

## License

[MIT](../LICENSE) — Copyright (c) 2026 Aryan Hamedani.

Not affiliated with or endorsed by Porsche AG. Porsche, 911 and Carrera are trademarks of Porsche AG.
