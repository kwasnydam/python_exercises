#!/usr/bin/env python3

from hashingTablesModule import *

# myHash function test
print('myHash function test')
for item in ('hello world', 'world hello', 'gello xorld'):
    print('{string}: {key}'.format(string = item, key = myHash(item)))
