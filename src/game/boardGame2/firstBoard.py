from src.game.boardGame2.boardRenderer import BoardRenderer
from src.game.boardGame2.board import Board
from src.game.boardGame2.tile import Tile
from src.game.boardGame2.spriteLoader import SpriteLoader
from src.game.boardGame2.player import Player


'''
Created by: Andrew Bunn
Was hesitant to upload, but it is a critical part of the project.
This setup does not need to be in here.
Will be shoved into a csv file or something of the sort later on
Use pandas to manipulate data?
'''

class FirstBoard():

    def __init__(self):
        self.startTile = None
        pass

    def testFirstBoard(self):
        """
        The first game board everyone will work with
        Consists of 38 tiles, and a couple split paths
        No previous tiles hooked up yet (can't walk backward)

        :return: returns the instantiated board filled with tiles
        """

        startTile = Tile()
        startTile.x = 0
        startTile.y = 416
        startTile.width = 32
        startTile.height = 32
        startTile.image = SpriteLoader().loadImage("blueTile.png")

        tile2 = Tile(startTile)
        tile2.x += 32
        tile2.y -= 32
        tile2.image = SpriteLoader().loadImage("blueTile.png")

        tile3 = Tile(tile2)
        tile3.x += 32
        tile3.y -= 32

        tile4 = Tile(tile3)
        tile4.x += 32
        tile4.y -= 32

        # Split low right
        tile5 = Tile(tile4)
        tile5.x += 32
        tile5.y += 32

        # Split high
        tile6 = Tile(tile4)
        tile6.x -= 32
        tile6.y -= 32

        # starting from 5 loop
        tile7 = Tile(tile5)
        tile7.x += 32
        tile7.y += 32

        tile8 = Tile(tile7)
        tile8.x += 32

        tile9 = Tile(tile8)
        tile9.x += 32

        tile10 = Tile(tile9)
        tile10.x += 32

        tile11 = Tile(tile10)
        tile11.x += 32
        tile11.y -= 32

        tile12 = Tile(tile11)
        tile12.x += 32
        tile12.y -= 32

        tile13 = Tile(tile12)
        tile13.x -= 32
        tile13.y -= 32

        tile14 = Tile(tile13)
        tile14.x -= 32
        tile14.y -= 32


        tile15 = Tile(tile14)
        tile15.x += 32
        tile15.y -= 32

        tile16 = Tile(tile15)
        tile16.x += 32

        tile17 = Tile(tile16)
        tile17.x += 32

        tile18 = Tile(tile17)
        tile18.x += 32

        tile19 = Tile(tile18)
        tile19.x += 32
        tile19.y -= 32

        tile20 = Tile(tile19)
        tile20.x -= 32
        tile20.y -= 32

        tile21 = Tile(tile20)
        tile21.y -= 32

        tile22 = Tile(tile21)
        tile22.x -= 32
        tile22.y -= 32

        tile23 = Tile(tile22)
        tile23.y -= 32

        tile24 = Tile(tile23)
        tile24.x -= 32
        tile24.y -= 32

        tile25 = Tile(tile24)
        tile25.x -= 32
        tile25.y += 32

        tile26 = Tile(tile25)
        tile26.y += 32

        tile27 = Tile(tile26)
        tile27.x -= 32
        tile27.y += 32

        tile28 = Tile(tile27)
        tile28.x -= 32
        tile28.y += 32

        tile29 = Tile(tile28)
        tile29.x -= 32

        tile30 = Tile(tile29)
        tile30.x -= 32

        tile31 = Tile(tile30)
        tile31.x -= 32

        tile32 = Tile(tile31)
        tile32.x -= 32
        tile32.y += 32

        tile33 = Tile(tile32)
        tile33.x -= 32
        tile33.y += 32

        tile34 = Tile(tile33)
        tile34.y += 32

        tile35 = Tile(tile4)
        tile35.x += 32
        tile35.y -= 32

        tile36 = Tile(tile35)
        tile36.x += 32
        tile36.y -= 32

        tile37 = Tile(tile36)
        tile37.x += 32

        tile38 = Tile(tile37)
        tile38.x += 32

        # make split path tiles red
        tile4.image = SpriteLoader().loadImage("redTile.png")
        tile14.image = SpriteLoader().loadImage("redTile.png")

        # Create the path
        startTile.nextTiles.append(tile2)
        tile2.nextTiles.append(tile3)
        tile3.nextTiles.append(tile4)
        tile4.nextTiles.append(tile5)
        tile4.nextTiles.append(tile6)
        tile5.nextTiles.append(tile7)
        tile6.nextTiles.append(tile4)
        tile7.nextTiles.append(tile8)
        tile8.nextTiles.append(tile9)
        tile9.nextTiles.append(tile10)
        tile10.nextTiles.append(tile11)
        tile11.nextTiles.append(tile12)
        tile12.nextTiles.append(tile13)
        tile13.nextTiles.append(tile14)
        tile14.nextTiles.append(tile15)
        tile15.nextTiles.append(tile16)
        tile16.nextTiles.append(tile17)
        tile17.nextTiles.append(tile18)
        tile18.nextTiles.append(tile19)
        tile19.nextTiles.append(tile20)
        tile20.nextTiles.append(tile21)
        tile21.nextTiles.append(tile22)
        tile22.nextTiles.append(tile23)
        tile23.nextTiles.append(tile24)
        tile24.nextTiles.append(tile25)
        tile25.nextTiles.append(tile26)
        tile26.nextTiles.append(tile27)
        tile27.nextTiles.append(tile28)
        tile28.nextTiles.append(tile29)
        tile29.nextTiles.append(tile30)
        tile30.nextTiles.append(tile31)
        tile31.nextTiles.append(tile32)
        tile32.nextTiles.append(tile33)
        tile33.nextTiles.append(tile34)
        tile34.nextTiles.append(tile6)
        tile4.nextTiles.append(tile35)
        tile35.nextTiles.append(tile36)
        tile36.nextTiles.append(tile37)
        tile37.nextTiles.append(tile38)
        tile38.nextTiles.append(tile14)

        # put all tiles in the board
        board = Board()
        board.addTile(startTile)
        board.addTile(tile2)
        board.addTile(tile3)
        board.addTile(tile4)
        board.addTile(tile5)
        board.addTile(tile6)
        board.addTile(tile7)
        board.addTile(tile8)
        board.addTile(tile9)
        board.addTile(tile10)
        board.addTile(tile11)
        board.addTile(tile12)
        board.addTile(tile13)
        board.addTile(tile14)
        board.addTile(tile15)
        board.addTile(tile16)
        board.addTile(tile17)
        board.addTile(tile18)
        board.addTile(tile19)
        board.addTile(tile20)
        board.addTile(tile21)
        board.addTile(tile22)
        board.addTile(tile23)
        board.addTile(tile24)
        board.addTile(tile25)
        board.addTile(tile26)
        board.addTile(tile27)
        board.addTile(tile28)
        board.addTile(tile29)
        board.addTile(tile30)
        board.addTile(tile31)
        board.addTile(tile32)
        board.addTile(tile33)
        board.addTile(tile34)
        board.addTile(tile35)
        board.addTile(tile36)
        board.addTile(tile37)
        board.addTile(tile38)

        board.startTile = startTile
        renderer = BoardRenderer(board)
        return board
