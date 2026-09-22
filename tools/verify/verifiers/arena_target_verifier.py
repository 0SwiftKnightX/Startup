from __future__ import annotations

from pathlib import Path

from .base_verifier import BaseVerifier, VerificationResult


class ArenaTargetVerifier(BaseVerifier):
    name = "ArenaTargetVerifier"

    def run(self, repo_root: Path) -> VerificationResult:
        details: list[str] = []
        ok = True
        for needle in [
            "class_name ArenaTarget",
            "func receive_attack",
            "func reset",
            "signal damaged",
            "signal defeated",
        ]:
            if not self.require_text(repo_root, "scripts/arena_target.gd", needle, self.name, details):
                ok = False
        for needle in [
            "@onready var arena_target: ArenaTarget",
            "arena_target.receive_attack()",
            "Target health",
        ]:
            if not self.require_text(repo_root, "scripts/interaction_lab.gd", needle, self.name, details):
                ok = False
        summary = "Arena target health, attack, defeat, and reset contracts are present." if ok else "Arena target verification failed."
        return VerificationResult(name=self.name, ok=ok, summary=summary, details=details)
