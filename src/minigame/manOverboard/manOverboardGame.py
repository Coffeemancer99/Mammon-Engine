import pygame

from src.engine.physics import spritegen, physics
from src.minigame.manOverboard import swimmerPlayer


def startGame(mainWindow, scale, framerate):
    clock = pygame.time.Clock()  # Clock used for frame rate
    windowX, windowY = pygame.display.get_surface().get_size()
    isRunning = True
    weirdScale = 0.0375 * scale/2

    swimmer1Sprite = spritegen.grab_sprite("data/assets/sprites/goodSprites/barrelSub.png", weirdScale)
    objects = []
    p1 = swimmerPlayer.SwimmerPlayer(64, 256, scale, pygame.K_w, pygame.K_a, pygame.K_d, pygame.K_s, swimmer1Sprite, 1,
                                     objects)
    p2 = swimmerPlayer.SwimmerPlayer(256, 64, scale, pygame.K_UP, pygame.K_LEFT, pygame.K_RIGHT, pygame.K_DOWN,
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
                physics.velHandler(obj, objects)

        pygame.display.update()
