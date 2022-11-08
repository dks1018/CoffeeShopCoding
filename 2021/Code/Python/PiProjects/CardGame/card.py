class Card:
    
    def __init__(self, suit, number):
        self._suit = suit
        self._number = number
        
    def __repr__(self):
        return self._number + " of " + self.suit
    
    @property
    def suit(self):
        return self._suit
    
    @suit.setter
    def suit(self, suit):
        if suit in ["Hearts", "Clubs", "Diamonds", "Spades"]:
            self._suit = suit
        else:
            print("That is not a valid suit!")
            
    @property
    def number(self):
        return self._number
    
    @number.setter
    def number(self, number):
        if number in ["2","3","4","5","6","7","8","9","10","J","Q","K"]:
            self._number = number
        else:
            print("That is not a valid number!")
            
# my_card = Card("Hearts", "2")
# print(my_card)

# my_card.suit = "Clubs"
# my_card.number = "J"
# print(my_card)
