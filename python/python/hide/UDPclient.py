import socket

import os

os.system("color 2")


Host = "127.0.0.1"

portNumber = 7000

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
addr = (Host, portNumber)


while True:
    
    try:

      UserInput = str(input("Please enter a expression>>>"))

      sock.sendto(UserInput.encode(), addr)
     
      returnTuple = sock.recvfrom(1024)

      print(str(returnTuple[0]).replace("b'"," ").replace("'"," "))

      input("Hit enter to continue>>>")

      os.system("cls")

    except Exception as e:

      print(e)


sock.close()  
