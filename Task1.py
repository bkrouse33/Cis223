# Alejandro Castillo, Mitchell Kimball, Brian Krouse

class Stack:

    def __init__(self,maxsize):
        self.items = []				#This creates an array for our items to be stored in later when using the push and pop function
        self.maxsize = maxsize		#maxsize that is passed as a parameter when initialized.		
        self.tos = -1				#Top of stack acts as a pointer to show if its full or empty  

    def isEmpty(self):
        if self.tos == -1:			#Checks if tos is -1 if so then this means that is empty
            return True				#Will return true if -1 
        else:
            return False			#will return fals if is not empty 

    def isFull(self):
        if len(self.items) == self.maxsize:			#looks at the length of the array items and sees if its the same as maxsize or not if so then is full returns true 
            return True								
        else:
            return False

    def push(self,item):							
        if len(self.items) != self.maxsize:			#First checks if its full or not 
            self.items.append(item)					#if is not full then uses append to add item to end of items 
            self.tos = self.tos + 1 				#adds 1 to tos for the isempty or isfull checks to work 

    def pop(self):									
        if len(self.items) != 0:					# first checks 	if is empty 
            self.tos = self.tos - 1					# if it is empty then subtracts 1 from tos
            return self.items.pop() 				# uses the pop function to return the item at top of the list 
    
    def peek(self):
        return self.items[len(self.items)-1]

    def getSize(self):
        return len(self.items)


class Queue:

	def __init__(self,maxsize):
		self.maxsize = maxsize
		self.stack1 = Stack(maxsize)
		self.stack2 = Stack(maxsize)

	def Enqueue(self,key):
		if len(self.stack1.items) != self.maxsize:
			self.stack1.push(key)

	def Dequeue(self):
		if self.stack1.tos != -1:

			for i in range(self.maxsize):
				self.stack2.push(self.stack1.pop())
			temp = self.stack2.pop()

			for i in range(self.maxsize):
				self.stack1.push(self.stack2.pop())
			return temp
	def isfull(self):
		if len(self.stack1.items) == self.maxsize:
			return True
		else:
			return False
	
	def isEmpty(self):
		if self.stack1.tos == -1:
			return True
		else:
			return False


			
			
#------------------------------------#
# Driver test code			
Q = Queue(5)
if Q.isEmpty():
	print("is empty")
else:
	print("is not empty")

Q.Enqueue(1)
if Q.isEmpty():
	print("is empty")
else:
	print("is not empty")

Q.Enqueue(2)
Q.Enqueue(3)
Q.Enqueue(4)
if Q.isfull():
	print("is full")
else:
	print("is not full")
Q.Enqueue(5)

if Q.isfull():
	print("is full")
else:
	print("is not full")


print("-------------")
print("DEQ")
for i in range(5):
	print(Q.Dequeue())
#---------------



S = Stack(4)
print("#########")
if S.isEmpty():
	print("is empty")
else:
	print("is not empty")

S.push(6)

if S.isEmpty():
	print("is empty")
else:
	print("is not empty")

S.push(7)
S.push(8)
if S.isFull():
	print("is full")
else:
	print("is not full")
S.push(9)

if S.isFull():
	print("is full")
else:
	print("is not full")
print("----------------------")
print("Using the peek function")
print(S.peek())

print("----------------------")
print("Using the pop function")
for i in range(4):
	print(S.pop())



