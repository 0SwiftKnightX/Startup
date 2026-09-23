# GitHub Automation

This folder contains repository automation.

- `workflows/android-quest3s-debug.yml` builds the Android ARM64 debug APK in GitHub Actions.
- The workflow imports the Godot project, runs `tools/verify/run_all.py`, exports the `Android Quest 3S` preset, and uploads the APK as an artifact.

The cloud build does not validate physical Quest tracking, controller behavior, comfort, or performance. Those require a Quest 3S acceptance test.
