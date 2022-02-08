import pygame
from src.engine import ecs
from src.engine import physics

# from ..ecs import entity -- EXAMPLE OF OTHER WAY

#This function creates a straight line of sprites.
#Window = The current pygame window, sprite = the sprite to paint
#numBlocks = the number of blocks to paint, spriteSize = the size of the sprite (one side)
#Start X/Start Y = The position to start
#up = Boolean, true is vertical platform false is horizontal
def createPlatform(window, sprite, ground, numBlocks, spriteSize, startX, startY, up):

    start = 0
    while(start<numBlocks):
        if(up):
            window.blit(sprite, (startX, startY - (start * spriteSize)))

        else:
            window.blit(sprite, (startX + (start * spriteSize), startY - spriteSize))
        start+=1
    pygame.display.update()
    return window
#staticAsserts = list of entities
#repaint the entities
def clearBG(window, background, staticAssets=None):
    window.fill(background)
    #Repaint assets that belong here
    #Repaint dynamic/moving assets in the main loop
    if staticAssets!=None:
        for asset in staticAssets:
            pass

    pygame.display.update()

# ground can be a list i append objs to

    #This draws the vertical and horizontal bars
    # mainWindow = sceneCreator.createPlatform(mainWindow, grndSprite1, ground, 512/64, 64,0,h, True)
    # mainWindow = sceneCreator.createPlatform(mainWindow, grndSprite1, ground, 512 / 64, 64, 0, h, False)
    # mainWindow = sceneCreator.createPlatform(mainWindow, grndSprite1, ground, 512 / 64, 64, 0, 64, False)
    # mainWindow = sceneCreator.createPlatform(mainWindow, grndSprite1, ground, 512 / 64, 64, w-64, h, True)
    # mainWindow.blit(testImg, (0, 0))  # This draws the person