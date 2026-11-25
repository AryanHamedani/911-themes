# Carrera for Zen Browser

A dark stylesheet pair (`userChrome.css` and `userContent.css`) inspired by the Porsche 911 Heritage Cockpit:
recessed `#101215` toolbars and sidebars, Basalt Alcantara `#15171a` browser canvas, elevated `#1e2025` URL bar and cards,
Chalk (`#d6d2c7`) text, and Carmine Red (`#e1656c`) focus accents.

## Install

1. Locate your Zen Browser profile directory (e.g. `~/.config/zen/<profile>/` or `~/.zen/<profile>/`, check `about:profiles`).
2. Copy `userChrome.css` and `userContent.css` into the profile's `chrome/` folder without overwriting `zen-themes.css` (which is managed by Zen Mods):

   ```bash
   mkdir -p ~/.config/zen/<your-profile>/chrome
   cp zen-browser/userChrome.css zen-browser/userContent.css ~/.config/zen/<your-profile>/chrome/
   ```

3. Open `about:config` in Zen Browser and set:

   ```text
   toolkit.legacyUserProfileCustomizations.stylesheets = true
   ```

4. Restart Zen Browser.

> Note: `userContent.css` is strictly scoped inside `@-moz-document url-prefix("about:")` so external websites are not styled.

---

Not affiliated with or endorsed by Porsche AG. Porsche, 911 and Carrera are trademarks of Porsche AG.

License: [MIT](../LICENSE)
