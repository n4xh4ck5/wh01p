import socket
def GetIP(target):
	ip=""
	try:
		ip = socket.gethostbyname(target)
	except Exception as e:
		print e
		print "It can't obtain the reverse IP"
		ip = "0.0.0.0"
		exit (0)
	return ip
