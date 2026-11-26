# 911 for Fastfetch

Porsche 911 (`992.2`) Precision Night Cockpit system telemetry card for [Fastfetch](https://github.com/fastfetch-cli/fastfetch) — disciplined 90/9/1 Guards Red restraint (`#e55c5a`), brushed dark silver keys (`#b4b7be`), muted gauge rules (`#858a96` / `#434854`), crisp Ice Grey readouts (`#dadad6`), and semantic Oak Green / Racing Gold / Carmine Red gauge bars.

## Files

- `911.jsonc` — Complete Fastfetch JSONC theme and telemetry layout (`logo`, `display`, and 14 curated Omarchy/Arch + Hyprland modules: `os`, `kernel`, `uptime`, `packages`, `shell`, `wm`, `terminal`, `cpu`, `gpu`, `memory`, `disk`, `battery`, `localip`, `colors`). Requires Fastfetch >= v2.42.0.

## Design Highlights

- **Color hierarchy**: Guards Red (`#e55c5a`) reserved strictly for the `user` title accent, Pure dial highlight (`#edede9`) for `host`, brushed dark silver (`#b4b7be`) for fixed-width aligned keys, muted (`#858a96`) for ` │ ` separators, and Ice Grey (`#dadad6`) for values.
- **Semantic gauges**: `display.percent.type: 11` with auto-colored elapsed bars (`#7fb887` green → `#e0be66` yellow → `#e56c6a` red) over Slate Grey Neo tracks (`#292d36`) framed by `#434854` bezels.
- **Scannable ergonomics**: Fixed 8-character key column, compact `1h 21m` durations, 1-decimal sizes/frequencies, P+E core counts + CPU/GPU temperatures, root `/` disk filter, and clean Local IP without CIDR noise.

## Install

```bash
mkdir -p ~/.config/fastfetch
cp 911.jsonc ~/.config/fastfetch/config.jsonc
```

## Validate

```bash
fastfetch --config 911.jsonc --show-errors
```

## Disclaimer

Not affiliated with or endorsed by Porsche AG. Porsche and 911 are trademarks of Porsche AG.
