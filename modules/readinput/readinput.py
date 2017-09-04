#!/usr/bin/env python
#-*- coding:utf-8 -*-

import json
def ReadInput (path):
	data = []
	extension = path.split(".")[1]
	try:
		if extension == "json":
			with open(path) as json_data:
				data =json.loads(json_data.read())
			return data
		if extension == "txt":
			with open(path) as f:
				lines = f.readlines() 
				for line in lines:
					data.append(line.rstrip('\n'))
				f.close()
			return data
		if extension != "json" and extension != "txt":
			print "Output incorrect"
			exit(1)
	except Exception as e:
		print e
