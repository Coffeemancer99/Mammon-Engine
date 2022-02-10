import pygame
import src.engine.scenecreator.tile as tile
def drawScene(window, tilemap, images):

    window.fill((0, 0, 0))

    for row in range(len(tilemap)):
        for col in range(len(tilemap[0])):
            spriteValue = tilemap[row][col]
            if(spriteValue==0):
                continue
            currImage = images[spriteValue]
            x = col * currImage.get_width()
            y = row * currImage.get_height()
            window.blit(currImage, (x, y))

    pygame.display.update()

    #Have array corresponds to an img
    #Tilemap is an array of integers that indexes into the array

def generateTiles(tilemap, images):
    staticTiles = []
    for row in range(len(tilemap)):
        for col in range(len(tilemap[0])):
            spriteValue = tilemap[row][col]
            if(spriteValue==0):
                continue
            currImage = images[spriteValue]
            x = col * currImage.get_width()
            y = row * currImage.get_height()
            newTile = tile.tile(currImage, x, y)
            staticTiles.append(newTile)

    return staticTiles
