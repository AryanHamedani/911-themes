# Carrera for Hyprland

A native Hyprlang color configuration for Hyprland (`0.56.2+`) inspired by the Porsche 911 Heritage Cockpit:
smoked Carmine Red tail-light gradient (`rgba(e1656ccc) rgba(3a2429cc) 135deg`) on focused windows,
dark graphite (`rgba(262930aa)`) on inactive borders, Cognac Amber (`rgba(e8965acc)`) for locked groups,
and deep Basalt (`rgb(15171a)`) background fill.

## Install

Copy `carrera.conf` to `~/.config/hypr/carrera.conf` and source it at the end of `~/.config/hypr/hyprland.conf`:

```bash
cp hyprland/carrera.conf ~/.config/hypr/carrera.conf
```

```ini
# In ~/.config/hypr/hyprland.conf
source = ~/.config/hypr/carrera.conf
```

> Note: On Omarchy setups using `hyprland.lua`, Omarchy's theme template generator already derives `hyprland_active_border` and `hyprland_inactive_border` from `omarchy-carrera-theme/colors.toml`.

---

Not affiliated with or endorsed by Porsche AG. Porsche, 911 and Carrera are trademarks of Porsche AG.

License: [MIT](../LICENSE)
