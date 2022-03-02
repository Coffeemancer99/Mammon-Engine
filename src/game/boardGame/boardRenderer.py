from board import Board
from pathManager import PathManager
import pygame
from src.engine.scenecreator import tile

class BoardRenderer:
    def __init__(self):
        pass



def getBoardMap():
    boardMap = Board()
    boardMap.generateBoard(14, 14)
    return boardMap


def drawScene(window, tilemap, images):
    window.fill((0, 0, 0))

    for row in range(len(tilemap)):
        for col in range(len(tilemap[0])):
            spriteValue = tilemap[row][col]
            if (spriteValue == 0):
                continue
            currImage = images[spriteValue]
            x = col * currImage.get_width()
            y = row * currImage.get_height()
            window.blit(currImage, (x, y))

    pygame.display.update()

    # Have array corresponds to an img
    # Tilemap is an array of integers that indexes into the array

'''
'''
def generateTiles(board, images):
    staticTiles = []
    for row in range(board.getWidth()):
        for col in range(board.getHeight()):
            spriteValue = board.getObjsAt(row, col)
            if (spriteValue is None):
                continue
            currImage = images[spriteValue]
            x = col * currImage.get_width()
            y = row * currImage.get_height()
            newTile = tile.tile(currImage, x, y)
            staticTiles.append(newTile)

    return staticTiles


'''
'''
def startGame(mainWindow, scale, framerate):
    clock = pygame.time.Clock()  # Clock used for frame rate

    groundSprite = pygame.image.load("D:\Mammon-Engine\data\\assets\sprites\groundSprite1.png")
    groundSprite = pygame.transform.scale(groundSprite, ((groundSprite.get_width()) * scale, (groundSprite.get_height()) * scale))

    images = [None, groundSprite]
    currMap = getBoardMap()
    staticTiles = generateTiles(currMap, images)

    for tile in staticTiles:
        print(tile.rectCol.x, tile.rectCol.y)
    isRunning=True

    while(isRunning):
        clock.tick(framerate)
        # brian.update()

        drawScene(mainWindow, currMap, images) #Redraws the main window
        # mainWindow.blit(brian.sprite, (brian.rect.x, brian.rect.y))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                isRunning=False
        # collision.staticHandler(staticTiles, brian)
        # brian.updateRect()

        pygame.display.update()
