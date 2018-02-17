'''
Stack (stos) is a LIFO (Last Input First Output) data structure(like
a tower of books, in order to grab the first book you have to remove all the
books above in the first place). Stack is used to perform things like keeping
return adress from the function and passing parameters between functions
There are two main operation performed on stack - pop and push
pop - taking element from the Stack
push - pushing elemnt on top of the stack
'''
from pointerStructModule import myNode, myDoubleNode
#the node is the same as previous, so why dont use it again, deshou?

class myStack:
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, data):
        node = myNode(data)
        if self.top == None:
            self.top = node
        else:
            node.next = self.top
            self.top = node
        self.size += 1

    def pop(self):
        if self.size:
            self.size -= 1
            if self.top.next:
                temp = self.top
                self.top = self.top.next
                return temp
            else:
                temp = self.top
                self.top = None
                return temp

        else: return None
'''
Queue is a FIFO (First Input First Output) data structure. As the name suggest,
it works like a normal queue, which means that the item that came first is the
first to be served.
Queue supports two basic operations: enqueue, which adds an object at the end
of the queue and dequeue, which removes the first item from the list
'''
class myQueue:
    '''
    self.head - poczatek kolejki
    self.tail - koniec kolejki
    '''
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def enqueue(self, data):
        node = myDoubleNode(data)
        if self.head == None:       #when Queue is empty
            self.head = node
            self.tail = node
        else:                           #else, attach object at the end
            self.tail.next = node       #current last next points new last
            node.previous = self.tail   #new last prev points current Last
            self.tail = node            #new is the new last
        self.size += 1

    def dequeue(self):
        if self.head == None:           #if the list is empty
            return -1
        elif self.head == self.tail:    #if it contains one element
            temp = self.head
            self.head = None
            self.tail = None
            self.size -= 1
            return temp
        else:
            temp = self.head
            self.head.next.previous = None
            self.head = self.head.next
            self.size -= 1
            return temp
