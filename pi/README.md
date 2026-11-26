# 911 for Pi

Porsche 911 (`992.2`) Precision Night Cockpit theme for [Pi](https://pi.dev/) — Race-Tex Charcoal (`#141619`), Ice Grey (`#dadad6`), GT Silver (`#9297a2`), and 911 Guards/Carmine Red (`#e55c5a`).

## Files

- `911.json` — Complete Pi theme (`vars`, `colors`, `export`) covering cockpit surfaces, borders, scrollbars, search matches, tool states, diffs, Markdown, syntax tokens, and thinking levels.

## Install

Copy `911.json` to `~/.pi/agent/themes/911.json` and set `"theme": "911"` in `~/.pi/agent/settings.json` (on Omarchy with the `911` theme active, `~/.pi/agent/themes/omarchy-system.json` is automatically kept in sync).

## Validate

```bash
python3 -c 'import json; d=json.load(open("911.json")); assert d["name"]=="911" and "colors" in d and "export" in d'
```

## Disclaimer

Not affiliated with or endorsed by Porsche AG. Porsche and 911 are trademarks of Porsche AG.
