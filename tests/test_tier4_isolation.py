"""Tier 4: Real-World End-User Scenarios & R4 Isolation Proofs."""

from __future__ import annotations

import tempfile
import unittest
import zipfile
from pathlib import Path

from lib import (
    get_nvim_colorscheme_name,
    get_nvim_rtp,
    get_project_root,
    get_reference_colors,
    get_reference_repo,
    is_isolated_nvim_mode,
)
from lib.baseline import (
    BASELINE_ABSENT_PATHS,
    BASELINE_FILE_SHA256,
    verify_absent_paths,
    verify_baseline_files,
    verify_reference_repo_integrity,
    verify_zen_profile_isolation,
)
from lib.palette import load_palette
from lib.parsers import validate_png_bytes, validate_tdesktop_theme
from lib.validators import validate_nvim_colorscheme, validate_nvim_default


def _int_to_hex(val: int) -> str:
    return f"#{val:06x}"


class TestTier4Isolation(unittest.TestCase):
    """Real-world headless Neovim, R4 baseline checksums, reference repo integrity, Telegram roundtrip."""

    def test_headless_nvim_default_startup_remains_aether(self) -> None:
        if is_isolated_nvim_mode():
            self.skipTest("Skipped live ~/.config/nvim startup check under isolated nvim mode")
        res = validate_nvim_default()
        self.assertTrue(res.ok, res.message)

    def test_headless_nvim_explicit_carrera_loads_cleanly(self) -> None:
        palette = load_palette(get_reference_colors())
        res = validate_nvim_colorscheme(
            get_nvim_colorscheme_name(),
            rtp_dir=get_nvim_rtp(),
            isolated=is_isolated_nvim_mode(),
        )
        self.assertTrue(res.ok, res.message)
        hls = res.data
        normal_fg, normal_bg = hls["Normal"]
        self.assertIsNotNone(normal_fg)
        self.assertIsNotNone(normal_bg)
        self.assertEqual(
            _int_to_hex(normal_fg),
            palette.foreground,
            f"Normal fg {_int_to_hex(normal_fg)} != {palette.foreground}",
        )
        self.assertEqual(
            _int_to_hex(normal_bg),
            palette.background,
            f"Normal bg {_int_to_hex(normal_bg)} != {palette.background}",
        )
        for grp in ("Comment", "Keyword", "Function", "String", "Type"):
            fg, bg = hls[grp]
            self.assertIsNotNone(fg, f"Highlight group {grp} missing fg")
            ok, reason = palette.is_allowed_hex(_int_to_hex(fg), "neovim")
            self.assertTrue(ok, f"Neovim {grp} fg: {reason}")
            if bg is not None:
                ok_bg, reason_bg = palette.is_allowed_hex(_int_to_hex(bg), "neovim")
                self.assertTrue(ok_bg, f"Neovim {grp} bg: {reason_bg}")
        for grp in ("NormalFloat", "CursorLine", "Visual", "StatusLine"):
            fg, bg = hls[grp]
            self.assertTrue(
                fg is not None or bg is not None,
                f"Highlight group {grp} missing both fg and bg",
            )
            if fg is not None:
                ok_fg, reason_fg = palette.is_allowed_hex(_int_to_hex(fg), "neovim")
                self.assertTrue(ok_fg, f"Neovim {grp} fg: {reason_fg}")
            if bg is not None:
                ok_bg, reason_bg = palette.is_allowed_hex(_int_to_hex(bg), "neovim")
                self.assertTrue(ok_bg, f"Neovim {grp} bg: {reason_bg}")

    def test_r4_baseline_active_configs_unchanged(self) -> None:
        self.assertEqual(len(BASELINE_FILE_SHA256), 43)
        errors = verify_baseline_files(BASELINE_FILE_SHA256) + verify_zen_profile_isolation()
        self.assertEqual(
            errors,
            [],
            "R4 isolation violation(s) in active user configs:\n" + "\n".join(errors),
        )

    def test_r4_absent_paths_remain_absent(self) -> None:
        self.assertEqual(len(BASELINE_ABSENT_PATHS), 5)
        errors = verify_absent_paths(BASELINE_ABSENT_PATHS)
        self.assertEqual(
            errors,
            [],
            "R4 isolation violation(s) — absent path now exists:\n" + "\n".join(errors),
        )

    def test_reference_omarchy_carrera_theme_git_and_hash_integrity(self) -> None:
        repo = get_reference_repo()
        errors = verify_reference_repo_integrity(repo)
        self.assertEqual(
            errors,
            [],
            "Reference omarchy-carrera-theme integrity failure:\n" + "\n".join(errors),
        )

    def test_telegram_tdesktop_theme_zip_extraction_roundtrip(self) -> None:
        root = get_project_root()
        palette = load_palette(get_reference_colors())
        zip_path = root / "telegram/carrera.tdesktop-theme"
        info = validate_tdesktop_theme(zip_path)

        with tempfile.TemporaryDirectory(prefix="carrera_tg_rt_") as tmp:
            extract_dir = Path(tmp)
            with zipfile.ZipFile(zip_path, "r") as zf:
                zf.extractall(extract_dir)

            colors_file = extract_dir / "colors.tdesktop-theme"
            bg_file = extract_dir / info["background"]
            self.assertTrue(colors_file.is_file())
            self.assertTrue(bg_file.is_file())

            if info["background"].endswith(".png"):
                png_info = validate_png_bytes(bg_file.read_bytes())
                self.assertGreater(png_info["width"], 0)
                self.assertGreater(png_info["height"], 0)

            entries = info["entries"]
            self.assertGreaterEqual(len(entries), 100)
            for k, v in entries.items():
                cur = v
                while not cur.startswith("#"):
                    cur = entries[cur]
                ok, reason = palette.is_allowed_hex(cur, "telegram")
                self.assertTrue(ok, f"Telegram key {k!r} resolved to {cur!r}: {reason}")


if __name__ == "__main__":
    unittest.main()
