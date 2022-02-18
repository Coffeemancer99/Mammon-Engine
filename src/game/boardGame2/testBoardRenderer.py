import unittest

import pygame

from boardRenderer import BoardRenderer
from board import Board
from tile import Tile
from spriteLoader import SpriteLoader


class TestBoardRenderer(unittest.TestCase):

    def testPaintEx(self):
        startTile = Tile()
        startTile.x = 64
        startTile.y = 64
        startTile.width = 32
        startTile.height = 32
        startTile.image = SpriteLoader().loadImage("bolSprite.png")

        tile2 = Tile(startTile)
        tile2.x += 32
        tile2.image = SpriteLoader().loadImage("groundSprite1.png")

        tile3 = Tile(tile2)
        tile3.x += 32

        tile4 = Tile(tile3)
        tile4.x += 32

        # Split high
        tile5 = Tile(tile4)
        tile5.x += 32
        tile5.y += 32

        # Split low
        tile6 = Tile(tile4)
        tile6.x += 32
        tile6.y -= 32

        startTile.nextTiles.append(tile2)
        tile2.nextTiles.append(tile3)
        tile3.nextTiles.append(tile4)
        tile4.nextTiles.append(tile5)
        tile4.nextTiles.append(tile6)

        board = Board()
        board.addTile(startTile)
        board.addTile(tile2)
        board.addTile(tile3)
        board.addTile(tile4)
        board.addTile(tile5)
        board.addTile(tile6)

        renderer = BoardRenderer(board)
        isRunning = True
        while(isRunning):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

            # render everything
            renderer.render()

        # Come back for backtiles later

