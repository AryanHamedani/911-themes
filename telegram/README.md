# Carrera for Telegram Desktop

Porsche 911 Heritage Cockpit (`v2.0.0`) dark theme for Telegram Desktop, built directly from [`../colors.toml`](../colors.toml).

## Files

- `carrera.tdesktop-theme` — Root-level archive containing:
  - `colors.tdesktop-theme`: Full 606-key palette (`586/586` `lib_ui` `colors.palette` keys in topological dependency order + `20` legacy `night.tdesktop-theme` keys for cross-version compatibility, zero forward references, zero duplicate keys).
  - `background.png`: Solid Basalt Alcantara (`#15171a`) non-interlaced PNG wallpaper so Telegram's auto-palette adjuster does not shift service/scrollbar hues.

## Palette & Contrast Notes

- **Surfaces**: Basalt Alcantara (`#15171a`) primary canvas, `#101215` recessed chat list/sidebar/compose well, `#0b0c0e` deep shadows/media backdrop, `#1e2025` elevated hover rows & outgoing bubbles, `#2b2e35` active selection, and `#3a2429` smoked Carmine tint for selected outgoing bubbles.
- **Carmine Red Accessibility**: Filled accent buttons, unread badges, verified checks, and tray counters (`#e1656c`) use `#101215` (`dark_background`) foregrounds (`5.61:1` WCAG AA contrast, vs `2.68:1` if `#eae6dc` were placed on `#e1656c`). `windowFgActive` stays `#eae6dc` for dark selection and overlay surfaces (`#2b2e35`, `#101215e5`).

## Manual Installation (Non-Activating)

Applying the theme is completely manual and does not touch your running Telegram Desktop instance until you import it yourself:

1. Open **Telegram Desktop**.
2. Go to **Settings → Chat Settings → Theme** (click the `...` menu) → **Create new theme** / **Import existing theme** (or open `telegram/carrera.tdesktop-theme` directly with Telegram Desktop).
3. Select `carrera.tdesktop-theme` and click **Keep Changes** when ready.

## Verification

Archive integrity, root-only layout, `#15171a` PNG decoding, 606-key coverage, identifier grammar (`[A-Za-z0-9_]+`), topological ordering, and Carrera v2.0.0 hex provenance are verified against `telegramdesktop/tdesktop` (`window_theme.cpp`) and `desktop-app/lib_ui` (`style_core_palette.cpp`, `colors.palette`) rules.

---

Not affiliated with or endorsed by Porsche AG. Porsche, 911 and Carrera are trademarks of Porsche AG. Licensed under [MIT](../LICENSE).
