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

        # Godot may normalize the explicit mobile renderer entry during import.
        # Accept either the source form or the canonical imported form; both
        # require the project to remain on the mobile renderer.
        project_text = (repo_root / "project.godot").read_text(encoding="utf-8")
        mobile_renderer = (
            'renderer/rendering_method.mobile="mobile"' in project_text
            or 'renderer/rendering_method="mobile"' in project_text
        )
        if not mobile_renderer:
            details.append(
                'Expected mobile renderer setting in project.godot: '
                'renderer/rendering_method="mobile" or '
                'renderer/rendering_method.mobile="mobile"'
            )
            ok = False

        if not self.require_text(repo_root, "project.godot", "openxr/enabled=true", self.name, details):
            ok = False

        if ok:
            summary = "XR runtime configuration is present for the startup foundation."
        else:
            summary = "XR runtime verification failed."

        return VerificationResult(name=self.name, ok=ok, summary=summary, details=details)
