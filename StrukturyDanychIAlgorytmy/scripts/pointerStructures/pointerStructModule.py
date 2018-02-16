#!/usr/bin/env python3


class myNode:
    '''Class Implementing the node abstraction'''
    def __init__(self, data = None):
        self.data = data
        self.next = None
    def __str__(self):
        return str(self.data)

# Intruducing single linked list:
class mySinglyLinkedList:
    ''' Implementing simple singlyLinkedList data structure '''
    def __init__(self):
        self.tail = None
    def append(self, data):
        node = myNode(data)     #creating node objects
        if self.tail == None:   #if list is empty, it becomers the first node
            self.tail = node
        else:                   #else
            current = self.tail
            while current.next:
                current = current.next  #Traversing the list
            current.next = node         #adding the new node to the last position

#Problem with the design: adding element needs traversing n elements, thus O(n)

class myImprovedSinglyLinkedList:
    ''' head property for O(1) append and count property for O(1) size count
    '''
    def __init__(self):
        self.tail = None
        self.head = None
        self.count = 0
    def append(self, data):
        self.count += 1
        node = myNode(data)         #creating node objects
        if self.head:               #if there is a head
            self.head.next = node   #append the node as the next item
            self.head = node        #this is the new head (but the previous one has address to it)
        else:                       #else(i.e. the list is empty)
            self.tail = node
            self.head = node
    def iter(self):
        ''' generator that yields data contained in the list's nodes.
        User can ignore the inner representation of data in the list '''
        current = self.tail
        while current:
            yield current.data
            current = current.next

    def delete(self, data):
        '''deletes 'data' object from the list
        Takes advantage of the fact that the data is actually a reference
        to the data thus node.data == data is possible, and when that happens
        we just cut reference to the desired object, eliminating it from the
        chain
        '''
        if self.tail.data == data:
            self.tail = self.tail.next
            return
        current = self.tail
        while current.next:

            if current.next.data == data:
                self.count -= 1
                if current.next is not self.head:
                    current.next = current.next.next
                else:
                    current.next = None
                return
            current = current.next
    def clear(self):
        '''
        Deleting tail and head nodes effectively clears the list
        '''
        self.tail = None
        self.head = None

    def find(self, data):
        content = self.iter()
        for item in content:
            if item == data:
                return True
        return False

class myDoubleNode(myNode):
    def __init__(self, data = None, next = None, previous = None):
        myNode.__init__(self, data)
        self.previous = previous

class myDoubleLinkedList(myImprovedSinglyLinkedList):
    ''' Trying out the inheritance mechanism in Python'''
    def __init__(self):
        super(myDoubleLinkedList, self).__init__()
    def append(self, data):
        self.count += 1
        node = myDoubleNode(data)         #creating node objects
        if self.head:               #if there is a head
            node.previous=self.head #new node's prev points to the prev last
            self.head.next = node   #current last's next points to new last
            self.head = node        #this is the new head (but the previous one has address to it)
        else:                       #else(i.e. the list is empty)
            self.tail = node
            self.head = node

    def delete(self, data):
        '''4 scenarios:
        1. there is no item to deletes
        2. first item (tail) is to be deleted
        3. last item (head) is to be deleted
        4. item to be deleted is inside the list
        '''
        deletion_succesful = False
        if self.tail.data == data:  #2.
            self.tail = self.tail.next
            self.tail.previous = None
            self.count -= 1
            deletion_succesful = True
            return deletion_succesful
        elif self.head.data == data:
            self.head.previous.next = None
            self.head.previous = None
            self.count -= 1
            deletion_succesful = True
            return deletion_succesful
        else:
            current = self.tail
            while current.next:
                if current.data == data:
                    current.previous.next = current.next
                    current.next.previous = current.previous
                    self.count -= 1
                    deletion_succesful = True
                    return deletion_succesful
                current = current.next
        return deletion_succesful
