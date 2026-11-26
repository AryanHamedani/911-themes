# 911 for OpenCode

Porsche 911 (`992.2`) Precision Night Cockpit theme for [OpenCode](https://opencode.ai/) — Race-Tex Charcoal (`#141619`), Ice Grey (`#dadad6`), GT Silver (`#9297a2`), and restrained 911 Guards/Carmine Red (`#e55c5a`) focus accents.

## Design Highlights

- **4-Plane Cockpit Depth**: Recessed carbon panels (`#0f1114`) → Race-Tex canvas (`#141619`) → Vanadium elevated menus (`#1a1d23`) → raised interactive elements (`#1d2026`).
- **WCAG AA Contrast (`>= 4.5:1`)**: Deep diffuser ink (`#0a0b0d`) on Guards Red selected list items (`5.63:1`) and destructive actions (`6.26:1`), GT Silver (`#9297a2`) diff gutter line numbers (`>= 5.27:1` on add/delete gutter tints), and glare-free Ice Grey (`#dadad6`, `12.93:1`) body text.
- **90/9/1 Guards Red Restraint**: Guards Red (`#e55c5a`) is reserved for primary focus, active borders, and interactive selection; Markdown headings (`#6fa2de`) and list bullets (`#9297a2`) stay calm for long AI coding sessions.
- **Canonical Diff Tints**: Opaque `alpha-over-#141619` diff fills (`#202825` / `#2d2023`) and line-number gutter tints (`#1f2624` / `#2a2124`).

## Files

- `911.json` — Complete OpenCode theme (`$schema`, `defs`, `theme`) covering UI chrome, 4-plane cockpit surfaces, borders, diffs, Markdown, syntax highlighting, and `thinkingOpacity`.

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
