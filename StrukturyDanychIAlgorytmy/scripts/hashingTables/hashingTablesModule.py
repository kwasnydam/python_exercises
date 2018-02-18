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
    def __init__(self):
        self.size = 256       #maximum number of slots
        self.slots = [None for i in range(self.size)]   #stores elements in list
        self.count = 0        #used number of slots

    def _hash(self, key):
        return myHash(key) % self.size

    def put(self, key, value):
        item = myHashItem(key, value)
        h = _hash(key)
        while self.slots[h] is not None:
            if self.slots[h].key is key:
                break
            else:
                h = (h+1)%self.size
        if self.slots[h] is None:
            self.count += 1
        self.slots[h] = item
