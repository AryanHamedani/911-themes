# 911 for bat

Porsche 911 (`992.2`) Precision Night Cockpit TextMate theme for [bat](https://github.com/sharkdp/bat) (and [delta](https://github.com/dandavison/delta) via `syntax-theme = 911`) — Race-Tex Charcoal (`#141619`), Ice Grey (`#dadad6`), GT Silver (`#9297a2`), and disciplined 911 Guards/Carmine Red (`#e55c5a`).

## Files

- `911.tmTheme` — Apple Property List XML 1.0 TextMate theme calibrated for `bat` / `syntect` Sublime grammars across Python, Go, TypeScript/JS, Rust, Bash/Zsh, YAML, JSON, TOML, SQL, Dockerfile, Diff, and Markdown:
  - Distinct docstrings/doc-comments (`#9297a2` italic) vs line comments (`#858a96` italic) and JSDoc/doc tags (`#ad7f66` italic)
  - Strings (`#7fb887`), interpolation delimiters (`#e55c5a`), format placeholders (`#caa2e0`), regex (`#6ac4cb`), and escapes (`#84d8de`)
  - Control/word keywords (`#e56c6a`) vs subtle symbolic operators and structural punctuation (`#9297a2`), storage modifiers (`#b488cc`), and primitive/SQL types (`#e0be66`)
  - User functions (`#6fa2de`) vs builtin functions/macros (`#6ac4cb`), types/classes (`#e0be66`), inherited classes (`#f0d282` italic), parameters (`#b4b7be` italic), `self`/`cls`/`this` (`#b488cc` italic), properties/shell vars (`#8cb9f2`), and decorators/annotations (`#ad7f66`)
  - Structured JSON/YAML/TOML keys (`#6fa2de`), TOML table headers & YAML anchors/aliases (`#e0be66` bold)
  - Full Markdown H1–H6 hierarchy (`#e55c5a` → `#e0be66` → `#6fa2de` → `#6ac4cb` → `#b488cc` → `#9297a2`), inline code pills (`#7fb887` on `#1a1d23`), fenced code blocks, links, blockquotes, and Guards Red list bullets
  - Diff hunk headers/ranges and canonical opaque diff tints (`#202825` inserted, `#2d2023` deleted, `#1f2731` changed), plus Guards Red illegal badge (`#f4f3ef` on `#bf3b3e`) and deprecated warning (`#e0be66` on `#282721`)

## Install

1. Copy `911.tmTheme` into bat's `themes/` directory and rebuild bat's theme cache:

   ```bash
   mkdir -p "$(bat --config-dir)/themes"
   cp 911.tmTheme "$(bat --config-dir)/themes/911.tmTheme"
   bat cache --build
   ```

2. Configure `~/.config/bat/config`:

   ```text
   # 911 (992.2) Precision Night Cockpit
   --theme="911"
   --style="numbers,changes,header"
   --italic-text=always
   ```

## Validate

```bash
python3 -c 'import plistlib; p=plistlib.load(open("911.tmTheme","rb")); assert p["name"]=="911"'
bat --list-themes | grep -x '911'
```

## Disclaimer

Not affiliated with or endorsed by Porsche AG. Porsche and 911 are trademarks of Porsche AG.
