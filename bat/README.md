# 911 for bat

Porsche 911 (`992.2`) Precision Night Cockpit TextMate theme for [bat](https://github.com/sharkdp/bat) — Race-Tex Charcoal (`#141619`), Ice Grey (`#dadad6`), GT Silver (`#9297a2`), and 911 Guards/Carmine Red (`#e55c5a`).

## Files

- `911.tmTheme` — Apple Property List XML 1.0 TextMate theme covering cockpit UI chrome, comprehensive syntax scopes (comments, docs, strings, interpolation, regex, numbers, constants, variables, parameters, properties, keywords, storage, types, classes, functions, tags, attributes, CSS, JSON/YAML/TOML keys, decorators, invalid/deprecated), Markdown, and diff highlights.

## Palette Notes

- Diff backgrounds (`#202825` inserted, `#2d2023` deleted, `#1f2731` changed) and search highlight (`#5b5134`) use the canonical `911` opaque tints over `#141619`.
- Invalid illegal badges use Guards Red filled badge (`#bf3b3e`) with `#f4f3ef` ink (`4.84:1` AA).

## Install

1. Copy `911.tmTheme` into bat's `themes/` directory and rebuild bat's theme cache:

   ```bash
   mkdir -p "$(bat --config-dir)/themes"
   cp 911.tmTheme "$(bat --config-dir)/themes/911.tmTheme"
   bat cache --build
   ```

2. Add to `~/.config/bat/config`:

   ```text
   --theme="911"
   ```

## Validate

```bash
python3 -c 'import plistlib; p=plistlib.load(open("911.tmTheme","rb")); assert p["name"]=="911"'
bat --list-themes | grep -x '911'
```

## Disclaimer

Not affiliated with or endorsed by Porsche AG. Porsche and 911 are trademarks of Porsche AG.
