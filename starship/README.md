# 911 for Starship

A dark, glare-free [Starship](https://starship.rs) prompt theme inspired by the **Porsche 911 (`992.2`) Precision Night Cockpit**: **Race-Tex Charcoal** (`#141619`), **Ice Grey (Crayon)** (`#dadad6`), and **Guards/Carmine Red** (`#e55c5a`).

Calibrated in OKLCH for 8-hour daily engineering sessions and verified to WCAG AA contrast targets.

## Design Highlights

- **2-Line Cockpit Layout**: Context lives on Line 1 (`directory`, `git`, active runtimes, and `kubernetes`), while Line 2 stays clean for command entry with right-aligned telemetry (`right_format`: exit `status`, `cmd_duration`, `jobs`, `time`).
- **90/9/1 Accent Discipline**: Guards Red (`#e55c5a`) is reserved strictly for instrument-needle alerts — failed prompt character (`✗`), non-zero exit codes, Git merge conflicts, and production Kubernetes clusters (`idk-c8`, `*prod*`, `*darkube*`).
- **5-Step Typographic Hierarchy**: Crisp focal `repo_root` (`#edede9`), stepped-down subpaths and runtime versions (`#b4b7be`), muted glyphs/virtualenvs (`#9297a2`), and quiet clock/delimiters (`#858a96`).
- **100ms Git Scannability**: Per-state semantic colors in `git_status` (staged `green`, modified `yellow`, deleted `red`, renamed `cyan`, stashed `magenta`, untracked `dark_foreground`, ahead/behind `blue`, conflicted `bold accent`), plus `git_state` (rebase/merge/cherry-pick) and `git_metrics`.
- **Context-Aware Infra**: `kubernetes` illuminates automatically in k8s/Helm/GitOps directories or when `KUBECONFIG` is set, color-coded by environment; `docker_context` appears only with Docker files; `username`/`hostname` appear only over SSH.

## Files Included

- `911.toml` — Complete Starship configuration with `[palettes.911]` (all canonical base and derived cockpit tokens) and module styling for `character` (with vi-mode), `username`, `hostname`, `directory`, `git_branch`, `git_state`, `git_status`, `git_metrics`, `python`, `golang`, `rust`, `nodejs`, `docker_context`, `kubernetes`, `status`, `cmd_duration`, `jobs`, and `time`.

## Manual Install

```sh
cp ~/.config/starship.toml ~/.config/starship.toml.bak-911
cp 911.toml ~/.config/starship.toml
starship print-config > /dev/null
```

Palette reference: [`../colors.toml`](../colors.toml).

---

Not affiliated with or endorsed by Porsche AG. Porsche and 911 are trademarks of Porsche AG.

License: [MIT](../LICENSE)
