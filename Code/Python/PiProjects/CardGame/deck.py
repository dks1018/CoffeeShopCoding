from card import Card
from random import shuffle
import Gamers

class Deck:

    def __init__(self):
        self._cards = []
        self.populate()
        self.shuffleCards()
        print(self._cards)
    
    def populate(self):
        suits = ["Hearts", "Clubs", "Diamonds", "Spades"]
        numbers = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
        self._cards = [ Card(s,n) for s in suits for n in numbers ]
           
    def shuffleCards(self):
        shuffle(self._cards)
        
    #def deal():
    
myDeck = Deck()

        # cards = []  #Create an empty list of cards
        # for suit in suits:  #For each Suit...
        #     for number in numbers:  #For each number... 
        #         #Create a new card object and add it to the list
        #         cards.append( Card(suit, number) )
        # self._cards = cards