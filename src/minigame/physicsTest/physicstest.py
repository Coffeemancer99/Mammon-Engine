
import src.engine.scenecreator.drawTileMap as drawTileMap
import src.engine.scenecreator.tile as tile
import src.engine.player.playerController as player
import src.engine.collision as collision
import src.engine.physics.physics as physics
import src.engine.physics.terrain as terrain
import src.minigame.physicsTest.ball as ball
import pygame
import time
import math # for dev values
from functools import partial


def startGame(mainWindow, scale, framerate):
    clock = pygame.time.Clock()  # Clock used for frame rate

    coco = ball.Ball(pygame.image.load("data/assets/sprites/bluebox.png"), scale, 80, 185, name="coco")
    lemon = physics.DynamicObject(terrain.generate_ellipse(70,110), scale*1, 100,50, name="lemon")
    box = physics.Object(terrain.generate_circle(50), 1, 20,20, name="box")
    triY = 100; triX = 100
    triangle = terrain.from_polygon([[0,400],[0+triX,400],[0,400-triY]], scale, color = (0,255,0,255))
    # triangle = physics.Object(terrain.generate_rectangle(800, 50), scale, 0, 400)
    objects = [coco, lemon, box, triangle]

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

    while(isRunning):
        clock.tick(framerate)
        mainWindow.fill((0,0,0))


        key = pygame.key.get_pressed()

        if key[pygame.K_w]:
            coco.momY -= 3
        if key[pygame.K_s]:
            coco.momY += 3
        if key[pygame.K_a]:
            coco.momX -= 3
        if key[pygame.K_d]:
            coco.momX += 3
        if key[pygame.K_SPACE]:
            if physics.grounded(coco, objects, onlyStatics=True):
                coco.momY -= 50

        if key[pygame.K_f]:
            coco.angle = math.pi/2
            print("angle = 90")

        if key[pygame.K_g]:
            coco.angle = math.pi/4
            print("angle = 45")
        if key[pygame.K_g]:
            coco.x = 0
        if key[pygame.K_h]:
            isPrimed = True
            print("Primed")
        # if key[pygame.K_h]:
        #     (coco.x, coco.y) = (376, 333)
        #     coco.momX = 0
        #     coco.momY = 0
        #     time.sleep(.3)

        if key[pygame.K_c]:
            coco.momX = 0
            coco.momY = 0

        if key[pygame.K_UP]:
            lemon.momY -= 2
        if key[pygame.K_DOWN]:
            lemon.momY += 2
        if key[pygame.K_LEFT]:
            lemon.momX -= 2
        if key[pygame.K_RIGHT]:
            lemon.momX += 2

        if key[pygame.K_b]:
            print("\n######################################")
            for object in objects:
                print(object)
            print("######################################")
            time.sleep(0.3)

        for object in objects: # Physics, movement
            if isinstance(object, physics.DynamicObject):
                # if object is coco:
                #     coco.momY += 1.5 #gravity
                object.update()
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