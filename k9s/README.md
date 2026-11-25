# Carrera for K9s

Porsche 911 Heritage Cockpit (`Carrera v2.0.0`) skin for [K9s](https://k9scli.io/) — Basalt Alcantara (`#15171a`), Chalk (`#d6d2c7`), GT Silver (`#9599a2`), and Carmine Red (`#e1656c`).

## Files

- `carrera.yaml` — Full K9s skin (`body`, `prompt`, `help`, `info`, `dialog`, `frame`, `views`) using quoted `#rrggbb` truecolor hex values.

### Derived Hex Notes

- `frame.border.fgColor` and `prompt.border.default` use `#454954` (`btop.theme` `cpu_box`/`mem_box`/`net_box`/`proc_box` border).

## Installation

1. Copy `carrera.yaml` to `~/.config/k9s/skins/carrera.yaml`:

   ```bash
   mkdir -p ~/.config/k9s/skins
   cp carrera.yaml ~/.config/k9s/skins/carrera.yaml
   ```

2. Enable it manually in `~/.config/k9s/config.yaml` (this repository does not modify your active config):

   ```yaml
   k9s:
     ui:
       skin: carrera
   ```

## Verification

```bash
python3 -c 'import yaml; d=yaml.safe_load(open("carrera.yaml"))["k9s"]; assert all(k in d for k in ("body","prompt","help","info","dialog","frame","views"))'
```

## License

[MIT](../LICENSE) — Copyright (c) 2026 Aryan Hamedani.

Not affiliated with or endorsed by Porsche AG. Porsche, 911 and Carrera are trademarks of Porsche AG.
