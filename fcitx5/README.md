# Carrera for Fcitx5

A dark ClassicUI theme for Fcitx5 inspired by the Porsche 911 Heritage Cockpit:
Basalt Alcantara panel (`#15171a`) with machined `#2b2e35` borders, Chalk (`#d6d2c7`) candidate text,
and Carmine Red (`#e1656c`) active highlight with `#15171a` candidate foreground (`5.37:1` contrast).

## Install

1. Copy `fcitx5/carrera/` into `~/.local/share/fcitx5/themes/`:

   ```bash
   mkdir -p ~/.local/share/fcitx5/themes
   cp -r fcitx5/carrera ~/.local/share/fcitx5/themes/carrera
   ```

2. Link or copy Fcitx5's standard SVG glyphs into the theme directory so page buttons, checkboxes, and submenu arrows render:

   ```bash
   for svg in arrow.svg next.svg prev.svg radio.svg; do
     ln -sf "/usr/share/fcitx5/themes/default/$svg" "$HOME/.local/share/fcitx5/themes/carrera/$svg"
   done
   ```

3. Set `Theme=carrera` and `DarkTheme=carrera` in `~/.config/fcitx5/conf/classicui.conf`, then restart Fcitx5 (`fcitx5 -r`).

---

Not affiliated with or endorsed by Porsche AG. Porsche, 911 and Carrera are trademarks of Porsche AG.

License: [MIT](../LICENSE)
