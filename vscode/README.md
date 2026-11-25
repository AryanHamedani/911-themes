# Carrera for VS Code & Antigravity IDE

A dark color theme inspired by the Porsche 911 Heritage Cockpit on a night drive:
Basalt Alcantara surfaces (`#15171a` editor / `#101215` recessed panels), warm Chalk (`Kreide`, `#d6d2c7`) text,
brushed GT Silver trim, and a single disciplined spark of Carmine Red (`#e1656c`) for active focus and selection accents.

## Install

Copy this `vscode/` directory into your editor's extensions folder without overwriting existing settings:

### VS Code / VSCodium

```bash
cp -r vscode ~/.vscode/extensions/carrera-theme
# or for VSCodium:
cp -r vscode ~/.vscode-oss/extensions/carrera-theme
```

### Antigravity IDE

```bash
cp -r vscode ~/.antigravity-ide/extensions/carrera-theme
```

Then restart the editor and select **Carrera** via **Preferences: Color Theme** (`Ctrl+K Ctrl+T`), or set `"workbench.colorTheme": "Carrera"` in your `settings.json`:

- VS Code: `~/.config/Code/User/settings.json`
- Antigravity IDE: `~/.config/Antigravity IDE/User/settings.json`

## Notes

- **Cursor color**: `editorCursor.foreground` and `terminalCursor.foreground` default to glare-free Chalk Highlight (`#eae6dc`). To use the Carmine Red needle (`#e1656c`) from `colors.toml`, override `"workbench.colorCustomizations"` or edit `themes/carrera-color-theme.json`.
- **Line highlight**: Uses `#1e2025` (`lighter_background`) and `#262930` border directly from the Carrera v2.0.0 palette.

---

Not affiliated with or endorsed by Porsche AG. Porsche, 911 and Carrera are trademarks of Porsche AG.

License: [MIT](../LICENSE)
