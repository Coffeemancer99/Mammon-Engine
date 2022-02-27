import pygame
from src.engine.andrewMenus import testGameMenu
from src.engine.menus import mainmenu
from src.engine.button import Button

'''
Menu to choose what type of minigames to launch such as 
FFA, 2v2, 3v1
Make a back button
No need to accept, just click and launch
'''

def launchMinigameMenu(mainWindow, framerate, scale):
    clock = pygame.time.Clock()

    newBackButtonImg, newFfaButton, newOneVThreeButton, newTestButton, \
    newTwoVTwoButton = createAllMinigameButtons(mainWindow, framerate, scale)

    buttons = []
    buttons.extend((newFfaButton, newTwoVTwoButton,
                    newOneVThreeButton, newBackButtonImg, newTestButton))

    # Paint buttons and images to screen
    mainWindow.fill((55, 55, 55))

    for button in buttons:
        button.renderButton()

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

                for button in buttons:
                    if button.wasClicked(click) == True:
                        if button.dummy == False:
                            return button.handleClick(click)
                        else:
                            button.handleClick(click)
                        break



def createAllMinigameButtons(mainWindow, framerate, scale):
    width, height = pygame.display.get_surface().get_size()

    def onClickRando():
        print("Unassigned")

    def onClickBackButton():
        return mainmenu.launch(width, height, framerate, scale)

    def onClickTestButton():
        return testGameMenu.launchTestMinigame(mainWindow, framerate, scale)

    newFfaButton = Button(24, 208, 464, 128, scale, onClickRando,
                          "data/assets/sprites/smallerFFAButton.png", mainWindow)
    newFfaButton.dummy = True
    newOneVThreeButton = Button(24, 16, 464, 128, scale, onClickRando,
                                "data/assets/sprites/smaller1v3Button.png", mainWindow)
    newOneVThreeButton.dummy = True
    newTwoVTwoButton = Button(24, 112, 464, 128, scale, onClickRando,
                              "data/assets/sprites/smaller2v2Button.png", mainWindow)
    newTwoVTwoButton.dummy = True
    newBackButtonImg = Button(4, 412, 96, 32, scale, onClickBackButton,
                              "data/assets/sprites/backMenuButton.png", mainWindow)
    newTestButton = Button(412, 412, 96, 32, scale, onClickTestButton,
                           "data/assets/sprites/testingButton.png", mainWindow)
    return newBackButtonImg, newFfaButton, newOneVThreeButton, newTestButton, newTwoVTwoButton
