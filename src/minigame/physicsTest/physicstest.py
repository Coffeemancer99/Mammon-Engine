import src.engine.physics.physics as physics
from src.engine.physics.physics import Object, DynamicObject, RectObject
from src.engine.graphics.spritegen import *
import src.minigame.exampleGame.myObjects as myObjects
import src.minigame.physicsTest.ball as ball
import pygame
import time
import math

def removeObj(objects, object):
    if isinstance(object, DynamicObject): object.halt()
    if object in objects: objects.remove(object)
    else:
        print("ERROR: Object ",object,"\n\t not found in objects!")

def startGame(mainWindow, scale, framerate):
    gravity = 1.5
    objects = []
    clock = pygame.time.Clock()  # Clock used for frame rate

    coco = ball.Ball(grab_sprite("data/assets/sprites/coconut.png", scale/2), scale, 70, 20, objects, "coco", 5)

    def takeInputs(key, gravity = gravity): # inputs not associated with an object
        nonlocal coco
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
        if key[pygame.K_i]:
            print("Setting up...")
            setupArc()
            time.sleep(.3)

        if key[pygame.K_h]:
            for object in objects:
                if isinstance(object, DynamicObject):
                    object.halt()


    def addCrate(x, y, value = 10, scale = scale, objects = objects): # the code for adding objects is kind of messy,
        # so this can be preferable.
        sprite = grab_sprite("data/assets/sprites/bluebox.png", scale)
        objects.append(myObjects.Crate(sprite,scale, x, y - sprite.get_height()/scale, objects, value))

    def addBall(sprite, x, y, scale = scale, name = "undefinedBall", mass = 10):
        nonlocal objects
        objects.append(ball.Ball(sprite, scale, x, y, objects, name, mass))
    addBall(generate_circle(10,scale), 55, 120)

    def addCup(x, y, scale = scale, name = "undefinedBowl", objects = objects):
        sprite = grab_sprite("data/assets/sprites/bowl.png", scale)
        objects.append(Object(sprite, scale, x, y - sprite.get_height()/scale, objects, name))
    def addRect(position, dimensions, frict = physics.frictS, color = (180,180,180), scale = scale, objects = objects, bounce = 0):
        objects.append(RectObject(dimensions, scale, position[0], position[1], objects, frict, color = color, bounce = bounce))

    def setupBounce():
        nonlocal objects
        nonlocal gravity
        nonlocal coco
        objects.clear()
        gravity = 2.2

        addRect((0, 400), (500, 50), bounce = .7) # floor

        # triangle = terrain.from_polygon([[20,345],[50,310],[20,280]], scale, objects, color = (0,255,0,255), name="triangle")
        # objects.append(triangle)

        addRect((300,50),(50,200), bounce = 1) # wall
        addRect((120,50),(50,200), bounce = 1) # wall

        addCrate(420, 400) # y-position is for bottom of crate rather than top
        addCup(300,400)
        coco.halt()
        coco.x = 170; coco.y = 355
        coco.angle = math.pi*(1/3)
        coco.power = 130
        coco.launch()
        objects.append(coco)

    def setupArc():
        nonlocal objects
        nonlocal gravity
        nonlocal coco
        objects.clear()
        gravity = 2.2

        addRect((0, 400), (500, 50), bounce = .7) # floor

        # triangle = terrain.from_polygon([[20,345],[50,310],[20,280]], scale, objects, color = (0,255,0,255), name="triangle")
        # objects.append(triangle)


        addCup(70,400)
        coco.halt()
        coco.x = 400; coco.y = 355
        coco.angle = math.pi*(2/3)
        coco.power = 130
        coco.launch()
        objects.append(coco)

    setupBounce()

    isRunning=True
    while(isRunning):
        clock.tick(framerate)
        mainWindow.fill((0,0,0)) # wipes the screen
        takeInputs(pygame.key.get_pressed()) # inputs not associated with an object



        for object in objects: # Physics, movement
            if isinstance(object, physics.Dynamic):
                object.momY += gravity
                object.update(maxMom = 150)
                if ((abs(object.dX) >= 1) or (abs(object.dY) >= 1)):
                    physics.velHandler(object, objects)
        # if(coco.y > 90): coco.y = 90

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