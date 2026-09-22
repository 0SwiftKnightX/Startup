# Startup

An experimental Godot XR game project focused on responsive, comfortable, and
polished experiences for Meta Quest headsets.

## Project Status

Early development. The repository now contains a minimal Godot foundation with
boot, menu, and interaction-lab scenes. XR plugin integration and device
validation are still pending.

## Target Platform

- **Headset:** Meta Quest 3S
- **Quest target declaration:** 4.7.1
- **XR runtime:** OpenXR
- **Engine:** Godot 4.7.2-stable (validated locally)

The target declaration must be checked against the selected Godot editor and
plugin versions before implementation begins.

## XR Stack

- [Godot XR Tools current master](https://github.com/GodotVR/godot-xr-tools/tree/master)
	for locomotion, grabbing, climbing, interaction, haptics, and XR UI. The
	current branch includes the Godot 4.7 compatibility fixes documented in its
	version history.
- [OpenXR Vendors 5.1.0-stable](https://github.com/GodotVR/godot_openxr_vendors/releases/tag/5.1.0-stable)
	for Android headset support and vendor-specific OpenXR extensions.
- [Godot XR Tools documentation](https://godotvr.github.io/godot-xr-tools/)
	for implementation guidance and reference scenes.

## Reference Repositories

These repositories inform the XR stack and development approach for Startup.
They are reference sources, not automatically integrated dependencies. Their
branches, releases, and Godot compatibility must be checked before reuse.

| Repository | Primary use case | Key features referenced |
| --- | --- | --- |
| [GodotVR/godot-xr-template](https://github.com/GodotVR/godot-xr-template) | Project initialization | Android and Meta Quest export presets, vendor loaders, main menu structure, and basic locomotion configuration. |
| [GodotVR/godot-xr-tools](https://github.com/GodotVR/godot-xr-tools) | Core library and API reference | Physics-based hands, viewport UI interaction, grab and throw mechanics, and standard snap-turning. |
| [BastiaanOlij/godot-xr-flynn-demo](https://github.com/BastiaanOlij/godot-xr-flynn-demo) | Advanced architecture study | Multi-level management, performance-aware asset structure, and stable game-loop integration. |
| [Malcolmnixon/godot-xr-tools-demo](https://github.com/Malcolmnixon/godot-xr-tools-demo) | Advanced locomotion recipes | Gliding, low-traction surfaces, wind-assisted movement, and physics climbing. |

The project combines stable, compatible ideas from these references rather than
copying their projects wholesale. See the [Project Bible](docs/PROJECT_BIBLE.md)
and [Architecture](docs/ARCHITECTURE.md) for the adopted direction.

## Planned Mechanics

- Comfortable direct movement and teleportation
- Controller and hand-based interaction
- Physical grabbing and object manipulation
- Climbing and traversal systems
- Haptic feedback and spatial UI
- Quest-friendly performance and comfort settings

## Documentation

- [Documentation index](docs/INDEX.md) - map of project documentation.
- [Project Bible](docs/PROJECT_BIBLE.md) - product intent and scope.
- [Architecture](docs/ARCHITECTURE.md) - planned system boundaries.
- [Validation](docs/VALIDATION.md) - evidence and current validation status.
- [Test Plan](docs/TEST_PLAN.md) - desktop and Quest 3S test gates.
- [Audit Archive](docs/AUDIT_ARCHIVE.md) - dated findings and decisions.
- [Historical GPT Log](docs/HISTORICAL_GPT_LOG.md) - preserved historical record.
- [GPT Worklog](docs/GPT_WORKLOG.md) - active AI-assisted engineering log.
- [Integration Blueprint](docs/INTEGRATION_BLUEPRINT.md) - how the four reference repositories combine.
- [Interaction Contracts](docs/INTERACTION_CONTRACTS.md) - grab, UI, hands, and snap-turn behavior.
- [Locomotion Profiles](docs/LOCOMOTION_PROFILES.md) - movement feature boundaries.
- [Level Flow](docs/LEVEL_FLOW.md) - scene transition and game-loop responsibilities.
- [Asset Pipeline](docs/ASSET_PIPELINE.md) - performance-aware asset organization.

## AI-Assisted Development

AI governance and agent-specific worklogs are maintained separately in the
[ai/](ai/README.md) directory. All agents must follow the [AI Rules and
Regulations](ai/AI_RULES.md) and must distinguish verified evidence from plans.

## Development Setup

The foundation can be opened in Godot 4.7.2 and starts with a desktop menu and
interaction-lab placeholder. Install compatible XR dependencies before enabling
OpenXR or Quest deployment. Start with the [Integration Blueprint](docs/INTEGRATION_BLUEPRINT.md),
then follow the [Test Plan](docs/TEST_PLAN.md) and [Validation](docs/VALIDATION.md).

Physical Quest testing is required for tracking, performance, passthrough,
comfort, and controller behavior. PCVR preview and headless checks do not replace
device evidence.

## Changelog

See the [CHANGELOG.md](CHANGELOG.md) file for the project history and upcoming
changes.

## Update Record

- **Updated:** 2026-09-22T03:50:49Z
- **Signed:** GitHub Copilot
