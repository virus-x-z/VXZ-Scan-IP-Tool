# ViRuS-X-Z Team
# VXZ-Tools
# VXZ-Gathering-Website-Information-Tool

# imports
import os
import socket
from Functions import *
from time import *
from datetime import *

# Start-script-programming
loading1 ()
loading0 ()
banner3 ()
login ()
print ("Welcom in VXZ-Scan-IP-Tool")
print ("    ")

# V ========== X ========== Z

ip=input ("Enter IP Address ===> ")
print ("Starting scan for "+ip)
sleep(1)

# V ========== X ========== Z

try:
	for port in range(1,6553):
		s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		if(s.connect_ex((ip,port))==0):
			try:
				serv=socket.getservbyport(port)
			except socket.error:
				serv="Unknown Service"
			print ("Port %s Open Service %s"%(port,serv))
	print ("Scanning Completed ...")
except KeyboardInterrupt:
	print ("Good bye ^_^")

# V ========== X ========== Z
# V ========== X ========== Z
# E ========== N ========== D
