---
description: Undo the last file change using git or backup
agent: build
---

Undo the last file change made by the agent.

1. Check if git is available in the current directory
2. If git is available, run `git diff` to see what changed
3. Run `git checkout -- <file>` to undo the last change
4. If git is not available, check for backup files
5. Report what was undone
