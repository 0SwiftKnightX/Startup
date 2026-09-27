# Reference and Code Reuse Rules

## Purpose

Startup uses other repositories as research and implementation references. Reuse proven work when it is legally permitted and technically compatible, without treating a public repository as automatic permission to copy everything.

## Required AI behavior

Before copying code, assets, documentation, or other protected material:

1. Locate the source repository and exact file/path.
2. Inspect its LICENSE and any path-specific notices.
3. Identify the applicable license.
4. Confirm that the intended copy, modification, and distribution are permitted.
5. Preserve required copyright, license, attribution, or notice text.
6. Record source repository, source path, source commit/release, license, and reused scope in the worklog/provenance record.
7. Verify compatibility with Startup's Godot/XR versions.
8. Run Startup verification after integration.
9. If permission or licensing is unclear, do not copy the material. Use it as a conceptual reference or obtain permission.

## Prompt rule

Startup development prompts should say:

> Reuse existing implementations, patterns, and code when the source license or explicit permission permits the intended use. Prefer proven, compatible implementations over unnecessary reinvention. Preserve required notices and record provenance. Never copy code solely because it is publicly visible on GitHub.

## Current approved reference set

- GodotVR/godot-xr-template — project initialization and Android/Quest structure.
- GodotVR/godot-xr-tools — XR interaction, locomotion, grabbing, UI, and haptics.
- BastiaanOlij/godot-xr-flynn-demo — multi-level/performance architecture reference.
- Malcolmnixon/godot-xr-tools-demo — locomotion/traversal reference.
- 0SwiftKnightX/ProjectMythos — owner-owned prior Godot prototype reference.
- 0SwiftKnightX/Personal-quest-development- — owner-owned XR composition/reference project.
- 0SwiftKnightX/XrGpt — owner-owned XR foundation reference; Startup remains separate.

## License evidence checked 2026-09-27

- GodotVR/godot-xr-template — MIT
- GodotVR/godot-xr-tools — MIT
- BastiaanOlij/godot-xr-flynn-demo — MIT
- Malcolmnixon/godot-xr-tools-demo — MIT

MIT reuse still requires preservation of the copyright and permission notice in copies or substantial portions.

Startup currently has no root LICENSE file. Do not infer a project license that is not present.

## Separation rule

Reference, research, and provenance do not automatically mean code was copied. Record only material actually reused as reused material.