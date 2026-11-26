# 911 for kubecolor

Porsche 911 (`992.2`) Precision Night Cockpit theme for [kubecolor](https://kubecolor.github.io/) (`v0.9.0+`) — calibrated to match the K9s 911 triage ladder so switching between `k9s` and `kubectl` feels like one unified cockpit.

## Files

- `color.yaml` — Full kubecolor theme covering `default`, `base`, `shell`, `data` (incl. `ratio` and `durationfresh`), `status`, `table`, `describe`, `explain`, `version`, `stderr`, `options`, `help`, `apply`, `delete`, `diff`, `rollout`, and `logs` (incl. `severity`).

## Design Highlights

- **Calm Wide Tables**: `table.header` in Brushed Silver (`#b4b7be:bold`) with a 3-step `table.columns` cadence (`#dadad6 / #6fa2de / #b4b7be`) for horizontal row tracking across `kubectl get pods -A -o wide` without rainbow clutter.
- **Unified K9s Triage**: `status` (`#7fb887` success, `#e0be66` warning, `#e56c6a:bold` error) and `apply` (`#7fb887` created, `#6fa2de` configured, `#858a96` unchanged, `#6ac4cb` dryrun, `#dadad6` fallback) mirror K9s 911 semantic states.
- **Structured YAML/JSON Data**: 3-level key nesting (`#6fa2de / #6ac4cb / #b488cc`), Oak Green strings (`#7fb887`), Lava Orange numbers/quantities (`#e89158`), Racing Gold booleans (`#e0be66`), and muted italic nulls (`#858a96:italic`).
- **90/9/1 Accent Discipline**: Guards Red (`#e55c5a:bold`) is reserved exclusively for `help.header` and `explain.required`.

## Install

```bash
mkdir -p ~/.kube
cp color.yaml ~/.kube/color.yaml
```

## Validate

```bash
python3 -c 'import yaml; d=yaml.safe_load(open("color.yaml")); assert d["preset"]=="dark"'
KUBECOLOR_CONFIG="$PWD/color.yaml" kubecolor version --client --output=yaml
KUBECOLOR_CONFIG="$PWD/color.yaml" kubecolor --help >/dev/null
```

## Disclaimer

Not affiliated with or endorsed by Porsche AG. Porsche and 911 are trademarks of Porsche AG.
