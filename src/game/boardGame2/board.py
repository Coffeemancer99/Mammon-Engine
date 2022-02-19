
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


    '''
    getPotentialMoves - Given a player, get the potential moves
    returns the tile the player is on's next tiles list
    '''
    def getPotentialMoves(self, player):
        for tile in self.tiles:
            for searchPlayer in tile.players:
                if player == searchPlayer:
                    return tile.nextTiles

    def getCurrentTile(self, player):
        for tile in self.tiles:
            for searchPlayer in tile.players:
                if player == searchPlayer:
                    return tile


    '''
    movePlayer - move the specified player to the next tile
    '''
    def movePlayer(self, nextTile, player):
        foundTile = None
        # find player in a tile
        for walkTile in self.tiles:
            for walkPlayer in walkTile.players:
                # if tile found
               if player == walkPlayer:
                   foundTile = walkTile

        # remove player from current tile
        if foundTile:
            foundTile.players.remove(player)
            nextTile.players.append(player)