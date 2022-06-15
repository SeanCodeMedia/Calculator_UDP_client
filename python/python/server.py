
#TCP 

import os
import socket
import operator  as o
import stack as StackClass
os.system("color 2")

Sock = socket.socket()

UserInput = None

print("socket was created ")

portNumber = 2000

Sock.bind(('127.0.0.1', portNumber))

Sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

Sock.listen(2)

def get_operator ( Math_operator):

	return  {
    '+' : o.add,
    '-' : o.sub,
    '*' : o.mul,
    '/' : o.truediv,
    }[Math_operator]


def calculate ():
	if(operator.Size() == 1 and operand.Size() == 2):


		Number1 = int(operand.pop()); 

		Number2 = int(operand.pop()); 

		op = operator.pop()


		result = get_operator(op)(Number1,Number2)

		operand.push(result)






	
try:


	connection, address = Sock.accept() 
	print("Address "+ str(address) +"has connected to server")

	while True:

		UserInput = str(connection.recv(1024).decode("utf-8"))

		operand =  StackClass.stack()

		operator = StackClass.stack()

		temp = ""

		count = 0; 


		for x in range(0,len(UserInput)):

			count += 1

			if(UserInput[x] == "+" or UserInput[x] == "-"  or UserInput[x] == "*" or UserInput[x] == "/"):

				operand.push(temp)
				temp = ""
				calculate()
				operator.push(UserInput[x])



			else:

				temp += UserInput[x].strip();




			if(count == len(UserInput)):

				operand.push(temp)

				calculate()

				#print(operand.printStack())

				connection.sendall(str(operand.printStack()[0]).encode())



	
except Exception as e:
	print(e)


connection.close()








