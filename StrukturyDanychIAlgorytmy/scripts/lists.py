"""
Listy są najpopularniejszym wbudowanym typen danych, bo moga skladac sie z
dowolnych typow danych/obiektow. Podobnie jak w przypadku stringow, listy
mozna przegladac po indeksie.
Złożoność obliczeniowa operacji na typie list:
append -> O(1)
len -> O(1)
remove -> O(n)
insert -> O(n)
min -> O(n)
max -> O(n)
in -> O(n)
"""
x = 1
y = 2
z = 3
listInt = [x, y, z]
for el in enumerate(listInt): print(el) #([0 1] [1 2] [2 3])
listInt.append(4)   #dodaje element na koncu listy
print('appended list:\n')
for el in enumerate(listInt): print(el) #([0 1] [1 2] [2 3] [3 4])
listInt.extend(listInt)
print('extended list:\n')
for el in enumerate(listInt): print(el)
#([0 1] [1 2] [2 3] [3 4] [0 1] [1 2] [2 3] [3 4])
print(listInt.count(1))     #2
listInt.insert(0, 10)
for el in enumerate(listInt): print(el)
#na poczayku jest 10
#s.pop(index) - zwraca el. na tym indkesie i usuwa go z Listy
#s.remove(object) - usuwa obiekt z listy
listInt.reverse()   #Odwraca kolejnosc elementow w liscie
print('reversed list\n')
for el in enumerate(listInt): print(el)


#Kopiowanie list (i innych kontenerow) jest implicit. Nowe obiekty sa tworzone
#dopiero wtedy kiedy zajdzie taka potrzeba, czyli poczatkowo dwie Listy
#wskazuja na to samo miejsce w pamieci
#Dodatkowo, listy moga zawierac dowolne obiekty, na przyklad inne listy
items = [['ryz', 2.4, 8], ['maka', 1.9, 5], ['popkorn', 5.1, 10]]
print('Przedmiot\tcena\tilosc\n')
for item in items:
    for element in item:
        print(element, end='\t')
    print('')
print(items[1][1]*1.2)  #Do elementow mozemy dostac sie poprzez indeksy, 2.28

def x2(x): return x*2
def x4(x): return x*4
#List Comprehension przykład
lst = []
print('Generowanie listy z uzycim petli for')
for i in range(4):
    lst.append(x2(x4(i)))   #Wynik: 0 8 16 24
    print(lst[i])
print('Generowanie listy za pomoca "list Comprehension"')
print([x2(x) for x in range(16) if x in [x4(j) for j in range(4)]]) #wynik 0 8 16 24
#inne uzycie list Comprehension:
sentence = 'Python wa sugoi desu ne?'
words = sentence.split()
print([[word, len(word)] for word in words])
