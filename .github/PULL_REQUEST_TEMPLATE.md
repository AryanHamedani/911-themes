## Summary

- App(s) touched:
- What changed and why:

## Design & Palette Checklist

- [ ] Uses **only** canonical tokens from `colors.toml` and Section 2 of `INVENTORY.md` (zero unapproved or legacy hexes)
- [ ] All readable foreground/background pairs clear **WCAG AA (`>= 4.5:1`)**
- [ ] Follows the 4-plane cockpit hierarchy and 90/9/1 Guards Red accent restraint
- [ ] Updated the app's `README.md` if keys/install steps changed
- [ ] Verified locally with `python3 tests/run_e2e.py --tier 1 --tier 2` (and `--tier 3` if the CLI is installed)
