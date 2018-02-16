'''
Understanding the mechanism of shallow and deep copy in python
'''
# 1. Shallow copy

some_dict = {'a': [1, 1, 2, 3]}
another_dict = some_dict.copy()
print([another_dict]) #Looks the same as some_dict

# Let's make a change to the coped dict's  list

some_dict['a'].append(5)
print([some_dict])
print('id_some_dict["a"] = {first_dict}\nid_another_dict["a"] = {second_dict}'\
.format(first_dict=id (some_dict['a']), second_dict =id (another_dict['a'])))
'''
As you can see, both ids are the same, which means that despite the copy,
both objects points to the same place in the memory.
ids of some_dict and another_dict are in fact different, but the id of mutabl
objects they contain are identical, which means these are the same objects

If we want a deep copy of an mutable object, one which competly disconnects them
we need to try harder -> we use the 'copy' library
'''

# 2. Deep copy
import copy
another_dict = copy.deepcopy(some_dict)  # Deep copy of an object

# Let's perform the same operations and check the results this time around
some_dict['a'].append(50)
print('some_dict[a] = {original_dict}\nanother_dict[a] = {copied_dict}\n\
id_some_dict["a"] = {first_dict}\nid_another_dict["a"] = {second_dict}'\
.format(original_dict = some_dict['a'], copied_dict = another_dict['a'],\
first_dict=id (some_dict['a']), second_dict =id (another_dict['a'])))
'''
This time around the copies were indeed deep, and the results difer, also both
dict's mutable elements now lay in different place in memory
'''
