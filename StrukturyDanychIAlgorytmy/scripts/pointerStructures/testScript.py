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
from pointerStructModule import *
# Intruducing some variables
str1, str2, str3 = 'jajka', 'szynka', 'spam'

# Creating a chain of nodes: a single linked list:
n1, n2, n3 = myNode(str1), myNode(str2), myNode(str3)
n1.next = n2
n2.next = n3

# Traversing a chain od nodes:
current = n1
while current:
    print(current)
    current=current.next

# Testing singlyLinkedList:

words = mySinglyLinkedList()
words.append(str1)
words.append(str2)
words.append(str3)

current = words.tail
while current:
    print(current)
    current = current.next
# It works, but still requires too much effort

# Testing myImprovedSinglyLinkedList:
words = myImprovedSinglyLinkedList()
words.append(str1)
words.append(str2)
words.append(str3)

current = words.tail
while current:
    print(current)
    current = current.next

# testing generator utility (can we get rid of nodes already?)
print([item for item in words.iter()]) #-> YAY, it actually works xD

# testing delete method
words.delete(str3)
print([item for item in words.iter()]) #-> YAY, it actually works as well xD

# testing find method:
print(words.find(str1))

# testing count method:
print(words.count)

# testing myDoubleLinkedList:
words2 = myDoubleLinkedList()
words2.append(str1)
words2.append(str2)
words2.append(str3)
print([item for item in words2.iter()]) #Kore wa ii desu! Subarashii, desune?

# testing myDoubleLinkedList delete method:
print(words2.delete(str3))
print([item for item in words2.iter()]) #Kore wa ii desu! Subarashii, desune?
#KORE WA MO II DESU!
