# 911 for Herdr

A dark, glare-free [Herdr](https://herdr.dev) terminal multiplexer theme inspired by the **Porsche 911 (`992.2`) Precision Night Cockpit**, engineered for 8-hour daily multi-agent sessions with a strict 4-plane surface hierarchy, restrained **Guards/Carmine Red** (`#e55c5a`) focus discipline, and OKLCH-calibrated agent lifecycle telemetry.

## Cockpit Architecture

| Plane / Role | Herdr Token | Hex | Contrast (`#dadad6` / `#141619`) |
|---|---|---|---|
| **Plane 0** — Recessed sidebar & workspaces | `sidebar_bg` | `#0c0e11` | `13.79:1` |
| **Plane 1** — Top/bottom bar chrome | `surface_dim` | `#131519` | `13.04:1` |
| **Plane 2** — Active terminal canvas & active-tab ink | `panel_bg` | `#141619` | `12.93:1` (`5.19:1` on `#e55c5a`) |
| **Plane 3** — Vanadium elevated popups, modals & menus | `surface0` | `#1a1d23` | `12.04:1` |
| **Plane 4** — Smoked Carmine active workspace/agent row | `active_row_bg` | `#261b1f` | `11.90:1` |
| **Selection** — Copy-mode & text highlight | `selection_bg` | `#292d36` | `9.84:1` |
| **Inactive Border** — Pane divider & modal hairline | `surface1` | `#2f3440` | Crisp subtle rule vs `#e55c5a` focus |
| **Active Focus** — Active pane border & active tab | `accent` / `[ui].accent` | `#e55c5a` | `5.19:1` on canvas |

### Typography & Agent Lifecycle Telemetry

- **Typography**: `text = "#dadad6"` (`12.93:1`), `subtext0 = "#b4b7be"` (`9.03:1`), `overlay1 = "#9297a2"` (`6.19:1`), `overlay0 = "#858a96"` (`5.24:1`) — every tier passes WCAG AA (`>= 4.5:1`) across all cockpit planes.
- **Agent States**: `red = "#e56c6a"` (blocked/error), `yellow = "#e0be66"` (working/warning), `green = "#7fb887"` (done/ready), `overlay0 = "#858a96"` (idle), `blue = "#6fa2de"` (info), `teal = "#6ac4cb"` (remote/telemetry), `peach = "#e89158"` (warm attention), `mauve = "#b488cc"` (agent/prefix mode).

## Files Included

- `911.toml` — Complete `[theme]`, `[theme.custom]` (all 19 Herdr `0.9.5` color tokens), and `[ui]` accent configuration.

## Manual Install

Merge `[theme]`, `[theme.custom]`, and `[ui].accent` from `911.toml` into `~/.config/herdr/config.toml` (keeping your personal `[keys]`, `[terminal]`, and `[ui]` layout settings), then validate and live-reload without restarting Herdr:

```sh
herdr config check
herdr server reload-config
```

Palette reference: [`../colors.toml`](../colors.toml).

---

Not affiliated with or endorsed by Porsche AG. Porsche and 911 are trademarks of Porsche AG.

License: [MIT](../LICENSE)
