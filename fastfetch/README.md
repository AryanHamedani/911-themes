# 911 for Fastfetch

Porsche 911 (`992.2`) Precision Night Cockpit theme for [Fastfetch](https://github.com/fastfetch-cli/fastfetch) — Race-Tex Charcoal (`#141619`), Ice Grey (`#dadad6`), GT Silver (`#9297a2`), and 911 Guards/Carmine Red (`#e55c5a`).

## Files

- `911.jsonc` — Fastfetch JSONC color configuration (`logo.color`, `display.color`, `display.percent.color`, `display.bar.color`, `display.temp.color`) using exact `911` palette hex values (requires Fastfetch >= v2.42.0).

## Install

```bash
mkdir -p ~/.config/fastfetch
cp 911.jsonc ~/.config/fastfetch/config.jsonc
```

## Validate

```bash
fastfetch --config 911.jsonc --logo none --structure Title:OS:CPU:Memory
```

## Disclaimer

Not affiliated with or endorsed by Porsche AG. Porsche and 911 are trademarks of Porsche AG.
