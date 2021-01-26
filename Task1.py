

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

    def pop(self):
        if len(self.items) != 0:
            return self.items.pop()
    
    def peek(self):
        return self.items[len(self.items)-1]

    def getSize(self):
        return len(self.items)



class Queue:

    def __init__(self,maxsize):
        self.maxsize = maxsize
        self.stack1 = Stack(maxsize)
        self.stack2 = Stack(maxsize)

    def Enqueue(self,key):      # this is where we will have to loop through and transfer to one stack from anoither 
        #First we much check of this queue is full or empty or if first element 
        if self.Rear != self.maxsize:
            if self.Front == -1 and self.Rear == -1:    #First element is going to be added to queue
                self.queue.append()
                self.Front = 0
                self.Rear = 0
            else:
                self.queue.append()
                self.Front =+ 1
        else:
            return "is full"


    def Dequeue(self):
        if self.Front==-1 and self.Rear == -1:
            return "Is Empty"


    def isFull(self):
        if self.Rear == self.maxsize:
            return True 
        else:
            return False

    def isEmpty(self):
        if self.Front==-1 and self.Rear == -1:
            return True
        else:
            return False

    





S = Stack(5)
S.push(1)
S.push(12)
S.push(6)
S.push(17)
S.push(100)


#for i in range(5):
 #   print(S.pop())