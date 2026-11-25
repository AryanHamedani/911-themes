#!/usr/bin/env python3
"""Canonical CLI runner for the Carrera v2.0.0 opaque-box E2E validation suite."""

from __future__ import annotations

import argparse
import os
import sys
import unittest
from pathlib import Path

TESTS_DIR = Path(__file__).resolve().parent
if str(TESTS_DIR) not in sys.path:
    sys.path.insert(0, str(TESTS_DIR))

from lib import (  # noqa: E402
    DEFAULT_NVIM_COLORSCHEME,
    DEFAULT_PROJECT_ROOT,
    DEFAULT_REFERENCE_COLORS,
)

TIER_MODULES: dict[str, str] = {
    "1": "test_tier1_coverage",
    "2": "test_tier2_boundaries",
    "3": "test_tier3_consistency",
    "4": "test_tier4_isolation",
}


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="run_e2e.py",
        description="Carrera v2.0.0 opaque-box E2E validation suite (Tiers 1-4 & --self-test).",
    )
    parser.add_argument(
        "--tier",
        choices=("1", "2", "3", "4", "all"),
        default="all",
        help="Validation tier to run (default: all).",
    )
    parser.add_argument(
        "--project-root",
        type=Path,
        default=DEFAULT_PROJECT_ROOT,
        help=f"Path to carrera_themes repository (default: {DEFAULT_PROJECT_ROOT}).",
    )
    parser.add_argument(
        "--nvim-colorscheme",
        type=Path,
        default=DEFAULT_NVIM_COLORSCHEME,
        help=f"Path to standalone Neovim colorscheme (default: {DEFAULT_NVIM_COLORSCHEME}).",
    )
    parser.add_argument(
        "--reference-colors",
        type=Path,
        default=DEFAULT_REFERENCE_COLORS,
        help=f"Path to reference colors.toml (default: {DEFAULT_REFERENCE_COLORS}).",
    )
    parser.add_argument(
        "--self-test",
        action="store_true",
        help="Run self-test positive synthetic suite and negative mutation checks in temp dirs.",
    )
    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="Verbose unittest output.",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    os.environ["CARRERA_PROJECT_ROOT"] = str(args.project_root.resolve())
    os.environ["CARRERA_NVIM_COLORSCHEME"] = str(args.nvim_colorscheme)
    os.environ["CARRERA_REFERENCE_COLORS"] = str(args.reference_colors.resolve())

    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    if args.self_test:
        suite.addTests(loader.loadTestsFromName("test_self"))
    else:
        selected = ("1", "2", "3", "4") if args.tier == "all" else (args.tier,)
        for tier_id in selected:
            suite.addTests(loader.loadTestsFromName(TIER_MODULES[tier_id]))

    verbosity = 2 if args.verbose else 1
    runner = unittest.TextTestRunner(verbosity=verbosity)
    result = runner.run(suite)
    return 0 if result.wasSuccessful() else 1


if __name__ == "__main__":
    raise SystemExit(main())
