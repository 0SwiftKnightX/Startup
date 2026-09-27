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
            '[node name="PlayerBody" parent="." instance=ExtResource("6_body")]',
            '[node name="XRCamera3D" type="XRCamera3D" parent="."]',
            '[node name="LeftController" type="XRController3D" parent="."]',
            '[node name="RightController" type="XRController3D" parent="."]',
            '[node name="MovementDirect" parent="LeftController" instance=ExtResource("7_direct")]',
            '[node name="MovementTurn" parent="RightController" instance=ExtResource("8_turn")]',
            '[node name="MovementJog" parent="." instance=ExtResource("9_jog")]',
            'res://addons/godot-xr-tools/functions/movement_jog.tscn',
            '[node name="Pointer" parent="LeftController" instance=ExtResource("3_pointer")]',
            '[node name="Pointer" parent="RightController" instance=ExtResource("3_pointer")]',
            "distance = 8.0",
            "laser_length = 1",
            "show_target = true",
            'tracker = &"left_hand"',
            'tracker = &"right_hand"',
            'pickup_axis_action = "grip"',
            'action_button_action = "trigger_click"',
            'ranged_enable = true',
            'ranged_distance = 5.0',
            'res://addons/godot-xr-tools/xr/start_xr.tscn',
            "ground_control = 0",
            'res://scripts/comfort_locomotion.gd',
        ]
        for contract in contracts:
            if not self.require_text(repo_root, "scenes/xr_player.tscn", contract, self.name, details):
                ok = False

        rig_scene = (repo_root / "scenes" / "xr_player.tscn").read_text(encoding="utf-8")
        right_pickup_block = rig_scene.split('[node name="Pickup" parent="RightController"', 1)[-1].split("\n\n", 1)[0]
        if 'pickup_axis_action = "grip"' not in right_pickup_block:
            details.append("scenes/xr_player.tscn:RightController/Pickup requires XR action 'grip'.")
            ok = False
        if 'action_button_action = "trigger_click"' not in right_pickup_block:
            details.append("scenes/xr_player.tscn:RightController/Pickup requires XR action 'trigger_click'.")
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
            "openxr/enabled=true",
            'openxr/default_action_map="res://openxr_action_map.tres"',
            "shaders/enabled=true",
            'renderer/rendering_method="mobile"',
        ]:
            if not self.require_text(repo_root, "project.godot", contract, self.name, details):
                ok = False

        for action in [
            'resource_name = "trigger"',
            'resource_name = "trigger_click"',
            'resource_name = "grip"',
            'resource_name = "primary"',
            'resource_name = "ax_button"',
            'resource_name = "by_button"',
            'resource_name = "haptic"',
            'interaction_profile_path = "/interaction_profiles/oculus/touch_controller"',
        ]:
            if not self.require_text(repo_root, "openxr_action_map.tres", action, self.name, details):
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

        for contract in [
            "$PlayerRig/MovementJog.enabled = enabled",
            "XRToolsUserSettings.snap_turning = not enabled",
        ]:
            if not self.require_text(repo_root, "scripts/main.gd", contract, self.name, details):
                ok = False

        summary = "Canonical XR origin, controllers, pickup functions, and action names are wired." if ok else "XR player verification failed."
        return VerificationResult(name=self.name, ok=ok, summary=summary, details=details)
