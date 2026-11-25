# Carrera for bat

Porsche 911 Heritage Cockpit (`Carrera v2.0.0`) TextMate theme for [bat](https://github.com/sharkdp/bat) — Basalt Alcantara (`#15171a`), Chalk (`#d6d2c7`), GT Silver (`#9599a2`), and Carmine Red (`#e1656c`).

## Files

- `Carrera.tmTheme` — Apple Property List XML 1.0 TextMate theme covering UI chrome, syntax scopes, Markdown, and diff highlights.

### Derived Hex Notes

- `selectionBorder` / `stackGuide` (`#31353f`), `invisibles` / `activeGuide` (`#454954`), and `guide` (`#262930`) use the shared `btop.theme` / `colors.toml` structural border hexes.
- Diff backgrounds (`#222a23` inserted, `#2d1e20` deleted, `#202731` changed) use the shared `Carrera` opaque tints over `#15171a`.

## Installation

1. Copy `Carrera.tmTheme` into bat's `themes/` directory and rebuild bat's theme cache:

   ```bash
   mkdir -p "$(bat --config-dir)/themes"
   cp Carrera.tmTheme "$(bat --config-dir)/themes/Carrera.tmTheme"
   bat cache --build
   ```

2. Enable it manually in `~/.config/bat/config` (this repository does not modify your active config):

   ```text
   --theme="Carrera"
   ```

## Verification

```bash
python3 -c 'import plistlib; p=plistlib.load(open("Carrera.tmTheme","rb")); assert p["name"]=="Carrera"'
```

## License

[MIT](../LICENSE) — Copyright (c) 2026 Aryan Hamedani.

Not affiliated with or endorsed by Porsche AG. Porsche, 911 and Carrera are trademarks of Porsche AG.
