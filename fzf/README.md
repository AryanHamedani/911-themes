# Carrera for fzf

A dark, glare-free [fzf](https://github.com/junegunn/fzf) color theme inspired by the Porsche 911 Heritage Cockpit on a night drive: **Basalt Alcantara** (`#15171a`) surfaces, warm **Chalk (`Kreide`)** (`#d6d2c7`) dial numerals, and a disciplined spark of **Carmine Red** (`#e1656c`).

Calibrated in OKLCH for long daily sessions and tuned to WCAG AA / APCA contrast targets.

## Files Included

- `carrera.sh` — POSIX-compatible shell snippet (works in `sh`, `bash`, and `zsh`) that appends `--color=...` to `FZF_DEFAULT_OPTS` without clobbering existing layout flags.

## Manual Install

1. Copy `carrera.sh` to your shell config directory (for example, `~/.config/fzf/carrera.sh`):

   ```sh
   mkdir -p ~/.config/fzf
   cp carrera.sh ~/.config/fzf/carrera.sh
   ```

2. Source it in `~/.zshrc` or `~/.bashrc` **after** any layout options (`--border`, `--layout`, `--pointer`, etc.) so the `--color` flags apply on top without overwriting your layout:

   ```sh
   # Example layout flags (optional):
   # export FZF_DEFAULT_OPTS="--border=rounded --layout=reverse --info=inline-right"

   . ~/.config/fzf/carrera.sh
   ```

Palette reference: [`../colors.toml`](../colors.toml).

---

Not affiliated with or endorsed by Porsche AG. Porsche, 911 and Carrera are trademarks of Porsche AG.

License: [MIT](../LICENSE)
