
import os
import socket
import operator  as o
import stack as StackClass
os.system("color 2")



Running = True

#while Running:

UserInput =  "50+50+30/2" #input("Please enter a expression>>>")

operand =  StackClass.stack()

operator = StackClass.stack()

temp = ""

count = 0; 

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

		print(operand.printStack())








