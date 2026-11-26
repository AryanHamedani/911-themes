# 911 (`992.2`) for Telegram Desktop

Porsche 911 (`992.2`) Precision Night Cockpit dark theme for Telegram Desktop, built directly from [`../colors.toml`](../colors.toml) and the derived 4-plane cockpit contract.

## Files

- `911.tdesktop-theme` — Root-level archive containing:
  - `colors.tdesktop-theme`: Complete **617-key** palette in topological dependency order (zero forward references, zero duplicate keys, full `lib_ui` + legacy cross-version coverage).
  - `background.jpg`: Custom Porsche 911 flyline dark cockpit wallpaper calibrated so Telegram's auto-palette adjuster preserves cockpit surface contrast.

## Palette & Contrast Notes

- **4-Plane Cockpit Depth**: Deep Carbon (`#0c0e11`), Race-Tex Chrome (`#131519`), Vanadium Elevated (`#1a1d23`), and Smoked Carmine tint (`#261b1f`, `11.90:1` with `#dadad6`), grounded in Race-Tex Charcoal (`#141619`) and `#0f1114` / `#0a0b0d`.
- **Guards Red Accessibility**: Filled accent buttons, unread badges, verified checks, and tray counters use `#bf3b3e` with `#f4f3ef` ink (`4.84:1` WCAG AA), muted badges use `#363b47` with `#f4f3ef` (`10.10:1`), and all **18 WCAG AA contrast checks pass**.

## Manual Installation (Non-Activating)

Applying the theme is completely manual and does not touch your running Telegram Desktop instance until you import it yourself:

1. Open **Telegram Desktop**.
2. Go to **Settings → Chat Settings → Theme** (click the `...` menu) → **Import existing theme** (or open `telegram/911.tdesktop-theme` directly with Telegram Desktop).
3. Select `911.tdesktop-theme` and click **Keep Changes**.

---

Not affiliated with or endorsed by Porsche AG. Porsche and 911 are trademarks of Porsche AG. Licensed under [MIT](../LICENSE).
