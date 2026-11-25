"""Tier 3: Cross-Feature & Integration Consistency."""

from __future__ import annotations

import os
import re
import unittest
from pathlib import Path

from lib import get_nvim_colorscheme, get_project_root, get_reference_colors, get_reference_repo
from lib.baseline import sha256_file
from lib.palette import load_palette
from lib.parsers import parse_btop_theme, parse_ghostty, parse_ini, parse_kitty, parse_toml
from lib.specs import APP_DIRS, DELIVERABLE_SPECS


class TestTier3Consistency(unittest.TestCase):
    """Cross-feature parity, inventory accuracy, documentation, and R4 hygiene."""

    def test_colors_toml_byte_parity_with_reference(self) -> None:
        root = get_project_root()
        ref = get_reference_colors()
        local = root / "colors.toml"
        self.assertTrue(local.is_file(), f"Missing {local}")
        self.assertTrue(ref.is_file(), f"Missing {ref}")
        self.assertEqual(
            sha256_file(local),
            sha256_file(ref),
            "carrera_themes/colors.toml is not byte-identical to reference colors.toml",
        )

    def test_license_mit_and_copyright(self) -> None:
        lic = (get_project_root() / "LICENSE").read_text(encoding="utf-8")
        self.assertIn("MIT License", lic)
        self.assertIn("Copyright (c) 2026 Aryan Hamedani", lic)

    def test_neovim_copy_parity(self) -> None:
        root = get_project_root()
        repo_lua = root / "neovim/colors/carrera.lua"
        active_lua = get_nvim_colorscheme()
        self.assertTrue(repo_lua.is_file(), f"Missing {repo_lua}")
        self.assertTrue(active_lua.is_file(), f"Missing {active_lua}")
        self.assertEqual(
            sha256_file(repo_lua),
            sha256_file(active_lua),
            f"{repo_lua} differs from {active_lua}",
        )

    def test_btop_parity_with_reference(self) -> None:
        root = get_project_root()
        ref_btop = get_reference_repo() / "btop.theme"
        local_btop = root / "btop/carrera.theme"
        self.assertTrue(local_btop.is_file(), f"Missing {local_btop}")
        self.assertTrue(ref_btop.is_file(), f"Missing {ref_btop}")
        local_map = parse_btop_theme(local_btop)
        ref_map = parse_btop_theme(ref_btop)
        self.assertEqual(
            local_map,
            ref_map,
            "btop/carrera.theme key/value map does not match reference btop.theme",
        )

    def test_inventory_md_lists_all_36_apps_and_existing_paths(self) -> None:
        root = get_project_root()
        inv_path = root / "INVENTORY.md"
        self.assertTrue(inv_path.is_file(), f"Missing {inv_path}")
        inv = inv_path.read_text(encoding="utf-8")
        for app in APP_DIRS:
            self.assertIn(
                app,
                inv,
                f"INVENTORY.md missing application directory reference {app!r}",
            )
        for spec in DELIVERABLE_SPECS:
            if spec.feature_id < 2:
                continue
            for rel in spec.theme_files:
                self.assertIn(
                    rel,
                    inv,
                    f"INVENTORY.md missing theme file path {rel!r}",
                )
                self.assertTrue(
                    (root / rel).is_file(),
                    f"INVENTORY.md path does not exist on disk: {root / rel}",
                )

        # Verify no extra undocumented top-level app directories exist (excluding tests/ and hidden)
        for child in root.iterdir():
            if not child.is_dir():
                continue
            if child.name.startswith(".") or child.name in ("tests", "__pycache__"):
                continue
            self.assertIn(
                child.name,
                APP_DIRS,
                f"Undocumented directory {child.name!r} outside 36-app INVENTORY",
            )

    def test_root_readme_completeness_and_disclaimer(self) -> None:
        root = get_project_root()
        readme = (root / "README.md").read_text(encoding="utf-8")
        self.assertIn("Carrera", readme)
        self.assertIn("Porsche", readme)
        self.assertNotIn("omarchy-theme-set", readme)
        palette = load_palette(get_reference_colors())
        self.assertIn(palette.background, readme.lower())
        self.assertIn(palette.foreground, readme.lower())
        self.assertIn(palette.accent, readme.lower())
        for app in APP_DIRS:
            self.assertIn(
                app,
                readme,
                f"Root README.md missing application listing for {app!r}",
            )

    def test_no_auto_activation_scripts_or_hooks(self) -> None:
        root = get_project_root()
        allowed_shell_files = {
            (root / "fzf/carrera.sh").resolve(),
            (root / "zsh-syntax-highlighting/carrera.zsh").resolve(),
        }
        disallowed_script_suffixes = {
            ".sh", ".zsh", ".bash", ".fish", ".nu", ".py", ".rb", ".pl", ".ps1",
        }
        binary_suffixes = {".png", ".jpg", ".jpeg", ".tdesktop-theme", ".zip", ".ico", ".webp"}
        for p in root.rglob("*"):
            if not p.is_file():
                continue
            rel_parts = p.relative_to(root).parts
            if any(part in ("tests", ".git", "__pycache__") for part in rel_parts):
                continue
            resolved = p.resolve()
            if p.suffix.lower() in disallowed_script_suffixes and resolved not in allowed_shell_files:
                self.fail(f"Unexpected script in repository: {p}")
            if p.suffix.lower() in binary_suffixes:
                continue
            text = p.read_text(encoding="utf-8", errors="ignore")
            if resolved not in allowed_shell_files and text.startswith("#!"):
                self.fail(f"Unexpected shebang/executable script in repository: {p}")
            if os.access(p, os.X_OK) and resolved not in allowed_shell_files:
                self.fail(f"Unexpected executable file in repository: {p}")
            self.assertNotIn(
                "omarchy-theme-set",
                text,
                f"Auto-activation command 'omarchy-theme-set' found in {p}",
            )

    def test_ansi_16_alignment_across_terminals(self) -> None:
        root = get_project_root()
        palette = load_palette(get_reference_colors())
        t = palette.tokens
        expected_16 = [
            t["background"],
            t["red"],
            t["green"],
            t["yellow"],
            t["blue"],
            t["magenta"],
            t["cyan"],
            t["foreground"],
            t["muted"],
            t["bright_red"],
            t["bright_green"],
            t["bright_yellow"],
            t["bright_blue"],
            t["bright_magenta"],
            t["bright_cyan"],
            t["bright_foreground"],
        ]

        # Foot
        foot_sec = parse_ini(root / "foot/carrera.ini")["colors-dark"]
        foot_16 = [
            "#" + foot_sec[f"regular{i}"].lower() for i in range(8)
        ] + ["#" + foot_sec[f"bright{i}"].lower() for i in range(8)]
        self.assertEqual(foot_16, expected_16, "Foot ANSI 0..15 mismatch with colors.toml")

        # Ghostty
        ghostty_pal = {}
        for k, v in parse_ghostty(root / "ghostty/carrera"):
            if k == "palette" and "=" in v:
                idx, col = v.split("=", 1)
                ghostty_pal[int(idx.strip())] = col.strip().lower()
        ghostty_16 = [ghostty_pal[i] for i in range(16)]
        self.assertEqual(ghostty_16, expected_16, "Ghostty ANSI 0..15 mismatch with colors.toml")

        # Alacritty
        ala = parse_toml(root / "alacritty/carrera.toml")["colors"]
        order = ("black", "red", "green", "yellow", "blue", "magenta", "cyan", "white")
        ala_16 = [ala["normal"][c].lower() for c in order] + [
            ala["bright"][c].lower() for c in order
        ]
        self.assertEqual(ala_16, expected_16, "Alacritty ANSI 0..15 mismatch with colors.toml")

        # Kitty
        kit = parse_kitty(root / "kitty/carrera.conf")
        kit_16 = [kit[f"color{i}"].lower() for i in range(16)]
        self.assertEqual(kit_16, expected_16, "Kitty ANSI 0..15 mismatch with colors.toml")

        # Neovim terminal_color_0..15 via isolated headless runtime evaluation
        import shutil
        import subprocess
        import tempfile

        with tempfile.TemporaryDirectory(prefix="carrera_t3_nvim_") as tmp:
            rtp = Path(tmp)
            (rtp / "colors").mkdir(parents=True)
            shutil.copy2(root / "neovim/colors/carrera.lua", rtp / "colors/carrera.lua")
            lua_cmd = (
                'lua for i=0,15 do io.stdout:write("TC_"..i.."="..tostring(vim.g["terminal_color_"..i]).."\\n") end'
            )
            proc = subprocess.run(
                [
                    "nvim",
                    "--headless",
                    "-u",
                    "NONE",
                    "--cmd",
                    f"set rtp^={rtp}",
                    "-c",
                    "colorscheme carrera",
                    "-c",
                    lua_cmd,
                    "-c",
                    "qa!",
                ],
                capture_output=True,
                text=True,
                timeout=15,
            )
            self.assertEqual(proc.returncode, 0, proc.stderr)
            self.assertEqual(proc.stderr.strip(), "", proc.stderr)
            nvim_tc: dict[int, str] = {}
            for line in proc.stdout.splitlines():
                if line.startswith("TC_") and "=" in line:
                    k_s, v_s = line[3:].split("=", 1)
                    nvim_tc[int(k_s)] = v_s.strip().lower()
            nvim_16 = [nvim_tc.get(i) for i in range(16)]
            self.assertEqual(
                nvim_16,
                expected_16,
                "Neovim terminal_color_0..15 mismatch with colors.toml",
            )


if __name__ == "__main__":
    unittest.main()
