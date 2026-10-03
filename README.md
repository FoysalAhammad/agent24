<div align="center">

# Agent 24

**An autonomous AI coding & technical assistant for Android.**

Chat with leading AI models, let it plan and execute multi-step work, edit files,
run shell commands, browse the web, drive the terminal, and control parts of the
device itself — all from one app that keeps you in charge through an explicit
permission system.

[![Platform](https://img.shields.io/badge/platform-Android-3DDC84?logo=android&logoColor=white)](https://foysalahammad.github.io/agent24)
[![Tools](https://img.shields.io/badge/built--in%20tools-31-blueviolet)](https://foysalahammad.github.io/agent24/#tools)
[![Docs](https://img.shields.io/badge/docs-foysalahammad.github.io%2Fagent24-22d3ee)](https://foysalahammad.github.io/agent24)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

[Docs](https://foysalahammad.github.io/agent24) ·
[Features](#-what-you-get) ·
[Agents](#-agents) ·
[Tools](#-tools) ·
[Providers](#-providers) ·
[Getting started](#-getting-started)

</div>

---

![Agent 24 chat screen](https://raw.githubusercontent.com/FoysalAhammad/agent24/main/docs/screenshots/chat.png)

---

## Introduction

Most Android "AI assistants" stop at chat replies. Agent 24 is built the other
way around: you state the goal, it works out a plan, picks the right tools,
runs them, checks the result, and only then reports back. Every step that could
touch your files, your shell, or your device goes through a permission gate, so
nothing surprising happens behind your back.

It ships as a complete workspace:

![Workspace drawer](https://raw.githubusercontent.com/FoysalAhammad/agent24/main/docs/screenshots/workspace.png)

- **AI Chat** — the main agent loop with streaming replies, tool cards, and
  reasoning display
- **Terminal** — a real Termux-based shell with the package manager, storage
  already mounted, and a welcome banner that links to this repository
- **Code Editor** — edit files without leaving the app
- **File Explorer** — browse the device and project tree

## What you get

| | |
|---|---|
| 🧠 **Truly agentic** | Plans, executes, verifies, and iterates — not just replies. |
| 🔧 **31 built-in tools** | Shell, files, search, patches, web, git, documents, vision, device control. |
| 🔐 **Permission-first** | Every sensitive action is `allow` / `ask` / `deny`, with a Deny · Always · Allow popup. |
| 📱 **Device control** | Read sensors, flash the torch, vibrate, change brightness, toggle wifi/location and more. |
| 🌍 **Model-agnostic** | Works with 13+ pre-configured providers and dozens of models. |
| 📴 **Everything stays local** | Sessions, history, memory and settings live on your device. |
| 🌐 **Speaks your language** | Understands you in Bangla, Hindi, and 97 other languages — with an option to force the reply language. |
| 🔌 **MCP-ready** | External MCP servers plug straight into the tool layer. |

## Agents

A layered agent system — pick the right one for the job.

| Agent | Type | Purpose |
|---|---|---|
| **Build** | Primary | Default agent with full tool access for real work. |
| **Plan** | Primary | Read-only analysis; asks before any edit or command. |
| **General** | Subagent | Autonomous multi-step tasks delegated by the main agent. |
| **Explore** | Subagent | Fast, read-only codebase search and summarisation. |
| **Scout** | Subagent | External documentation and dependency research. |
| **Compaction** | System | Summarises context automatically when it grows too long. |
| **Title / Summary** | System | Generates session titles and conversation summaries. |

## Tools

The model can call these during any conversation:

**Core** — `bash` `shell` `read` `write` `edit` `diff` `apply_patch`

**Search** — `grep` `glob` `list`

**Web** — `webfetch` `websearch`

**Documents & media** — `pdf` `pdf_edit` `pdf_maker` `docx_maker` `cv_maker`
`archive` `image_analyze` `image_describe`

**Device & system** — `screenshot` `ui_dump` `sensor`

**Productivity** — `git` `memory` `schedule` `todowrite` `todoread` `task`
`skill` `question`

You can also drop in your own tools as plain markdown files in the config
folder.

### Device control

The `sensor` tool talks to the hardware directly:

- list every sensor the phone exposes, take a live reading, or sample one over
  a few seconds with min/max/avg
- flashlight, vibrate, brightness, volume, rotation lock
- wifi, bluetooth, location, airplane mode, do-not-disturb, screen on/off

System-level changes ask for permission first and run through `su` when the
device is rooted — on a rooted phone the agent can grant its own missing
permission (like camera for the torch) with your approval.

### Slash commands

`/new` `/clear` `/sessions` `/model` `/connect` `/build` `/plan` `/init`
`/diff` `/cwd` `/undo` `/redo` `/fork` `/review` `/compact` `/share` `/skills`
`/agents` `/theme` `/export` `/import` `/help`

## Permissions

Every tool sits behind a permission key — `read`, `edit`, `bash`, `task`,
`webfetch`, `sensor`, and so on — with one of three values:

- **allow** — runs right away
- **ask** — pops a confirmation (Deny · Always · Allow) and waits
- **deny** — blocked completely

On first launch the app asks for everything it needs up front: storage, camera,
battery exemption, and all-files access. "Always" grants permission for the
whole session, so you are not clicking the same thing twice.

API credentials stay on your device, never show up in chat, and are never
written into exported sessions.

## Terminal

The terminal is a full Termux environment:

- search, install, and upgrade packages
- storage is mounted automatically at first launch — no setup command to type
- a welcome banner with links to the docs and this repository
- sessions share the same home directory the agent works in, so what it writes
  is what you see

## Reply language

The agent mirrors your language by default. If you prefer a fixed language, pick
one of 99 languages in settings and every reply comes back in that language,
no matter what language you typed in.

## Providers

Bring your own key — Agent 24 speaks the OpenAI-compatible protocol and comes
pre-configured for a wide ecosystem:

OpenAI · Anthropic · Google · Groq · DeepSeek · Mistral · xAI · Together ·
OpenRouter · HuggingFace · GitHub Models · Pollinations · and more.

Depending on the model you get tool calling, image input, reasoning display,
streaming, retry with exponential backoff, and automatic fallback when a
provider is unavailable.

## Requirements

- Android 8.0 (Oreo) or newer
- About 100 MB of free storage
- An internet connection for the AI providers
- An API key from any supported provider (free tiers work fine)

## Getting started

1. Install Agent 24 on your device.
2. Connect a provider with `/connect` — pick one, paste your API key.
3. Choose a model with `/model`.
4. Describe what you want and let it work.

```text
you   > build a script that renames all images in a folder by date
agent > plan → write the script → run it → verify the output → report back
```

Full documentation lives at
[foysalahammad.github.io/agent24](https://foysalahammad.github.io/agent24) —
agents, tools, permissions, providers, skills, MCP, sessions, and troubleshooting.

## Roadmap

- [x] MCP (Model Context Protocol) support
- [ ] Team sessions & shared workspaces
- [ ] Plugin / skill marketplace
- [ ] Local (on-device) model backend
- [ ] Desktop companion app

Bug reports and feature ideas are welcome in
[issues](https://github.com/FoysalAhammad/agent24/issues).

---

<div align="center">

**Developer:** [Foysal Ahammad](https://github.com/FoysalAhammad)

Released under the [MIT License](LICENSE).

**⭐ Star the repository if Agent 24 is useful to you.**

Made for the Android community

</div>
