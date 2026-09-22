from __future__ import annotations

from pathlib import Path

from .base_verifier import BaseVerifier, VerificationResult


class ProjectContractVerifier(BaseVerifier):
    name = "ProjectContractVerifier"

    def run(self, repo_root: Path) -> VerificationResult:
        details: list[str] = []
        ok = True

        scene_contracts = {
            "scenes/main.tscn": [
                '[node name="StartupXR" type="Node"]',
                'script = ExtResource("1_main")',
                '[node name="LaunchButton" type="Button" parent="MainMenu/Panel/Content"]',
            ],
            "scenes/interaction_lab.tscn": [
                '[node name="InteractionLab" type="Node3D"]',
                'script = ExtResource("1_lab")',
                '[node name="Pointer" type="RayCast3D" parent="."]',
                '[node name="SoulBlock" type="RigidBody3D" parent="."]',
                'script = ExtResource("4_pickable")',
                '[node name="ScanStation" type="Node3D" parent="."]',
                'script = ExtResource("5_scan")',
                '[node name="InteractionArea" type="Area3D" parent="ScanStation"]',
                '[node name="HeroState" type="Node" parent="."]',
                '[node name="PlayerRig" parent="." instance=ExtResource("3_player")]',
                '[node name="ArenaTarget" type="Node3D" parent="."]',
                'script = ExtResource("6_target")',
            ],
        }
        for scene_path, contracts in scene_contracts.items():
            for contract in contracts:
                if not self.require_text(repo_root, scene_path, contract, self.name, details):
                    ok = False

        input_contracts = [
            "interact_grab={",
            "interact_primary={",
            "move_forward={",
            "move_back={",
            "move_left={",
            "move_right={",
        ]
        for contract in input_contracts:
            if not self.require_text(repo_root, "project.godot", contract, self.name, details):
                ok = False

        summary = "Project scene, script, node, and input contracts are present." if ok else "Project contract verification failed."
        return VerificationResult(name=self.name, ok=ok, summary=summary, details=details)
