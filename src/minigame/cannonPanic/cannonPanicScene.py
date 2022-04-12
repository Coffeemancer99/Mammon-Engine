import math
import src.minigame.physicsTest.ball as ball
import src.minigame.cannonPanic.cannonPanicController as cannonPlayer
import pygame
from src.engine.physics.physics import Object, DynamicObject, RectObject, DynamicRect
import src.engine.physics.spritegen as spritegen
import src.engine.physics.physics as physics
import src.minigame.cannonPanic.playerController as player
import src.minigame.cannonPanic.cannonball as cannonball

#Daniels code
def removeObj(objects, object):
    if isinstance(object, DynamicObject): object.halt()
    if object in objects:

        objects.remove(object)

def startGame(mainWindow, scale, framerate):
    clock = pygame.time.Clock()  # Clock used for frame rate
    windowX, windowY = pygame.display.get_surface().get_size()
    isRunning = True
    gravity = 1.0
    cannonX = 25
    cannonY = 200
    scaleFancy = 0.05
    cannonSprite = pygame.image.load("data/assets/sprites/goodSprites/Canon.png")
    pirateMan = spritegen.grab_sprite("data/assets/sprites/goodSprites/pirateDude.png", scaleFancy)

    cannonSprite = pygame.transform.scale(cannonSprite, ((cannonSprite.get_width()) * scaleFancy, (cannonSprite.get_height()) * scaleFancy))
    cannon = cannonPlayer.CannonPlayer(cannonSprite, scale, cannonX, cannonY, pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d, pygame.K_SPACE, None,
                                     0, False, name="cannon", mass=4, maxpower=80)

    pirateMan = player.playerController(pirateMan, scale, 200, 200, pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d, pygame.K_SPACE, None,
                                     0, False, name="cannon", mass=4, maxpower=80)

    objects = [cannon, pirateMan]
    for objectz in objects:  # rendering
        objectz.draw(mainWindow)
    while(isRunning):
        clock.tick(framerate)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                isRunning=False
        mainWindow.fill((0, 0, 0))




        for object in objects: # Physics, movement
            if isinstance(object, DynamicObject):
                if isinstance(object, cannonPlayer.CannonPlayer):
                    if object.primedBall:
                        if object.primedBall not in objects:
                            objects.append(object.primedBall)

                            if(not object.ready):
                                object.primedBall = None
                    if object.isLaunched:
                        object.fall(gravity)


                object.update(maxMom = 150)
                object.rect = object.sprite.get_rect(center=object.sprite.get_rect(center=(object.x, object.y)).center)
                # if(isLoud and (object is cannon)): print(cannon)
                if ((abs(object.dX) >= 1) or (abs(object.dY) >= 1)):
                    didImpact = physics.velHandler(object, objects)

                    if (isinstance(object, player.playerController)):
                        continue



                    if(didImpact!=[]):
                        for agents in didImpact:
                            if (isinstance(agents, player.playerController)):

                                agents.loseHealth()
                                if (agents.isDead()):
                                    print(f"\nAnd the player health iiiiiiiiiiiiiis{agents.health}\n")
                                    removeObj(objects, agents)
                        removeObj(objects, object)
                       # object.loseHealth()
                       # print("SHOULD BE RIGHT AFTER ")

                       # print(f"Agents {didImpact}")
                        # for agents in didImpact:
                        #     removeObj(objects, agents)
                        # print("DID IMPACT %d" %didImpact)
                        # removeObj(objects, object)
                        cannon.ready = True
                       # print(f"sdfsdfsdsdf{didImpact}")

        #cannon.fall(gravity)
        for objectz in objects:
            newSprite = pygame.transform.rotate(objectz.sprite, objectz.angle*180/math.pi)

            mainWindow.blit(newSprite, (objectz.rect.x, objectz.rect.y))
            if not objectz.alive:
                removeObj(objects, objectz)
                cannon.ready = True
                #cannon2.ready = True
            objectz.timeUntilDeletion()
            if not isinstance(objectz, cannonPlayer.CannonPlayer) and not isinstance(objectz, player.playerController):
                objectz.fall(gravity)
        # for objectz in objects:
        #     if ((abs(objectz.dX) >= 1) or (abs(objectz.dY) >= 1)):
        #         physics.velHandler(object, objects)

        pygame.display.update()