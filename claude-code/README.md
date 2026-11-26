# 911 for Claude Code

Porsche 911 (`992.2`) Precision Night Cockpit theme for [Claude Code](https://docs.anthropic.com/en/docs/claude-code) — Race-Tex Charcoal (`#141619`), Ice Grey (`#dadad6`), GT Silver (`#9297a2`), and 911 Guards/Carmine Red (`#e55c5a`).

## Files

- `911.json` — Complete Claude Code custom theme defining all 37 `overrides` keys aligned with the canonical `911` palette contract.

## Install

Copy `911.json` into your Claude Code theme configuration or let Omarchy's active `911` theme manage `~/.local/state/omarchy/current/theme/claude.json`.

## Validate

```bash
python3 -c 'import json; d=json.load(open("911.json")); assert d["name"]=="911" and len(d["overrides"])==37'
```

## Disclaimer

Not affiliated with or endorsed by Porsche AG. Porsche and 911 are trademarks of Porsche AG.
