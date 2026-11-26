# 911 for pgcli

Porsche 911 (`992.2`) Precision Night Cockpit theme for [pgcli](https://www.pgcli.com/) — Race-Tex Charcoal (`#141619`), Race-Tex chrome (`#131519`), Vanadium elevated menus (`#1a1d23`), Smoked Carmine active selection (`#261b1f`), Ice Grey dial typography (`#dadad6`), and 911 Guards/Carmine Red (`#e55c5a` / `#bf3b3e`) instrument needles.

## Files

- `911.pgclirc` — Complete `[main]` cockpit ergonomics (`psql_unicode` hairline tables, compact `∅` null indicator, multi-column completion menu, transaction-aware prompt `\u@\h:\d\T> `, `keyword_casing = auto`) and full `[colors]` coverage across Prompt Toolkit UI surfaces (completion menu + fuzzy-match highlights, scrollbar, search/incsearch, matching brackets, auto-suggestions, Race-Tex toolbars, transaction badges, tabular output) and PostgreSQL Pygments tokens (`pygments.*`).

## Install

```bash
mkdir -p ~/.config/pgcli
cp 911.pgclirc ~/.config/pgcli/config
```

If you already have a `~/.config/pgcli/config` with `[alias_dsn]`, `[named queries]`, or `[init-commands]`, merge `[main]` and `[colors]` into your existing file instead of overwriting it.

## Validate

```bash
pgcli --pgclirc 911.pgclirc --list-dsn
```

## Disclaimer

Not affiliated with or endorsed by Porsche AG. Porsche and 911 are trademarks of Porsche AG.
