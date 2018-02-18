#!/usr/bin/env python3
'''
Tree is a hierarchical data structure with parent-child type of relationship
between items. A picture of a tree is added as an example.
Terminology:
node - holds the data
root node - The only node from which all other nodes come
sub-tree - it's nodes originate from some other tree
degree - number of subtrees for a given node
leaf node (liść)- node from which nothing comes, 0 degree
edge (krawędź) - connection between two nodes
parent (rodzic) - node from which other nodes originate
child - connected to a parrent, originate from parent
sibling - node that originates from the same parent
level - number of connections from the root node
height - number of levels
depth - number of edges from the root node to that node
binary tree - each node has maximum of two children
binary search tree (BST) - binary tree where for a given node with a value,
all the nodes in the left subtree have values lower or equal
'''

class myTreeNode:
    ''' node of a binary tree '''
    def __init__(self, data):
        self.data = data
        self.right_child = None
        self.left_child = None

class myBST:
    ''' Implementation of a binary search tree. A binary search tree
    is extremely useful when it comes to searching for a known value, since
    it only requires O(h) operation, where h = log2(n) is a tree height
    '''
    def __init__(self):
        self.root_node = None
    def find_min(self):
        ''' We just have to traverse the left subtree to the leaf '''
        current = self.root_node
        while current.left_child:
            print(current.data)
            current = current.left_child
        return current.data
    def find_max(self):
        current = self.root_node
        while current.right_child:
            print(current.data)
            current = current.right_child
        return current.data
    def insert(self, data):
        ''' It is an important operation. In order to have a sorted tree, we
        compare the item to be inserted with existing items, trying to find a
        fit
        '''
        node = myTreeNode(data)
        if not self.root_node:
            self.root_node = node
        else:
            current = self.root_node
            while current:
                if node.data <= current.data:
                    if current.left_child:
                        current = current.left_child
                    else:
                        current.left_child = node
                        return
                else:
                    if current.right_child:
                        current = current.right_child
                    else:
                        current.right_child = node
                        return
    def search(self, data):
        if self.root_node == None: return -1
        current = self.root_node
        while current:
            if current.data == data: return current.data
            elif data < current.data:
                if current.left_child:
                    current = current.left_child
                else:
                    return None
            else:
                if current.right_child:
                    current = current.right_child
                else:
                    return None
    #The delete operation is actually slightly more complicated and for now
    # i wont implement it
