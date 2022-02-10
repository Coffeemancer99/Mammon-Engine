import pygame
import math
import time
from src.engine.menus import testgame


def startGame(mainWindow, scale, framerate):
    clock = pygame.time.Clock()  # Clock used for frame rate
    #TEST IMAGES
    groundSprite = pygame.image.load("../../data/assets/sprites/groundSprite1.png")
    groundSprite = pygame.transform.scale(groundSprite, ((groundSprite.get_width()) * scale, (groundSprite.get_height()) * scale))

    images = [None, groundSprite]
    #currMap = getGameMap()
    #drawTileMap.drawScene(mainWindow, currMap, images)

    isRunning=True
    while(isRunning):
        clock.tick(framerate)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                isRunning=False
            pos = pygame.mouse.get_pos()
            # new game button
            if (pos[1] < 112 * scale and pos[1] >= 0):
                print("Turns")
                return testgame.startGame(mainWindow, scale, framerate)

                # return
            # Settings button
            if (pos[1] > 112 * scale and pos[1] < 224 * scale):
                print("Map 1")
                #return settings.launch(width, height, framerate, mainWindow, scale)