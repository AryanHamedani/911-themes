# Carrera for kubecolor

Porsche 911 Heritage Cockpit (`Carrera v2.0.0`) theme for [kubecolor](https://kubecolor.github.io/) — Basalt Alcantara (`#15171a`), Chalk (`#d6d2c7`), GT Silver (`#9599a2`), and Carmine Red (`#e1656c`).

## Files

- `color.yaml` — `kubecolor` theme (`preset: dark` plus `base`, `data`, `status`, `table`, `stderr`, `options`, `help`, `apply`, `delete`, `diff`, and `logs` overrides using exact `colors.toml` hex values).

## Installation

Back up any existing `~/.kube/color.yaml` first (or use `cp -i`), then copy `color.yaml` to `~/.kube/color.yaml` (or point `KUBECOLOR_CONFIG` at it manually without copying; this repository does not modify your active config):

```bash
mkdir -p ~/.kube
cp -i color.yaml ~/.kube/color.yaml
```

## Verification

```bash
python3 -c 'import yaml; yaml.safe_load(open("color.yaml"))'
KUBECOLOR_CONFIG="$PWD/color.yaml" KUBECOLOR_FORCE_COLORS=true kubecolor --help
```

## License

[MIT](../LICENSE) — Copyright (c) 2026 Aryan Hamedani.

Not affiliated with or endorsed by Porsche AG. Porsche, 911 and Carrera are trademarks of Porsche AG.
