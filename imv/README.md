# 911 (`992.2`) for imv

Distraction-free Precision Night Cockpit lightbox theme for the `imv` image viewer, aligned with [`../colors.toml`](../colors.toml).

## Design & Palette Mapping

`imv` requires bare 6-digit hexadecimal values without a leading `#` and 2-digit hexadecimal alpha channels.

| Element | Option | Value | Role & Contrast |
|---|---|---|---|
| **Lightbox Canvas** | `background` | `141619` | Race-Tex Charcoal (`background`) — glare-free neutral dark plane that avoids pure-black halation around bright images |
| **Overlay Surface** | `overlay_background_color` / `overlay_background_alpha` | `0f1114` @ `e6` (90%) | Recessed Carbon (`dark_background`) float — grounded dark-glass telemetry bar |
| **Overlay Typography** | `overlay_text_color` / `overlay_text_alpha` | `dadad6` @ `ff` (100%) | Ice Grey / Crayon (`foreground`) — `13.55:1` on `0f1114` (`10.58:1` worst-case over pure white at 90% alpha) |

### Lightbox Ergonomics
- **Compact bottom telemetry**: Docked at the bottom edge (`overlay_position_bottom = true`) in `JetBrains Mono:12` with clean `·` and `×` typographic separators; press `d` in `imv` to toggle the overlay off for a 100% unobstructed canvas.
- **Window title parity**: `title_text` mirrors the filename, index, dimensions, and zoom percentage even when the overlay is hidden.
- **Faithful scaling**: `scaling_mode = shrink`, `upscaling_method = linear`, `initial_pan = 50 50`, and `loop_input = true` keep small UI captures crisp at 1:1 while fitting large photos cleanly in the viewport.

## Installation

Merge the `[options]` section from [`911.ini`](911.ini) into `~/.config/imv/config`, preserving your existing `[binds]` section intact.

---

Not affiliated with or endorsed by Porsche AG. Licensed under [MIT](../LICENSE).
