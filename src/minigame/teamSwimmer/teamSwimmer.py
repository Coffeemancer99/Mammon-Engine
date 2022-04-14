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
    scaleFancy = 0.05 * scale

    subSprite = pygame.image.load("data/assets/sprites/goodSprites/barrelSub.png")
    team1X = 50
    team1Y = 50
    team2X = 200
    team2Y = 50

    team1AControls = {
        "left": pygame.K_a,
        "right": pygame.K_d
    }

    team1BControls = {
        "up": pygame.K_w,
    }

    team2AControls = {
        "left": pygame.K_LEFT,
        "right": pygame.K_RIGHT
    }

    team2BControls = {
        "up": pygame.K_UP,
    }
    objects = []
    team1Sub = swimmerPlayer.swimmerPlayer(subSprite, scale, team1X, team1Y, objects, team1AControls, team1BControls)
    team2Sub = swimmerPlayer.swimmerPlayer(subSprite, scale, team2X, team2Y, objects, team2AControls, team2BControls)

    while(isRunning):
        clock.tick(framerate)
        mainWindow.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                isRunning=False

        pygame.display.update()
