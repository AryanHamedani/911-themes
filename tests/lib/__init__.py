"""Shared helpers and configuration resolution for the Carrera E2E test suite."""

from __future__ import annotations

import os
from pathlib import Path

DEFAULT_PROJECT_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_NVIM_COLORSCHEME = Path.home() / ".config/nvim/colors/911.lua"
_LOCAL_OMARCHY_911 = Path(
    "/home/aryan/Work/personal/AryanHamedani/omarchy-911-theme"
)
DEFAULT_REFERENCE_REPO = (
    _LOCAL_OMARCHY_911 if _LOCAL_OMARCHY_911.is_dir() else DEFAULT_PROJECT_ROOT
)
DEFAULT_REFERENCE_COLORS = DEFAULT_REFERENCE_REPO / "colors.toml"


def get_project_root() -> Path:
    return Path(os.environ.get("CARRERA_PROJECT_ROOT", str(DEFAULT_PROJECT_ROOT)))


def get_nvim_colorscheme() -> Path:
    return Path(
        os.environ.get("CARRERA_NVIM_COLORSCHEME", str(DEFAULT_NVIM_COLORSCHEME))
    )


def get_reference_colors() -> Path:
    return Path(
        os.environ.get("CARRERA_REFERENCE_COLORS", str(DEFAULT_REFERENCE_COLORS))
    )


def get_reference_repo() -> Path:
    ref_colors = get_reference_colors()
    if "CARRERA_REFERENCE_REPO" in os.environ:
        return Path(os.environ["CARRERA_REFERENCE_REPO"])
    return ref_colors.parent if ref_colors != DEFAULT_REFERENCE_COLORS else DEFAULT_REFERENCE_REPO


def get_nvim_rtp() -> Path | None:
    val = os.environ.get("CARRERA_NVIM_RTP", "").strip()
    return Path(val) if val else None


def get_nvim_colorscheme_name() -> str:
    return os.environ.get("CARRERA_NVIM_COLORSCHEME_NAME", "911")


def is_isolated_nvim_mode() -> bool:
    return os.environ.get("CARRERA_NVIM_ISOLATED", "0") == "1"
