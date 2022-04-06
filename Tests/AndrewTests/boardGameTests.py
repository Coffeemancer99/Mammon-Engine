import unittest

from src.game.boardGame2.firstBoard import FirstBoard
from src.game.boardGame2.tile import Tile
from src.engine.button import Button
from src.game.boardGame.boardPlayers import BoardPlayer
from src.game.boardGame2.board import Board
from src.game.boardGame2.spriteLoader import SpriteLoader
import pygame


class TestBoardGame(unittest.TestCase):
    # White Box Test
    """
    White Box Test achieves Branch Coverage for checking a button was pressed

     def wasClicked(self, click):
        :param click: location of click in the window (x,y)
        :return: return true if the button was clicked within it's bounds
                 else return false

        if((click[0] > self.x * self.scale) and (click[0] <= (self.x + self.width) * self.scale)):  # x
            if ((click[1] > self.y * self.scale) and (click[1] <= (self.y + self.height) * self.scale)):  # y
                return True
        return False
    """
    def testButtonPressedBranchCoverage(self):
        mainWindow = pygame.display.set_mode((512, 448))
        # x, y, width, height, onClick, buttonImage, window
        button1 = Button(0, 0, 24, 24, 1, None, "oneVOneButton", mainWindow)

        click = [1, 1]
        clickInBounds = button1.wasClicked(click)
        self.assertTrue(clickInBounds, "Click [1,1] should be in bounds")

        click = [128, 128]
        clickInBounds = button1.wasClicked(click)
        self.assertFalse(clickInBounds, "Click [128,128] should return false, out of bounds")

        click = [1, 128]
        clickInBounds = button1.wasClicked(click)
        self.assertFalse(clickInBounds, "Click [1,128] should return false, out of bounds in y dim")

        click = [128, 1]
        clickInBounds = button1.wasClicked(click)
        self.assertFalse(clickInBounds, "Click [128,1] should return false, out of bounds in x dim")



    # Integration Tests
    def testNumberOfTiles(self):
        # Integration Test - Make sure that firstBoard is filled with 38 tiles
        # Approach - Big Bang because we tried connecting all our modules after we completed them.
        #            Avoid in the future...
        # Classes being used:
        #   Board - Andrew's
        #   Tile - Andrew's

        firstBoard = FirstBoard()
        gameBoard = firstBoard.testFirstBoard()
        tileCount = len(gameBoard.tiles)
        self.assertEqual(tileCount, 38, "Expected 38 tiles in firstBoard")



    def testPlayerPotentialMoves(self):
        # Integration Test - check that the potential moves for a player on the starting tile is the second tile (the
        #  next tile in the pathway)
        # Approach - Big Bang because we tried connecting all our modules after we completed them.
        #            Avoid in the future...
        # Classes being used:
        #   BoardPlayer - Joel's
        #   Board - Andrew's
        #   Tile - Andrew's

        # Tile Setup
        tile1 = Tile()
        tile2 = Tile()
        tile1.typeOfTile = "FirstTile"
        tile2.typeOfTile = "SecondTile"

        # Player setup
        player = BoardPlayer(1)
        tile1.players.append(player)
        player.currentPosition = tile1

        # Board Setup
        gameBoard = Board()
        gameBoard.addTile(tile1)
        gameBoard.addTile(tile2)
        tile1.addNextTile(tile2)
        tile2.addPrevTile(tile1)
        gameBoard.startTile = tile1

        # Get next tile and move player there
        nextTiles = gameBoard.getPotentialMoves(player)
        self.assertEqual(len(nextTiles), 1, "Expected one move from start tile")
        self.assertEqual(nextTiles[0].typeOfTile, tile2.typeOfTile, "Next tile is not the second tile")


    def testMovePlayer(self):
        # Integration Test - check that the player ends up on the correct tile when the player moves
        # Approach - Big Bang because we tried connecting all our modules after we completed them.
        #            Avoid in the future...
        # Classes being used:
        #   BoardPlayer - Joel's
        #   Board - Andrew's
        #   Tile - Andrew's

        # Tile Setup
        tile1 = Tile()
        tile2 = Tile()
        tile1.typeOfTile = "FirstTile"
        tile2.typeOfTile = "SecondTile"

        # Player setup
        player = BoardPlayer(1)
        tile1.players.append(player)
        player.currentPosition = tile1

        # Board Setup
        gameBoard = Board()
        gameBoard.addTile(tile1)
        gameBoard.addTile(tile2)
        tile1.addNextTile(tile2)
        tile2.addPrevTile(tile1)
        gameBoard.startTile = tile1

        # Get next tile and move player there
        nextTile = gameBoard.getPotentialMoves(player)
        self.assertIsNotNone(nextTile, "Expected tile(s)")
        self.assertEqual(len(nextTile), 1, "Expected 1 next tile")

        gameBoard.movePlayer(nextTile[0], player)
        self.assertEqual(tile2.players[0], player, "Player is not on second tile")

        # Black Box Tests/ Acceptance Tests

    def testNextTile(self):
        # Acceptance Test testing the ability to add a single next tile to a specific tile
        firstTile = Tile()
        secondTile = Tile()
        firstTile.addNextTile(secondTile)
        self.assertEqual(firstTile.nextTiles[0], secondTile, "First tile next is not second tile")

    def testPrevTile(self):
        # Acceptance Test testing the ability to add a single previous tile to a specific tile
        firstTile = Tile()
        secondTile = Tile()
        secondTile.addPrevTile(firstTile)
        self.assertEqual(secondTile.prevTiles[0], firstTile, "Second tile previous is not first tile")

    def testRetNextTiles(self):
        # Acceptance Test testing my method for getting the next tiles back from a tile
        firstTile = Tile()
        secondTile = Tile()
        thirdTile = Tile()
        firstTile.addNextTile(secondTile)
        firstTile.addNextTile(thirdTile)

        nextTiles = firstTile.getNextTiles()
        self.assertEqual(nextTiles, [secondTile, thirdTile])

    def testRetPrevTiles(self):
        # Acceptance Test testing my method for getting the previous tiles back from a tile
        firstTile = Tile()
        secondTile = Tile()
        thirdTile = Tile()
        thirdTile.addPrevTile(firstTile)
        thirdTile.addPrevTile(secondTile)

        prevTiles = thirdTile.getPrevTiles()
        self.assertEqual(prevTiles, [firstTile, secondTile])

    def testNextTiles(self):
        # Acceptance Test testing the ability to add a multiple next tiles (through one function) to a specific tile
        # and get them back
        firstTile = Tile()
        secondTile = Tile()
        thirdTile = Tile()
        firstTile.addMultNextTiles([secondTile, thirdTile])
        self.assertEqual(firstTile.getNextTiles(), [secondTile, thirdTile], "First tile next is not second "
                                                                            "and third tile")

    def testPrevTiles(self):
        # Acceptance Test testing the ability to add a multiple previous tiles (through one function) to a specific tile
        # and get them back
        firstTile = Tile()
        secondTile = Tile()
        thirdTile = Tile()
        thirdTile.addMultPrevTiles([firstTile, secondTile])
        self.assertEqual(thirdTile.getPrevTiles(), [firstTile, secondTile], "Third tile previous is not first "
                                                                            "and second tile")

    def testTileCopy(self):
        # Acceptance Test testing that I can successfully copy a tile from a given tile
        origTile = Tile()
        origTile.x = 32
        origTile.y = 64
        origTile.typeOfTile = "normal"
        newTile = Tile(origTile)
        self.assertEqual(origTile.x, newTile.x, "X coords don't match")
        self.assertEqual(origTile.y, newTile.y, "Y coords don't match")
        self.assertEqual(origTile.width, newTile.width, "Widths don't match")
        self.assertEqual(origTile.height, newTile.height, "Heights don't match")
        self.assertEqual(origTile.typeOfTile, newTile.typeOfTile, "Different types")

    def testSpriteLoader(self):
        # Acceptance Test testing that sprite loader does not return None and that it returns a Pygame Surface object
        actual = SpriteLoader().loadImage("coconut.png")
        self.assertIsNotNone(actual)
        self.assertTrue(isinstance(actual, pygame.Surface))
