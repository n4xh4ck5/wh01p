#!/usr/bin/env python
import os

def GetWhois(target):
	try:
		whois = os.system("whois "+target+"> whois.txt")
		with open('whois.txt','r+') as f:
			lines = f.readlines()
			for line in lines:
				if '%' not in line:
					if line != '\n':
						print "\n\t-" +line
			f.close()
	except Exception as e:
		print e