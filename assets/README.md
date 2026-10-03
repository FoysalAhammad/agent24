# Assets

Everything in this folder is meant to be dropped straight into the app — ask
the agent ("install the settings skill from the repo") or copy the files
yourself.

| Folder | What it is | Install into |
|--------|-----------|--------------|
| `skills/` | Agent skills (markdown) | `~/.config/agent24/skills/` |
| `commands/` | Slash commands (markdown) | `~/.config/agent24/commands/` |
| `config/` | Default `tui.json` settings | `~/.config/agent24/tui.json` (back yours up first) |
| `fonts/` | TTF fonts used by the PDF tools | `/data/data/com.agnt24/cache/fonts/` |
| `termux/` | Terminal welcome banner | ships inside the APK — kept here as the source copy |

## Download a single file

```
https://raw.githubusercontent.com/FoysalAhammad/agent24/main/assets/<folder>/<file>
```

Example — pull a skill into the app:

```bash
curl -L -o ~/.config/agent24/skills/settings-customization.md \
  https://raw.githubusercontent.com/FoysalAhammad/agent24/main/assets/skills/settings-customization.md
```

Skills and commands are live on the next turn (`/skills` lists them). Fonts
placed in `cache/fonts/` are picked up by the PDF tools right away — UI and
terminal fonts are baked into the APK.

Looking for the agent's own instruction files? Those ship with the app and are
not part of this folder.
