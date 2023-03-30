extends KinematicBody2D

var tween = null

func set_XY(pos):
	var target_rotation = (pos - global_position).angle() + PI / 2 #PI/2 = 90 graus de offset
	tween.tween_property(self, "rotation", target_rotation, 1) #tempo de rotação

func set_Z(size):
	var claw = get_node("garra")
	size = clamp(size, 0, 100)
	size = 1.0 + size/100.0
	#claw.scale = Vector2(size, size)
	tween.tween_property(claw, "scale", Vector2(size, size), 1) 


func set_R(degrees):
	var claw = get_node("garra")
	#claw.rotation_degrees = degrees
	tween.tween_property(claw, "rotation_degrees", clamp(degrees, 0, 360), 1) #tempo de rotação

#var json_global = {}

func _on_HTTPRequest_request_completed(result, response_code, headers, body):
	var json = JSON.parse(body.get_string_from_utf8())
	process_response(json.result["x"], json.result["y"], json.result["z"], json.result["r"])
	
func process_response(x, y, z, r):
	print(x)
	print(y)
	print(z)
	print(r)
	
	var target_pos = Vector2(x, y) # posição de destino do braço robótico
	tween = get_tree().create_tween()
	set_XY(target_pos) # move o braço robótico
	set_R(r)
	set_Z(z)
	
func _ready():
	$HTTPRequest.connect("request_completed", self, "on_request_completed")
	$HTTPRequest.request('http://127.0.0.1:5000/simulation')


func _on_Timer_timeout():
	$HTTPRequest.request('http://127.0.0.1:5000/simulation')
	
	
