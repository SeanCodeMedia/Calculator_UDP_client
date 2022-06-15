
import os
import socket
import operator  as o
import stack as StackClass

portNumber = 7000

IP = "127.0.0.1"

Data = False

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.bind((IP, portNumber))

print("socket was created ")

def get_operator ( Math_operator):

	return  {
    '+' : o.add,
    '-' : o.sub,
    '*' : o.mul,
    '/' : o.truediv,
    }[Math_operator]


def calculate ():
	if(operator.Size() == 1 and operand.Size() == 2):


		try:

			Number1 = int(operand.pop()); 

			Number2 = int(operand.pop()); 


			op = operator.pop()

			result = get_operator(op)(Number1,Number2)

			operand.push(result)

	
		except Exception as e:
        	
        	 print(e);

		






	
try:

	if(Data == True):

		sock.sendto(str(operand.printStack()[0]).encode(),addr)

		Data = False

		input()

	while True:

			userTuple,d = sock.recvfrom(1024)

			UserInput = str(userTuple).replace("b","").replace("'","");

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

					print(operand.printStack()[0])

					addr = (IP, portNumber)


					data = True
                    
					
					#input()
             
except Exception as e:
	print(e)



#while True:
#	data, addr = sock.recvfrom(1024)
	#print("received message:", data)

