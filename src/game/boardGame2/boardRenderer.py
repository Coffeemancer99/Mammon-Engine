from board import Board
from tile import Tile
import pygame

class BoardRenderer:
    width = 512
    height = 512

    def __init__(self, board):
        self.board = board
        pygame.init()
        backgroundColor = (255,255,255)
        self.window = pygame.display.set_mode((self.width, self.height))
        self.window.fill(backgroundColor)
        pygame.display.flip()


    def renderTile(self, tile):
        self.window.blit(tile.image, (tile.x, tile.y))
        pygame.display.update()
        pass


    def render(self):
        for tile in self.board.getTiles():
            self.renderTile(tile)
