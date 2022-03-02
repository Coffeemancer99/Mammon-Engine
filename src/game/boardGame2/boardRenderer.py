import pygame
from src.game.boardGame2.board import Board
from src.game.boardGame2.tile import Tile
from src.game.boardGame2.player import Player

'''
Created by: Andrew Bunn
Class for rendering the game board, all it's tiles, and players
'''

class BoardRenderer:
    width = 512
    height = 448

    def __init__(self, board):
        """
        :param board: the board to render
        """
        self.board = board
        pygame.init()
        backgroundColor = (255, 255, 255)
        self.window = pygame.display.set_mode((self.width, self.height))
        self.window.fill(backgroundColor)
        pygame.display.update()


    def renderTile(self, tile):
        """
        renders the tile to the screen at its current position
        :param tile:
        """
        self.window.blit(tile.image, (tile.x, tile.y))


    def renderPlayer(self, player, tile):
        """
        renders a player on a given tile
        :param player: player to render
        :param tile: tile to render player on
        """
        self.window.blit(player.image, (tile.x, tile.y))


    def render(self):
        """
        Renders all the tiles and players
        """
        self.window.fill((155, 155, 155))

        for tile in self.board.getTiles():
            self.renderTile(tile)

        # render players after tiles
        for tile in self.board.getTiles():
            for player in tile.players:
                self.renderPlayer(player, tile)

        pygame.display.update()


