# Carrera for Delta

Porsche 911 Heritage Cockpit (`Carrera v2.0.0`) theme for [delta](https://github.com/dandavison/delta) — Basalt Alcantara (`#15171a`), Chalk (`#d6d2c7`), GT Silver (`#9599a2`), and Carmine Red (`#e1656c`).

## Files

- `carrera.gitconfig` — Named `[delta "carrera"]` feature include defining diff, line-number, file, hunk-header, commit, blame, and whitespace styles.

### Derived Hex Notes

- `plus-style` (`#222a23`) and `minus-style` (`#2d1e20`) use the shared `Carrera` opaque diff tints over `#15171a`; `plus-emph-style` (`#3a4b3a`) and `minus-emph-style` (`#563537`) use the 32% `green`/`red` over `#15171a` mixes from Omarchy's theme templates.
- `commit-decoration-style` uses `#31353f` (`btop.theme` `div_line`).
- `syntax-theme = ansi` is set so `carrera.gitconfig` runs without warnings standalone. If you also install `../bat/Carrera.tmTheme` and rebuild `bat cache --build`, override with `syntax-theme = Carrera` under `[delta]`.

## Installation

1. Copy `carrera.gitconfig` to `~/.config/git/carrera.gitconfig`:

   ```bash
   mkdir -p ~/.config/git
   cp carrera.gitconfig ~/.config/git/carrera.gitconfig
   ```

2. Include it and enable the `carrera` feature manually in `~/.config/git/config` (this repository does not modify your active config):

   ```ini
   [include]
       path = ~/.config/git/carrera.gitconfig

   [delta]
       features = carrera
   ```

## Verification

```bash
git config --file carrera.gitconfig --list | grep -q '^delta\.carrera\.'
TMP=$(mktemp -d)
printf '[include]\n    path = %s/carrera.gitconfig\n[delta]\n    features = carrera\n' "$PWD" > "$TMP/delta.gitconfig"
printf 'diff --git a/a b/a\n--- a/a\n+++ b/a\n@@ -1 +1 @@\n-old\n+new\n' | HOME="$TMP" XDG_CONFIG_HOME="$TMP/xdg" delta --config "$TMP/delta.gitconfig" --true-color=always --paging=never
rm -rf "$TMP"
```

## License

[MIT](../LICENSE) — Copyright (c) 2026 Aryan Hamedani.

Not affiliated with or endorsed by Porsche AG. Porsche, 911 and Carrera are trademarks of Porsche AG.
