# 911 for fzf

A dark, glare-free [fzf](https://github.com/junegunn/fzf) fuzzy finder theme inspired by the **Porsche 911 (`992.2`) Precision Night Cockpit**: **Race-Tex Charcoal** (`#141619`) list plane, **Carbon Well** (`#0f1114`) preview plane, **Vanadium Grey** (`#1d2026`) active line, and **Guards/Carmine Red** (`#e55c5a`) prompt, pointer, and match highlights.

Calibrated in OKLCH for long daily sessions and verified to WCAG AA contrast targets.

## Files Included

- `911.sh` — POSIX-compatible shell snippet appending 40+ `--color` roles to `FZF_DEFAULT_OPTS` (preserving any existing layout flags).

## Manual Install

1. Copy `911.sh` to `~/.config/zsh/fzf-911.sh`:

   ```sh
   mkdir -p ~/.config/zsh
   cp 911.sh ~/.config/zsh/fzf-911.sh
   ```

2. Source it from `~/.zshrc` (or `~/.bashrc`):

   ```sh
   source ~/.config/zsh/fzf-911.sh
   ```

Palette reference: [`../colors.toml`](../colors.toml).

---

Not affiliated with or endorsed by Porsche AG. Porsche and 911 are trademarks of Porsche AG.

License: [MIT](../LICENSE)
