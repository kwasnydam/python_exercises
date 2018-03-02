import random

class Player(object):
    """Player class represents a Coin Flip game Player.
    Parameters:
    mame
    predicition

    Methods:
    getPredicition
    setPredicition  -   forced from outside
    makePredicition - random if choosen
    """
    def __init__(self, name = None, prediction = None):
        self.name = name
        self.prediction = prediction

    @property
    def prediction(self):
        return self.__prediction

    @prediction.setter
    def prediction(self, prediction):
        if prediction == 'H':
            self.__prediction = 'T'
        else:
            self.__prediction = 'H'
        print('{} has {}'.format(self.name, self.prediction))
    def makePrediction(self):
        self.predicition = random.choice(['H', 'T'])
        print('{} predicted {}'.format(self.name, self.prediction))

class Coin(object):
    """Coin class is responsible for flipping a coin"""
    def __init__(self):
        self.result = None

    @property
    def result(self):
        return self.__result

    @result.setter
    def result(self, val):
        self.__result = val

    def flip(self):
        self.__result = random.choice(['H', 'T'])

class CoinGame(object):
    """Runs the Coin Flip Game"""
    def __init__(self, player1=None, player2=None, coin=None):
        self.player1 = player1
        self.player2 = player2
        self.coin = coin

    @property
    def player1(self):
        return self.__player1

    @player1.setter
    def player1(self, player):
        try:
            if isinstance(player, Player):
                self.__player1 = player
            else:
                raise ValueError
        except ValueError as e:
            print('ValueError: Expected {} was {}'.format(
            Player.__name__, type(player).__name__))


    @property
    def player2(self):
        return self.__player2

    @player2.setter
    def player2(self, player):
        try:
            if isinstance(player, Player):
                self.__player2 = player
                print('U did it man')
            else:
                raise ValueError
        except ValueError as e:
            print('ValueError: Expected {} was {}'.format(
            Player.__name__, type(player).__name__))

    @property
    def coin(self):
        return self.__coin

    @coin.setter
    def coin(self, coin):
        try:
            if isinstance(coin, Coin):
                self.__coin = coin
            else:
                raise TypeError
        except TypeError as e:
            print('ValueError: Expected {} was {}'.format(
            Coin.__name__, type(coin).__name__))

    def winner(self):
        if self.player1.prediction == self.coin.result:
            print('{} won'.format(self.player1.name))
        else:
            print('{} won'.format(self.player2.name))

    def resultsLogger(self):
        with open('coinFlipLog.txt','a+', encoding = 'utf-8') as f:
            f.write('Coin: {} {}: {} {} {}\n'.format(self.coin.result, self.player1.name,
            self.player1.prediction, self.player2.name,self.player2.prediction))
            if self.player1.prediction == self.coin.result:
                f.write('{} won'.format(self.player1.name))
            else:
                f.write('{} won'.format(self.player2.name))
            f.write('\n')

    def startGame(self):
        if self.player1 and self.player2 and self.coin:
            pass
        else:
            return
        print('Welcome to the coin Flip game')
        print('Player1 name is {}'.format(self.player1.name))
        print('Player2 name is {}'.format(self.player2.name))
        #So we are in the game
        while True:
            chosenPlayer = random.choice([1, 2])
            if chosenPlayer == 1:
                self.player1.makePrediction()
                self.player2.prediction = (self.player1.prediction)
            else:
                self.player2.makePrediction()
                self.player1.prediction = (self.player2.prediction)

            self.coin.flip()
            result = self.coin.result
            print('Coin: {} {}: {} {} {}'.format(result, self.player1.name,
            self.player1.prediction, self.player2.name,self.player2.prediction))
            self.winner()
            self.resultsLogger()
            playAgain = input('type "y" if you want to have a next round: ')
            if playAgain == 'y':
                pass
            else:
                break
def main():
    player1 = Player(name='Joe')
    player2 = Player(name='Steve')
    coin = Coin()
    coinGame = CoinGame(player1, player2, coin)
    coinGame.startGame()

main()
