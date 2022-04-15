import math
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

def startGame(mainWindow, scale, framerate):
    clock = pygame.time.Clock()  # Clock used for frame rate
    windowX, windowY = pygame.display.get_surface().get_size()
    isRunning = True
    gravity = 2.0 * scale

    scaleFancy = 0.0375 * scale
    subSprite = spritegen.grab_sprite("data/assets/sprites/goodSprites/barrelSub.png", scaleFancy)

    bg1 = spritegen.grab_sprite("data/assets/sprites/layers/layer1.png", scale)
    bg2 = spritegen.grab_sprite("data/assets/sprites/layers/layer2.png", scale)
    bg = [bg1, bg2]

    vertSprite = spritegen.grab_sprite("data/assets/sprites/barVert.png", scale)
    horSprite = spritegen.grab_sprite("data/assets/sprites/horVert.png", scale)
    team1X = 50
    team1Y = 50
    team2X = 200
    team2Y = 50

    #The controls for team 1
    #This is the player who moves the sub left and right
    team1AControls = {
        "left": pygame.K_a,
        "right": pygame.K_d
    }
    #This is the player who controls the depth
    team1BControls = {
        "up": pygame.K_w
    }

    #The controls for team 2
    #This is the player who moves the sub left and right
    team2AControls = {
        "left": pygame.K_LEFT,
        "right": pygame.K_RIGHT
    }
    #This is the player who controls the depth
    team2BControls = {
        "up": pygame.K_UP
    }
    objects = []
    team1Sub = swimmerPlayer.swimmerPlayer(subSprite, scale, team1X, team1Y, objects, team1AControls, team1BControls)
    team2Sub = swimmerPlayer.swimmerPlayer(subSprite, scale, team2X, team2Y, objects, team2AControls, team2BControls)

    vert1 = DynamicObject(vertSprite, scale, -1, 0, objects)
    vert2 = DynamicObject(vertSprite, scale, windowX, 0, objects)
    hor1 = DynamicObject(horSprite, scale, 0, -1, objects)
    hor2 = DynamicObject(horSprite, scale, 0, windowY, objects)
    objects.append(team1Sub)
    objects.append(team2Sub)
    objects.append(vert1)
    objects.append(vert2)
    objects.append(hor1)
    objects.append(hor2)
    while(isRunning):
        clock.tick(framerate)
        primedInputs = []
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                isRunning=False
            #Get every time the button is held up (Prevent holding down the button)_
            if event.type == pygame.KEYUP:
                primedInputs.append(event)
        #if(len(primedInputs)>0):
            #print(primedInputs[0].key)

        mainWindow.fill((0, 0, 0))
        mainWindow.blit(bg1, (0,0))
        for objectz in objects:
            mainWindow.blit(objectz.sprite, (objectz.x, objectz.y))
        mainWindow.blit(bg2, (0, 0))
        for objectz in objects:
            if(isinstance(objectz, swimmerPlayer.swimmerPlayer)):
                objectz.update(maxMom = 150)
                objectz.floatSub(primedInputs)
                if ((abs(objectz.dX) >= 1) or (abs(objectz.dY) >= 1)):
                    physics.velHandler(objectz, objects)
        pygame.display.update()
