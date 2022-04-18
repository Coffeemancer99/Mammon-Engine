import pygame

from src.engine.physics import spritegen, physics
from src.engine.physics.physics import DynamicObject
from src.minigame.manOverboard import swimmerPlayer


def startGame(mainWindow, scale, framerate):
    clock = pygame.time.Clock()  # Clock used for frame rate
    windowX, windowY = pygame.display.get_surface().get_size()
    isRunning = True
    weirdScale = 0.0375 * scale/1

    swimmer1Sprite = spritegen.grab_sprite("data/assets/sprites/goodSprites/barrelSub.png", weirdScale)
    objects = []
    p1 = swimmerPlayer.SwimmerPlayer(64, 256, scale, pygame.K_w, pygame.K_a, pygame.K_d, pygame.K_s, swimmer1Sprite, 1,
                                     objects)
    p2 = swimmerPlayer.SwimmerPlayer(256, 256, scale, pygame.K_UP, pygame.K_LEFT, pygame.K_RIGHT, pygame.K_DOWN,
                                     swimmer1Sprite, 1, objects)

    objects.append(p1)
    objects.append(p2)

    while isRunning:
        clock.tick(framerate)
        primedInputs = []
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                isRunning = False
            # Get every time the button is held up (Prevent holding down the button)
            if event.type == pygame.KEYUP:
                primedInputs.append(event)

        mainWindow.fill((30, 125, 255))  # make background blue

        # display all the objects
        for obj in objects:
            mainWindow.blit(obj.sprite, (obj.x, obj.y))

        for obj in objects:
            if isinstance(obj, physics.Dynamic):
                obj.update(maxMom=15)

            # if it's a player, act on their inputs
            if isinstance(obj, swimmerPlayer.SwimmerPlayer):
                obj.fightCurrent(primedInputs)

            # Update velocity if it is over 1 in any direction
            if (abs(obj.dX) >= 1) or (abs(obj.dY) >= 1):
                collisions = physics.velHandler(obj, objects)
                if len(collisions) != 0:
                    if isinstance(obj, swimmerPlayer.SwimmerPlayer): # If the current object is a player
                        for otherObj in collisions:
                            # Update velocity on collision
                            # TODO figure out why i can only bump once and need to wait for
                            #   it to slow back to mom = 0 before next bump
                            if isinstance(otherObj, swimmerPlayer.SwimmerPlayer):
                                if abs(otherObj.momX) < abs(obj.momX):
                                    otherObj.momX = obj.momX
                                if abs(otherObj.momY) < abs(obj.momY):
                                    otherObj.momY = obj.momY


            outOfBounds(objects)

        pygame.display.update()



def outOfBounds(objects):
    # if player x or y out of screen bounds
    for obj in objects:
        # had to do negative values to account for sprite size
        if obj.x > 512 or obj.y > 448 or obj.x < -32 or obj.y < -32:
            if isinstance(obj, swimmerPlayer.SwimmerPlayer):
                objects.remove(obj)
