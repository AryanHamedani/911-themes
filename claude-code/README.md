# Carrera for Claude Code

Porsche 911 Heritage Cockpit (`Carrera v2.0.0`) theme for [Claude Code](https://docs.anthropic.com/en/docs/claude-code) — Basalt Alcantara (`#15171a`), Chalk (`#d6d2c7`), GT Silver (`#9599a2`), and Carmine Red (`#e1656c`).

## Files

- `carrera.json` — Standalone custom theme (`base: "dark"`, all 37 `overrides` tokens).

### Derived Hex Notes

Shimmer, diff tint, and message surface overrides use Omarchy's theme templates with linear sRGB `mix(start, end, amount)` over `colors.toml` v2.0.0 (`claudeShimmer`: 35% `accent`→`foreground`; `inactive`/`inactiveShimmer`: 40%/25% `foreground`→`background`; `permissionShimmer`/`warningShimmer`: 35% token→`foreground`; `diffAdded`/`diffRemoved`: 15%/8%/32% `background`→`green`/`red`; `userMessageBackground`/`Hover`/`rate_limit_empty`: 6%/10%/20% `background`→`foreground`).

## Installation

1. Copy `carrera.json` to `~/.claude/themes/carrera.json`:

   ```bash
   mkdir -p ~/.claude/themes
   cp carrera.json ~/.claude/themes/carrera.json
   ```

2. Enable it manually in `~/.claude/settings.json` (this repository does not modify your active config):

   ```json
   {
     "theme": "custom:carrera"
   }
   ```

## Verification

```bash
python3 -c 'import json, re; d=json.load(open("carrera.json")); assert d["name"]=="Carrera" and d["base"]=="dark" and len(d["overrides"])==37 and all(re.fullmatch(r"#[0-9a-fA-F]{6}", v) for v in d["overrides"].values())'
```

## License

[MIT](../LICENSE) — Copyright (c) 2026 Aryan Hamedani.

Not affiliated with or endorsed by Porsche AG. Porsche, 911 and Carrera are trademarks of Porsche AG.
