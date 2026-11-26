"""Tier 1: Feature Coverage (>= 5 checks per deliverable across #1-#37 = 185 tests)."""

from __future__ import annotations

import unittest
from pathlib import Path

from lib import get_nvim_colorscheme, get_project_root
from lib.parsers import (
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
from lib.specs import (
    DELIVERABLE_SPECS,
    UNRESOLVED_PLACEHOLDER_RE,
    DeliverableSpec,
    validate_deliverable_structure,
)
from lib.validators import validate_luac


def _read_text_if_utf8(path: Path) -> str | None:
    if path.suffix in (".tdesktop-theme", ".png", ".jpg", ".zip"):
        return None
    return path.read_text(encoding="utf-8")


def _check_format_parse(spec: DeliverableSpec, project_root: Path) -> None:
    fid = spec.feature_id
    if fid == 1:
        parse_toml(project_root / "colors.toml")
    elif fid == 2:
        validate_tdesktop_theme(project_root / "telegram/911.tdesktop-theme")
    elif fid == 3:
        res = validate_luac(project_root / "neovim/colors/911.lua")
        if not res.ok:
            raise AssertionError(res.message)
    elif fid in (4, 24, 32, 35):
        parse_ini(project_root / spec.theme_files[0])
    elif fid == 5:
        parse_ghostty(project_root / "ghostty/911")
    elif fid in (6, 9, 10, 13, 25):
        parse_toml(project_root / spec.theme_files[0])
    elif fid == 7:
        parse_kitty(project_root / "kitty/911.conf")
    elif fid == 8:
        text = (project_root / "tmux/911.conf").read_text(encoding="utf-8")
        if not any(
            line.strip().startswith(("set", "setw", "set-option", "set-window-option"))
            for line in text.splitlines()
        ):
            raise AssertionError("tmux/911.conf contains no tmux set directives")
    elif fid in (11, 12):
        import subprocess

        proc = subprocess.run(
            ["zsh", "-n", str(project_root / spec.theme_files[0])],
            capture_output=True,
            text=True,
            timeout=10,
        )
        if proc.returncode != 0:
            raise AssertionError(f"zsh -n failed: {proc.stderr.strip()}")
    elif fid in (14, 15, 16):
        parse_json(project_root / spec.theme_files[0])
    elif fid == 17:
        parse_plist(project_root / "bat/911.tmTheme")
    elif fid == 18:
        parse_git_config(project_root / "delta/911.gitconfig")
    elif fid in (19, 20, 21, 22, 23):
        parse_yaml(project_root / spec.theme_files[0])
    elif fid == 26:
        parse_jsonc(project_root / "fastfetch/911.jsonc")
    elif fid == 27:
        parse_btop_theme(project_root / "btop/911.theme")
    elif fid == 28:
        parse_json(project_root / "vscode/package.json")
        parse_json(project_root / "vscode/themes/911-color-theme.json")
    elif fid == 29:
        parse_json(project_root / "obsidian/911/manifest.json")
        validate_css((project_root / "obsidian/911/theme.css").read_text(encoding="utf-8"))
    elif fid == 30:
        parse_json(project_root / "chromium/manifest.json")
        csv = (project_root / "chromium/chromium.theme").read_text(encoding="utf-8").strip()
        parts = [int(x.strip()) for x in csv.split(",")]
        if len(parts) != 3 or any(not (0 <= c <= 255) for c in parts):
            raise AssertionError(f"Invalid chromium.theme RGB CSV: {csv!r}")
    elif fid in (31, 34, 37):
        for rel in spec.theme_files:
            validate_css((project_root / rel).read_text(encoding="utf-8"))
    elif fid == 33:
        parse_mpv_conf(project_root / "mpv/mpv.conf")
    elif fid == 36:
        parse_hyprland_conf(project_root / "hyprland/911.conf")
    else:
        raise ValueError(f"Unhandled feature_id {fid}")


class TestTier1FeatureCoverage(unittest.TestCase):
    """5 distinct checks per feature (#1..#37) = 185 test cases."""


def _attach_feature_tests(spec: DeliverableSpec) -> None:
    fid = spec.feature_id
    prefix = f"test_f{fid:02d}"

    def _target_paths(root: Path) -> list[Path]:
        paths = [root / rel for rel in spec.required_files]
        if fid == 3:
            paths.append(get_nvim_colorscheme())
        return paths

    def test_01_exist(self: TestTier1FeatureCoverage) -> None:
        root = get_project_root()
        for p in _target_paths(root):
            self.assertTrue(
                p.is_file(),
                f"[{spec.name}] Required deliverable file missing: {p}",
            )

    def test_02_non_empty_no_placeholders(self: TestTier1FeatureCoverage) -> None:
        root = get_project_root()
        for p in _target_paths(root):
            self.assertTrue(p.is_file(), f"Missing file: {p}")
            self.assertGreater(p.stat().st_size, 0, f"Empty file: {p}")
            text = _read_text_if_utf8(p)
            if text is not None:
                m = UNRESOLVED_PLACEHOLDER_RE.search(text)
                self.assertIsNone(
                    m,
                    f"Unresolved template placeholder {m.group(0) if m else ''} in {p}",
                )

    def test_03_readme_valid_and_no_auto_activate(self: TestTier1FeatureCoverage) -> None:
        root = get_project_root()
        readme = root / spec.readme_file
        self.assertTrue(readme.is_file(), f"Missing README: {readme}")
        self.assertGreater(readme.stat().st_size, 0, f"Empty README: {readme}")
        content = readme.read_text(encoding="utf-8")
        self.assertIn("911", content, f"README {readme} must reference '911'")
        lower = content.lower()
        self.assertTrue(
            any(tok in lower for tok in ("install", "usage", "copy", "cp ", "ln ", "symlink", "load", "theme")),
            f"README {readme} missing installation/usage instructions",
        )
        self.assertNotIn(
            "omarchy-theme-set",
            content,
            f"README {readme} must not invoke omarchy-theme-set (R4 isolation)",
        )

    def test_04_format_parse(self: TestTier1FeatureCoverage) -> None:
        root = get_project_root()
        _check_format_parse(spec, root)

    def test_05_required_keys(self: TestTier1FeatureCoverage) -> None:
        root = get_project_root()
        validate_deliverable_structure(spec, root)

    test_01_exist.__doc__ = f"F{fid:02d} ({spec.name}): files exist"
    test_02_non_empty_no_placeholders.__doc__ = f"F{fid:02d} ({spec.name}): non-empty & no placeholders"
    test_03_readme_valid_and_no_placeholders = test_03_readme_valid_and_no_auto_activate
    test_03_readme_valid_and_no_placeholders.__doc__ = f"F{fid:02d} ({spec.name}): standalone README"
    test_04_format_parse.__doc__ = f"F{fid:02d} ({spec.name}): format parse"
    test_05_required_keys.__doc__ = f"F{fid:02d} ({spec.name}): required key groups"

    setattr(TestTier1FeatureCoverage, f"{prefix}_01_files_exist", test_01_exist)
    setattr(TestTier1FeatureCoverage, f"{prefix}_02_non_empty_no_placeholders", test_02_non_empty_no_placeholders)
    setattr(TestTier1FeatureCoverage, f"{prefix}_03_standalone_readme", test_03_readme_valid_and_no_auto_activate)
    setattr(TestTier1FeatureCoverage, f"{prefix}_04_format_parse", test_04_format_parse)
    setattr(TestTier1FeatureCoverage, f"{prefix}_05_required_keys", test_05_required_keys)


for _spec in DELIVERABLE_SPECS:
    _attach_feature_tests(_spec)


if __name__ == "__main__":
    unittest.main()
