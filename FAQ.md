# Agent24 — FAQ & Q&A

> Common questions and answers. Also tracked as [GitHub Issues](https://github.com/FoysalAhammad/agent24/issues?q=label%3Aquestion) with the `question` label.

---

## 💰 Pricing & Accounts

### Q: Is Agent24 free?
**A:** Yes. The app is 100% free, open source (MIT), with **no in-app purchases and no subscription**. You only pay your own AI provider (e.g. OpenAI) if you use a paid model. Free models are supported too (OpenCode Zen free tier, Gemini free tier, Ollama local). If ads appear, they come from the project's own signed configuration — no third-party ad SDK, no advertising identifier, no ad tracking.

### Q: Do I need to create an account?
**A:** No. There is no registration, no login, no Agent 24 server. Your conversations never leave your device except to the AI provider **you** configured (plus signed update/config checks, which contain no personal data).

### Q: Which AI providers are supported?
**A:** 12 providers: OpenAI, Anthropic, Google Gemini, DeepSeek, Groq, xAI, Meta (via providers), Alibaba Qwen, Ollama (local), LM Studio (local), GitHub Copilot, and OpenCode Zen. Add keys in **Settings → Models**.

### Q: Can I use it without internet?
**A:** Partially. Local models (Ollama / LM Studio on the same network) work offline. File tools, terminal, editor and sensors all work offline. Web tools and cloud AI need internet.

---

## 🔐 Privacy & Security

### Q: Does Agent24 collect my data?
**A:** No. There is no Agent24 server. Chat history lives in an app-private SQLite database on your device. Prompts go directly to the AI provider you chose, over TLS 1.3. See the [Privacy Policy](https://foysalahammad.github.io/agent24/#privacy).

### Q: Where are my API keys stored?
**A:** In the Android Keystore, encrypted with AES-256-GCM. They never leave your device except in the TLS request to your chosen provider.

### Q: Is the APK safe? How do I verify it?
**A:** Every GitHub Release publishes a SHA-256 checksum. The app also verifies its own integrity at launch: signing-certificate pin, SHA-512 dex fingerprint, and a native self-test that detects repackaging. Modified or re-signed builds are refused.

### Q: Does it need root?
**A:** No. Root is optional and only needed for the `sensor` tool's hardware controls (flashlight, brightness, volume). Everything else works without root.

### Q: Why does it ask for storage permission?
**A:** To read and write files in your workspace (the `read`, `write`, `edit`, `glob`, `grep` tools). All file access goes through the per-agent permission system.

---

## 🛠 Usage

### Q: How do I start?
**A:** 1) Install the APK, 2) Open **Settings → Models** → add one provider key, 3) Pick a model, 4) Chat. Type `/help` for commands.

### Q: What's the difference between Build and Plan mode?
**A:** **Build** mode has full tool access (runs commands, edits files). **Plan** mode is read-only — it analyses and proposes, then asks before any edit or shell command. Switch with `/build` or `/plan`.

### Q: How do I switch models or providers?
**A:** `/model` opens the model picker. `/connect` adds a provider key. Both live in **Settings → Models**.

### Q: A command failed — what now?
**A:** The agent shows the error and retries with a different approach. If it's stuck, `/new` starts a fresh session, or `/compact` shrinks a long conversation. 401 = re-enter key, 429 = wait or switch model.

### Q: How do I export my conversation?
**A:** `/export` — exports the session as Markdown or JSON to your device.

### Q: Can the agent break my phone?
**A:** Every tool call goes through a permission gate (`allow` / `ask` / `deny`), configurable per agent. Plan mode asks before every destructive action. The app cannot bypass Android's own security model.

---

## 📦 Install & Update

### Q: How do I install?
**A:** Download the APK from [Releases](https://github.com/foysalahammad/agent24/releases/latest) and open it, or `adb install -r agent24_arm64-v8a.apk`. Most phones (2017+) use the arm64 build.

### Q: How do I update?
**A:** The app checks GitHub Releases automatically and prompts you. Or manually download the newer APK — it installs over the existing one and keeps your data.

### Q: Will updating delete my sessions or keys?
**A:** No. Updates preserve the app-private data directory: sessions, settings and API keys are kept. Only the APK code changes.

### Q: Is it on Google Play?
**A:** Play Store release is in preparation (privacy policy, content rating and data safety forms are ready). Until then, install from GitHub Releases.

---

## 🐛 Problems

### Q: The app crashes on launch
**A:** Update to the latest release. If it persists, clear app data (Settings → Apps → Agent24 → Clear data) — note this removes sessions. Report with device model + Android version.

### Q: The terminal shows "bootstrap" messages
**A:** First run installs a Termux bootstrap (one-time). Later sessions open clean. If it repeats, uninstall and reinstall.

### Q: AI replies are slow
**A:** Switch to a faster model (`/model`). Local Ollama/LM Studio models are fastest but need a decent phone or LAN server.

### Q: How do I report a bug?
**A:** [Open an issue](https://github.com/FoysalAhammad/agent24/issues/new?template=bug_report.md) with device, Android version, app version, steps to reproduce, and logs if available.

### Q: How do I report a security vulnerability?
**A:** Do **not** open a public issue. Use [GitHub Security Advisories](https://github.com/FoysalAhammad/agent24/security/advisories) (private reporting). Acknowledged within 7 days.

---

## 🌐 Community

### Q: Where do I ask questions?
**A:** [GitHub Discussions](https://github.com/Foysalahammad/agent24/discussions) (if enabled) or open an issue with the `question` label. The in-app **Help** dialog also has an FAQ.

### Q: How do I contribute?
**A:** See [CONTRIBUTING.md](CONTRIBUTING.md). Fork → branch → test → PR. Bug reports and translations are welcome too.

### Q: Is there a roadmap?
**A:** [GitHub Issues](https://github.com/foysalahammad/agent24/issues) with the `enhancement` label tracks planned work.

---

*Last updated: 10 October 2026 · See also: [Privacy Policy v2.0](https://foysalahammad.github.io/agent24/#privacy) · [Documentation](https://foysalahammad.github.io/agent24/)*
