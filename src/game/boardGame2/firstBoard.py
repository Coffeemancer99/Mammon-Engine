from src.game.boardGame2.board import Board
from src.game.boardGame2.tile import Tile
from src.game.boardGame2.spriteLoader import SpriteLoader

'''
Created by: Andrew Bunn
Was hesitant to upload, but it is a critical part of the project.
This setup does not need to be in here.
Will be shoved into a csv file or something of the sort later on
'''


class FirstBoard:

    def __init__(self, scale):
        self.startTile = None
        self.scale = scale
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
        startTile.typeOfTile = "Regular"

        tile2 = Tile(startTile)
        tile2.x += 32
        tile2.y -= 32
        tile2.image = SpriteLoader().loadImage("blueTile.png")
        tile2.typeOfTile = "Regular"

        tile3 = Tile(tile2)
        tile3.x += 32
        tile3.y -= 32
        tile3.typeOfTile = "Regular"

        tile4 = Tile(tile3)
        tile4.x += 32
        tile4.y -= 32
        tile4.typeOfTile = "Regular"

        # Split low right
        tile5 = Tile(tile4)
        tile5.x += 32
        tile5.y += 32
        tile5.typeOfTile = "Regular"

        # Split high
        tile6 = Tile(tile4)
        tile6.x -= 32
        tile6.y -= 32
        tile6.typeOfTile = "Regular"

        # starting from 5 loop
        tile7 = Tile(tile5)
        tile7.x += 32
        tile7.y += 32
        tile7.typeOfTile = "Regular"

        tile8 = Tile(tile7)
        tile8.x += 32
        tile8.typeOfTile = "Bad"

        tile9 = Tile(tile8)
        tile9.x += 32
        tile9.typeOfTile = "Regular"

        tile10 = Tile(tile9)
        tile10.x += 32
        tile10.typeOfTile = "Regular"

        tile11 = Tile(tile10)
        tile11.x += 32
        tile11.y -= 32
        tile11.typeOfTile = "Bad"

        tile12 = Tile(tile11)
        tile12.x += 32
        tile12.y -= 32
        tile12.typeOfTile = "Regular"

        tile13 = Tile(tile12)
        tile13.x -= 32
        tile13.y -= 32
        tile13.typeOfTile = "Regular"

        tile14 = Tile(tile13)
        tile14.x -= 32
        tile14.y -= 32
        tile14.typeOfTile = "Regular"

        tile15 = Tile(tile14)
        tile15.x += 32
        tile15.y -= 32
        tile15.typeOfTile = "Regular"

        tile16 = Tile(tile15)
        tile16.x += 32
        tile16.typeOfTile = "Regular"

        tile17 = Tile(tile16)
        tile17.x += 32
        tile17.typeOfTile = "Regular"

        tile18 = Tile(tile17)
        tile18.x += 32
        tile18.typeOfTile = "Regular"

        tile19 = Tile(tile18)
        tile19.x += 32
        tile19.y -= 32
        tile19.typeOfTile = "Regular"

        tile20 = Tile(tile19)
        tile20.x -= 32
        tile20.y -= 32
        tile20.typeOfTile = "Bad"

        tile21 = Tile(tile20)
        tile21.y -= 32
        tile21.typeOfTile = "Regular"

        tile22 = Tile(tile21)
        tile22.x -= 32
        tile22.y -= 32
        tile22.typeOfTile = "Regular"

        tile23 = Tile(tile22)
        tile23.y -= 32
        tile23.typeOfTile = "Regular"

        tile24 = Tile(tile23)
        tile24.x -= 32
        tile24.y -= 32
        tile24.typeOfTile = "Dual"

        tile25 = Tile(tile24)
        tile25.x -= 32
        tile25.y += 32
        tile25.typeOfTile = "Regular"

        tile26 = Tile(tile25)
        tile26.y += 32
        tile26.typeOfTile = "Regular"

        tile27 = Tile(tile26)
        tile27.x -= 32
        tile27.y += 32
        tile27.typeOfTile = "Regular"

        tile28 = Tile(tile27)
        tile28.x -= 32
        tile28.y += 32
        tile28.typeOfTile = "Bad"

        tile29 = Tile(tile28)
        tile29.x -= 32
        tile29.typeOfTile = "Regular"

        tile30 = Tile(tile29)
        tile30.x -= 32
        tile30.typeOfTile = "Store"

        tile31 = Tile(tile30)
        tile31.x -= 32
        tile31.typeOfTile = "Regular"

        tile32 = Tile(tile31)
        tile32.x -= 32
        tile32.y += 32
        tile32.typeOfTile = "Regular"

        tile33 = Tile(tile32)
        tile33.x -= 32
        tile33.y += 32
        tile33.typeOfTile = "Regular"

        tile34 = Tile(tile33)
        tile34.y += 32
        tile34.typeOfTile = "Dual"

        tile35 = Tile(tile4)
        tile35.x += 32
        tile35.y -= 32
        tile35.typeOfTile = "Store"

        tile36 = Tile(tile35)
        tile36.x += 32
        tile36.y -= 32
        tile36.typeOfTile = "Regular"

        tile37 = Tile(tile36)
        tile37.x += 32
        tile37.typeOfTile = "Regular"

        tile38 = Tile(tile37)
        tile38.x += 32
        tile38.typeOfTile = "Regular"

        # make split path tiles red for now
        tile4.image = SpriteLoader().loadImage("redTile.png")
        tile14.image = SpriteLoader().loadImage("redTile.png")

        # Create the path
        startTile.addNextTile(tile2)
        tile2.addNextTile(tile3)
        tile3.addNextTile(tile4)
        tile4.addNextTile(tile5)
        # tile4.addNextTile(tile6)
        tile5.addNextTile(tile7)
        tile6.addNextTile(tile4)
        tile7.addNextTile(tile8)
        tile8.addNextTile(tile9)
        tile9.addNextTile(tile10)
        tile10.addNextTile(tile11)
        tile11.addNextTile(tile12)
        tile12.addNextTile(tile13)
        tile13.addNextTile(tile14)
        tile14.addNextTile(tile15)
        tile15.addNextTile(tile16)
        tile16.addNextTile(tile17)
        tile17.addNextTile(tile18)
        tile18.addNextTile(tile19)
        tile19.addNextTile(tile20)
        tile20.addNextTile(tile21)
        tile21.addNextTile(tile22)
        tile22.addNextTile(tile23)
        tile23.addNextTile(tile24)
        tile24.addNextTile(tile25)
        tile25.addNextTile(tile26)
        tile26.addNextTile(tile27)
        tile27.addNextTile(tile28)
        tile28.addNextTile(tile29)
        tile29.addNextTile(tile30)
        tile30.addNextTile(tile31)
        tile31.addNextTile(tile32)
        tile32.addNextTile(tile33)
        tile33.addNextTile(tile34)
        tile34.addNextTile(tile6)
        tile4.addNextTile(tile35)
        tile35.addNextTile(tile36)
        tile36.addNextTile(tile37)
        tile37.addNextTile(tile38)
        tile38.addNextTile(tile14)

        # Set up previous tiles
        tile2.addPrevTile(startTile)
        tile3.addPrevTile(tile2)
        tile4.addPrevTile(tile3)
        tile4.addPrevTile(tile6)
        tile5.addPrevTile(tile4)
        tile6.addPrevTile(tile34)
        tile7.addPrevTile(tile5)
        tile8.addPrevTile(tile7)
        tile9.addPrevTile(tile8)
        tile10.addPrevTile(tile9)
        tile11.addPrevTile(tile10)
        tile12.addPrevTile(tile11)
        tile13.addPrevTile(tile12)
        tile14.addPrevTile(tile13)
        tile14.addPrevTile(tile38)
        tile15.addPrevTile(tile14)
        tile16.addPrevTile(tile15)
        tile17.addPrevTile(tile16)
        tile18.addPrevTile(tile17)
        tile19.addPrevTile(tile18)
        tile20.addPrevTile(tile19)
        tile21.addPrevTile(tile20)
        tile22.addPrevTile(tile21)
        tile23.addPrevTile(tile22)
        tile24.addPrevTile(tile23)
        tile25.addPrevTile(tile24)
        tile26.addPrevTile(tile25)
        tile27.addPrevTile(tile26)
        tile28.addPrevTile(tile27)
        tile29.addPrevTile(tile28)
        tile30.addPrevTile(tile29)
        tile31.addPrevTile(tile30)
        tile32.addPrevTile(tile31)
        tile33.addPrevTile(tile32)
        tile34.addPrevTile(tile6)  # left off
        tile35.addPrevTile(tile4)
        tile36.addPrevTile(tile35)
        tile37.addPrevTile(tile36)
        tile38.addPrevTile(tile37)

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
        # renderer = BoardRenderer(board)
        return board
