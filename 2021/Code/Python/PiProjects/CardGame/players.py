class Gamers:

    def __init__(self, players, playerCount):
       self._players = players
       self._playerCount = playerCount

    def __playerInfo__(self):
        return "There are " + self.playerCount + " players, they are:\n" + self.players 
    
    def __players__(self, count):
        self._playerCount = (int(input("How many people are playing: ")))
    
    def __playerNames__(self, players):
        for i in range(self._playerCount):
            self._players = (str(input("Input player names: ")))
            