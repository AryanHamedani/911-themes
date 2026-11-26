# 911 for Lazydocker

Porsche 911 (`992.2`) Precision Night Cockpit theme for [Lazydocker](https://github.com/jesseduffield/lazydocker) — Race-Tex Charcoal (`#141619`), Ice Grey (`#dadad6`), GT Silver (`#9297a2`), and 911 Guards/Carmine Red (`#e55c5a`).

## Files

- `911.yml` — `gui.theme` configuration covering all 4 Lazydocker theme keys (`activeBorderColor`, `inactiveBorderColor`, `selectedLineBgColor`, `optionsTextColor`).

## Install

Merge the `gui.theme` block from `911.yml` into `~/.config/lazydocker/config.yml`.

## Validate

```bash
python3 -c 'import yaml; d=yaml.safe_load(open("911.yml")); assert set(d["gui"]["theme"])=={"activeBorderColor","inactiveBorderColor","selectedLineBgColor","optionsTextColor"}'
```

## Disclaimer

Not affiliated with or endorsed by Porsche AG. Porsche and 911 are trademarks of Porsche AG.
