
class Tile:

    # leave out of constructor for now, just to mess around with some things
    x = None
    y = None
    width = None
    height = None
    prevTiles = []
    nextTiles = []
    players = []
    image = None

#  Works with nothing or can work as a
#  Copy Constructor
    def __init__(self, tile = None):

        if tile is not None:
            self.x = tile.x
            self.y = tile.y
            self.width = tile.width
            self.height = tile.height
            self.prevTiles = tile.prevTiles
            self.nextTiles = tile.nextTiles
            self.players = tile.players
            self.image = tile.image
