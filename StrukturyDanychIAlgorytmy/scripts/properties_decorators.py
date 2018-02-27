'''
@author: Damian Kwasny

This little file shows the usage of property decorator as a way to achieve a
getter and setter kind of interface. Propety allows us to refere to a public
members of a class as to atrributes but in fact it is itself a method That con
run addidtional code like in C++ for example
'''
class Employee:
    def __init__(self, first='Foo', last='Bar'):
        self.first = first
        self.last = last

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    @property
    def last(self):
        #it acts like a method but is called like na attribute
        return self.last

    @last.setter
    def last(self, last):
        #this one allows use to do instance.last = 'something', but internally
        #is a method
        self.last = last

emp = Employee()

print(emp.first)
print(emp.last)
print(emp.email)        # it runs like this is an attribute
print(emp.fullname())   # wherea this one runs like this is a method
                        # and they do pretty much the same thing
