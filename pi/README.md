# 911 for Pi

Porsche 911 (`992.2`) Precision Night Cockpit theme for [Pi](https://pi.dev/) — Race-Tex Charcoal (`#141619`), Vanadium Grey elevated surfaces (`#1a1d23` / `#1d2026`), Ice Grey (`#dadad6`), GT Silver (`#9297a2`), and a restrained 911 Guards/Carmine Red (`#e55c5a`) instrument needle.

## Design Architecture

- **4-Plane Cockpit Surfaces**: Recessed carbon export well (`#0f1114`) → Race-Tex Charcoal canvas (`#141619`) → Vanadium Grey message/tool cards (`#1a1d23` / `#1d2026`) → Smoked Carmine active selection (`#261b1f`) and canonical search match (`#5b5134`).
- **90/9/1 Guards Red Restraint**: `#e55c5a` is reserved for primary focus (`accent`, `borderAccent`) and `thinkingMax` redline; tool headers (`#edede9`), Markdown links (`#6fa2de`), and custom message labels (`#6fa2de`) stay calm for 8-hour daily sessions.
- **Tachometer Thinking Ramp**: Monotonic rev-counter progression from `thinkingOff` (`#858a96`) → `thinkingMinimal` (`#9297a2`) → `thinkingLow` (`#6ac4cb`) → `thinkingMedium` (`#6fa2de`) → `thinkingHigh` (`#e0be66`) → `thinkingXhigh` (`#e89158`) → `thinkingMax` (`#e55c5a`).
- **Canonical Syntax & Tool States**: Aligned 1:1 with `neovim/colors/911.lua` and `opencode/911.json` (Lava Orange `#e89158` numbers, PCCB Gold `#e0be66` types, Oak Green `#7fb887` strings, Lugano Blue `#6fa2de` functions, Carmine Red `#e56c6a` keywords) and calm opaque tool panels (`#1d2026` pending, `#202825` success, `#2d2023` error).

## Files

- `911.json` — Complete 56-token Pi theme (`vars`, `colors`, `export`) covering cockpit surfaces, borders, scrollbars, search matches, tool states, diffs, Markdown, syntax tokens, thinking levels, and HTML exports.

## Install

Copy `911.json` to `~/.pi/agent/themes/911.json` and set `"theme": "911"` in `~/.pi/agent/settings.json` (on Omarchy with the `911` theme active, `~/.pi/agent/themes/omarchy-system.json` is automatically kept in sync).

## Validate

```bash
python3 -c 'import json; d=json.load(open("911.json")); assert d["name"]=="911" and "colors" in d and "export" in d'
```

## Disclaimer

Not affiliated with or endorsed by Porsche AG. Porsche and 911 are trademarks of Porsche AG.
