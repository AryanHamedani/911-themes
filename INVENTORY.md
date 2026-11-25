# Carrera v2.0.0 — Workstation Software & Theme Inventory

## 1. Source Contract & R4 Isolation Guarantee

- **Authoritative Palette**: [`colors.toml`](colors.toml) — exact byte-for-byte copy of `/home/aryan/Work/personal/AryanHamedani/omarchy-carrera-theme/colors.toml` (SHA-256: `0787d5a2381a649ab857c2c9634a470bd59dc9ac275cec0ad61b98ff29745f7a`).
- **License**: [`LICENSE`](LICENSE) — exact byte-for-byte copy of `/home/aryan/Work/personal/AryanHamedani/omarchy-carrera-theme/LICENSE` (MIT License, Copyright (c) 2026 Aryan Hamedani).
- **R4 Generate-Only Isolation**: No files inside `/home/aryan/Work/personal/AryanHamedani/omarchy-carrera-theme/` and no existing active user configs under `~/.config/`, `~/.claude/`, `~/.pi/`, `~/.codex/`, `~/.local/`, or `~/.zshrc` are modified or activated. Neovim's standalone colorscheme is placed at `~/.config/nvim/colors/carrera.lua` without changing the active startup colorscheme (`aether`).

## 2. Palette Derivation Rules

All generated theme files derive colors strictly from [`colors.toml`](colors.toml) according to these canonical rules:

### 2.1 Base Palette Tokens (`colors.toml`)
- `mode = "dark"`
- Surfaces: `background = "#15171a"`, `dark_background = "#101215"`, `darker_background = "#0b0c0e"`, `lighter_background = "#1e2025"`, `selection = "#2b2e35"`, `selection_background = "#2b2e35"`
- Foregrounds: `foreground = "#d6d2c7"`, `bright_foreground = "#eae6dc"`, `selection_foreground = "#eae6dc"`, `light_foreground = "#b3afa6"`, `dark_foreground = "#9599a2"`, `muted = "#838792"`
- Accent & Cursor: `accent = "#e1656c"`, `cursor = "#e1656c"`
- Hyprland Borders: `hyprland_active_border = "rgba(e1656ccc) rgba(3a2429cc) 135deg"`, `hyprland_inactive_border = "rgba(262930aa)"`
- Semantic / Normal ANSI 1–6 + Extras: `red = "#e07476"`, `orange = "#e8965a"`, `yellow = "#dcbb6a"`, `green = "#89b87f"`, `cyan = "#6fc7cb"`, `blue = "#74a0d7"`, `magenta = "#b886b8"`, `brown = "#ae7e62"`
- Bright ANSI 9–14: `bright_red = "#f28a8b"`, `bright_yellow = "#edcf86"`, `bright_green = "#a1ce97"`, `bright_cyan = "#87d9dd"`, `bright_blue = "#8eb9f0"`, `bright_magenta = "#d09fd1"`

### 2.2 Format Encoding Rules
- **Standard hex**: `#rrggbb` (lowercase or case-insensitive `#RRGGBB` when required, e.g., Cliamp strict `^#[0-9a-fA-F]{6}$`).
- **Translucent overlays (`#rrggbbaa` / `rgba(...)`)**: Exact `colors.toml` RGB combined with an explicit alpha channel (e.g., `#e1656c33`, `#0b0c0e99`, `rgba(225, 101, 108, 0.2)`), used in `.tdesktop-theme`, CSS `rgba(...)`, VS Code `#rrggbbaa`, and Hyprland `rgba(rrggbbaa)`.
- **No-`#` 6-digit hex (`rrggbb`)**: Required by **Foot** (`[colors-dark]`) and **imv** (`[options]`).
- **Decimal `[r, g, b]` arrays**: Required by **Chromium** (`manifest.json` `theme.colors` and `chromium.theme`), e.g., `[21, 23, 26]` for `#15171a`.

### 2.3 Canonical Opaque `alpha-over-#15171a` Surface Stops
When an application requires opaque tinted surfaces (borders, diffs, diagnostic virtual-text backgrounds, search highlights) and does not support `#rrggbbaa`, use only this minimal calibrated set derived over `#15171a` (`(21, 23, 26)`):

| Hex | Role | Derivation / Provenance |
|---|---|---|
| `#31353f` | Divider / hairline border | Verbatim `omarchy-carrera-theme/btop.theme` (`div_line`) |
| `#454954` | Box border / subtle rule | Verbatim `omarchy-carrera-theme/btop.theme` (`cpu_box`..`proc_box`) |
| `#262930` | Inactive border / hairline | Verbatim `colors.toml` `hyprland_inactive_border` RGB (~16% `#838792` over `#15171a`) |
| `#3a2429` | Carmine border/selection tint | Verbatim `colors.toml` `hyprland_active_border` stop 2 RGB (~18% `#e1656c` over `#15171a`) |
| `#222a23` | Diff add background | Canonical opaque green tint (~11% `#89b87f` over `#15171a`) |
| `#2d1e20` | Diff delete background | Canonical opaque red tint (~12% `#e07476`/`#e1656c` over `#15171a`) |
| `#202731` | Diff change background | Exact 12% `#74a0d7` over `#15171a` |
| `#2b3646` | Diff text highlight background | ~23% `#74a0d7` over `#15171a` |
| `#2b2225` | Diagnostic error virtual-text bg | Exact 10% `#f28a8b` over `#15171a` |
| `#292722` | Diagnostic warn virtual-text bg | Exact 10% `#dcbb6a` over `#15171a` |
| `#1e252d` | Diagnostic info virtual-text bg | Exact 10% `#74a0d7` over `#15171a` |
| `#1e292c` | Diagnostic hint virtual-text bg | Exact 10% `#6fc7cb` over `#15171a` |
| `#212724` | Diagnostic ok virtual-text bg | Exact 10% `#89b87f` over `#15171a` |
| `#5b5036` | Search highlight background | Exact 35% `#dcbb6a` over `#15171a` |

### 2.4 `cursor` Color Choice (`#e1656c` vs `#eae6dc`)
- `colors.toml` line 8 defines `cursor = "#e1656c"` (Carmine Red rev needle).
- Omarchy's runtime helper `/usr/bin/omarchy-theme-color` (line 219) overrides `THEME_COLORS[cursor]` with `bright_foreground` (`#eae6dc`) when rendering Omarchy templates.
- **Standalone policy**: Standalone Carrera themes in this repository use `cursor = "#e1656c"` per `colors.toml` (Carmine Red needle), while noting the `#eae6dc` Omarchy runtime override in relevant documentation where applicable.

---

## 3. Target Applications Inventory (36 Apps: 1 R1 + 1 R2 + 20 A1 + 13 A2 + 1 B)

| # | Group | Application | Target File Path(s) | Recommended User Install Path | Isolated Validation Method | Milestone | Status |
|---|---|---|---|---|---|---|---|
| 1 | R1 | **Telegram Desktop** | `telegram/carrera.tdesktop-theme`, `telegram/README.md` | Import `carrera.tdesktop-theme` via Telegram Settings → Chat Settings → Theme | Python ZIP/PNG check + 606-key `colors.palette`/`night.tdesktop-theme` parser & dependency order check | M1 | Complete (M1) |
| 2 | R2 | **Neovim** | `neovim/colors/carrera.lua`, `/home/aryan/.config/nvim/colors/carrera.lua`, `neovim/README.md` | `~/.config/nvim/colors/carrera.lua` (`:colorscheme carrera`) | `cmp -s`, `stylua --check`, `nvim --headless -c 'colorscheme carrera'`, default startup still `aether` | M1 | Complete (M1) |
| 3 | A1 | **OpenCode** | `opencode/carrera.json`, `opencode/README.md` | `~/.config/opencode/themes/carrera.json` | `jq empty` / `json.load` + OpenCode TUI schema keys check | M3 | Complete (M3) |
| 4 | A1 | **Cliamp** | `cliamp/carrera.toml`, `cliamp/README.md` | `~/.config/cliamp/themes/carrera.toml` | `tomllib.load` + strict `^#[0-9a-fA-F]{6}$` and required keys check | M3 | Complete (M3) |
| 5 | A1 | **Starship** | `starship/carrera.toml`, `starship/README.md` | `~/.config/starship.toml` (`[palettes.carrera]`) | `STARSHIP_CONFIG=<file> starship print-config` | M2 | Complete (M2) |
| 6 | A1 | **K9s** | `k9s/carrera.yaml`, `k9s/README.md` | `~/.config/k9s/skins/carrera.yaml` | `yaml.safe_load` + K9s skin structure check | M3 | Complete (M3) |
| 7 | A1 | **bat** | `bat/Carrera.tmTheme`, `bat/README.md` | `$(bat --config-dir)/themes/Carrera.tmTheme` | `xml.etree.ElementTree` + isolated `XDG_CONFIG_HOME`/`XDG_CACHE_HOME` `bat cache --build` | M3 | Complete (M3) |
| 8 | A1 | **Delta** | `delta/carrera.gitconfig`, `delta/README.md` | `~/.config/git/carrera.gitconfig` (`[include]`) | `git config --file <file> --list` | M3 | Complete (M3) |
| 9 | A1 | **Lazygit** | `lazygit/carrera.yml`, `lazygit/README.md` | `~/.config/lazygit/config.yml` (`gui.theme`) | `yaml.safe_load` + `gui.theme` key check | M3 | Complete (M3) |
| 10 | A1 | **Lazydocker** | `lazydocker/carrera.yml`, `lazydocker/README.md` | `~/.config/lazydocker/config.yml` (`gui.theme`) | `yaml.safe_load` + `gui.theme` key check | M3 | Complete (M3) |
| 11 | A1 | **Herdr** | `herdr/carrera.toml`, `herdr/README.md` | `~/.config/herdr/config.toml` (`[theme.custom]`) | `tomllib.load` + `[theme.custom]` hex check | M2 | Complete (M2) |
| 12 | A1 | **fzf** | `fzf/carrera.sh`, `fzf/README.md` | Source in `~/.zshrc` (`FZF_DEFAULT_OPTS`) | `zsh -n` / `bash -n` + isolated `fzf --filter=""` option check | M2 | Complete (M2) |
| 13 | A1 | **eza** | `eza/theme.yml`, `eza/README.md` | `~/.config/eza/theme.yml` (`$EZA_CONFIG_DIR`) | `yaml.safe_load` + `EZA_CONFIG_DIR=<dir> eza --color=always` | M3 | Complete (M3) |
| 14 | A1 | **kubecolor** | `kubecolor/color.yaml`, `kubecolor/README.md` | `~/.kube/color.yaml` | `yaml.safe_load` + `KUBECOLOR_CONFIG=<file> kubecolor` parse check | M3 | Complete (M3) |
| 15 | A1 | **Atuin** | `atuin/carrera.toml`, `atuin/README.md` | `~/.config/atuin/themes/carrera.toml` | `tomllib.load` + Atuin theme key check | M2 | Complete (M2) |
| 16 | A1 | **Zen Browser** | `zen-browser/userChrome.css`, `zen-browser/userContent.css`, `zen-browser/README.md` | `~/.config/zen/<profile>/chrome/` | CSS balanced-brace & variable/hex validation | M4 | Complete (M4) |
| 17 | A1 | **imv** | `imv/carrera.ini`, `imv/README.md` | `~/.config/imv/config` (`[options]`) | `configparser` + 6-digit hex without `#` regex | M4 | Complete (M4) |
| 18 | A1 | **mpv** | `mpv/mpv.conf`, `mpv/README.md` | `~/.config/mpv/carrera.conf` (`include=~~/carrera.conf` in `~/.config/mpv/mpv.conf`) | `mpv --no-config --include=<file> --idle=no --vo=null --ao=null` | M4 | Complete (M4) |
| 19 | A1 | **zsh-syntax-highlighting** | `zsh-syntax-highlighting/carrera.zsh`, `zsh-syntax-highlighting/README.md` | Source in `~/.zshrc` | `zsh -n <file>` + subshell `zsh -fc 'source ...'` | M2 | Complete (M2) |
| 20 | A1 | **GTK 3 / GTK 4** | `gtk/gtk.css`, `gtk/README.md` | `~/.config/gtk-3.0/gtk.css` & `~/.config/gtk-4.0/gtk.css` | CSS syntax & `@define-color` hex validation | M4 | Complete (M4) |
| 21 | A1 | **pgcli** | `pgcli/carrera.pgclirc`, `pgcli/README.md` | `~/.config/pgcli/config` (`[colors]`) | `configparser` + prompt_toolkit `#rrggbb` syntax check | M3 | Complete (M3) |
| 22 | A1 | **Fastfetch** | `fastfetch/carrera.jsonc`, `fastfetch/README.md` | `~/.config/fastfetch/carrera.jsonc` (or merge into `~/.config/fastfetch/config.jsonc`) | Comment-stripped `json.loads` + `fastfetch --config <file> --structure Title` | M3 | Complete (M3) |
| 23 | A2 | **Foot** | `foot/carrera.ini`, `foot/README.md` | `~/.config/foot/themes/carrera.ini` (`include=...`) | `foot -c <file> --check-config` (`[colors-dark]`, no `#`) | M2 | Complete (M2) |
| 24 | A2 | **Ghostty** | `ghostty/carrera`, `ghostty/README.md` | `~/.config/ghostty/themes/carrera` | `ghostty +validate-config --config-file=<file>` | M2 | Complete (M2) |
| 25 | A2 | **Alacritty** | `alacritty/carrera.toml`, `alacritty/README.md` | `~/.config/alacritty/themes/carrera.toml` (`general.import`) | `tomllib.load` + Alacritty `[colors.*]` hex check | M2 | Complete (M2) |
| 26 | A2 | **Kitty** | `kitty/carrera.conf`, `kitty/README.md` | `~/.config/kitty/themes/carrera.conf` (`include`) | Line-oriented key `#rrggbb` parser & key check | M2 | Complete (M2) |
| 27 | A2 | **tmux** | `tmux/carrera.conf`, `tmux/README.md` | `~/.config/tmux/themes/carrera.conf` (`source-file`) | Isolated `tmux -L carrera-val -f <file> new-session -d -s val true \; kill-server` | M2 | Complete (M2) |
| 28 | A2 | **Fcitx5** | `fcitx5/carrera/theme.conf`, `fcitx5/README.md` | `~/.local/share/fcitx5/themes/carrera/theme.conf` | `configparser` + `[Metadata]`/`[InputPanel]`/`[Menu]` check | M4 | Complete (M4) |
| 29 | A2 | **Obsidian** | `obsidian/Carrera/manifest.json`, `obsidian/Carrera/theme.css`, `obsidian/README.md` | `<Vault>/.obsidian/themes/Carrera/` | `json.load` on `manifest.json` + CSS syntax check on `theme.css` | M4 | Complete (M4) |
| 30 | A2 | **Claude Code** | `claude-code/carrera.json`, `claude-code/README.md` | `~/.claude/themes/carrera.json` | `json.load` + key completeness vs `claude.json.tpl` | M3 | Complete (M3) |
| 31 | A2 | **Pi Coding Agent** | `pi/carrera.json`, `pi/README.md` | `~/.pi/agent/themes/carrera.json` | `json.load` + `vars`/`colors`/`export` ref check | M3 | Complete (M3) |
| 32 | A2 | **VS Code / Antigravity IDE** | `vscode/package.json`, `vscode/themes/carrera-color-theme.json`, `vscode/README.md` | `~/.vscode/extensions/` or `~/.antigravity-ide/extensions/` | `json.load` on both files + theme schema check | M4 | Complete (M4) |
| 33 | A2 | **Chromium** | `chromium/manifest.json`, `chromium/chromium.theme`, `chromium/README.md` | Load unpacked extension in `chrome://extensions` | `json.load` + `[r, g, b]` 0–255 integer range check | M4 | Complete (M4) |
| 34 | A2 | **Hyprland** | `hyprland/carrera.conf`, `hyprland/README.md` | `~/.config/hypr/carrera.conf` (`source = ...`) | Hyprland `rgba(rrggbbaa)` & config syntax check | M4 | Complete (M4) |
| 35 | A2 | **Hyprland Preview Share Picker** | `hyprland-preview-share-picker/style.css`, `hyprland-preview-share-picker/README.md` | `~/.config/hyprland-preview-share-picker/style.css` | CSS syntax & `@define-color` hex validation | M4 | Complete (M4) |
| 36 | B | **btop** | `btop/carrera.theme`, `btop/README.md` | `~/.config/btop/themes/carrera.theme` | Line regex `^theme\[[a-z_]+\]="#[0-9a-fA-F]{6}"$` (42 keys) | M3 | Complete (M3) |

*Note: Repo Foundation (`LICENSE`, `colors.toml`, `README.md`, `INVENTORY.md`), all 36 target application themes (M1–M4), and the E2E validation suite (`tests/`, Tiers 1–4) are Complete.*

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
