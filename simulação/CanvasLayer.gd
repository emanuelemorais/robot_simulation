extends CanvasLayer


func _on_Button_pressed():
	print('oi')
	$HTTPRequest.request('https://catfact.ninja/fact')


func _on_HTTPRequest_request_completed(result, response_code, headers, body):
	var json = JSON.parse(body.get_string_from_utf8())
	print(json.result) # Replace with function body.
