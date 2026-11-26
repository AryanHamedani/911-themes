# 911 (`992.2`) for Fcitx5

Precision Night Cockpit dark theme for Fcitx5 Classic UI, aligned with [`../colors.toml`](../colors.toml).

## Palette Mapping

- **Panel & Menu Surface**: Race-Tex Chrome (`#131519`) with `#2f3440` / `#434854` borders.
- **Typography**: Ice Grey (`#dadad6`) normal candidates.
- **Active Highlight**: Filled Guards Red (`#bf3b3e`) with `#f4f3ef` foreground (`4.84:1` WCAG AA).
- **Menu Separator**: `#2f3440` divider.

## Installation

```bash
mkdir -p ~/.local/share/fcitx5/themes/911
cp 911/theme.conf ~/.local/share/fcitx5/themes/911/theme.conf
```

Then set `Theme=911` and `DarkTheme=911` in `~/.config/fcitx5/conf/classicui.conf` and run `fcitx5-remote -r`.

> **Omarchy note**: Omarchy's active `911` theme already manages `~/.local/share/fcitx5/themes/omarchy/` (`Theme=omarchy`).

---

Not affiliated with or endorsed by Porsche AG. Licensed under [MIT](../LICENSE).
