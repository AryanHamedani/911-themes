# Carrera for Hyprland Preview Share Picker

A GTK 4 stylesheet for `hyprland-preview-share-picker` (`v0.2.1+`) covering all 10 `schema.json` classes:
translucent Basalt Alcantara window (`#15171a` at 95% alpha), `#1e2025` preview cards, Chalk (`#d6d2c7`) labels,
and Carmine Red (`#e1656c`) borders and action buttons with `#15171a` dark button labels (`5.37:1` contrast).

## Install

Copy `style.css` to `~/.config/hyprland-preview-share-picker/style.css`:

```bash
mkdir -p ~/.config/hyprland-preview-share-picker
cp hyprland-preview-share-picker/style.css ~/.config/hyprland-preview-share-picker/style.css
```

Then reference it in `~/.config/hyprland-preview-share-picker/config.yaml`:

```yaml
stylesheets:
  - ./style.css
```

---

Not affiliated with or endorsed by Porsche AG. Porsche, 911 and Carrera are trademarks of Porsche AG.

License: [MIT](../LICENSE)
