
'''
Created by: Andrew Bunn
Class defines what a game board is
Holds tiles and players
'''

class Board:
    tiles = []
    players = []

    def __init__(self):
        self.startTile = None


    def addTile(self, tile):
        """
        add a tile to the boards list of tiles
        :param tile: tile to add to the board
        """
        self.tiles.append(tile)


    def getTiles(self):
        """
        get the list of tiles from the board
        :return return the list of tiles
        """
        return self.tiles

    # get a specified tile


    def addPlayer(self, player):
        """
        add a player to the board
        :param player: player to add to the board's list of players
        """
        self.players.append(player)


    def getPlayers(self):
        """
        get the list of players on the board
        :return: return the board's list of players
        """
        return self.players


    def getPotentialMoves(self, player):
        """
        gets all the possible moves for a specified player
        :param player: player to get the next moves for
        :return: returns a list of tiles
        """
        for tile in self.tiles:
            for searchPlayer in tile.players:
                if player == searchPlayer:
                    return tile.nextTiles


    def getCurrentTile(self, player):
        """
        get the current tile the specified player is on
        :param player: player to get the tile location from
        :return: returns the tile
        """
        for tile in self.tiles:
            for searchPlayer in tile.players:
                if player == searchPlayer:
                    return tile
        return None


    def movePlayer(self, nextTile, player):
        """
        moves a player to the next tile
        :param nextTile: list of potential next moves
        :param player: player to move
        """
        foundTile = None
        # find player in a tile
        foundTile = self.getCurrentTile(player)

        # remove player from current tile
        if foundTile:
            foundTile.players.remove(player)
            nextTile.players.append(player)


    def getStartTile(self):
        """
        gets the starting tile of the board
        :return: returns the start tile
        """
        return self.startTile