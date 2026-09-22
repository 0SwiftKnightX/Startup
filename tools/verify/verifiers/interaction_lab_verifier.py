from __future__ import annotations

from pathlib import Path

from .base_verifier import BaseVerifier, VerificationResult


class InteractionLabVerifier(BaseVerifier):
    name = "InteractionLabVerifier"

    def run(self, repo_root: Path) -> VerificationResult:
        details: list[str] = []
        ok = True

        if not self.require_file(repo_root, "scenes/interaction_lab.tscn", self.name, details):
            ok = False
        if not self.require_file(repo_root, "scripts/interaction_lab.gd", self.name, details):
            ok = False

        if not self.require_text(repo_root, "scripts/interaction_lab.gd", "MAIN_MENU_SCENE", self.name, details):
            ok = False
        if not self.require_text(repo_root, "scripts/interaction_lab.gd", "menu_cancel", self.name, details):
            ok = False
        if not self.require_text(repo_root, "scripts/interaction_lab.gd", "change_scene_to_file", self.name, details):
            ok = False

        if ok:
            summary = "Interaction lab foundation is present and returns to the main menu correctly."
        else:
            summary = "Interaction lab verification failed."

        return VerificationResult(name=self.name, ok=ok, summary=summary, details=details)
