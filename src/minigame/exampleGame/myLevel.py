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
        nonlocal myBall, gravity # myBall and gravity belong to startGame
        if key[pygame.K_w]:
            myBall.momY -= 3
        if key[pygame.K_s]:
            myBall.momY += 3
        if key[pygame.K_a]:
            myBall.momX -= 2
        if key[pygame.K_d]:
            myBall.momX += 2
        if key[pygame.K_SPACE]:
            if physics.grounded(myBall, objects, onlyStatics=True):
                myBall.momY -= 50

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
    def addCrate(x, y, value = 10, scale = scale):
        nonlocal objects
        sprite = grab_sprite("data/assets/sprites/bluebox.png", scale)
        objects.append(myObjects.Crate(sprite,scale, x, y - sprite.get_height(), value))

    clock = pygame.time.Clock()  # Clock used for frame rate

    objects = []
    myBall = myObjects.Ball(generate_circle(20,scale), scale, 25, 20, name="myBall", mass = 4)
    triangle = terrain.from_polygon([[20,345],[50,310],[20,280]], scale, color = (0,255,0,255), name="triangle")

    objects.append(triangle)
    objects.append(myBall)

    objects.append(RectObject((500,50), scale, 100,400, frict = .1))
    objects.append(RectObject((50, 200), scale, 300, 50))
    addCrate(420, 400) # y-position is for bottom of crate rather than top
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