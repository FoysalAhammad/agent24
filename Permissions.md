# 🔐 Permissions

> Safety by design: nothing sensitive happens without your rules allowing it.

---

## 🎛️ The Three Values

| Value | Behaviour |
|---|---|
| ✅ **allow** | Execute immediately |
| ❓ **ask** | Show a confirmation dialog, wait for your decision |
| 🚫 **deny** | Block entirely |

---

## 🗝️ Permission Keys

| Key | Guards |
|---|---|
| `read` | File reading |
| `edit` | Write / edit / patch operations |
| `bash` | Shell & sessions |
| `task` | Subagent delegation |
| `webfetch` / `websearch` | Network access |
| `glob` / `grep` / `list` | Search operations |
| `todowrite` | Todo list access |
| `skill` / `question` | Skill loading / user prompts |
| `external_directory` | Anything outside the workspace |

---

## 🤖 Agent Defaults

<details>
<summary><b>Who gets what — click to expand</b></summary>

| Agent | Default posture |
|---|---|
| **Build** | Unrestricted — full speed ahead |
| **Plan** | Asks before every edit or command |
| **General** | Autonomous executor for delegated work |
| **Explore / Scout** | Read-only research, no modifications |

</details>

---

## 🔑 Credential Privacy

> API credentials stay on your device, are **never displayed in chat**, and are
> never written into exported sessions or documentation.

---

<div align="center">

**Next: [FAQ →](FAQ)**

</div>
