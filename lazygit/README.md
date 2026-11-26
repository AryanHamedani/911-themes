# 911 for Lazygit

Porsche 911 (`992.2`) Precision Night Cockpit theme for [Lazygit](https://github.com/jesseduffield/lazygit) — Race-Tex Charcoal (`#141619`), Ice Grey (`#dadad6`), GT Silver (`#9297a2`), and 911 Guards/Carmine Red (`#e55c5a`).

## Files

- `911.yml` — Complete `gui.theme` configuration covering all 15 Lazygit theme keys (`activeBorderColor`, `inactiveBorderColor`, `searchingActiveBorderColor`, `optionsTextColor`, `selectedLineFgColor`, `selectedLineBgColor`, `inactiveViewSelectedLineBgColor`, `cherryPickedCommitFgColor`, `cherryPickedCommitBgColor`, `markedBaseCommitFgColor`, `markedBaseCommitBgColor`, `unstagedChangesColor`, `defaultFgColor`, `authorColors`, `branchColorPatterns`).

## Install

Merge the `gui.theme` block from `911.yml` into `~/.config/lazygit/config.yml`, or pass it alongside your config:

```bash
lazygit --use-config-file="$HOME/.config/lazygit/config.yml,$PWD/911.yml"
```

## Validate

```bash
python3 -c 'import yaml; d=yaml.safe_load(open("911.yml")); assert len(d["gui"]["theme"])==15'
```

## Disclaimer

Not affiliated with or endorsed by Porsche AG. Porsche and 911 are trademarks of Porsche AG.
