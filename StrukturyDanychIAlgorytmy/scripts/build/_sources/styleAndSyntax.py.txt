#!/usr/bin/env python3
#Documentation string:
"""
SUMMARY
=====

Plik zawiera wskazowki na temat stylu pisania w Pythonie

DESCRIPTION
===========

::
    First Paragraph

::
    Second Paragraph
"""
import math
example_value = (63/25)*(17+15*math.sqrt(5))/(7+15*math.sqrt(5))
mantissa_fraction, exponent = math.frexp(example_value)
mantissa_whole =int(mantissa_fraction*2**53)

''' Ponizsze wyraznie jest w chuj dlugie i chcemy je skrocic
 mozemy to zrobic zamykajac cale wyrazenie w () albo uzywac \ na koncu linii\
 zeby stala sie bardziej czytalena '''
messege_text1 = 'the internal representation is{mantissa:d}/2**53*2**{exponent:d}'.format(mantissa=mantissa_whole,exponent=exponent)
print(messege_text1)

'''Mozemy rozbic to w nastepujacy sposob, korzystajac z () i backslasha,
wynik jest taki sam, a przyjemniej sie czyta'''
messege_text2 = ( 'the internal representation is\
{mantissa:d}/2**53*2**{exponent:d}'.\
format(mantissa=mantissa_whole,exponent=exponent) )
print(messege_text2)
