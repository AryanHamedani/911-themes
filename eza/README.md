# Carrera for eza

Porsche 911 Heritage Cockpit (`Carrera v2.0.0`) theme for [eza](https://eza.rocks/) — Basalt Alcantara (`#15171a`), Chalk (`#d6d2c7`), GT Silver (`#9599a2`), and Carmine Red (`#e1656c`).

## Files

- `theme.yml` — Complete `eza` truecolor `UiStylesOverride` theme (`colourful`, `filekinds`, `perms`, `size`, `users`, `links`, `git`, `git_repo`, `security_context`, `file_type`, and scalar styles).

### `LS_COLORS` Precedence Note

`eza` evaluates `LS_COLORS` and `EZA_COLORS` after loading `theme.yml`, so an exported `LS_COLORS` variable (e.g., `di=01;34`, `ex=01;32`) will override `filekinds` entries in `theme.yml`. To let `theme.yml` control `filekinds` colors completely, set `export LS_COLORS=""` or `unset LS_COLORS` in your shell profile.

## Installation

Back up any existing `~/.config/eza/theme.yml` first (or use `cp -i`), then copy `theme.yml` to `~/.config/eza/theme.yml` (`eza` loads `$EZA_CONFIG_DIR/theme.yml` automatically on startup; this repository does not copy or activate it):

```bash
mkdir -p ~/.config/eza
cp -i theme.yml ~/.config/eza/theme.yml
```

## Verification

```bash
python3 -c 'import yaml; d=yaml.safe_load(open("theme.yml")); assert d["colourful"] is True and "filekinds" in d'
env -u LS_COLORS -u EZA_COLORS EZA_CONFIG_DIR="$PWD" eza --color=always -la
```

## License

[MIT](../LICENSE) — Copyright (c) 2026 Aryan Hamedani.

Not affiliated with or endorsed by Porsche AG. Porsche, 911 and Carrera are trademarks of Porsche AG.
