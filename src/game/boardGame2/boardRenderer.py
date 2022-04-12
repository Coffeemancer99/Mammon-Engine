import pygame

'''
Created by: Andrew Bunn
Class for rendering the game board, all it's tiles, and players
'''


class BoardRenderer:
    # width = 512
    # height = 448

    def __init__(self, board, window, scale):
        """
        :param board: the board to render
        """
        self.board = board
        pygame.init()
        backgroundColor = (255, 255, 255)
        self.window = window
        self.scale = scale
        self.window.fill(backgroundColor)
        pygame.display.update()

    def renderTile(self, tile):
        """
        renders the tile to the screen at its current position
        :param tile:
        """
        img = tile.image
        img = pygame.transform.scale(img,
                                     ((img.get_width()) * self.scale,
                                      (img.get_height()) * self.scale))
        self.window.blit(img, (tile.x, tile.y))

    def renderPlayer(self, player, tile):
        """
        renders a player on a given tile
        :param player: player to render
        :param tile: tile to render player on
        """
        img = player.image
        img = pygame.transform.scale(img,
                                     ((img.get_width()) * self.scale,
                                      (img.get_height()) * self.scale))
        self.window.blit(img, (tile.x, tile.y))

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
