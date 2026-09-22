from __future__ import annotations

from pathlib import Path

from .base_verifier import BaseVerifier, VerificationResult


class HeroFlowVerifier(BaseVerifier):
    name = "HeroFlowVerifier"

    def run(self, repo_root: Path) -> VerificationResult:
        details: list[str] = []
        ok = True

        required_files = [
            "scripts/hero_state.gd",
            "scripts/interaction_lab.gd",
            "scenes/interaction_lab.tscn",
        ]
        for path in required_files:
            if not self.require_file(repo_root, path, self.name, details):
                ok = False

        state_contract = [
            "class_name HeroState",
            "SOUL_SELECTED",
            "SOUL_SCANNED",
            "TRANSFORMED",
            "ARENA",
            "func scan_soul()",
            "func transform()",
        ]
        for needle in state_contract:
            if not self.require_text(repo_root, "scripts/hero_state.gd", needle, self.name, details):
                ok = False

        interaction_contract = [
            "RayCast3D",
            "interact_grab",
            "interact_primary",
            "soul_block",
            "scan_station",
            "hero_state.select_soul()",
            "hero_state.scan_soul()",
            "hero_state.transform()",
        ]
        for needle in interaction_contract:
            if not self.require_text(repo_root, "scripts/interaction_lab.gd", needle, self.name, details) and not self.require_text(repo_root, "scenes/interaction_lab.tscn", needle, self.name, details):
                ok = False

        if ok:
            summary = "Soul selection, scanning, transformation, and arena state contracts are wired."
        else:
            summary = "Hero flow verification failed."

        return VerificationResult(name=self.name, ok=ok, summary=summary, details=details)
