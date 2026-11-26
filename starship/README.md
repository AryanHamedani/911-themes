# 911 for Starship

A dark, glare-free [Starship](https://starship.rs) prompt theme inspired by the **Porsche 911 (`992.2`) Precision Night Cockpit**: **Race-Tex Charcoal** (`#141619`), **Ice Grey (Crayon)** (`#dadad6`), and **Guards/Carmine Red** (`#e55c5a`).

Calibrated in OKLCH for long daily sessions and verified to WCAG AA contrast targets.

## Files Included

- `911.toml` — Complete Starship configuration with `[palettes.911]` (all base and derived cockpit tokens) and rich module styling for `directory`, `git_branch`, `git_status`, `git_metrics`, `python`, `golang`, `rust`, `nodejs`, `docker_context`, `kubernetes`, `cmd_duration`, `jobs`, `status`, `fill`, `time`, and `character` (including vi-mode indicators).

## Manual Install

```sh
cp ~/.config/starship.toml ~/.config/starship.toml.bak-911
cp 911.toml ~/.config/starship.toml
starship print-config > /dev/null
```

Palette reference: [`../colors.toml`](../colors.toml).

---

Not affiliated with or endorsed by Porsche AG. Porsche and 911 are trademarks of Porsche AG.

License: [MIT](../LICENSE)
