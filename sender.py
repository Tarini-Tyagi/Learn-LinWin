#!/usr/bin/python2

# THIS PROGRAM IS FOR THE SERVER! HAVE A LOOK

import socket
import sys

# AF_INET refers to addresss family of ipv4   and SOCK-DGRAM refers to UTP protocol
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

# set IP adress as of server
ip = "49.15.187.117"
port = 8888
TIMEOUT = 100


s.bind((ip, port))
s.settimeout(TIMEOUT)

try:
	while True:
		# receiving the message from user in message variale
		r = s.recvfrom(1000)
		# In line below [r] the r[0] contain the message while the r[1] contains the ip and port!
		print("receive from client : " + r[0])
		# replying to the user
		reply = raw_input('server : ')
		client_address = r[1]
		s.sendto(reply, client_address)
except:
	print("timeout or no server running")