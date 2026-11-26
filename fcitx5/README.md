# 911 (`992.2`) for Fcitx5

Precision Night Cockpit dark theme for Fcitx5 Classic UI, aligned with [`../colors.toml`](../colors.toml).

## Palette Mapping

- **Input Panel Surface**: Race-Tex Chrome (`#131519`) with a 1px `#2f3440` hairline border.
- **Menu Surface**: Vanadium Elevated (`#1a1d23`) with a 1px `#434854` box border and `#2f3440` separator.
- **Foreground Hierarchy**: Ice Grey (`#dadad6`, `13.04:1`) candidates, brushed dark silver (`#b4b7be`, `9.10:1`) candidate index labels, and GT Silver (`#9297a2`, `6.24:1`) candidate comments.
- **Preedit Cursor / Composition Highlight**: Guards Red (`#e55c5a`) on Smoked Carmine tint (`#261b1f`, `4.77:1` WCAG AA).
- **Active Candidate & Menu Highlight**: Filled Guards Red (`#bf3b3e`) with `#f4f3ef` ink across candidate text, label, and comment (`4.84:1` WCAG AA).

## Installation

```bash
mkdir -p ~/.local/share/fcitx5/themes/911
cp 911/theme.conf ~/.local/share/fcitx5/themes/911/theme.conf
for icon in arrow.svg next.svg prev.svg radio.svg; do
  ln -sf "/usr/share/fcitx5/themes/default-dark/$icon" ~/.local/share/fcitx5/themes/911/
done
```

Then set `Theme=911` and `DarkTheme=911` in `~/.config/fcitx5/conf/classicui.conf` and run `fcitx5-remote -r`.

> **Omarchy note**: Omarchy's active `911` theme already manages `~/.local/share/fcitx5/themes/omarchy/` (`Theme=omarchy`).

---

Not affiliated with or endorsed by Porsche AG. Licensed under [MIT](../LICENSE).
