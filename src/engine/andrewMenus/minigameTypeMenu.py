import pygame
from src.engine.andrewMenus import testGameMenu
from src.engine.menus import mainmenu
from src.engine.button import Button
from src.engine.andrewMenus.menu import Menu

'''
Created by: Andrew Bunn
Menu to choose what type of minigames to launch such as 
FFA, 2v2, 3v1
'''

def launchMinigameMenu(mainWindow, framerate, scale):
    """
    launchs the minigame menu
    :param mainWindow: the window to display the menu in
    :param framerate: set the refresh rate of the menu
    :param scale: what to scale the display by
    """
    minigameMenuButtons = createAllMinigameButtons(mainWindow, framerate, scale)

    minigameMenu = Menu("Minigame Types", minigameMenuButtons)
    minigameMenu.launch(mainWindow, framerate)



def createAllMinigameButtons(mainWindow, framerate, scale):
    """
    creates all the buttons for the minigame menu and returns them
    :param mainWindow: the window to display the menu in
    :param framerate: set the refresh rate of the menu
    :param scale: what to scale the display by
    :return:
    """
    width, height = pygame.display.get_surface().get_size()

    def onClickRando(listOfButtons=None):
        print("Unassigned")

    def onClickBackButton(listOfButtons=None):
        return mainmenu.launch(width, height, framerate, scale)

    def onClickTestButton(listOfButtons=None):
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
                           "data/assets/sprites/testingButton.png", mainWindow, "test")
    return newBackButtonImg, newFfaButton, newOneVThreeButton, newTestButton, newTwoVTwoButton
