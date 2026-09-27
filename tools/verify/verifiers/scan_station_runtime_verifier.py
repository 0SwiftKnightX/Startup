from __future__ import annotations

import subprocess
import shutil
from pathlib import Path

from .base_verifier import BaseVerifier, VerificationResult


class ScanStationRuntimeVerifier(BaseVerifier):
    name = "ScanStationRuntimeVerifier"

    def run(self, repo_root: Path) -> VerificationResult:
        local_godot = repo_root / ".tools" / "godot"
        godot = str(local_godot) if local_godot.is_file() else shutil.which("godot")
        scene = repo_root / "tools" / "verify" / "runtime" / "scan_station_runtime_test.tscn"
        if not godot or not scene.exists():
            return VerificationResult(
                name=self.name,
                ok=False,
                summary="Godot executable or scan-station runtime test scene is missing.",
                details=[f"Checked {local_godot} and PATH.", str(scene)],
            )

        completed = subprocess.run(
            [godot, "--headless", "--path", str(repo_root), str(scene), "--quit-after", "30"],
            capture_output=True,
            text=True,
            timeout=20,
            check=False,
        )
        output = f"{completed.stdout}\n{completed.stderr}".strip()
        if completed.returncode != 0 or "RUNTIME_PASS ScanStation contract" not in output:
            return VerificationResult(
                name=self.name,
                ok=False,
                summary="Scan station runtime contract failed.",
                details=[f"Command exited with status {completed.returncode}.", output[-2000:]],
            )

        return VerificationResult(
            name=self.name,
            ok=True,
            summary="Scan station overlap, soul filtering, duplicate rejection, and reset execute correctly.",
        )
