from __future__ import annotations

from pathlib import Path

from .base_verifier import BaseVerifier, VerificationResult


class SetupControllerVerifier(BaseVerifier):
    name = "SetupControllerVerifier"

    def run(self, repo_root: Path) -> VerificationResult:
        details: list[str] = []
        ok = True

        required_dirs = [
            "addons",
            "ai",
            "docs",
            "scenes",
            "scripts",
            "tools",
        ]
        for path in required_dirs:
            if not self.require_dir(repo_root, path, self.name, details):
                ok = False

        required_files = [
            "project.godot",
            "README.md",
            ".tools/godot",
        ]
        for path in required_files:
            if not self.require_file(repo_root, path, self.name, details):
                ok = False

        if not self.require_text(repo_root, "project.godot", 'run/main_scene="res://scenes/main.tscn"', self.name, details):
            ok = False

        if not self.require_text(repo_root, "project.godot", 'config/name="Startup XR"', self.name, details):
            ok = False

        if ok:
            summary = "Project setup and controller foundations are valid."
        else:
            summary = "Project setup validation failed."

        return VerificationResult(name=self.name, ok=ok, summary=summary, details=details)
