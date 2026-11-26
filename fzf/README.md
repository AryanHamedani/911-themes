# 911 for fzf

A dark, glare-free [fzf](https://github.com/junegunn/fzf) fuzzy finder theme and cockpit layout inspired by the **Porsche 911 (`992.2`) Precision Night Cockpit**.

Calibrated in OKLCH for 8-hour daily engineering sessions with every readable foreground/background pair verified at WCAG AA (`>= 4.5:1`).

## Surface & Accent Architecture

| Plane / Role | Hex | Token / Purpose |
|---|---|---|
| Preview well (`preview-bg`) | `#0c0e11` | Deep carbon recessed inspection pane (`13.79:1` w/ `#dadad6`) |
| Chrome bars (`input-bg`, `header-bg`, `footer-bg`) | `#131519` | Race-Tex chrome command bar & header/footer planes |
| List canvas (`bg`, `list-bg`, `gutter`) | `#141619` | Race-Tex Charcoal cockpit canvas (`12.93:1` w/ `#dadad6`) |
| Active row (`bg+` + `--highlight-line`) | `#261b1f` | Smoked Carmine full-width selection bar (`14.21:1` w/ `#edede9`) |
| Multi-select row (`selected-bg`) | `#292d36` | Slate Grey Neo distinct from active cursor (`11.75:1` w/ `#edede9`) |
| Focus needle (`prompt`, `pointer`) | `#e55c5a` | Guards Red (`90/9/1` restrained focal indicator) |
| Match highlights (`hl`, `hl+`, `selected-hl`) | `#e0be66` / `#f0d282` | PCCB Racing Gold & Weissgold bold highlights (`>= 9.35:1`) |
| Telemetry & indicators (`marker`, `spinner`, `info`) | `#7fb887` / `#6ac4cb` / `#9297a2` | Oak Green multi-select, Ice Glacier spinner, GT Silver counters |

## Ergonomics

`911.sh` is POSIX-compatible and prepends clean command-palette defaults before any existing `$FZF_DEFAULT_OPTS` (so your own layout flags always win), then appends all 44 `--color` roles:

- `--layout=reverse --border=rounded --info=inline-right`
- `--prompt='› ' --pointer='▌' --marker='┃' --separator='─' --scrollbar='▎' --ellipsis='…'`
- `--scroll-off=3 --highlight-line`

## Files Included

- `911.sh` — POSIX-compatible shell snippet setting cockpit layout defaults and 44 `--color` roles in `FZF_DEFAULT_OPTS`.

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
