#!/usr/bin/env python3
from treesModule import *
# Let's try the myTreeNode class:
# building a simple tree
n1 =myTreeNode('root node')
n2 =myTreeNode('left child node')
n3 =myTreeNode('rioght child node')
n4 =myTreeNode('left grandchild node')
n1.left_child = n2
n1.right_child = n3
n2.left_child = n4

# traversing left sub-tree:
current = n1
while current:
    print(current.data)
    current = current.left_child
# Omedetou Damian san, kono codu wa ii desu

# Now, let's test the BST Implementation
# 1. insert
testBST = myBST()
testBST.insert(5)
testBST.insert(3)
testBST.insert(7)
testBST.insert(1)
testBST.insert(2)
testBST.insert(11)
print('max value = {max}'.format(max = testBST.find_max()))
print('min value = {min}'.format(min = testBST.find_min()))
# mou ichi dou, Omedetou gozaimasu!

# 2. search
print(testBST.search(1))
print(testBST.search(123))
