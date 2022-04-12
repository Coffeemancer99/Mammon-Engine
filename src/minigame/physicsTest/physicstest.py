from collections.abc import Iterable
import src.engine.scenecreator.drawTileMap as drawTileMap
import src.engine.scenecreator.tile as tile
import src.engine.player.playerController as player
import src.engine.collision as collision
import src.engine.physics.physics as physics
from src.engine.physics.physics import Object, DynamicObject, RectObject, DynamicRect
from src.engine.physics.spritegen import *
import src.engine.physics.terrain as terrain
import src.minigame.physicsTest.ball as ball
import pygame
import time
import logging
import math # for dev values
from functools import partial

def removeObj(objects, object):
    if isinstance(object, DynamicObject): object.halt()
    if object in objects: objects.remove(object)

def startGame(mainWindow, scale, framerate):
    clock = pygame.time.Clock()  # Clock used for frame rate

    objects = []
    cocoX = 25; cocoY = 20
    coco = ball.Ball(generate_circle(20,1), scale, cocoX, cocoY, name="coco", mass = 4, maxpower = 80)
    lemonX = 100; lemonY = 50
    lemon = DynamicRect(generate_ellipse(45,65,1), scale*1, lemonX,lemonY, name="lemon")
    triY = 30; triX = 55
    triangle = terrain.from_polygon([[20,345],[20+triX,311],[20,311-triY]], scale, color = (0,255,0,255), name="triangle")

    # objects.append(lemon)
    objects.append(triangle)
    objects.append(coco)

    objects.append(RectObject((500,50), scale, 100,400))
    objects.append(RectObject((50, 200), scale, 300, 50))
    print("######")
    for object in objects:
        print(object)
    print("######\n")
    isRunning=True
    print("\n-----------------------------------------------")
    print("PHYSICS TESTING")
    print("-----------------------------------------------")
    print("press u-i-o-j-k to manipulate the cannon settings")
    print("WASD and arrow keys to move around coconut and lemon,space to jump the coconut")

    gravity = 1.5
    isLoud = False
    while(isRunning):
        clock.tick(framerate)
        mainWindow.fill((0,0,0))


        key = pygame.key.get_pressed()

        if key[pygame.K_w]:
            coco.momY -= 3
            if key[pygame.K_LSHIFT]:
                coco.momY -= 3
        if key[pygame.K_s]:
            coco.momY += 3
            if key[pygame.K_LSHIFT]:
                coco.momY += 7
        if key[pygame.K_a]:
            coco.momX -= 2
            if key[pygame.K_LSHIFT]:
                coco.momX -= 4
        if key[pygame.K_d]:
            coco.momX += 2
            if key[pygame.K_LSHIFT]:
                coco.momX += 4
        if key[pygame.K_SPACE]:
            if physics.grounded(coco, objects, onlyStatics=True):
                coco.momY -= 50

        if key[pygame.K_f]:
            coco.x = cocoX; coco.y = cocoY
            coco.momX = 0; coco.momY = 0
            lemon.x = lemonX; lemon.y = lemonY
            lemon.momX = 0; lemon.momY = 0
        if key[pygame.K_g]:
            if key[pygame.K_LSHIFT]:
                gravity -= .5
            if key[pygame.K_LCTRL]:
                gravity -= .05
            if not (key[pygame.K_LCTRL] or key[pygame.K_LSHIFT]):
                gravity -= .1
            print("gravity = {:.3f}".format(gravity))
            time.sleep(.3)
        if key[pygame.K_t]:
            if key[pygame.K_LSHIFT]:
                gravity += .5
            if key[pygame.K_LCTRL]:
                gravity += .05
            if not (key[pygame.K_LCTRL] or key[pygame.K_LSHIFT]):
                gravity += .1
            print("gravity = {:.3f}".format(gravity))
            time.sleep(.3)
        if key[pygame.K_h]:
            coco.prime()
            time.sleep(.3)
        if key[pygame.K_n]:
            print("gravity = 0")
            gravity = 0
            time.sleep(.3)
        #     coco.momX = 0
        #     coco.momY = 0
        #     time.sleep(.3)



        if key[pygame.K_UP]:
            lemon.momY -= .8
        if key[pygame.K_DOWN]:
            lemon.momY += .8
        if key[pygame.K_LEFT]:
            lemon.momX -= .8
        if key[pygame.K_RIGHT]:
            lemon.momX += .8

        if key[pygame.K_b]:
            print("\n######################################")
            for object in objects:
                print(object)
            print("######################################")
            time.sleep(0.3)

        for object in objects: # Physics, movement
            if isinstance(object, physics.Dynamic):
                if object is coco:
                    coco.momY += gravity #gravity
                if (object is coco) and key[pygame.K_c]:
                    coco.halt()
                if (object is lemon) and key[pygame.K_v]:
                    lemon.halt()
                object.update(maxMom = 150)
                # if(isLoud and (object is coco)): print(coco)
                if ((abs(object.dX) >= 1) or (abs(object.dY) >= 1)):
                    physics.velHandler(object, objects)
        # if physics.grounded(coco, objects):
        #     if isPrimed and (coco.power == 0):
        #         pass

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