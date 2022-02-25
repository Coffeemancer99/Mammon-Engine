import pygame
from src.engine.andrewMenus import testGameMenu
from src.engine.menus import mainmenu

'''
Menu to choose what type of minigames to launch such as 
FFA, 2v2, 3v1
Make a back button
No need to accept, just click and launch
'''
def launchMinigameMenu(mainWindow, framerate, scale):
    clock = pygame.time.Clock()
    width, height = pygame.display.get_surface().get_size()

    ffaButton = pygame.image.load("data/assets/sprites/smallerFFAButton.png")
    oneVThreeButton = pygame.image.load("data/assets/sprites/smaller1v3Button.png")
    twoVTwoButton = pygame.image.load("data/assets/sprites/smaller2v2Button.png")
    backButtonImg = pygame.image.load("data/assets/sprites/backMenuButton.png")
    testButton = pygame.image.load("data/assets/sprites/testingButton.png")

    # Scale buttons
    ffaButton = pygame.transform.scale(ffaButton,
                                        ((ffaButton.get_width()) * scale,
                                         (ffaButton.get_height()) * scale))
    oneVThreeButton = pygame.transform.scale(oneVThreeButton,
                                          ((oneVThreeButton.get_width()) * scale,
                                           (oneVThreeButton.get_height()) * scale))
    twoVTwoButton = pygame.transform.scale(twoVTwoButton,
                                          ((twoVTwoButton.get_width()) * scale,
                                           (twoVTwoButton.get_height()) * scale))
    backButtonImg = pygame.transform.scale(backButtonImg,
                                         ((backButtonImg.get_width()) * scale,
                                          (backButtonImg.get_height()) * scale))
    testButton = pygame.transform.scale(testButton,
                                         ((testButton.get_width()) * scale,
                                          (testButton.get_height()) * scale))

    # Paint buttons and images to screen
    mainWindow.fill((55, 55, 55))
    mainWindow.blit(oneVThreeButton, (24 * scale, 16 * scale))
    mainWindow.blit(twoVTwoButton, (24 * scale, 112 * scale))
    mainWindow.blit(ffaButton, (24 * scale, 208 * scale))       # 464 x 64
    mainWindow.blit(backButtonImg,(4 * scale, 412 * scale))
    mainWindow.blit(testButton,(412 * scale, 412 * scale))

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

                if ((click[0] > 24 * scale) and (click[0] <= 488 * scale)):     # x
                    if ((click[1] > 16 * scale) and (click[1] <= 80 * scale)):  # y
                        print("1v3 Selected")
                    elif ((click[1] > 112 * scale) and (click[1] <= 176 * scale)):
                        print("2v2 Selected")
                    elif((click[1] > 208 * scale) and (click[1] <= 252 * scale)):
                        print("FFA")

                if ((click[1] > 412 * scale) and (click[1] <= 444 * scale)):      # x
                    if ((click[0] > 4 * scale) and (click[0] <= 100 * scale)):    # y
                        print("BACK")
                        return mainmenu.launch(width, height, framerate, scale)
                    elif((click[0] > 412 * scale) and (click[0] <= 508 * scale)):
                        print("TEST GAMES")
                        return testGameMenu.launchTestMinigame(mainWindow, framerate, scale)

