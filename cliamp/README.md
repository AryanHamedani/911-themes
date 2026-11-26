# 911 for Cliamp

Porsche 911 (`992.2`) Precision Night Cockpit theme for [Cliamp](https://github.com/bjarneo/cliamp) — styled as a dark Porsche center-console audio instrument with Race-Tex Charcoal surfaces (`#141619`), glare-free dial highlights (`#edede9`), Ice Grey metadata (`#dadad6`), a disciplined Guards/Carmine Red playhead (`#e55c5a`), and an OKLCH-calibrated spectrum/VU/equalizer ramp.

## Files

- `911.toml` — Complete 7-key Cliamp theme (`bg`, `accent`, `bright_fg`, `fg`, `green`, `yellow`, `red`; strict `#RRGGBB` format).

## Token Mapping & Contrast

All 7 keys supported by Cliamp's `theme.Theme` schema map directly to canonical 911 (`992.2`) base tokens from `colors.toml` and pass WCAG AA (`>= 4.5:1`) on `#141619`:

| Key | Hex | 911 (`992.2`) Token | Cliamp Instrument Role | Contrast on `bg` |
|---|---|---|---|---|
| `bg` | `#141619` | Race-Tex Charcoal | Cockpit background surface | — |
| `accent` | `#e55c5a` | Guards/Carmine Red | Active playhead, progress bar, focus highlight | `5.19:1` (AA) |
| `bright_fg` | `#edede9` | Pure Dial Highlight | Active track title, primary digital readouts | `15.44:1` (AAA) |
| `fg` | `#dadad6` | Ice Grey (Crayon) | Playlist rows, metadata, switchgear labels | `12.93:1` (AAA) |
| `green` | `#7fb887` | Oak Green Metallic Neo | Spectrum / VU / EQ low-level band | `7.86:1` (AAA) |
| `yellow` | `#e0be66` | PCCB Racing Gold | Spectrum / VU / EQ mid-level band | `10.12:1` (AAA) |
| `red` | `#e56c6a` | Carmine Red | Spectrum / VU / EQ peak & redline clip | `5.77:1` (AA) |

## Install

1. Copy `911.toml` to `~/.config/cliamp/themes/911.toml`:

   ```bash
   mkdir -p ~/.config/cliamp/themes
   cp 911.toml ~/.config/cliamp/themes/911.toml
   ```

2. Activate the theme in `~/.config/cliamp/config.toml` (or run `cliamp theme 911`):

   ```toml
   theme = "911"
   visualizer = "Wave"
   ```

## Validate

```bash
python3 -c 'import re, tomllib; d=tomllib.load(open("911.toml","rb")); assert set(d)=={"bg","accent","bright_fg","fg","green","yellow","red"}; assert all(re.fullmatch(r"#[0-9a-fA-F]{6}", v) for v in d.values())'
cliamp theme list | grep -qx '  911'
```

## Disclaimer

Not affiliated with or endorsed by Porsche AG. Porsche and 911 are trademarks of Porsche AG.
