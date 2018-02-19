#!/usr/bin/env python3
'''
Hashing - representing an object with unique integer identifier. In this example,
the discussion will be limited to string. So, we want to represent each string
with a unique 'key'.
'''
def myHash(string):
    multiplier = 1
    hashValue = 0
    for char in string:
        hashValue += multiplier * ord(char) #ord returns a unicode of character
        multiplier += 1
    return hashValue

class myHashItem:
    def __init__(self, key, value):
        self.key = key
        self.value = value

class myHashTable:
    '''
    Hashtable is used when we know what we are searching for (i.e. known key).
    We can use this key as an index, and immediately return a value. Problem
    arises when the hastable count approaches its size, because it slows down
    both get and put operations
    '''
    def __init__(self):
        self.size = 256       #maximum number of slots
        self.slots = [None for i in range(self.size)]   #stores elements in list
        self.count = 0        #used number of slots

    def _hash(self, key):
        return myHash(key) % self.size

    def put(self, key, value):
        item = myHashItem(key, value)
        h = self._hash(key)                  #calculating the hash of they key
        while self.slots[h] is not None:#if slot with index h is not empty
            if self.slots[h].key is key:#if it is the same as they key, do nothin
                break
            else:
                h = (h+1)%self.size     #else, check next hash index
        if self.slots[h] is None:       #if slot with hash index h is free/empty
            self.count += 1             #increment count of table
        self.slots[h] = item            #Put an item at thios hash index

    def get(self, key):
        '''
        To get the value associated with the key 'key' we peroform opposite
        of put procedure
        '''
        h = self._hash(key)                  #again, get the hash of the key
        while self.slots[h] is not None:#check table element at ind h
            if self.slots[h].key is key:#if they keys match, return value
                return self.slots[h].value
            else:
                h = (h+1)%self.size     #else, check next index
    def __setitem__(self, key, value):
        self.put(key, value)
    def __getitem__(self, key):
        self.get(key)
