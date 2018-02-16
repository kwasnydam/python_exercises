import random

'''
SUMMARY
=======

Przedstawia uzycie setow
'''

def arrival1(n=8: int):
    ''' Zwraca losowa wartosc calkowita z przedzialu 0-n

    sluzy do modelowania przybycia klienta

    :param n: Gorna granica zbioru liczb do losowania
    :returns: Wygenerowana losowa liczba z przedzialu 0-n
    '''
    while True:
        yield random.randrange(n)

def samples(limit, generator):
    for n, val in enumerate(generator)
