

class Stack:

    def __init__(self,maxsize):
        self.items = []
        self.maxsize = maxsize
        self.tos = -1

    def isEmpty(self):
        if self.tos == -1:
            return True
        else:
            return False

    def isFull(self):
        if len(self.items) == self.maxsize:
            return True
        else:
            return False

    def push(self,item):
        if len(self.items) != self.maxsize:
            self.items.append(item)
            self.tos = self.tos + 1 

    def pop(self):
        if len(self.items) != 0:
            self.tos = self.tos - 1
            return self.items.pop() 
    
    def peek(self):
        return self.items[len(self.items)-1]

    def getSize(self):
        return len(self.items)



class Queue:

    def __init__(self,maxsize):
        
        self.maxsize = maxsize
        self.tos = -1 
        self.stack1 = Stack(self.maxsize)
        self.stack2 = Stack(self.maxsize)


    def Enqueue(self,key):
     # this is where we will have to loop through and transfer to one stack from anoither 
        #First we much check of this queue is full or empty or if first element 
        if len(self.stack1.items) != self.maxsize:
            self.stack1.push(key)
            self.tos = self.tos + 1
            #print(self.stack1.peek())


    def Dequeue(self):
        if self.tos != -1:  #this checks if the Queue/ Stack is empty or not 
            for i in range(self.maxsize):
                print(i)
                self.stack2.push(self.stack1.pop())
            self.stack2.pop()
            
    def whatsSize(self):
        return self.maxsize


            
    


Q = Queue(5)

Q.Enqueue(1)
Q.Enqueue(2)
Q.Enqueue(3)
Q.Enqueue(4)

#S = Stack(3)
#S.push(1)
#S.push(2)
#S.push(3)
#p = S.peek()
#print(p)

#print(v)
#print(S.pop)


(Q.Dequeue())

