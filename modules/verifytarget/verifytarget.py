#!/usr/bin/env python
import re
import socket
def VerifyTarget(target):
	match = True
	#True -> IP
	# False -> Domain
	try:
		try:
		#Verify if target is an IP
			if re.match(r'^((\d{1,2}|1\d{2}|2[0-4]\d|25[0-5])\.){3}(\d{1,2}|1\d{2}|2[0-4]\d|25[0-5])$', target):  
				#Valid IP
				return True
			"""else:
				print "Invalid IP. Please enter an IP or domain"
				exit (0)"""
		except Exception as e:
			print e
			pass
		#elsif-> Verify if the target is a domain
		try:
			match = socket.gethostbyname(target)
			if match == False:
				print "The input is not a correct IP and also hostname. Please, enter a correct value"
				exit (0)
			else:
				#Ok, target is a domain -> return False
				return False
		except Exception as e:
			print e
			pass
	except Exception as e:
		print e
		pass		