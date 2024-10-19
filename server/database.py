class Database:
    def __init__(self):
        self.boardGames = {"Catan": {"playercount": "4", "gametime": "60 minutes", "age": "10", "gamecount": 5},
                           "Monopoly": {"playercount": "4", "gametime": "90 minutes", "age": "8", "gamecount": 3},
                           "Risk": {"playercount": "6", "gametime": "120 minutes", "age": "10", "gamecount": 2}}

    def add_game(self, data):
        self.boardGames.update(data)

    def delete_game(self, name):
        # Check if the game exists before deleting
        if name in self.boardGames:
            del self.boardGames[name]
            return True
        else:
            return False
