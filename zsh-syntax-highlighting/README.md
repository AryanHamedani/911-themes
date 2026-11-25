# Carrera for zsh-syntax-highlighting

A dark, glare-free [zsh-syntax-highlighting](https://github.com/zsh-users/zsh-syntax-highlighting) theme inspired by the Porsche 911 Heritage Cockpit on a night drive: **Basalt Alcantara** (`#15171a`) surfaces, warm **Chalk (`Kreide`)** (`#d6d2c7`) dial numerals, and a disciplined spark of **Carmine Red** (`#e1656c`).

Calibrated in OKLCH for long daily sessions and tuned to WCAG AA / APCA contrast targets.

## Files Included

- `carrera.zsh` — 24-bit `#rrggbb` `ZSH_HIGHLIGHT_STYLES` definitions covering `main`, `brackets`, `cursor`, `root`, and `line` highlighters.

## Manual Install

1. Copy `carrera.zsh` to a themes directory (for example, `~/.config/zsh/themes/carrera.zsh`):

   ```sh
   mkdir -p ~/.config/zsh/themes
   cp carrera.zsh ~/.config/zsh/themes/carrera.zsh
   ```

2. Source it in `~/.zshrc` (before or after sourcing `zsh-syntax-highlighting.zsh`):

   ```zsh
   # Optional: enable bracket highlighting as well
   # ZSH_HIGHLIGHT_HIGHLIGHTERS=(main brackets)

   source ~/.config/zsh/themes/carrera.zsh
   source /usr/share/zsh/plugins/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh
   ```

Palette reference: [`../colors.toml`](../colors.toml).

---

Not affiliated with or endorsed by Porsche AG. Porsche, 911 and Carrera are trademarks of Porsche AG.

License: [MIT](../LICENSE)
