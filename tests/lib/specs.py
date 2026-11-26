"""Declarative specification registry and structural validators for deliverables #1-#37."""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from .palette import HEX6_RE, HEX8_RE, BARE_HEX6_RE, HYPR_RGBA_RE, PaletteContract, hex_to_rgb
from .parsers import (
    extract_lua_hex_literals,
    parse_btop_theme,
    parse_ghostty,
    parse_git_config,
    parse_hyprland_conf,
    parse_ini,
    parse_json,
    parse_jsonc,
    parse_kitty,
    parse_mpv_conf,
    parse_plist,
    parse_toml,
    parse_yaml,
    validate_css,
    validate_tdesktop_theme,
)


@dataclass(frozen=True, slots=True)
class DeliverableSpec:
    feature_id: int
    name: str
    app_dir: str
    required_files: tuple[str, ...]
    readme_file: str
    theme_files: tuple[str, ...]
    palette_mode: str  # "foundation" | "direct" | "blended"


DELIVERABLE_SPECS: tuple[DeliverableSpec, ...] = (
    DeliverableSpec(1, "Repo Foundation & Palette", ".", ("LICENSE", "colors.toml", "README.md", "INVENTORY.md"), "README.md", ("colors.toml",), "foundation"),
    DeliverableSpec(2, "Telegram Desktop (R1)", "telegram", ("telegram/911.tdesktop-theme", "telegram/README.md"), "telegram/README.md", ("telegram/911.tdesktop-theme",), "blended"),
    DeliverableSpec(3, "Neovim (R2)", "neovim", ("neovim/colors/911.lua", "neovim/README.md"), "neovim/README.md", ("neovim/colors/911.lua",), "blended"),
    DeliverableSpec(4, "Foot", "foot", ("foot/911.ini", "foot/README.md"), "foot/README.md", ("foot/911.ini",), "direct"),
    DeliverableSpec(5, "Ghostty", "ghostty", ("ghostty/911", "ghostty/README.md"), "ghostty/README.md", ("ghostty/911",), "direct"),
    DeliverableSpec(6, "Alacritty", "alacritty", ("alacritty/911.toml", "alacritty/README.md"), "alacritty/README.md", ("alacritty/911.toml",), "direct"),
    DeliverableSpec(7, "Kitty", "kitty", ("kitty/911.conf", "kitty/README.md"), "kitty/README.md", ("kitty/911.conf",), "direct"),
    DeliverableSpec(8, "tmux", "tmux", ("tmux/911.conf", "tmux/README.md"), "tmux/README.md", ("tmux/911.conf",), "direct"),
    DeliverableSpec(9, "Herdr", "herdr", ("herdr/911.toml", "herdr/README.md"), "herdr/README.md", ("herdr/911.toml",), "direct"),
    DeliverableSpec(10, "Starship", "starship", ("starship/911.toml", "starship/README.md"), "starship/README.md", ("starship/911.toml",), "direct"),
    DeliverableSpec(11, "zsh-syntax-highlighting", "zsh-syntax-highlighting", ("zsh-syntax-highlighting/911.zsh", "zsh-syntax-highlighting/README.md"), "zsh-syntax-highlighting/README.md", ("zsh-syntax-highlighting/911.zsh",), "direct"),
    DeliverableSpec(12, "fzf", "fzf", ("fzf/911.sh", "fzf/README.md"), "fzf/README.md", ("fzf/911.sh",), "direct"),
    DeliverableSpec(13, "Atuin", "atuin", ("atuin/911.toml", "atuin/README.md"), "atuin/README.md", ("atuin/911.toml",), "direct"),
    DeliverableSpec(14, "OpenCode", "opencode", ("opencode/911.json", "opencode/README.md"), "opencode/README.md", ("opencode/911.json",), "blended"),
    DeliverableSpec(15, "Claude Code", "claude-code", ("claude-code/911.json", "claude-code/README.md"), "claude-code/README.md", ("claude-code/911.json",), "blended"),
    DeliverableSpec(16, "Pi Coding Agent", "pi", ("pi/911.json", "pi/README.md"), "pi/README.md", ("pi/911.json",), "blended"),
    DeliverableSpec(17, "bat", "bat", ("bat/911.tmTheme", "bat/README.md"), "bat/README.md", ("bat/911.tmTheme",), "blended"),
    DeliverableSpec(18, "Delta", "delta", ("delta/911.gitconfig", "delta/README.md"), "delta/README.md", ("delta/911.gitconfig",), "blended"),
    DeliverableSpec(19, "Lazygit", "lazygit", ("lazygit/911.yml", "lazygit/README.md"), "lazygit/README.md", ("lazygit/911.yml",), "direct"),
    DeliverableSpec(20, "Lazydocker", "lazydocker", ("lazydocker/911.yml", "lazydocker/README.md"), "lazydocker/README.md", ("lazydocker/911.yml",), "direct"),
    DeliverableSpec(21, "eza", "eza", ("eza/theme.yml", "eza/README.md"), "eza/README.md", ("eza/theme.yml",), "direct"),
    DeliverableSpec(22, "K9s", "k9s", ("k9s/911.yaml", "k9s/README.md"), "k9s/README.md", ("k9s/911.yaml",), "direct"),
    DeliverableSpec(23, "kubecolor", "kubecolor", ("kubecolor/color.yaml", "kubecolor/README.md"), "kubecolor/README.md", ("kubecolor/color.yaml",), "direct"),
    DeliverableSpec(24, "pgcli", "pgcli", ("pgcli/911.pgclirc", "pgcli/README.md"), "pgcli/README.md", ("pgcli/911.pgclirc",), "direct"),
    DeliverableSpec(25, "Cliamp", "cliamp", ("cliamp/911.toml", "cliamp/README.md"), "cliamp/README.md", ("cliamp/911.toml",), "direct"),
    DeliverableSpec(26, "Fastfetch", "fastfetch", ("fastfetch/911.jsonc", "fastfetch/README.md"), "fastfetch/README.md", ("fastfetch/911.jsonc",), "direct"),
    DeliverableSpec(27, "btop", "btop", ("btop/911.theme", "btop/README.md"), "btop/README.md", ("btop/911.theme",), "direct"),
    DeliverableSpec(28, "VS Code / Antigravity IDE", "vscode", ("vscode/package.json", "vscode/themes/911-color-theme.json", "vscode/README.md"), "vscode/README.md", ("vscode/themes/911-color-theme.json",), "blended"),
    DeliverableSpec(29, "Obsidian", "obsidian", ("obsidian/911/manifest.json", "obsidian/911/theme.css", "obsidian/README.md"), "obsidian/README.md", ("obsidian/911/theme.css",), "blended"),
    DeliverableSpec(30, "Chromium", "chromium", ("chromium/manifest.json", "chromium/chromium.theme", "chromium/README.md"), "chromium/README.md", ("chromium/manifest.json", "chromium/chromium.theme"), "direct"),
    DeliverableSpec(31, "Zen Browser", "zen-browser", ("zen-browser/userChrome.css", "zen-browser/userContent.css", "zen-browser/README.md"), "zen-browser/README.md", ("zen-browser/userChrome.css", "zen-browser/userContent.css"), "blended"),
    DeliverableSpec(32, "imv", "imv", ("imv/911.ini", "imv/README.md"), "imv/README.md", ("imv/911.ini",), "direct"),
    DeliverableSpec(33, "mpv", "mpv", ("mpv/mpv.conf", "mpv/README.md"), "mpv/README.md", ("mpv/mpv.conf",), "direct"),
    DeliverableSpec(34, "GTK 3 / GTK 4", "gtk", ("gtk/gtk.css", "gtk/README.md"), "gtk/README.md", ("gtk/gtk.css",), "blended"),
    DeliverableSpec(35, "Fcitx5", "fcitx5", ("fcitx5/911/theme.conf", "fcitx5/README.md"), "fcitx5/README.md", ("fcitx5/911/theme.conf",), "direct"),
    DeliverableSpec(36, "Hyprland", "hyprland", ("hyprland/911.conf", "hyprland/README.md"), "hyprland/README.md", ("hyprland/911.conf",), "direct"),
    DeliverableSpec(37, "Hyprland Preview Share Picker", "hyprland-preview-share-picker", ("hyprland-preview-share-picker/style.css", "hyprland-preview-share-picker/README.md"), "hyprland-preview-share-picker/README.md", ("hyprland-preview-share-picker/style.css",), "direct"),
)

SPEC_BY_ID: dict[int, DeliverableSpec] = {s.feature_id: s for s in DELIVERABLE_SPECS}
APP_DIRS: tuple[str, ...] = tuple(s.app_dir for s in DELIVERABLE_SPECS if s.feature_id >= 2)

# Unresolved Omarchy template placeholders
UNRESOLVED_PLACEHOLDER_RE = re.compile(r"\{\{[^}]+\}\}")
GENERIC_HEX_RE = re.compile(r"#[0-9a-fA-F]{3,8}\b")
HASH_TOKEN_RE = re.compile(r"(?<![A-Za-z0-9_])#([0-9A-Za-z]+)")
URL_RE = re.compile(r"https?://\S+")
HYPR_HEX_INT_RE = re.compile(r"\b0x([0-9a-fA-F]{8})\b", re.IGNORECASE)
FOOT_TWO_HEX_KEYS: frozenset[str] = frozenset(
    {
        "cursor",
        "jump-labels",
        "scrollback-indicator",
        "search-box-no-match",
        "search-box-match",
    }
)


def walk_strings(obj: Any) -> list[str]:
    out: list[str] = []
    if isinstance(obj, str):
        out.append(obj)
    elif isinstance(obj, list):
        for item in obj:
            out.extend(walk_strings(item))
    elif isinstance(obj, dict):
        for val in obj.values():
            out.extend(walk_strings(val))
    return out


def _extract_hash_tokens_from_strings(strings: list[str]) -> tuple[list[str], list[str]]:
    """Extract valid (#rrggbb/#rrggbbaa) and malformed (#...) tokens from strings, skipping URLs."""
    valid: list[str] = []
    malformed: list[str] = []
    for s in strings:
        cleaned = URL_RE.sub("", s)
        for m in HASH_TOKEN_RE.finditer(cleaned):
            tok = "#" + m.group(1)
            if HEX6_RE.match(tok) or HEX8_RE.match(tok):
                valid.append(tok.lower())
            else:
                malformed.append(tok)
    return valid, malformed


def _check_hex_values(
    hex_values: list[str], palette: PaletteContract, app_name: str, *, allow_mpv_argb: bool = False
) -> list[str]:
    errors: list[str] = []
    for hx in hex_values:
        ok, reason = palette.is_allowed_hex(hx, app_name, allow_mpv_argb=allow_mpv_argb)
        if not ok:
            errors.append(reason)
    return errors


def _check_strings_hash_tokens(
    strings: list[str], palette: PaletteContract, app_name: str, errors: list[str]
) -> list[str]:
    valid, malformed = _extract_hash_tokens_from_strings(strings)
    for bad in malformed:
        errors.append(f"Malformed hex color {bad!r} in {app_name}")
    errors.extend(_check_hex_values(valid, palette, app_name))
    return valid


def validate_deliverable_structure(
    spec: DeliverableSpec, project_root: Path
) -> dict[str, Any]:
    """Parse deliverable and verify required sections/keys/tokens (Tier 1 checks 4 & 5)."""
    fid = spec.feature_id

    if fid == 1:
        lic = (project_root / "LICENSE").read_text(encoding="utf-8")
        if "MIT License" not in lic or "2026" not in lic or "Aryan Hamedani" not in lic:
            raise AssertionError("LICENSE missing MIT License or Copyright (c) 2026 Aryan Hamedani")
        colors = parse_toml(project_root / "colors.toml")
        if colors.get("mode") != "dark":
            raise AssertionError(f"colors.toml mode must be 'dark', got {colors.get('mode')!r}")
        for k in ("background", "foreground", "accent", "red", "green", "blue"):
            if k not in colors:
                raise AssertionError(f"colors.toml missing key {k!r}")
        readme = (project_root / "README.md").read_text(encoding="utf-8")
        if "Porsche" not in readme:
            raise AssertionError("Root README.md missing Porsche trademark disclaimer")
        inv = (project_root / "INVENTORY.md").read_text(encoding="utf-8")
        if "911" not in inv:
            raise AssertionError("INVENTORY.md missing '911'")
        return {"colors": colors}

    if fid == 2:
        info = validate_tdesktop_theme(project_root / "telegram/911.tdesktop-theme")
        return info

    if fid == 3:
        p = project_root / "neovim/colors/911.lua"
        text = p.read_text(encoding="utf-8")
        for needle in (
            "colors_name",
            "911",
            "background",
            "dark",
            "termguicolors",
            "Normal",
            "NormalFloat",
            "FloatBorder",
            "CursorLine",
            "Visual",
            "StatusLine",
            "LineNr",
            "Comment",
            "Keyword",
            "Function",
            "String",
            "Type",
            "Constant",
            "Operator",
            "PreProc",
            "Special",
            "DiffAdd",
            "DiffChange",
            "DiffDelete",
            "DiffText",
            "Diagnostic",
            "@lsp.",
            "terminal_color_0",
            "terminal_color_15",
        ):
            if needle not in text:
                raise AssertionError(f"neovim/colors/911.lua missing required token {needle!r}")
        return {"text": text}

    if fid == 4:
        cp = parse_ini(project_root / "foot/911.ini")
        if not cp.has_section("colors-dark"):
            raise AssertionError("foot/911.ini missing [colors-dark] section")
        sec = cp["colors-dark"]
        required = (
            "foreground",
            "background",
            "selection-foreground",
            "selection-background",
            "cursor",
        ) + tuple(f"regular{i}" for i in range(8)) + tuple(f"bright{i}" for i in range(8))
        missing = [k for k in required if k not in sec]
        if missing:
            raise AssertionError(f"foot/911.ini missing keys: {missing}")
        return {"ini": cp}

    if fid == 5:
        pairs = parse_ghostty(project_root / "ghostty/911")
        keys = {k for k, _ in pairs}
        for req in ("background", "foreground", "cursor-color", "selection-background", "selection-foreground"):
            if req not in keys:
                raise AssertionError(f"ghostty/911 missing key {req!r}")
        pal_indices = set()
        for k, v in pairs:
            if k == "palette" and "=" in v:
                idx_s, _ = v.split("=", 1)
                pal_indices.add(idx_s.strip())
        missing_pal = [str(i) for i in range(16) if str(i) not in pal_indices]
        if missing_pal:
            raise AssertionError(f"ghostty/911 missing palette indices: {missing_pal}")
        return {"pairs": pairs}

    if fid == 6:
        data = parse_toml(project_root / "alacritty/911.toml")
        colors = data.get("colors", {})
        for sec in ("primary", "cursor", "selection", "normal", "bright"):
            if sec not in colors or not isinstance(colors[sec], dict):
                raise AssertionError(f"alacritty/911.toml missing [colors.{sec}]")
        for ansi in ("black", "red", "green", "yellow", "blue", "magenta", "cyan", "white"):
            if ansi not in colors["normal"] or ansi not in colors["bright"]:
                raise AssertionError(f"alacritty/911.toml missing ANSI {ansi!r} in normal/bright")
        return data

    if fid == 7:
        kv = parse_kitty(project_root / "kitty/911.conf")
        req = (
            "foreground",
            "background",
            "selection_foreground",
            "selection_background",
            "cursor",
            "cursor_text_color",
        ) + tuple(f"color{i}" for i in range(16))
        missing = [k for k in req if k not in kv]
        if missing:
            raise AssertionError(f"kitty/911.conf missing keys: {missing}")
        return kv

    if fid == 8:
        text = (project_root / "tmux/911.conf").read_text(encoding="utf-8")
        req = (
            "status-style",
            "status-left",
            "status-right",
            "window-status-format",
            "window-status-current-format",
            "pane-border-style",
            "pane-active-border-style",
            "message-style",
            "mode-style",
            "clock-mode-colour",
        )
        missing = [k for k in req if k not in text]
        if missing:
            raise AssertionError(f"tmux/911.conf missing required options: {missing}")
        return {"text": text}

    if fid == 9:
        data = parse_toml(project_root / "herdr/911.toml")
        custom = data.get("theme", {}).get("custom")
        if not isinstance(custom, dict):
            raise AssertionError("herdr/911.toml missing [theme.custom]")
        req = ("accent", "sidebar_bg", "active_row_bg", "selection_bg", "panel_bg", "surface_dim", "red", "green", "yellow", "text")
        missing = [k for k in req if k not in custom]
        if missing:
            raise AssertionError(f"herdr/911.toml missing [theme.custom] keys: {missing}")
        return data

    if fid == 10:
        data = parse_toml(project_root / "starship/911.toml")
        if data.get("palette") != "911":
            raise AssertionError(f"starship/911.toml palette must be 'carrera', got {data.get('palette')!r}")
        pal = data.get("palettes", {}).get("911")
        if not isinstance(pal, dict) or len(pal) < 8:
            raise AssertionError("starship/911.toml missing populated [palettes.carrera]")
        return data

    if fid == 11:
        text = (project_root / "zsh-syntax-highlighting/911.zsh").read_text(encoding="utf-8")
        req = (
            "command",
            "builtin",
            "alias",
            "function",
            "single-quoted-argument",
            "double-quoted-argument",
            "comment",
            "unknown-token",
            "path",
            "globbing",
            "redirection",
        )
        missing = [k for k in req if k not in text]
        if missing or "ZSH_HIGHLIGHT_STYLES" not in text:
            raise AssertionError(f"zsh-syntax-highlighting/911.zsh missing keys: {missing}")
        return {"text": text}

    if fid == 12:
        text = (project_root / "fzf/911.sh").read_text(encoding="utf-8")
        if "FZF_DEFAULT_OPTS" not in text or "--color=" not in text:
            raise AssertionError("fzf/911.sh missing FZF_DEFAULT_OPTS or --color=")
        for k in ("bg:", "bg+:", "fg:", "fg+:", "hl:", "hl+:", "info:", "prompt:", "pointer:", "marker:", "spinner:", "header:", "border:"):
            if k not in text:
                raise AssertionError(f"fzf/911.sh missing fzf color key {k!r}")
        return {"text": text}

    if fid == 13:
        data = parse_toml(project_root / "atuin/911.toml")
        theme = data.get("theme")
        colors = data.get("colors")
        if not isinstance(theme, dict) or theme.get("name") != "911":
            raise AssertionError("atuin/911.toml missing [theme] name = 'carrera'")
        if not isinstance(colors, dict):
            raise AssertionError("atuin/911.toml missing [colors]")
        norm_keys = {k.replace("-", "").replace("_", "").lower() for k in colors}
        req = (
            "alertinfo",
            "alertwarn",
            "alerterror",
            "annotation",
            "base",
            "guidance",
            "important",
            "title",
            "muted",
            "syntaxcommand",
            "syntaxflag",
            "syntaxstring",
            "syntaxvariable",
            "syntaxoperator",
            "syntaxcomment",
        )
        missing = [k for k in req if k not in norm_keys]
        if missing:
            raise AssertionError(f"atuin/911.toml missing Meaning keys: {missing}")
        return data

    if fid == 14:
        data = parse_json(project_root / "opencode/911.json")
        if not isinstance(data.get("defs"), dict) or not isinstance(data.get("theme"), dict):
            raise AssertionError("opencode/911.json missing defs/theme objects")
        theme = data["theme"]
        defs = data["defs"]
        req = (
            "primary",
            "secondary",
            "accent",
            "error",
            "warning",
            "success",
            "info",
            "text",
            "textMuted",
            "background",
            "backgroundPanel",
            "backgroundElement",
            "border",
            "borderActive",
            "borderSubtle",
        )
        missing = [k for k in req if k not in theme]
        if missing:
            raise AssertionError(f"opencode/911.json missing theme keys: {missing}")
        if not any(k.startswith("diff") for k in theme) or not any(k.startswith("markdown") for k in theme) or not any(k.startswith("syntax") for k in theme):
            raise AssertionError("opencode/911.json missing diff*/markdown*/syntax* keys")
        for k, v in theme.items():
            refs = list(v.values()) if isinstance(v, dict) else [v]
            for r in refs:
                if isinstance(r, str) and not r.startswith("#") and r != "none" and r not in defs:
                    raise AssertionError(f"opencode/911.json dangling ref {k!r} -> {r!r}")
        return data

    if fid == 15:
        data = parse_json(project_root / "claude-code/911.json")
        if str(data.get("name", "")).lower() != "911" or data.get("base") != "dark":
            raise AssertionError("claude-code/911.json must have name='Carrera' and base='dark'")
        ov = data.get("overrides")
        if not isinstance(ov, dict):
            raise AssertionError("claude-code/911.json missing overrides")
        req = (
            "claude",
            "text",
            "inverseText",
            "subtle",
            "suggestion",
            "permission",
            "success",
            "error",
            "warning",
            "merged",
            "promptBorder",
            "planMode",
            "autoAccept",
            "bashBorder",
            "ide",
            "diffAdded",
            "diffRemoved",
            "userMessageBackground",
            "selectionBg",
            "rate_limit_fill",
        )
        missing = [k for k in req if k not in ov]
        if missing:
            raise AssertionError(f"claude-code/911.json missing overrides keys: {missing}")
        return data

    if fid == 16:
        data = parse_json(project_root / "pi/911.json")
        if str(data.get("name", "")).lower() != "911":
            raise AssertionError("pi/911.json must have name='carrera'")
        vars_d = data.get("vars")
        colors_d = data.get("colors")
        export_d = data.get("export")
        if not isinstance(vars_d, dict) or not isinstance(colors_d, dict) or not isinstance(export_d, dict):
            raise AssertionError("pi/911.json missing vars/colors/export objects")
        for k in ("pageBg", "cardBg", "infoBg"):
            if k not in export_d:
                raise AssertionError(f"pi/911.json export missing {k!r}")
        if len(colors_d) < 30:
            raise AssertionError(f"pi/911.json expected >=30 colors keys, got {len(colors_d)}")
        for section_name, mapping in (("colors", colors_d), ("export", export_d)):
            for k, v in mapping.items():
                if isinstance(v, str) and v not in ("", "none") and not v.startswith("#") and v not in vars_d:
                    raise AssertionError(f"pi/911.json {section_name}.{k} dangling var ref {v!r}")
        return data

    if fid == 17:
        data = parse_plist(project_root / "bat/911.tmTheme")
        if data.get("name") != "911":
            raise AssertionError(f"bat/911.tmTheme name must be 'Carrera', got {data.get('name')!r}")
        settings = data.get("settings")
        if not isinstance(settings, list) or len(settings) < 2:
            raise AssertionError("bat/911.tmTheme missing settings array")
        global_entry = next((s.get("settings") for s in settings if isinstance(s, dict) and "scope" not in s and isinstance(s.get("settings"), dict)), None)
        if not global_entry:
            raise AssertionError("bat/911.tmTheme missing global settings dict")
        for k in ("background", "foreground", "caret", "selection", "lineHighlight", "gutter", "gutterForeground"):
            if k not in global_entry:
                raise AssertionError(f"bat/911.tmTheme global settings missing {k!r}")
        scopes_str = " ".join(str(s.get("scope", "")) for s in settings if isinstance(s, dict))
        for sc in ("comment", "keyword", "string", "constant.numeric", "entity.name.function", "entity.name.type"):
            if sc not in scopes_str:
                raise AssertionError(f"bat/911.tmTheme missing scope {sc!r}")
        return data

    if fid == 18:
        cfg = parse_git_config(project_root / "delta/911.gitconfig")
        leaf_keys = {k.rsplit(".", 1)[-1] for k in cfg}
        req = (
            "plus-style",
            "plus-emph-style",
            "minus-style",
            "minus-emph-style",
            "line-numbers-plus-style",
            "line-numbers-minus-style",
            "line-numbers-zero-style",
            "file-style",
            "file-decoration-style",
            "hunk-header-style",
            "hunk-header-file-style",
            "hunk-header-line-number-style",
            "blame-palette",
        )
        missing = [k for k in req if k not in leaf_keys]
        if missing:
            raise AssertionError(f"delta/911.gitconfig missing keys: {missing}")
        return cfg

    if fid == 19:
        data = parse_yaml(project_root / "lazygit/911.yml")
        theme = data.get("gui", {}).get("theme")
        if not isinstance(theme, dict):
            raise AssertionError("lazygit/911.yml missing gui.theme")
        req = (
            "activeBorderColor",
            "inactiveBorderColor",
            "searchingActiveBorderColor",
            "optionsTextColor",
            "selectedLineBgColor",
            "inactiveViewSelectedLineBgColor",
            "cherryPickedCommitFgColor",
            "cherryPickedCommitBgColor",
            "markedBaseCommitFgColor",
            "unstagedChangesColor",
            "defaultFgColor",
        )
        missing = [k for k in req if k not in theme]
        if missing:
            raise AssertionError(f"lazygit/911.yml missing gui.theme keys: {missing}")
        return data

    if fid == 20:
        data = parse_yaml(project_root / "lazydocker/911.yml")
        theme = data.get("gui", {}).get("theme")
        if not isinstance(theme, dict):
            raise AssertionError("lazydocker/911.yml missing gui.theme")
        for k in ("activeBorderColor", "inactiveBorderColor", "selectedLineBgColor", "optionsTextColor"):
            if k not in theme:
                raise AssertionError(f"lazydocker/911.yml missing gui.theme.{k}")
        return data

    if fid == 21:
        data = parse_yaml(project_root / "eza/theme.yml")
        if data.get("colourful") is not True:
            raise AssertionError("eza/theme.yml must set colourful: true")
        for k in ("filekinds", "perms", "size", "users", "links", "git", "file_type"):
            if k not in data or not isinstance(data[k], dict):
                raise AssertionError(f"eza/theme.yml missing section {k!r}")
        return data

    if fid == 22:
        data = parse_yaml(project_root / "k9s/911.yaml")
        k9s = data.get("k9s")
        if not isinstance(k9s, dict):
            raise AssertionError("k9s/911.yaml missing top-level k9s key")
        for k in ("body", "prompt", "info", "dialog", "frame", "views"):
            if k not in k9s:
                raise AssertionError(f"k9s/911.yaml missing k9s.{k}")
        for fk in ("border", "menu", "crumbs", "status", "title"):
            if fk not in k9s["frame"]:
                raise AssertionError(f"k9s/911.yaml missing k9s.frame.{fk}")
        for vk in ("charts", "table", "xray", "yaml", "logs"):
            if vk not in k9s["views"]:
                raise AssertionError(f"k9s/911.yaml missing k9s.views.{vk}")
        return data

    if fid == 23:
        data = parse_yaml(project_root / "kubecolor/color.yaml")
        if data.get("preset") != "dark":
            raise AssertionError("kubecolor/color.yaml must have preset: dark")
        theme = data.get("theme", {})
        base = theme.get("base", {})
        for k in ("info", "primary", "secondary", "success", "warning", "danger", "muted", "key"):
            if k not in base:
                raise AssertionError(f"kubecolor/color.yaml missing theme.base.{k}")
        for k in ("table", "data"):
            if k not in theme:
                raise AssertionError(f"kubecolor/color.yaml missing theme.{k}")
        return data

    if fid == 24:
        cp = parse_ini(project_root / "pgcli/911.pgclirc")
        if not cp.has_section("colors"):
            raise AssertionError("pgcli/911.pgclirc missing [colors] section")
        sec = cp["colors"]
        req = (
            "completion-menu.completion.current",
            "completion-menu.completion",
            "selected",
            "search",
            "search.current",
            "bottom-toolbar",
            "bottom-toolbar.on",
            "bottom-toolbar.off",
            "bottom-toolbar.transaction.valid",
            "bottom-toolbar.transaction.failed",
        )
        missing = [k for k in req if k not in sec]
        if missing:
            raise AssertionError(f"pgcli/911.pgclirc missing [colors] keys: {missing}")
        return {"ini": cp}

    if fid == 25:
        p = project_root / "cliamp/911.toml"
        if p.name == "default.toml":
            raise AssertionError("cliamp theme must not be named default.toml")
        data = parse_toml(p)
        req = ("bg", "accent", "bright_fg", "fg", "green", "yellow", "red")
        missing = [k for k in req if k not in data]
        if missing:
            raise AssertionError(f"cliamp/911.toml missing required keys: {missing}")
        return data

    if fid == 26:
        data = parse_jsonc(project_root / "fastfetch/911.jsonc")
        color = data.get("display", {}).get("color")
        if not isinstance(color, dict):
            raise AssertionError("fastfetch/911.jsonc missing display.color")
        for k in ("keys", "title", "separator", "output"):
            if k not in color:
                raise AssertionError(f"fastfetch/911.jsonc missing display.color.{k}")
        return data

    if fid == 27:
        data = parse_btop_theme(project_root / "btop/911.theme")
        if len(data) < 41:
            raise AssertionError(f"btop/911.theme expected >=41 keys, got {len(data)}")
        for k in ("main_bg", "main_fg", "title", "hi_fg", "selected_bg", "selected_fg", "div_line"):
            if k not in data:
                raise AssertionError(f"btop/911.theme missing key {k!r}")
        return data

    if fid == 28:
        pkg = parse_json(project_root / "vscode/package.json")
        for k in ("name", "displayName", "version", "engines", "contributes"):
            if k not in pkg:
                raise AssertionError(f"vscode/package.json missing {k!r}")
        if "vscode" not in pkg["engines"]:
            raise AssertionError("vscode/package.json missing engines.vscode")
        themes = pkg["contributes"].get("themes", [])
        if not themes or themes[0].get("uiTheme") != "vs-dark":
            raise AssertionError("vscode/package.json contributes.themes[0].uiTheme must be 'vs-dark'")
        rel_path = themes[0].get("path", "")
        resolved = (project_root / "vscode" / rel_path).resolve()
        if not resolved.is_file():
            raise AssertionError(f"vscode/package.json theme path does not exist: {rel_path}")
        theme_data = parse_json(resolved)
        if theme_data.get("type") != "dark":
            raise AssertionError("vscode theme type must be 'dark'")
        for k in ("colors", "tokenColors", "semanticTokenColors"):
            if k not in theme_data:
                raise AssertionError(f"vscode theme missing {k!r}")
        return {"package": pkg, "theme": theme_data}

    if fid == 29:
        man = parse_json(project_root / "obsidian/911/manifest.json")
        if man.get("name") != "911":
            raise AssertionError("obsidian/911/manifest.json name must be 'Carrera'")
        for k in ("version", "minAppVersion", "author"):
            if k not in man:
                raise AssertionError(f"obsidian/911/manifest.json missing {k!r}")
        css = validate_css((project_root / "obsidian/911/theme.css").read_text(encoding="utf-8"))
        if not any(".theme-dark" in s for s in css["selectors"]):
            raise AssertionError("obsidian/911/theme.css missing .theme-dark selector")
        req_vars = (
            "--background-primary",
            "--background-secondary",
            "--text-normal",
            "--text-selection",
            "--background-modifier-border",
            "--text-title-h1",
            "--text-title-h6",
            "--text-link",
            "--text-accent",
            "--interactive-accent",
            "--code-normal",
            "--text-error",
            "--text-success",
        )
        missing = [v for v in req_vars if v not in css["variables"]]
        if missing:
            raise AssertionError(f"obsidian/911/theme.css missing CSS variables: {missing}")
        return {"manifest": man, "css": css}

    if fid == 30:
        man = parse_json(project_root / "chromium/manifest.json")
        if man.get("manifest_version") != 3:
            raise AssertionError("chromium/manifest.json manifest_version must be 3")
        for k in ("name", "version", "theme"):
            if k not in man:
                raise AssertionError(f"chromium/manifest.json missing {k!r}")
        colors = man["theme"].get("colors", {})
        for k in ("frame", "toolbar", "tab_text", "tab_background_text", "bookmark_text", "ntp_background", "ntp_text"):
            if k not in colors:
                raise AssertionError(f"chromium/manifest.json missing theme.colors.{k}")
        csv_text = (project_root / "chromium/chromium.theme").read_text(encoding="utf-8").strip()
        try:
            csv_parts = [int(x.strip()) for x in csv_text.split(",")]
        except ValueError as exc:
            raise AssertionError(f"chromium/chromium.theme must be R,G,B integers, got {csv_text!r}") from exc
        if len(csv_parts) != 3 or any(not (0 <= c <= 255) for c in csv_parts):
            raise AssertionError(f"chromium/chromium.theme must be valid 0..255 R,G,B CSV, got {csv_text!r}")
        return {"manifest": man, "csv": csv_text}

    if fid == 31:
        uc = validate_css((project_root / "zen-browser/userChrome.css").read_text(encoding="utf-8"))
        ucon = validate_css((project_root / "zen-browser/userContent.css").read_text(encoding="utf-8"))
        if not any(":root" in s for s in uc["selectors"]):
            raise AssertionError("zen-browser/userChrome.css missing :root selector")
        for v in (
            "--zen-primary-color",
            "--zen-main-browser-background",
            "--zen-dialog-background",
            "--zen-urlbar-background",
            "--toolbar-bgcolor",
            "--toolbar-color",
        ):
            if v not in uc["variables"]:
                raise AssertionError(f"zen-browser/userChrome.css missing variable {v!r}")
        if not ucon["variables"] and not ucon["declarations"]:
            raise AssertionError("zen-browser/userContent.css has no rules")
        return {"userChrome": uc, "userContent": ucon}

    if fid == 32:
        cp = parse_ini(project_root / "imv/911.ini")
        if not cp.has_section("options"):
            raise AssertionError("imv/911.ini missing [options] section")
        sec = cp["options"]
        for k in ("background", "overlay_text_color", "overlay_background_color"):
            if k not in sec:
                raise AssertionError(f"imv/911.ini missing [options].{k}")
        return {"ini": cp}

    if fid == 33:
        kv = parse_mpv_conf(project_root / "mpv/mpv.conf")
        for k in ("background-color", "osd-color", "osd-back-color", "osd-selected-color"):
            if k not in kv:
                raise AssertionError(f"mpv/mpv.conf missing option {k!r}")
        if "osd-outline-color" not in kv and "osd-border-color" not in kv:
            raise AssertionError("mpv/mpv.conf missing option 'osd-outline-color' (or alias 'osd-border-color')")
        return kv

    if fid == 34:
        css = validate_css((project_root / "gtk/gtk.css").read_text(encoding="utf-8"))
        dc = css["define_colors"]
        req = (
            "window_bg_color",
            "window_fg_color",
            "view_bg_color",
            "view_fg_color",
            "headerbar_bg_color",
            "headerbar_fg_color",
            "accent_bg_color",
            "accent_color",
            "card_bg_color",
            "popover_bg_color",
            "dialog_bg_color",
        )
        missing = [k for k in req if k not in dc]
        if missing:
            raise AssertionError(f"gtk/gtk.css missing @define-color tokens: {missing}")
        return css

    if fid == 35:
        cp = parse_ini(project_root / "fcitx5/911/theme.conf")
        for sec in (
            "Metadata",
            "InputPanel",
            "InputPanel/Background",
            "InputPanel/Highlight",
            "Menu",
            "Menu/Background",
            "Menu/Highlight",
            "Menu/Separator",
        ):
            if not cp.has_section(sec):
                raise AssertionError(f"fcitx5/911/theme.conf missing [{sec}]")
        for k in ("Name", "Version"):
            if k not in cp["Metadata"]:
                raise AssertionError(f"fcitx5/911/theme.conf [Metadata] missing {k!r}")
        for k in ("NormalColor", "HighlightCandidateColor", "HighlightColor", "HighlightBackgroundColor"):
            if k not in cp["InputPanel"]:
                raise AssertionError(f"fcitx5/911/theme.conf [InputPanel] missing {k!r}")
        return {"ini": cp}

    if fid == 36:
        secs = parse_hyprland_conf(project_root / "hyprland/911.conf")
        if "general" not in secs or "group" not in secs:
            raise AssertionError("hyprland/911.conf must have general {} and group {} sections")
        for k in ("col.active_border", "col.inactive_border"):
            if k not in secs["general"]:
                raise AssertionError(f"hyprland/911.conf general missing {k!r}")
        for k in ("col.border_active", "col.border_inactive"):
            if k not in secs["group"]:
                raise AssertionError(f"hyprland/911.conf group missing {k!r}")
        return secs

    if fid == 37:
        css = validate_css(
            (project_root / "hyprland-preview-share-picker/style.css").read_text(encoding="utf-8")
        )
        dc = css["define_colors"]
        for k in ("foreground", "background", "accent", "muted", "card_bg", "accent_ink", "accent_hover", "selected_tab", "text"):
            if k not in dc:
                raise AssertionError(f"hyprland-preview-share-picker/style.css missing @define-color {k!r}")
        joined_sel = " ".join(css["selectors"])
        for sel in (".window", ".card", ".region-button"):
            if sel not in joined_sel:
                raise AssertionError(f"hyprland-preview-share-picker/style.css missing selector {sel!r}")
        return css

    raise ValueError(f"Unknown feature_id {fid}")


def validate_deliverable_palette(
    spec: DeliverableSpec, project_root: Path, palette: PaletteContract
) -> list[str]:
    """Extract all color encodings from deliverable and verify Palette Contract + anchor colors."""
    fid = spec.feature_id
    app = spec.app_dir
    errors: list[str] = []

    if fid == 1:
        data = parse_toml(project_root / "colors.toml")
        for k, v in data.items():
            if isinstance(v, str) and v.startswith("#"):
                if not HEX6_RE.match(v) or v.lower() not in palette.base_hexes:
                    errors.append(f"colors.toml {k}={v!r} invalid")
        return errors

    if fid == 2:
        info = validate_tdesktop_theme(project_root / "telegram/911.tdesktop-theme")
        legacy_carrera = {
            "#15171a", "#e1656c", "#d6d2c7", "#74a0d7",
            "#89b87f", "#6fc7cb", "#dcbb6a", "#b886b8", "#ae7e62",
        }
        for hx in info["hexes"]:
            if hx[:7].lower() in legacy_carrera:
                errors.append(f"telegram contains legacy Carrera v2 hex {hx!r}")
        entries = info["entries"]
        if "windowBg" not in entries:
            errors.append("telegram missing required windowBg key")
        else:
            cur = entries["windowBg"]
            while not cur.startswith("#"):
                cur = entries[cur]
            if cur[:7].lower() != palette.background:
                errors.append(
                    f"telegram windowBg (resolved {entries['windowBg']!r} -> {cur!r}) != {palette.background}"
                )
        return errors

    if fid == 3:
        text = (project_root / "neovim/colors/911.lua").read_text(encoding="utf-8")
        valid, malformed = extract_lua_hex_literals(text)
        if malformed:
            errors.append(f"neovim malformed hex literals: {malformed}")
        errors.extend(_check_hex_values(valid, palette, app))
        if palette.background not in valid or palette.foreground not in valid or palette.accent not in valid:
            errors.append("neovim missing core Carrera anchor colors (background/foreground/accent)")
        return errors

    if fid == 4:
        cp = parse_ini(project_root / "foot/911.ini")
        all_sections: list[tuple[str, Any]] = [(s, cp[s]) for s in cp.sections()]
        if cp.defaults():
            all_sections.append(("DEFAULT", cp.defaults()))
        for sec_name, sec_map in all_sections:
            is_color_sec = sec_name == "DEFAULT" or sec_name.lower().startswith("colors")
            for k, v in sec_map.items():
                if k in ("alpha", "flash-alpha"):
                    continue
                tokens = v.split()
                if is_color_sec:
                    expected_len = 2 if k in FOOT_TWO_HEX_KEYS else 1
                    if len(tokens) != expected_len:
                        errors.append(
                            f"foot [{sec_name}] {k}={v!r} expected {expected_len} hex token(s)"
                        )
                    for tok in tokens:
                        if tok.startswith("#"):
                            errors.append(f"foot [{sec_name}] {k}={v!r} MUST NOT have '#' prefix")
                        elif not BARE_HEX6_RE.match(tok):
                            errors.append(f"foot [{sec_name}] {k}={v!r} invalid bare 6-hex")
                        else:
                            errors.extend(_check_hex_values(["#" + tok], palette, app))
                else:
                    for tok in tokens:
                        if "#" in tok:
                            errors.append(f"foot [{sec_name}] {k}={v!r} MUST NOT contain '#'")
                        elif BARE_HEX6_RE.match(tok):
                            errors.extend(_check_hex_values(["#" + tok], palette, app))
        sec = cp["colors-dark"]
        if sec["background"].lower() != palette.background[1:] or sec["foreground"].lower() != palette.foreground[1:]:
            errors.append("foot background/foreground anchor mismatch")
        return errors

    if fid == 5:
        pairs = parse_ghostty(project_root / "ghostty/911")
        kv = dict(pairs)
        for k, v in pairs:
            if k == "palette" and "=" in v:
                _, col = v.split("=", 1)
                errors.extend(_check_hex_values([col.strip()], palette, app))
            elif v.startswith("#") or k in ("background", "foreground", "cursor-color", "cursor-text", "selection-background", "selection-foreground"):
                errors.extend(_check_hex_values([v], palette, app))
        if kv.get("background", "").lower() != palette.background or kv.get("foreground", "").lower() != palette.foreground:
            errors.append("ghostty background/foreground anchor mismatch")
        if kv.get("cursor-color", "").lower() not in palette.valid_cursors:
            errors.append(f"ghostty cursor-color={kv.get('cursor-color')!r} invalid")
        return errors

    if fid == 6:
        data = parse_toml(project_root / "alacritty/911.toml")
        colors = data["colors"]
        for s in walk_strings(colors):
            errors.extend(_check_hex_values([s], palette, app))
        if colors["primary"]["background"].lower() != palette.background or colors["primary"]["foreground"].lower() != palette.foreground:
            errors.append("alacritty primary background/foreground anchor mismatch")
        return errors

    if fid == 7:
        kv = parse_kitty(project_root / "kitty/911.conf")
        for k, v in kv.items():
            if v.startswith("#") or k in ("foreground", "background", "cursor", "cursor_text_color", "selection_foreground", "selection_background") or k.startswith("color"):
                errors.extend(_check_hex_values([v], palette, app))
        if kv["background"].lower() != palette.background or kv["foreground"].lower() != palette.foreground:
            errors.append("kitty background/foreground anchor mismatch")
        return errors

    if fid == 8:
        text = (project_root / "tmux/911.conf").read_text(encoding="utf-8")
        lines = [l for l in text.splitlines() if not l.lstrip().startswith("#")]
        code = "\n".join(lines)
        for m in GENERIC_HEX_RE.finditer(code):
            errors.extend(_check_hex_values([m.group(0)], palette, app))
        for m in re.finditer(r"\b(?:fg|bg)=([^\s,'\",\]};]+)", code):
            val = m.group(1).strip()
            if not HEX6_RE.match(val):
                errors.append(f"tmux style {m.group(0)!r} must use #rrggbb (no named/indexed colors)")
            else:
                errors.extend(_check_hex_values([val], palette, app))
        for m in re.finditer(r"-(?:colour|color)\s+[\"']?([^\s\"';]+)[\"']?", code):
            val = m.group(1).strip()
            if not HEX6_RE.match(val):
                errors.append(f"tmux colour option {m.group(0)!r} must use #rrggbb (no named/indexed colors)")
            else:
                errors.extend(_check_hex_values([val], palette, app))
        has_bg_plane = palette.background in code.lower() or "#131519" in code.lower()
        if not has_bg_plane or palette.foreground not in code.lower() or palette.accent not in code.lower():
            errors.append("tmux missing core anchor colors")
        return errors

    if fid == 9:
        data = parse_toml(project_root / "herdr/911.toml")
        for k, v in data["theme"]["custom"].items():
            if not isinstance(v, str) or not HEX6_RE.match(v):
                errors.append(f"herdr [theme.custom].{k}={v!r} must be #rrggbb")
            else:
                errors.extend(_check_hex_values([v], palette, app))
        if data["theme"]["custom"]["accent"].lower() not in (palette.accent, "#bf3b3e"):
            errors.append("herdr accent anchor mismatch")
        return errors

    if fid == 10:
        data = parse_toml(project_root / "starship/911.toml")
        pal = data["palettes"]["911"]
        for k, v in pal.items():
            if not isinstance(v, str) or not HEX6_RE.match(v):
                errors.append(f"starship palettes.carrera.{k}={v!r} must be #rrggbb")
            else:
                errors.extend(_check_hex_values([v], palette, app))
        _check_strings_hash_tokens(walk_strings(data), palette, app, errors)
        return errors

    if fid == 11:
        text = (project_root / "zsh-syntax-highlighting/911.zsh").read_text(encoding="utf-8")
        code = "\n".join(l for l in text.splitlines() if not l.lstrip().startswith("#"))
        for m in re.finditer(r"\b(?:fg|bg)=([^\s,'\"]+)", code):
            val = m.group(1).strip()
            if not HEX6_RE.match(val):
                errors.append(f"zsh-syntax-highlighting style {m.group(0)!r} must use #rrggbb (no named/indexed colors)")
        cleaned_code = URL_RE.sub("", code)
        hexes: list[str] = []
        for m in re.finditer(r"(?<![A-Za-z0-9_${])#([0-9A-Za-z]+)", cleaned_code):
            tok = "#" + m.group(1)
            if HEX6_RE.match(tok):
                hexes.append(tok.lower())
            else:
                errors.append(f"Malformed hex color {tok!r} in zsh-syntax-highlighting")
        if not hexes:
            errors.append("zsh-syntax-highlighting contains no hex colors")
        errors.extend(_check_hex_values(hexes, palette, app))
        return errors

    if fid == 12:
        text = (project_root / "fzf/911.sh").read_text(encoding="utf-8")
        code = "\n".join(l for l in text.splitlines() if not l.lstrip().startswith("#"))
        hexes = [m.group(0) for m in GENERIC_HEX_RE.finditer(code)]
        if not hexes:
            errors.append("fzf contains no hex colors")
        errors.extend(_check_hex_values(hexes, palette, app))
        if palette.background not in [h.lower() for h in hexes] or palette.foreground not in [h.lower() for h in hexes]:
            errors.append("fzf missing background/foreground anchor colors")
        return errors

    if fid == 13:
        data = parse_toml(project_root / "atuin/911.toml")
        for k, v in data["colors"].items():
            if not isinstance(v, str) or not HEX6_RE.match(v):
                errors.append(f"atuin [colors].{k}={v!r} must be #rrggbb")
            else:
                errors.extend(_check_hex_values([v], palette, app))
        return errors

    if fid == 14:
        data = parse_json(project_root / "opencode/911.json")
        hexes = _check_strings_hash_tokens(walk_strings(data), palette, app, errors)
        if not hexes:
            errors.append("opencode/911.json contains no hex colors")
        return errors

    if fid == 15:
        data = parse_json(project_root / "claude-code/911.json")
        for k, v in data["overrides"].items():
            if not isinstance(v, str) or not HEX6_RE.match(v):
                errors.append(f"claude-code overrides.{k}={v!r} must be #rrggbb")
            else:
                errors.extend(_check_hex_values([v], palette, app))
        return errors

    if fid == 16:
        data = parse_json(project_root / "pi/911.json")
        hexes = _check_strings_hash_tokens(walk_strings(data), palette, app, errors)
        if not hexes:
            errors.append("pi/911.json contains no hex colors")
        return errors

    if fid == 17:
        data = parse_plist(project_root / "bat/911.tmTheme")
        hexes = _check_strings_hash_tokens(walk_strings(data["settings"]), palette, app, errors)
        if not hexes:
            errors.append("bat/911.tmTheme contains no hex colors")
        return errors

    if fid == 18:
        cfg = parse_git_config(project_root / "delta/911.gitconfig")
        hexes = _check_strings_hash_tokens(list(cfg.values()), palette, app, errors)
        if not hexes:
            errors.append("delta/911.gitconfig contains no hex colors")
        return errors

    if fid in (19, 20, 21, 22, 23):
        rel = spec.theme_files[0]
        data = parse_yaml(project_root / rel)
        hexes = _check_strings_hash_tokens(walk_strings(data), palette, app, errors)
        if not hexes:
            errors.append(f"{rel} contains no hex colors")
        return errors

    if fid == 24:
        cp = parse_ini(project_root / "pgcli/911.pgclirc")
        all_vals = [v for sec_name in cp.sections() for v in cp[sec_name].values()]
        hexes = _check_strings_hash_tokens(all_vals, palette, app, errors)
        if not hexes:
            errors.append("pgcli/911.pgclirc contains no hex colors")
        return errors

    if fid == 25:
        data = parse_toml(project_root / "cliamp/911.toml")
        for k in ("bg", "accent", "bright_fg", "fg", "green", "yellow", "red"):
            v = data[k]
            if not isinstance(v, str) or not HEX6_RE.match(v):
                errors.append(f"cliamp {k}={v!r} must strictly match ^#[0-9a-fA-F]{{6}}$")
            else:
                errors.extend(_check_hex_values([v], palette, app))
        if data["bg"].lower() != palette.background or data["fg"].lower() != palette.foreground or data["accent"].lower() != palette.accent:
            errors.append("cliamp anchor color mismatch")
        return errors

    if fid == 26:
        data = parse_jsonc(project_root / "fastfetch/911.jsonc")
        disp_hexes = _check_strings_hash_tokens(
            walk_strings(data.get("display", {}).get("color", {})), palette, app, []
        )
        if not disp_hexes:
            errors.append("fastfetch/911.jsonc display.color has no hex colors")
        _check_strings_hash_tokens(walk_strings(data), palette, app, errors)
        return errors

    if fid == 27:
        data = parse_btop_theme(project_root / "btop/911.theme")
        errors.extend(_check_hex_values(list(data.values()), palette, app))
        if data["main_bg"] != palette.background or data["main_fg"] != palette.foreground or data["hi_fg"] != palette.accent:
            errors.append("btop anchor color mismatch")
        return errors

    if fid == 28:
        pkg = parse_json(project_root / "vscode/package.json")
        rel_path = pkg["contributes"]["themes"][0]["path"]
        theme = parse_json((project_root / "vscode" / rel_path).resolve())
        hexes = _check_strings_hash_tokens(walk_strings(theme), palette, app, errors)
        if not hexes:
            errors.append("vscode theme contains no hex colors")
        return errors

    if fid in (29, 31, 34, 37):
        for rel in spec.theme_files:
            css = validate_css((project_root / rel).read_text(encoding="utf-8"))
            errors.extend(_check_hex_values(css["hexes"], palette, app))
            for rgb in css["rgb_tuples"]:
                ok, reason = palette.is_allowed_rgb_tuple(rgb, app)
                if not ok:
                    errors.append(f"{rel}: {reason}")
        return errors

    if fid == 30:
        man = parse_json(project_root / "chromium/manifest.json")
        for k, arr in man["theme"]["colors"].items():
            if not isinstance(arr, list) or len(arr) not in (3, 4):
                errors.append(f"chromium theme.colors.{k}={arr!r} must be [r,g,b] or [r,g,b,a]")
                continue
            rgb = arr[:3]
            if not all(isinstance(c, int) and not isinstance(c, bool) and 0 <= c <= 255 for c in rgb):
                errors.append(f"chromium theme.colors.{k}={arr!r} channels must be ints 0..255")
                continue
            if len(arr) == 4 and (not isinstance(arr[3], (int, float)) or isinstance(arr[3], bool) or not (0.0 <= arr[3] <= 1.0)):
                errors.append(f"chromium theme.colors.{k}={arr!r} alpha must be 0..1")
                continue
            ok, reason = palette.is_allowed_rgb_tuple((rgb[0], rgb[1], rgb[2]), app)
            if not ok:
                errors.append(f"chromium theme.colors.{k}: {reason}")
        csv_text = (project_root / "chromium/chromium.theme").read_text(encoding="utf-8").strip()
        expected_csv = ",".join(map(str, hex_to_rgb(palette.background)))
        if csv_text != expected_csv:
            errors.append(f"chromium/chromium.theme {csv_text!r} != {expected_csv!r}")
        return errors

    if fid == 32:
        cp = parse_ini(project_root / "imv/911.ini")
        all_sections: list[tuple[str, Any]] = [(s, cp[s]) for s in cp.sections()]
        if cp.defaults():
            all_sections.append(("DEFAULT", cp.defaults()))
        for sec_name, sec_map in all_sections:
            for k, v in sec_map.items():
                if "#" in v:
                    errors.append(f"imv [{sec_name}] {k}={v!r} MUST NOT have '#' prefix")
                    continue
                is_color_key = (
                    k in ("background", "foreground", "overlay_text_color", "overlay_background_color")
                    or k.endswith("_color")
                    or k.endswith("color")
                    or sec_name.lower().startswith("colors")
                )
                if is_color_key:
                    if not BARE_HEX6_RE.match(v):
                        errors.append(f"imv [{sec_name}] {k}={v!r} invalid bare 6-hex")
                    else:
                        errors.extend(_check_hex_values(["#" + v], palette, app))
                elif BARE_HEX6_RE.match(v):
                    errors.extend(_check_hex_values(["#" + v], palette, app))
        sec = cp["options"]
        if sec["background"].lower() != palette.background[1:]:
            errors.append("imv background anchor mismatch")
        return errors

    if fid == 33:
        kv = parse_mpv_conf(project_root / "mpv/mpv.conf")
        for k, v in kv.items():
            if k.endswith("-color"):
                if not (HEX6_RE.match(v) or HEX8_RE.match(v)):
                    errors.append(f"mpv {k}={v!r} must be #rrggbb or #aarrggbb (no float r/g/b or named color)")
                else:
                    # mpv 8-hex is #AARRGGBB (alpha first!)
                    errors.extend(_check_hex_values([v], palette, app, allow_mpv_argb=True))
            elif v.startswith("#"):
                errors.extend(_check_hex_values([v], palette, app, allow_mpv_argb=True))
            elif re.fullmatch(r"\d+(?:\.\d+)?(?:/\d+(?:\.\d+)?){2,3}", v):
                errors.append(f"mpv {k}={v!r} float r/g/b color format is disallowed; use #rrggbb or #aarrggbb")
        return errors

    if fid == 35:
        cp = parse_ini(project_root / "fcitx5/911/theme.conf")
        for sec_name in cp.sections():
            for k, v in cp[sec_name].items():
                for m in GENERIC_HEX_RE.finditer(v):
                    errors.extend(_check_hex_values([m.group(0)], palette, app))
        return errors

    if fid == 36:
        secs = parse_hyprland_conf(project_root / "hyprland/911.conf")
        found = 0
        for sec_dict in secs.values():
            for k, v in sec_dict.items():
                for m in HYPR_RGBA_RE.finditer(v):
                    found += 1
                    errors.extend(_check_hex_values(["#" + m.group(1)], palette, app))
                for m in HYPR_HEX_INT_RE.finditer(v):
                    found += 1
                    # 0xAARRGGBB -> RGB is slice [4:10]
                    errors.extend(_check_hex_values(["#" + m.group(0)[4:10]], palette, app))
                for m in GENERIC_HEX_RE.finditer(v):
                    found += 1
                    errors.extend(_check_hex_values([m.group(0)], palette, app))
        if found == 0:
            errors.append("hyprland/911.conf contains no rgba()/hex colors")
        return errors

    raise ValueError(f"Unknown feature_id {fid}")
