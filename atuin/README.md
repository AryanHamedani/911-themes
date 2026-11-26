# 911 for Atuin

A dark, glare-free [Atuin](https://atuin.sh) shell history TUI theme inspired by the **Porsche 911 (`992.2`) Precision Night Cockpit**: **Ice Grey (Crayon)** (`#dadad6`) command text, **Guards/Carmine Red** (`#e55c5a`) highlights, and OKLCH-calibrated semantic syntax colors.

Calibrated in OKLCH for long daily sessions and verified to WCAG AA contrast targets.

## Files Included

- `911.toml` — Complete Atuin theme with all PascalCase Meaning keys (`AlertInfo`, `AlertWarn`, `AlertError`, `Annotation`, `Base`, `Guidance`, `Important`, `Title`, `Muted`, `SyntaxCommand`, `SyntaxFlag`, `SyntaxString`, `SyntaxVariable`, `SyntaxOperator`, `SyntaxComment`).

## Manual Install

1. Copy `911.toml` to your Atuin themes directory (`~/.atuin/themes/` or `~/.config/atuin/themes/` depending on `atuin info`):

   ```sh
   mkdir -p ~/.atuin/themes
   cp 911.toml ~/.atuin/themes/911.toml
   ```

2. Activate it in `~/.atuin/config.toml`:

   ```toml
   [theme]
   name = "911"
   ```

Palette reference: [`../colors.toml`](../colors.toml).

---

Not affiliated with or endorsed by Porsche AG. Porsche and 911 are trademarks of Porsche AG.

License: [MIT](../LICENSE)
