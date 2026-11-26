# 911 for Cliamp

Porsche 911 (`992.2`) Precision Night Cockpit theme for [Cliamp](https://github.com/bjarneo/cliamp) — Race-Tex Charcoal (`#141619`), Ice Grey (`#dadad6`), GT Silver (`#9297a2`), and 911 Guards/Carmine Red (`#e55c5a`).

## Files

- `911.toml` — Complete Cliamp theme defining `bg`, `accent`, `bright_fg`, `fg`, `green`, `yellow`, and `red`.

## Install

1. Copy `911.toml` to `~/.config/cliamp/themes/911.toml`:

   ```bash
   mkdir -p ~/.config/cliamp/themes
   cp 911.toml ~/.config/cliamp/themes/911.toml
   ```

2. Set `theme = "911"` in `~/.config/cliamp/config.toml` (or run `cliamp theme 911`).

## Validate

```bash
python3 -c 'import tomllib; d=tomllib.load(open("911.toml","rb")); assert len(d)==7'
cliamp theme list | grep -q '911'
```

## Disclaimer

Not affiliated with or endorsed by Porsche AG. Porsche and 911 are trademarks of Porsche AG.
