# 911 for Atuin

A dark, glare-free [Atuin](https://atuin.sh) shell history TUI theme inspired by the **Porsche 911 (`992.2`) Precision Night Cockpit**: a strict 5-step mineral typographic hierarchy (`#edede9` -> `#dadad6` -> `#b4b7be` -> `#9297a2` -> `#858a96`), **Guards/Carmine Red** (`#e55c5a` / `#e56c6a`) as a disciplined instrument needle, and OKLCH-calibrated shell syntax tokens synchronized 1:1 with `zsh-syntax-highlighting/911.zsh`.

Calibrated in OKLCH for 8-hour daily sessions and verified to WCAG AA (`>= 5.19:1` on `#141619` and `>= 4.67:1` on `#1d2026` across all 15 keys).

## Files Included

- `911.toml` — Complete 15-key Atuin theme covering every PascalCase `Meaning` key (`AlertInfo`, `AlertWarn`, `AlertError`, `Title`, `Base`, `Annotation`, `Guidance`, `Muted`, `Important`, `SyntaxCommand`, `SyntaxFlag`, `SyntaxString`, `SyntaxVariable`, `SyntaxOperator`, `SyntaxComment`).

## Palette & Role Mapping

| Meaning Key | Hex | 911 Token | Contrast on `#141619` | Atuin TUI Role |
|---|---|---|---|---|
| `Title` | `#edede9` | Pure dial highlight | `15.44:1` | Section & view headers |
| `Base` | `#dadad6` | Ice Grey (Crayon) | `12.93:1` | Default command text & version |
| `Annotation` | `#b4b7be` | Brushed dark silver | `9.03:1` | Preview pane, keymap hints, history count, directory/datetime/host columns |
| `Guidance` | `#9297a2` | GT Silver in shadow | `6.19:1` | Relative timestamps (`5m ago`) & contextual guidance |
| `Muted` | `#858a96` | Unlit gauge markings | `5.24:1` | Subdued chrome & borders |
| `Important` | `#e55c5a` | Guards/Carmine Red | `5.19:1` | Active tab needle & Inspector emphasis |
| `AlertInfo` | `#7fb887` | Oak Green Metallic Neo | `7.86:1` | Success durations, exit `0`, info alerts |
| `AlertWarn` | `#e0be66` | PCCB Racing Gold | `10.12:1` | Matched search characters on selected row, warnings |
| `AlertError` | `#e56c6a` | Carmine Red (text) | `5.77:1` | Selected command row, failed durations, non-zero exit codes |
| `SyntaxCommand` | `#7fb887` | Oak Green Metallic Neo | `7.86:1` | Executables & aliases |
| `SyntaxFlag` | `#b4b7be` | Brushed dark silver | `9.03:1` | Short & long flags |
| `SyntaxString` | `#e0be66` | PCCB Racing Gold | `10.12:1` | Quoted strings |
| `SyntaxVariable` | `#6ac4cb` | Ice Glacier Cyan | `8.95:1` | Variables & expansions |
| `SyntaxOperator` | `#e89158` | Lava Orange | `7.44:1` | Pipes, redirections & operators |
| `SyntaxComment` | `#858a96` | Unlit gauge markings | `5.24:1` | Inline shell comments |

## Manual Install

1. Copy `911.toml` to your Atuin themes directory (`~/.atuin/themes/` or `~/.config/atuin/themes/` depending on `atuin info`):

   ```sh
   mkdir -p ~/.atuin/themes
   cp 911.toml ~/.atuin/themes/911.toml
   ```

2. Activate the theme and recommended cockpit ergonomics in `~/.atuin/config.toml`:

   ```toml
   style = "compact"
   inline_height = 24
   show_preview = true
   max_preview_height = 4
   show_help = true
   show_tabs = true

   [preview]
   strategy = "auto"

   [theme]
   name = "911"
   max_depth = 10

   [ui]
   syntax_highlight = true
   ```

Palette reference: [`../colors.toml`](../colors.toml).

---

Not affiliated with or endorsed by Porsche AG. Porsche and 911 are trademarks of Porsche AG.

License: [MIT](../LICENSE)
