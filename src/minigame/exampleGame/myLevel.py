from src.engine.player.playerController import *
import src.engine.player.controls as controls
import src.engine.physics.terrain as terrain
import src.minigame.exampleGame.myObjects as myObjects
import src.engine.physics.physics as physics
from src.engine.physics.physics import Object, DynamicObject, RectObject, DynamicRect
import pygame
import time

def removeObj(object):
    objects = object.objects
    if isinstance(object, DynamicObject): object.halt()
    if object in objects: objects.remove(object)

def startGame(mainWindow, scale, framerate):
    gravity = 1.5
    objects = []
    clock = pygame.time.Clock()  # Clock used for frame rate
    playerNum = 1

    def takeInputs(key, gravity = gravity): # inputs not associated with an object

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

    def addCrate(x, y, value = 10, scale = scale, objects = objects): # the code for adding objects is kind of messy, so this
        # can be preferable.
        sprite = grab_sprite("data/assets/sprites/bluebox.png", scale)
        objects.append(myObjects.Crate(sprite,scale, x, y - sprite.get_height()/scale, objects, value)) # y-position is for bottom of crate rather than top

    def addPlayer(sprite, x, y, controls, xSpeed = 2, ySpeed = 45, scale = scale, mass = 10, objects = objects):
        nonlocal playerNum
        name = "Player " + str(playerNum)
        playerNum += 1

        objects.append( myObjects.Pirate(sprite, scale, x, y, objects, xSpeed, ySpeed, name, mass, controls) )
    def addRect(position, dimensions, frict = physics.frictS, color = (180,180,180), scale = scale, objects = objects):
        """
        The RectObject constructor allows for dimensions to be passed for the sprite, which it will use to
        generate a rectangle of the given color.
        """
        objects.append(RectObject(dimensions, scale, position[0], position[1], objects, frict, color = color))


    triangle = terrain.from_polygon([[20,345],[50,310],[20,280]], scale, objects, color = (0,255,0,255), name="triangle")
    objects.append(triangle)

    addRect((100,400), (500, 50))
    addRect((300,50),(50,200))

    addCrate(420, 400) # y-position is for bottom of crate rather than top
    addPlayer(generate_circle(20, scale), 25, 20, controls.singleplayer)

    isRunning=True
    while(isRunning):
        clock.tick(framerate)
        mainWindow.fill((0,0,0)) # wipes the screen
        takeInputs(pygame.key.get_pressed()) # inputs not associated with an object

        for object in objects: # Physics, movement
            if isinstance(object, DynamicObject):
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