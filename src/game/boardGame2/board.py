from tile import Tile

class Board:
    tiles = []
    players = []

    def __init__(self):
        pass

    def addTile(self, tile):
        self.tiles.append(tile)

    def getTiles(self):
        return self.tiles

    # get a specified tile

    def addPlayer(self, player):
        self.players.append(player)

    def getPlayers(self):
        return self.players