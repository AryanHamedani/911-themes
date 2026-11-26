# 911 (`992.2`) for GTK 3 & GTK 4 / libadwaita

Shared `@define-color` stylesheet for GTK 3 and GTK 4 / libadwaita applications, aligned with the **911 (`992.2`) Precision Night Cockpit** palette (`../colors.toml`).

## Coverage

- Complete libadwaita 1.x tokens: `accent_*` (`#bf3b3e` / `#f4f3ef` `4.84:1` AA, `#e55c5a` text accent), `destructive_*`, `success_*`, `warning_*`, `error_*`, `window_*`, `view_*`, `headerbar_*`, `sidebar_*`, `secondary_sidebar_*`, `card_*`, `dialog_*`, `popover_*`, `thumbnail_*`, `shade_color`, and `scrollbar_outline_color`.
- Full GTK 3 Adwaita-dark aliases: `theme_*`, `insensitive_*`, `theme_unfocused_*`, `borders`, `content_view_bg`, `text_view_bg`, `wm_*`, `osd_*`, and `tooltip_*`.

## Installation

```bash
mkdir -p ~/.config/gtk-3.0 ~/.config/gtk-4.0
cp gtk.css ~/.config/gtk-3.0/gtk.css
cp gtk.css ~/.config/gtk-4.0/gtk.css
```

---

Not affiliated with or endorsed by Porsche AG. Licensed under [MIT](../LICENSE).
