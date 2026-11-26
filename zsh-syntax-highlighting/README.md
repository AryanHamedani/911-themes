# 911 for zsh-syntax-highlighting

A dark, glare-free [zsh-syntax-highlighting](https://github.com/zsh-users/zsh-syntax-highlighting) theme inspired by the **Porsche 911 (`992.2`) Precision Night Cockpit**: **Ice Grey (Crayon)** (`#dadad6`), **Oak Green Metallic Neo** (`#7fb887`) commands, **Lugano Blue** (`#6fa2de`) builtins and functions, **Brushed Dark Silver** (`#b4b7be`) flags, **PCCB Racing Gold** (`#e0be66`) strings, **Lava Orange** (`#e89158`) redirections and arithmetic, and restrained **Guards/Carmine Red** (`#e55c5a` / `#bf3b3e`) reserved strictly for pipeline separators, typos, and destructive warnings.

Calibrated in OKLCH for 8-hour daily sessions and verified to WCAG AA (`>= 4.5:1`) on every foreground/background pair.

## Files Included

- `911.zsh` — Complete `ZSH_HIGHLIGHT_STYLES` and `ZSH_HIGHLIGHT_PATTERNS` configuration covering all 59 token styles across the `main`, `brackets`, `pattern`, `cursor`, `root`, and `line` highlighters:
  - **Commands & errors**: valid executables/aliases in `#7fb887`, builtins/functions in `#6fa2de`, global aliases in `#6ac4cb`, precommands/autodirectories in `#98ce9f,underline`, unknown/typo commands in `#e56c6a,bold`.
  - **Paths & flags**: existing paths underlined in `#dadad6` with muted `#9297a2` `/` separators (breaking underlines cleanly per segment), partial `path_prefix` matches in `#b4b7be,underline`, and CLI flags in `#b4b7be`.
  - **Quotes & substitutions**: strings in `#e0be66` / `#f0d282` with `#6ac4cb` variable interpolations, `#84d8de` escapes, Ultraviolet `#b488cc` / `#caa2e0` substitution delimiters, and calm `#f48583,underline` unclosed-quote feedback while typing.
  - **Brackets**: 5-level matching cycle (`#6fa2de`, `#e0be66`, `#7fb887`, `#b488cc`, `#6ac4cb`), `#edede9` on `#292d36` underlined matching-pair highlight, and `#f48583` on `#2a2124` unmatched-bracket diagnostic pill.
  - **Safety redline**: AA-verified Guards Red badge (`fg=#f4f3ef,bg=#bf3b3e,bold`, `4.84:1`) on `root` sessions and destructive `rm -rf` / `rm -fr` invocations (leaving target paths readable).

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
