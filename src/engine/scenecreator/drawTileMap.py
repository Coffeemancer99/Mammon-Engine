import pygame

def drawScene(window, tilemap, images):
    window.fill((0, 0, 0))
    for row in range(len(tilemap)):
        for col in range(len(tilemap[0])):
            spriteValue = tilemap[row][col]
            if(spriteValue==0):
                continue
            currImage = images[spriteValue]
            window.blit(currImage, (col * currImage.get_width(), row * currImage.get_height()))
    pygame.display.update()
    #Have array corresponds to an img
    #Tilemap is an array of integers that indexes into the array
