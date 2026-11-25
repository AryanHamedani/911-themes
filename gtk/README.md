# Carrera for GTK 3 & GTK 4

A unified `@define-color` stylesheet for GTK 3, GTK 4, and libadwaita applications:
Basalt Alcantara windows (`#15171a`), recessed views and sidebars (`#101215`),
elevated headerbars/cards/popovers (`#1e2025`), Chalk (`#d6d2c7`) text, and Carmine Red (`#e1656c`) accents
with `#15171a` accent foreground (`5.37:1` WCAG AA contrast).

## Install

Copy `gtk.css` to your GTK 3 and GTK 4 user config directories (back up any existing `gtk.css` first):

```bash
mkdir -p ~/.config/gtk-3.0 ~/.config/gtk-4.0
cp gtk/gtk.css ~/.config/gtk-3.0/gtk.css
cp gtk/gtk.css ~/.config/gtk-4.0/gtk.css
```

Ensure dark mode is preferred in your desktop session:

```bash
gsettings set org.gnome.desktop.interface color-scheme 'prefer-dark'
gsettings set org.gnome.desktop.interface gtk-theme 'Adwaita-dark'
```

---

Not affiliated with or endorsed by Porsche AG. Porsche, 911 and Carrera are trademarks of Porsche AG.

License: [MIT](../LICENSE)
