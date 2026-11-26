# 911 for Lazydocker

Porsche 911 (`992.2`) Precision Night Cockpit theme and ergonomic configuration for [Lazydocker](https://github.com/jesseduffield/lazydocker) (`v0.25.2+`) — Race-Tex Charcoal (`#141619`), Smoked Carmine selection (`#261b1f`), cockpit box borders (`#434854`), Ice Grey typography (`#dadad6`), Lugano Blue options chrome (`#6fa2de`), and disciplined 911 Guards/Carmine Red (`#e55c5a`) focus.

## Files

- `911.yml` — Complete `gui.theme` configuration (all 4 Lazydocker true-color theme keys), ergonomic cockpit layout (`rounded` borders, `0.30` side panel width with `expandFocusedSidePanel: true`, wrapped main panel, `scrollHeight: 2`, `showBottomLine: true`), clean `logs` defaults (`since: "60m"`, `tail: "300"`), and `stats.graphs` telemetry calibrated for the 911 terminal ANSI palette.

## Palette Highlights

| Role | Token | Value |
|---|---|---|
| Active panel border & title | Guards Red (`bold`) | `#e55c5a` |
| Inactive panel border & title | Cockpit box border | `#434854` |
| Selected row background | Smoked Carmine (`11.90:1` w/ `#dadad6`) | `#261b1f` |
| Bottom options bar text | Lugano Blue | `#6fa2de` |
| CPU (%) telemetry graph | ANSI `cyan` → Ice Glacier Cyan | `cyan` (`#6ac4cb`) |
| Memory (%) telemetry graph | ANSI `green` → Oak Green Metallic Neo | `green` (`#7fb887`) |

*Note: Lazydocker `v0.25.2` supports true-color `#rrggbb` hex values in `gui.theme.*` (via `gocui.NewRGBColor`), while `stats.graphs[].color` uses named ANSI attributes (`fatih/color`) that inherit the 911 terminal palette.*

## Install

Copy or merge `911.yml` into `~/.config/lazydocker/config.yml`:

```bash
cp 911.yml ~/.config/lazydocker/config.yml
```

## Validate

```bash
python3 -c 'import yaml; d=yaml.safe_load(open("911.yml")); assert set(d["gui"]["theme"])=={"activeBorderColor","inactiveBorderColor","selectedLineBgColor","optionsTextColor"}'
```

## Disclaimer

Not affiliated with or endorsed by Porsche AG. Porsche and 911 are trademarks of Porsche AG.
