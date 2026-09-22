from __future__ import annotations

from pathlib import Path

from .base_verifier import BaseVerifier, VerificationResult


class XRPlayerVerifier(BaseVerifier):
    name = "XRPlayerVerifier"

    def run(self, repo_root: Path) -> VerificationResult:
        details: list[str] = []
        ok = True
        contracts = [
            '[node name="XRPlayer" type="XROrigin3D"]',
            '[node name="XRCamera3D" type="XRCamera3D" parent="."]',
            '[node name="LeftController" type="XRController3D" parent="."]',
            '[node name="RightController" type="XRController3D" parent="."]',
            'tracker = &"left_hand"',
            'tracker = &"right_hand"',
            'ranged_enable = true',
            'ranged_distance = 5.0',
            'res://addons/godot-xr-tools/xr/start_xr.tscn',
            'res://scripts/comfort_locomotion.gd',
        ]
        for contract in contracts:
            if not self.require_text(repo_root, "scenes/xr_player.tscn", contract, self.name, details):
                ok = False

        for action in [
            "xr_move_left={",
            "xr_move_right={",
            "xr_move_forward={",
            "xr_move_back={",
            "xr_turn_left={",
            "xr_turn_right={",
            "xr_left_grip={",
            "xr_right_grip={",
            "xr_left_trigger={",
            "xr_right_trigger={",
        ]:
            if not self.require_text(repo_root, "project.godot", action, self.name, details):
                ok = False

        for contract in [
            "left_pickup.has_picked_up.connect",
            "right_pickup.has_picked_up.connect",
            "left_pickup.has_dropped.connect",
            "right_pickup.has_dropped.connect",
            "func _on_xr_picked_up",
            "func _on_xr_dropped",
        ]:
            if not self.require_text(repo_root, "scripts/interaction_lab.gd", contract, self.name, details):
                ok = False

        summary = "Canonical XR origin, controllers, pickup functions, and action names are wired." if ok else "XR player verification failed."
        return VerificationResult(name=self.name, ok=ok, summary=summary, details=details)
