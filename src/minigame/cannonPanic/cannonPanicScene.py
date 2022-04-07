from src.minigame.physicsTest import ball as ball
import pygame
from src.engine.physics.physics import Object, DynamicObject, RectObject, DynamicRect
import src.engine.physics.spritegen as spritegen

def startGame(mainWindow, scale, framerate):
    clock = pygame.time.Clock()  # Clock used for frame rate
    windowX, windowY = pygame.display.get_surface().get_size()
    isRunning = True
    gravity = 1.5
    cocoX = 25;
    cocoY = 20
    cocoSprite = pygame.image.load("data/assets/sprites/goodSprites/coconut.png")
    scaleFancy = 0.05 * scale
    cocoSprite = pygame.transform.scale(cocoSprite, ((cocoSprite.get_width()) * scaleFancy, (cocoSprite.get_height()) * scaleFancy))
    coco = ball.Ball(cocoSprite, scale, cocoX, cocoY, name="coco", mass=4, maxpower=80)
    objects = [coco]
    while(isRunning):
        mainWindow.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                isRunning=False
        for object in objects: # rendering
            object.draw(mainWindow)

        pygame.display.update()