# 911 for eza

Porsche 911 (`992.2`) Precision Night Cockpit theme for [eza](https://eza.rocks/) (`v0.23.5`) — Race-Tex Charcoal (`#141619`), Ice Grey (`#dadad6`), GT Silver (`#9297a2`), and restrained 911 Guards/Carmine Red (`#e55c5a`) highlights.

## Files

- `theme.yml` — Complete `eza` theme covering `colourful`, `filekinds`, `perms`, `size`, `users`, `links`, `git`, `git_repo`, `security_context`, `file_type`, `punctuation`, `date`, `inode`, `blocks`, `header`, `octal`, `flags`, `symlink_path`, `control_char`, `broken_symlink`, `broken_path_overlay`, and `filenames` (immediate project files like `README.md`, `Makefile`, `Dockerfile`, `pyproject.toml`, `Cargo.toml`, `package.json`, `go.mod`, `.env`, `.gitignore`).

## Design Hierarchy

- **Calm metadata chrome:** Punctuation (`-`, `->`), inodes, blocks, and octal permissions stay muted (`#858a96`); timestamps, link counts, and secondary owners use GT Silver (`#9297a2`) and brushed silver (`#b4b7be`).
- **Progressive size scale:** Quiet bytes (`#9297a2`) → kilobytes (`#b4b7be`) → megabytes (`#dadad6`) → bold gold gigabytes (`#e0be66`) → bold Guards Red terabytes+ (`#e55c5a`).
- **Scannable file kinds & permissions:** Directories in bold Lugano Blue (`#6fa2de`), executables in bold Oak Green (`#7fb887`), symlinks in Ice Glacier Cyan (`#6ac4cb`), broken symlinks in bold underlined Carmine Red (`#e56c6a`); semantic `r`/`w`/`x` bits in `#e0be66` / `#e56c6a` / `#7fb887`.
- **Clean Git status:** Added (`#7fb887`), modified (`#e0be66`), deleted (`#e56c6a`), renamed (`#6ac4cb`), typechange (`#b488cc`), ignored (`#858a96`), and conflicted (`#e55c5a` bold).

## Install

```bash
mkdir -p ~/.config/eza
cp theme.yml ~/.config/eza/theme.yml
```

## Validate

```bash
python3 -c 'import yaml; d=yaml.safe_load(open("theme.yml")); assert d["colourful"] is True'
EZA_CONFIG_DIR="$PWD" eza -la --git --header --icons --color=always >/dev/null
```

## Disclaimer

Not affiliated with or endorsed by Porsche AG. Porsche and 911 are trademarks of Porsche AG.
