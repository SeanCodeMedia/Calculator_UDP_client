import socket
import sys
import operator  as o
import stack as StackClass
# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the port
server_address = ('localhost', 600)
print('starting up on {} port {}'.format(*server_address))
sock.bind(server_address)


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


while True:
    print('\nwaiting to receive message')
    data, address = sock.recvfrom(4096)

    print('received {} bytes from {}'.format(
        len(data), address))


    UserInput = str(data.decode("utf-8"))

    operand =  StackClass.stack()

    operator = StackClass.stack()

    temp = ""

    count = 0


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

    if data:
        sent = sock.sendto(str(operand.printStack()[0]).encode(), address)
        print('sent {} bytes back to {}'.format(
            sent, address))