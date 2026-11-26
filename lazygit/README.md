# 911 for Lazygit

Porsche 911 (`992.2`) Precision Night Cockpit theme and ergonomic configuration for [Lazygit](https://github.com/jesseduffield/lazygit) (`v0.66.2+`) — Race-Tex Charcoal (`#141619`), Vanadium Grey (`#1d2026`), Smoked Carmine selection (`#261b1f`), hairline borders (`#2f3440`), Ice Grey typography (`#dadad6` / `#edede9`), GT Silver metadata (`#9297a2`), Ice Glacier Cyan search (`#6ac4cb`), and disciplined 911 Guards Red (`#e55c5a`) focus.

## Files

- `911.yml` — Complete `gui` theme (all 15 `gui.theme` keys, including `authorColors` and semantic `branchColorPatterns`), ergonomic cockpit layout (`rounded` borders, Nerd Fonts v3, file numstats, branch hashes & divergence, auto-expanding focused side panel, quiet bottom chrome), and `git.diffRenderers` wired to `delta --dark --paging=never`.

## Palette Highlights

| Role | Token | Hex |
|---|---|---|
| Active panel border | Guards Red (`bold`) | `#e55c5a` |
| Inactive panel border | Hairline divider | `#2f3440` |
| Search / filter border | Ice Glacier Cyan (`bold`) | `#6ac4cb` |
| Active selection bg / fg | Smoked Carmine / Pure Dial (`bold`) | `#261b1f` / `#edede9` |
| Inactive selection bg | Vanadium Grey | `#1d2026` |
| Interactive options | Lugano Blue | `#6fa2de` |
| Unstaged changes | Carmine Red (text) | `#e56c6a` |
| Primary text / authors | Ice Grey / GT Silver | `#dadad6` / `#9297a2` |
| Cherry-picked commit | Deep Diffuser on Glacier Cyan | `#0a0b0d` on `#6ac4cb` |
| Marked rebase base | Deep Diffuser on Racing Gold | `#0a0b0d` on `#e0be66` |

## Install

Merge `911.yml` into `~/.config/lazygit/config.yml`, or layer it alongside your existing config:

```bash
lazygit --use-config-file="$HOME/.config/lazygit/config.yml,$PWD/911.yml"
```

Pair with `../delta/911.gitconfig` (and `../bat/911.tmTheme`) so diffs rendered by `delta --dark --paging=never` match the 911 cockpit seamlessly.

## Validate

```bash
python3 -c 'import yaml; d=yaml.safe_load(open("911.yml")); assert len(d["gui"]["theme"])==15'
```

## Disclaimer

Not affiliated with or endorsed by Porsche AG. Porsche and 911 are trademarks of Porsche AG.
