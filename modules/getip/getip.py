#!/usr/bin/env python
#-*- coding:utf-8 -*-

import socket
import requests

def GetIP(target):
	timeout = 8
	ip=""
	valid_responses = ['200', '401', '403', '404', '301', '302']

	try:

		if str(requests.get('http://' + target,timeout = timeout).status_code)  not in valid_responses:

			if str(requests.get('https://' + target, timeout= timeout).status_code) in valid_responses:

				ip = socket.getbyhostname(target)

			else:

				domain_ip = '0.0.0.0'
				print "The target is not up"
				exit(0)

		else:

			ip = socket.gethostbyname(target)	

	except Exception as e:
		print e
		pass

	return ip
