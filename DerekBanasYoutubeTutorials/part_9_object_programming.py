class Fighter(object):
    """Fighter class represents a simple warrior
    @name - name of the fighter
    @hp - Health Points of a warrior
    @ap - Attack Points of a warrior
    """
    def __init__(self, name= '', hp= 0, ap= 0):
        self.name = name
        self.hp = hp
        self.ap = ap
        self.alive = True

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if type(name) == str:
            self.__name = name
        else:
            print('Give me a proper name, geez')


    @property
    def hp(self):
        return self.__hp

    @hp.setter
    def hp(self, hp):
        if type(hp) == int:
            if hp>=0:
                self.__hp = hp
            else:
                print('{}: im so dead lol'.format(self.name))
                self.__alive = False

        else:
            print('HP is a NUMBER you baka')

    @property
    def ap(self):
        return self.__ap

    @ap.setter
    def ap(self, ap):
        if type(ap) == int:
            if ap>=0:
                self.__ap = ap
            else:
                print('im hurting myself lol')
        else:
            print('AP is a NUMBER you baka')

    @property
    def alive(self):
        return self.__alive

    @alive.setter
    def alive(self, alive):
        self.__alive = alive

    def attack(self, opponent):
        opponent.hp -= self.ap

class Duel(object):
    """the class represents the fight between fighters"""
    def __init__(self, fighter_one, fighter_two):
        self.fighter_one = fighter_one
        self.fighter_two = fighter_two

    def fight(self):
        while True:
            self.fighter_one.attack(self.fighter_two)
            print('{} attacks, {} with {} hp left'.format(self.fighter_one.name,\
            self.fighter_two.name, self.fighter_two.hp))
            if not (self.fighter_one.alive and self.fighter_two.alive):
                break
            self.fighter_two.attack(self.fighter_one)
            print('{} attacks, {} with {} hp left'.format(self.fighter_two.name,\
            self.fighter_one.name, self.fighter_one.hp))
            if not (self.fighter_one.alive and self.fighter_two.alive):
                break

        if self.fighter_one.alive:
            print('{} has {} hp left so he won'.format(self.fighter_one.name, \
            self.fighter_one.hp))
        else:
            print('{} has {} hp left so he won'.format(self.fighter_two.name, \
            self.fighter_two.hp))

    def attack(self):
        ''' I guess that should be a fighter class method but ii desu '''
        pass


def main():
    naruto = Fighter('Naruto', 9999, 999)
    sasuke = Fighter('Sasuke', 9998, 998)
    print([naruto.name, naruto.hp, naruto.ap])

    duel = Duel(naruto, sasuke)
    duel.fight()

main()
