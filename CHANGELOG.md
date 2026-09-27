# Changelog

All notable changes to this project will be documented in this file.

The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and
this project uses semantic versioning when releases begin.

## [Unreleased]

### Added

- Established Meta Quest 3S as the initial target device.
- Standardized the current engine baseline on Godot 4.7.2-stable.
- Documented the Godot 4.7.2-stable, OpenXR, Godot XR Tools, and OpenXR Vendors stack.
- Defined the initial XR mechanics roadmap.
- Added organized docs/ documentation for the project bible, architecture,
  validation, test planning, audit archive, historical GPT records, and active
  GPT worklog.
- Added ai/ governance with shared AI rules and separate Copilot and Gemini
  worklogs.
- Added the initial Godot project foundation with boot, menu, interaction-lab,
  input, and shared game-state files.
- Added integration blueprint, interaction contracts, locomotion profiles, level
  flow, and asset-pipeline documentation.
- Installed and integrated Godot 4.7.2-stable, XR Tools master, and OpenXR
  Vendors 5.1.0-stable for local validation.
- Installed the matching Godot 4.7.2 Android export templates for future Quest
  APK builds.
- Enabled OpenXR and XR shaders and added a Quest Touch action map for controls,
  poses, and haptics.
- Added the canonical XR player rig, low-poly tracked hands, world-space XR
  menu, XR Tools body/movement/pickup/pointer components, and optional arm-swing.
- Added scan station feedback, haptics, an aim-gated arena target, and a
  deterministic fallback end-to-end runtime test.
- Expanded the verification suite to twelve checks.
- Updated the Quest Android workflow to install Python before project verification.
- Added a lit 3D Quest lobby around the separate world-space menu.
- Corrected fallback camera height, fallback controller placement, menu placement,
  pointer reach, and XR Tools locomotion configuration.

### Validation and Limitations

- Godot 4.7.2 headless import and the 12-check verifier suite pass locally.
- The end-to-end desktop fallback loop passes; it does not constitute Quest device validation.
- GitHub Actions run 36226832612 failed because the CI image lacked Python; the
  workflow now installs Python and needs a fresh successful run before an APK artifact
  can be treated as evidenced.
- An exploratory Quest 3S run has confirmed tracked hands and controller button input,
  but the lobby/menu was extremely dark or not visible and there was no usable player
  area. This exposed the presentation/lobby gap now being repaired.
- Full Quest acceptance, comfort, performance, APK deployment, and lifecycle evidence
  remain open.

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


## 2026-09-27 - Startup continuity v1.1 and XR baseline

### Added

- Added Project Handoff Template Version 1.1 with AI self-naming/collision rules, Eastern Time recording, worklog/changelog continuity, and reference/code-reuse provenance.
- Added `ai/REFERENCE_AND_REUSE_RULES.md`.
- Added README credits/reference links for the official XR repositories and owner-owned related repositories.

### Changed

- Enabled a 90 Hz physics tick baseline for the Quest XR project.
- Enabled XR viewport VRS for the Mobile renderer through the canonical XR player startup path.

### Validation

- Changes are statically inspected in GitHub.
- Godot/Quest runtime validation remains a separate evidence gate and is not claimed by this documentation/configuration change.
