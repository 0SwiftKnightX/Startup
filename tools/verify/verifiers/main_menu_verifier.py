from __future__ import annotations

from pathlib import Path

from .base_verifier import BaseVerifier, VerificationResult


class MainMenuVerifier(BaseVerifier):
    name = "MainMenuVerifier"

    def run(self, repo_root: Path) -> VerificationResult:
        details: list[str] = []
        ok = True

        if not self.require_file(repo_root, "scenes/main.tscn", self.name, details):
            ok = False
        if not self.require_file(repo_root, "scripts/main.gd", self.name, details):
            ok = False

        if not self.require_text(repo_root, "scripts/main.gd", "launch_button", self.name, details):
            ok = False
        if not self.require_text(repo_root, "scripts/main.gd", "quit_button", self.name, details):
            ok = False
        if not self.require_text(repo_root, "scripts/main.gd", "change_scene_to_file", self.name, details):
            ok = False

        if ok:
            summary = "Main menu boot flow is present and wired to the interaction lab."
        else:
            summary = "Main menu verification failed."

        return VerificationResult(name=self.name, ok=ok, summary=summary, details=details)
