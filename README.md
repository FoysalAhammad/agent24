<div align="center">

# 🤖 Agent 24

**An autonomous AI coding & technical assistant for Android.**

A full agentic workspace that runs entirely on your phone — chat with leading AI
models, let it plan and execute multi-step tasks, edit files, run shell commands,
browse the web, and manage projects with a permission-aware tool system.

[![Platform](https://img.shields.io/badge/platform-Android-3DDC84?logo=android&logoColor=white)]()
[![Language](https://img.shields.io/badge/language-Kotlin%20%7C%20Java-7F52FF?logo=kotlin&logoColor=white)]()
[![Built with](https://img.shields.io/badge/AI-agentic%20workflows-blue)]()
[![License](https://img.shields.io/badge/license-MIT-green)]()

[Features](#-features) · [Agents](#-agents) · [Tools](#-tools) · [Providers](#-providers) · [Getting Started](#-getting-started)

</div>

---

## ✨ Introduction

**Agent 24** brings the power of a modern agentic AI assistant to Android.
Instead of a simple chatbot, it operates like a real engineering companion:
it reads your request, forms a plan, calls the right tools, verifies the result,
and reports back — all while keeping you in control through an explicit
permission model.

Whether you are writing code, debugging a script, researching documentation,
automating repetitive shell work, or just exploring an idea, Agent 24 gives you
a complete, self-contained workspace that travels with you.

### Why Agent 24?

| | |
|---|---|
| 🧠 **Truly agentic** | Plans, executes, verifies and iterates — not just replies. |
| 🔧 **18 built-in tools** | Shell, files, search, patches, web, git, tasks, vision and more. |
| 🔐 **Permission-first** | Every sensitive action is `allow` / `ask` / `deny` — you decide. |
| 🌍 **Model-agnostic** | Works with 13+ pre-configured providers and dozens of models. |
| 📴 **Works on-device** | Sessions, history and databases live locally on your device. |
| 🌐 **Multilingual** | Understands and replies in your language, including Bangla and Hindi. |

---

## 🤖 Agents

Agent 24 ships with a layered agent system — pick the right brain for the job.

| Agent | Type | Purpose |
|---|---|---|
| **Build** | Primary | Default agent with full tool access for real work. |
| **Plan** | Primary | Read-only analysis; asks before any edit or command. |
| **General** | Subagent | Autonomous multi-step tasks delegated by the main agent. |
| **Explore** | Subagent | Fast, read-only codebase search and summarisation. |
| **Scout** | Subagent | External documentation and dependency research. |
| **Compaction** | System | Automatically summarises context when it grows too long. |
| **Title / Summary** | System | Auto-generates session titles and conversation summaries. |

---

## 🔧 Tools

A unified tool layer the model can call during any conversation:

`bash` · `shell` · `read` · `write` · `edit` · `grep` · `glob` · `list` ·
`diff` · `apply_patch` · `webfetch` · `websearch` · `task` · `skill` ·
`question` · `todowrite` · `todoread` · `git`

Plus extended capabilities: **interactive task delegation**, **structured todo
tracking**, **pixel-level image inspection**, **UI hierarchy dumps** and
**screen understanding**.

### Slash commands

`/new` `/clear` `/sessions` `/model` `/connect` `/build` `/plan` `/init`
`/diff` `/undo` `/redo` `/fork` `/review` `/component` `/compact` `/share`
`/skills` `/agents` `/theme` `/export` `/import` `/help`

---

## 🌍 Providers

Bring your own model — Agent 24 speaks the OpenAI-compatible protocol and ships
with pre-configured support for a wide ecosystem:

OpenAI · Anthropic · Google · Groq · DeepSeek · Mistral · xAI · Together ·
OpenRouter · HuggingFace · GitHub Models · Pollinations · and more.

Features per model: **tool calling**, **image input**, **reasoning display**,
**streaming**, and automatic **retry with exponential backoff** plus
**provider fallback** when an endpoint is unavailable.

---

## 🔐 Safety & Permissions

Every tool is gated by a fine-grained permission key (`read`, `edit`, `bash`,
`task`, `webfetch`, …) with three possible values:

- **allow** — execute immediately
- **ask** — show a confirmation dialog, wait for your decision
- **deny** — block entirely

Agents come with sensible defaults: the Build agent is unrestricted, the Plan
agent asks before touching anything, and research subagents are read-only.

> 🔑 **Privacy:** API credentials stay on your device, are never displayed in
> chat, and are never written into exported sessions or documentation.

---

## 📱 Requirements

- Android 8.0 (Oreo) or newer
- ~100 MB free storage
- Internet connection for AI providers
- An API key from any supported provider (free tiers available)

---

## 🚀 Getting Started

1. **Install** Agent 24 on your Android device.
2. **Connect** a provider with `/connect` — pick a provider, paste your API key.
3. **Choose a model** with `/model`.
4. **Start working** — describe what you want; Agent 24 plans, executes and verifies.

```text
you   > build a script that renames all images in a folder by date
agent > plan → create script → run it → verify output → report ✅
```

---

## 🗺️ Roadmap

- [ ] MCP (Model Context Protocol) server support
- [ ] Team sessions & shared workspaces
- [ ] Plugin / skill marketplace
- [ ] Local (on-device) model backend
- [ ] Desktop companion app

Contributions, issue reports and feature ideas are welcome.

---

## 👨‍💻 Developer

**Foysal Ahammad**

- GitHub: [github.com/FoysalAhammad](https://github.com/FoysalAhammad)

---

## 📄 License

Released under the MIT License. See [LICENSE](LICENSE) for details.

---

<div align="center">

**⭐ Star this repository if you find Agent 24 useful.**

Made with ❤️ for the Android community

</div>
