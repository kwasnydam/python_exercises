import random
from fractions import Fraction
from statistics import mean
"""
SUMMARY
=======

Przedstawia uzycie setow
"""

def arrival1(n=8):
    """ Zwraca losowa wartosc calkowita z przedzialu 0-n

    sluzy do modelowania przybycia klienta

    :param n: Gorna granica zbioru liczb do losowania
    :returns: Wygenerowana losowa liczba z przedzialu 0-n
    """
    while True:
        yield random.randrange(n)

def samples(limit, generator):
    for n, val in enumerate(generator):
        if n == limit: break
        yield val

random.seed(1)
testSequence = list(samples(100000, arrival1()))  #Test sequence
#for sample in testSequence: print(sample)
def expected(n=8):
    return n*sum(Fraction(1, i+1) for i in range(n))
#print(float(expected())) #21.74 ~= 22 klientow zanim przyjdzie kazdy z nich
def coupon_collector(n, data):
    counter, collection = 0, set()
    for item in data:
        counter+=1
        collection.add(item)    #W secie (zbiorze) dana wartosc moze wystepowac
        #Tylko raz, dodanie drugi raz tego samego obiektu nic nie robi
        if len(collection)==n:
            yield counter
            counter, collection = 0, set()

expectedTime = float(expected())
waitTimes = list(coupon_collector(8, testSequence))
print(mean(waitTimes))
