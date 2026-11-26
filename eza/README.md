# 911 for eza

Porsche 911 (`992.2`) Precision Night Cockpit theme for [eza](https://eza.rocks/) — Race-Tex Charcoal (`#141619`), Ice Grey (`#dadad6`), GT Silver (`#9297a2`), and 911 Guards/Carmine Red (`#e55c5a`).

## Files

- `theme.yml` — Complete eza theme covering `filekinds`, `perms`, `size`, `users`, `links`, `git`, `git_repo`, `security_context`, `file_type`, `punctuation`, `date`, `inode`, `blocks`, `header`, `octal`, `flags`, `symlink_path`, `control_char`, `broken_symlink`, and `broken_path_overlay`.

## Install

```bash
mkdir -p ~/.config/eza
cp theme.yml ~/.config/eza/theme.yml
```

## Validate

```bash
python3 -c 'import yaml; d=yaml.safe_load(open("theme.yml")); assert d["colourful"] is True'
EZA_CONFIG_DIR="$PWD" eza -la --git --color=always >/dev/null
```

## Disclaimer

Not affiliated with or endorsed by Porsche AG. Porsche and 911 are trademarks of Porsche AG.
