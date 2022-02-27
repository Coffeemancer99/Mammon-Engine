import unittest
import time
import pygame

from src.game.boardGame2.boardRenderer import BoardRenderer
from src.game.boardGame2.board import Board
from src.game.boardGame2.tile import Tile
from src.game.boardGame2.spriteLoader import SpriteLoader
from src.game.boardGame2.player import Player


class TestBoardRenderer(unittest.TestCase):

    def testPaintEx(self):
        #make a player
        player1 = Player()

        startTile = Tile()
        startTile.x = 64
        startTile.y = 64
        startTile.width = 32
        startTile.height = 32
        startTile.image = pygame.image.load("data/assets/sprites/blueTile.png")

        tile2 = Tile(startTile)
        tile2.x += 32
        tile2.image = pygame.image.load("data/assets/sprites/blueTile.png")

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

        # change tile color after so 5 and 6 don't inherit the color
        tile4.image = SpriteLoader().loadImage("redTile.png")

        player1.image = SpriteLoader().loadImage("testPlayer.png")
        tile2.players.append(player1)

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

            # render everything === change to render and update movement separately
            renderer.render()
            time.sleep(1)

            # get all the moves for player 1
            moves = board.getPotentialMoves(player1)

            # move player 1 to the first possible move in the move array
            if(len(moves) > 0):
                board.movePlayer(moves[0], player1)

        # Come back for backtiles later