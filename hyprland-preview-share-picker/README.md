# 911 (`992.2`) for Hyprland Preview Share Picker

GTK 4 stylesheet for `hyprland-preview-share-picker`, aligned with the **911 (`992.2`) Precision Night Cockpit** palette (`../colors.toml`).

## Coverage

- **Window & Chrome**: Race-Tex Charcoal window (`#141619` @ 96% opacity) with `#e55c5a` Guards Red frame and Race-Tex Chrome (`#131519`) notebook header strip divided by `#2f3440`.
- **Notebook Tabs**: `#858a96` inactive (`5.29:1` AA), `#b4b7be` hover (`9.10:1` AA), and `#edede9` active (`15.57:1` AA) with a 2px `#e55c5a` Guards Red bottom lightbar indicator.
- **Preview Cards**: 3-step tactile progression — resting Vanadium (`#1a1d23`, `#252932` border, `#b4b7be` caption), hover Vanadium Grey (`#1d2026`, `#434854` border, `#dadad6` caption), and selected/focused Smoked Carmine (`#261b1f`, `#e55c5a` border, `#edede9` caption).
- **Loading State**: Recessed carbon well (`#0f1114`) with `#2f3440` border, `#e55c5a` Guards Red spinner (`5.41:1`), and `#858a96` status label (`5.47:1` AA).
- **AA Action Buttons**: `.region-button` and `.restore-button` (including checkbox indicator) in `#bf3b3e` / `#f4f3ef` (`4.84:1` AA), `#e55c5a` / `#0a0b0d` on hover/focus (`5.63:1` AA), and `#1a1d23` / `#9297a2` when disabled (`5.76:1` AA).
- **Scrollbars**: Deep carbon trough (`#0c0e11` @ 55%), `#434854` resting thumb, `#858a96` hover, and `#e55c5a` active drag.

## Installation

Reference `style.css` in `~/.config/hyprland-preview-share-picker/config.yaml`:

```yaml
stylesheets: ["/path/to/style.css"]
```

> **Omarchy note**: Omarchy's active `911` theme already wires `~/.local/state/omarchy/current/theme/hyprland-preview-share-picker.css` in `~/.config/hyprland-preview-share-picker/config.yaml`.

---

Not affiliated with or endorsed by Porsche AG. Licensed under [MIT](../LICENSE).
