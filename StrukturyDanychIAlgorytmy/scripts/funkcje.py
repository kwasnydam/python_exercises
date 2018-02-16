"""
Funkcje w pythonie są "first class objects". Oznacza to, że:
- mogą być tworzone w czasie pracy
- mogą być przypisane jak zmienna lub wewnątrz struktury
- mogą być przekazane jako argument do funkcji
- mogą być przekazane jako wynik fukncji
"""
def callFunction(funkcja):
    lang = 'jap'
    return funkcja(lang)

def greeting(lang):
    if lang == 'eng':
        return "Hello world!"
    elif lang == 'jap':
        return "Konnichiwa sekai!"
    else:
        return "Kono gengo wakarimasen!"

#ponizej funkcja jako element listy (a raczej jej wyniki)
greetingsList = [greeting('eng'), greeting('jap'), greeting('pol')]
for greeting_inst in greetingsList: print(greeting_inst)

#Teraz funkcja przekazana jako argument do innej funkcji i zwrocona jako wynik

powitanie = callFunction(greeting)
print(powitanie)    #'Konnichiwa sekai' desu

#Funkcje rekurencyjne - przyklad silnia
def silnia(x):
    if x == 1:
        return 1
    return x*silnia(x-1)
silniaWynik = silnia(5)
print(silniaWynik)      #120

"""
Funkcje generatory - kod skladajacy sie na funkcje generator nie zostaje wykonany
w momencie wywołania funkcji, zamiast tego tworzony jest specjalny obiekt -
generator. Kod znajdujący się wewnątrz funkcji - generatora zostaje odpalony
dopiero w momencie kiedy jakas petla for probuje przejsc po obiekcie generatorze
"""
def genNieparzystych (start, end):
    while (start<end):
        yield start
        start += 2
gen1 = genNieparzystych(1,25)
#print(sum(gen1))
for value in gen1 : print(value)

#oprócz funkcji generatorów mamy jeszcze wyrażenie generatorowe (generator expression)
gen2 = (10**i for i in range(4)) #wyglada jak list comprehension, ale ma (), nie[]
for value in gen2: print(value)
