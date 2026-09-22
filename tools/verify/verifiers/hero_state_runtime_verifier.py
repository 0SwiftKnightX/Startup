from __future__ import annotations

import subprocess
from pathlib import Path

from .base_verifier import BaseVerifier, VerificationResult


class HeroStateRuntimeVerifier(BaseVerifier):
    name = "HeroStateRuntimeVerifier"

    def run(self, repo_root: Path) -> VerificationResult:
        details: list[str] = []
        test_scene = repo_root / "tools" / "verify" / "runtime" / "hero_state_runtime_test.tscn"
        godot = repo_root / ".tools" / "godot"

        if not godot.exists():
            return VerificationResult(
                name=self.name,
                ok=False,
                summary="Godot executable is unavailable for runtime verification.",
                details=[str(godot)],
            )
        if not test_scene.exists():
            return VerificationResult(
                name=self.name,
                ok=False,
                summary="Hero state runtime test scene is missing.",
                details=[str(test_scene)],
            )

        command = [
            str(godot),
            "--headless",
            "--path",
            str(repo_root),
            str(test_scene),
            "--quit-after",
            "2",
        ]
        completed = subprocess.run(
            command,
            capture_output=True,
            text=True,
            timeout=15,
            check=False,
        )
        output = f"{completed.stdout}\n{completed.stderr}".strip()
        if completed.returncode != 0 or "RUNTIME_PASS HeroState transitions" not in output:
            details.append(f"Command exited with status {completed.returncode}.")
            details.append(output[-2000:] if output else "No runtime output.")
            return VerificationResult(
                name=self.name,
                ok=False,
                summary="HeroState runtime transitions failed.",
                details=details,
            )

        return VerificationResult(
            name=self.name,
            ok=True,
            summary="HeroState transitions execute and reset correctly in Godot.",
        )
