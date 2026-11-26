# 911 for kubecolor

Porsche 911 (`992.2`) Precision Night Cockpit theme for [kubecolor](https://kubecolor.github.io/) — Race-Tex Charcoal (`#141619`), Ice Grey (`#dadad6`), GT Silver (`#9297a2`), and 911 Guards/Carmine Red (`#e55c5a`).

## Files

- `color.yaml` — Full kubecolor configuration covering `base`, `data`, `status`, `table`, `describe`, `explain`, `version`, `stderr`, `options`, `help`, `apply`, `delete`, `diff`, and `logs`.

## Install

```bash
mkdir -p ~/.kube
cp color.yaml ~/.kube/color.yaml
```

## Validate

```bash
python3 -c 'import yaml; d=yaml.safe_load(open("color.yaml")); assert d["preset"]=="dark"'
KUBECOLOR_CONFIG="$PWD/color.yaml" kubecolor --help >/dev/null
```

## Disclaimer

Not affiliated with or endorsed by Porsche AG. Porsche and 911 are trademarks of Porsche AG.
