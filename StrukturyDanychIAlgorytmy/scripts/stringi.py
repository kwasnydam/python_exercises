#są niemutowalne (iimutable) -> kazda z metod zwraca wartosc, ale nie zmienia
#obiektu, bo tego nie mozna zrobic
s = "Damian jest pajacem"
print(s.count('a'))    #Liczy wystapienia podciagu w ciagu, zwroci 4
print(s.find('mi'))    #Zwraca index pierwszego wystapienia podciagu, zwroci 2
print(s.isalnum())     #True jesli jest ltera lub liczba
print(s.isalpha())     #True jesli zaweira same litery
print(s.isdigit())     #True, jesli zaweira same liczby
print(s.replace('Damian', 'Patryk'))   #w wyniku 'Patryk jest pajacem'
#Zwraca nowy string zamiast modyfikować wejściowy!!
sLits = s.split()       #dzieli na wyrazy
for element in sLits:
    print(element)
#ta petla wypisuje poszczegolne wyrazy

#indeksowanie stringow ( i kazdych innych typow sekwencyjnych):
print(s[2])             #wypisze 3 element: 'm'
print(s[s.find('mi')])  #wypisze to smao co powyzej: 'm'
print(s[2:8])           #wypisze znaki od 3 do 9:    'mian j'
print(s[::2])           #wypisze co drugi znak:      'Dma etpjcm'

#modyfikowanie strnigow jako tworzenie nowych na bazie starych
nihonNoS = 'Damian san wa baka desu'
ind = nihonNoS.find('baka')
newNihonNoS = nihonNoS[:ind] + 'hontoni ' + nihonNoS[ind:]
print(newNihonNoS)
