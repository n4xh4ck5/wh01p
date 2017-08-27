import json
def ReadInput (path):
	try:
		with open(path) as json_data:
			data =json.loads(json_data.read())
		return data
	except Exception as e:
		print e