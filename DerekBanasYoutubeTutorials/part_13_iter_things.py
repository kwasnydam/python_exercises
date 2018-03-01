class Alphabet:
    ''' custom iterator example '''
    def __init__(self):
        self.letters = 'ABCDEFGHIJKLMNOUPRSTUWZ'
        self.index = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.letters) - 1:
            raise StopIteration
        self.index += 1
        return self.letters[self.index]

# PROBLEM 1:
# Create a class that returns a values from the Fibonaci sequence each time
# next is called

class iterableFibonacci:

    def __init__(self, count):
        self.index = 1
        self.count = count

    def calculateFibonacciNumber(self, num):
        if num <= 0:
            return 0
        if num == 1:
            return 1
        return self.calculateFibonacciNumber(num - 1) + self.calculateFibonacciNumber(num - 2)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= self.count - 1:
            raise StopIteration
        self.index += 1
        return self.calculateFibonacciNumber(self.index)


    def testThis(self):
        for i in range (10):
            print('{}: {}'.format(i, self.calculateFibonacciNumber(i)))

def main():
    #custom iterator class
    alpha = Alphabet()
    for letter in alpha:
        print(letter)

    fibo = iterableFibonacci(10)
    for el in fibo:
        print(el)
#    fibo.testThis()

main()
