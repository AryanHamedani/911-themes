# 911 (`992.2`) for VS Code / Antigravity IDE

Precision Night Cockpit dark theme for Visual Studio Code and Antigravity IDE, built from [`../colors.toml`](../colors.toml) and the derived 911 cockpit surface contract.

## Coverage

- **681 Workbench UI tokens**: Strict 4-plane depth (`#0c0e11` activity bar, `#0f1114` sidebar/panel/terminal, `#141619` editor canvas, `#131519` title/tab/status chrome, `#1a1d23`/`#1d2026` elevated quickInput/menus/hover/suggest/chat), Smoked Carmine (`#261b1f`) active list focus, WCAG AA (`#bf3b3e` / `#f4f3ef`) badges & primary buttons, sticky scroll, command center, inline chat / chat, diff & merge editors, minimap, bracket pair colorization, and all 16 ANSI terminal colors.
- **66 Semantic Token Colors**: Full Python, Go, TypeScript, and Rust LSP coverage — italic `#b4b7be` parameters, italic `#b488cc` `self`/`cls`, distinct doc-comments (`#9297a2`) vs inline comments (`#858a96`), italic `#6ac4cb` decorators/lifetimes/attributes, readonly constants, structs, traits, and macros.
- **94 TextMate Scopes**: Full syntax coverage across code, docstrings vs comments, decorators, SQL, YAML, TOML, JSON, CSS, HTML/JSX, Markdown, and diffs.

## Installation

```bash
mkdir -p ~/.vscode/extensions/911-theme
cp -r package.json themes ~/.vscode/extensions/911-theme/
```

Reload VS Code or Antigravity IDE and select **911** from **Preferences: Color Theme** (`Ctrl+K Ctrl+T`).

---

Not affiliated with or endorsed by Porsche AG. Licensed under [MIT](../LICENSE).
