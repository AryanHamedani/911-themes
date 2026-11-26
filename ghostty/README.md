# 911 for Ghostty

A dark, glare-free [Ghostty](https://ghostty.org) terminal theme inspired by the **Porsche 911 (`992.2`) Precision Night Cockpit**: **Race-Tex Charcoal** (`#141619`) surfaces, **Ice Grey (Crayon)** (`#dadad6`) dial typography, and a disciplined spark of **Guards/Carmine Red** (`#e55c5a`).

Calibrated in OKLCH for 8-hour daily engineering sessions and verified to WCAG AA (`>= 4.5:1`) contrast targets across every surface, highlight, and ANSI entry.

## Files Included

- [`911`](911) — Complete standalone Ghostty theme covering background/foreground, cursor, selection, split divider, unfocused split fill & opacity, search match/selected-match highlights, Race-Tex chrome GTK titlebar, AA-calibrated `faint-opacity`, and all 16 ANSI palette entries.

## Design Highlights

- **Cockpit Surface Hierarchy**: Deep diffuser cursor ink (`#0a0b0d`) → Recessed carbon unfocused split well (`#0f1114` at `0.85` opacity) → Race-Tex chrome titlebar (`#131519`, `13.04:1` AAA when `window-theme = ghostty`) → Race-Tex Charcoal canvas (`#141619`, `12.93:1` AAA) → Slate Grey Neo selection (`#292d36`, `11.75:1` AAA) → Vanadium hairline split divider (`#2f3440`).
- **Guards Red Discipline**: Standalone cursor needle (`#e55c5a` with `#0a0b0d` ink, `5.63:1` AA) and active search match badge (`#bf3b3e` with `#f4f3ef` ink, `4.84:1` AA); candidate search matches use the calibrated 35% PCCB Racing Gold tint (`#5b5134` with `#edede9` ink, `6.70:1` AA).
- **Legible Dim & Semantic Palette**: `faint-opacity = 0.6` keeps SGR dim text at `~5.3:1` AA (aligned with `muted = #858a96` at `5.24:1`) instead of Ghostty's `0.5` default (`4.09:1`). Every ANSI color 1–15 meets WCAG AA (`5.24:1`–`15.44:1`), and `bold-color` is intentionally left unset so bold text preserves semantic ANSI hues.

## Manual Install

1. Copy `911` to your Ghostty themes directory:

   ```sh
   mkdir -p ~/.config/ghostty/themes
   cp 911 ~/.config/ghostty/themes/911
   ```

2. Enable it in `~/.config/ghostty/config`:

   ```ini
   theme = 911
   ```

> **Omarchy note**: On Omarchy with the active `911` theme, `~/.config/ghostty/config` already includes `~/.local/state/omarchy/current/theme/ghostty.conf` (which maps `cursor-color` to `bright_foreground` `#edede9` at runtime). Standalone `911` uses the canonical `#e55c5a` Guards/Carmine Red cursor needle.

Palette reference: [`../colors.toml`](../colors.toml).

---

Not affiliated with or endorsed by Porsche AG. Porsche and 911 are trademarks of Porsche AG.

License: [MIT](../LICENSE)
