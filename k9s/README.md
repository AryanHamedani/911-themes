# 911 for K9s

Porsche 911 (`992.2`) Precision Night Cockpit skin for [K9s](https://k9scli.io/) (`v0.51+`) — Race-Tex Charcoal (`#141619`), Ice Grey (`#dadad6`), GT Silver (`#9297a2`), Smoked Carmine selection (`#261b1f`), and disciplined 911 Guards/Carmine Red (`#e55c5a` / `#bf3b3e`).

## Files

- `911.yaml` — Complete K9s `v0.51` skin covering every `Styles` schema key (`body`, `prompt`, `help`, `info`, `dialog`, `frame`: `border`/`menu`/`crumbs`/`status`/`title`, `views`: `charts`/`table`/`xray`/`yaml`/`picker`/`logs`) using quoted `#rrggbb` truecolor hex values.

## Design System & Cockpit Hierarchy

- **4-Plane Surfaces**:
  - Recessed carbon (`#0f1114`): `:` / `/` prompt input and Pulse/Charts graph wells.
  - Primary canvas (`#141619`): tables, logs, xray tree, YAML/describe views.
  - Race-Tex chrome (`#131519`) & Vanadium elevated (`#1a1d23` / `#1d2026`): table column headers, frame titles, `?` help overlay, log toggle bar, chart dials, and modal dialogs.
  - Smoked Carmine selection (`#261b1f` + `#edede9` ink): active table and xray cursor row without blinding highlight bars.
- **90/9/1 Accent Discipline**:
  - Guards Red (`#e55c5a`) acts as an instrument needle for focused frame borders, `:command` prompt border, sort indicator, active namespace highlight, and help section headers.
  - `/filter` prompt border uses Ice Glacier Cyan (`#6ac4cb`) to distinguish filtering from `:command` mode at a glance.
  - Header metadata labels (`info.sectionColor`) and menu descriptions (`frame.menu.fgColor` with `fgStyle: "normal"`) stay quiet in GT Silver (`#9297a2`), while shortcut keycaps use Lugano Blue (`#6fa2de`) and namespace numbers use PCCB Racing Gold (`#e0be66`).
- **AA Badges & Triage Ladder**:
  - Active breadcrumb, focused dialog button, and focused chart badge use `#bf3b3e` with `#f4f3ef` ink (`4.84:1` AA); inactive breadcrumbs use `#363b47` with `#f4f3ef` ink (`10.10:1` AAA).
  - Resource status triage separates Running/Ready (`#7fb887`), Pending/Warning (`#e0be66`), Terminating (`#f48583`), Error/CrashLoopBackOff (`#e56c6a`), and Completed (`#858a96`).

## Install

1. Copy `911.yaml` to `~/.config/k9s/skins/911.yaml`:

   ```bash
   mkdir -p ~/.config/k9s/skins
   cp 911.yaml ~/.config/k9s/skins/911.yaml
   ```

2. Set `k9s.ui.skin: 911` in `~/.config/k9s/config.yaml`.

### Recommended Ergonomic Settings (`~/.config/k9s/config.yaml`)

For long debugging sessions, these non-destructive UI defaults reclaim vertical table rows and remove startup friction without affecting cluster/context settings:

```yaml
k9s:
  ui:
    logoless: true    # Reclaims 6 vertical rows for pods/deployments/logs
    splashless: true  # Instant startup without splash delay
    skin: 911
  logger:
    tail: 200         # Deeper initial log context
    buffer: 5000
```

## Validate

```bash
python3 -c 'import yaml; d=yaml.safe_load(open("911.yaml")); assert set(d["k9s"]["views"])=={"charts","table","xray","yaml","picker","logs"}'
```

## Disclaimer

Not affiliated with or endorsed by Porsche AG. Porsche and 911 are trademarks of Porsche AG.
