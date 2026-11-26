# 911 (`992.2`) for Hyprland

Precision Night Cockpit border, shadow, glow, groupbar, and canvas configuration for Hyprland, aligned with [`../colors.toml`](../colors.toml) and `omarchy-911-theme/hyprland.lua`.

## Coverage

- **Borders (`general`)**: Guards/Carmine Red gradient (`rgba(e55c5acc) rgba(332024cc) 135deg`) for active and nogroup-active windows; quiet Vanadium hairline (`rgba(252932aa)`) for inactive and nogroup-inactive windows.
- **Shadows & Glow (`decoration.shadow`, `decoration.glow`)**: Deep diffuser shadow (`#0a0b0d`) for active (`aa`) and inactive (`66`) windows; restrained Guards Red inner glow (`rgba(e55c5a33)`) when `decoration:glow:enabled` is turned on.
- **Groups (`group` & `groupbar`)**:
  - Active: Guards/Carmine Red border gradient, AA filled Guards Red tab (`#bf3b3e`) with `#f4f3ef` badge ink (`4.84:1` opaque / `5.30:1` composited over `#141619`).
  - Inactive: `#252932` border hairline, Vanadium elevated tab (`#1a1d23`) with Ice Grey `#dadad6` text (`12.17:1`).
  - Locked active: Lava Orange (`#e89158`) to Carmine (`#332024`) border gradient, Smoked Carmine tab (`#261b1f`) with `#f4f3ef` text (`15.12:1`).
  - Locked inactive: Subtle Carmine border hairline (`#332024`), recessed carbon tab (`#0f1114`) with GT Silver `#9297a2` text (`6.41:1`).
- **Canvas (`misc`)**: Race-Tex Charcoal background (`rgb(141619)`) and AA-compliant GT Silver splash (`rgba(9297a2ee)`, `5.55:1` over `#141619`).

## Installation

```bash
cp 911.conf ~/.config/hypr/911.conf
```

Then add `source = ~/.config/hypr/911.conf` to `~/.config/hypr/hyprland.conf` and reload with `hyprctl reload`.

> **Omarchy note**: Omarchy's active `911` theme already applies `~/.local/state/omarchy/current/theme/hyprland.lua`.

---

Not affiliated with or endorsed by Porsche AG. Licensed under [MIT](../LICENSE).
