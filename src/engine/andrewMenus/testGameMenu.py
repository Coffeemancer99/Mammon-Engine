import pygame
from src.engine.andrewMenus import minigameTypeMenu
from src.minigame.fruitPanic import handGame
from src.minigame.physicsTest import physicstest


def launchTestMinigame(mainWindow, framerate, scale):
    clock = pygame.time.Clock()
    width, height = pygame.display.get_surface().get_size()

    backButtonImg = pygame.image.load("data/assets/sprites/backMenuButton.png")
    rando1 = pygame.image.load("data/assets/sprites/rando1Button.png")
    rando2 = pygame.image.load("data/assets/sprites/rando2Button.png")
    rando3 = pygame.image.load("data/assets/sprites/rando3Button.png")
    rando4 = pygame.image.load("data/assets/sprites/rando4Button.png")
    rando5 = pygame.image.load("data/assets/sprites/rando5Button.png")
    rando6 = pygame.image.load("data/assets/sprites/rando6Button.png")


    # Scale buttons
    backButtonImg = pygame.transform.scale(backButtonImg,
                                         ((backButtonImg.get_width()) * scale,
                                          (backButtonImg.get_height()) * scale))
    rando1 = pygame.transform.scale(rando1,
                                         ((rando1.get_width()) * scale,
                                          (rando1.get_height()) * scale))
    rando2 = pygame.transform.scale(rando2,
                                    ((rando2.get_width()) * scale,
                                     (rando2.get_height()) * scale))
    rando3 = pygame.transform.scale(rando3,
                                    ((rando3.get_width()) * scale,
                                     (rando3.get_height()) * scale))
    rando4 = pygame.transform.scale(rando4,
                                    ((rando4.get_width()) * scale,
                                     (rando4.get_height()) * scale))
    rando5 = pygame.transform.scale(rando5,
                                    ((rando5.get_width()) * scale,
                                     (rando5.get_height()) * scale))
    rando6 = pygame.transform.scale(rando6,
                                    ((rando6.get_width()) * scale,
                                     (rando6.get_height()) * scale))

    # Paint buttons and images to screen
    mainWindow.fill((55, 55, 55))
    mainWindow.blit(rando1,(16 * scale, 16 * scale))
    mainWindow.blit(rando2, (264 * scale, 16 * scale))
    mainWindow.blit(rando3, (16 * scale, 96 * scale))
    mainWindow.blit(rando4, (264 * scale, 96 * scale))
    mainWindow.blit(rando5, (16 * scale, 176 * scale))
    mainWindow.blit(rando6, (264 * scale, 176 * scale))
    mainWindow.blit(backButtonImg, (4 * scale, 412 * scale))

    pygame.display.update()
    isRunning = True

    while (isRunning):
        clock.tick(framerate)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                isRunning = False

            # Handle Clicks
            if event.type == pygame.MOUSEBUTTONUP:
                click = pygame.mouse.get_pos()

                # Left column of buttons
                if ((click[0] > 16 * scale) and (click[0] <= 248 * scale)):     # x
                    if((click[1] > 16 * scale) and (click[1] <= 80 * scale)):   # y
                        print("Game 1")
                        return handGame.startGame(mainWindow, scale, framerate)
                    elif((click[1] > 96 * scale) and (click[1] <= 160 * scale)):
                        print("Game 3")
                    elif ((click[1] > 176 * scale) and (click[1] <= 240 * scale)):
                        print("Game 5")

                # Right column of buttons
                if((click[0] > 264 * scale) and (click[0] <= 496 * scale)):
                    if ((click[1] > 16 * scale) and (click[1] <= 80 * scale)):  # y
                        print("Game 2")
                        return physicstest.startGame(mainWindow, scale, framerate)
                    elif ((click[1] > 96 * scale) and (click[1] <= 160 * scale)):  # y
                        print("Game 4")
                    elif ((click[1] > 176 * scale) and (click[1] <= 240 * scale)):  # y
                        print("Game 6")

                # Back button
                if ((click[1] > 412 * scale) and (click[1] <= 444 * scale)):
                    if ((click[0] > 4 * scale) and (click[0] <= 100 * scale)):
                        print("BACK")
                        return minigameTypeMenu.launchMinigameMenu(mainWindow, framerate, scale)


