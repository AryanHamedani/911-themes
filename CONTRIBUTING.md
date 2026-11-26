# Contributing to 911 Themes

Thank you for helping elevate the **911 (`992.2`) Precision Night Cockpit** theme suite!

## Palette & Craftsmanship Rules

1. **Single Source of Truth:** Every color must come from [`colors.toml`](colors.toml) (synced byte-for-byte from [`omarchy-911-theme`](https://github.com/AryanHamedani/omarchy-911-theme)) or the approved derived cockpit surfaces, borders, AA badges, and canonical opaque tints documented in Section 2 of [`INVENTORY.md`](INVENTORY.md).
2. **4-Plane Surface Hierarchy:**
   - Recessed chrome / sidebars: `#0c0e11` / `#0f1114`
   - Primary canvas: `#141619`
   - Race-Tex chrome (bars, headers, toolbars): `#131519`
   - Vanadium elevated (cards, floats, popovers): `#1a1d23` / `#1d2026`
   - Smoked Carmine active selection: `#261b1f` / `#292d36`
3. **90/9/1 Accent Restraint:** Guards/Carmine Red (`#e55c5a`, filled AA badge `#bf3b3e` + `#f4f3ef` ink) is reserved for focus, active indicators, primary CTAs, and critical alerts — never noisy wallpaper.
4. **WCAG AA Contrast:** Every readable foreground/background pair must clear `>= 4.5:1` on both `#141619` and elevated `#1d2026` surfaces.

## Running Validation Locally

```bash
# Palette contract, file structure, and syntax/parser checks (no external CLIs required)
python3 tests/run_e2e.py --tier 1 --tier 2

# Full suite including live CLI validators (nvim, starship, foot, ghostty, mpv, bat, delta, tmux, etc.)
python3 tests/run_e2e.py --tier 1 --tier 2 --tier 3
```

Every pull request must pass CI cleanly before merge.
