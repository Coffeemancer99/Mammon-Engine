from src.game.boardGame2.board import Board
from src.game.boardGame2.tile import Tile
from src.game.boardGame2.player import Player
import pygame

class BoardRenderer:
    width = 512
    height = 448

    def __init__(self, board):
        self.board = board
        pygame.init()
        backgroundColor = (255,255,255)
        self.window = pygame.display.set_mode((self.width, self.height))
        self.window.fill(backgroundColor)
        pygame.display.flip()


    def renderTile(self, tile):
        self.window.blit(tile.image, (tile.x, tile.y))



    def renderPlayer(self, player, tile):
        self.window.blit(player.image, (tile.x, tile.y))


    def render(self):
        self.window.fill((155, 155, 155))

        for tile in self.board.getTiles():
            self.renderTile(tile)

        for tile in self.board.getTiles():
            for player in tile.players:
                self.renderPlayer(player, tile)

        pygame.display.update()


