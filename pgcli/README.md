# 911 for pgcli

Porsche 911 (`992.2`) Precision Night Cockpit theme for [pgcli](https://www.pgcli.com/) — Race-Tex Charcoal (`#141619`), Ice Grey (`#dadad6`), GT Silver (`#9297a2`), and 911 Guards/Carmine Red (`#e55c5a`).

## Files

- `911.pgclirc` — Complete `[main]` and `[colors]` configuration covering all Prompt Toolkit UI elements (completion menu, scrollbar, search/selection, toolbars, transaction states, tabular output) and Pygments SQL token styles (`pygments.*`).

## Install

```bash
mkdir -p ~/.config/pgcli
cp 911.pgclirc ~/.config/pgcli/config
```

(If you already have a `~/.config/pgcli/config`, merge the `[colors]` section and `syntax_style = native` under `[main]`.)

## Validate

```bash
python3 -c 'import configparser; c=configparser.ConfigParser(); c.read("911.pgclirc"); assert "colors" in c and len(c["colors"]) >= 45'
```

## Disclaimer

Not affiliated with or endorsed by Porsche AG. Porsche and 911 are trademarks of Porsche AG.
