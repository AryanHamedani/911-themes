"""Tier 2: Boundary & Corner Cases (Palette Contract, Format Rules, Isolated CLI Validators)."""

from __future__ import annotations

import shutil
import tempfile
import unittest
from pathlib import Path

from lib import get_project_root, get_reference_colors
from lib.palette import BARE_HEX6_RE, HEX6_RE, HEX8_RE, hex_to_rgb, load_palette
from lib.parsers import (
    parse_ini,
    parse_json,
    parse_jsonc,
    parse_mpv_conf,
    parse_toml,
    validate_tdesktop_theme,
)
from lib.specs import (
    DELIVERABLE_SPECS,
    FOOT_TWO_HEX_KEYS,
    DeliverableSpec,
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
    validate_luac,
    validate_mpv,
    validate_nvim_colorscheme,
    validate_pgcli,
    validate_starship,
    validate_tmux,
    validate_zsh_syntax_highlighting,
)


class TestTier2PaletteContract(unittest.TestCase):
    """Verify exact Palette Contract compliance across all 37 deliverables."""


def _attach_palette_test(spec: DeliverableSpec) -> None:
    def test_palette(self: TestTier2PaletteContract) -> None:
        root = get_project_root()
        palette = load_palette(get_reference_colors())
        validate_deliverable_structure(spec, root)
        errors = validate_deliverable_palette(spec, root, palette)
        self.assertEqual(
            errors,
            [],
            f"[{spec.name}] Palette Contract violations:\n" + "\n".join(errors),
        )

    test_palette.__doc__ = f"F{spec.feature_id:02d} ({spec.name}): Palette Contract"
    setattr(
        TestTier2PaletteContract,
        f"test_palette_f{spec.feature_id:02d}",
        test_palette,
    )


for _spec in DELIVERABLE_SPECS:
    _attach_palette_test(_spec)


class TestTier2FormatBoundaries(unittest.TestCase):
    """Format-specific edge cases and boundary constraints."""

    def test_foot_no_hash_prefix_and_6hex(self) -> None:
        root = get_project_root()
        cp = parse_ini(root / "foot/carrera.ini")
        sections = [(s, cp[s]) for s in cp.sections()]
        if cp.defaults():
            sections.append(("DEFAULT", cp.defaults()))
        for sec_name, sec in sections:
            is_color_sec = sec_name == "DEFAULT" or sec_name.lower().startswith("colors")
            for k, v in sec.items():
                if k == "alpha":
                    continue
                tokens = v.split()
                if is_color_sec:
                    expected_len = 2 if k in FOOT_TWO_HEX_KEYS else 1
                    self.assertEqual(
                        len(tokens),
                        expected_len,
                        f"foot [{sec_name}] {k}={v!r} expected {expected_len} token(s)",
                    )
                for tok in tokens:
                    self.assertNotIn("#", tok, f"foot [{sec_name}] {k}={v!r} must omit '#'")
                    if is_color_sec:
                        self.assertRegex(tok, BARE_HEX6_RE, f"foot [{sec_name}] {k}={v!r} invalid 6-hex")

    def test_imv_no_hash_prefix_and_6hex(self) -> None:
        root = get_project_root()
        cp = parse_ini(root / "imv/carrera.ini")
        sections = [(s, cp[s]) for s in cp.sections()]
        if cp.defaults():
            sections.append(("DEFAULT", cp.defaults()))
        for sec_name, sec in sections:
            for k, v in sec.items():
                self.assertNotIn("#", v, f"imv [{sec_name}] {k}={v!r} must omit '#'")
                is_color_key = (
                    k in ("background", "foreground", "overlay_text_color", "overlay_background_color")
                    or k.endswith("_color")
                    or k.endswith("color")
                    or sec_name.lower().startswith("colors")
                )
                if is_color_key:
                    self.assertRegex(v, BARE_HEX6_RE, f"imv [{sec_name}] {k}={v!r} invalid 6-hex")

    def test_cliamp_strict_7_keys_and_filename(self) -> None:
        root = get_project_root()
        p = root / "cliamp/carrera.toml"
        self.assertNotEqual(p.name, "default.toml")
        data = parse_toml(p)
        req = {"bg", "accent", "bright_fg", "fg", "green", "yellow", "red"}
        self.assertTrue(req.issubset(set(data.keys())), f"Missing cliamp keys: {req - set(data.keys())}")
        for k in req:
            self.assertRegex(str(data[k]), HEX6_RE, f"cliamp {k}={data[k]!r} must be #RRGGBB")

    def test_telegram_zip_flat_layout_and_png_crc(self) -> None:
        root = get_project_root()
        info = validate_tdesktop_theme(root / "telegram/carrera.tdesktop-theme")
        self.assertGreaterEqual(len(info["entries"]), 100)
        self.assertEqual(info["background"], "background.png")
        self.assertGreater(info["bg_info"]["width"], 0)
        self.assertGreater(info["bg_info"]["height"], 0)

    def test_mpv_argb_alpha_first_parsing(self) -> None:
        root = get_project_root()
        palette = load_palette(get_reference_colors())
        kv = parse_mpv_conf(root / "mpv/mpv.conf")
        for k, v in kv.items():
            if v.startswith("#"):
                if HEX8_RE.match(v):
                    rgb_part = "#" + v[3:9].lower()
                    self.assertIn(
                        rgb_part,
                        palette.base_hexes,
                        f"mpv {k}={v!r}: #AARRGGBB RGB {rgb_part} not in BASE_HEXES",
                    )
                else:
                    self.assertRegex(v, HEX6_RE, f"mpv {k}={v!r} invalid hex")
                    self.assertIn(v.lower(), palette.base_hexes)

    def test_chromium_rgb_arrays_and_csv(self) -> None:
        root = get_project_root()
        palette = load_palette(get_reference_colors())
        man = parse_json(root / "chromium/manifest.json")
        self.assertEqual(man["manifest_version"], 3)
        for k, arr in man["theme"]["colors"].items():
            self.assertIsInstance(arr, list)
            self.assertIn(len(arr), (3, 4))
            for ch in arr[:3]:
                self.assertIsInstance(ch, int)
                self.assertNotIsInstance(ch, bool)
                self.assertGreaterEqual(ch, 0)
                self.assertLessEqual(ch, 255)
            hx = f"#{arr[0]:02x}{arr[1]:02x}{arr[2]:02x}"
            self.assertIn(hx, palette.base_hexes, f"chromium {k} -> {hx} not in BASE_HEXES")
        csv_text = (root / "chromium/chromium.theme").read_text(encoding="utf-8").strip()
        expected_csv = ",".join(map(str, hex_to_rgb(palette.background)))
        self.assertEqual(csv_text, expected_csv)

    def test_fastfetch_jsonc_parses_after_comment_strip(self) -> None:
        root = get_project_root()
        data = parse_jsonc(root / "fastfetch/carrera.jsonc")
        self.assertIn("display", data)
        self.assertIn("color", data["display"])

    def test_opencode_and_pi_no_dangling_references(self) -> None:
        root = get_project_root()
        oc = parse_json(root / "opencode/carrera.json")
        for k, v in oc["theme"].items():
            vals = list(v.values()) if isinstance(v, dict) else [v]
            for item in vals:
                if isinstance(item, str) and not item.startswith("#") and item != "none":
                    self.assertIn(item, oc["defs"], f"opencode dangling ref {k} -> {item}")
        pi = parse_json(root / "pi/carrera.json")
        for section in ("colors", "export"):
            for k, v in pi[section].items():
                if isinstance(v, str) and v not in ("", "none") and not v.startswith("#"):
                    self.assertIn(v, pi["vars"], f"pi dangling ref {section}.{k} -> {v}")

    def test_vscode_package_theme_path_resolves(self) -> None:
        root = get_project_root()
        pkg = parse_json(root / "vscode/package.json")
        rel = pkg["contributes"]["themes"][0]["path"]
        target = (root / "vscode" / rel).resolve()
        self.assertTrue(target.is_file(), f"VS Code theme path missing: {target}")


class TestTier2CliValidators(unittest.TestCase):
    """Isolated CLI validator execution with stdout/stderr/exit-code trap checks."""

    def test_cli_luac_neovim(self) -> None:
        res = validate_luac(get_project_root() / "neovim/colors/carrera.lua")
        self.assertTrue(res.ok, res.message)

    def test_cli_nvim_headless_isolated_rtp(self) -> None:
        src_lua = get_project_root() / "neovim/colors/carrera.lua"
        with tempfile.TemporaryDirectory(prefix="carrera_nvim_rtp_") as tmp:
            rtp = Path(tmp)
            colors_dir = rtp / "colors"
            colors_dir.mkdir(parents=True)
            shutil.copy2(src_lua, colors_dir / "carrera.lua")
            res = validate_nvim_colorscheme("carrera", rtp_dir=rtp, isolated=True)
            self.assertTrue(res.ok, res.message)

    def test_cli_foot(self) -> None:
        res = validate_foot(get_project_root() / "foot/carrera.ini")
        self.assertTrue(res.ok, res.message)

    def test_cli_ghostty(self) -> None:
        res = validate_ghostty(get_project_root() / "ghostty/carrera")
        self.assertTrue(res.ok, res.message)

    def test_cli_starship(self) -> None:
        res = validate_starship(get_project_root() / "starship/carrera.toml")
        self.assertTrue(res.ok, res.message)

    def test_cli_bat(self) -> None:
        res = validate_bat(get_project_root() / "bat/Carrera.tmTheme", theme_name="Carrera")
        self.assertTrue(res.ok, res.message)

    def test_cli_git_delta(self) -> None:
        res = validate_git_delta(get_project_root() / "delta/carrera.gitconfig")
        self.assertTrue(res.ok, res.message)

    def test_cli_tmux(self) -> None:
        res = validate_tmux(get_project_root() / "tmux/carrera.conf")
        self.assertTrue(res.ok, res.message)

    def test_cli_eza(self) -> None:
        res = validate_eza(get_project_root() / "eza/theme.yml")
        self.assertTrue(res.ok, res.message)

    def test_cli_kubecolor(self) -> None:
        res = validate_kubecolor(get_project_root() / "kubecolor/color.yaml")
        self.assertTrue(res.ok, res.message)

    def test_cli_fastfetch(self) -> None:
        res = validate_fastfetch(get_project_root() / "fastfetch/carrera.jsonc")
        self.assertTrue(res.ok, res.message)

    def test_cli_pgcli(self) -> None:
        res = validate_pgcli(get_project_root() / "pgcli/carrera.pgclirc")
        self.assertTrue(res.ok, res.message)

    def test_cli_herdr(self) -> None:
        res = validate_herdr(get_project_root() / "herdr/carrera.toml")
        self.assertTrue(res.ok, res.message)

    def test_cli_mpv(self) -> None:
        res = validate_mpv(get_project_root() / "mpv/mpv.conf")
        self.assertTrue(res.ok, res.message)

    def test_cli_hyprland(self) -> None:
        res = validate_hyprland(get_project_root() / "hyprland/carrera.conf")
        self.assertTrue(res.ok, res.message)

    def test_cli_zsh_syntax_highlighting(self) -> None:
        res = validate_zsh_syntax_highlighting(
            get_project_root() / "zsh-syntax-highlighting/carrera.zsh"
        )
        self.assertTrue(res.ok, res.message)

    def test_cli_fzf(self) -> None:
        res = validate_fzf(get_project_root() / "fzf/carrera.sh")
        self.assertTrue(res.ok, res.message)


if __name__ == "__main__":
    unittest.main()
