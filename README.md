# 911 (`992.2`) Precision Night Cockpit Themes

A standalone, shareable collection of **911 (`992.2`) Precision Night Cockpit** themes inspired by the Porsche 911 (992.2) cockpit on a night drive: Race-Tex Charcoal surfaces (`#141619`), crisp Ice Grey (`Crayon`) dial typography (`#dadad6`), Vanadium Grey elevated trim (`#1d2026`), brushed dark silver switchgear (`#b4b7be`), and a single disciplined spark of 911 Guards/Carmine Red (`#e55c5a`) for the lightbar, redline, and focus state.

Built from [`colors.toml`](colors.toml) (canonical source: [`omarchy-911-theme`](https://github.com/AryanHamedani/omarchy-911-theme), formerly Carrera), calibrated in OKLCH for long daily coding sessions: perceptually uniform syntax hues, glare-free contrast tuned to avoid halation, and WCAG AA conformance across every readable text and badge role.

## Palette & Contrast

Every readable text role — including comments (`#858a96` at `5.24:1` on canvas / `4.72:1` on elevated), Carmine Red accents (`#e55c5a` at `5.19:1` / `4.67:1`), and Truffle Club Leather (`#ad7f66` at `5.18:1` / `4.67:1`) — clears **WCAG AA (`>= 4.5:1`)** on both the Race-Tex Charcoal canvas (`#141619`) and Vanadium Grey elevated surface (`#1d2026`). Primary Ice Grey text sits at **`12.93:1`** for crisp, glare-free readability.

### Base Tokens (`colors.toml`)

| Token | Porsche / Role | Hex | RGB |
|---|---|---|---|
| `background` | Race-Tex Charcoal cockpit (primary canvas) | `#141619` | `20, 22, 25` |
| `dark_background` | Recessed carbon well, floats, sidebars | `#0f1114` | `15, 17, 20` |
| `darker_background` | Deep diffuser shadow, sunken wells | `#0a0b0d` | `10, 11, 13` |
| `lighter_background` | Vanadium Grey elevated surface, cursorline | `#1d2026` | `29, 32, 38` |
| `selection` / `selection_background` | Slate Grey Neo dash trim (selection bg) | `#292d36` | `41, 45, 54` |
| `foreground` | Ice Grey (`Crayon`, primary text, `12.93:1`) | `#dadad6` | `218, 218, 214` |
| `bright_foreground` / `selection_foreground` | Pure dial highlight (glare-free, `15.44:1`) | `#edede9` | `237, 237, 233` |
| `light_foreground` | Brushed dark silver switchgear | `#b4b7be` | `180, 183, 190` |
| `dark_foreground` | GT Silver in shadow | `#9297a2` | `146, 151, 162` |
| `muted` | Unlit gauge markings (comments, `5.24:1`) | `#858a96` | `133, 138, 150` |
| `accent` | 911 Guards/Carmine Red (lightbar, redline, focus, cursor) | `#e55c5a` | `229, 92, 90` |
| `red` | 911 Carmine Red (text-weight / ANSI 1) | `#e56c6a` | `229, 108, 106` |
| `orange` | Lava Orange | `#e89158` | `232, 145, 88` |
| `yellow` | PCCB Racing Gold / Satin Neodyme (ANSI 3) | `#e0be66` | `224, 190, 102` |
| `green` | Oak Green Metallic Neo (ANSI 2) | `#7fb887` | `127, 184, 135` |
| `cyan` | Ice Glacier Cyan (HD Matrix / digital cluster / ANSI 6) | `#6ac4cb` | `106, 196, 203` |
| `blue` | Lugano Blue (ANSI 4) | `#6fa2de` | `111, 162, 222` |
| `magenta` | Ultraviolet / PTS Amethyst (ANSI 5) | `#b488cc` | `180, 136, 204` |
| `brown` | Truffle Club Leather (decorators / PreProc) | `#ad7f66` | `173, 127, 102` |
| `bright_red` | Carmine Glow (ANSI 9) | `#f48583` | `244, 133, 131` |
| `bright_yellow` | Weissgold (ANSI 11) | `#f0d282` | `240, 210, 130` |
| `bright_green` | Oak Green Light (ANSI 10) | `#98ce9f` | `152, 206, 159` |
| `bright_cyan` | Glacier Light (ANSI 14) | `#84d8de` | `132, 216, 222` |
| `bright_blue` | Lugano Light (ANSI 12) | `#8cb9f2` | `140, 185, 242` |
| `bright_magenta` | Ultraviolet Light (ANSI 13) | `#caa2e0` | `202, 162, 224` |
| `hyprland_active_border` | Active border gradient (`135deg`, `cc` alpha) | `#e55c5a`, `#332024` | — |
| `hyprland_inactive_border` | Inactive border (`aa` alpha) | `#252932` | `37, 41, 50` |

### Approved Derived Cockpit Surfaces, Borders & Badges

| Token / Role | Hex | Notes |
|---|---|---|
| Deep carbon plane | `#0c0e11` | Recessed sidebars, deep wells (`13.79:1` w/ `#dadad6`) |
| Race-Tex chrome | `#131519` | Status bars, headers, toolbars (`13.04:1` w/ `#dadad6`) |
| Vanadium elevated | `#1a1d23` | Cards, panels, hover surfaces (`12.04:1` w/ `#dadad6`) |
| Smoked Carmine tint | `#261b1f` | Active selection/row tint (`11.90:1` w/ `#dadad6`) |
| Filled Guards Red badge + ink | `#bf3b3e` / `#f4f3ef` | High-emphasis badges & primary buttons (`4.84:1` AA) |
| Muted badge + ink | `#363b47` / `#f4f3ef` | Secondary badges & counters (`10.10:1` AAA) |
| Divider / box borders | `#252932`, `#2f3440`, `#434854` | Hairline (`hyprland`), divider (`btop`), box border (`btop`) |

See [`INVENTORY.md`](INVENTORY.md) for the complete palette derivation rules (translucent `#rrggbbaa`/`rgba(...)`, no-`#` hex formats, `[r, g, b]` arrays, and canonical opaque `alpha-over-#141619` diff/diagnostic/search stops).

## Application Index (36 Apps)

### Core Targets (`R1`, `R2`)
| App | Group | Target Files | Workstation Status | Guide |
|---|---|---|---|---|
| **Telegram Desktop** | R1 | `telegram/911.tdesktop-theme` | Standalone (617 keys + flyline bg, import via Telegram) | [telegram/README.md](telegram/README.md) |
| **Neovim** | R2 | `neovim/colors/911.lua` | Installed (`~/.config/nvim/colors/911.lua`; Omarchy `theme.lua` preserved) | [neovim/README.md](neovim/README.md) |

### Terminals, Multiplexers & Shells (10 Apps)
| App | Group | Target Files | Workstation Status | Guide |
|---|---|---|---|---|
| **Foot** | A2 | `foot/911.ini` | Omarchy active `911` include preserved | [foot/README.md](foot/README.md) |
| **Ghostty** | A2 | `ghostty/911` | Omarchy active `911` include preserved | [ghostty/README.md](ghostty/README.md) |
| **Alacritty** | A2 | `alacritty/911.toml` | Omarchy active `911` include preserved | [alacritty/README.md](alacritty/README.md) |
| **Kitty** | A2 | `kitty/911.conf` | Omarchy active `911` include preserved | [kitty/README.md](kitty/README.md) |
| **tmux** | A2 | `tmux/911.conf` | Applied live (`~/.config/tmux/911.conf` sourced in `tmux.conf`) | [tmux/README.md](tmux/README.md) |
| **Herdr** | A1 | `herdr/911.toml` | Applied live (`~/.config/herdr/config.toml`, live reloaded) | [herdr/README.md](herdr/README.md) |
| **Starship** | A1 | `starship/911.toml` | Applied live (`~/.config/starship.toml`) | [starship/README.md](starship/README.md) |
| **zsh-syntax-highlighting** | A1 | `zsh-syntax-highlighting/911.zsh` | Applied live (`~/.config/zsh/zsh-syntax-highlighting-911.zsh` in `~/.zshrc`) | [zsh-syntax-highlighting/README.md](zsh-syntax-highlighting/README.md) |
| **fzf** | A1 | `fzf/911.sh` | Applied live (`~/.config/zsh/fzf-911.sh` in `~/.zshrc`) | [fzf/README.md](fzf/README.md) |
| **Atuin** | A1 | `atuin/911.toml` | Applied live (`~/.atuin/themes/911.toml` + `config.toml`) | [atuin/README.md](atuin/README.md) |

### CLI & TUI Developer Tools (14 Apps)
| App | Group | Target Files | Workstation Status | Guide |
|---|---|---|---|---|
| **OpenCode** | A1 | `opencode/911.json` | Applied live (`~/.config/opencode/themes/911.json` + `opencode.json`) | [opencode/README.md](opencode/README.md) |
| **Claude Code** | A2 | `claude-code/911.json` | Omarchy active `911` theme preserved | [claude-code/README.md](claude-code/README.md) |
| **Pi Coding Agent** | A2 | `pi/911.json` | Omarchy active `911` theme preserved | [pi/README.md](pi/README.md) |
| **bat** | A1 | `bat/911.tmTheme` | Applied live (`~/.config/bat/themes/911.tmTheme` + cache built) | [bat/README.md](bat/README.md) |
| **Delta** | A1 | `delta/911.gitconfig` | Applied live (`~/.config/git/911-delta.gitconfig` in `~/.config/git/config`) | [delta/README.md](delta/README.md) |
| **Lazygit** | A1 | `lazygit/911.yml` | Applied live (`~/.config/lazygit/config.yml`) | [lazygit/README.md](lazygit/README.md) |
| **Lazydocker** | A1 | `lazydocker/911.yml` | Applied live (`~/.config/lazydocker/config.yml`) | [lazydocker/README.md](lazydocker/README.md) |
| **eza** | A1 | `eza/theme.yml` | Applied live (`~/.config/eza/theme.yml`) | [eza/README.md](eza/README.md) |
| **K9s** | A1 | `k9s/911.yaml` | Applied live (`~/.config/k9s/skins/911.yaml` + `config.yaml`) | [k9s/README.md](k9s/README.md) |
| **kubecolor** | A1 | `kubecolor/color.yaml` | Applied live (`~/.kube/color.yaml`) | [kubecolor/README.md](kubecolor/README.md) |
| **pgcli** | A1 | `pgcli/911.pgclirc` | Applied live (`~/.config/pgcli/config`) | [pgcli/README.md](pgcli/README.md) |
| **Cliamp** | A1 | `cliamp/911.toml` | Applied live (`~/.config/cliamp/themes/911.toml` + `config.toml`) | [cliamp/README.md](cliamp/README.md) |
| **Fastfetch** | A1 | `fastfetch/911.jsonc` | Applied live (`~/.config/fastfetch/config.jsonc`) | [fastfetch/README.md](fastfetch/README.md) |
| **btop** | B | `btop/911.theme` | Omarchy active `911` theme preserved (exact byte-for-byte match) | [btop/README.md](btop/README.md) |

### IDEs, Browsers, Desktop, WM & Toolkits (10 Apps)
| App | Group | Target Files | Workstation Status | Guide |
|---|---|---|---|---|
| **VS Code / Antigravity IDE** | A2 | `vscode/package.json`, `vscode/themes/911-color-theme.json` | Standalone extension | [vscode/README.md](vscode/README.md) |
| **Obsidian** | A2 | `obsidian/911/manifest.json`, `obsidian/911/theme.css` | Applied live (`Obsidian Vault/.obsidian/themes/911/` + `appearance.json`) | [obsidian/README.md](obsidian/README.md) |
| **Chromium** | A2 | `chromium/manifest.json`, `chromium/chromium.theme` | Omarchy active `911` theme preserved | [chromium/README.md](chromium/README.md) |
| **Zen Browser** | A1 | `zen-browser/userChrome.css`, `zen-browser/userContent.css` | Applied live (`~/.config/zen/<profile>/chrome/` + `user.js`) | [zen-browser/README.md](zen-browser/README.md) |
| **imv** | A1 | `imv/911.ini` | Applied live (`~/.config/imv/config`) | [imv/README.md](imv/README.md) |
| **mpv** | A1 | `mpv/mpv.conf` | Applied live (`~/.config/mpv/mpv.conf`) | [mpv/README.md](mpv/README.md) |
| **GTK 3 / GTK 4** | A1 | `gtk/gtk.css` | Standalone (`~/.config/gtk-3.0/` & `gtk-4.0/`) | [gtk/README.md](gtk/README.md) |
| **Fcitx5** | A2 | `fcitx5/911/theme.conf` | Omarchy active `911` theme preserved | [fcitx5/README.md](fcitx5/README.md) |
| **Hyprland** | A2 | `hyprland/911.conf` | Omarchy active `911` theme preserved | [hyprland/README.md](hyprland/README.md) |
| **Hyprland Preview Share Picker** | A2 | `hyprland-preview-share-picker/style.css` | Omarchy active `911` theme preserved | [hyprland-preview-share-picker/README.md](hyprland-preview-share-picker/README.md) |

## Workstation Safety & Backups

Every live workstation config modified during the 911 (`992.2`) rollout was backed up to `<file>.bak-911` prior to editing, and all Omarchy-managed `911` theme symlinks (`~/.local/state/omarchy/current/theme/`) were preserved untouched. Each subdirectory remains fully self-contained with its own `README.md` for standalone installation on any machine.

See [`INVENTORY.md`](INVENTORY.md) for the full palette derivation contract, workstation audit, validation commands, and exclusion rationale.

---

Not affiliated with or endorsed by Porsche AG. Porsche, 911 and Carrera are trademarks of Porsche AG.

Licensed under the [MIT License](LICENSE).
