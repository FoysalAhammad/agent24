# Agent24 Settings Customization Skill

You are an AI agent that can customize itself based on user settings from `tui.json`.

## How to Read Settings

When you start a session, read the settings file:
```
~/.config/agent24/tui.json
```

## Settings Structure

The settings are organized in sections:

### 1. General Settings
- `language` - Display language (English, Bangla, Hindi)
- `auto_accept_permissions` - Auto-approve tool permissions (true/false)
- `terminal_shell` - Shell type (Auto, Bash, Zsh, Fish)
- `show_reasoning` - Show reasoning summaries (true/false)
- `expand_shell_tools` - Expand shell tool parts (true/false)
- `expand_edit_tools` - Expand edit tool parts (true/false)

### 2. Appearance Settings
- `color_scheme` - Color scheme (Dark, Light, System)
- `theme` - UI theme (Nord, Default, Monokai)
- `ui_font` - UI font (System Sans, Roboto, Inter)
- `code_font` - Code font (System Mono, Fira Code, JetBrains Mono)
- `terminal_font` - Terminal font (JetBrainsMono, Fira Code, Hack)

### 3. Notification Settings
- `notif_agent` - Agent completion notifications (true/false)
- `notif_permissions` - Permission request notifications (true/false)
- `notif_errors` - Error notifications (true/false)

### 4. Sound Settings
- `sound_agent` - Agent completion sound (Bip-bop 07, None, Chime)
- `sound_permissions` - Permission request sound (Bip-bop 07, None, Chime)
- `sound_errors` - Error sound (Nope 02, None, Bip-bop 07)

### 5. Display Settings
- `pinch_zoom` - Pinch to zoom (true/false)

### 6. Advanced Settings
- `file_tree` - Show file tree panel (true/false)
- `command_palette` - Show command palette (true/false)
- `server_status` - Show server status (true/false)
- `show_agent` - Show agent selector (true/false)

## How to Customize Behavior

### Based on Language
- If `language` is "English" - Use English responses
- If `language` is "Bangla" - Use Bangla responses
- If `language` is "Hindi" - Use Hindi responses

### Based on Auto-Accept
- If `auto_accept_permissions` is true - Skip permission prompts
- If `auto_accept_permissions` is false - Ask for permission before actions

### Based on Shell
- If `terminal_shell` is "Bash" - Use bash commands
- If `terminal_shell` is "Zsh" - Use zsh commands
- If `terminal_shell` is "Fish" - Use fish commands
- If `terminal_shell` is "Auto (Default)" - Detect from environment

### Based on Show Reasoning
- If `show_reasoning` is true - Include reasoning summaries
- If `show_reasoning` is false - Keep responses concise

### Based on Expand Tools
- If `expand_shell_tools` is true - Show full shell output
- If `expand_shell_tools` is false - Show condensed output
- If `expand_edit_tools` is true - Show full edit details
- If `expand_edit_tools` is false - Show condensed details

### Based on Color Scheme
- If `color_scheme` is "Dark" - Use dark theme colors
- If `color_scheme` is "Light" - Use light theme colors
- If `color_scheme` is "System" - Match system theme

### Based on Notifications
- If `notif_agent` is true - Notify when task complete
- If `notif_permissions` is true - Notify when permission needed
- If `notif_errors` is true - Notify on errors

### Based on Sounds
- If `sound_agent` is not "None" - Play sound on completion
- If `sound_permissions` is not "None" - Play sound for permission
- If `sound_errors` is not "None" - Play sound on error

### Based on Display
- If `pinch_zoom` is true - Enable zoom gestures
- If `pinch_zoom` is false - Disable zoom gestures

### Based on Advanced
- If `file_tree` is true - Show file tree in responses
- If `file_tree` is false - Hide file tree
- If `command_palette` is true - Show command palette
- If `command_palette` is false - Hide command palette
- If `server_status` is true - Show server status
- If `server_status` is false - Hide server status
- If `show_agent` is true - Show agent selector
- If `show_agent` is false - Hide agent selector

## Important Notes

1. Always read `tui.json` at session start
2. Apply settings immediately
3. If setting not found, use default value
4. Log setting changes for debugging
5. Respect user preferences
