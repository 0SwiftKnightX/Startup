# Verifiers

Each Python module in this folder defines a project or feature verifier.

- Static verifiers check files, scenes, scripts, node contracts, input actions, and wiring.
- Runtime verifiers invoke Godot tests when static inspection cannot prove behavior.
- Every verifier class must be listed in `tools/verify/verifier_manifest.json`.

Run the complete suite from the repository root:

```bash
python3 tools/verify/run_all.py
```

A new system is incomplete until its verifier and validation evidence are added.
