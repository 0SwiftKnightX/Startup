extends XROrigin3D

signal runtime_status_changed(status: String)

var runtime_status := "desktop_fallback"

@onready var camera: XRCamera3D = $XRCamera3D

func _ready() -> void:
	# Godot 4.7 recommends VRS_XR for Mobile/Forward+ XR renderers.
	# If the device does not support VRS, Godot ignores this setting.
	get_viewport().vrs_mode = Viewport.VRS_XR

	var openxr := XRServer.find_interface("OpenXR") as OpenXRInterface
	if openxr and openxr.is_initialized():
		runtime_status = "xr_active"
	else:
		runtime_status = "desktop_fallback"
		# Keep the fallback camera at a usable eye height without affecting
		# the physical XR camera, whose pose is supplied by OpenXR.
		camera.position = Vector3(0.0, 1.6, 0.0)
	runtime_status_changed.emit(runtime_status)
	print("XR player status: ", runtime_status)
