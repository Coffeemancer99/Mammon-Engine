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
from src.minigame.teamSwimmer import swimmerPlayer as swimmerPlayer
from src.minigame.teamSwimmer import seaItem as seaItem
import random
from src.minigame.timer.timer import timer as timer
from src.minigame.minigameData import minigameData as minigameData

#Daniels code
def removeObj(objects, object):
    if isinstance(object, DynamicObject): object.halt()
    if object in objects:
        objects.remove(object)

def spawnCoin(objects, scale, xPos):

    scaleFancy = 0.05* scale
    coinSprite = spritegen.grab_sprite("data/assets/sprites/goodSprites/coinS.png", scaleFancy)




    coin = seaItem.seaItem(coinSprite, scale, xPos, 0, objects, 2)



    objects.append(coin)



def startGame(mainWindow, scale, framerate, winningPlayers, winnings=10):
    clock = pygame.time.Clock()  # Clock used for frame rate
    windowX, windowY = pygame.display.get_surface().get_size()
    isRunning = True

    scaleFancy = 0.06 * scale

    stage = spritegen.grab_sprite("data/assets/sprites/layers/stage.png", scale)
    seats = spritegen.grab_sprite("data/assets/sprites/layers/seats.png", scale)
    player1Spr = spritegen.grab_sprite("data/assets/sprites/goodSprites/pirateDude.png", scaleFancy)
    player2Spr = spritegen.grab_sprite("data/assets/sprites/goodSprites/pirateDude.png", scaleFancy)
    player3Spr = spritegen.grab_sprite("data/assets/sprites/goodSprites/pirateDude.png", scaleFancy)
    player4Spr = spritegen.grab_sprite("data/assets/sprites/goodSprites/pirateDude.png", scaleFancy)
    objects = []
    pirate1= DynamicObject(player1Spr, scale, windowX/4, windowY/4, objects)
    pirate2 = DynamicObject(player2Spr, scale, windowX / 4 + windowX/8, windowY / 4, objects)
    pirate3 = DynamicObject(player3Spr, scale, windowX / 2, windowY / 4, objects)
    pirate4 = DynamicObject(player4Spr, scale, windowX / 2 + windowX / 8, windowY / 4, objects)

    objects.append(pirate1)
    objects.append(pirate2)
    objects.append(pirate3)
    objects.append(pirate4)
    seq = "data/assets/sounds/Another.mp3"
    ost = pygame.mixer.Sound(seq)
    ost.play(loops=-1)
    players=[pirate1, pirate2, pirate3, pirate4]
    for winningPlayer in winningPlayers:
        dropLoc = players[winningPlayer].x
        spawnCoin(objects, scale, dropLoc)

    while(isRunning):
        clock.tick(framerate)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                isRunning=False
        mainWindow.fill((0, 0, 0))
        mainWindow.blit(seats, (0, 0))
        mainWindow.blit(stage, (0, 0))
        for objectz in objects:  # rendering
            objectz.draw(mainWindow)
        for objectz in objects:  # rendering


            objectz.update()
            if(isinstance(objectz, seaItem.seaItem)):
                objectz.fall()

            if ((abs(objectz.dX) >= 1) or (abs(objectz.dY) >= 1)):
                collisions = physics.velHandler(objectz, objects)
                if(isinstance(objectz, seaItem.seaItem) and collisions!=[]):

                    removeObj(objects, objectz)

        pygame.display.update()