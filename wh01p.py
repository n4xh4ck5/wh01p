#!/usr/bin/env python
#-*- coding:utf-8 -*-

import requests
#Libraries to export results
from urlparse import urlparse
import optparse
from urllib2 import urlopen
from contextlib import closing
import json
#Parser arguments
import argparse
from argparse import RawTextHelpFormatter
import os
import re
import socket
import sys
#import
from modules.verifytarget import *
from modules.geoip import *
from modules.getwhois import *
from modules.getsubnet import *
from modules.sh4d0m import *
from modules.readinput import *
from modules.getip import *
from modules.getcensys import *

""" FUNCTION BANNER """
def banner():
	print """
	 __          ___      ___  __       
	 \ \        / / |    / _ \/_ |      
	  \ \  /\  / /| |__ | | | || |_ __  
	   \ \/  \/ / | '_ \| | | || | '_ \ 
	    \  /\  /  | | | | |_| || | |_) |
	     \/  \/   |_| |_|\___/ |_| .__/ 
	                             | |    
	                             |_|   
			 """
 	print"\n"
	print """
	** Tool to obtain information about IP or domain: Geolocation, network, whois and opened ports.
    ** Author: Ignacio Brihuega Rodriguez a.k.a N4xh4ck5
    ** DISCLAMER This tool was developed for educational goals. 
    ** The author is not responsible for using to others goals.
    ** A high power, carries a high responsibility!
    ** Version 1.0"""

"""FUNCTION HELP """
def help():
	print  """ \nThis script obtains information about IP or domain: Geolocation, network, whois and open ports.

 			Example of usage: python whoip.py -t apple.com

 			Multiples IP/domain such as a file input: python whoip.py -i <<FILE.json>> """
def main (argv):
	parser = argparse.ArgumentParser(description="Tool to obtain information about IP or domain: Geolocation, network, whois and open ports", formatter_class=RawTextHelpFormatter)
	parser.add_argument('-t','--target', help="The IP which it wants to search",required=False)
	parser.add_argument('-i','--input', help="File which contains the domains or IP to obtain a piece of information in format txt or json",required=False)
	args = parser.parse_args()
	banner()
	help()
	data_input = [] 
	#Enter and validate the input parameters
	### TARGET ###
	target=args.target
	### INPUT ###
	path = args.input
	try:
		if path is not None:
			data_input = readinput.ReadInput(path)
		else:
			data_input.append(target)
		for target in data_input:
			print "\n\t---" + target + "---\n"
			flag = verifytarget.VerifyTarget(target)
			if flag == False:
				#Target is a domain -> obtain the IP
				target = getip.GetIP(target)
			### Get info and subnet
			print "\nInformation about network:\n"
			getsubnet.GetSubnet(target)
			print "\nInformation about GeoLocation:\n"
			geoip.GeoIP(target)
			print "\nInformation about whois\n"
			#call whois
			getwhois.GetWhois(target)
			print "\nInformation about ports opened\n"
			print "\n - Shodan:"
			sh4d0m.CreateShodan(target)
			print "\n - Censys"
			getcensys.GetCensys(target)
	except Exception as e:
		print e
#MAIN
if __name__ == "__main__":
   main(sys.argv[1:])
