"""Carrera v2.0.0 Palette Contract loader and color validation rules."""

from __future__ import annotations

import re
import tomllib
from functools import lru_cache
from pathlib import Path

HEX6_RE = re.compile(r"^#[0-9a-fA-F]{6}$")
HEX8_RE = re.compile(r"^#[0-9a-fA-F]{8}$")
BARE_HEX6_RE = re.compile(r"^[0-9a-fA-F]{6}$")
HYPR_RGBA_RE = re.compile(r"rgba?\(([0-9a-fA-F]{6})([0-9a-fA-F]{2})?\)")
CSS_RGB_FUNC_RE = re.compile(
    r"rgba?\(\s*([0-9]{1,3})\s*[,\s]\s*([0-9]{1,3})\s*[,\s]\s*([0-9]{1,3})"
    r"(?:\s*[,/]\s*([0-9]*\.?[0-9]+%?))?\s*\)",
    re.IGNORECASE,
)

# Documented opaque diff/surface hexes from PROJECT.md § Palette Contract
DOC_DERIVED_HEXES: frozenset[str] = frozenset(
    {
        "#222a23",  # diff add
        "#2d1e20",  # diff delete
        "#202731",  # diff change
        "#2b3646",  # diff text
    }
)

# Fallback reference btop dividers if sibling btop.theme is absent under custom path
DEFAULT_BTOP_DIVIDERS: frozenset[str] = frozenset({"#31353f", "#454954"})

# Schemas allowed to use DOC_DERIVED_HEXES and linear-RGB mix(c1, c2, p%) closures
BLENDED_SURFACE_APPS: frozenset[str] = frozenset(
    {
        "claude-code",
        "pi",
        "delta",
        "opencode",
        "neovim",
        "telegram",
        "bat",
        "vscode",
        "obsidian",
        "zen-browser",
        "gtk",
    }
)

# Direct-palette apps restricted strictly to BASE_HEXES (no derived blends)
DIRECT_PALETTE_APPS: frozenset[str] = frozenset(
    {
        "foot",
        "ghostty",
        "alacritty",
        "kitty",
        "tmux",
        "herdr",
        "starship",
        "zsh-syntax-highlighting",
        "fzf",
        "atuin",
        "lazygit",
        "lazydocker",
        "eza",
        "cliamp",
        "k9s",
        "kubecolor",
        "pgcli",
        "fastfetch",
        "btop",
        "imv",
        "mpv",
        "fcitx5",
        "hyprland",
        "hyprland-preview-share-picker",
        "chromium",
    }
)

REQUIRED_COLORS_TOML_KEYS: tuple[str, ...] = (
    "mode",
    "accent",
    "cursor",
    "selection",
    "selection_background",
    "selection_foreground",
    "muted",
    "background",
    "dark_background",
    "darker_background",
    "lighter_background",
    "foreground",
    "dark_foreground",
    "light_foreground",
    "bright_foreground",
    "hyprland_active_border",
    "hyprland_inactive_border",
    "red",
    "orange",
    "yellow",
    "green",
    "cyan",
    "blue",
    "magenta",
    "brown",
    "bright_red",
    "bright_yellow",
    "bright_green",
    "bright_cyan",
    "bright_blue",
    "bright_magenta",
)


def hex_to_rgb(hex_color: str) -> tuple[int, int, int]:
    h = hex_color.lstrip("#")
    if len(h) != 6:
        raise ValueError(f"Expected 6-digit hex color, got {hex_color!r}")
    return (int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16))


def rgb_to_hex(r: int, g: int, b: int) -> str:
    for ch in (r, g, b):
        if not (0 <= ch <= 255):
            raise ValueError(f"RGB channel out of range 0..255: {(r, g, b)}")
    return f"#{r:02x}{g:02x}{b:02x}"


class PaletteContract:
    """Authoritative Carrera v2.0.0 palette loaded from reference colors.toml."""

    def __init__(self, reference_colors_path: Path) -> None:
        self.reference_colors_path = reference_colors_path
        with open(reference_colors_path, "rb") as f:
            self.raw_toml: dict[str, object] = tomllib.load(f)

        self.tokens: dict[str, str] = {}
        base_set: set[str] = set()

        for key in REQUIRED_COLORS_TOML_KEYS:
            if key not in self.raw_toml:
                raise ValueError(
                    f"Reference colors.toml missing required key {key!r}: {reference_colors_path}"
                )

        for key, val in self.raw_toml.items():
            if not isinstance(val, str):
                continue
            if HEX6_RE.match(val):
                norm = val.lower()
                self.tokens[key] = norm
                base_set.add(norm)
            elif key.startswith("hyprland_"):
                for match in HYPR_RGBA_RE.finditer(val):
                    base_set.add(f"#{match.group(1).lower()}")

        # Load btop.theme dividers (#31353f, #454954) dynamically if sibling exists
        btop_path = reference_colors_path.parent / "btop.theme"
        if btop_path.is_file():
            btop_text = btop_path.read_text(encoding="utf-8")
            for m in re.finditer(
                r'^theme\[[a-z_]+\]="(#[0-9a-fA-F]{6})"$', btop_text, re.MULTILINE
            ):
                base_set.add(m.group(1).lower())
        else:
            base_set.update(DEFAULT_BTOP_DIVIDERS)

        self.base_hexes: frozenset[str] = frozenset(base_set)
        self.doc_derived_hexes: frozenset[str] = DOC_DERIVED_HEXES
        self._base_rgbs: tuple[tuple[int, int, int], ...] = tuple(
            hex_to_rgb(h) for h in sorted(self.base_hexes)
        )
        # Documented surface-blending base canvases (PROJECT.md § Derivation Rules:
        # alpha-over-#15171a background and recessed #101215 dark_background).
        self._surface_rgbs: tuple[tuple[int, int, int], ...] = (
            hex_to_rgb(self.tokens["background"]),
            hex_to_rgb(self.tokens["dark_background"]),
        )

    @property
    def background(self) -> str:
        return self.tokens["background"]

    @property
    def foreground(self) -> str:
        return self.tokens["foreground"]

    @property
    def accent(self) -> str:
        return self.tokens["accent"]

    @property
    def valid_cursors(self) -> frozenset[str]:
        # Both #e1656c (colors.toml cursor/accent) and #eae6dc (omarchy-theme-color cursor)
        return frozenset({self.tokens["cursor"], self.tokens["bright_foreground"]})

    @lru_cache(maxsize=4096)
    def is_linear_mix(self, hex6: str) -> bool:
        """Return True iff hex6 is BASE_HEXES, DOC_DERIVED_HEXES, or alpha-over-dark-surface tint (p in 1..60)."""
        norm = hex6.lower()
        if norm in self.base_hexes or norm in self.doc_derived_hexes:
            return True
        target = hex_to_rgb(norm)
        for bg in self._surface_rgbs:
            for fg in self._base_rgbs:
                if bg == fg:
                    continue
                # Quick bounding-box prune per channel (tolerance <= 1)
                if not all(
                    min(bg[ch], fg[ch]) - 1 <= target[ch] <= max(bg[ch], fg[ch]) + 1
                    for ch in range(3)
                ):
                    continue
                for p in range(1, 61):
                    if all(
                        abs(target[ch] - (bg[ch] + (fg[ch] - bg[ch]) * p / 100.0)) <= 1.0
                        for ch in range(3)
                    ):
                        return True
        return False

    def is_allowed_hex(self, hex_value: str, app_name: str, *, allow_mpv_argb: bool = False) -> tuple[bool, str]:
        """Validate a #rrggbb, #rrggbbaa, or (for mpv) #aarrggbb color against app's policy."""
        if not isinstance(hex_value, str):
            return False, f"Non-string color value: {hex_value!r}"
        s = hex_value.strip()
        if HEX6_RE.match(s):
            rgb_hex = s.lower()
        elif HEX8_RE.match(s):
            if allow_mpv_argb and app_name == "mpv":
                # mpv 8-hex is #AARRGGBB (alpha first)
                rgb_hex = "#" + s[3:9].lower()
            else:
                # Standard #RRGGBBAA (alpha last)
                rgb_hex = "#" + s[1:7].lower()
        else:
            return False, f"Malformed hex color {hex_value!r} in {app_name}"

        if rgb_hex in self.base_hexes:
            return True, "base"

        if app_name in BLENDED_SURFACE_APPS:
            if rgb_hex in self.doc_derived_hexes:
                return True, "doc_derived"
            if self.is_linear_mix(rgb_hex):
                return True, "linear_mix"
            return False, f"Color {hex_value!r} (RGB {rgb_hex}) in blended app {app_name!r} is outside BASE_HEXES | DOC_DERIVED_HEXES | MIX_ALLOWED"

        return False, f"Color {hex_value!r} (RGB {rgb_hex}) in direct-palette app {app_name!r} is not in BASE_HEXES"

    def is_allowed_rgb_tuple(self, rgb: tuple[int, int, int], app_name: str) -> tuple[bool, str]:
        try:
            hx = rgb_to_hex(*rgb)
        except ValueError as exc:
            return False, str(exc)
        return self.is_allowed_hex(hx, app_name)


def load_palette(reference_colors_path: Path | None = None) -> PaletteContract:
    from . import get_reference_colors

    path = reference_colors_path or get_reference_colors()
    return PaletteContract(path)
