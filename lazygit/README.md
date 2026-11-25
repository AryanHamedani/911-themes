# Carrera for Lazygit

Porsche 911 Heritage Cockpit (`Carrera v2.0.0`) theme for [Lazygit](https://github.com/jesseduffield/lazygit) — Basalt Alcantara (`#15171a`), Chalk (`#d6d2c7`), GT Silver (`#9599a2`), and Carmine Red (`#e1656c`).

## Files

- `carrera.yml` — `gui.theme` configuration covering all 15 Lazygit theme keys (`activeBorderColor`, `inactiveBorderColor`, `searchingActiveBorderColor`, `optionsTextColor`, `selectedLineFgColor`, `selectedLineBgColor`, `inactiveViewSelectedLineBgColor`, `cherryPickedCommitFgColor`, `cherryPickedCommitBgColor`, `markedBaseCommitFgColor`, `markedBaseCommitBgColor`, `unstagedChangesColor`, `defaultFgColor`, `authorColors`, `branchColorPatterns`).

### Derived Hex Notes

- `inactiveBorderColor` uses `#31353f` (`btop.theme` `div_line`).

## Installation

Merge the `gui.theme` block from `carrera.yml` manually into `~/.config/lazygit/config.yml` (this repository does not modify your active config), or pass it alongside your config with `lazygit --use-config-file="$HOME/.config/lazygit/config.yml,$HOME/.config/lazygit/carrera.yml"`.

## Verification

```bash
python3 -c 'import yaml; d=yaml.safe_load(open("carrera.yml")); assert len(d["gui"]["theme"])==15'
```

## License

[MIT](../LICENSE) — Copyright (c) 2026 Aryan Hamedani.

Not affiliated with or endorsed by Porsche AG. Porsche, 911 and Carrera are trademarks of Porsche AG.
