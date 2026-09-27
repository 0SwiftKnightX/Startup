# Changelog

All notable changes to this project will be documented in this file.

The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and
this project uses semantic versioning when releases begin.

## [Unreleased]

### Added

- Established Meta Quest 3S as the initial target device.
- Documented the Godot 4.6+, OpenXR, Godot XR Tools, and OpenXR Vendors stack.
- Defined the initial XR mechanics roadmap.
- Added organized `docs/` documentation for the project bible, architecture,
	validation, test planning, audit archive, historical GPT records, and active
	GPT worklog.
- Added `ai/` governance with shared AI rules and separate Copilot and Gemini
	worklogs.
- Reworked the root README into a navigation-first project overview.
- Added all four approved XR reference repositories with direct links and use
	cases: the Godot XR Template, Godot XR Tools, the Flynn demo, and the Malcolm
	Nixon XR Tools demo.
- Added the initial Godot project foundation with boot, menu, interaction-lab,
  input, and shared game-state files.
- Added integration blueprint, interaction contracts, locomotion profiles, level
  flow, and asset-pipeline documentation for combining the reference features.
- Installed and integrated Godot 4.7.2-stable, XR Tools master, and OpenXR
	Vendors 5.1.0-stable for local validation.
- Installed the matching Godot 4.7.2 Android export templates for future Quest
  APK builds.
- Enabled the OpenXR module and shaders, configured the Mobile renderer, and
	added a Quest Touch action map for controls, poses, and haptics.
- Added the canonical XR player rig, low-poly tracked hands, world-space XR
	menu, XR Tools body/movement/pickup/pointer components, and optional arm-swing.
- Added scan station feedback, haptics, an aim-gated arena target, and a
	deterministic fallback end-to-end runtime test.
- Expanded the shared verification suite to twelve checks, including a negative
	contract test and CI-compatible Godot executable discovery.
- Updated the Quest Android workflow to install Python before running project
	verification.

### Validation and Limitations

- Godot 4.7.2 headless import and the 12-check verifier suite pass locally.
- The end-to-end desktop fallback loop passes; it does not constitute OpenXR or
	Quest device validation.
- The latest observed GitHub Actions run failed because the CI image lacked
	Python. The workflow fix is local and still requires a push and successful
	rerun before an APK artifact is available.
- This workspace lacks a usable OpenXR runtime, Android SDK/ADB, and Android
	export templates. Quest 3S acceptance, comfort, and performance evidence are
	still pending.

## 2026-09-22

### Documentation

- **Updated:** 2026-09-22T03:39:19Z
- **Signed:** GitHub Copilot

### XR Reference Documentation

- Recorded the four-repository XR reference set in the README, Project Bible,
  Architecture document, audit archive, and AI worklogs.
- **Updated:** 2026-09-22T03:42:08Z
- **Signed:** GitHub Copilot

### Godot Foundation

- Added the first staged implementation slice and documented the remaining XR
	addon and Quest validation gates.
- **Updated:** 2026-09-22T03:50:49Z
- **Signed:** GitHub Copilot

### Toolchain Installation

- Installed Godot locally and integrated the XR Tools and OpenXR Vendors addons.
- Headless editor import and project smoke test passed.
- Desktop OpenXR and physical Quest 3S validation remain pending.
- **Updated:** 2026-09-22T03:58:23Z
- **Signed:** GitHub Copilot

### Android Export Preparation

- Installed Godot 4.7.2-stable Android export templates.
- Android SDK, ADB, and physical Quest 3S deployment remain pending.
- **Updated:** 2026-09-22T04:00:17Z
- **Signed:** GitHub Copilot

[unreleased]: https://github.com/0SwiftKnightX/Startup/compare/HEAD...HEAD
