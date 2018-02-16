
#!/usr/bin/env python3
'''
Further investigation of how Python treats variables (as references)
Implementing single and doubly-linked lists

DESCRIPTION
::
    As established before, Python treats variables as references to the objects
    in memory. Actual cpies of objects are like never performed, unless a
    specified functions are invoked by the programmer

LIST
::
    List is a data structure that consist of nodes. Each node holds the data of
    a certain object (more like a reference to this data) and an additional
    address of next item, previous item and some other convenient adresses
'''
# Intruducing some variables
str1, str2, str3 = 'jajka', 'szynka', 'spam'

# Intruducing new type: node (węzeł) - contains data and link to some other node
class myNode:
    '''Class Implementing the node abstraction'''
    def __init__(self, data = None):
        self.data = data
        self.next = None
    def __str__(self):
        return str(self.data)

# Creating a chain of nodes: a single linked list:
n1, n2, n3 = myNode(str1), myNode(str2), myNode(str3)
n1.next = n2
n2.next = n3

# Traversing a chain od nodes:
current = n1
while current:
    print(current)
    current=current.next

# Intruducing single linked list:
class MySinglyLinkedList:
    def __init__(self):
        self.tail = None
    def append(self, data):
        node = myNode(data)     #creating node objects
        if self.tail == None:   #if list is empty, it becomers the first node
            self.tail = node
        else:                   #else
            current = self.tail
            while current:
                current = current.next  #Traversing the list
            current.next = node #adding the new node to the last position
#Problem with the design: adding element needs traversing n elements, thus O(n)
