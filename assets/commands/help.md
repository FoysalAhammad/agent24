---
description: Show help dialog
agent: build
---

# /help Command

Show help dialog with all available commands and shortcuts.

## Kaj (Bangla)

Shob available commands ar shortcuts show kore help dialog e.

## Flow

1. Help dialog open koro
2. Commands list show koro
3. Shortcuts show koro
4. Usage examples show koro
5. Close button dekhao

## Available Commands

### Session Commands
- `/new` - Notun session start koro
- `/sessions` - Sessions list/switch koro
- `/compact` - Session compact koro

### Edit Commands
- `/undo` - Last message undo koro
- `/redo` - Undo kora message abar koro

### Share Commands
- `/share` - Session share koro
- `/unshare` - Session unshare koro

### Settings Commands
- `/connect` - Provider add koro
- `/models` - Available models list
- `/themes` - Available themes list
- `/thinking` - Thinking blocks toggle

### Info Commands
- `/help` - Ei help dialog
- `/details` - Tool execution details

## Android Implementation

1. Help dialog/activity open koro
2. RecyclerView/list e commands show koro
3. Each command er description dekhao
4. Tap hole command execute koro
5. Close button diye bondho koro

## Desktop Reference

Real OpenCode te `/help` command:
- TUI help modal show kore
- Keyboard shortcuts show kore
- Command list show kore

## Permissions

- UI permission (dialog show)

## Example

```
/help
```

## Help Dialog Layout

```
┌─────────────────────────────────────┐
│           HELP                      │
├─────────────────────────────────────┤
│ SESSION                             │
│   /new        New session           │
│   /sessions   List sessions         │
│   /compact    Compact session       │
│                                     │
│ EDIT                                │
│   /undo       Undo last message     │
│   /redo       Redo message          │
│                                     │
│ SHARE                               │
│   /share      Share session         │
│   /unshare    Unshare session       │
│                                     │
│ SETTINGS                            │
│   /connect    Add provider          │
│   /models     List models           │
│   /themes     List themes           │
│   /thinking   Toggle thinking       │
│                                     │
│ INFO                                │
│   /help       Show this help        │
│   /details    Toggle details        │
└─────────────────────────────────────┘
```

## Keyboard Shortcuts (Desktop Reference)

- `ctrl+p` - Command palette
- `ctrl+n` - New session
- `ctrl+x c` - Compact
- `ctrl+x u` - Undo
- `ctrl+x r` - Redo
- `ctrl+x l` - Sessions
- `ctrl+x m` - Models
- `ctrl+x t` - Themes

## Android Touch Gestures

- Swipe right - Undo
- Swipe left - Redo
- Long press - Context menu
- Double tap - Quick action
