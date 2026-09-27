from __future__ import annotations

import shutil
import subprocess
from pathlib import Path

from .base_verifier import BaseVerifier, VerificationResult


class FirstSliceRuntimeVerifier(BaseVerifier):
    name = "FirstSliceRuntimeVerifier"

    def run(self, repo_root: Path) -> VerificationResult:
        local_godot = repo_root / ".tools" / "godot"
        godot = str(local_godot) if local_godot.is_file() else shutil.which("godot")
        scene = repo_root / "tools" / "verify" / "runtime" / "first_slice_runtime_test.tscn"
        if not godot or not scene.is_file():
            return VerificationResult(
                name=self.name,
                ok=False,
                summary="Godot executable or first-slice runtime test scene is missing.",
                details=[f"Checked {local_godot} and PATH.", str(scene)],
            )

        completed = subprocess.run(
            [godot, "--headless", "--path", str(repo_root), str(scene), "--quit-after", "60"],
            capture_output=True,
            text=True,
            timeout=30,
            check=False,
        )
        output = f"{completed.stdout}\n{completed.stderr}".strip()
        if completed.returncode != 0 or "RUNTIME_PASS Quest first-slice fallback loop" not in output:
            return VerificationResult(
                name=self.name,
                ok=False,
                summary="First-slice runtime loop failed.",
                details=[f"Command exited with status {completed.returncode}.", output[-3000:]],
            )

        return VerificationResult(
            name=self.name,
            ok=True,
            summary="Menu-independent fallback loop scans the soul, gates attacks by aim, defeats the target, and resets.",
        )
