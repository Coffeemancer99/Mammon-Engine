
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
            self.prevTiles = [] # dont want them to copy other's next or prev tiles
            # for tile in tile.prevTiles:
            #     self.prevTiles.append(tile)
            self.nextTiles = []
            self.players = []
            # for player in tile.players:
            #     self.players.append(player)
            self.image = tile.image
