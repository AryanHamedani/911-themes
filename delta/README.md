# 911 for Delta

Porsche 911 (`992.2`) Precision Night Cockpit theme for [delta](https://github.com/dandavison/delta) — Race-Tex Charcoal (`#141619`), Ice Grey (`#dadad6`), GT Silver (`#9297a2`), and 911 Guards/Carmine Red (`#e55c5a`).

## Files

- `911.gitconfig` — Named `[delta "911"]` feature include defining precision 2-tier diff highlights, inline word emphasis, tabular line numbers, Guards Red file headers, sculpted hunk headers, 4-step cockpit `blame-palette`, `rg --json | delta` grep styling, `zdiff3` merge-conflict headers, moved-block `map-styles`, OSC 8 `hyperlinks`, `navigate`, and whitespace error badges.

## Palette Notes

- **2-tier diff highlights**: `plus-style` (`#202825`) and `minus-style` (`#2d2023`) use the canonical `911` opaque tints over `#141619` with full syntax highlighting; inline word emphasis (`plus-emph-style`, `minus-emph-style`) elevates exact changed tokens with `bright_green` (`#98ce9f` bold underline on `#202825`, `8.38:1` AA) and `bright_red` (`#f48583` bold underline on `#332024`, `6.21:1` AA).
- **4-step blame ladder**: `blame-palette` steps cleanly across `#141619` (canvas) -> `#1a1d23` (Vanadium elevated) -> `#1d2026` (Vanadium lighter) -> `#261b1f` (Smoked Carmine), with `blame-code-style = syntax` keeping source text glare-free.
- **Moved blocks (`--color-moved`)**: `map-styles` maps git's moved-block ANSI styles to `#261b1f`, `#1f2731`, `#1d272b`, and `#282721` while preserving syntax highlighting.
- **Syntax theme**: `syntax-theme = 911` pairs directly with `../bat/911.tmTheme` (install via `bat cache --build`).

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

   > Note: In `delta`, keys set directly under `[delta]` take precedence over `[delta "<feature>"]` sections. Ensure no earlier included config sets conflicting keys under `[delta]` if you want `[delta "911"]` to control every setting.

## Validate

```bash
git config --file 911.gitconfig --list | grep -q '^delta\.911\.'
delta --config 911.gitconfig --features 911 --show-config
```

## Disclaimer

Not affiliated with or endorsed by Porsche AG. Porsche and 911 are trademarks of Porsche AG.
