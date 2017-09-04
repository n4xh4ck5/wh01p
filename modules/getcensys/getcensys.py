#!/usr/bin/env python
#-*- coding:utf-8 -*-

import json 
import requests

#API values
UID="UID"
SECRET="SECRET"
url ="https://www.censys.io/api/v1"
def GetCensys(ip):

	target={'query':ip, 'flatten':True}

	try:
		response = requests.post(url + "/search/ipv4", json = target, auth =(UID,SECRET))
		if response.status_code != 200:
			print "Error to connect with Censys API", response.status_code
	except Exception as e:
		print e

	data = response.json()
	for i in data['results']:
		print "\n\t-Direction IP:" + i['ip']
		print "\n\t-Country:" + i['location.country']
		protocols = i["protocols"]
		for k in protocols:
			print "\n\t -Port: " + k.split("/")[0] + " Protocol:" + k.split("/")[1]
