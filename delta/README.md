# 911 for Delta

Porsche 911 (`992.2`) Precision Night Cockpit theme for [delta](https://github.com/dandavison/delta) — Race-Tex Charcoal (`#141619`), Ice Grey (`#dadad6`), GT Silver (`#9297a2`), and 911 Guards/Carmine Red (`#e55c5a`).

## Files

- `911.gitconfig` — Named `[delta "911"]` feature include defining diff lines, inline word emphasis, line numbers, file/commit/hunk headers, blame palette, grep/ripgrep styling, merge-conflict headers, and whitespace error highlights.

## Palette Notes

- `plus-style` (`#202825`) and `minus-style` (`#2d2023`) use the canonical `911` opaque diff tints over `#141619`; inline emphasis highlights with `bright_green` (`#98ce9f`) and `bright_red` (`#f48583`) over `#202825` and `#332024`.
- `syntax-theme = 911` pairs directly with `../bat/911.tmTheme` (install via `bat cache --build`).

## Install

1. Copy `911.gitconfig` to `~/.config/git/911-delta.gitconfig`:

   ```bash
   mkdir -p ~/.config/git
   cp 911.gitconfig ~/.config/git/911-delta.gitconfig
   ```

2. Include it and enable the `911` feature in `~/.config/git/config`:

   ```ini
   [include]
       path = ~/.config/git/911-delta.gitconfig
   [delta]
       features = 911
   ```

## Validate

```bash
git config --file 911.gitconfig --list | grep -q '^delta\.911\.'
```

## Disclaimer

Not affiliated with or endorsed by Porsche AG. Porsche and 911 are trademarks of Porsche AG.
