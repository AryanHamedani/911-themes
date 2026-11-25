# Carrera for Neovim

Standalone Porsche 911 Heritage Cockpit (`v2.0.0`) Neovim colorscheme (`colors/carrera.lua`) built directly from [`../colors.toml`](../colors.toml).

> **Note**: This colorscheme is intentionally standalone and does **not** activate itself on startup. Your existing LazyVim / Neovim configuration remains untouched until you explicitly invoke `:colorscheme carrera` or configure it yourself.

## Design Philosophy

- **Colour carries meaning, weight stays regular**: Only `CursorLineNr` (`#e1656c`) and `MatchParen` (`#f28a8b`) use bold in normal editing chrome; red is reserved for keywords (`#e07476`) and errors (`#f28a8b`).
- **OKLCH Ergonomic Contrast**: Basalt Alcantara (`#15171a`), recessed instrument wells (`#101215`), Chalk foregrounds (`#d6d2c7` at `11.89:1`), Carmine Red (`#e1656c`) rev-needle accents, and derived `alpha-over-#15171a` diff and diagnostic backgrounds.
- **Broad Ecosystem Support**: Core UI, standard Vim syntax, Treesitter (`@...`), LSP semantic tokens (`@lsp.*`), Diagnostics (`undercurl` + tinted virtual text), Diff/GitSigns/Diffview, Telescope, Snacks, Neo-tree, Oil, Blink.cmp, nvim-cmp, WhichKey, Noice, Trouble, Flash, Lazy, Mason, RenderMarkdown, GrugFar, Mini, Lualine `"auto"` compatibility, and `terminal_color_0..15`.

## Manual Installation (Non-Activating)

1. Copy `neovim/colors/carrera.lua` to your Neovim runtime directory:

   ```bash
   mkdir -p ~/.config/nvim/colors
   cp neovim/colors/carrera.lua ~/.config/nvim/colors/carrera.lua
   ```

2. Try it temporarily inside Neovim without changing your default configuration:

   ```vim
   :colorscheme carrera
   ```

3. Optional — make it your default in LazyVim (`~/.config/nvim/lua/plugins/colorscheme.lua`):

   ```lua
   return {
     {
       "LazyVim/LazyVim",
       opts = {
         colorscheme = "carrera",
       },
     },
   }
   ```

## Verification

Test loading in headless Neovim without touching your startup config:

```bash
nvim --headless -c 'colorscheme carrera' -c 'lua print(vim.g.colors_name)' -c 'qa!'
```

---

Not affiliated with or endorsed by Porsche AG. Porsche, 911 and Carrera are trademarks of Porsche AG. Licensed under [MIT](../LICENSE).
