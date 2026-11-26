# 911 for Herdr

A dark, glare-free [Herdr](https://herdr.dev) terminal multiplexer theme inspired by the **Porsche 911 (`992.2`) Precision Night Cockpit**, engineered for 8-hour daily multi-agent sessions with a seamless **Race-Tex Charcoal** (`#141619`) surface progression (eliminating harsh sidebar cutouts against translucent terminals like Foot), calm **Filled Guards Red** (`#bf3b3e`) focus discipline, and OKLCH-calibrated agent lifecycle telemetry.

## Cockpit Architecture

| Plane / Role | Herdr Token | Hex | Contrast / Notes |
|---|---|---|---|
| **Sidebar** — Seamless Race-Tex workspaces & agents | `sidebar_bg` | `#141619` | `12.93:1` w/ `#dadad6`; matches Foot `#141619` padding with zero slab seam |
| **Chrome Bar** — Top/bottom bar chrome | `surface_dim` | `#131519` | `13.04:1` w/ `#dadad6`; blends cleanly into Race-Tex edges |
| **Canvas** — Active terminal canvas & active-tab ink | `panel_bg` | `#141619` | `12.93:1` w/ `#dadad6` |
| **Elevated** — Vanadium popups, modals & menus | `surface0` | `#1a1d23` | `12.04:1` w/ `#dadad6` |
| **Active Row** — Smoked Carmine active workspace/agent row | `active_row_bg` | `#261b1f` | `11.90:1` w/ `#dadad6` |
| **Selection** — Copy-mode & text highlight | `selection_bg` | `#292d36` | `9.84:1` w/ `#dadad6` |
| **Inactive Border** — Pane divider & modal hairline | `surface1` | `#2f3440` | Crisp subtle rule vs `#bf3b3e` focus |
| **Active Focus** — Active tab fill, pane border & modal focus | `accent` / `[ui].accent` | `#bf3b3e` | Calm Filled Guards Red (`4.84:1` AA badge fill) without coral glare |

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
