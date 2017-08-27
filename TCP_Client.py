#!/usr/bin/env python

import socket
import sys

def main(message, target, port):

    # create a socket object
    client = socket.socket()

    # connect the client
    client.connect((target, port))

    # send some data
    client.send("{}\r\nHost: {}\r\n\r\n".format(message,target))

    # receive some data
    response = client.recv(4096)

    print response

# ./TCP_Client.py [message] [target] [port]
main(sys.argv[1], sys.argv[2], int(sys.argv[3]))
