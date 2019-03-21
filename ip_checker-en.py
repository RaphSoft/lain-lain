import os 
import socket, sys 

os.system("figlet IP CHECKER") 
host = raw_input ("Enter you host:") 
try:
     ip = socket.gethostbyname(host) 
     print "IP address from %s is %s"%(ip, host) 
except socket.gaierror: 
     print "Sorry no internet connection" 