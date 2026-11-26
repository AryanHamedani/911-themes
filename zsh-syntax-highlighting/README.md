# 911 for zsh-syntax-highlighting

A dark, glare-free [zsh-syntax-highlighting](https://github.com/zsh-users/zsh-syntax-highlighting) theme inspired by the **Porsche 911 (`992.2`) Precision Night Cockpit**: **Ice Grey (Crayon)** (`#dadad6`), **Oak Green Metallic Neo** (`#7fb887`) commands, **Lugano Blue** (`#6fa2de`) builtins/functions, **PCCB Racing Gold** (`#e0be66`) strings, **Lava Orange** (`#e89158`) redirections/arithmetic, and **Guards/Carmine Red** (`#e55c5a`) delimiters.

Calibrated in OKLCH for long daily sessions and verified to WCAG AA contrast targets.

## Files Included

- `911.zsh` — Complete `ZSH_HIGHLIGHT_STYLES` associative array covering 55+ token styles across the `main`, `brackets` (levels 1–5 + `cursor-matchingbracket`), `cursor`, `root` (Guards Red `#bf3b3e` badge with `#f4f3ef` ink, `4.84:1` AA), and `line` highlighters.

## Manual Install

1. Copy `911.zsh` to `~/.config/zsh/zsh-syntax-highlighting-911.zsh`:

   ```sh
   mkdir -p ~/.config/zsh
   cp 911.zsh ~/.config/zsh/zsh-syntax-highlighting-911.zsh
   ```

2. Source it in `~/.zshrc` **after** `zsh-syntax-highlighting.zsh`:

   ```zsh
   source /usr/share/zsh/plugins/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh
   source ~/.config/zsh/zsh-syntax-highlighting-911.zsh
   ```

Palette reference: [`../colors.toml`](../colors.toml).

---

Not affiliated with or endorsed by Porsche AG. Porsche and 911 are trademarks of Porsche AG.

License: [MIT](../LICENSE)
