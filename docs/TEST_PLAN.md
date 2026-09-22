# Test Plan

## Objective

Establish a repeatable path from a local Godot change to a verified Meta Quest
3S build without confusing automated checks with physical XR evidence.

## Test Levels

### Level 1: Documentation and Static Checks

- Markdown links resolve to files in the repository.
- Version declarations agree across README, project bible, and validation docs.
- No document claims a test that has not been run.

### Level 2: Godot Project Checks

- Project opens in the locked Godot editor version.
- Main scene imports without parser errors.
- Boot menu opens the interaction lab and the cancel action returns to the menu.
- Input actions and XR scene dependencies resolve.
- Android export preset is present and loads correctly.

### Level 3: Desktop XR Checks

- OpenXR starts with a supported desktop runtime.
- Camera and controller poses track correctly.
- Locomotion, interaction, grabbing, and haptics behave as designed.
- No blocking runtime errors occur during a short smoke session.

### Level 4: Quest 3S Checks

- Candidate APK installs and launches.
- OpenXR initializes on the physical headset.
- Head tracking and both controller poses are correct.
- Intended interaction and locomotion paths work repeatedly.
- Comfort settings and tracking-loss behavior are acceptable.
- Performance is measured during the representative scene.

## Release Gate

A build is not Quest-ready until Levels 1 through 4 have evidence recorded in
[VALIDATION.md](VALIDATION.md) and the [Audit Archive](AUDIT_ARCHIVE.md).

## Test Record Template

```text
Date (UTC):
Commit:
Godot version:
Device/runtime:
Build or command:
Checks performed:
Result:
Failures and follow-up:
Tester:
```
