import pygame
from src.engine.andrewMenus import minigameTypeMenu
from src.minigame.fruitPanic import handGame
from src.minigame.physicsTest import physicstest
from src.engine.button import Button
from src.minigame.teamMasher import masher
from src.engine.andrewMenus.menu import Menu
from src.minigame.cannonPanic import cannonPanicScene
import src.minigame.exampleGame.myLevel as myLevel
import src.minigame.teamSwimmer.teamSwimmer as teamSwimmer
import src.minigame.winScreen.winScreen as winScreen
import src.minigame.chartACourse.chartACourse as chartACourse


'''
Created by Andrew Bunn
Menu for testing minigames, not the final products. Mainly for experimenting
'''


def launchTestMinigame(mainWindow, framerate, scale):
    """
    launches the test minigames menu
    :param mainWindow: window to display in
    :param framerate: refresh rate for the display
    :param scale: what to scale the window and all items inside by (factor)
    """
    gameMenuButtons = createAllGameMenuButtons(mainWindow, framerate, scale)

    testGameMenu = Menu("Test Games", gameMenuButtons)
    testGameMenu.launch(mainWindow, framerate)


def createAllGameMenuButtons(mainWindow, framerate, scale):
    """
    creates all the buttons for this menu and returns them
    :param mainWindow: the window to display the menu in
    :param framerate: set the refresh rate of the menu
    :param scale: what to scale the display by
    :return: returns all the game menu buttons in a tuple
    """

    def onClickRando1Button(listOfButtons=None, listOfImages=None):
        return handGame.startGame(mainWindow, scale, framerate)

    def onClickRando2Button(listOfButtons=None, listOfImages=None):
        return physicstest.startGame(mainWindow, scale, framerate)

    def onClickRando3Button(listOfButtons=None, listOfImages=None):
        return masher.startGame(mainWindow, scale, framerate)

    def onClickRando4Button(listOfButtons=None, listOfImages=None):
        return chartACourse.startGame(mainWindow, scale, framerate)

    def onClickRando5Button(listOfButtons=None, listOfImages=None):
        return myLevel.startGame(mainWindow, scale, framerate)

    def onClickRando6Button(listOfButtons=None, listOfImages=None):
        return teamSwimmer.startGame(mainWindow, scale, framerate)

    def onClickBackButton(listOfButtons=None, listOfImages=None):
        return minigameTypeMenu.launchMinigameMenu(mainWindow, framerate, scale)

    def onClickRandoButtonUnassigned():
        print("Unassigned to anything, Goodbye")

    # generate buttons
    newRando1 = Button(16, 16, 232, 64, scale, onClickRando1Button,
                       "data/assets/sprites/rando1Button.png", mainWindow)
    newRando2 = Button(264, 16, 232, 64, scale, onClickRando2Button,
                       "data/assets/sprites/rando2Button.png", mainWindow)
    newRando3 = Button(16, 96, 232, 64, scale, onClickRando3Button,
                       "data/assets/sprites/rando3Button.png", mainWindow)
    newRando4 = Button(264, 96, 232, 64, scale, onClickRando4Button,
                       "data/assets/sprites/rando4Button.png", mainWindow)
    newRando4.dummy = True  # Assign dummy to true if button returns nothing/has no functionality yet
    newRando5 = Button(16, 176, 232, 64, scale, onClickRando5Button,
                       "data/assets/sprites/rando5Button.png", mainWindow)
    newRando5.dummy = True
    newRando6 = Button(264, 176, 232, 64, scale, onClickRando6Button,
                       "data/assets/sprites/rando6Button.png", mainWindow)
    newRando6.dummy = True
    newBackButton = Button(4, 412, 96, 32, scale, onClickBackButton,
                           "data/assets/sprites/backMenuButton.png", mainWindow)
    return newBackButton, newRando1, newRando2, newRando3, newRando4, newRando5, newRando6
