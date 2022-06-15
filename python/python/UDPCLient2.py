import socket
import sys
import os
os.system("color 2")

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


while(True):

	server_address = ('localhost', 600)

	message = input("Please enter a expression or hit Q to quit program>>>")

	if(message.lower() == "q"):

		exit()


	try:

		sent = sock.sendto(message.encode(), server_address)

		print('waiting to receive data from sever...')

		data, server = sock.recvfrom(4096)

		print("The answer is "+data.decode())

		input("Please hit enter to continue>>>")

		os.system("cls") 

	except Exception as e:

		print(e)
