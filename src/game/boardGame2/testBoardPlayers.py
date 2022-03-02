import unittest
import time
import pygame

from src.game.boardGame2.boardRenderer import BoardRenderer
from src.game.boardGame2.board import Board
from src.game.boardGame.boardGame import getPlayerTurn
from src.game.boardGame.boardPlayers import BoardPlayer
from src.game.boardGame2.tile import Tile
from src.game.boardGame2.spriteLoader import SpriteLoader


'''
testBoardPlayers.py
Created by: Andrew Bunn
OLD test class to test board players and their movement
'''

class TestBoardPlayers(unittest.TestCase):

    def testMoving(self):
        """
        Test the movement of a player from tile to tile
        Render it on the board
        === OLD TEST ===
        Ended up changing things and not asserting anything,
        worked more like a main than a test
        Someone else touched file, commented out their additions
        """
        # self.thing = 0
        # numOfSpots = 0
        # moveTracker = 0
        #make a player
        player1 = BoardPlayer(1)
        player2 = BoardPlayer(2)

        # create the tiles
        startTile = Tile()
        startTile.x = 64
        startTile.y = 64
        startTile.width = 32
        startTile.height = 32
        startTile.image = SpriteLoader().loadImage("bluetile.png")

        tile2 = Tile(startTile)
        tile2.x += 32
        tile2.image = SpriteLoader().loadImage("bluetile.png")

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
        player2.image = SpriteLoader().loadImage("testPlayer2.png")
        tile2.players.append(player1)
        tile2.players.append(player2)

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
            time.sleep(1)

            # move player 1 to the first possible move in the move array
            nextTiles = board.getPotentialMoves(player2)
            # If the length of the next Tiles > 1 then we need to have
            # the player pick where to go (for now default to first option)
            if(len(nextTiles) == 0):
                print("No more moves!")
                pass
            else:
                board.movePlayer(nextTiles[0], player2)

