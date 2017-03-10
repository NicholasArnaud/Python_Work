'''Card Dealer'''
import random
'''
A Dealer deals 5 cards to players at the beginning of a game.
Cards can have a value of 5 or 10 if they are "Light" or "Dark".
Write a function that determines which player has the highest total
and return that player with the total.
'''
totalplayers = []

class Card(object):
    '''Card selection class'''

    def __init__(self):
        colornum = random.randint(1, 2)
        if colornum == 1:
            self._color = "Light"
            self._value = 5
        else:
            self._color = "Dark"
            self._value = 10

    @property
    def value(self):
        '''value'''
        return self._value


class Player(object):
    '''Player class'''

    def __init__(self, _id):
        self.cards = []
        self.ide = _id
        self.totalcards = 0
        totalplayers.append(self)

    def recievecard(self, card):
        '''Gives card to Player'''
        self.cards.append(card)


    def cardinhand(self):
        '''shows card'''
        print 'Player '+ str(self.ide) + ' has cards'
        for card in self.cards:
            print card.value,

    @property
    def total(self):
        '''total'''
        cardtotal = 0
        for i in self.cards:
            cardtotal += i.value
        return cardtotal


def addplayer(player):
    '''Adds player to list'''
    totalplayers.append(player)


def main():
    '''Main function/ Entry point'''
    joe = Player("joe")
    bob = Player("bob")
    bill = Player("bill")
    chris = Player("chris")
    jimmy = Player("jimmy")

    cardselect()

    winner = checkwinner(totalplayers)
    print "Player "+ winner[0].ide + " wins with "+ str(winner[1]) + " points"


def cardselect():
    '''Players revieve cards'''
    deck = [Card() for c in range(52)]

    for i in range(1, 6):
        for player in totalplayers:
            randomcard = random.randint(1, 51)
            player.recievecard(deck[randomcard])
            player.totalcards = i


def checkwinner(players):
    '''Checks for winner'''
    players.sort(key=lambda x: x.total, reverse=True)
    return [players[0], players[0].total]


if __name__ == "__main__":
    main()
