"""Isolated CLI validator wrappers with empirical exit-code/stream trap checks."""

from __future__ import annotations

import itertools
import os
import shlex
import shutil
import subprocess
import tempfile
import tomllib
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from .parsers import parse_yaml

_TMUX_COUNTER = itertools.count(1)


@dataclass(slots=True)
class ValidationResult:
    ok: bool
    returncode: int
    stdout: str
    stderr: str
    message: str
    data: Any = None


def _run(
    cmd: list[str],
    *,
    env: dict[str, str] | None = None,
    input_text: str | None = None,
    timeout: int = 20,
) -> subprocess.CompletedProcess[str]:
    merged_env = os.environ.copy()
    if env:
        merged_env.update(env)
    return subprocess.run(
        cmd,
        env=merged_env,
        input=input_text,
        capture_output=True,
        text=True,
        timeout=timeout,
    )


def validate_luac(path: Path) -> ValidationResult:
    proc = _run(["luac", "-p", str(path)])
    ok = proc.returncode == 0 and proc.stderr.strip() == ""
    msg = "ok" if ok else f"luac failed (rc={proc.returncode}): {proc.stderr.strip()}"
    return ValidationResult(ok, proc.returncode, proc.stdout, proc.stderr, msg)


def validate_nvim_default() -> ValidationResult:
    lua_cmd = (
        'lua io.stdout:write("DEFAULT="..tostring(vim.g.colors_name).."\\n"); '
        'io.stdout:write("BG="..tostring(vim.o.background).."\\n")'
    )
    proc = _run(["nvim", "--headless", "-c", lua_cmd, "-c", "qa!"])
    out = proc.stdout
    err = proc.stderr.strip()
    ok = (
        proc.returncode == 0
        and err == ""
        and "DEFAULT=aether" in out
        and "BG=dark" in out
    )
    msg = "ok" if ok else f"nvim default failed (rc={proc.returncode}, out={out!r}, err={err!r})"
    return ValidationResult(ok, proc.returncode, proc.stdout, proc.stderr, msg)


def validate_nvim_colorscheme(
    colorscheme_name: str = "carrera",
    *,
    rtp_dir: Path | None = None,
    isolated: bool = False,
) -> ValidationResult:
    cmd = ["nvim", "--headless"]
    if isolated:
        cmd.extend(["-u", "NONE"])
    if rtp_dir is not None:
        cmd.extend(["--cmd", f"set rtp^={rtp_dir}"])
    lua_probe = (
        'lua io.stdout:write("EXPLICIT="..tostring(vim.g.colors_name).."\\n"); '
        'io.stdout:write("BG="..tostring(vim.o.background).."\\n"); '
        'for _,g in ipairs({"Normal","NormalFloat","CursorLine","Visual","StatusLine","Comment","Keyword","Function","String","Type"}) do '
        'local h=vim.api.nvim_get_hl(0,{name=g,link=false}); '
        'io.stdout:write("HL_"..g.."="..tostring(h.fg)..":"..tostring(h.bg).."\\n") end'
    )
    cmd.extend(["-c", f"colorscheme {colorscheme_name}", "-c", lua_probe, "-c", "qa!"])
    proc = _run(cmd)
    out = proc.stdout
    err = proc.stderr.strip()

    hls: dict[str, tuple[int | None, int | None]] = {}
    for line in out.splitlines():
        if line.startswith("HL_") and "=" in line:
            name_part, val_part = line[3:].split("=", 1)
            fg_s, bg_s = val_part.split(":", 1)
            fg = None if fg_s == "nil" else int(fg_s)
            bg = None if bg_s == "nil" else int(bg_s)
            hls[name_part] = (fg, bg)

    ok = (
        proc.returncode == 0
        and err == ""
        and f"EXPLICIT={colorscheme_name}" in out
        and "BG=dark" in out
        and "Normal" in hls
        and hls["Normal"][0] is not None
        and hls["Normal"][1] is not None
        and all(g in hls and hls[g][0] is not None for g in ("Comment", "Keyword", "Function", "String", "Type"))
        and all(
            g in hls and (hls[g][0] is not None or hls[g][1] is not None)
            for g in ("NormalFloat", "CursorLine", "Visual", "StatusLine")
        )
    )
    msg = "ok" if ok else f"nvim colorscheme failed (rc={proc.returncode}, out={out!r}, err={err!r})"
    return ValidationResult(ok, proc.returncode, proc.stdout, proc.stderr, msg, data=hls)


def validate_foot(path: Path) -> ValidationResult:
    proc = _run(["foot", "-c", str(path), "--check-config"])
    ok = proc.returncode == 0 and proc.stderr.strip() == ""
    msg = "ok" if ok else f"foot failed (rc={proc.returncode}): {proc.stderr.strip()}"
    return ValidationResult(ok, proc.returncode, proc.stdout, proc.stderr, msg)


def validate_ghostty(path: Path) -> ValidationResult:
    proc = _run(["ghostty", "+validate-config", f"--config-file={path}"])
    ok = proc.returncode == 0 and proc.stderr.strip() == ""
    msg = "ok" if ok else f"ghostty failed (rc={proc.returncode}): {proc.stderr.strip() or proc.stdout.strip()}"
    return ValidationResult(ok, proc.returncode, proc.stdout, proc.stderr, msg)


def validate_starship(path: Path) -> ValidationResult:
    proc = _run(
        ["starship", "print-config"],
        env={"STARSHIP_CONFIG": str(path)},
    )
    err = proc.stderr.strip()
    ok = (
        proc.returncode == 0
        and err == ""
        and "[ERROR]" not in proc.stdout
        and "[WARN]" not in proc.stdout
    )
    msg = "ok" if ok else f"starship failed (rc={proc.returncode}): err={err!r}"
    return ValidationResult(ok, proc.returncode, proc.stdout, proc.stderr, msg)


def validate_bat(path: Path, theme_name: str = "Carrera") -> ValidationResult:
    with tempfile.TemporaryDirectory(prefix="carrera_bat_") as tmp:
        tmp_path = Path(tmp)
        cfg_dir = tmp_path / "cfg"
        cache_dir = tmp_path / "cache"
        themes_dir = cfg_dir / "themes"
        themes_dir.mkdir(parents=True)
        cache_dir.mkdir(parents=True)
        shutil.copy2(path, themes_dir / path.name)

        env = {"BAT_CONFIG_DIR": str(cfg_dir), "BAT_CACHE_PATH": str(cache_dir)}
        build_proc = _run(["bat", "cache", "--build"], env=env)
        if (
            build_proc.returncode != 0
            or build_proc.stderr.strip() != ""
            or "Failed to load" in build_proc.stdout
            or "Failed to load" in build_proc.stderr
        ):
            return ValidationResult(
                False,
                build_proc.returncode,
                build_proc.stdout,
                build_proc.stderr,
                f"bat cache --build failed: stdout={build_proc.stdout!r}, stderr={build_proc.stderr!r}",
            )

        list_proc = _run(["bat", "--list-themes"], env=env)
        themes = [line.strip() for line in list_proc.stdout.splitlines()]
        found = any(t == theme_name or t.startswith(f"{theme_name} ") for t in themes)
        if list_proc.returncode != 0 or list_proc.stderr.strip() != "" or not found:
            return ValidationResult(
                False,
                list_proc.returncode,
                list_proc.stdout,
                list_proc.stderr,
                f"Theme {theme_name!r} missing from bat --list-themes",
            )

        sample = tmp_path / "sample.py"
        sample.write_text("def carrera():\n    return '#e1656c'\n", encoding="utf-8")
        render_proc = _run(["bat", f"--theme={theme_name}", "--color=always", str(sample)], env=env)
        ok = render_proc.returncode == 0 and render_proc.stderr.strip() == ""
        msg = "ok" if ok else f"bat render failed: stderr={render_proc.stderr!r}"
        return ValidationResult(ok, render_proc.returncode, render_proc.stdout, render_proc.stderr, msg)


def validate_tmux(path: Path) -> ValidationResult:
    sock = f"carrera-val-{os.getpid()}-{next(_TMUX_COUNTER)}"
    sock_file = Path(f"/tmp/tmux-{os.getuid()}/{sock}")
    try:
        start_proc = _run(
            ["tmux", "-L", sock, "-f", "/dev/null", "new-session", "-d", "-s", "val", "sleep 30"]
        )
        if start_proc.returncode != 0:
            return ValidationResult(
                False,
                start_proc.returncode,
                start_proc.stdout,
                start_proc.stderr,
                f"tmux isolated server failed to start: {start_proc.stderr.strip()}",
            )
        src_proc = _run(["tmux", "-L", sock, "source-file", str(path)])
        ok = (
            src_proc.returncode == 0
            and src_proc.stdout.strip() == ""
            and src_proc.stderr.strip() == ""
        )
        msg = (
            "ok"
            if ok
            else f"tmux source-file failed (rc={src_proc.returncode}, out={src_proc.stdout!r}, err={src_proc.stderr!r})"
        )
        return ValidationResult(ok, src_proc.returncode, src_proc.stdout, src_proc.stderr, msg)
    finally:
        _run(["tmux", "-L", sock, "kill-server"])
        if sock_file.exists():
            try:
                sock_file.unlink()
            except OSError:
                pass


def validate_mpv(path: Path) -> ValidationResult:
    proc = _run(
        ["mpv", "--no-config", f"--include={path}", "--idle=no", "--vo=null", "--ao=null"]
    )
    out = proc.stdout
    err = proc.stderr.strip()
    bad_markers = (
        "Error parsing option",
        "invalid color",
        "failed.",
        "Error:",
    )
    has_error = any(m.lower() in out.lower() for m in bad_markers)
    ok = proc.returncode == 0 and err == "" and not has_error
    msg = "ok" if ok else f"mpv failed (rc={proc.returncode}, err={err!r}, out_err={has_error})"
    return ValidationResult(ok, proc.returncode, proc.stdout, proc.stderr, msg)


def validate_eza(path: Path) -> ValidationResult:
    try:
        parsed = parse_yaml(path)
    except Exception as exc:
        return ValidationResult(False, 1, "", str(exc), f"eza YAML parse failed: {exc}")

    with tempfile.TemporaryDirectory(prefix="carrera_eza_") as tmp:
        tmp_path = Path(tmp)
        shutil.copy2(path, tmp_path / "theme.yml")
        proc = _run(
            ["eza", "--color=always", str(tmp_path)],
            env={"EZA_CONFIG_DIR": str(tmp_path)},
        )
        ok = proc.returncode == 0 and proc.stderr.strip() == ""
        msg = "ok" if ok else f"eza failed (rc={proc.returncode}): {proc.stderr.strip()}"
        return ValidationResult(ok, proc.returncode, proc.stdout, proc.stderr, msg, data=parsed)


def validate_git_delta(path: Path) -> ValidationResult:
    proc = _run(["git", "config", "--file", str(path), "--list"])
    ok = proc.returncode == 0 and proc.stderr.strip() == "" and proc.stdout.strip() != ""
    msg = "ok" if ok else f"git config failed (rc={proc.returncode}): {proc.stderr.strip()}"
    return ValidationResult(ok, proc.returncode, proc.stdout, proc.stderr, msg)


def validate_zsh_syntax_highlighting(path: Path) -> ValidationResult:
    syn = _run(["zsh", "-n", str(path)])
    if syn.returncode != 0 or syn.stderr.strip() != "":
        return ValidationResult(
            False,
            syn.returncode,
            syn.stdout,
            syn.stderr,
            f"zsh -n failed: {syn.stderr.strip()}",
        )
    script = (
        'typeset -A ZSH_HIGHLIGHT_STYLES; '
        'source "$1"; '
        'for k in "${(@k)ZSH_HIGHLIGHT_STYLES}"; do '
        'printf "%s\t%s\n" "$k" "${ZSH_HIGHLIGHT_STYLES[$k]}"; '
        "done"
    )
    src = _run(["zsh", "-fc", script, "_", str(path)])
    styles: dict[str, str] = {}
    for line in src.stdout.splitlines():
        if "\t" in line:
            k, v = line.split("\t", 1)
            styles[k] = v
    ok = src.returncode == 0 and src.stderr.strip() == "" and bool(styles)
    msg = "ok" if ok else f"zsh source failed (rc={src.returncode}): {src.stderr.strip()}"
    return ValidationResult(ok, src.returncode, src.stdout, src.stderr, msg, data=styles)


def validate_fzf(path: Path) -> ValidationResult:
    for shell in ("zsh", "bash"):
        syn = _run([shell, "-n", str(path)])
        if syn.returncode != 0 or syn.stderr.strip() != "":
            return ValidationResult(
                False,
                syn.returncode,
                syn.stdout,
                syn.stderr,
                f"{shell} -n failed: {syn.stderr.strip()}",
            )

    src = _run(
        ["zsh", "-fc", 'FZF_DEFAULT_OPTS=""; source "$1"; printf "%s" "$FZF_DEFAULT_OPTS"', "_", str(path)]
    )
    if src.returncode != 0 or src.stderr.strip() != "":
        return ValidationResult(
            False,
            src.returncode,
            src.stdout,
            src.stderr,
            f"fzf script source failed: {src.stderr.strip()}",
        )

    tokens = shlex.split(src.stdout)
    color_spec: str | None = None
    for idx, tok in enumerate(tokens):
        if tok.startswith("--color="):
            color_spec = tok[len("--color=") :]
        elif tok == "--color" and idx + 1 < len(tokens):
            color_spec = tokens[idx + 1]

    if not color_spec:
        return ValidationResult(
            False, 1, src.stdout, src.stderr, "No --color=... found in FZF_DEFAULT_OPTS"
        )

    fzf_proc = _run(
        ["fzf", "--filter=alpha", f"--color={color_spec}"],
        input_text="alpha\nbeta\n",
    )
    ok = (
        fzf_proc.returncode == 0
        and fzf_proc.stderr.strip() == ""
        and fzf_proc.stdout.strip() == "alpha"
    )
    msg = (
        "ok"
        if ok
        else f"fzf --filter failed (rc={fzf_proc.returncode}): {fzf_proc.stderr.strip()}"
    )
    return ValidationResult(ok, fzf_proc.returncode, fzf_proc.stdout, fzf_proc.stderr, msg, data=color_spec)


def validate_kubecolor(path: Path) -> ValidationResult:
    proc = _run(
        ["kubecolor", "version", "--client"],
        env={"KUBECOLOR_CONFIG": str(path), "KUBECONFIG": "/dev/null"},
    )
    ok = proc.returncode == 0 and proc.stderr.strip() == ""
    msg = "ok" if ok else f"kubecolor failed (rc={proc.returncode}): {proc.stderr.strip()}"
    return ValidationResult(ok, proc.returncode, proc.stdout, proc.stderr, msg)


def validate_fastfetch(path: Path) -> ValidationResult:
    proc = _run(["fastfetch", "--config", str(path), "--structure", "Title", "--pipe", "true"])
    ok = proc.returncode == 0 and proc.stderr.strip() == ""
    msg = "ok" if ok else f"fastfetch failed (rc={proc.returncode}): {proc.stderr.strip()}"
    return ValidationResult(ok, proc.returncode, proc.stdout, proc.stderr, msg)


def validate_pgcli(path: Path) -> ValidationResult:
    proc = _run(["pgcli", "--pgclirc", str(path), "--list-dsn"])
    ok = proc.returncode == 0 and proc.stderr.strip() == ""
    msg = "ok" if ok else f"pgcli failed (rc={proc.returncode}): {proc.stderr.strip()}"
    return ValidationResult(ok, proc.returncode, proc.stdout, proc.stderr, msg)


def validate_herdr(path: Path) -> ValidationResult:
    raw = path.read_text(encoding="utf-8")
    try:
        parsed = tomllib.loads(raw)
    except Exception as exc:
        return ValidationResult(False, 1, "", str(exc), f"herdr TOML parse failed: {exc}")

    with tempfile.TemporaryDirectory(prefix="carrera_herdr_") as tmp:
        xdg = Path(tmp)
        cfg_dir = xdg / "herdr"
        cfg_dir.mkdir(parents=True)
        cfg_file = cfg_dir / "config.toml"
        theme_tbl = parsed.get("theme")
        if isinstance(theme_tbl, dict) and "name" in theme_tbl:
            cfg_file.write_text(raw, encoding="utf-8")
        else:
            cfg_file.write_text('[theme]\nname = "terminal"\n\n' + raw, encoding="utf-8")

        proc = _run(["herdr", "config", "check"], env={"XDG_CONFIG_HOME": str(xdg)})
        ok = proc.returncode == 0 and proc.stderr.strip() == ""
        msg = (
            "ok"
            if ok
            else f"herdr config check failed (rc={proc.returncode}): {proc.stdout.strip()} {proc.stderr.strip()}"
        )
        return ValidationResult(ok, proc.returncode, proc.stdout, proc.stderr, msg, data=parsed)


def validate_hyprland(path: Path) -> ValidationResult:
    proc = _run(["Hyprland", "--verify-config", "--config", str(path)])
    ok = proc.returncode == 0 and proc.stderr.strip() == ""
    msg = (
        "ok"
        if ok
        else f"Hyprland --verify-config failed (rc={proc.returncode}): {proc.stdout.strip()} {proc.stderr.strip()}"
    )
    return ValidationResult(ok, proc.returncode, proc.stdout, proc.stderr, msg)
