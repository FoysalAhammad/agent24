---
description: Compact the current session
agent: build
---

# /compact Command

Compact the current session to save context and improve performance.

## Kaj (Bangla)

Current session ke compact kore context save kore ar performance improve kore.

## Flow

1. Current session er messages read koro
2. Important information extract koro
3. Summary create koro
4. Old messages remove koro
5. Summary store koro

## Why Compact?

- Context window full hole performance komay
- Long conversation manage kore
- Memory save kore
- Better responses dite help kore

## Android Implementation

1. SQLite database theke messages read koro
2. Messages analyze koro
3. Summary generate koro (AI diye)
4. Database update koro
5. UI refresh koro

## Desktop Reference

Real OpenCode te `/compact` command:
- Git history use kore
- File changes track kore
- Context summarize kore

## Permissions

- Database read/write permission
- AI model access (summary generate)

## Example

```
/compact
```

## Compact Result

```
Session compacted!

Before: 50 messages (15,000 tokens)
After: 5 messages (2,000 tokens)
Saved: 13,000 tokens (87%)

Summary:
- User asked to create login page
- Created Login.tsx with form
- Added API integration
- Tested with 3 test cases
```

## Auto-Compact

Agent24 automatically compacts when:
- Context window > 80% full
- Session > 100 messages
- User requests compact

## Config Location

Android:
```
/data/data/com.agnt24/files/home/.local/share/agent24/sessions/<session-id>/
├── messages.json
├── compacted.json  ← Compact summary stored here
└── metadata.json
```
