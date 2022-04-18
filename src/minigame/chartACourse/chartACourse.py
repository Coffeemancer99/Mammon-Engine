import math
import time

import src.minigame.physicsTest.ball as ball
import src.minigame.cannonPanic.cannonPanicController as cannonPlayer
import pygame
from src.engine.physics.physics import Object, DynamicObject, RectObject, DynamicRect
import src.engine.physics.spritegen as spritegen
import src.engine.physics.physics as physics
import src.minigame.cannonPanic.playerController as player
import src.minigame.cannonPanic.cannonball as cannonball
import src.engine.scenecreator.tile as tile
import src.engine.scenecreator.drawTileMap as tilemap
from src.minigame.chartACourse.patientPlayer import patientPlayer
from src.minigame.teamSwimmer import swimmerPlayer as swimmerPlayer
from src.minigame.teamSwimmer import seaItem as seaItem
import random
from src.minigame.timer.timer import timer as timer
from src.minigame.minigameData import minigameData as minigameData
from src.minigame.winScreen import winScreen as winScreen

def startGame(mainWindow, scale, framerate):
    clock = pygame.time.Clock()  # Clock used for frame rate
    windowX = mainWindow.get_width()  # Dimensions of window
    windowY = mainWindow.get_height()
    isRunning = True  # Determines if the main game loop is running
    gravity = 2.0 * scale
    scaleFancy = 0.0375 * scale  # A smaller scale for the giant fancy sprites


    # Load game assets and set up starting posiitons
    player1Spr = spritegen.grab_sprite("data/assets/sprites/goodSprites/pirateDude.png", scaleFancy)
    player2Spr = spritegen.grab_sprite("data/assets/sprites/goodSprites/pirateDude.png", scaleFancy)
    player3Spr = spritegen.grab_sprite("data/assets/sprites/goodSprites/pirateDude.png", scaleFancy)
    player4Spr = spritegen.grab_sprite("data/assets/sprites/goodSprites/pirateDude.png", scaleFancy)

    maps = []
    for i in range(1,9):
        currMap = spritegen.grab_sprite("data/assets/sprites/map"+str(i)+".png", scale*2)
        maps.append(currMap)

    #Refactored code. Original : Updated is in the for loop
    # map1 = spritegen.grab_sprite("data/assets/sprites/map1.png", scale)
    # map2 = spritegen.grab_sprite("data/assets/sprites/map2.png", scale)
    # map3 = spritegen.grab_sprite("data/assets/sprites/map3.png", scale)
    # map4 = spritegen.grab_sprite("data/assets/sprites/map4.png", scale)
    # map5 = spritegen.grab_sprite("data/assets/sprites/map5.png", scale)
    # map6 = spritegen.grab_sprite("data/assets/sprites/map6.png", scale)
    # map7 = spritegen.grab_sprite("data/assets/sprites/map7.png", scale)
    # map8 = spritegen.grab_sprite("data/assets/sprites/map8.png", scale)
    # maps.append(map1)
    # maps.append(map2)
    # maps.append(map3)
    # maps.append(map4)
    # maps.append(map5)
    # maps.append(map6)
    # maps.append(map7)
    # maps.append(map8)






    randomMap = random.randint(0,7)

    targetMapSprite = maps[randomMap]

    mapXPos = windowX/2 - targetMapSprite.get_width()/2
    mapYPos = windowY/2 - targetMapSprite.get_height()/2

    waterSpr = spritegen.grab_sprite("data/assets/sprites/layers/waterTop.png", scale)
    objects = []
    print("WindowX/4 is %s" %str(windowX/4))
    pirate1X = (windowX/4) - (player1Spr.get_width()/2)
    pirate1Y = (windowY/4) - (player1Spr.get_height()/2)

    pirate2X = windowX - (windowX/4) -(player2Spr.get_width()/2)
    pirate2Y = (windowY/4) - (player2Spr.get_height()/2)

    pirate3X = (windowX/4) - (player1Spr.get_width()/2)
    pirate3Y = windowY - (windowY/4) - (player3Spr.get_width())

    pirate4X = windowX - (windowX/4) -(player2Spr.get_width()/2)
    pirate4Y = windowY - (windowY/4) - (player3Spr.get_width())

    pirate1= patientPlayer(player1Spr, scale, pirate1X, pirate1Y, objects)
    pirate2 = patientPlayer(player2Spr, scale, pirate2X, pirate2Y, objects)
    pirate3 = patientPlayer(player3Spr, scale, pirate3X, pirate3Y, objects)
    pirate4 = patientPlayer(player4Spr, scale, pirate4X, pirate4Y, objects)

    groundSprite = spritegen.grab_sprite("data/assets/sprites/standBlock.png", scale*0.80)


    # pirate2 = DynamicObject(player2Spr, scale, windowX / 4 + windowX/8, windowY / 4, objects)
    # pirate3 = DynamicObject(player3Spr, scale, windowX / 2, windowY / 4, objects)
    # pirate4 = DynamicObject(player4Spr, scale, windowX / 2 + windowX / 8, windowY / 4, objects)
    objects.append(pirate1)
    objects.append(pirate2)
    objects.append(pirate3)
    objects.append(pirate4)


    while(isRunning):
        clock.tick(framerate)
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                isRunning = False
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                print("THE POS IS %s" %str(pos))

        mainWindow.fill((0, 0, 0))
        mainWindow.blit(waterSpr, (0,0))
        mainWindow.blit(targetMapSprite, (mapXPos, mapYPos))

        for actors in objects:
            if(isinstance(actors, patientPlayer)):
                mainWindow.blit(groundSprite, (actors.x-actors.sprite.get_width()/2, actors.y+actors.sprite.get_height()/2))
            mainWindow.blit(actors.sprite, (actors.x, actors.y))




        pygame.display.update()