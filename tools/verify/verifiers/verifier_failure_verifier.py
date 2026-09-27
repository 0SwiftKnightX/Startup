from __future__ import annotations

import tempfile
from pathlib import Path

from .base_verifier import BaseVerifier, VerificationResult
from .project_contract_verifier import ProjectContractVerifier


class VerifierFailureVerifier(BaseVerifier):
    name = "VerifierFailureVerifier"

    def run(self, repo_root: Path) -> VerificationResult:
        with tempfile.TemporaryDirectory(prefix="startup-verifier-negative-") as temporary_directory:
            fixture_root = Path(temporary_directory)
            scenes = fixture_root / "scenes"
            scenes.mkdir()
            (scenes / "main.tscn").write_text(
                '\n'.join([
                    '[node name="StartupXR" type="Node"]',
                    'script = ExtResource("1_main")',
                    '[node name="PlayerRig" parent="." instance=ExtResource("2_player")]',
                    '[node name="MenuSurface" parent="PlayerRig" instance=ExtResource("3_viewport")]',
                    'scene = ExtResource("4_menu")',
                ]),
                encoding="utf-8",
            )
            (scenes / "main_menu_panel.tscn").write_text(
                '[node name="MainMenuPanel" type="Control"]\n'
                '[node name="QuitButton" type="Button" parent="Panel/Content"]\n',
                encoding="utf-8",
            )
            (scenes / "interaction_lab.tscn").write_text(
                '\n'.join([
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
                    '[node name="ArenaTarget" type="StaticBody3D" parent="."]',
                    '[node name="Collision" type="CollisionShape3D" parent="ArenaTarget"]',
                    'script = ExtResource("6_target")',
                ]),
                encoding="utf-8",
            )
            (fixture_root / "project.godot").write_text(
                "interact_grab={\ninteract_primary={\nmove_forward={\nmove_back={\nmove_left={\nmove_right={\n",
                encoding="utf-8",
            )

            result = ProjectContractVerifier().run(fixture_root)
            failed_with_source = (
                not result.ok
                and any("scenes/main_menu_panel.tscn" in detail for detail in result.details)
                and any("LaunchButton" in detail for detail in result.details)
            )

        if not failed_with_source:
            return VerificationResult(
                name=self.name,
                ok=False,
                summary="Project contract verifier did not clearly reject a missing scene node.",
                details=result.details,
            )

        return VerificationResult(
            name=self.name,
            ok=True,
            summary="Project contract verifier rejects a missing required node and reports its scene path.",
        )
