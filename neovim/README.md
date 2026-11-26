# 911 (`992.2`) for Neovim

Standalone, zero-dependency Lua colorscheme for Neovim aligned with the **911 (`992.2`) Precision Night Cockpit** palette (`../colors.toml`).

## Coverage

- **Core UI & Chrome**: 4-plane cockpit surfaces (`#0a0b0d` / `#0f1114` / `#141619` / `#1d2026`), Race-Tex chrome (`#131519`), Vanadium elevated (`#1a1d23`), Smoked Carmine (`#261b1f`), Guards Red badges (`#bf3b3e` / `#f4f3ef`, `4.84:1` AA), cursorline, floats, popups, folds, spellchecks.
- **Syntax, TreeSitter & LSP Semantic Tokens**: Full `@keyword`, `@function`, `@type`, `@string`, `@number`, `@variable`, `@property`, `@markup`, `@tag`, and `@lsp.type.*` / `@lsp.typemod.*` coverage.
- **Diagnostics & Diffs**: Canonical opaque `alpha-over-#141619` tints for `DiagnosticVirtualText*`, `DiffAdd`, `DiffDelete`, `DiffChange`, `DiffText`, `GitSigns*`, and `Diffview*`.
- **Plugins**: Telescope, Snacks, Neo-tree, Oil, Blink.cmp, nvim-cmp, Which-Key, Noice, nvim-notify, Trouble, Indent-blankline (`Ibl*` & legacy), Lualine (`package.preload["lualine.themes.911"]`), Flash, Lazy, Mason, RenderMarkdown, `obsidian.nvim`, GrugFar, Mini.
- **Terminal**: Complete ANSI 16 `vim.g.terminal_color_0..15`.

## Installation

```bash
mkdir -p ~/.config/nvim/colors
cp colors/911.lua ~/.config/nvim/colors/911.lua
```

Activate in Neovim:

```vim
:colorscheme 911
```

Or with Lualine:

```lua
require("lualine").setup({ options = { theme = "911" } })
```

> **Omarchy note**: Omarchy's active `911` theme manages `~/.config/nvim/lua/plugins/theme.lua` via `aether.nvim`. Installing `~/.config/nvim/colors/911.lua` makes `:colorscheme 911` available without breaking Omarchy theme hot-reload.

---

Not affiliated with or endorsed by Porsche AG. Licensed under [MIT](../LICENSE).
