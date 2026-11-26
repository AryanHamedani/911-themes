# 911 for btop

Porsche 911 (`992.2`) Precision Night Cockpit theme for [btop](https://github.com/aristocratos/btop) — Race-Tex Charcoal (`#141619`), Ice Grey (`#dadad6`), GT Silver (`#9297a2`), and 911 Guards/Carmine Red (`#e55c5a`).

## Files

- `911.theme` — Standalone copy of `omarchy-911-theme/btop.theme` defining all 50 `theme[...]` keys including `gradient_color_0..7`.

## Palette Notes

- Box borders (`cpu_box`, `mem_box`, `net_box`, `proc_box`) use `#434854` and `div_line` uses `#2f3440`, matching `omarchy-911-theme/btop.theme`.
- Graphs sweep like a 992.2 tachometer from Oak Green Metallic Neo (`#7fb887`) through PCCB Racing Gold (`#e0be66`) to 911 Guards/Carmine Red (`#e55c5a`).

## Install

1. Copy `911.theme` to `~/.config/btop/themes/911.theme`:

   ```bash
   mkdir -p ~/.config/btop/themes
   cp 911.theme ~/.config/btop/themes/911.theme
   ```

2. Set in `~/.config/btop/btop.conf`:

   ```ini
   color_theme = "911"
   ```

   (On Omarchy with the `911` theme active, `~/.config/btop/themes/current.theme` already symlinks to `omarchy-911-theme/btop.theme`.)

## Validate

```bash
grep -E '^theme\[[a-z0-9_]+\]="#[0-9a-fA-F]{6}"$' 911.theme | wc -l
```

## Disclaimer

Not affiliated with or endorsed by Porsche AG. Porsche and 911 are trademarks of Porsche AG.
