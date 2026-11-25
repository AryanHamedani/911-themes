"""Format parsers and structural validators using pure Python 3.15 stdlib + yq/git."""

from __future__ import annotations

import configparser
import json
import plistlib
import re
import struct
import subprocess
import tomllib
import xml.etree.ElementTree as ET
import zipfile
import zlib
from pathlib import Path
from typing import Any


# ---------------------------------------------------------------------------
# PNG & JPEG binary validators
# ---------------------------------------------------------------------------

PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"


def validate_png_bytes(data: bytes) -> dict[str, Any]:
    """Strictly validate PNG signature, IHDR/IEND ordering, chunk lengths, and CRC32."""
    if len(data) < 8 or data[:8] != PNG_SIGNATURE:
        raise ValueError("Invalid PNG magic signature")

    pos = 8
    chunks: list[tuple[bytes, bytes]] = []
    while pos < len(data):
        if pos + 12 > len(data):
            raise ValueError(f"Truncated PNG chunk header at offset {pos}")
        length = struct.unpack(">I", data[pos : pos + 4])[0]
        chunk_type = data[pos + 4 : pos + 8]
        chunk_end = pos + 8 + length
        if chunk_end + 4 > len(data):
            raise ValueError(
                f"Truncated PNG chunk {chunk_type!r} at offset {pos}: declared length {length}"
            )
        chunk_data = data[pos + 8 : chunk_end]
        expected_crc = struct.unpack(">I", data[chunk_end : chunk_end + 4])[0]
        actual_crc = zlib.crc32(chunk_type + chunk_data) & 0xFFFFFFFF
        if actual_crc != expected_crc:
            raise ValueError(
                f"PNG CRC32 mismatch in chunk {chunk_type!r}: expected 0x{expected_crc:08x}, got 0x{actual_crc:08x}"
            )
        chunks.append((chunk_type, chunk_data))
        pos = chunk_end + 4
        if chunk_type == b"IEND":
            break

    if pos != len(data):
        raise ValueError(f"Trailing bytes after PNG IEND chunk: {len(data) - pos} bytes")
    if not chunks:
        raise ValueError("PNG contains no chunks")
    if chunks[0][0] != b"IHDR":
        raise ValueError(f"First PNG chunk must be IHDR, got {chunks[0][0]!r}")
    if chunks[-1][0] != b"IEND" or len(chunks[-1][1]) != 0:
        raise ValueError("Last PNG chunk must be empty IEND")

    ihdr = chunks[0][1]
    if len(ihdr) != 13:
        raise ValueError(f"Invalid IHDR length {len(ihdr)} (expected 13)")
    width, height = struct.unpack(">II", ihdr[:8])
    if width == 0 or height == 0:
        raise ValueError(f"Invalid PNG dimensions {width}x{height}")

    return {
        "width": width,
        "height": height,
        "chunks": [c[0].decode("ascii", errors="replace") for c in chunks],
    }


def validate_jpeg_bytes(data: bytes) -> dict[str, Any]:
    """Basic JPEG SOI/EOI marker validation."""
    if len(data) < 4 or data[:2] != b"\xff\xd8" or data[-2:] != b"\xff\xd9":
        raise ValueError("Invalid JPEG SOI/EOI markers")
    return {"bytes": len(data)}


def generate_solid_png(width: int, height: int, rgb: tuple[int, int, int]) -> bytes:
    """Create a minimal valid 8-bit RGB PNG image for self-test fixtures."""

    def _chunk(ctype: bytes, payload: bytes) -> bytes:
        crc = zlib.crc32(ctype + payload) & 0xFFFFFFFF
        return struct.pack(">I", len(payload)) + ctype + payload + struct.pack(">I", crc)

    r, g, b = rgb
    ihdr = struct.pack(">IIBBBBB", width, height, 8, 2, 0, 0, 0)
    row = b"\x00" + bytes([r, g, b]) * width
    raw = row * height
    idat = zlib.compress(raw)
    return PNG_SIGNATURE + _chunk(b"IHDR", ihdr) + _chunk(b"IDAT", idat) + _chunk(b"IEND", b"")


# ---------------------------------------------------------------------------
# JSON / JSONC
# ---------------------------------------------------------------------------


def strip_jsonc_comments(text: str) -> str:
    """Strip // and /* ... */ comments outside JSON string literals."""
    out: list[str] = []
    n = len(text)
    i = 0
    in_string = False

    while i < n:
        ch = text[i]
        if in_string:
            out.append(ch)
            if ch == "\\":
                if i + 1 < n:
                    out.append(text[i + 1])
                    i += 2
                    continue
            elif ch == '"':
                in_string = False
            i += 1
            continue

        if ch == '"':
            in_string = True
            out.append(ch)
            i += 1
        elif ch == "/" and i + 1 < n and text[i + 1] == "/":
            i += 2
            while i < n and text[i] != "\n":
                i += 1
        elif ch == "/" and i + 1 < n and text[i + 1] == "*":
            i += 2
            closed = False
            while i + 1 < n:
                if text[i] == "*" and text[i + 1] == "/":
                    i += 2
                    closed = True
                    break
                if text[i] == "\n":
                    out.append("\n")
                i += 1
            if not closed:
                raise ValueError("Unclosed /* ... */ comment in JSONC")
        else:
            out.append(ch)
            i += 1

    if in_string:
        raise ValueError("Unclosed string literal in JSONC")
    return "".join(out)


def parse_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def parse_jsonc(path: Path) -> Any:
    raw = path.read_text(encoding="utf-8")
    stripped = strip_jsonc_comments(raw)
    return json.loads(stripped)


# ---------------------------------------------------------------------------
# TOML / YAML / Plist XML / INI / Gitconfig
# ---------------------------------------------------------------------------


def parse_toml(path: Path) -> dict[str, Any]:
    with open(path, "rb") as f:
        return tomllib.load(f)


_RUBY_YAML_DUP_CHECK = r"""
require "psych"

def check_dups(node, path = "root")
  return unless node
  if node.is_a?(Psych::Nodes::Mapping)
    seen = {}
    node.children.each_slice(2) do |k, v|
      kv = begin
        k.to_ruby
      rescue StandardError
        k.respond_to?(:value) ? k.value : k.inspect
      end
      if seen.key?(kv)
        warn "Duplicate YAML key #{kv.inspect} at #{path}"
        exit 2
      end
      seen[kv] = true
      check_dups(v, "#{path}.#{kv}")
    end
  elsif node.respond_to?(:children) && node.children
    node.children.each_with_index { |c, i| check_dups(c, "#{path}[#{i}]") }
  end
end

stream = Psych.parse_stream(File.read(ARGV[0], encoding: "UTF-8"), filename: ARGV[0])
check_dups(stream)
"""


def parse_yaml(path: Path) -> Any:
    dup_proc = subprocess.run(
        ["ruby", "-e", _RUBY_YAML_DUP_CHECK, str(path)],
        capture_output=True,
        text=True,
        timeout=15,
    )
    if dup_proc.returncode != 0:
        raise ValueError(
            f"YAML Psych parse/duplicate-key check failed for {path}: {dup_proc.stderr.strip()}"
        )
    proc = subprocess.run(
        ["yq", "-o=json", ".", str(path)],
        capture_output=True,
        text=True,
        timeout=15,
    )
    if proc.returncode != 0:
        raise ValueError(f"yq YAML parse failed for {path}: {proc.stderr.strip()}")
    if not proc.stdout.strip():
        raise ValueError(f"YAML file produced empty JSON output: {path}")
    return json.loads(proc.stdout)


def parse_plist(path: Path) -> Any:
    # Check strict XML structure first via ElementTree, then plistlib
    ET.parse(path)
    with open(path, "rb") as f:
        data = plistlib.load(f)
    if not isinstance(data, dict):
        raise ValueError(f"Expected plist root dict in {path}, got {type(data).__name__}")
    return data


def parse_ini(path: Path) -> configparser.ConfigParser:
    cp = configparser.ConfigParser(interpolation=None)
    cp.optionxform = str  # preserve case
    text = path.read_text(encoding="utf-8")
    cp.read_string(text, source=str(path))
    return cp


def parse_git_config(path: Path) -> dict[str, str]:
    proc = subprocess.run(
        ["git", "config", "--file", str(path), "--list"],
        capture_output=True,
        text=True,
        timeout=10,
    )
    if proc.returncode != 0:
        raise ValueError(f"git config parse failed for {path}: {proc.stderr.strip()}")
    result: dict[str, str] = {}
    for line in proc.stdout.splitlines():
        if "=" in line:
            k, v = line.split("=", 1)
            result[k] = v
    return result


# ---------------------------------------------------------------------------
# Strict CSS lexer & validator
# ---------------------------------------------------------------------------

_CSS_DEFINE_COLOR_RE = re.compile(
    r"@define-color\s+([A-Za-z_][A-Za-z0-9_-]*)\s+([^;{}\n]+);"
)
_CSS_HEX_TOKEN_RE = re.compile(r"(?<![A-Za-z0-9_-])#([0-9A-Za-z]+)\b")
_CSS_RGB_CALL_RE = re.compile(r"\brgba?\(([^)]*)\)", re.IGNORECASE)
_CSS_DISALLOWED_COLOR_FUNC_RE = re.compile(
    r"\b(?:hsla?|oklch|oklab|hwb|lch|lab)\s*\(", re.IGNORECASE
)


def _strip_css_comments_and_check_balance(text: str) -> str:
    """Validate CSS comments, strings, braces {}, and parens (), returning comment-free CSS."""
    out: list[str] = []
    n = len(text)
    i = 0
    brace_depth = 0
    paren_depth = 0
    quote_char: str | None = None

    while i < n:
        ch = text[i]
        if quote_char is not None:
            out.append(ch)
            if ch == "\\":
                if i + 1 < n:
                    out.append(text[i + 1])
                    i += 2
                    continue
            elif ch == quote_char:
                quote_char = None
            i += 1
            continue

        if ch in ('"', "'"):
            quote_char = ch
            out.append(ch)
            i += 1
        elif ch == "/" and i + 1 < n and text[i + 1] == "*":
            i += 2
            closed = False
            while i + 1 < n:
                if text[i] == "*" and text[i + 1] == "/":
                    i += 2
                    closed = True
                    break
                if text[i] == "\n":
                    out.append("\n")
                i += 1
            if not closed:
                raise ValueError("Unclosed /* ... */ comment in CSS")
            out.append(" ")
        else:
            if ch == "{":
                brace_depth += 1
            elif ch == "}":
                brace_depth -= 1
                if brace_depth < 0:
                    raise ValueError("Unbalanced '}' in CSS")
            elif ch == "(":
                paren_depth += 1
            elif ch == ")":
                paren_depth -= 1
                if paren_depth < 0:
                    raise ValueError("Unbalanced ')' in CSS")
            out.append(ch)
            i += 1

    if quote_char is not None:
        raise ValueError(f"Unclosed {quote_char} string literal in CSS")
    if brace_depth != 0:
        raise ValueError(f"Unbalanced '{{' in CSS (remaining depth {brace_depth})")
    if paren_depth != 0:
        raise ValueError(f"Unbalanced '(' in CSS (remaining depth {paren_depth})")

    return "".join(out)


def _split_top_level_semicolons(block_body: str) -> list[str]:
    stmts: list[str] = []
    buf: list[str] = []
    paren_depth = 0
    quote_char: str | None = None
    i = 0
    n = len(block_body)
    while i < n:
        ch = block_body[i]
        if quote_char is not None:
            buf.append(ch)
            if ch == "\\" and i + 1 < n:
                buf.append(block_body[i + 1])
                i += 2
                continue
            if ch == quote_char:
                quote_char = None
        else:
            if ch in ('"', "'"):
                quote_char = ch
                buf.append(ch)
            elif ch == "(":
                paren_depth += 1
                buf.append(ch)
            elif ch == ")":
                paren_depth -= 1
                buf.append(ch)
            elif ch == ";" and paren_depth == 0:
                stmt = "".join(buf).strip()
                if stmt:
                    stmts.append(stmt)
                buf.clear()
                i += 1
                continue
            else:
                buf.append(ch)
        i += 1
    tail = "".join(buf).strip()
    if tail:
        stmts.append(tail)
    return stmts


def _extract_css_value_colors(
    value: str,
    hexes: list[str],
    rgb_tuples: list[tuple[int, int, int]],
    malformed: list[str],
) -> None:
    # Remove url(...) fragments so SVG #id refs are not confused with hex colors
    cleaned = re.sub(r"url\([^)]*\)", "", value, flags=re.IGNORECASE)
    for bad_fn in _CSS_DISALLOWED_COLOR_FUNC_RE.finditer(cleaned):
        malformed.append(f"disallowed CSS color function {bad_fn.group(0).strip()}")
    for m in _CSS_HEX_TOKEN_RE.finditer(cleaned):
        raw = m.group(1)
        if re.fullmatch(r"[0-9a-fA-F]{6}|[0-9a-fA-F]{8}", raw):
            hexes.append("#" + raw.lower())
        else:
            malformed.append("#" + raw)

    for m in _CSS_RGB_CALL_RE.finditer(cleaned):
        inner = m.group(1).strip()
        if "var(" in inner:
            continue
        # Handle comma-separated or space-separated CSS Color 4 syntax (with optional / alpha)
        if "," in inner:
            parts = [p.strip() for p in inner.split(",")]
        else:
            slash_parts = inner.split("/")
            rgb_parts = slash_parts[0].split()
            parts = rgb_parts + ([slash_parts[1].strip()] if len(slash_parts) > 1 else [])
        if len(parts) not in (3, 4):
            malformed.append(m.group(0))
            continue
        try:
            rgb = tuple(int(parts[idx]) for idx in range(3))
        except ValueError:
            malformed.append(m.group(0))
            continue
        if any(not (0 <= c <= 255) for c in rgb):
            malformed.append(m.group(0))
            continue
        if len(parts) == 4:
            a_str = parts[3]
            try:
                if a_str.endswith("%"):
                    a_val = float(a_str[:-1]) / 100.0
                else:
                    a_val = float(a_str)
            except ValueError:
                malformed.append(m.group(0))
                continue
            if not (0.0 <= a_val <= 1.0):
                malformed.append(m.group(0))
                continue
        rgb_tuples.append(rgb)


def validate_css(text: str) -> dict[str, Any]:
    """Strictly parse and validate CSS, extracting @define-color, variables, selectors, and colors."""
    cleaned = _strip_css_comments_and_check_balance(text)

    # Check for unclosed @define-color lines (must terminate with ;)
    for line in cleaned.splitlines():
        s = line.strip()
        if s.startswith("@define-color") and not s.endswith(";"):
            raise ValueError(f"@define-color missing semicolon: {s!r}")

    define_colors: dict[str, str] = {}
    for m in _CSS_DEFINE_COLOR_RE.finditer(cleaned):
        define_colors[m.group(1)] = m.group(2).strip()

    # Extract selectors and innermost rule blocks
    selectors: list[str] = []
    declarations: list[tuple[str, str]] = []
    variables: dict[str, str] = {}

    # Walk blocks iteratively
    stack: list[tuple[str, int]] = []
    n = len(cleaned)
    i = 0
    last_header_start = 0
    quote_char: str | None = None

    while i < n:
        ch = cleaned[i]
        if quote_char is not None:
            if ch == "\\" and i + 1 < n:
                i += 2
                continue
            if ch == quote_char:
                quote_char = None
            i += 1
            continue
        if ch in ('"', "'"):
            quote_char = ch
        elif ch == "{":
            header = cleaned[last_header_start:i].strip()
            # Keep only trailing selector after last ';' if at-rules preceded it
            if ";" in header:
                header = header.rsplit(";", 1)[-1].strip()
            if header:
                selectors.append(header)
            stack.append((header, i + 1))
            last_header_start = i + 1
        elif ch == "}":
            header, body_start = stack.pop()
            body = cleaned[body_start:i]
            # Only parse declarations in leaf blocks (blocks that don't contain nested '{')
            if "{" not in body:
                for stmt in _split_top_level_semicolons(body):
                    if ":" not in stmt:
                        raise ValueError(
                            f"Malformed CSS declaration without ':' in {header!r}: {stmt!r}"
                        )
                    prop, val = stmt.split(":", 1)
                    prop_s = prop.strip()
                    val_s = val.strip()
                    if not prop_s or not val_s:
                        raise ValueError(f"Empty CSS property or value in {header!r}: {stmt!r}")
                    declarations.append((prop_s, val_s))
                    if prop_s.startswith("--"):
                        variables[prop_s] = val_s
            last_header_start = i + 1
        i += 1

    hexes: list[str] = []
    rgb_tuples: list[tuple[int, int, int]] = []
    malformed: list[str] = []

    for val in define_colors.values():
        _extract_css_value_colors(val, hexes, rgb_tuples, malformed)
    for _, val in declarations:
        _extract_css_value_colors(val, hexes, rgb_tuples, malformed)

    if malformed:
        raise ValueError(f"Malformed color syntax in CSS: {malformed}")

    return {
        "define_colors": define_colors,
        "variables": variables,
        "declarations": declarations,
        "selectors": selectors,
        "hexes": hexes,
        "rgb_tuples": rgb_tuples,
    }


# ---------------------------------------------------------------------------
# Telegram Desktop (.tdesktop-theme) ZIP & colors.tdesktop-theme parser
# ---------------------------------------------------------------------------

REQUIRED_TELEGRAM_PREFIXES: tuple[str, ...] = (
    "window",
    "title",
    "dialogs",
    "history",
    "msg",
    "mediaview",
    "active",
    "box",
    "menu",
    "scroll",
    "tooltip",
    "notification",
)


def _strip_tdesktop_comments(text: str) -> str:
    """Strip /* ... */ and // ... comments from colors.tdesktop-theme."""
    out: list[str] = []
    n = len(text)
    i = 0
    while i < n:
        if text[i : i + 2] == "/*":
            i += 2
            closed = False
            while i + 1 < n:
                if text[i : i + 2] == "*/":
                    i += 2
                    closed = True
                    break
                if text[i] == "\n":
                    out.append("\n")
                i += 1
            if not closed:
                raise ValueError("Unclosed /* ... */ comment in colors.tdesktop-theme")
        elif text[i : i + 2] == "//":
            i += 2
            while i < n and text[i] != "\n":
                i += 1
        else:
            out.append(text[i])
            i += 1
    return "".join(out)


def validate_tdesktop_theme(zip_path: Path) -> dict[str, Any]:
    """Validate .tdesktop-theme ZIP archive, background image, key syntax, and alias closure."""
    if not zipfile.is_zipfile(zip_path):
        raise ValueError(f"Not a valid ZIP archive: {zip_path}")

    with zipfile.ZipFile(zip_path, "r") as zf:
        corrupt = zf.testzip()
        if corrupt is not None:
            raise ValueError(f"Corrupt ZIP entry {corrupt!r} in {zip_path}")

        names = zf.namelist()
        nested = [n for n in names if "/" in n or "\\" in n]
        if nested:
            raise ValueError(
                f".tdesktop-theme must place files at ZIP root, found nested entries: {nested}"
            )
        if "colors.tdesktop-theme" not in names:
            raise ValueError("Missing colors.tdesktop-theme in ZIP root")

        bg_candidates = [
            n
            for n in ("background.png", "background.jpg", "tiled.png", "tiled.jpg")
            if n in names
        ]
        if not bg_candidates:
            raise ValueError(
                f"Missing background.(png|jpg) or tiled.(png|jpg) in ZIP root: {names}"
            )

        bg_name = bg_candidates[0]
        bg_bytes = zf.read(bg_name)
        if bg_name.endswith(".png"):
            bg_info = validate_png_bytes(bg_bytes)
        else:
            bg_info = validate_jpeg_bytes(bg_bytes)

        colors_raw = zf.read("colors.tdesktop-theme").decode("utf-8")

    cleaned = _strip_tdesktop_comments(colors_raw)
    entries: dict[str, str] = {}
    hex_values: list[str] = []

    for lineno, raw_line in enumerate(cleaned.splitlines(), start=1):
        line = raw_line.strip()
        if not line:
            continue
        m = re.fullmatch(r"([A-Za-z0-9_]+)\s*:\s*([^;]+);", line)
        if not m:
            raise ValueError(
                f"Invalid colors.tdesktop-theme syntax at line {lineno}: {line!r}"
            )
        key, val = m.group(1), m.group(2).strip()
        entries[key] = val

    if len(entries) < 100:
        raise ValueError(
            f"colors.tdesktop-theme has {len(entries)} keys; expected >= 100"
        )

    # Validate values & alias references (must resolve without cycles or dangling keys)
    for key, val in entries.items():
        if val.startswith("#"):
            if not re.fullmatch(r"#[0-9a-fA-F]{6}([0-9a-fA-F]{2})?", val):
                raise ValueError(f"Invalid hex value for {key!r}: {val!r}")
            hex_values.append(val.lower())
        else:
            seen: set[str] = {key}
            cur = val
            while not cur.startswith("#"):
                if cur not in entries:
                    raise ValueError(
                        f"Dangling alias reference in colors.tdesktop-theme: {key!r} -> {cur!r}"
                    )
                if cur in seen:
                    raise ValueError(
                        f"Cyclic alias reference in colors.tdesktop-theme involving {cur!r}"
                    )
                seen.add(cur)
                cur = entries[cur]
            if not re.fullmatch(r"#[0-9a-fA-F]{6}([0-9a-fA-F]{2})?", cur):
                raise ValueError(
                    f"Alias {key!r} -> {val!r} resolved to invalid hex {cur!r}"
                )

    lower_keys = [k.lower() for k in entries]
    missing_groups = [
        prefix
        for prefix in REQUIRED_TELEGRAM_PREFIXES
        if not any(k.startswith(prefix) for k in lower_keys)
    ]
    if missing_groups:
        raise ValueError(
            f"colors.tdesktop-theme missing required UI groups: {missing_groups}"
        )

    return {
        "namelist": names,
        "background": bg_name,
        "bg_info": bg_info,
        "entries": entries,
        "hexes": hex_values,
    }


# ---------------------------------------------------------------------------
# Line-based & Lua parsers
# ---------------------------------------------------------------------------


def parse_btop_theme(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    result: dict[str, str] = {}
    for lineno, raw_line in enumerate(text.splitlines(), start=1):
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        m = re.fullmatch(r'theme\[([a-z_]+)\]="(#[0-9a-fA-F]{6})"', line)
        if not m:
            raise ValueError(
                f"Invalid btop.theme syntax at line {lineno}: {line!r}"
            )
        result[m.group(1)] = m.group(2).lower()
    if not result:
        raise ValueError(f"No theme entries found in {path}")
    return result


def parse_ghostty(path: Path) -> list[tuple[str, str]]:
    text = path.read_text(encoding="utf-8")
    pairs: list[tuple[str, str]] = []
    for lineno, raw_line in enumerate(text.splitlines(), start=1):
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        if "=" not in line:
            raise ValueError(f"Invalid Ghostty line {lineno} (expected key = val): {line!r}")
        k, v = line.split("=", 1)
        pairs.append((k.strip(), v.strip()))
    return pairs


def parse_kitty(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    result: dict[str, str] = {}
    for lineno, raw_line in enumerate(text.splitlines(), start=1):
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        # Strip trailing comment if preceded by whitespace and not a hex color
        parts = line.split()
        if len(parts) < 2:
            raise ValueError(f"Invalid Kitty line {lineno}: {line!r}")
        key = parts[0]
        if "=" in key or parts[1].startswith("="):
            raise ValueError(f"Kitty config must be space-separated, found '=' at line {lineno}: {line!r}")
        val = parts[1]
        result[key] = val
    return result


def parse_mpv_conf(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    result: dict[str, str] = {}
    for lineno, raw_line in enumerate(text.splitlines(), start=1):
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        # Strip inline comment outside quotes
        cleaned = re.sub(r'\s+#(?![0-9a-fA-F]{6,8}\b).*$', "", line).strip()
        if "=" not in cleaned:
            raise ValueError(f"Invalid mpv.conf line {lineno}: {line!r}")
        k, v = cleaned.split("=", 1)
        k = k.strip()
        v = v.strip()
        if (v.startswith('"') and v.endswith('"')) or (v.startswith("'") and v.endswith("'")):
            v = v[1:-1]
        result[k] = v
    return result


def parse_hyprland_conf(path: Path) -> dict[str, dict[str, str]]:
    text = path.read_text(encoding="utf-8")
    sections: dict[str, dict[str, str]] = {"_root": {}}
    stack: list[str] = []
    for lineno, raw_line in enumerate(text.splitlines(), start=1):
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        # Strip trailing comment (outside rgba(...) and #...)
        line = re.sub(r"\s+#(?![0-9a-fA-F]{6,8}\b).*$", "", line).strip()
        if line.endswith("{"):
            sec = line[:-1].strip()
            full_sec = ".".join(stack + [sec]) if stack else sec
            stack.append(sec)
            sections.setdefault(full_sec, {})
        elif line == "}":
            if not stack:
                raise ValueError(f"Unbalanced '}}' in Hyprland config line {lineno}")
            stack.pop()
        elif "=" in line:
            k, v = line.split("=", 1)
            cur = ".".join(stack) if stack else "_root"
            sections.setdefault(cur, {})[k.strip()] = v.strip()
        else:
            raise ValueError(f"Unrecognized Hyprland config line {lineno}: {line!r}")
    if stack:
        raise ValueError(f"Unclosed Hyprland section(s): {stack}")
    return sections


_LUA_LONG_OPEN_RE = re.compile(r"\[(=*)\[")
_LUA_URL_RE = re.compile(r"https?://[^\s'\"<>]+")
_LUA_HASH_RE = re.compile(r"(?<![A-Za-z0-9_])#([0-9a-zA-Z]+)")
_LUA_HEX_INT_RE = re.compile(r"(?<![0-9A-Za-z_])0[xX]([0-9a-fA-F]{6})(?![0-9a-fA-F])")


def _scan_lua(text: str) -> tuple[str, list[str]]:
    """Strip Lua comments and return (code_outside_strings, list_of_string_contents)."""
    code_out: list[str] = []
    strings: list[str] = []
    n = len(text)
    i = 0

    while i < n:
        ch = text[i]
        if text[i : i + 2] == "--":
            long_m = _LUA_LONG_OPEN_RE.match(text, i + 2)
            if long_m:
                eqs = long_m.group(1)
                close_tok = "]" + eqs + "]"
                end = text.find(close_tok, long_m.end())
                if end == -1:
                    raise ValueError("Unclosed Lua long block comment")
                code_out.append("\n" * text[long_m.end() : end].count("\n"))
                i = end + len(close_tok)
            else:
                i += 2
                while i < n and text[i] != "\n":
                    i += 1
        elif ch in ('"', "'"):
            quote = ch
            i += 1
            buf: list[str] = []
            while i < n:
                c = text[i]
                if c == "\\" and i + 1 < n:
                    buf.append(text[i : i + 2])
                    i += 2
                    continue
                if c == quote:
                    i += 1
                    break
                buf.append(c)
                i += 1
            strings.append("".join(buf))
            code_out.append(" ")
        elif ch == "[":
            long_m = _LUA_LONG_OPEN_RE.match(text, i)
            if long_m:
                eqs = long_m.group(1)
                close_tok = "]" + eqs + "]"
                end = text.find(close_tok, long_m.end())
                if end == -1:
                    raise ValueError("Unclosed Lua long string literal")
                strings.append(text[long_m.end() : end])
                code_out.append(" ")
                i = end + len(close_tok)
                continue
            code_out.append(ch)
            i += 1
        else:
            code_out.append(ch)
            i += 1

    return "".join(code_out), strings


def strip_lua_comments(text: str) -> str:
    """Strip Lua block and line comments outside string literals."""
    out: list[str] = []
    n = len(text)
    i = 0
    while i < n:
        ch = text[i]
        if text[i : i + 2] == "--":
            long_m = _LUA_LONG_OPEN_RE.match(text, i + 2)
            if long_m:
                eqs = long_m.group(1)
                close_tok = "]" + eqs + "]"
                end = text.find(close_tok, long_m.end())
                if end == -1:
                    raise ValueError("Unclosed Lua long block comment")
                out.append("\n" * text[long_m.end() : end].count("\n"))
                i = end + len(close_tok)
            else:
                i += 2
                while i < n and text[i] != "\n":
                    i += 1
        elif ch in ('"', "'"):
            quote = ch
            out.append(ch)
            i += 1
            while i < n:
                c = text[i]
                out.append(c)
                if c == "\\" and i + 1 < n:
                    out.append(text[i + 1])
                    i += 2
                    continue
                if c == quote:
                    i += 1
                    break
                i += 1
        elif ch == "[":
            long_m = _LUA_LONG_OPEN_RE.match(text, i)
            if long_m:
                eqs = long_m.group(1)
                close_tok = "]" + eqs + "]"
                end = text.find(close_tok, long_m.end())
                if end == -1:
                    raise ValueError("Unclosed Lua long string literal")
                out.append(text[i : end + len(close_tok)])
                i = end + len(close_tok)
                continue
            out.append(ch)
            i += 1
        else:
            out.append(ch)
            i += 1
    return "".join(out)


def extract_lua_hex_literals(text: str) -> tuple[list[str], list[str]]:
    """Return (valid_hexes, malformed_hex_literals) from Lua strings and 0xRRGGBB integer literals."""
    code_outside_strings, strings = _scan_lua(text)
    valid: list[str] = []
    malformed: list[str] = []
    for s in strings:
        cleaned = _LUA_URL_RE.sub("", s)
        for m in _LUA_HASH_RE.finditer(cleaned):
            lit = "#" + m.group(1)
            if re.fullmatch(r"#[0-9a-fA-F]{6}", lit):
                valid.append(lit.lower())
            else:
                malformed.append(lit)
    for m in _LUA_HEX_INT_RE.finditer(code_outside_strings):
        valid.append("#" + m.group(1).lower())
    return valid, malformed
