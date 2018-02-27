'''
@author: Damian Kwaśny
decorators used to alter the functionality of functions (xD)
Where and why use fnction decorators?:
1. logging -> keeping track of how many times a fucntion was called
and what arguments it received
2. timing how long a function runs
'''
from functools import wraps
#above lib is needed to preserve the info about the function we are decorating
#like its documentation

#Clousures
def outer_function():
    message = 'Hi'
    def inner_function():
        print(message)
    return inner_function()

#decorators
def decorator_function(original_function):
    ''' Using decorator we can enhance the functionality without changing
    anything inside the actual fucntion we are decorating
    '''

    @wraps#u use it to preserve the info about the original_function
    def wrapper_function(*args, **kwargs):
        print('wrapper run function: {}'.format(original_function.__name__))
        return original_function(*args, **kwargs)   #multi argument
    return wrapper_function

@decorator_function
def display():
    '''everytime we use display we actually use wrapper_function thus extenbding
    functionality of this function
    it's equal to: display = decorator_function(disply) -> EQUAL
    '''
    print('display()')

@decorator_function
def display_info(name, age):
    print('display_info: {} {}'. format(name, age))

decorated_display = decorator_function(display) #it has a wrapper_function ready to be executed
decorated_display() # Executes wrapper so in fact executes the original_function, display
display()           #The same output thanks to @decorator_function

display_info('damian', 22)

"""
#class decorators
#this is just another syntax
class decorator_class(object):
    #decorator class instead of decorator function
    def __init__(self, original_function):
        self.original_function = original_function

    def __call__(self, *args, **kwargs):
        #it raplaces wrapper function
        print('call method executed this before {}'. format(\
                self.original_function.__name__))
        return self.original_function(*args, **kwargs)

@decorator_class
def display_info(name, age):
    print('display_info: {} {}'. format(name, age))

display_info('damian', 22)
"""
