# Carrera for pgcli

Porsche 911 Heritage Cockpit (`Carrera v2.0.0`) color scheme for [pgcli](https://www.pgcli.com/) — Basalt Alcantara (`#15171a`), Chalk (`#d6d2c7`), GT Silver (`#9599a2`), and Carmine Red (`#e1656c`).

## Files

- `carrera.pgclirc` — `[colors]` section defining all 29 supported `pgcli` `PROMPT_STYLE_TO_TOKEN` keys using exact `colors.toml` hex values.

## Installation

1. Copy the `[colors]` section from `carrera.pgclirc` into `~/.config/pgcli/config` (this repository does not modify your active config), and optionally set `syntax_style = native` under `[main]`:

   ```ini
   [main]
   syntax_style = native
   ```

2. Or launch `pgcli` with `--pgclirc path/to/carrera.pgclirc` on a dedicated copy containing your `[main]` settings.

## Verification

```bash
python3 -c 'import configparser; cp=configparser.ConfigParser(); cp.read("carrera.pgclirc"); assert len(cp["colors"])==29'
```

## License

[MIT](../LICENSE) — Copyright (c) 2026 Aryan Hamedani.

Not affiliated with or endorsed by Porsche AG. Porsche, 911 and Carrera are trademarks of Porsche AG.
