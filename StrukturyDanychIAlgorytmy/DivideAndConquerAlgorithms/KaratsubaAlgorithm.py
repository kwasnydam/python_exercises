#!/usr/bin/env python3


def karatsubaProduct(firstValue=111111, secondValue=111111):
    firstValueStr, secondValueStr = firstValue, secondValue
    if type(firstValueStr) is not str:
        firstValueStr = str(firstValueStr)
    if type(secondValueStr) is not str:
        secondValueStr = str(secondValueStr)
    #print('{} {}'.format((len(firstValueStr)), len(secondValueStr)))
    #print(firstValueStr[0:(len(firstValueStr)/2)])
    if (len(firstValueStr) == 1) or (len(secondValueStr)== 1):
        return int(firstValueStr)*int(secondValueStr)

    if len(firstValueStr)%2 == 1:
        firstValueStr = '0' + firstValueStr
        #exponent = len(firstValueStr)-1
    if len(secondValueStr)%2 == 1:
        secondValueStr = '0' + secondValueStr
        #exponent = len(secondValueStr)-1

    '''if len(secondValueStr) != len(firstValueStr):
        if len(secondValueStr) > len(firstValueStr):
            exponent = len(firstValueStr)
        else:
            exponent = len(secondValueStr)
    else:
        exponent = len(firstValueStr)'''
    if len(firstValueStr) == 0: return
    a = firstValueStr[0:(len(firstValueStr)//2)]
    b = firstValueStr[(len(firstValueStr)//2):]
    c = secondValueStr[0:(len(secondValueStr)//2)]
    d = secondValueStr[(len(secondValueStr)//2):]
    #print('{} {} {} {}'.format(a, b, c, d))
    ac = karatsubaProduct(a, c)
    if ac is None:
        ac = 0
    print('ac = {}'.format(ac))
    bd = karatsubaProduct(b, d)
    if bd is None:
        bd = 0
    print('bd = {}'.format(bd))
    temp = karatsubaProduct((int(a)+int(b)),(int(c)+int(d)))
    temp = int(temp) - int(ac) - int(bd)
    if temp is None:
        temp = 0
    print('temp = {}'.format(temp))

    return float((10**(len(firstValueStr)))*int(ac) + (10**(len(firstValueStr)//2)*int(temp)) + int(bd))
    #return (10**exp)*ac + (10**(exp//2))*temp + bd


print(karatsubaProduct())
print('jest = {}, ma byc = {}'.format(karatsubaProduct(12, 23), 12*23))
print('jest = {}, ma byc = {}'.format(karatsubaProduct(1243, 3876), 1243*3876))
print('jest = {}, ma byc = {}'.format(karatsubaProduct(198765, 234567), float(198765*234567)))
print('jest = {}, ma byc = {}'.format(karatsubaProduct(119876511, 23456711), float(11198765*1234567)))
#print(karatsubaProduct(1643, 5876))     #9654268
#print(karatsubaProduct(398765, 634567)) #25304310980
