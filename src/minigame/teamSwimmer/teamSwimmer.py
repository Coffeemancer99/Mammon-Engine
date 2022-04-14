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


def startGame(mainWindow, scale, framerate):
    clock = pygame.time.Clock()  # Clock used for frame rate
    windowX, windowY = pygame.display.get_surface().get_size()
    isRunning = True
    gravity = 2.0 * scale
    scaleFancy = 0.05 * scale
    
    while(isRunning):
        clock.tick(framerate)
        mainWindow.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                isRunning=False

        pygame.display.update()
