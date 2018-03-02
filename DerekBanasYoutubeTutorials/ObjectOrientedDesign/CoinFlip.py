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
    def __init__(self, name):
        self.name = name
        self.prediction = None
    @property
    def prediction(self):
        return self.__prediction

    @predicition.setter
    def predicition(self, prediction):
        if prediction == 'H':
            self.__prediction = 'T'
        else:
            self.__prediction = 'H'
    def makePrediction(self):
        self.predicition = random.choice(['H', 'T'])

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
            if player isinstance(Player):
                self.player1 = player
            else:
                raise ValueError
        except ValueError as e:
            print('ValueError: Expected {} was {}'.format(
            Player.__name__, type(player).__name__))
        else:
            print('U screwed up man')

    @property
    def player2(self):
        return self.__player2

    @player2.setter
    def player2(self, player):
        try:
            if player isinstance(Player):
                self.player2 = player
            else:
                raise ValueError
        except ValueError as e:
            print('ValueError: Expected {} was {}'.format(
            Player.__name__, type(player).__name__))
        else:
            print('U screwed up man')

    @property
    def coin(self):
        return self.__coin

    @coin.setter
    def coin(self, coin):
        try:
            if coin isinstance(Coin):
                self.coin = coin
            else:
                raise TypeError
        except TypeError as e:
            print('ValueError: Expected {} was {}'.format(
            Coin.__name__, type(coin).__name__))
        else:
            print('U screwed up man')

    def startGame(self):
        if self.player1 and self.player2 and self.coin:
            pass
        else:
            break

        #So we are in the game
        chosenPlayer = random.choice([1, 2])
        if chosenPlayer == 1:
            self.player1.makePrediction()
            self.player2.setPredicition(self.player1.prediction)
        else:
            self.player2.makePrediction()
            self.player1.setPredicition(self.player2.prediction)

        self.coin.flip()
        result = self.coin.result
        print('Coin: {} Player1: {} Player2 {}'.format(result, self.player1.prediction,
        self.player2.prediction))

def main():
    player1 = Player(name='Joe')
    player2 = Player(name='Steve')
    coin = Coin()
    coinGame = CoinGame(player1, player2, coin)
    coinGame.startGame()

main()
