
#Sending functions as arguments to functions
def mult_2(num):
    return num * 2

def do_math(func, num):
    return func(num)
# PROBLEM 1
# create a function that receives a lista and a function
# The passed function will return True/False if a list element is odd
# The surrounding function will return a list of odd number

def isOdd(num):
    return bool(num%2)

#function annotation for documentation purposes
def listOddFilter(_list: list, _func) -> list:
    '''recevives a list to filter and a function to perform filtering'''
    result = list()
    for num in _list:
        if _func(num):
            result.append(num)
        else:
            pass
    return result

#PROBLEM 2
# Create random list filled with characters H and T 4 heads and tails
# Output the number of Hs and Ts
#   example o: Heads: 54 Tails: 48

def headsAndTails(number):
    head_or_tail = ['H', 'T']
    random_list = list()
    Hs, Ts = 0, 0
    for i in range(number):
        figure = random.choice(head_or_tail)
        random_list.append(figure)
        if figure == 'H':
            Hs += 1
        else:
            Ts += 1
    print([random_list])
    return [Hs,Ts]

# Map function
def howMapsWorks():
    oneTo10 = range(1, 11)
    print(list(map(mult_2, oneTo10)))

    print(list(map(lambda x: x*3, oneTo10)))

    aList = list(map((lambda x, y: x+y), [1, 2, 3], [2, 3, 4]))
    print([aList])


#PROBLEM 3:
# find multiples of 9 in a random list of 100 val range(1, 1000)
def findMultiples():
    #aList = [x]
    aList=list()
    for x in range(100):
        aList.append(random.randrange(1,1000))
    resultList = list(filter((lambda x: x % 9 == 0), aList))
    print(resultList)

def main():
    print(do_math(mult_2, 2))
    list_of_func = [mult_2, do_math]
    print('5 * 9 = {}'. format(list_of_func[0](2))) #list of functions, welp

    odds = listOddFilter(_list=range(10), _func=isOdd)
    print([odds])

    # lambda anonymous functions
    # lamdbas are generally used when you need a one time short functions
    # and t is pointless to unneceserily define them explicitly
    sum = lambda x, y: x + y
    print(sum(2, 3))

    powers = [  lambda x: x ** 2,
                lambda x: x ** 3,
                lambda x: x ** 4]

    for func in powers:
        print(func(4))
    print(headsAndTails(10))
    # as you can see, you can do basically anything with a function in
    # python


    #Maps testing

    howMapsWorks()
    findMultiples()
import random
main()
