# Carrera for imv

A dark Heritage Cockpit color configuration for the `imv` image viewer:
Basalt Alcantara canvas (`15171a`), recessed overlay (`101215` at `e6` alpha), and Chalk overlay text (`d6d2c7`).

## Install

Merge the `[options]` values from `imv/carrera.ini` into your `~/.config/imv/config`, keeping your existing `[binds]` section intact:

```ini
[options]
background = 15171a
overlay_text_color = d6d2c7
overlay_text_alpha = ff
overlay_background_color = 101215
overlay_background_alpha = e6
```

> Note: `imv` requires 6-digit hex colors **without** `#`, and `inih` does not strip inline `#` comments on `key = value` lines.

---

Not affiliated with or endorsed by Porsche AG. Porsche, 911 and Carrera are trademarks of Porsche AG.

License: [MIT](../LICENSE)
