extends CanvasLayer


func _on_Button_pressed():
	$HTTPRequest.request('http://127.0.0.1:5000/simulation')


func _on_HTTPRequest_request_completed(result, response_code, headers, body):
	var json = JSON.parse(body.get_string_from_utf8())
	print(json.result) # Replace with function body.
