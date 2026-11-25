"""R4 isolation baseline SHA-256 snapshot and reference repository integrity checks."""

from __future__ import annotations

import hashlib
import subprocess
from pathlib import Path

BASELINE_FILE_SHA256: dict[str, str] = {
    "/home/aryan/.config/alacritty/alacritty.toml": "3e341215143a2dd4f3cf5322b1a7d9e4c9f7a7f8f4fcded7bddc3f584a22d26d",
    "/home/aryan/.config/bat/config": "cc8c0e6c24041533f620cc4cf425cad569ce58696cafd2b5798e65824dca8916",
    "/home/aryan/.config/btop/btop.conf": "4e17dd28c43948af48a408ed9b0901c008e57dfe3b8fcf09649ec10f28746137",
    "/home/aryan/.config/cliamp/config.toml": "af232a4d0a8d29d23c1b72e399a6956d4c74c53d966b86bfd16d7efeee4ad6ed",
    "/home/aryan/.config/fcitx5/conf/classicui.conf": "7fcab0f08da73828af2a27fefb36a324e0bb3f4fd233a01e1bbcb76224cc0cc2",
    "/home/aryan/.config/foot/foot.ini": "d4bf854c8fb4c49422e0e39a7494e448602b43a19cafd300a86cfd5985a983e5",
    "/home/aryan/.config/ghostty/config": "8e4017b55236cfa98d00c0e80b326b3d72bb7dbb60c3768594d26e31d7f388bb",
    "/home/aryan/.config/git/config": "011562c855a3a494b476ef1dad77858f8b1e49c407aeac2fb33683096abd6782",
    "/home/aryan/.config/git/omarchy-delta.gitconfig": "6f8490e407caed3d27b71a91dfda6809f2a5cf258f8bce63726f7c9151aaf2ab",
    "/home/aryan/.config/herdr/config.toml": "40ffd3d13e05e14c46a965d244ed98439991a8ff5490ab558bb356c7ab92f8d0",
    "/home/aryan/.config/hypr/hyprland.lua": "39974ad22f150e7b47f407a808ed60299dbec53a80f7908425e5b153ace3fe8d",
    "/home/aryan/.config/hypr/looknfeel.lua": "646db6e60bbf5b8b351bf255e169a97c4c18530847f8eb48b5519fbd11c24f2f",
    "/home/aryan/.config/hyprland-preview-share-picker/config.yaml": "b2eb82413614b69ff03f145888a23ce06aaffe903a018ad0ffbe6ddade161fab",
    "/home/aryan/.config/imv/config": "3350ffbb8004f493846129d72f5ab96cb3a10ad62e70c60962792a9fe9b69b75",
    "/home/aryan/.config/k9s/config.yaml": "7c0975ca067a79ee22b495af0a23673071b130f9a817a173d2bddd86ae79aa36",
    "/home/aryan/.config/k9s/skins/omarchy.yaml": "03ef46cd667c922aff6022f94eabb6f1742618341bbc15b79b4194aea8ca2fbd",
    "/home/aryan/.config/kitty/kitty.conf": "1869e1ea69076ecdf513d5a5464a090c323e0f15244a2bbd3cc77fa2546d93b3",
    "/home/aryan/.config/lazydocker/config.yml": "583c200b52fe93715f6795a620c888617a52bc61ee0b47a7f52215089a6dd9ca",
    "/home/aryan/.config/lazygit/config.yml": "4533a352a4787034aa2ab21d416570aa70a3f0f80145e8e3eeb5a5280cd71fe9",
    "/home/aryan/.config/nvim/init.lua": "3b2d6e9976a515b7c8df08ed7c7f61a5751e9c08a6ff5579d621b87312c9e2c6",
    "/home/aryan/.config/nvim/lua/config/lazy.lua": "14653a615b10689aa91915f45c284d07d5e7cb6c5f21fdbbf82c7664b9db4eb0",
    "/home/aryan/.config/nvim/lazyvim.json": "483304d02fd494df5c7de230b190a6ed230b6df7b47edd1748be1ecfb439d1c6",
    "/home/aryan/.config/nvim/lua/plugins/theme.lua": "21baf00105f6b470da4a79218e00833fa921e791672ea2eab66e0b87d0eba45f",
    "/home/aryan/.config/nvim/lua/plugins/all-themes.lua": "5747b94480c3688ac5bdde70b9aa3e3a04491acf1b1f38ea756ee64cb9995ad0",
    "/home/aryan/.config/nvim/lua/plugins/omarchy-theme-hotreload.lua": "d4f74ba06eec038006daf7ac509ac4102270c634c6b5a80babce037503a8e2a1",
    "/home/aryan/.config/nvim/lua/plugins/lualine-transparent.lua": "d59f78b55f99ced1423db44b84b97f855daa49e7ba8b9ce9a432aab73075bcb7",
    "/home/aryan/.config/nvim/plugin/after/transparency.lua": "2f4ab7aa4ddf3ee57a6ab9fdd4fd467659b0843703989a977f3735dc324418cc",
    "/home/aryan/.config/obsidian/obsidian.json": "202b9f15a07a870bf5b78230a2d36f3bf99bd4fec425eec1b672bf7164c848f7",
    "/home/aryan/.config/opencode/opencode.json": "8e1e55250539456dbe7e5a68e5bba9c84fa575ce21dcf15816e11a4ae429bb4e",
    "/home/aryan/.config/opencode/tui.jsonc": "6443aefa781c310f4beec27e3308ee37e4b2cae0c875556701940493929025e0",
    "/home/aryan/.config/starship.toml": "b17c9b5f096fc125e97050e359171c6011d6b3c7d7e9ac28f630e75b4d4bb9db",
    "/home/aryan/.config/tmux/tmux.conf": "d3eeec762196b3132d4b187ed2eb95d113cea698a3833fe87a0f60df6e38e544",
    "/home/aryan/.config/xournalpp/settings.xml": "1c1a9efbf1b6dc7813bf3440fd5bf8409fc283e8d0192ca297dc36a10e12c846",
    "/home/aryan/.claude/settings.json": "bfc180925d886ef2e851e2ca3886ac5b9b356147e8e68b2b50738c1d792ad2c4",
    "/home/aryan/.claude/themes/omarchy.json": "63e46d5672eee8f99d56093f50417abcceccd126cecf77dce6f24f0e6b9bf676",
    "/home/aryan/.pi/agent/settings.json": "7b779eab03a4dd34c2c87b24d796c9a2ae45af3593159bcf4fe0c71258c90642",
    "/home/aryan/.pi/agent/themes/omarchy-system.json": "e92cb0f7ecab3c90dde033a33c148a7798684e4c2a4d1f429ee1d733d31c6af2",
    "/home/aryan/.codex/config.toml": "6a19fb2c01cd8f405ac9f3b504353e7a859f1f232011e5578b105524cfdda908",
    "/home/aryan/.config/Antigravity IDE/User/settings.json": "73d0cccf3e73178bd26f2a7723e65b89615bc1187f9a0b9bc6e419470ffa9604",
    "/home/aryan/.zshrc": "7fcd675ddce1df81564aa937a83543bcc0bd7327a9d04c8f9d09b931897fb59e",
    "/home/aryan/.local/state/omarchy/current/theme.name": "3d7d85ca25f352be341a5908d1cd57dcd11659eabbe83b5477332e3ec324f781",
    "/home/aryan/.local/share/fcitx5/themes/omarchy/theme.conf": "eb350832740e73eb346a312eb4a58b5a68e396be6e5cf335dde32cd940c46b18",
    "/home/aryan/.config/zen/i64rv1pg.Default (release)/chrome/zen-themes.css": "f257f64fa3152a8b66c053435ab3b53c25304d6f8861a3a6c2c5f58df57e2d5d",
}

ZEN_PROFILE_DIR = Path("/home/aryan/.config/zen/i64rv1pg.Default (release)")

BASELINE_ABSENT_PATHS: tuple[str, ...] = (
    "/etc/xdg/gtk-3.0/settings.ini",
    "/home/aryan/.config/gtk-3.0/settings.ini",
    "/home/aryan/.config/gtk-4.0/gtk.css",
    "/home/aryan/.config/zen/i64rv1pg.Default (release)/chrome/userChrome.css",
    "/home/aryan/.config/zen/i64rv1pg.Default (release)/chrome/userContent.css",
)

REFERENCE_REPO_HEAD = "2779d4bacfff05133456b8ec8806a60a706a574b"
REFERENCE_FILE_SHA256: dict[str, str] = {
    "colors.toml": "0787d5a2381a649ab857c2c9634a470bd59dc9ac275cec0ad61b98ff29745f7a",
    "btop.theme": "f16c697926f0388d29f47ae435dc4c361282459df1eef479c0a91acb5cdea78b",
    "icons.theme": "1e2b9f6caf14f72f8c5812942c07a56eb48fa42240ebfbd09e4694f3a414f30c",
}


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        while chunk := f.read(65536):
            h.update(chunk)
    return h.hexdigest()


def verify_baseline_files(baseline_map: dict[str, str] | None = None) -> list[str]:
    """Return list of mismatch/missing error strings for baseline R4 files."""
    target = baseline_map if baseline_map is not None else BASELINE_FILE_SHA256
    errors: list[str] = []
    for path_str, expected_hash in target.items():
        p = Path(path_str)
        if not p.exists():
            errors.append(f"Baseline file missing: {path_str}")
            continue
        actual_hash = sha256_file(p)
        if actual_hash != expected_hash:
            errors.append(
                f"Baseline SHA-256 mismatch for {path_str}: expected {expected_hash}, got {actual_hash}"
            )
    return errors


def verify_absent_paths(paths: tuple[str, ...] = BASELINE_ABSENT_PATHS) -> list[str]:
    errors: list[str] = []
    for path_str in paths:
        if Path(path_str).exists():
            errors.append(f"Path must remain absent under R4, but exists: {path_str}")
    return errors


def verify_zen_profile_isolation(profile_dir: Path = ZEN_PROFILE_DIR) -> list[str]:
    """Verify Zen Browser prefs.js has no Carrera/legacyUserProfileCustomizations activation."""
    errors: list[str] = []
    prefs = profile_dir / "prefs.js"
    if prefs.is_file():
        text = prefs.read_text(encoding="utf-8", errors="replace")
        if "carrera" in text.lower():
            errors.append(f"Zen prefs.js unexpectedly references 'carrera': {prefs}")
        if "toolkit.legacyUserProfileCustomizations.stylesheets" in text and "true" in text.lower():
            for line in text.splitlines():
                if "toolkit.legacyUserProfileCustomizations.stylesheets" in line and "true" in line.lower():
                    errors.append(f"Zen prefs.js enabled userChrome stylesheets: {line.strip()}")
    return errors


def verify_reference_repo_integrity(repo_path: Path) -> list[str]:
    errors: list[str] = []
    if not repo_path.is_dir():
        return [f"Reference repo missing: {repo_path}"]

    status_proc = subprocess.run(
        ["git", "-C", str(repo_path), "status", "--porcelain"],
        capture_output=True,
        text=True,
        timeout=10,
    )
    if status_proc.returncode != 0:
        errors.append(f"git status failed in {repo_path}: {status_proc.stderr.strip()}")
    elif status_proc.stdout.strip() != "":
        errors.append(
            f"Reference repo working tree is dirty:\n{status_proc.stdout.strip()}"
        )

    head_proc = subprocess.run(
        ["git", "-C", str(repo_path), "rev-parse", "HEAD"],
        capture_output=True,
        text=True,
        timeout=10,
    )
    if head_proc.returncode != 0:
        errors.append(f"git rev-parse HEAD failed: {head_proc.stderr.strip()}")
    elif head_proc.stdout.strip() != REFERENCE_REPO_HEAD:
        errors.append(
            f"Reference repo HEAD mismatch: expected {REFERENCE_REPO_HEAD}, got {head_proc.stdout.strip()}"
        )

    lua_files = sorted(str(p) for p in repo_path.rglob("*.lua"))
    if lua_files:
        errors.append(f"Unsupported .lua files found in reference repo: {lua_files}")

    for rel, expected_hash in REFERENCE_FILE_SHA256.items():
        fp = repo_path / rel
        if not fp.is_file():
            errors.append(f"Reference file missing: {fp}")
            continue
        actual = sha256_file(fp)
        if actual != expected_hash:
            errors.append(
                f"Reference file {rel} SHA-256 mismatch: expected {expected_hash}, got {actual}"
            )
    return errors
