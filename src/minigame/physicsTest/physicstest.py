import src.engine.physics.physics as physics
from src.engine.physics.physics import Object, DynamicObject, RectObject, DynamicRect
from src.engine.physics.spritegen import *
import src.engine.physics.terrain as terrain
import src.minigame.exampleGame.myObjects as myObjects
import pygame
import time

def removeObj(objects, object):
    if isinstance(object, DynamicObject): object.halt()
    if object in objects: objects.remove(object)

def startGame(mainWindow, scale, framerate):
    def takeInputs(key): # inputs not associated with an object
        nonlocal gravity # gravity belongs to startGame

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

        if key[pygame.K_p]:
            print("Setting up...")
            setup()

    objects = []

    def addCrate(x, y, value = 10, scale = scale, objects = objects): # the code for adding objects is kind of messy, so this
        # can be preferable.
        # nonlocal objects
        sprite = grab_sprite("data/assets/sprites/bluebox.png", scale)
        objects.append(myObjects.Crate(sprite,scale, x, y - sprite.get_height()/scale, objects, value))
    def addBall(sprite, x, y, scale = scale, name = "undefinedBall", mass = 10):
        nonlocal objects
        objects.append(myObjects.Ball(sprite, scale, x, y, objects, name, mass))
    def addRect(position, dimensions, frict = physics.frictS, color = (180,180,180), scale = scale):
        nonlocal objects
        objects.append(RectObject(dimensions, scale, position[0], position[1], objects, frict, color = color))

    def setup():
        nonlocal objects
        nonlocal gravity
        for object in objects:
            removeObj(objects, object)
        gravity = 3

        addRect((100, 400), (500, 50)) # floor

    clock = pygame.time.Clock()  # Clock used for frame rate

    triangle = terrain.from_polygon([[20,345],[50,310],[20,280]], scale, objects, color = (0,255,0,255), name="triangle")
    objects.append(triangle)

    addRect((100,400), (500, 50))
    addRect((300,50),(50,200))

    addCrate(420, 400) # y-position is for bottom of crate rather than top

    addBall(generate_circle(20,scale), 25, 20)
    isRunning=True


    gravity = 1.5
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