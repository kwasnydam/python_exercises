var1 = [2, 4, 6]    #var1 nie jest obiektem, jest referencja
print(var1) #       [2 4 6]
var2 = var1         #var2
var2.append(8)
print(var1)         #[2 4 6 8]
print(var2)         #[2 4 6 8]

#Typowanie dynamiczne
var1 = 1
print(type(var1))   #int
var1 += 0.1
print(type(var1))   #float

#zasieg zmiennych
zm1 = 10
zm2 = zm1**2
def zasiegZmiennych():
    global zm1
    zm1 = 11
    zm2 = 25
print(zm1, zm2)     #10 100
zasiegZmiennych()
print(zm1, zm2)     #11 100

#porównywanie zmiennych
"""
if a == b -> jeśli a i b mają tą samą wartość
if a is b -> Jeśli a i b są tym samym obiektem
if type(a) is type(b) -> jesli a i b są tego samego typu
