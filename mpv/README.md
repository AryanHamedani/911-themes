# Carrera for mpv

A dark Heritage Cockpit color configuration for `mpv` (`v0.41.0+`):
Basalt Alcantara canvas (`#15171a`), recessed OSD/subtitle backing (`#cc101215` in `#AARRGGBB`),
Chalk (`#d6d2c7` / `#eae6dc`) typography, and Carmine Red (`#e1656c`) active OSD selection.

## Install

Include `mpv.conf` from your `~/.config/mpv/mpv.conf` without overwriting existing playback settings:

```bash
cp mpv/mpv.conf ~/.config/mpv/carrera.conf
```

Then add this line to `~/.config/mpv/mpv.conf`:

```ini
include=~~/carrera.conf
```

Or test one-off from the command line:

```bash
mpv --include=/path/to/mpv/mpv.conf video.mp4
```

> Note: `mpv` uses **alpha-first** `#AARRGGBB` for 8-digit hex colors, and `#` values must be quoted so they are not treated as inline comments.

---

Not affiliated with or endorsed by Porsche AG. Porsche, 911 and Carrera are trademarks of Porsche AG.

License: [MIT](../LICENSE)
