# 911 for Claude Code

Porsche 911 (`992.2`) Precision Night Cockpit theme for [Claude Code](https://docs.anthropic.com/en/docs/claude-code) — Race-Tex Charcoal (`#141619`), Ice Grey (`#dadad6`), GT Silver (`#9297a2`), and disciplined 911 Guards/Carmine Red (`#e55c5a`) focus accents.

## Files

- `911.json` — Complete Claude Code custom theme defining all 37 `overrides` keys aligned with the canonical `911` (`992.2`) palette contract and WCAG AA (`>= 4.5:1`) contrast targets:
  - **4-surface message separation**: Assistant prose on Race-Tex canvas (`#141619`), user prompts on Vanadium elevated (`#1d2026`, hover `#252932`), `!` bash commands in recessed carbon (`#0f1114`), and `#` memory cards in subtle warm amber (`#282721`).
  - **Mode & tool-call clarity**: Guards Red (`#e55c5a`) active prompt border and rate-limit needle, Ice Glacier Cyan (`#6ac4cb`) plan mode & suggestions, Lugano Blue (`#6fa2de`) permissions & user brief label, PCCB Racing Gold (`#e0be66`) auto-accept & warnings, and Lava Orange (`#e89158`) bash mode border.
  - **Canonical opaque diffs**: `#202825` / `#2d2023` line tints, `#1f2624` / `#2a2124` dimmed tints, and `#293646` / `#332024` inline word emphasis.

## Install

Copy `911.json` into your Claude Code theme configuration or let Omarchy's active `911` theme manage `~/.local/state/omarchy/current/theme/claude.json`.

## Validate

```bash
python3 -c 'import json; d=json.load(open("911.json")); assert d["name"]=="911" and d["base"]=="dark" and len(d["overrides"])==37'
```

## Disclaimer

Not affiliated with or endorsed by Porsche AG. Porsche and 911 are trademarks of Porsche AG.
