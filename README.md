# Carrera Themes (`v2.0.0`)

A standalone, shareable collection of **Carrera v2.0.0 ("Heritage Cockpit")** themes inspired by the Porsche 911 Heritage Cockpit on a night drive: Basalt Alcantara surfaces (`#15171a`), warm Chalk (`Kreide`) dial numerals (`#d6d2c7`), brushed GT Silver trim (`#9599a2`), and a single disciplined spark of Carmine Red (`#e1656c`) for the rev needle and smoked tail-light horizon.

Built from [`colors.toml`](colors.toml) (canonical source: [`omarchy-carrera-theme`](https://github.com/AryanHamedani/omarchy-carrera-theme)), calibrated in OKLCH for long daily coding sessions: perceptually balanced syntax hues, glare-free contrast tuned to the APCA ergonomic band, and restrained chroma that eliminates red/blue chromostereopsis.

> **Non-Activating Distribution (Generate-Only)**: Every application directory in this repository is self-contained and non-activating. Nothing modifies or switches your live desktop, shell, editor, or application settings automatically; follow each `<app>/README.md` to preview or install a theme manually.

## Palette & Contrast

Every readable text role — including comments (`#838792`) and Carmine Red accents (`#e1656c`) — meets at least **WCAG AA (`>= 4.5:1`)** on the Basalt canvas (`#15171a`) and cursorline (`#1e2025`), with primary Chalk text sitting at **`11.9:1` (`APCA Lc -78`)** to avoid halation.

| Token | Porsche / Role | Hex | RGB |
|---|---|---|---|
| `background` | Basalt Alcantara (primary canvas) | `#15171a` | `21, 23, 26` |
| `dark_background` | Recessed instrument well, floats, sidebars | `#101215` | `16, 18, 21` |
| `darker_background` | Deep shadow, borders | `#0b0c0e` | `11, 12, 14` |
| `lighter_background` | Elevated surface, cursorline, panels | `#1e2025` | `30, 32, 37` |
| `selection` / `selection_background` | Machined dash trim (selection bg) | `#2b2e35` | `43, 46, 53` |
| `foreground` | Chalk (`Kreide`, primary text) | `#d6d2c7` | `214, 210, 199` |
| `bright_foreground` / `selection_foreground` | Chalk highlight (glare-free) | `#eae6dc` | `234, 230, 220` |
| `light_foreground` | Brushed aluminum switchgear | `#b3afa6` | `179, 175, 166` |
| `dark_foreground` | GT Silver in shadow | `#9599a2` | `149, 153, 162` |
| `muted` | Unlit gauge markings (comments) | `#838792` | `131, 135, 146` |
| `accent` | Carmine Red (rev needle, focus, alerts) | `#e1656c` | `225, 101, 108` |
| `cursor` | Carmine Red needle (`colors.toml`) | `#e1656c` | `225, 101, 108` |
| `red` | Carmine Red (text-weight / ANSI 1) | `#e07476` | `224, 116, 118` |
| `orange` | Cognac Amber (VDO gauge glow) | `#e8965a` | `232, 150, 90` |
| `yellow` | Satin Neodyme (champagne gold / ANSI 3) | `#dcbb6a` | `220, 187, 106` |
| `green` | Oak Green Sage (ANSI 2) | `#89b87f` | `137, 184, 127` |
| `cyan` | Fjord Glacier (ANSI 6) | `#6fc7cb` | `111, 199, 203` |
| `blue` | Aetna Blue (ANSI 4) | `#74a0d7` | `116, 160, 215` |
| `magenta` | Amethyst Metallic (ANSI 5) | `#b886b8` | `184, 134, 184` |
| `brown` | Club Cognac leather (decorators / PreProc) | `#ae7e62` | `174, 126, 98` |
| `bright_red` | Carmine Glow (ANSI 9) | `#f28a8b` | `242, 138, 139` |
| `bright_yellow` | Weissgold (ANSI 11) | `#edcf86` | `237, 207, 134` |
| `bright_green` | Oak Green Light (ANSI 10) | `#a1ce97` | `161, 206, 151` |
| `bright_cyan` | Glacier Light (ANSI 14) | `#87d9dd` | `135, 217, 221` |
| `bright_blue` | Aetna Light (ANSI 12) | `#8eb9f0` | `142, 185, 240` |
| `bright_magenta` | Amethyst Light (ANSI 13) | `#d09fd1` | `208, 159, 209` |
| `hyprland_active_border` | Active border gradient (`135deg`, `cc` alpha) | `#e1656c`, `#3a2429` | — |
| `hyprland_inactive_border` | Inactive border (`aa` alpha) | `#262930` | `38, 41, 48` |

See [`INVENTORY.md`](INVENTORY.md) for the complete palette derivation rules (translucent `#rrggbbaa`/`rgba(...)`, no-`#` hex formats, `[r, g, b]` arrays, and canonical `alpha-over-#15171a` surface stops).

## Application Index (36 Apps)

### Core Targets (`R1`, `R2`)
| App | Group | Target Files | Guide |
|---|---|---|---|
| **Telegram Desktop** | R1 | `telegram/carrera.tdesktop-theme` | [telegram/README.md](telegram/README.md) |
| **Neovim** | R2 | `neovim/colors/carrera.lua` (+ `~/.config/nvim/colors/carrera.lua`) | [neovim/README.md](neovim/README.md) |

### Terminals, Multiplexers & Shells (10 Apps)
| App | Group | Target Files | Guide |
|---|---|---|---|
| **Foot** | A2 | `foot/carrera.ini` | [foot/README.md](foot/README.md) |
| **Ghostty** | A2 | `ghostty/carrera` | [ghostty/README.md](ghostty/README.md) |
| **Alacritty** | A2 | `alacritty/carrera.toml` | [alacritty/README.md](alacritty/README.md) |
| **Kitty** | A2 | `kitty/carrera.conf` | [kitty/README.md](kitty/README.md) |
| **tmux** | A2 | `tmux/carrera.conf` | [tmux/README.md](tmux/README.md) |
| **Herdr** | A1 | `herdr/carrera.toml` | [herdr/README.md](herdr/README.md) |
| **Starship** | A1 | `starship/carrera.toml` | [starship/README.md](starship/README.md) |
| **zsh-syntax-highlighting** | A1 | `zsh-syntax-highlighting/carrera.zsh` | [zsh-syntax-highlighting/README.md](zsh-syntax-highlighting/README.md) |
| **fzf** | A1 | `fzf/carrera.sh` | [fzf/README.md](fzf/README.md) |
| **Atuin** | A1 | `atuin/carrera.toml` | [atuin/README.md](atuin/README.md) |

### CLI & TUI Developer Tools (14 Apps)
| App | Group | Target Files | Guide |
|---|---|---|---|
| **OpenCode** | A1 | `opencode/carrera.json` | [opencode/README.md](opencode/README.md) |
| **Claude Code** | A2 | `claude-code/carrera.json` | [claude-code/README.md](claude-code/README.md) |
| **Pi Coding Agent** | A2 | `pi/carrera.json` | [pi/README.md](pi/README.md) |
| **bat** | A1 | `bat/Carrera.tmTheme` | [bat/README.md](bat/README.md) |
| **Delta** | A1 | `delta/carrera.gitconfig` | [delta/README.md](delta/README.md) |
| **Lazygit** | A1 | `lazygit/carrera.yml` | [lazygit/README.md](lazygit/README.md) |
| **Lazydocker** | A1 | `lazydocker/carrera.yml` | [lazydocker/README.md](lazydocker/README.md) |
| **eza** | A1 | `eza/theme.yml` | [eza/README.md](eza/README.md) |
| **K9s** | A1 | `k9s/carrera.yaml` | [k9s/README.md](k9s/README.md) |
| **kubecolor** | A1 | `kubecolor/color.yaml` | [kubecolor/README.md](kubecolor/README.md) |
| **pgcli** | A1 | `pgcli/carrera.pgclirc` | [pgcli/README.md](pgcli/README.md) |
| **Cliamp** | A1 | `cliamp/carrera.toml` | [cliamp/README.md](cliamp/README.md) |
| **Fastfetch** | A1 | `fastfetch/carrera.jsonc` | [fastfetch/README.md](fastfetch/README.md) |
| **btop** | B | `btop/carrera.theme` | [btop/README.md](btop/README.md) |

### IDEs, Browsers, Desktop, WM & Toolkits (10 Apps)
| App | Group | Target Files | Guide |
|---|---|---|---|
| **VS Code / Antigravity IDE** | A2 | `vscode/package.json`, `vscode/themes/carrera-color-theme.json` | [vscode/README.md](vscode/README.md) |
| **Obsidian** | A2 | `obsidian/Carrera/manifest.json`, `obsidian/Carrera/theme.css` | [obsidian/README.md](obsidian/README.md) |
| **Chromium** | A2 | `chromium/manifest.json`, `chromium/chromium.theme` | [chromium/README.md](chromium/README.md) |
| **Zen Browser** | A1 | `zen-browser/userChrome.css`, `zen-browser/userContent.css` | [zen-browser/README.md](zen-browser/README.md) |
| **imv** | A1 | `imv/carrera.ini` | [imv/README.md](imv/README.md) |
| **mpv** | A1 | `mpv/mpv.conf` | [mpv/README.md](mpv/README.md) |
| **GTK 3 / GTK 4** | A1 | `gtk/gtk.css` | [gtk/README.md](gtk/README.md) |
| **Fcitx5** | A2 | `fcitx5/carrera/theme.conf` | [fcitx5/README.md](fcitx5/README.md) |
| **Hyprland** | A2 | `hyprland/carrera.conf` | [hyprland/README.md](hyprland/README.md) |
| **Hyprland Preview Share Picker** | A2 | `hyprland-preview-share-picker/style.css` | [hyprland-preview-share-picker/README.md](hyprland-preview-share-picker/README.md) |

## Installation Note

Each subdirectory contains standalone theme files and a short `README.md` detailing where to place or include them on your system without altering active defaults until you choose to activate them. For Neovim (`R2`), `neovim/colors/carrera.lua` is mirrored to `~/.config/nvim/colors/carrera.lua` so `:colorscheme carrera` works out of the box without altering your default startup colorscheme.

See [`INVENTORY.md`](INVENTORY.md) for the full workstation audit, validation commands, and exclusion rationale.

---

Not affiliated with or endorsed by Porsche AG. Porsche, 911 and Carrera are trademarks of Porsche AG.

Licensed under the [MIT License](LICENSE).
