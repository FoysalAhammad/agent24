# 🤖 Agents

> Agent 24 ships with a layered agent system — pick the right brain for the job.

---

## 🎯 Primary Agents

| Agent | Mode | Best for |
|---|---|---|
| **Build** | Full access | Real work: editing, running, shipping. |
| **Plan** | Read-only + ask | Analysis and review before touching anything. |

---

## 🛠️ Subagents

| Agent | Role |
|---|---|
| **General** | Autonomous multi-step tasks delegated by the main agent. |
| **Explore** | Fast, read-only codebase search and summarisation. |
| **Scout** | External documentation and dependency research. |

---

## ⚙️ System Agents (automatic)

| Agent | Trigger | What it does |
|---|---|---|
| **Compaction** | Context grows long | Summarises history to keep the session healthy. |
| **Title** | First message | Generates a short session title. |
| **Summary** | Session switch | Writes a conversation summary. |

---

## 🔁 How they work together

<details>
<summary><b>Typical flow — click to expand</b></summary>

1. You send a request in **Build** or **Plan** mode.
2. The main agent plans and, if needed, delegates research to **Explore** / **Scout**.
3. **General** handles heavy multi-step subtasks.
4. **Compaction** keeps context clean automatically.
5. **Title** / **Summary** organise your sessions in the background.

</details>

---

<div align="center">

**Next: [Tools →](Tools)**

</div>
