# Tym razem spróbujemy napisać prostą klasę do gry w kości

import random

class Dice:
    #inicjalizacja obiektu klasy odbywa się w metodzie __init__
    def __init__(self):
        self.faces = None   #zmienna 'self' jest referencja na ten obiektu
    def roll(self):         #rzut osci, aktualizuje stan obiektu
        self.faces = (random.randint(1, 6), random.randint(1, 6))
    def total(self):        #zwraca sume wyrzuconych kosci
        return sum(self.faces)
    def hardway(self):
        return self.faces[0] == self.faces[1]
    def easyway(self):
        return self.faces[0] != self.faces[1]
#Python jest typowany dynamicznie i klasy nie maja scislej listy danych jakie
#zawierają, zamiast tego mozemy je inicjalizowac w roznych miejscach (nie tylko
#w konst ale tez w metodach)
random.seed(1)
d1 = Dice()
d1.roll()
print(d1.total())
print([face for face in d1.faces])

'''
Teraz projekt klasy, ktora zawierac bedzie inna klase
'''
from collections import Counter
import math
class CounterStatistics:
    '''
    SUMMARY
    =======
    Rozszerza mozliwosci klasy Counter poprzez zdefiniowanie dla niej operacji
    statystycznych
    '''
    def __init__(self, raw_counter:Counter):
        self.raw_counter = raw_counter
        self.mean = self.compute_mean()
        self.std = self.compute_std()
    def compute_mean(self):
        total, count = 0, 0
        for value, frequency in self.raw_counter.items():
            total += frequency*value
            count += frequency
        return total/count

    def compute_std(self):
        total, count = 0, 0
        for value, frequency in self.raw_counter.items():
            total += frequency*(value-self.mean)**2
            count += frequency
        return math.sqrt(total/(count-1))

'''
Teraz wygenerujemy jakies dane ktore mozemy wykorzystac zeby przetestowac klase
'''

from sety import *
def raw_data(n=8, limit=1000, arrival_fun=arrival1):
    exp_time = float(expected(n))
    data = samples(limit, arrival_fun(n))
    wait_times = Counter(coupon_collector(n, data))
    return wait_times
example_data = raw_data()
stats = CounterStatistics(example_data)

print('Mean: {0:.2f}'.format(stats.mean))
