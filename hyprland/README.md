# 911 (`992.2`) for Hyprland

Precision Night Cockpit border, shadow, groupbar, and canvas configuration for Hyprland, aligned with [`../colors.toml`](../colors.toml) and `omarchy-911-theme/hyprland.lua`.

## Coverage

- **Borders (`general`)**: Guards/Carmine Red gradient (`rgba(e55c5acc) rgba(332024cc) 135deg`) for active & nogroup-active windows; inactive hairline (`rgba(252932aa)`).
- **Shadows (`decoration.shadow`)**: Deep diffuser shadow (`#0a0b0d`) for active and inactive windows.
- **Groups (`group` & `groupbar`)**: Active, inactive, locked-active (Lava Orange `#e89158` gradient + Smoked Carmine `#261b1f` bar), and locked-inactive states with Ice Grey / Pure Highlight text.
- **Canvas (`misc`)**: Race-Tex Charcoal background (`rgb(141619)`) and muted splash (`#858a96`).

## Installation

```bash
cp 911.conf ~/.config/hypr/911.conf
```

Then add `source = ~/.config/hypr/911.conf` to `~/.config/hypr/hyprland.conf` and reload with `hyprctl reload`.

> **Omarchy note**: Omarchy's active `911` theme already applies `~/.local/state/omarchy/current/theme/hyprland.lua`.

---

Not affiliated with or endorsed by Porsche AG. Licensed under [MIT](../LICENSE).
