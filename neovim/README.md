# 911 (`992.2`) for Neovim

Standalone, zero-dependency Lua colorscheme for Neovim crafted with **GitHub Primer clarity × Porsche 911 (`992.2`) Precision Night Cockpit** (`../colors.toml`).

## Design Architecture

- **4-Plane Surface Hierarchy**:
  - **Plane 0 (Recessed sidebars & panels)**: `#0a0b0d` / `#0c0e11` / `#0f1114` (`NormalSB`, `NeoTreeNormal`, `TroubleNormal`, `DiffviewNormal`, `DapUINormal`, `SnacksPickerList`)
  - **Plane 1 (Primary canvas)**: `#141619` Race-Tex Charcoal (`Normal`, `SignColumn`, `FoldColumn`, `WinBar`)
  - **Plane 2 (Chrome bars)**: `#131519` Race-Tex Chrome (`StatusLine`, `TabLine`, `BufferLineBackground`, `LspInlayHint`)
  - **Plane 3 (Vanadium elevated)**: `#1a1d23` / `#1d2026` (`NormalFloat`, `Pmenu`, `BlinkCmpMenu`, `WhichKeyFloat`, `NoiceCmdlinePopup`, `CursorLine`, `Folded`)
  - **Active selection & focus**: `#292d36` Slate Grey Neo (`Visual`, `PmenuSel`) and `#261b1f` Smoked Carmine (`LspReferenceWrite`, `MatchParen`, `QuickFixLine`, multi-selection)
- **90/9/1 Accent Discipline**: Guards Red (`#e55c5a` needle; `#bf3b3e` fill + `#f4f3ef` ink at `4.84:1` AA) reserved for `Cursor`, `CursorLineNr`, `CurSearch`, `BufferLineIndicatorSelected`, primary badges, and critical alerts.
- **5-Step Typographic Hierarchy**: `#edede9` (focal) → `#dadad6` (primary) → `#b4b7be` (parameters/secondary) → `#9297a2` (operators/docstrings/tertiary) → `#858a96` (comments/line numbers/inlay hints, `5.24:1` AA on `#141619`).

## Coverage

- **Core UI & Ergonomics**: Seamless gutter-to-canvas `CursorLine` (`CursorLineNr`/`CursorLineSign`/`CursorLineFold`), AA-legible `LineNr`, distinct `Visual` vs `Search` vs `IncSearch` vs `CurSearch` vs `MatchParen`, calm `LspInlayHint`, differentiated `LspReferenceText`/`Read`/`Write`, folds, spellchecks.
- **Syntax, TreeSitter & LSP Semantic Tokens**: Fine-grained highlighting tuned for Python (Django/DRF/FastAPI), Go, TypeScript/TSX, Rust, SQL, YAML, JSON, TOML, and Markdown. `@lsp.type.variable` is intentionally left unstyled so higher-priority LSP tokens never clobber TreeSitter captures (`@variable.builtin`, `@constant`), with dedicated `@lsp.typemod.*` support.
- **Diagnostics & Diffs**: Canonical opaque `alpha-over-#141619` tints for `DiagnosticVirtualText*`, `DiffAdd`/`Change`/`Delete`/`Text`, `GitSigns*` (including staged hunks & inline diffs), and `Diffview*`.
- **Plugins**: `snacks.nvim` (picker, explorer, dashboard, indent, notifier, input), `bufferline.nvim`, `lualine.nvim` (`package.preload["lualine.themes.911"]`), `blink.cmp`, `nvim-cmp`, `telescope.nvim`, `noice.nvim`, `nvim-notify`, `which-key.nvim`, `trouble.nvim`, `flash.nvim`, `aerial.nvim`, `nvim-navic`, `nvim-treesitter-context`, `neo-tree.nvim`, `oil.nvim`, `nvim-dap` / `nvim-dap-ui` / `nvim-dap-virtual-text`, `neotest`, `todo-comments.nvim`, `yanky.nvim`, `grug-far.nvim`, `lazy.nvim`, `mason.nvim`, `vim-dadbod-ui`, `crates.nvim`, `render-markdown.nvim`, `markview.nvim`, `obsidian.nvim`, `indent-blankline.nvim`, and `mini.*`.
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
