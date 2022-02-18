from tile import Tile

class Board:
    tiles = []

    def __init__(self):
        pass

    def addTile(self, tile):
        self.tiles.append(tile)

    def getTiles(self):
        return self.tiles