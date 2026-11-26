# 911 (`992.2`) for mpv

Precision Night Cockpit dark theme for `mpv`, aligned with [`../colors.toml`](../colors.toml).

## Coverage

- **Canvas & Alpha Grid**: Race-Tex Charcoal (`#141619`) window canvas with calibrated `#141619` / Vanadium Grey (`#1d2026`) alpha checkerboard tiles when `--background=tiles` is active.
- **OSD & Interactive Menus**: Ice Grey (`#dadad6`) typography in `JetBrainsMono Nerd Font` over a 90% opaque Recessed Carbon Well panel (`#e60f1114`, `background-box` with 4px padding), Deep Diffuser Shadow hairline outline (`#0a0b0d`), and 911 Guards/Carmine Red active selection (`#e55c5a`).
- **Telemetry Bar**: Low-profile progress/volume bar (`osd-bar-h=1.4`, `osd-bar-w=62`) anchored at `y=0.92` with crisp vertical `line` chapter ticks.
- **Subtitles**: Cinema-grade Pure Dial Highlight (`#edede9`) in `Inter` with `outline-and-shadow`, 2.0px Deep Diffuser Shadow stroke (`#0a0b0d`), 0.3px optical edge blur, and 60% drop shadow (`#990a0b0d`) — no opaque box obscuring the frame.

> Note: `mpv` uses `#AARRGGBB` (alpha first) for 8-digit hex colors, and `osd-shadow-color` / `sub-shadow-color` are aliases of `osd-back-color` / `sub-back-color`, so each surface defines `*-back-color` once without alias collision.

## Installation

```bash
mkdir -p ~/.config/mpv
cp mpv.conf ~/.config/mpv/mpv.conf
```

Or include it from an existing `~/.config/mpv/mpv.conf`:

```ini
include=/path/to/mpv/mpv.conf
```

---

Not affiliated with or endorsed by Porsche AG. Licensed under [MIT](../LICENSE).
