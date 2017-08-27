#!/usr/bin/env python

import socket
import sys

def main(target, port):

    # create a socket object
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # send some data
    client.sendto("AAABBBCCC",(target,port))

    # receive some data
    data, addr = client.recvfrom(4096)

    print data

# ./UDP_Client.py google.com 80
main(sys.argv[1], int(sys.argv[2]))
