'''
static methods can be used without an instance of the class (like c++)

static members are shared between instances of the class (like c++)
'''
class Sum:

    @staticmethod
    def getSum(*args):
        sum = 0
        print('jestem w {}'.format(Sum.__name__))
        for i in args:
            sum += i

        return sum

class Dog:
    nr_of_dogs = 0
    def __init__(self, race):
        self.race = race
        Dog.nr_of_dogs += 1

def main():
    print('Sum = {}'.format(Sum.getSum(1,2,3,4)))
    print('Before a dog appears there are: {}'.format(Dog.nr_of_dogs))
    dog1 = Dog('Biszon')
    print('After a dog appeared there are: {}'.format(Dog.nr_of_dogs))

main()
