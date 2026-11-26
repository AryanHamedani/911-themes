# 911 (`992.2`) Precision Night Cockpit — Workstation Software & Theme Inventory

## 1. Source Contract & Workstation Safety Guarantee

- **Authoritative Palette**: [`colors.toml`](colors.toml) — exact byte-for-byte copy of `/home/aryan/Work/personal/AryanHamedani/omarchy-911-theme/colors.toml` (SHA-256: `d4938495cdc44ad1f5f5ecce48dc1bf656b0666cf263134b47e913d4824fc187`).
- **License**: [`LICENSE`](LICENSE) — exact byte-for-byte copy of `/home/aryan/Work/personal/AryanHamedani/omarchy-911-theme/LICENSE` (MIT License, Copyright (c) 2026 Aryan Hamedani).
- **Workstation Rollout Safety**: No files inside `/home/aryan/Work/personal/AryanHamedani/omarchy-911-theme/` or `~/.local/state/omarchy/current/theme/` were modified. All Omarchy-managed app themes (`alacritty`, `foot`, `ghostty`, `kitty`, `btop`, `claude-code`, `pi`, `chromium`, `fcitx5`, `hyprland`, `hyprland-preview-share-picker`, `neovim/theme.lua`) were preserved untouched. Every existing user config updated for 911 was backed up to `<file>.bak-911` beforehand.

## 2. Palette Derivation Rules

All generated theme files derive colors strictly from [`colors.toml`](colors.toml) and the approved cockpit extensions below:

### 2.1 Base Palette Tokens (`colors.toml`)
- `mode = "dark"`
- Surfaces: `background = "#141619"`, `dark_background = "#0f1114"`, `darker_background = "#0a0b0d"`, `lighter_background = "#1d2026"`, `selection = "#292d36"`, `selection_background = "#292d36"`
- Foregrounds: `foreground = "#dadad6"` (`12.93:1`), `bright_foreground = "#edede9"` (`15.44:1`), `selection_foreground = "#edede9"`, `light_foreground = "#b4b7be"`, `dark_foreground = "#9297a2"`, `muted = "#858a96"` (`5.24:1` on bg / `4.72:1` on elev)
- Accent & Cursor: `accent = "#e55c5a"` (`5.19:1` on bg / `4.67:1` on elev)
- Hyprland Borders: `hyprland_active_border = "rgba(e55c5acc) rgba(332024cc) 135deg"`, `hyprland_inactive_border = "rgba(252932aa)"`
- Semantic / Normal ANSI 1–6 + Extras: `red = "#e56c6a"`, `orange = "#e89158"`, `yellow = "#e0be66"`, `green = "#7fb887"`, `cyan = "#6ac4cb"`, `blue = "#6fa2de"`, `magenta = "#b488cc"`, `brown = "#ad7f66"` (`5.18:1` on bg / `4.67:1` on elev)
- Bright ANSI 9–14: `bright_red = "#f48583"`, `bright_yellow = "#f0d282"`, `bright_green = "#98ce9f"`, `bright_cyan = "#84d8de"`, `bright_blue = "#8cb9f2"`, `bright_magenta = "#caa2e0"`

### 2.2 Format Encoding Rules
- **Standard hex**: `#rrggbb` (lowercase or case-insensitive `#RRGGBB` when required, e.g., Cliamp strict `^#[0-9a-fA-F]{6}$`).
- **Translucent overlays (`#rrggbbaa` / `#AARRGGBB` / `rgba(...)`)**: Exact 911 RGB combined with an explicit alpha channel (e.g., `#e55c5a33`, `#0a0b0d99`, `rgba(229, 92, 90, 0.2)`), used in `.tdesktop-theme`, CSS `rgba(...)`, VS Code `#rrggbbaa`, `mpv` `#AARRGGBB`, and Hyprland `rgba(rrggbbaa)`.
- **No-`#` 6-digit hex (`rrggbb`)**: Required by **Foot** (`[colors-dark]`, `[csd]`) and **imv** (`[options]`).
- **Decimal `[r, g, b]` arrays / CSV**: Required by **Chromium** (`manifest.json` `theme.colors` and `chromium.theme`), e.g., `[20, 22, 25]` / `20,22,25` for `#141619`.

### 2.3 Approved Derived Cockpit Surfaces, Borders & Badges
Calibrated in OKLCH to preserve the 4-plane Race-Tex / Vanadium cockpit hierarchy and WCAG AA contrast (`>= 4.5:1`) on filled badges:

| Hex | Role | Derivation / Provenance |
|---|---|---|
| `#0c0e11` | Deep carbon plane | Recessed sidebar/panel plane (`13.79:1` w/ `#dadad6`) |
| `#131519` | Race-Tex chrome | Status bar, header, toolbar plane (`13.04:1` w/ `#dadad6`) |
| `#1a1d23` | Vanadium elevated | Cards, menus, subtle raised surfaces (`12.04:1` w/ `#dadad6`) |
| `#261b1f` | Smoked Carmine tint | Active row/selection tint (`11.90:1` w/ `#dadad6`) |
| `#bf3b3e` | Filled Guards Red badge / button | High-emphasis badge & button fill (`4.84:1` AA w/ `#f4f3ef`) |
| `#f4f3ef` | Badge ink | Crisp warm-neutral ink on filled badges (`4.84:1` on `#bf3b3e`, `10.10:1` on `#363b47`) |
| `#363b47` | Muted badge fill | Secondary counter/tag fill (`10.10:1` w/ `#f4f3ef`) |
| `#252932` | Inactive border / hairline | Verbatim `colors.toml` `hyprland_inactive_border` RGB |
| `#332024` | Active Carmine border stop 2 | Verbatim `colors.toml` `hyprland_active_border` stop 2 RGB |
| `#2f3440` | Divider / hairline border | Verbatim `omarchy-911-theme/btop.theme` (`div_line`) |
| `#434854` | Box border / subtle rule | Verbatim `omarchy-911-theme/btop.theme` (`cpu_box`..`proc_box`) |

### 2.4 Canonical Opaque `alpha-over-#141619` Tints (Diff / Diagnostics / Search)
When an application requires opaque tinted surfaces (diffs, diagnostic virtual-text backgrounds, search highlights) without `#rrggbbaa`, use only this calibrated set blended over `#141619` (`(20, 22, 25)`):

| Hex | Role | Derivation |
|---|---|---|
| `#202825` | Diff add background | Exact 11% `#7fb887` over `#141619` (`10.76:1` w/ `#dadad6`) |
| `#2d2023` | Diff delete background | Exact 12% `#e56c6a` over `#141619` (`11.16:1` w/ `#dadad6`) |
| `#1f2731` | Diff change background | Exact 12% `#6fa2de` over `#141619` (`10.76:1` w/ `#dadad6`) |
| `#293646` | Diff text highlight background | Exact 23% `#6fa2de` over `#141619` (`8.76:1` w/ `#dadad6`) |
| `#2a2124` | Diagnostic error virtual-text bg | Exact 10% `#f48583` over `#141619` |
| `#282721` | Diagnostic warn virtual-text bg | Exact 10% `#e0be66` over `#141619` |
| `#1d242d` | Diagnostic info virtual-text bg | Exact 10% `#6fa2de` over `#141619` |
| `#1d272b` | Diagnostic hint virtual-text bg | Exact 10% `#6ac4cb` over `#141619` |
| `#1f2624` | Diagnostic ok virtual-text bg | Exact 10% `#7fb887` over `#141619` |
| `#5b5134` | Search highlight background | Exact 35% `#e0be66` over `#141619` (`6.70:1` w/ `#edede9`) |

### 2.5 `cursor` Color Policy (`#e55c5a` vs `#edede9`)
- `omarchy-911-theme/colors.toml` defines `accent = "#e55c5a"` without a separate `cursor` key.
- Omarchy's runtime helper `/usr/bin/omarchy-theme-color` maps `cursor` to `bright_foreground` (`#edede9`) when rendering Omarchy templates.
- **Standalone policy**: Standalone 911 themes in this repository use `cursor = "#e55c5a"` (Guards/Carmine Red needle) with `#0a0b0d` or `#141619` cursor-text, while noting Omarchy's `#edede9` runtime override where applicable.

---

## 3. Target Applications Inventory (36 Apps: 1 R1 + 1 R2 + 20 A1 + 13 A2 + 1 B)

| # | Group | Application | Target File Path(s) | Applied Workstation Path / Status | Isolated Validation Method | Status |
|---|---|---|---|---|---|---|
| 1 | R1 | **Telegram Desktop** | `telegram/911.tdesktop-theme`, `telegram/README.md` | Standalone (617 keys, 4-plane depth, flyline `background.jpg`; manual import) | ZIP/PNG check + 617-key palette parser + 18 WCAG checks | Complete (911) |
| 2 | R2 | **Neovim** | `neovim/colors/911.lua`, `neovim/README.md` | Installed: `~/.config/nvim/colors/911.lua` (Omarchy `theme.lua` preserved) | `nvim --headless -c 'colorscheme 911'` + `lualine.themes.911` check | Complete (911) |
| 3 | A1 | **OpenCode** | `opencode/911.json`, `opencode/README.md` | Applied: `~/.config/opencode/themes/911.json` + `opencode.json` (`.bak-911`) | `json.load` + OpenCode TUI schema check | Complete (911) |
| 4 | A1 | **Cliamp** | `cliamp/911.toml`, `cliamp/README.md` | Applied: `~/.config/cliamp/themes/911.toml` + `config.toml` (`.bak-911`) | `tomllib.load` + `cliamp theme list` (`911`) | Complete (911) |
| 5 | A1 | **Starship** | `starship/911.toml`, `starship/README.md` | Applied: `~/.config/starship.toml` (`.bak-911`) | `STARSHIP_CONFIG=<file> starship print-config` | Complete (911) |
| 6 | A1 | **K9s** | `k9s/911.yaml`, `k9s/README.md` | Applied: `~/.config/k9s/skins/911.yaml` + `config.yaml` (`.bak-911`) | `yaml.safe_load` + K9s skin structure check | Complete (911) |
| 7 | A1 | **bat** | `bat/911.tmTheme`, `bat/README.md` | Applied: `~/.config/bat/themes/911.tmTheme` + `config` (`.bak-911`) + `bat cache --build` | `xml.etree.ElementTree` + `bat --list-themes` & render | Complete (911) |
| 8 | A1 | **Delta** | `delta/911.gitconfig`, `delta/README.md` | Applied: `~/.config/git/911-delta.gitconfig` + `~/.config/git/config` (`.bak-911`) | `git config --file <file> --list` + `delta` render | Complete (911) |
| 9 | A1 | **Lazygit** | `lazygit/911.yml`, `lazygit/README.md` | Applied: `~/.config/lazygit/config.yml` (`.bak-911`) | `yaml.safe_load` + `gui.theme` (15 keys) check | Complete (911) |
| 10 | A1 | **Lazydocker** | `lazydocker/911.yml`, `lazydocker/README.md` | Applied: `~/.config/lazydocker/config.yml` (`.bak-911`) | `yaml.safe_load` + `gui.theme` check | Complete (911) |
| 11 | A1 | **Herdr** | `herdr/911.toml`, `herdr/README.md` | Applied: `~/.config/herdr/config.toml` (`.bak-911`, live reloaded) | `tomllib.load` + `herdr config check` | Complete (911) |
| 12 | A1 | **fzf** | `fzf/911.sh`, `fzf/README.md` | Applied: `~/.config/zsh/fzf-911.sh` sourced in `~/.zshrc` (`.bak-911`) | `zsh -n` / `bash -n` + `fzf --filter=alpha` | Complete (911) |
| 13 | A1 | **eza** | `eza/theme.yml`, `eza/README.md` | Applied: `~/.config/eza/theme.yml` | `yaml.safe_load` + `eza -la --git --color=always` | Complete (911) |
| 14 | A1 | **kubecolor** | `kubecolor/color.yaml`, `kubecolor/README.md` | Applied: `~/.kube/color.yaml` | `yaml.safe_load` + `KUBECOLOR_CONFIG=<file> kubecolor` | Complete (911) |
| 15 | A1 | **Atuin** | `atuin/911.toml`, `atuin/README.md` | Applied: `~/.atuin/themes/911.toml` + `~/.atuin/config.toml` (`.bak-911`) | `tomllib.load` + 15 PascalCase `[colors]` keys check | Complete (911) |
| 16 | A1 | **Zen Browser** | `zen-browser/userChrome.css`, `zen-browser/userContent.css`, `zen-browser/README.md` | Applied: `~/.config/zen/i64rv1pg.Default (release)/chrome/` + `user.js` | CSS balanced-brace & token/hex validation | Complete (911) |
| 17 | A1 | **imv** | `imv/911.ini`, `imv/README.md` | Applied: `~/.config/imv/config` (`.bak-911`, `[binds]` preserved) | `configparser` + 6-digit no-`#` hex check | Complete (911) |
| 18 | A1 | **mpv** | `mpv/mpv.conf`, `mpv/README.md` | Applied: `~/.config/mpv/mpv.conf` | `mpv --no-config --include=<file> --idle=no --no-terminal` | Complete (911) |
| 19 | A1 | **zsh-syntax-highlighting** | `zsh-syntax-highlighting/911.zsh`, `zsh-syntax-highlighting/README.md` | Applied: `~/.config/zsh/zsh-syntax-highlighting-911.zsh` in `~/.zshrc` (`.bak-911`) | `zsh -n`, `zsh -fc`, `zsh -ic 'exit 0'` | Complete (911) |
| 20 | A1 | **GTK 3 / GTK 4** | `gtk/gtk.css`, `gtk/README.md` | Standalone (`~/.config/gtk-3.0/gtk.css` & `gtk-4.0/gtk.css`) | CSS syntax & `@define-color` hex validation | Complete (911) |
| 21 | A1 | **pgcli** | `pgcli/911.pgclirc`, `pgcli/README.md` | Applied: `~/.config/pgcli/config` | `ConfigObj` + `pgcli` `style_factory` (62 styles) | Complete (911) |
| 22 | A1 | **Fastfetch** | `fastfetch/911.jsonc`, `fastfetch/README.md` | Applied: `~/.config/fastfetch/config.jsonc` | Comment-stripped `json.loads` + `fastfetch` render | Complete (911) |
| 23 | A2 | **Foot** | `foot/911.ini`, `foot/README.md` | Omarchy active `911` include preserved | `foot -c <file> --check-config` (`[colors-dark]` + `[csd]`) | Complete (911) |
| 24 | A2 | **Ghostty** | `ghostty/911`, `ghostty/README.md` | Omarchy active `911` include preserved | `ghostty +validate-config --config-file=<file>` | Complete (911) |
| 25 | A2 | **Alacritty** | `alacritty/911.toml`, `alacritty/README.md` | Omarchy active `911` include preserved | `tomllib.load` + `[colors.*]` / `[bell]` check | Complete (911) |
| 26 | A2 | **Kitty** | `kitty/911.conf`, `kitty/README.md` | Omarchy active `911` include preserved | Line-oriented key `#rrggbb` parser & key check | Complete (911) |
| 27 | A2 | **tmux** | `tmux/911.conf`, `tmux/README.md` | Applied: `~/.config/tmux/911.conf` sourced in `~/.config/tmux/tmux.conf` (`.bak-911`) | Isolated `tmux -L 911-val -f <file>` load check | Complete (911) |
| 28 | A2 | **Fcitx5** | `fcitx5/911/theme.conf`, `fcitx5/README.md` | Omarchy active `911` theme preserved | `configparser` + `[Metadata]`/`[InputPanel*]`/`[Menu*]` check | Complete (911) |
| 29 | A2 | **Obsidian** | `obsidian/911/manifest.json`, `obsidian/911/theme.css`, `obsidian/README.md` | Applied: `~/Documents/Obsidian Vault/.obsidian/themes/911/` + `appearance.json` (`.bak-911`) | `json.load` on `manifest.json` + CSS syntax check on `theme.css` | Complete (911) |
| 30 | A2 | **Claude Code** | `claude-code/911.json`, `claude-code/README.md` | Omarchy active `911` theme preserved | `json.load` + 37 `overrides` key check | Complete (911) |
| 31 | A2 | **Pi Coding Agent** | `pi/911.json`, `pi/README.md` | Omarchy active `911` theme preserved | `json.load` + `vars`/`colors`/`export` ref check | Complete (911) |
| 32 | A2 | **VS Code / Antigravity IDE** | `vscode/package.json`, `vscode/themes/911-color-theme.json`, `vscode/README.md` | Standalone extension (670 workbench colors, 36 semantic tokens, 81 TextMate scopes) | `json.load` on both files + theme schema check | Complete (911) |
| 33 | A2 | **Chromium** | `chromium/manifest.json`, `chromium/chromium.theme`, `chromium/README.md` | Omarchy active `911` theme preserved | `json.load` + `[r, g, b]` 0–255 integer range check | Complete (911) |
| 34 | A2 | **Hyprland** | `hyprland/911.conf`, `hyprland/README.md` | Omarchy active `911` theme preserved | `hyprctl configerrors` empty + syntax check | Complete (911) |
| 35 | A2 | **Hyprland Preview Share Picker** | `hyprland-preview-share-picker/style.css`, `hyprland-preview-share-picker/README.md` | Omarchy active `911` theme preserved | CSS syntax & token/hex validation | Complete (911) |
| 36 | B | **btop** | `btop/911.theme`, `btop/README.md` | Omarchy active `911` theme preserved (exact byte-for-byte match) | 50-key `theme[key]="#rrggbb"` + `gradient_color_0..7` check | Complete (911) |

*Note: All 36 target application themes, root palette contract & documentation (`colors.toml`, `README.md`, `INVENTORY.md`), and the E2E validation suite (`tests/`) are aligned to **911 (`992.2`) Precision Night Cockpit**.*

---

## 4. Group C — Inspected & Excluded / Not Installed

### 4.1 Inspected & Excluded (12 Entries)
Installed or present on the workstation, verified via binary/package/config inspection to lack standalone file-based custom hex theming:

| # | Application / Category | Technical Reason for Exclusion |
|---|---|---|
| 1 | **Harlequin** (`2.17.0` via mise) | `harlequin/colors.py` validates `--theme` strictly against `BUILTIN_THEMES` + `"harlequin"`; no config-file hex theme loader. |
| 2 | **iredis** (`1.16.1` via mise) | `iredis/style.py` hardcodes prompt_toolkit `STYLE`; `iredisrc` has no `[colors]` section. |
| 3 | **Codex CLI** (`~/.codex/config.toml`) | No standalone custom hex theme file mechanism supported. |
| 4 | **Discord** (Electron) | Vanilla Electron binary without CSS injector modifications. |
| 5 | **Element** (Electron) | Vanilla Electron binary without CSS injector modifications. |
| 6 | **Mattermost** (Electron) | Vanilla Electron binary without CSS injector modifications. |
| 7 | **Bruno** (Electron) | Vanilla Electron binary without CSS injector modifications. |
| 8 | **1Password** (Electron) | Vanilla Electron binary without CSS injector modifications. |
| 9 | **LM Studio** (Electron) | Vanilla Electron binary without CSS injector modifications. |
| 10 | **DBeaver** | Uses Eclipse SWT/UI preferences rather than standalone portable hex theme files. |
| 11 | **Xournal++** (`~/.config/xournalpp/settings.xml`) | Only supports `themeVariant=forceDark` via GTK theme; no custom hex theme file. |
| 12 | **Omarchy Qt / Built-in Apps** (`monologue`, `hype`, `omacalc`, `omacut`, `omasnap`, `omawrite`) | Automatically follow the active Omarchy/Qt system palette (no separate standalone theme files). |

*(Additionally, `aether.nvim` is an upstream Neovim theme plugin dependency rather than a standalone target app.)*

### 4.2 Not Installed on Workstation (17 Entries)
Checked via `command -v` and `pacman -Q`; none are installed:

1. `helix`
2. `hermes`
3. `t3code`
4. `zed`
5. `zellij`
6. `waybar`
7. `mako`
8. `swaync`
9. `walker`
10. `fuzzel`
11. `rofi`
12. `wofi`
13. `yazi`
14. `zathura`
15. `difftastic`
16. `kvantum`
17. `qt6ct`
