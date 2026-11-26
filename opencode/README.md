# 911 for OpenCode

Porsche 911 (`992.2`) Precision Night Cockpit theme for [OpenCode](https://opencode.ai/) — Race-Tex Charcoal (`#141619`), Ice Grey (`#dadad6`), GT Silver (`#9297a2`), and 911 Guards/Carmine Red (`#e55c5a`).

## Files

- `911.json` — Complete OpenCode theme (`$schema`, `defs`, `theme`) covering UI chrome, cockpit planes, borders, diffs, Markdown, and syntax highlighting.

## Install

1. Copy `911.json` to `~/.config/opencode/themes/911.json`:

   ```bash
   mkdir -p ~/.config/opencode/themes
   cp 911.json ~/.config/opencode/themes/911.json
   ```

2. Set `"theme": "911"` in `~/.config/opencode/opencode.json`.

## Validate

```bash
python3 -c 'import json; d=json.load(open("911.json")); assert "defs" in d and "theme" in d'
```

## Disclaimer

Not affiliated with or endorsed by Porsche AG. Porsche and 911 are trademarks of Porsche AG.
