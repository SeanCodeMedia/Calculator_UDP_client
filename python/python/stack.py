

class stack:
	
	def __init__(self):


	 self.top = -1;

	 self.stackArray = [];

      
    	



	 def isEmpty(self):

	 	  if(self.top == -1): 

	 	  	  return True; 

	 	  else: 

	 	  	return False; 


	def Size(self):
		
		return len(self.stackArray)


	def push(self, value):

		self.top =+ 1; 
		
		self.stackArray.append(value); 



	def pop(self):

		 item = self.peek()

		 self.stackArray.pop(0); 

		 return item 


	def peek(self):

		return self.stackArray[self.top -1]


	def printStack(self):

		return self.stackArray;


		 

