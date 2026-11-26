"""Shared helpers and configuration resolution for the Carrera E2E test suite."""

from __future__ import annotations

import os
from pathlib import Path

DEFAULT_PROJECT_ROOT = Path("/home/aryan/teamwork_projects/carrera_themes")
DEFAULT_NVIM_COLORSCHEME = Path("/home/aryan/.config/nvim/colors/911.lua")
DEFAULT_REFERENCE_COLORS = Path(
    "/home/aryan/Work/personal/AryanHamedani/omarchy-911-theme/colors.toml"
)
DEFAULT_REFERENCE_REPO = Path(
    "/home/aryan/Work/personal/AryanHamedani/omarchy-911-theme"
)


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
