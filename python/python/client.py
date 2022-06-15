#TCP 

import socket

import os

os.system("color 2")


Host = "127.0.0.1"

portNumber = 2000

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM); 

sock.connect((Host,portNumber))

while True:
    
    try:

    	UserInput = str(input("Please enter a expression or hit Q to exit >>>"))


    	if(UserInput.lower() == "q"):

    		sock.close()

    		exit()

    	sock.sendall(UserInput.encode())

    	print(str(sock.recv(1024)).replace("b'"," ").replace("'"," "))

    	input("Hit enter to continue>>>")

    	os.system("cls")

    except Exception as e:

    	print(e)


sock.close()	

  
