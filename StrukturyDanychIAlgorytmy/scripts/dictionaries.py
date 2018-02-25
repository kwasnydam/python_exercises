#!# -*- coding: utf-8 -*-
#!/usr/bin/env python3

'''
DICTIONARY
    Dictionary is an unsorted map of items. It is build based on a hasing table,
which I already pracitced before. It takes pairs of [key, value], uses hash
function on the key and stores value corresponding to key it in a hashtable.
As the dict grows there ay be collisions and the performance will decrease
    Generally, operations such as add or contains takes O(1) operations,
but as the dict gorvs and hashing collisions appears the complexity may raise
to at worst O(n) if all the hashes are identical.
    Deleting items form a dictionary does not resize it. That means That
iterating and copying takes O(m) time where m is the size of the dict

'''
