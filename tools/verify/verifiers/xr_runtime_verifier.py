from __future__ import annotations

from pathlib import Path

from .base_verifier import BaseVerifier, VerificationResult


class XRRuntimeVerifier(BaseVerifier):
    name = "XRRuntimeVerifier"

    def run(self, repo_root: Path) -> VerificationResult:
        details: list[str] = []
        ok = True

        if not self.require_text(repo_root, "project.godot", "XRToolsUserSettings", self.name, details):
            ok = False
        if not self.require_text(repo_root, "project.godot", "XRToolsRumbleManager", self.name, details):
            ok = False
        if not self.require_text(repo_root, "project.godot", "hand_tracking=true", self.name, details):
            ok = False
        if not self.require_text(repo_root, "project.godot", "renderer/rendering_method.mobile=\"gl_compatibility\"", self.name, details):
            ok = False

        if ok:
            summary = "XR runtime configuration is present for the startup foundation."
        else:
            summary = "XR runtime verification failed."

        return VerificationResult(name=self.name, ok=ok, summary=summary, details=details)
