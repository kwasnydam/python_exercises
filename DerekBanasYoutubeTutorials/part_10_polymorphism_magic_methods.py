

class Animal(object):
    """Animal."""
    def __init__(self, birth_type = 'Unknown',
                appearence = 'Unknown', blooded = 'Unknown'):
        self.birth_type = birth_type
        self.appearence = appearence
        self.blooded = blooded

    @property
    def birth_type(self):
        return self.__birth_type
    @birth_type.setter
    def birth_type(self, birth_type):
        self.__birth_type = birth_type

    @property
    def appearence(self):
        return self.__appearence
    @appearence.setter
    def appearence(self, appearence):
        self.__appearence = appearence

    @property
    def blooded(self):
        return self.__blooded
    @blooded.setter
    def blooded(self, blooded):
        self.__blooded = blooded

    def __str__(self):
        ''' magic method that identifies the object '''
        return 'A {} is {} it is {} it is {}'.format(type(self).__name__,
        self.birth_type, self.blooded, self.appearence)

class Mammal(Animal):
    ''' Mammal inherits Animal '''
    def __init__(self, birth_type='born alive', appearence='hair or fur',
    blooded='warm blooded',  nurseYoung=True):
        Animal.__init__(self, birth_type, appearence, blooded)
        self.nurseYoung = nurseYoung

    @property
    def nurseYoung(self):
        return self.__nurseYoung

    @nurseYoung.setter
    def nurseYoung(self, nurseYoung):
        self.__nurseYoung = nurseYoung

    def __str__(self):
        return super().__str__() + 'and it is {} that they nurse their young'.\
        format(self.nurseYoung)

def main():
    animal_1 = Animal('born alive')

    print(animal_1.birth_type)
    print(animal_1)

    animal_2 = Mammal()
    print(animal_2.birth_type)
    print(animal_2)

main()
