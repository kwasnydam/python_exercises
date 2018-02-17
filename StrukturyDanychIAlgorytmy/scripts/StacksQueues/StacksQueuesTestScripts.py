'''
This script test the functionality of stack and queue implemenation
Author: Damian Kwasny
'''

from StackQueueModule import *
# testing stack push&pop functionalities
el1 = 'first value'
el2 = 'second value'
el3 = 'third value'
testList = [el1, el2, el3]
testStack = myStack()
# Push
for el in testList:
    testStack.push(el)
# How big has it gotten?
print(testStack.size)

# Pop
while testStack.size:
    print(testStack.pop())

# testing Queue:
testQueue = myQueue()
for el in testList:
    testQueue.enqueue(el)
# how big is it?
print(testQueue.size)

#let's draw elements from the Queue:
while(testQueue.size):
    print(testQueue.dequeue())
