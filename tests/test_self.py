"""Self-test suite: positive synthetic fixture (F1-F37) + comprehensive negative mutation suite."""

from __future__ import annotations

import io
import json
import os
import shutil
import tempfile
import unittest
import zipfile
from contextlib import contextmanager
from pathlib import Path
from typing import Iterator

from lib import DEFAULT_REFERENCE_COLORS
from lib.baseline import sha256_file, verify_absent_paths, verify_baseline_files
from lib.palette import BLENDED_SURFACE_APPS, DOC_DERIVED_HEXES, PaletteContract, hex_to_rgb
from lib.parsers import (
    extract_lua_hex_literals,
    generate_solid_png,
    parse_plist,
    parse_yaml,
    validate_css,
    validate_png_bytes,
    validate_tdesktop_theme,
)
from lib.specs import (
    SPEC_BY_ID,
    UNRESOLVED_PLACEHOLDER_RE,
    validate_deliverable_palette,
    validate_deliverable_structure,
)
from lib.validators import (
    validate_bat,
    validate_eza,
    validate_fastfetch,
    validate_foot,
    validate_fzf,
    validate_ghostty,
    validate_git_delta,
    validate_herdr,
    validate_hyprland,
    validate_kubecolor,
    validate_mpv,
    validate_nvim_colorscheme,
    validate_pgcli,
    validate_starship,
    validate_tmux,
    validate_zsh_syntax_highlighting,
)


@contextmanager
def _temp_env(overrides: dict[str, str]) -> Iterator[None]:
    old = {k: os.environ.get(k) for k in overrides}
    os.environ.update(overrides)
    try:
        yield
    finally:
        for k, v in old.items():
            if v is None:
                os.environ.pop(k, None)
            else:
                os.environ[k] = v


def _build_synthetic_project(root: Path, nvim_dest: Path, ref_colors: Path) -> None:
    """Create a complete valid synthetic Carrera v2.0.0 project covering F1-F37."""
    palette = PaletteContract(ref_colors)
    t = palette.tokens
    ref_repo = ref_colors.parent

    # F1: Foundation
    (root / "LICENSE").write_text(
        "MIT License\n\nCopyright (c) 2026 Aryan Hamedani\n", encoding="utf-8"
    )
    shutil.copy2(ref_colors, root / "colors.toml")

    app_dirs = [SPEC_BY_ID[i].app_dir for i in range(2, 38)]
    readme_lines = [
        "# Carrera v2.0.0 Themes",
        "",
        f"Background: `{t['background']}`, Foreground: `{t['foreground']}`, Accent: `{t['accent']}`.",
        "",
        "Porsche and Carrera are trademarks; this project is an independent palette.",
        "",
        "## Applications",
    ]
    inv_lines = ["# Carrera v2.0.0 Inventory", "", f"- `~/.config/nvim/colors/carrera.lua`"]
    for i in range(2, 38):
        sp = SPEC_BY_ID[i]
        readme_lines.append(f"- `{sp.app_dir}`")
        inv_lines.append(f"- `{sp.app_dir}`: " + ", ".join(f"`{f}`" for f in sp.theme_files))
        app_readme = root / sp.readme_file
        app_readme.parent.mkdir(parents=True, exist_ok=True)
        app_readme.write_text(
            f"# Carrera for {sp.name}\n\nManual install: copy the theme files to your config directory.\n",
            encoding="utf-8",
        )
    (root / "README.md").write_text("\n".join(readme_lines) + "\n", encoding="utf-8")
    (root / "INVENTORY.md").write_text("\n".join(inv_lines) + "\n", encoding="utf-8")

    # F2: Telegram Desktop
    tg_prefixes = (
        "window", "title", "dialogs", "history", "msg", "mediaview",
        "active", "box", "menu", "scroll", "tooltip", "notification",
    )
    tg_lines = [
        f"windowBg: {t['background']};",
        f"windowFg: {t['foreground']};",
        "windowBgOver: windowBg;",
    ]
    for pfx in tg_prefixes:
        for idx in range(9):
            col = t["foreground"] if idx % 2 else t["background"]
            tg_lines.append(f"{pfx}Item{idx}: {col};")
    tg_zip = root / "telegram/carrera.tdesktop-theme"
    with zipfile.ZipFile(tg_zip, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        zf.writestr("colors.tdesktop-theme", "\n".join(tg_lines) + "\n")
        zf.writestr("background.png", generate_solid_png(1, 1, (21, 23, 26)))

    # F3: Neovim
    lua_code = f"""vim.cmd("hi clear")
if vim.fn.exists("syntax_on") == 1 then vim.cmd("syntax reset") end
vim.o.background = "dark"
vim.o.termguicolors = true
vim.g.colors_name = "carrera"

local hl = vim.api.nvim_set_hl
hl(0, "Normal", {{ fg = "{t['foreground']}", bg = "{t['background']}" }})
hl(0, "CurSearch", {{ fg = "{t['background']}", bg = "{t['accent']}" }})
hl(0, "NormalFloat", {{ fg = "{t['foreground']}", bg = "{t['dark_background']}" }})
hl(0, "FloatBorder", {{ fg = "{t['muted']}", bg = "{t['dark_background']}" }})
hl(0, "CursorLine", {{ bg = "{t['lighter_background']}" }})
hl(0, "Visual", {{ bg = "{t['selection_background']}" }})
hl(0, "StatusLine", {{ fg = "{t['foreground']}", bg = "{t['lighter_background']}" }})
hl(0, "LineNr", {{ fg = "{t['muted']}" }})
hl(0, "Comment", {{ fg = "{t['muted']}", italic = true }})
hl(0, "Keyword", {{ fg = "{t['red']}" }})
hl(0, "Function", {{ fg = "{t['blue']}" }})
hl(0, "String", {{ fg = "{t['green']}" }})
hl(0, "Type", {{ fg = "{t['yellow']}" }})
hl(0, "Constant", {{ fg = "{t['orange']}" }})
hl(0, "Operator", {{ fg = "{t['cyan']}" }})
hl(0, "PreProc", {{ fg = "{t['brown']}" }})
hl(0, "Special", {{ fg = "{t['magenta']}" }})
hl(0, "DiffAdd", {{ bg = "#222a23" }})
hl(0, "DiffChange", {{ bg = "#202731" }})
hl(0, "DiffDelete", {{ bg = "#2d1e20" }})
hl(0, "DiffText", {{ bg = "#2b3646" }})
hl(0, "DiagnosticError", {{ fg = "{t['red']}" }})
hl(0, "@comment", {{ link = "Comment" }})
hl(0, "@lsp.type.function", {{ link = "Function" }})

vim.g.terminal_color_0 = "{t['background']}"
vim.g.terminal_color_1 = "{t['red']}"
vim.g.terminal_color_2 = "{t['green']}"
vim.g.terminal_color_3 = "{t['yellow']}"
vim.g.terminal_color_4 = "{t['blue']}"
vim.g.terminal_color_5 = "{t['magenta']}"
vim.g.terminal_color_6 = "{t['cyan']}"
vim.g.terminal_color_7 = "{t['foreground']}"
vim.g.terminal_color_8 = "{t['muted']}"
vim.g.terminal_color_9 = "{t['bright_red']}"
vim.g.terminal_color_10 = "{t['bright_green']}"
vim.g.terminal_color_11 = "{t['bright_yellow']}"
vim.g.terminal_color_12 = "{t['bright_blue']}"
vim.g.terminal_color_13 = "{t['bright_magenta']}"
vim.g.terminal_color_14 = "{t['bright_cyan']}"
vim.g.terminal_color_15 = "{t['bright_foreground']}"
"""
    (root / "neovim/colors").mkdir(parents=True, exist_ok=True)
    (root / "neovim/colors/carrera.lua").write_text(lua_code, encoding="utf-8")
    nvim_dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(root / "neovim/colors/carrera.lua", nvim_dest)

    # F4: Foot (no #)
    (root / "foot/carrera.ini").write_text(
        f"""[colors-dark]
foreground={t['foreground'][1:]}
background={t['background'][1:]}
selection-foreground={t['selection_foreground'][1:]}
selection-background={t['selection_background'][1:]}
cursor={t['background'][1:]} {t['bright_foreground'][1:]}
regular0={t['background'][1:]}
regular1={t['red'][1:]}
regular2={t['green'][1:]}
regular3={t['yellow'][1:]}
regular4={t['blue'][1:]}
regular5={t['magenta'][1:]}
regular6={t['cyan'][1:]}
regular7={t['foreground'][1:]}
bright0={t['muted'][1:]}
bright1={t['bright_red'][1:]}
bright2={t['bright_green'][1:]}
bright3={t['bright_yellow'][1:]}
bright4={t['bright_blue'][1:]}
bright5={t['bright_magenta'][1:]}
bright6={t['bright_cyan'][1:]}
bright7={t['bright_foreground'][1:]}
""",
        encoding="utf-8",
    )

    # F5: Ghostty
    (root / "ghostty/carrera").write_text(
        f"""background = {t['background']}
foreground = {t['foreground']}
cursor-color = {t['bright_foreground']}
selection-background = {t['selection_background']}
selection-foreground = {t['selection_foreground']}
palette = 0={t['background']}
palette = 1={t['red']}
palette = 2={t['green']}
palette = 3={t['yellow']}
palette = 4={t['blue']}
palette = 5={t['magenta']}
palette = 6={t['cyan']}
palette = 7={t['foreground']}
palette = 8={t['muted']}
palette = 9={t['bright_red']}
palette = 10={t['bright_green']}
palette = 11={t['bright_yellow']}
palette = 12={t['bright_blue']}
palette = 13={t['bright_magenta']}
palette = 14={t['bright_cyan']}
palette = 15={t['bright_foreground']}
""",
        encoding="utf-8",
    )

    # F6: Alacritty
    (root / "alacritty/carrera.toml").write_text(
        f"""[colors.primary]
background = "{t['background']}"
foreground = "{t['foreground']}"

[colors.cursor]
text = "{t['background']}"
cursor = "{t['bright_foreground']}"

[colors.selection]
text = "{t['selection_foreground']}"
background = "{t['selection_background']}"

[colors.normal]
black = "{t['background']}"
red = "{t['red']}"
green = "{t['green']}"
yellow = "{t['yellow']}"
blue = "{t['blue']}"
magenta = "{t['magenta']}"
cyan = "{t['cyan']}"
white = "{t['foreground']}"

[colors.bright]
black = "{t['muted']}"
red = "{t['bright_red']}"
green = "{t['bright_green']}"
yellow = "{t['bright_yellow']}"
blue = "{t['bright_blue']}"
magenta = "{t['bright_magenta']}"
cyan = "{t['bright_cyan']}"
white = "{t['bright_foreground']}"
""",
        encoding="utf-8",
    )

    # F7: Kitty
    (root / "kitty/carrera.conf").write_text(
        f"""foreground {t['foreground']}
background {t['background']}
selection_foreground {t['selection_foreground']}
selection_background {t['selection_background']}
cursor {t['bright_foreground']}
cursor_text_color {t['background']}
color0 {t['background']}
color1 {t['red']}
color2 {t['green']}
color3 {t['yellow']}
color4 {t['blue']}
color5 {t['magenta']}
color6 {t['cyan']}
color7 {t['foreground']}
color8 {t['muted']}
color9 {t['bright_red']}
color10 {t['bright_green']}
color11 {t['bright_yellow']}
color12 {t['bright_blue']}
color13 {t['bright_magenta']}
color14 {t['bright_cyan']}
color15 {t['bright_foreground']}
""",
        encoding="utf-8",
    )

    # F8: tmux
    (root / "tmux/carrera.conf").write_text(
        f"""set -g status-style "bg={t['background']},fg={t['foreground']}"
set -g status-left "#[fg={t['accent']}]#S "
set -g status-right "#[fg={t['muted']}]%H:%M"
set -g window-status-format "#I:#W"
set -g window-status-current-format "#[fg={t['accent']},bold]#I:#W"
set -g pane-border-style "fg={t['lighter_background']}"
set -g pane-active-border-style "fg={t['accent']}"
set -g message-style "bg={t['lighter_background']},fg={t['foreground']}"
set -g mode-style "bg={t['selection_background']},fg={t['selection_foreground']}"
set -g clock-mode-colour "{t['accent']}"
""",
        encoding="utf-8",
    )

    # F9: Herdr
    (root / "herdr/carrera.toml").write_text(
        f"""[theme.custom]
accent = "{t['accent']}"
sidebar_bg = "{t['dark_background']}"
active_row_bg = "{t['lighter_background']}"
selection_bg = "{t['selection_background']}"
panel_bg = "{t['background']}"
surface_dim = "{t['darker_background']}"
red = "{t['red']}"
green = "{t['green']}"
yellow = "{t['yellow']}"
text = "{t['foreground']}"
""",
        encoding="utf-8",
    )

    # F10: Starship
    (root / "starship/carrera.toml").write_text(
        f"""palette = "carrera"

[palettes.carrera]
bg = "{t['background']}"
fg = "{t['foreground']}"
accent = "{t['accent']}"
muted = "{t['muted']}"
red = "{t['red']}"
green = "{t['green']}"
yellow = "{t['yellow']}"
blue = "{t['blue']}"
cyan = "{t['cyan']}"
""",
        encoding="utf-8",
    )

    # F11: zsh-syntax-highlighting
    (root / "zsh-syntax-highlighting/carrera.zsh").write_text(
        f"""typeset -gA ZSH_HIGHLIGHT_STYLES
ZSH_HIGHLIGHT_STYLES[command]="fg={t['green']}"
ZSH_HIGHLIGHT_STYLES[builtin]="fg={t['cyan']}"
ZSH_HIGHLIGHT_STYLES[alias]="fg={t['green']}"
ZSH_HIGHLIGHT_STYLES[function]="fg={t['blue']}"
ZSH_HIGHLIGHT_STYLES[single-quoted-argument]="fg={t['yellow']}"
ZSH_HIGHLIGHT_STYLES[double-quoted-argument]="fg={t['yellow']}"
ZSH_HIGHLIGHT_STYLES[comment]="fg={t['muted']}"
ZSH_HIGHLIGHT_STYLES[unknown-token]="fg={t['red']}"
ZSH_HIGHLIGHT_STYLES[path]="fg={t['foreground']}"
ZSH_HIGHLIGHT_STYLES[globbing]="fg={t['magenta']}"
ZSH_HIGHLIGHT_STYLES[redirection]="fg={t['orange']}"
""",
        encoding="utf-8",
    )

    # F12: fzf
    (root / "fzf/carrera.sh").write_text(
        f"""export FZF_DEFAULT_OPTS="${{FZF_DEFAULT_OPTS}} --color=bg:{t['background']},bg+:{t['lighter_background']},fg:{t['foreground']},fg+:{t['bright_foreground']},hl:{t['accent']},hl+:{t['bright_red']},info:{t['blue']},prompt:{t['accent']},pointer:{t['accent']},marker:{t['green']},spinner:{t['yellow']},header:{t['muted']},border:{t['selection_background']}"
""",
        encoding="utf-8",
    )

    # F13: Atuin
    (root / "atuin/carrera.toml").write_text(
        f"""[theme]
name = "carrera"

[colors]
AlertInfo = "{t['cyan']}"
AlertWarn = "{t['yellow']}"
AlertError = "{t['red']}"
Annotation = "{t['muted']}"
Base = "{t['foreground']}"
Guidance = "{t['blue']}"
Important = "{t['accent']}"
Title = "{t['bright_foreground']}"
Muted = "{t['muted']}"
SyntaxCommand = "{t['green']}"
SyntaxFlag = "{t['orange']}"
SyntaxString = "{t['yellow']}"
SyntaxVariable = "{t['cyan']}"
SyntaxOperator = "{t['red']}"
SyntaxComment = "{t['muted']}"
""",
        encoding="utf-8",
    )

    # F14: OpenCode
    opencode_obj = {
        "$schema": "https://opencode.ai/theme.json",
        "defs": {
            "bg": t["background"],
            "panel": t["dark_background"],
            "elem": t["lighter_background"],
            "fg": t["foreground"],
            "muted": t["muted"],
            "accent": t["accent"],
            "blue": t["blue"],
            "red": t["red"],
            "yellow": t["yellow"],
            "green": t["green"],
            "cyan": t["cyan"],
            "diffAddBg": "#222a23",
        },
        "theme": {
            "primary": "accent",
            "secondary": "blue",
            "accent": "accent",
            "error": "red",
            "warning": "yellow",
            "success": "green",
            "info": "cyan",
            "text": "fg",
            "textMuted": "muted",
            "background": "bg",
            "backgroundPanel": "panel",
            "backgroundElement": "elem",
            "border": "elem",
            "borderActive": "accent",
            "borderSubtle": "panel",
            "diffAdded": "green",
            "diffAddedBg": "diffAddBg",
            "markdownHeading": "accent",
            "syntaxKeyword": "red",
        },
    }
    (root / "opencode/carrera.json").write_text(json.dumps(opencode_obj, indent=2), encoding="utf-8")

    # F15: Claude Code
    claude_obj = {
        "name": "Carrera",
        "base": "dark",
        "overrides": {
            "claude": t["accent"],
            "text": t["foreground"],
            "inverseText": t["background"],
            "subtle": t["muted"],
            "suggestion": t["blue"],
            "permission": t["yellow"],
            "success": t["green"],
            "error": t["red"],
            "warning": t["orange"],
            "merged": t["magenta"],
            "promptBorder": t["lighter_background"],
            "planMode": t["cyan"],
            "autoAccept": t["green"],
            "bashBorder": t["accent"],
            "ide": t["blue"],
            "diffAdded": "#222a23",
            "diffRemoved": "#2d1e20",
            "userMessageBackground": t["lighter_background"],
            "selectionBg": t["selection_background"],
            "rate_limit_fill": t["accent"],
        },
    }
    (root / "claude-code/carrera.json").write_text(json.dumps(claude_obj, indent=2), encoding="utf-8")

    # F16: Pi
    pi_colors = {f"c{i}": "fg" for i in range(35)}
    pi_colors["accent"] = "accent"
    pi_obj = {
        "$schema": "https://example.invalid/pi-theme.json",
        "name": "carrera",
        "vars": {"bg": t["background"], "panel": t["dark_background"], "fg": t["foreground"], "accent": t["accent"]},
        "colors": pi_colors,
        "export": {"pageBg": "bg", "cardBg": "panel", "infoBg": "panel"},
    }
    (root / "pi/carrera.json").write_text(json.dumps(pi_obj, indent=2), encoding="utf-8")

    # F17: bat
    (root / "bat/Carrera.tmTheme").write_text(
        f"""<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
  <key>name</key><string>Carrera</string>
  <key>settings</key>
  <array>
    <dict>
      <key>settings</key>
      <dict>
        <key>background</key><string>{t['background']}</string>
        <key>foreground</key><string>{t['foreground']}</string>
        <key>caret</key><string>{t['accent']}</string>
        <key>selection</key><string>{t['selection_background']}</string>
        <key>lineHighlight</key><string>{t['lighter_background']}</string>
        <key>gutter</key><string>{t['background']}</string>
        <key>gutterForeground</key><string>{t['muted']}</string>
      </dict>
    </dict>
    <dict>
      <key>scope</key><string>comment</string>
      <key>settings</key><dict><key>foreground</key><string>{t['muted']}</string></dict>
    </dict>
    <dict>
      <key>scope</key><string>keyword</string>
      <key>settings</key><dict><key>foreground</key><string>{t['red']}</string></dict>
    </dict>
    <dict>
      <key>scope</key><string>string</string>
      <key>settings</key><dict><key>foreground</key><string>{t['green']}</string></dict>
    </dict>
    <dict>
      <key>scope</key><string>constant.numeric</string>
      <key>settings</key><dict><key>foreground</key><string>{t['orange']}</string></dict>
    </dict>
    <dict>
      <key>scope</key><string>entity.name.function</string>
      <key>settings</key><dict><key>foreground</key><string>{t['blue']}</string></dict>
    </dict>
    <dict>
      <key>scope</key><string>entity.name.type</string>
      <key>settings</key><dict><key>foreground</key><string>{t['yellow']}</string></dict>
    </dict>
  </array>
</dict>
</plist>
""",
        encoding="utf-8",
    )

    # F18: Delta
    (root / "delta/carrera.gitconfig").write_text(
        f"""[delta "carrera"]
  plus-style = syntax "#222a23"
  plus-emph-style = syntax "#222a23"
  minus-style = syntax "#2d1e20"
  minus-emph-style = syntax "#2d1e20"
  line-numbers-plus-style = "{t['green']}"
  line-numbers-minus-style = "{t['red']}"
  line-numbers-zero-style = "{t['muted']}"
  file-style = bold "{t['foreground']}"
  file-decoration-style = "{t['accent']}" ul
  hunk-header-style = file line-number syntax
  hunk-header-file-style = "{t['blue']}"
  hunk-header-line-number-style = "{t['muted']}"
  blame-palette = "{t['background']} {t['dark_background']} {t['lighter_background']}"
""",
        encoding="utf-8",
    )

    # F19: Lazygit
    (root / "lazygit/carrera.yml").write_text(
        f"""gui:
  theme:
    activeBorderColor: ["{t['accent']}", "bold"]
    inactiveBorderColor: ["{t['muted']}"]
    searchingActiveBorderColor: ["{t['yellow']}", "bold"]
    optionsTextColor: ["{t['blue']}"]
    selectedLineBgColor: ["{t['selection_background']}"]
    inactiveViewSelectedLineBgColor: ["{t['lighter_background']}"]
    cherryPickedCommitFgColor: ["{t['accent']}"]
    cherryPickedCommitBgColor: ["{t['selection_background']}"]
    markedBaseCommitFgColor: ["{t['yellow']}"]
    unstagedChangesColor: ["{t['red']}"]
    defaultFgColor: ["{t['foreground']}"]
""",
        encoding="utf-8",
    )

    # F20: Lazydocker
    (root / "lazydocker/carrera.yml").write_text(
        f"""gui:
  theme:
    activeBorderColor: ["{t['accent']}", "bold"]
    inactiveBorderColor: ["{t['muted']}"]
    selectedLineBgColor: ["{t['selection_background']}"]
    optionsTextColor: ["{t['blue']}"]
""",
        encoding="utf-8",
    )

    # F21: eza
    (root / "eza/theme.yml").write_text(
        f"""colourful: true
filekinds:
  normal: {{foreground: "{t['foreground']}"}}
perms:
  user_read: {{foreground: "{t['yellow']}"}}
size:
  number_byte: {{foreground: "{t['green']}"}}
users:
  user_you: {{foreground: "{t['accent']}"}}
links:
  normal: {{foreground: "{t['cyan']}"}}
git:
  new: {{foreground: "{t['green']}"}}
file_type:
  source: {{foreground: "{t['blue']}"}}
""",
        encoding="utf-8",
    )

    # F22: K9s
    (root / "k9s/carrera.yaml").write_text(
        f"""k9s:
  body:
    fgColor: "{t['foreground']}"
    bgColor: "{t['background']}"
  prompt:
    fgColor: "{t['foreground']}"
    bgColor: "{t['dark_background']}"
  info:
    fgColor: "{t['cyan']}"
  dialog:
    fgColor: "{t['foreground']}"
    bgColor: "{t['dark_background']}"
  frame:
    border:
      fgColor: "{t['lighter_background']}"
    menu:
      fgColor: "{t['foreground']}"
    crumbs:
      fgColor: "{t['accent']}"
    status:
      newColor: "{t['green']}"
    title:
      fgColor: "{t['bright_foreground']}"
  views:
    charts:
      bgColor: "{t['background']}"
    table:
      bgColor: "{t['background']}"
    xray:
      fgColor: "{t['foreground']}"
    yaml:
      keyColor: "{t['blue']}"
    logs:
      fgColor: "{t['foreground']}"
""",
        encoding="utf-8",
    )

    # F23: kubecolor
    (root / "kubecolor/color.yaml").write_text(
        f"""preset: dark
theme:
  base:
    info: "{t['cyan']}"
    primary: "{t['blue']}"
    secondary: "{t['magenta']}"
    success: "{t['green']}"
    warning: "{t['yellow']}"
    danger: "{t['red']}"
    muted: "{t['muted']}"
    key: "{t['bright_foreground']}"
  table:
    header: "{t['bright_foreground']}"
  data:
    string: "{t['green']}"
""",
        encoding="utf-8",
    )

    # F24: pgcli
    (root / "pgcli/carrera.pgclirc").write_text(
        f"""[colors]
completion-menu.completion.current = "bg:{t['selection_background']} {t['bright_foreground']}"
completion-menu.completion = "bg:{t['dark_background']} {t['foreground']}"
selected = "bg:{t['selection_background']} {t['bright_foreground']}"
search = "bg:{t['lighter_background']} {t['foreground']}"
search.current = "bg:{t['accent']} {t['background']}"
bottom-toolbar = "bg:{t['dark_background']} {t['foreground']}"
bottom-toolbar.on = "bg:{t['dark_background']} {t['green']}"
bottom-toolbar.off = "bg:{t['dark_background']} {t['muted']}"
bottom-toolbar.transaction.valid = "bg:{t['dark_background']} {t['green']}"
bottom-toolbar.transaction.failed = "bg:{t['dark_background']} {t['red']}"
""",
        encoding="utf-8",
    )

    # F25: Cliamp
    (root / "cliamp/carrera.toml").write_text(
        f"""bg = "{t['background']}"
accent = "{t['accent']}"
bright_fg = "{t['bright_foreground']}"
fg = "{t['foreground']}"
green = "{t['green']}"
yellow = "{t['yellow']}"
red = "{t['red']}"
""",
        encoding="utf-8",
    )

    # F26: Fastfetch
    (root / "fastfetch/carrera.jsonc").write_text(
        f"""// Carrera fastfetch theme
{{
  "display": {{
    "color": {{
      "keys": "{t['accent']}",
      "title": "{t['bright_foreground']}",
      "separator": "{t['muted']}",
      "output": "{t['foreground']}"
    }}
  }}
}}
""",
        encoding="utf-8",
    )

    # F27: btop
    shutil.copy2(ref_repo / "btop.theme", root / "btop/carrera.theme")

    # F28: VS Code
    (root / "vscode/themes").mkdir(parents=True, exist_ok=True)
    (root / "vscode/package.json").write_text(
        json.dumps(
            {
                "name": "carrera-theme",
                "displayName": "Carrera",
                "version": "2.0.0",
                "engines": {"vscode": "^1.80.0"},
                "contributes": {
                    "themes": [
                        {
                            "label": "Carrera",
                            "uiTheme": "vs-dark",
                            "path": "./themes/carrera-color-theme.json",
                        }
                    ]
                },
            },
            indent=2,
        ),
        encoding="utf-8",
    )
    (root / "vscode/themes/carrera-color-theme.json").write_text(
        json.dumps(
            {
                "name": "Carrera",
                "type": "dark",
                "semanticHighlighting": True,
                "colors": {
                    "editor.background": t["background"],
                    "editor.foreground": t["foreground"],
                    "activityBarBadge.background": t["accent"],
                },
                "tokenColors": [
                    {"scope": "comment", "settings": {"foreground": t["muted"]}},
                    {"scope": "keyword", "settings": {"foreground": t["red"]}},
                ],
                "semanticTokenColors": {"function": t["blue"]},
            },
            indent=2,
        ),
        encoding="utf-8",
    )

    # F29: Obsidian
    (root / "obsidian/Carrera").mkdir(parents=True, exist_ok=True)
    (root / "obsidian/Carrera/manifest.json").write_text(
        json.dumps(
            {
                "name": "Carrera",
                "version": "2.0.0",
                "minAppVersion": "1.0.0",
                "author": "Aryan Hamedani",
            },
            indent=2,
        ),
        encoding="utf-8",
    )
    (root / "obsidian/Carrera/theme.css").write_text(
        f""".theme-dark {{
  --background-primary: {t['background']};
  --background-secondary: {t['dark_background']};
  --text-normal: {t['foreground']};
  --text-selection: {t['selection_background']};
  --background-modifier-border: {t['lighter_background']};
  --text-title-h1: {t['bright_foreground']};
  --text-title-h6: {t['light_foreground']};
  --text-link: {t['blue']};
  --text-accent: {t['accent']};
  --interactive-accent: {t['accent']};
  --code-normal: {t['green']};
  --text-error: {t['red']};
  --text-success: {t['green']};
}}
""",
        encoding="utf-8",
    )

    # F30: Chromium
    (root / "chromium/manifest.json").write_text(
        json.dumps(
            {
                "manifest_version": 3,
                "name": "Carrera",
                "version": "2.0.0",
                "theme": {
                    "colors": {
                        "frame": [16, 18, 21],
                        "toolbar": [21, 23, 26],
                        "tab_text": [214, 210, 199],
                        "tab_background_text": [149, 153, 162],
                        "bookmark_text": [214, 210, 199],
                        "ntp_background": [21, 23, 26],
                        "ntp_text": [214, 210, 199],
                    }
                },
            },
            indent=2,
        ),
        encoding="utf-8",
    )
    bg_csv = ",".join(map(str, hex_to_rgb(t["background"])))
    (root / "chromium/chromium.theme").write_text(f"{bg_csv}\n", encoding="utf-8")

    # F31: Zen Browser
    (root / "zen-browser/userChrome.css").write_text(
        f""":root {{
  --zen-primary-color: {t['accent']};
  --zen-main-browser-background: {t['background']};
  --zen-dialog-background: {t['dark_background']};
  --zen-urlbar-background: {t['lighter_background']};
  --toolbar-bgcolor: {t['dark_background']};
  --toolbar-color: {t['foreground']};
}}
""",
        encoding="utf-8",
    )
    (root / "zen-browser/userContent.css").write_text(
        f""":root {{
  --in-content-page-background: {t['background']};
  --in-content-page-color: {t['foreground']};
  --in-content-link-color: {t['blue']};
}}
""",
        encoding="utf-8",
    )

    # F32: imv (no #)
    (root / "imv/carrera.ini").write_text(
        f"""[options]
background = {t['background'][1:]}
overlay_text_color = {t['foreground'][1:]}
overlay_background_color = {t['dark_background'][1:]}
""",
        encoding="utf-8",
    )

    # F33: mpv (#AARRGGBB alpha first)
    (root / "mpv/mpv.conf").write_text(
        f"""background-color="{t['background']}"
osd-color="{t['foreground']}"
osd-back-color="#e6{t['dark_background'][1:]}"
osd-border-color="{t['lighter_background']}"
osd-selected-color="{t['accent']}"
""",
        encoding="utf-8",
    )

    # F34: GTK
    (root / "gtk/gtk.css").write_text(
        f"""@define-color window_bg_color {t['background']};
@define-color window_fg_color {t['foreground']};
@define-color view_bg_color {t['dark_background']};
@define-color view_fg_color {t['foreground']};
@define-color headerbar_bg_color {t['dark_background']};
@define-color headerbar_fg_color {t['foreground']};
@define-color accent_bg_color {t['accent']};
@define-color accent_color {t['accent']};
@define-color card_bg_color {t['lighter_background']};
@define-color popover_bg_color {t['lighter_background']};
@define-color dialog_bg_color {t['dark_background']};
""",
        encoding="utf-8",
    )

    # F35: Fcitx5
    (root / "fcitx5/carrera").mkdir(parents=True, exist_ok=True)
    (root / "fcitx5/carrera/theme.conf").write_text(
        f"""[Metadata]
Name=Carrera
Version=2.0.0

[InputPanel]
NormalColor={t['foreground']}
HighlightCandidateColor={t['bright_foreground']}
HighlightColor={t['bright_foreground']}
HighlightBackgroundColor={t['selection_background']}

[InputPanel/Background]
Color={t['background']}

[InputPanel/Highlight]
Color={t['selection_background']}

[Menu]
NormalColor={t['foreground']}

[Menu/Background]
Color={t['dark_background']}

[Menu/Highlight]
Color={t['selection_background']}

[Menu/Separator]
Color={t['lighter_background']}
""",
        encoding="utf-8",
    )

    # F36: Hyprland
    (root / "hyprland/carrera.conf").write_text(
        f"""general {{
  col.active_border = rgba(e1656ccc) rgba(3a2429cc) 135deg
  col.inactive_border = rgba(262930aa)
}}

group {{
  col.border_active = rgba(e1656ccc)
  col.border_inactive = rgba(262930aa)
}}
""",
        encoding="utf-8",
    )

    # F37: Hyprland Preview Share Picker
    (root / "hyprland-preview-share-picker/style.css").write_text(
        f"""@define-color foreground {t['foreground']};
@define-color background {t['background']};
@define-color accent {t['accent']};
@define-color muted {t['muted']};
@define-color card_bg {t['lighter_background']};
@define-color text_dark {t['dark_foreground']};
@define-color accent_hover {t['bright_red']};
@define-color selected_tab {t['selection_background']};
@define-color text {t['foreground']};

.window {{
  background-color: @background;
  color: @foreground;
}}

.card {{
  background-color: @card_bg;
}}

.region-button {{
  background-color: @selected_tab;
}}
""",
        encoding="utf-8",
    )


class TestSelfPositiveSuite(unittest.TestCase):
    """Verify Tiers 1-3 + isolated Tier 4 checks pass cleanly on a valid synthetic project."""

    def test_positive_synthetic_project_passes_tiers_1_to_3_and_isolated_tier4(self) -> None:
        with tempfile.TemporaryDirectory(prefix="carrera_selftest_pos_") as tmp:
            tmp_path = Path(tmp)
            proj = tmp_path / "carrera_themes"
            proj.mkdir()
            nvim_rtp = tmp_path / "nvim_rtp"
            nvim_dest = nvim_rtp / "colors/carrera.lua"
            _build_synthetic_project(proj, nvim_dest, DEFAULT_REFERENCE_COLORS)

            env = {
                "CARRERA_PROJECT_ROOT": str(proj),
                "CARRERA_NVIM_COLORSCHEME": str(nvim_dest),
                "CARRERA_REFERENCE_COLORS": str(DEFAULT_REFERENCE_COLORS),
                "CARRERA_REFERENCE_REPO": str(DEFAULT_REFERENCE_COLORS.parent),
                "CARRERA_NVIM_RTP": str(nvim_rtp),
                "CARRERA_NVIM_ISOLATED": "1",
            }
            with _temp_env(env):
                loader = unittest.TestLoader()
                suite = unittest.TestSuite()
                for mod_name in (
                    "test_tier1_coverage",
                    "test_tier2_boundaries",
                    "test_tier3_consistency",
                    "test_tier4_isolation",
                ):
                    suite.addTests(loader.loadTestsFromName(mod_name))
                buf = io.StringIO()
                runner = unittest.TextTestRunner(stream=buf, verbosity=1)
                result = runner.run(suite)
                self.assertTrue(
                    result.wasSuccessful(),
                    f"Positive synthetic suite failed:\n{buf.getvalue()}",
                )
                self.assertGreaterEqual(result.testsRun, 240)


class TestSelfNegativeMutations(unittest.TestCase):
    """Verify every negative mutation / exit-code trap is caught and fails."""

    def setUp(self) -> None:
        self.palette = PaletteContract(DEFAULT_REFERENCE_COLORS)
        self._tmp = tempfile.TemporaryDirectory(prefix="carrera_selftest_neg_")
        self.tmp_path = Path(self._tmp.name)

    def tearDown(self) -> None:
        self._tmp.cleanup()

    def test_neg_foreign_hex_rejected(self) -> None:
        for bad_hex in ("#1e1e2e", "#123456", "#cdd6f4", "#000000", "#ffffff"):
            ok, _ = self.palette.is_allowed_hex(bad_hex, "alacritty")
            self.assertFalse(ok, f"Direct app must reject foreign hex {bad_hex}")
            ok_b, _ = self.palette.is_allowed_hex(bad_hex, "neovim")
            self.assertFalse(ok_b, f"Blended app must reject foreign hex {bad_hex}")

        bad_ala = self.tmp_path / "alacritty/carrera.toml"
        bad_ala.parent.mkdir(parents=True)
        bad_ala.write_text(
            '[colors.primary]\nbackground = "#1e1e2e"\nforeground = "#d6d2c7"\n',
            encoding="utf-8",
        )
        errs = validate_deliverable_palette(SPEC_BY_ID[6], self.tmp_path, self.palette)
        self.assertTrue(errs, "Mutated alacritty with #1e1e2e must fail palette validation")

    def test_neg_hash_prefix_in_foot_and_imv_rejected(self) -> None:
        foot_p = self.tmp_path / "foot/carrera.ini"
        foot_p.parent.mkdir(parents=True)
        foot_p.write_text("[colors-dark]\nbackground=#15171a\nforeground=d6d2c7\n", encoding="utf-8")
        errs = validate_deliverable_palette(SPEC_BY_ID[4], self.tmp_path, self.palette)
        self.assertTrue(any("MUST NOT have '#'" in e for e in errs))
        self.assertFalse(validate_foot(foot_p).ok, "foot --check-config must fail on # prefix")

        imv_p = self.tmp_path / "imv/carrera.ini"
        imv_p.parent.mkdir(parents=True)
        imv_p.write_text(
            "[options]\nbackground = #15171a\noverlay_text_color = d6d2c7\noverlay_background_color = 101215\n",
            encoding="utf-8",
        )
        errs_imv = validate_deliverable_palette(SPEC_BY_ID[32], self.tmp_path, self.palette)
        self.assertTrue(any("MUST NOT have '#'" in e for e in errs_imv))

    def test_neg_cliamp_missing_key_and_bad_hex_rejected(self) -> None:
        cli_p = self.tmp_path / "cliamp/carrera.toml"
        cli_p.parent.mkdir(parents=True)
        cli_p.write_text('bg = "#15171a"\nfg = "#d6d2c7"\n', encoding="utf-8")
        with self.assertRaises(AssertionError):
            validate_deliverable_structure(SPEC_BY_ID[25], self.tmp_path)

        cli_p.write_text(
            'bg = "#15171a"\naccent = "#e1656cff"\nbright_fg = "#eae6dc"\n'
            'fg = "#d6d2c7"\ngreen = "#89b87f"\nyellow = "#dcbb6a"\nred = "#e07476"\n',
            encoding="utf-8",
        )
        errs = validate_deliverable_palette(SPEC_BY_ID[25], self.tmp_path, self.palette)
        self.assertTrue(errs, "8-hex in cliamp must fail strict #RRGGBB check")

    def test_neg_telegram_nested_dir_dangling_alias_and_bad_png_crc(self) -> None:
        tg_nested = self.tmp_path / "nested.tdesktop-theme"
        with zipfile.ZipFile(tg_nested, "w") as zf:
            zf.writestr("carrera/colors.tdesktop-theme", "windowBg: #15171a;\n")
            zf.writestr("carrera/background.png", generate_solid_png(1, 1, (21, 23, 26)))
        with self.assertRaises(ValueError):
            validate_tdesktop_theme(tg_nested)

        # Dangling alias
        tg_alias = self.tmp_path / "dangling.tdesktop-theme"
        lines = [f"k{i}: #15171a;" for i in range(105)] + ["broken: nonexistentAlias;"]
        with zipfile.ZipFile(tg_alias, "w") as zf:
            zf.writestr("colors.tdesktop-theme", "\n".join(lines))
            zf.writestr("background.png", generate_solid_png(1, 1, (21, 23, 26)))
        with self.assertRaises(ValueError):
            validate_tdesktop_theme(tg_alias)

        # Corrupt PNG CRC32
        good_png = bytearray(generate_solid_png(1, 1, (21, 23, 26)))
        good_png[-5] ^= 0xFF  # corrupt IEND CRC
        with self.assertRaises(ValueError):
            validate_png_bytes(bytes(good_png))

    def test_neg_bat_malformed_xml_exit0_trap_caught(self) -> None:
        bad_bat = self.tmp_path / "Carrera.tmTheme"
        bad_bat.write_text("<plist><dict><key>name</key><unclosed></plist>", encoding="utf-8")
        with self.assertRaises(Exception):
            parse_plist(bad_bat)
        res = validate_bat(bad_bat, theme_name="Carrera")
        self.assertFalse(res.ok, "bat validator must catch exit-0 malformed XML trap")

    def test_neg_neovim_copy_mismatch_and_missing_colorscheme_trap(self) -> None:
        res_missing = validate_nvim_colorscheme("nonexistent_carrera_xyz", isolated=True)
        self.assertFalse(res_missing.ok, "nvim validator must catch exit-0 E185 stderr trap")

        proj = self.tmp_path / "proj"
        (proj / "neovim/colors").mkdir(parents=True)
        (proj / "neovim/colors/carrera.lua").write_text("-- a\n", encoding="utf-8")
        active = self.tmp_path / "active.lua"
        active.write_text("-- b\n", encoding="utf-8")
        self.assertNotEqual(sha256_file(proj / "neovim/colors/carrera.lua"), sha256_file(active))

    def test_neg_tampered_r4_baseline_and_present_absent_path(self) -> None:
        sample = self.tmp_path / "cfg.toml"
        sample.write_text("theme = 'aether'\n", encoding="utf-8")
        errs = verify_baseline_files({str(sample): "0" * 64})
        self.assertTrue(errs, "Tampered baseline hash must be detected")
        absent_errs = verify_absent_paths((str(sample),))
        self.assertTrue(absent_errs, "Existing path in absent list must be detected")

    def test_neg_mpv_argb_rgb_channel_and_bad_option_trap(self) -> None:
        mpv_dir = self.tmp_path / "mpv"
        mpv_dir.mkdir()
        mpv_p = mpv_dir / "mpv.conf"
        # Valid #AARRGGBB using #15171a
        mpv_p.write_text('osd-back-color="#e615171a"\n', encoding="utf-8")
        self.assertEqual(validate_deliverable_palette(SPEC_BY_ID[33], self.tmp_path, self.palette), [])

        # Foreign RGB channel inside #AARRGGBB (#e6123456) -> must fail
        mpv_p.write_text('osd-back-color="#e6123456"\n', encoding="utf-8")
        errs = validate_deliverable_palette(SPEC_BY_ID[33], self.tmp_path, self.palette)
        self.assertTrue(errs, "mpv #AARRGGBB with foreign RGB 123456 must fail")

        # Bad option -> mpv exits 0 but prints Error to stdout
        mpv_p.write_text('bogus-mpv-option="#15171a"\n', encoding="utf-8")
        self.assertFalse(validate_mpv(mpv_p).ok, "mpv validator must catch exit-0 stdout error trap")

    def test_neg_starship_tmux_eza_cli_traps_caught(self) -> None:
        bad_starship = self.tmp_path / "starship.toml"
        bad_starship.write_text("palette = [unclosed\n", encoding="utf-8")
        self.assertFalse(validate_starship(bad_starship).ok, "starship exit-0 stderr trap must fail")

        bad_tmux = self.tmp_path / "tmux.conf"
        bad_tmux.write_text('set -g status-style "bg=#nothex"\n', encoding="utf-8")
        self.assertFalse(validate_tmux(bad_tmux).ok, "tmux source-file invalid style must fail")

        bad_eza = self.tmp_path / "eza.yml"
        bad_eza.write_text("bad: [unclosed\n", encoding="utf-8")
        self.assertFalse(validate_eza(bad_eza).ok, "eza exit-0 YAML trap must fail via yq")

    def test_neg_css_and_other_cli_validators(self) -> None:
        for bad_css in (
            ".a { color: #15171a;",
            "/* unclosed comment",
            "@define-color bg #15171a",
            ".a { color: #12345; }",
        ):
            with self.assertRaises(ValueError, msg=f"CSS should reject: {bad_css!r}"):
                validate_css(bad_css)

        bad_fzf = self.tmp_path / "fzf.sh"
        bad_fzf.write_text('export FZF_DEFAULT_OPTS="--color=bg:#nothex"\n', encoding="utf-8")
        self.assertFalse(validate_fzf(bad_fzf).ok)

        bad_kube = self.tmp_path / "kube.yaml"
        bad_kube.write_text('preset: dark\ntheme:\n  base:\n    info: "notacolor"\n', encoding="utf-8")
        self.assertFalse(validate_kubecolor(bad_kube).ok)

        bad_ff = self.tmp_path / "ff.jsonc"
        bad_ff.write_text('{"display":{"color":{"keys":"notacolor"}}}\n', encoding="utf-8")
        self.assertFalse(validate_fastfetch(bad_ff).ok)

        bad_pg = self.tmp_path / "pgclirc"
        bad_pg.write_text("[unclosed\n", encoding="utf-8")
        self.assertFalse(validate_pgcli(bad_pg).ok)

        bad_herdr = self.tmp_path / "herdr.toml"
        bad_herdr.write_text("[theme]\nname = [unclosed\n", encoding="utf-8")
        self.assertFalse(validate_herdr(bad_herdr).ok)

        bad_herdr_hex_dir = self.tmp_path / "herdr_hex/herdr"
        bad_herdr_hex_dir.mkdir(parents=True)
        (bad_herdr_hex_dir / "carrera.toml").write_text(
            '[theme.custom]\naccent = "notacolor"\n', encoding="utf-8"
        )
        self.assertTrue(
            validate_deliverable_palette(SPEC_BY_ID[9], self.tmp_path / "herdr_hex", self.palette),
            "herdr non-hex custom color must fail palette check",
        )

        bad_ghostty = self.tmp_path / "ghostty_bad"
        bad_ghostty.write_text("bogus-key = #15171a\n", encoding="utf-8")
        self.assertFalse(validate_ghostty(bad_ghostty).ok)

        bad_delta = self.tmp_path / "delta_bad.gitconfig"
        bad_delta.write_text('[delta "carrera\n  plus-style = syntax "#222a23"\n', encoding="utf-8")
        self.assertFalse(validate_git_delta(bad_delta).ok)

        bad_hypr = self.tmp_path / "hypr.conf"
        bad_hypr.write_text("general {\n  bogus_option_xyz = 123\n}\n", encoding="utf-8")
        self.assertFalse(validate_hyprland(bad_hypr).ok)

        bad_zsh = self.tmp_path / "bad.zsh"
        bad_zsh.write_text("if [ 1; then\n", encoding="utf-8")
        self.assertFalse(validate_zsh_syntax_highlighting(bad_zsh).ok)

    def test_neg_is_linear_mix_rejects_foreign_themes_and_grays(self) -> None:
        foreign_colors = (
            "#282828",  # Gruvbox bg0
            "#ebdbb2",  # Gruvbox fg1
            "#2e3440",  # Nord polar1
            "#4b5263",  # OneDark gutter
            "#808080",  # Neutral gray
            "#a89ea0",  # Muddy red+cyan cross-blend
            "#a19f9c",  # Muddy green+magenta cross-blend
        )
        for hx in foreign_colors:
            self.assertFalse(
                self.palette.is_linear_mix(hx),
                f"is_linear_mix must reject foreign/cross-blended color {hx}",
            )
            for app in ("vscode", "neovim", "opencode", "obsidian", "gtk"):
                self.assertIn(app, BLENDED_SURFACE_APPS)
                ok, _ = self.palette.is_allowed_hex(hx, app)
                self.assertFalse(ok, f"{app} must reject {hx}")

        for doc_hx in DOC_DERIVED_HEXES:
            self.assertTrue(self.palette.is_linear_mix(doc_hx), f"DOC_DERIVED_HEXES {doc_hx} must pass")
        self.assertTrue(self.palette.is_linear_mix("#1e252d"), "10% blue over #15171a must pass")

    def test_neg_neovim_0x_and_inline_hex_and_runtime_hl(self) -> None:
        t = self.palette.tokens
        # 1. Integer 0x123456 literal
        lua_int = (
            f'local n = #groups\n'
            f'hl(0, "Normal", {{ fg = "{t["foreground"]}", bg = "{t["background"]}" }})\n'
            f'hl(0, "CurSearch", {{ fg = "{t["accent"]}" }})\n'
            f'hl(0, "Visual", {{ bg = 0x123456 }})\n'
        )
        valid_int, mal_int = extract_lua_hex_literals(lua_int)
        self.assertEqual(mal_int, [], "Lua #groups length operator must not be flagged as hex")
        self.assertIn("#123456", valid_int)
        nv_dir = self.tmp_path / "nv1/neovim/colors"
        nv_dir.mkdir(parents=True)
        (nv_dir / "carrera.lua").write_text(lua_int, encoding="utf-8")
        errs_int = validate_deliverable_palette(SPEC_BY_ID[3], self.tmp_path / "nv1", self.palette)
        self.assertTrue(errs_int, "Neovim 0x123456 integer literal must fail palette check")

        # 2. Inline vim.cmd hex and malformed hex inside string
        lua_cmd = (
            f'hl(0, "Normal", {{ fg = "{t["foreground"]}", bg = "{t["background"]}" }})\n'
            f'hl(0, "CurSearch", {{ fg = "{t["accent"]}" }})\n'
            'vim.cmd("hi Visual guibg=#123456")\n'
        )
        (nv_dir / "carrera.lua").write_text(lua_cmd, encoding="utf-8")
        errs_cmd = validate_deliverable_palette(SPEC_BY_ID[3], self.tmp_path / "nv1", self.palette)
        self.assertTrue(errs_cmd, "Neovim vim.cmd inline #123456 must fail palette check")

        lua_mal = (
            f'hl(0, "Normal", {{ fg = "{t["foreground"]}", bg = "{t["background"]}" }})\n'
            f'hl(0, "CurSearch", {{ fg = "{t["accent"]}" }})\n'
            'vim.cmd("hi Visual guibg=#nothex")\n'
        )
        (nv_dir / "carrera.lua").write_text(lua_mal, encoding="utf-8")
        errs_mal = validate_deliverable_palette(SPEC_BY_ID[3], self.tmp_path / "nv1", self.palette)
        self.assertTrue(errs_mal, "Neovim malformed #nothex must fail palette check")

        # 3. Runtime Visual HL group probe catches computed off-palette Visual bg
        rtp = self.tmp_path / "nv_rt"
        (rtp / "colors").mkdir(parents=True)
        (rtp / "colors/carrera.lua").write_text(
            f"""vim.o.background = "dark"
vim.o.termguicolors = true
vim.g.colors_name = "carrera"
local hl = vim.api.nvim_set_hl
hl(0, "Normal", {{ fg = "{t['foreground']}", bg = "{t['background']}" }})
hl(0, "NormalFloat", {{ fg = "{t['foreground']}", bg = "{t['dark_background']}" }})
hl(0, "CursorLine", {{ bg = "{t['lighter_background']}" }})
hl(0, "Visual", {{ bg = "#".."123456" }})
hl(0, "StatusLine", {{ fg = "{t['foreground']}", bg = "{t['dark_background']}" }})
hl(0, "Comment", {{ fg = "{t['muted']}" }})
hl(0, "Keyword", {{ fg = "{t['red']}" }})
hl(0, "Function", {{ fg = "{t['blue']}" }})
hl(0, "String", {{ fg = "{t['green']}" }})
hl(0, "Type", {{ fg = "{t['yellow']}" }})
""",
            encoding="utf-8",
        )
        res_rt = validate_nvim_colorscheme("carrera", rtp_dir=rtp, isolated=True)
        self.assertTrue(res_rt.ok)
        vis_bg = res_rt.data["Visual"][1]
        self.assertIsNotNone(vis_bg)
        ok_vis, _ = self.palette.is_allowed_hex(f"#{vis_bg:06x}", "neovim")
        self.assertFalse(ok_vis, "Runtime Visual bg #123456 must fail PaletteContract")

    def test_neg_hyprland_0xaarrggbb_caught(self) -> None:
        hypr_dir = self.tmp_path / "hypr_hex/hyprland"
        hypr_dir.mkdir(parents=True)
        (hypr_dir / "carrera.conf").write_text(
            "general {\n  col.active_border = rgba(e1656ccc) 0xcc123456 135deg\n  col.inactive_border = rgba(262930aa)\n}\n"
            "group {\n  col.border_active = rgba(e1656ccc)\n  col.border_inactive = rgba(262930aa)\n}\n",
            encoding="utf-8",
        )
        errs = validate_deliverable_palette(SPEC_BY_ID[36], self.tmp_path / "hypr_hex", self.palette)
        self.assertTrue(errs, "Hyprland legacy 0xcc123456 must fail palette validation")

    def test_neg_all_sections_and_full_tree_scoping(self) -> None:
        t = self.palette.tokens
        # Foot [colors-light] foreign hex
        foot_root = self.tmp_path / "foot_sec"
        (foot_root / "foot").mkdir(parents=True)
        (foot_root / "foot/carrera.ini").write_text(
            f"[colors-dark]\nbackground={t['background'][1:]}\nforeground={t['foreground'][1:]}\n"
            f"[colors-light]\nbackground=123456\nforeground=abcdef\n",
            encoding="utf-8",
        )
        self.assertTrue(validate_deliverable_palette(SPEC_BY_ID[4], foot_root, self.palette))

        # imv extra section with # prefix / foreign hex
        imv_root = self.tmp_path / "imv_sec"
        (imv_root / "imv").mkdir(parents=True)
        (imv_root / "imv/carrera.ini").write_text(
            f"[options]\nbackground={t['background'][1:]}\noverlay_text_color={t['foreground'][1:]}\n"
            f"overlay_background_color={t['dark_background'][1:]}\n[colors]\nextra=123456\n",
            encoding="utf-8",
        )
        self.assertTrue(validate_deliverable_palette(SPEC_BY_ID[32], imv_root, self.palette))

        # Fastfetch logo.color outside display.color
        ff_root = self.tmp_path / "ff_logo"
        (ff_root / "fastfetch").mkdir(parents=True)
        (ff_root / "fastfetch/carrera.jsonc").write_text(
            json.dumps(
                {
                    "$schema": "https://github.com/fastfetch-cli/fastfetch/raw/dev/doc/json_schema.json",
                    "logo": {"color": {"1": "#123456"}},
                    "display": {"color": {"keys": t["accent"]}},
                }
            ),
            encoding="utf-8",
        )
        self.assertTrue(validate_deliverable_palette(SPEC_BY_ID[26], ff_root, self.palette))

        # Starship outside [palettes.carrera]
        ss_root = self.tmp_path / "ss_char"
        (ss_root / "starship").mkdir(parents=True)
        (ss_root / "starship/carrera.toml").write_text(
            f'palette = "carrera"\n[character]\nsuccess_symbol = "[>](#123456)"\n'
            f'[palettes.carrera]\nbg = "{t["background"]}"\n',
            encoding="utf-8",
        )
        self.assertTrue(validate_deliverable_palette(SPEC_BY_ID[10], ss_root, self.palette))

    def test_neg_compound_padded_and_malformed_hash_tokens(self) -> None:
        t = self.palette.tokens
        # OpenCode leading space " #123456"
        oc_root = self.tmp_path / "oc_pad"
        (oc_root / "opencode").mkdir(parents=True)
        (oc_root / "opencode/carrera.json").write_text(
            json.dumps(
                {
                    "$schema": "https://opencode.ai/theme.json",
                    "defs": {"bg": t["background"], "bad": " #123456"},
                    "theme": {"background": "bg"},
                }
            ),
            encoding="utf-8",
        )
        self.assertTrue(validate_deliverable_palette(SPEC_BY_ID[14], oc_root, self.palette))

        # Kubecolor compound "bg:#123456" and "bg:#nothex"
        kc_root = self.tmp_path / "kc_comp"
        (kc_root / "kubecolor").mkdir(parents=True)
        (kc_root / "kubecolor/color.yaml").write_text(
            'preset: dark\ntheme:\n  base:\n    info: "bg:#123456"\n', encoding="utf-8"
        )
        self.assertTrue(validate_deliverable_palette(SPEC_BY_ID[23], kc_root, self.palette))

        (kc_root / "kubecolor/color.yaml").write_text(
            'preset: dark\ntheme:\n  base:\n    info: "bg:#nothex"\n', encoding="utf-8"
        )
        self.assertTrue(validate_deliverable_palette(SPEC_BY_ID[23], kc_root, self.palette))

        # Valid kubecolor compound "#838792:italic" and "#74a0d7 / #6fc7cb" passes
        (kc_root / "kubecolor/color.yaml").write_text(
            'preset: dark\ntheme:\n  base:\n    muted: "#838792:italic"\n    key: "#74a0d7 / #6fc7cb"\n',
            encoding="utf-8",
        )
        self.assertEqual(validate_deliverable_palette(SPEC_BY_ID[23], kc_root, self.palette), [])

        # pgcli bg:#nothex
        pg_root = self.tmp_path / "pg_bad"
        (pg_root / "pgcli").mkdir(parents=True)
        (pg_root / "pgcli/carrera.pgclirc").write_text(
            '[colors]\ncompletion-menu.completion = "bg:#nothex"\n', encoding="utf-8"
        )
        self.assertTrue(validate_deliverable_palette(SPEC_BY_ID[24], pg_root, self.palette))

        # vscode: valid "C# Attribute" passes, while "bold #123456" fails
        vs_root = self.tmp_path / "vs_comp"
        (vs_root / "vscode/themes").mkdir(parents=True)
        (vs_root / "vscode/package.json").write_text(
            json.dumps({"contributes": {"themes": [{"path": "./themes/t.json"}]}}),
            encoding="utf-8",
        )
        (vs_root / "vscode/themes/t.json").write_text(
            json.dumps(
                {
                    "colors": {"editor.background": t["background"]},
                    "tokenColors": [{"name": "C# Attribute", "settings": {"foreground": t["foreground"]}}],
                }
            ),
            encoding="utf-8",
        )
        self.assertEqual(validate_deliverable_palette(SPEC_BY_ID[28], vs_root, self.palette), [])
        (vs_root / "vscode/themes/t.json").write_text(
            json.dumps({"colors": {"editor.background": "bold #123456"}}),
            encoding="utf-8",
        )
        self.assertTrue(validate_deliverable_palette(SPEC_BY_ID[28], vs_root, self.palette))

    def test_neg_telegram_windowbg_alias_mismatch(self) -> None:
        tg_root = self.tmp_path / "tg_alias"
        (tg_root / "telegram").mkdir(parents=True)
        prefixes = (
            "window", "title", "dialogs", "history", "msg", "mediaview",
            "active", "box", "menu", "scroll", "tooltip", "notification",
        )
        lines = ["windowBg: badBgAlias;", "badBgAlias: #e1656c;"]
        for pfx in prefixes:
            for i in range(9):
                lines.append(f"{pfx}K{i}: #15171a;")
        with zipfile.ZipFile(tg_root / "telegram/carrera.tdesktop-theme", "w") as zf:
            zf.writestr("colors.tdesktop-theme", "\n".join(lines))
            zf.writestr("background.png", generate_solid_png(1, 1, (21, 23, 26)))
        errs = validate_deliverable_palette(SPEC_BY_ID[2], tg_root, self.palette)
        self.assertTrue(errs, "Telegram windowBg alias resolving to #e1656c instead of #15171a must fail")

    def test_neg_yaml_duplicate_key_rejected(self) -> None:
        dup_yaml = self.tmp_path / "eza_dup.yml"
        dup_yaml.write_text(
            'colourful: true\nfilekinds:\n  normal: {foreground: "#123456"}\n  normal: {foreground: "#d6d2c7"}\n',
            encoding="utf-8",
        )
        with self.assertRaises(ValueError):
            parse_yaml(dup_yaml)
        self.assertFalse(validate_eza(dup_yaml).ok, "Duplicate YAML key must fail validate_eza")

    def test_neg_css_non_hex_functions_and_mpv_float_rgb(self) -> None:
        for bad_fn_css in (
            ".a { color: hsl(0, 100%, 50%); }",
            ".a { color: hsla(0, 100%, 50%, 0.5); }",
            ".a { color: oklch(0.65 0.2 25); }",
            ".a { color: oklab(0.6 0.1 0.1); }",
        ):
            with self.assertRaises(ValueError, msg=f"CSS must reject {bad_fn_css!r}"):
                validate_css(bad_fn_css)

        mpv_root = self.tmp_path / "mpv_float"
        (mpv_root / "mpv").mkdir(parents=True)
        (mpv_root / "mpv/mpv.conf").write_text('osd-color="1.0/0.0/0.0"\n', encoding="utf-8")
        self.assertTrue(
            validate_deliverable_palette(SPEC_BY_ID[33], mpv_root, self.palette),
            "mpv float r/g/b color must fail palette check",
        )

    def test_neg_zsh_and_tmux_named_ansi_colors_and_dotted_placeholders(self) -> None:
        t = self.palette.tokens
        zsh_root = self.tmp_path / "zsh_named"
        (zsh_root / "zsh-syntax-highlighting").mkdir(parents=True)
        (zsh_root / "zsh-syntax-highlighting/carrera.zsh").write_text(
            f'typeset -gA ZSH_HIGHLIGHT_STYLES\nZSH_HIGHLIGHT_STYLES[command]="fg=red"\n'
            f'ZSH_HIGHLIGHT_STYLES[comment]="fg={t["muted"]}"\n',
            encoding="utf-8",
        )
        self.assertTrue(validate_deliverable_palette(SPEC_BY_ID[11], zsh_root, self.palette))

        tmux_root = self.tmp_path / "tmux_named"
        (tmux_root / "tmux").mkdir(parents=True)
        (tmux_root / "tmux/carrera.conf").write_text(
            f'set -g status-style "bg=colour196,fg={t["foreground"]}"\n'
            f'set -g clock-mode-colour "{t["accent"]}"\n'
            f'set -g pane-border-style "fg={t["background"]}"\n',
            encoding="utf-8",
        )
        self.assertTrue(validate_deliverable_palette(SPEC_BY_ID[8], tmux_root, self.palette))

        for bad_ph in ("{{ background.hex }}", "{{ foreground | strip_hash }}", "{{ accent }}"):
            self.assertIsNotNone(
                UNRESOLVED_PLACEHOLDER_RE.search(bad_ph),
                f"UNRESOLVED_PLACEHOLDER_RE must catch {bad_ph!r}",
            )

    def test_neg_non_shell_installer_and_git_skip_and_chromium_csv(self) -> None:
        from test_tier3_consistency import TestTier3Consistency

        repo_root = self.tmp_path / "repo_r4"
        (repo_root / "fzf").mkdir(parents=True)
        (repo_root / "zsh-syntax-highlighting").mkdir(parents=True)
        (repo_root / "fzf/carrera.sh").write_text('export FZF_DEFAULT_OPTS="--color=bg:#15171a"\n', encoding="utf-8")
        (repo_root / "zsh-syntax-highlighting/carrera.zsh").write_text('ZSH_HIGHLIGHT_STYLES[default]="fg=#d6d2c7"\n', encoding="utf-8")
        # .git/hooks/*.sample executable must be skipped cleanly
        git_hook = repo_root / ".git/hooks/pre-commit.sample"
        git_hook.parent.mkdir(parents=True)
        git_hook.write_text("#!/bin/sh\nexit 0\n", encoding="utf-8")
        os.chmod(git_hook, 0o755)

        t3 = TestTier3Consistency("test_no_auto_activation_scripts_or_hooks")
        with _temp_env({"CARRERA_PROJECT_ROOT": str(repo_root)}):
            t3.test_no_auto_activation_scripts_or_hooks()
            # Adding install.py with omarchy-theme-set must fail
            (repo_root / "install.py").write_text(
                'import os\nos.system("omarchy-theme-set carrera")\n', encoding="utf-8"
            )
            with self.assertRaises(AssertionError):
                t3.test_no_auto_activation_scripts_or_hooks()

        # Chromium dynamic CSV mismatch
        chr_root = self.tmp_path / "chr_bad"
        (chr_root / "chromium").mkdir(parents=True)
        (chr_root / "chromium/manifest.json").write_text(
            json.dumps({"manifest_version": 3, "theme": {"colors": {"frame": [21, 23, 26]}}}),
            encoding="utf-8",
        )
        (chr_root / "chromium/chromium.theme").write_text("0,0,0\n", encoding="utf-8")
        self.assertTrue(validate_deliverable_palette(SPEC_BY_ID[30], chr_root, self.palette))


if __name__ == "__main__":
    unittest.main()
