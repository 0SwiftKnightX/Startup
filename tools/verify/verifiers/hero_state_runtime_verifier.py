from __future__ import annotations

import subprocess
import shutil
from pathlib import Path

from .base_verifier import BaseVerifier, VerificationResult


class HeroStateRuntimeVerifier(BaseVerifier):
    name = "HeroStateRuntimeVerifier"

    def run(self, repo_root: Path) -> VerificationResult:
        details: list[str] = []
        test_scene = repo_root / "tools" / "verify" / "runtime" / "hero_state_runtime_test.tscn"
        local_godot = repo_root / ".tools" / "godot"
        godot = str(local_godot) if local_godot.is_file() else shutil.which("godot")

        if not godot:
            return VerificationResult(
                name=self.name,
                ok=False,
                summary="Godot executable is unavailable for runtime verification.",
            details=[f"Checked {local_godot} and PATH."],
            )
        if not test_scene.exists():
            return VerificationResult(
                name=self.name,
                ok=False,
                summary="Hero state runtime test scene is missing.",
                details=[str(test_scene)],
            )

        command = [
            godot,
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
        runtime_pass = (
            "RUNTIME_PASS HeroState transitions" in output
            or "RUNTIME_PASS Quest-first loop transitions" in output
        )
        if completed.returncode != 0 or not runtime_pass:
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
