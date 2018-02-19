#!/usr/bin/env python3

from hashingTablesModule import *

# myHash function test
print('myHash function test')
for item in ('hello world', 'world hello', 'gello xorld'):
    print('{string}: {key}'.format(string = item, key = myHash(item)))

# myHashTable test:
testHashTable = myHashTable()

#1. puting elements:
testHashTable.put('ongaku', '5')
testHashTable.put('anime', '4')
testHashTable.put('hon', '3')
testHashTable.put('ski', '2')
testHashTable.put('tabemono', '1')

#2. getting and printing elements
for key in ('ongaku', 'anime','ski','hon','tabemono'):
    print(testHashTable.get(key)) # 5 4 2 3 1
