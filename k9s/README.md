# 911 for K9s

Porsche 911 (`992.2`) Precision Night Cockpit skin for [K9s](https://k9scli.io/) — Race-Tex Charcoal (`#141619`), Ice Grey (`#dadad6`), GT Silver (`#9297a2`), and 911 Guards/Carmine Red (`#e55c5a`).

## Files

- `911.yaml` — Complete K9s skin (`body`, `prompt`, `help`, `info`, `dialog`, `frame`, `views`: `charts`, `table`, `xray`, `yaml`, `picker`, `logs`) using quoted `#rrggbb` truecolor hex values.

## Palette Notes

- Borders use `#434854` (`btop.theme` box border) with `#e55c5a` focus highlight; filled focused buttons and chart focus badges use `#bf3b3e` with `#f4f3ef` ink (`4.84:1` AA).

## Install

1. Copy `911.yaml` to `~/.config/k9s/skins/911.yaml`:

   ```bash
   mkdir -p ~/.config/k9s/skins
   cp 911.yaml ~/.config/k9s/skins/911.yaml
   ```

2. Set `k9s.ui.skin: 911` in `~/.config/k9s/config.yaml`.

## Validate

```bash
python3 -c 'import yaml; d=yaml.safe_load(open("911.yaml")); assert set(d["k9s"]["views"])=={"charts","table","xray","yaml","picker","logs"}'
```

## Disclaimer

Not affiliated with or endorsed by Porsche AG. Porsche and 911 are trademarks of Porsche AG.
