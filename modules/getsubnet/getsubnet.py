#!/usr/bin/env python
#-*- coding:utf-8 -*-

import requests
import json

#FUNTION GETSUBNET
def GetSubnet(target):
	url = "https://freeapi.robtex.com/ipquery/"+target
	user_agent = user_agent = {'User-agent': 'Mozilla/5.0'}
	response =""
	try:
		response = requests.get(url,headers=user_agent,allow_redirects=True)
		#Get json
		response = requests.get(url).json()
	except Exception as e:
		print e
	#data =json.loads(response.text)
	print "\n\t-Status:" + response['status']
	print "\n\t-Country:" + response['country']
	print "\n\t-as:" + str(response['as'])
	print "\n\t-router:" + response['routedesc']
	print "\n\t-IP Range:" + response['bgproute']
