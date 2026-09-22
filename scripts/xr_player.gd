extends XROrigin3D

signal runtime_status_changed(status: String)

var runtime_status := "desktop_fallback"

func _ready() -> void:
	if XRServer.primary_interface != null:
		runtime_status = "xr_active"
	else:
		runtime_status = "desktop_fallback"
	runtime_status_changed.emit(runtime_status)
	print("XR player status: ", runtime_status)
