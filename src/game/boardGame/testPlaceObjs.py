import networkx as nx
import networkx
import src.game.boardTile.tile as tile
import src.game.boardTile.boardGraph as bg

from board import Board
from pathManager import PathManager
import unittest
import pygame
import boardRenderer


class TestPlaceObjs(unittest.TestCase):

    def testGenerateBoard(self):
        width = 5
        height = 5
        board = Board()
        board.generateBoard(width, height)
        self.assertEqual(board.getWidth(), width)
        self.assertEqual(board.getHeight(), height)

    def testGenerateBoardDimensions(self):
        width = 3
        height = 3
        board = Board()
        board.generateBoard(width, height)
        self.assertEqual(board.getWidth(), width)
        self.assertEqual(board.getHeight(), height)
        board.placeObject(2, 2, "First One")
        # board.placeObject(2, 2, "Second One")
        board.debugBoard()

    def testPlaceObjects(self):
        width = 5
        height = 5
        board = Board()
        board.generateBoard(width, height)
        id = 1
        type = "Human"
        x = 3
        y = 4
        player = [id, type, x, y]
        randomStr = "Dis"
        aBigNum = 129023
        board.placeObject(x, y, player)
        board.placeObject(x, y, randomStr)
        board.placeObject(x, y, aBigNum)
        playerReturned = board.getObjsAt(x, y)
        self.assertEqual([player, randomStr, aBigNum], playerReturned)

'''
PathManagerTest:
tests whether there is a move from the current
position
'''
class PathManagerTest(unittest.TestCase):

    def test3x3OnePossibleMoveW(self):

        tileAttr = 'tile'
        width = 3
        height = 3
        board = Board()
        board.generateBoard(width, height)
        player = ["Tester", 42, "180-D"]

        # Place player
        board.placeObject(2,2, player)

        # Place one valid move
        board.placeObject(1, 2, tileAttr)

        pathMgr = PathManager()
        pathMgr.setBoard(board)

        moves = pathMgr.getMovesFromCurPos(2,2, tileAttr)
        self.assertEqual(1, len(moves))
        # works if there is a move from 2,2 to 1,2 and 1,2 is a tile!


'''
BoardGraphTests:
Working with a NetworkX directed graph i created
'''
class BoardGraphTests(unittest.TestCase):

    def testBoardGraphGeneration(self):
        # === Graph Testing ===
        # create the graph for the board
        board = bg.BoardGraph.generateBoard(None)

        print("Number of nodes currently:", board.number_of_nodes())
        print("Number of edges: ", board.number_of_edges())
        print("Paths from 3:", list(iter(board[3])))
        print("Predecessors of 3:", list(board.predecessors(3)))
        # print(board[1].name)
        for tile in board:
            print(tile)


'''
TestWindowDisplay:
Use as a quick reference for displaying and exiting 
a window. Can handle fps too
'''
class TestWindowDisplay(unittest.TestCase):
    def testBlankWindow(self):
        print("Hello!")

        # display a window
        pygame.init()
        clock = pygame.time.Clock()  # Clock used for frame rate
        framerate = 60

        isRunning = True
        background = (255, 255, 255)
        mainWindow = pygame.display.set_mode((448, 448))

        pygame.display.update()
        isRunning = True

        # Program is running
        while (isRunning):
            clock.tick(framerate)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    isRunning = False

            # boardRenderer.startGame(mainWindow, 1, framerate)
        pass
