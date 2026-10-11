# Contributing to Agent 24

Thanks for taking the time to contribute. This document explains the workflow
and the few rules that keep the project consistent.

## Ways to contribute

- **Bug reports** — open a bug issue with device model, Android version, app
  version and exact steps to reproduce. Logs help a lot.
- **Feature ideas** — open an issue with the `enhancement` label first, so the
  direction can be discussed before any code is written.
- **Translations** — in-app strings and docs translations are always welcome.
- **Code** — bug fixes, tool improvements, docs corrections.

## Development setup

1. Clone the repository.
2. Open the project in Android Studio (or build from the command line):

   ```bash
   export ANDROID_HOME=$HOME/Android/Sdk
   ./gradlew assembleDebug
   ```

3. Install on a device or emulator:

   ```bash
   adb install -r app/build/outputs/apk/debug/agent24_apt-android-7-debug_arm64-v8a.apk
   ```

Minimum tooling: JDK 17, Android SDK with build-tools, Gradle wrapper (bundled).

## Pull request workflow

1. Fork the repository and create a branch from `main`.
2. Make focused changes — one concern per PR.
3. Build both variants before pushing:

   ```bash
   ./gradlew assembleDebug assembleRelease
   ```

4. Test the change on a real device or the `testdev` emulator when it touches
   UI, permissions or tools.
5. Open a pull request with a short description of the problem and the fix.

## Style guidelines

- Java and Kotlin files follow the existing style of the file you touch —
  match indentation, naming and comment density of the surrounding code.
- User-facing text is written in plain, natural English. No filler, no
  hype.
- Keep privacy guarantees intact: never add telemetry, tracking or new data
  leaves without an issue discussing it first.
- Secrets, API keys and personal data never belong in the repository.

## Reporting security issues

Do **not** open a public issue for vulnerabilities. Use
[GitHub Security Advisories](https://github.com/FoysalAhammad/agent24/security/advisories)
for private reporting. Reports are acknowledged within 7 days.

## License

By contributing you agree that your contributions are licensed under the
[MIT License](LICENSE) that covers the project.
