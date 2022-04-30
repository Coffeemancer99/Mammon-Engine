import src.engine.physics.physics as physics
import src.engine.physics.terrain as terrain
from src.engine.physics.physics import Object, DynamicObject, RectObject
from src.engine.graphics.spritegen import *
from src.engine.player.playerController import *
from src.engine.player.controls import *
from src.minigame.dodgePanic.cannon import *
from src.minigame.physicsTest.testing import *
import src.minigame.physicsTest.testing as testing
import pygame
import time
import math




def removeObj(object):
    objects = object.objects
    if isinstance(object, DynamicObject): object.halt()
    if object in objects: objects.remove(object)
    else:
        print("ERROR: Object ",object,"\n\t not found in objects!")


def generateSprite(name, scale, width = None, offset = 0): # offset = how far to raise the platform to meet the sprite
    boxHeight = 20*scale
    baseSprite = grab_sprite(name, scale)
    if not width: width = int(2.0*baseSprite.get_width())
    height =  baseSprite.get_height() + boxHeight
    box = generate_rectangle(width, boxHeight + offset, 1) # scaling already performed in width and height
    toReturn = pygame.Surface((width, height), flags=pygame.SRCALPHA)
    toReturn.blit(baseSprite, (int(.5*width - .5*baseSprite.get_width()),0))
    toReturn.blit(box, (0,height - boxHeight - offset))
    return toReturn

def swapControls(p1, p2):
    assert isinstance(p1, Player) and isinstance(p2, Player)
    print("Swapping controls between {} and {}".format(p1.name, p2.name))
    backup = p1.controls
    p1.controls =  p2.controls
    p2.controls = backup

def startGame(mainWindow, scale, framerate):
    gravity = 1.5
    objects = []
    clock = pygame.time.Clock()  # Clock used for frame rate

    p1 = Platformer(grab_sprite("data/assets/sprites/bigTestPlayer1.png", scale/4), scale, 0,0, objects, 3, 50, name = "p1", controls = twoPlayer[0])
    p2 = CannonX(generateSprite("data/assets/sprites/bigTestPlayer2.png", scale/4), scale, 0, 0, objects, 5, .01, name = "p2", controls = None)
    p3 = CannonY(generateSprite("data/assets/sprites/bigTestPlayer3.png", scale/4), scale, 0, 0, objects, .01, 5, name = "p3", controls = twoPlayer[1])
    p4 = CannonY(generateSprite("data/assets/sprites/bigTestPlayer4.png", scale/4), scale, 0, 0, objects, .01, 5, name = "p4", controls = None)

    def takeInputs(key): # inputs not associated with an object
        nonlocal gravity

        if key[pygame.K_g]:
            gravity -= .1
            print("gravity = {:.3f}".format(gravity))
            time.sleep(.3)
        if key[pygame.K_b]:
            print("\n######################################")
            for object in objects:
                print(object)
            print("######################################")
            time.sleep(0.3)
        if key[pygame.K_t]:
            gravity += .1
            print("gravity = {:.3f}".format(gravity))
            time.sleep(.3)
        if key[pygame.K_n]:
            print("gravity = 0")
            gravity = 0
            time.sleep(.3)
        if key[pygame.K_u]:
            print("Setting up...")
            setupBounce()
            time.sleep(.3)
        if key[pygame.K_f]:
            swapControls(p1, p2)
            time.sleep(.3)
        if key[pygame.K_g]:
            swapControls(p3, p4)
            time.sleep(.3)

        if key[pygame.K_h]:
            for object in objects:
                if isinstance(object, DynamicObject):
                    object.halt()

    def addRect(position, dimensions, frict = physics.frictS, color = (180,180,180), scale = scale, objects = objects, bounce = 0):
        objects.append(RectObject(dimensions, scale, position[0], position[1], objects, frict, color = color, bounce = bounce))

    def setup():
        nonlocal gravity
        objects.clear()
        gravity = 1.8


        # addRect((120,50), (50,200), bounce = .8) # wall1
        # addRect((300,50), (50,200), bounce = .8) # wall2

        addRect((200, 300), (180,20)) # floor in middle
        for object in [p1, p2, p3, p4]:
            object.halt()
            if isinstance(object, Cannon):
                object.angle = object.minAngle
                object.power = 0
            objects.append(object)
        (p1.x, p1.y) = (250, 200)
        (p2.x, p2.y) = (250, 100)
        (p3.x, p3.y) = (100, 200)
        (p4.x, p4.y) = (350, 200)

    setup()

    isRunning=True
    while(isRunning):
        clock.tick(framerate)
        mainWindow.fill((20,20,20)) # wipes the screen
        takeInputs(pygame.key.get_pressed()) # inputs not associated with an object

        for object in objects: # Physics, movement
            if isinstance(object, physics.Dynamic):
                if isinstance(object, Platformer):
                    object.momY += gravity
                object.update(airRes = 2*physics.airRes)
                if ((abs(object.dX) >= 1) or (abs(object.dY) >= 1)):
                    physics.velHandler(object, objects)

        for object in objects: # rendering
            object.draw(mainWindow)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                isRunning=False
        pygame.display.update()




def main():
    pass

if(__name__ == "__main__"):
    main()