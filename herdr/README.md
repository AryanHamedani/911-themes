# 911 for Herdr

A dark, glare-free [Herdr](https://herdr.dev) workspace multiplexer theme inspired by the **Porsche 911 (`992.2`) Precision Night Cockpit**: **Race-Tex Charcoal** (`#141619`) panels, **Carbon Well** (`#0f1114`) sidebar, **Ice Grey (Crayon)** (`#dadad6`) text, and **Guards/Carmine Red** (`#e55c5a`) focus accents.

Calibrated in OKLCH for long daily sessions and verified to WCAG AA contrast targets.

## Files Included

- `911.toml` — Complete `[theme]`, `[theme.custom]`, and `[ui]` accent configuration covering every Herdr surface, overlay, text, and semantic color slot.

## Manual Install

Merge the `[theme]`, `[theme.custom]`, and `[ui]` sections from `911.toml` into `~/.config/herdr/config.toml`, then validate and reload:

```sh
herdr config check
herdr server reload-config
```

Palette reference: [`../colors.toml`](../colors.toml).

---

Not affiliated with or endorsed by Porsche AG. Porsche and 911 are trademarks of Porsche AG.

License: [MIT](../LICENSE)
