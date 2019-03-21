import os
import socket, sys 

os.system("figlet IP CHECKER")
host = raw_input ("Masukan host:")
try:
        ip =  socket.gethostbyname(host) 
        print "IP address dari %s adalah %s"%(ip, host)
except socket.gaierror: 
        print "Maaf tidak ada koneksi"
    
