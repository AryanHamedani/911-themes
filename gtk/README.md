# 911 (`992.2`) for GTK 3 & GTK 4 / libadwaita

Shared pure `@define-color` stylesheet for GTK 3 and GTK 4 / libadwaita applications, crafted to the **911 (`992.2`) Precision Night Cockpit** design system (`../colors.toml`).

## Surface & Contrast Architecture

| Plane | Role | Hex | Key Tokens |
|---|---|---|---|
| **Plane 0** | Deep shadow & recessed well | `#0a0b0d`, `#0c0e11`, `#0f1114` | `view_bg_color`, `sidebar_bg_color`, `*_backdrop_color`, `*_shade_color`, `osd_bg` |
| **Plane 1** | Race-Tex canvas & chrome | `#131519`, `#141619` | `headerbar_bg_color`, `secondary_sidebar_bg_color`, `window_bg_color`, `wm_bg` |
| **Plane 2** | Vanadium elevated planes | `#1a1d23`, `#1d2026` | `card_bg_color`, `dialog_bg_color`, `thumbnail_bg_color`, `popover_bg_color`, `tooltip_bg_color` |
| **Plane 3** | Slate trim & Smoked Carmine | `#292d36`, `#261b1f` | `theme_selected_bg_color`, `wm_button_active_color_*` |

- **5-step typography**: `#edede9` (highlight/selected/tooltip) -> `#dadad6` (Ice Grey primary) -> `#b4b7be` (secondary sidebar) -> `#9297a2` (unfocused) -> `#858a96` (insensitive/placeholder, WCAG AA `>= 4.72:1` across all planes).
- **90/9/1 Guards Red restraint**: `accent_bg_color` (`#bf3b3e`) + `accent_fg_color` (`#f4f3ef`) achieves `4.84:1` WCAG AA; standalone `accent_color` (`#e55c5a`) achieves `5.19:1` on window canvas and `4.67:1` on elevated popovers; links use Lugano Blue (`#6fa2de`) and Ultraviolet (`#b488cc`).
- **Complete coverage**: All libadwaita 1.x semantic tokens (`accent_*`, `destructive_*`, `success_*`, `warning_*`, `error_*`, `window_*`, `view_*`, `headerbar_*`, `sidebar_*`, `secondary_sidebar_*`, `card_*`, `dialog_*`, `popover_*`, `thumbnail_*`, `shade_color`, `scrollbar_outline_color`) plus full GTK 3 Adwaita-dark aliases (`theme_*`, `insensitive_*`, `unfocused_*`, `borders`, `content_view_bg`, `text_view_bg`, `placeholder_text_color`, `link_*`, `wm_*`, `osd_*`, `tooltip_*`).

## Installation

```bash
mkdir -p ~/.config/gtk-3.0 ~/.config/gtk-4.0
cp gtk.css ~/.config/gtk-3.0/gtk.css
cp gtk.css ~/.config/gtk-4.0/gtk.css
```

*(On Omarchy systems with managed GTK theme symlinks, keep Omarchy's symlinks intact and use this file as a standalone or custom theme override.)*

---

Not affiliated with or endorsed by Porsche AG. Licensed under [MIT](../LICENSE).
