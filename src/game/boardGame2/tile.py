"""
Created by: Andrew Bunn
Class defining what a tile is
"""


class Tile:

    # leave out of constructor for now

    #  Works with nothing or can work as a
    #  Copy Constructor for making new tiles quicker
    def __init__(self, tile=None):
        """
        :param tile: tile to copy (if not None)
        :param x: x pos of tile
        :param y: y pos of tile
        :param width: width of tile
        :param height: height of tile
        :param prevTiles: list of previous tiles
        :param nextTiles: list of next tiles in line
        :param players: list of players on tile
        :param image: tile image
        :param typeOfTile: tile type (string)
        """
        self.x = None
        self.y = None
        self.width = None
        self.height = None
        self.prevTiles = []
        self.nextTiles = []
        self.players = []
        self.image = None
        self.typeOfTile = ""

        if tile is not None:
            self.x = tile.x
            self.y = tile.y
            self.width = tile.width
            self.height = tile.height
            self.prevTiles = []  # don't want them to copy other's next or prev tiles
            for tile in tile.prevTiles:
                self.prevTiles.append(tile)
            self.nextTiles = []  # don't copy next tiles
            self.players = []  # don't copy prev tiles
            for player in tile.players:
                self.players.append(player)
            self.image = tile.image
            self.typeOfTile = tile.typeOfTile

    def addNextTile(self, tileToAdd):
        self.nextTiles.append(tileToAdd)

    def addPrevTile(self, tileToAdd):
        self.prevTiles.append(tileToAdd)

    def addMultNextTiles(self, tilesToAdd):
        self.nextTiles.extend(tilesToAdd)

    def addMultPrevTiles(self, tilesToAdd):
        self.prevTiles.extend(tilesToAdd)

    def getNextTiles(self):
        return self.nextTiles

    def getPrevTiles(self):
        return self.prevTiles
