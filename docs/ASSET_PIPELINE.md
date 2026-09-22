# Asset Pipeline

## Goals

Keep XR scenes fast to load, easy to profile, and safe to reuse across levels.

## Rules

- Store source assets separately from imported Godot resources.
- Prefer reusable scenes and shared materials over per-level duplicates.
- Keep collision meshes simple and intentional for Quest performance.
- Use level-specific asset manifests when multi-level loading is introduced.
- Avoid loading all levels and high-resolution assets at boot.
- Profile memory, draw calls, shader compilation, and frame timing on Quest 3S.
- Record major asset pipeline decisions in the audit archive.

## Proposed Layout

```text
assets/
  source/
  materials/
  meshes/
  textures/
  audio/
scenes/
  shared/
  levels/
  testbeds/
scripts/
  platform/
  xr/
  gameplay/
```

This layout is a target for the implementation phase; the repository currently
contains only the initial foundation scenes and documentation.
