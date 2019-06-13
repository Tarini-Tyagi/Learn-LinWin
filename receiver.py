#!/usr/bin/python2

# THIS PROGRAM IS FOR THE CLIENT USER!

import socket
import sys

# AF_INET refers to addresss family of ipv4   and SOCK-DGRAM refers to UTP protocol
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)


# set IP address as of server
ip = "49.15.187.117"
# SET port number as per your choice.
port = 8888
TIMEOUT = 100

s.settimeout(TIMEOUT)



while 4>2:
		message = input("Client : ")
		# using sendto function we are sending message to the server.
		s.sendto(message,(ip,port))
	    # ip and port of server ecvform function client are reciverd with
	    # using recvform function we are receiving message from the client
		t= s.recvfrom(1000)
		print("Receive from Server: " +t[0])
		user = input("Do you want to quit : Y/N")
		#   If user type(Y) then exit with connection from the user.
		if user == 'Y' :
			s.sendto("Client has Quit : Please exit",(ip,port))
			exit()

