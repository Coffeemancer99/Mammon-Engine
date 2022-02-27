import pygame
from src.engine.andrewMenus import minigameTypeMenu
from src.minigame.fruitPanic import handGame
from src.minigame.physicsTest import physicstest
from src.engine.button import Button
from src.minigame.teamMasher import masher


def launchTestMinigame(mainWindow, framerate, scale):
    clock = pygame.time.Clock()
    width, height = pygame.display.get_surface().get_size()


    def onClickRando1Button():
        return handGame.startGame(mainWindow, scale, framerate)

    def onClickRando2Button():
        return physicstest.startGame(mainWindow, scale, framerate)

    def onClickRando3Button():
        return masher.startGame(mainWindow, scale, framerate)

    def onClickBackButton():
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
    newRando4 = Button(264, 96, 232, 64, scale, onClickRandoButtonUnassigned,
                       "data/assets/sprites/rando4Button.png", mainWindow)
    newRando4.dummy = True # Assign dummy to true if button returns nothing
    newRando5 = Button(16, 176, 232, 64, scale, onClickRandoButtonUnassigned,
                       "data/assets/sprites/rando5Button.png", mainWindow)
    newRando5.dummy = True
    newRando6 = Button(264, 176, 232, 64, scale, onClickRandoButtonUnassigned,
                       "data/assets/sprites/rando6Button.png", mainWindow)
    newRando6.dummy = True
    newBackButton = Button(4, 412, 96, 32, scale, onClickBackButton,
                       "data/assets/sprites/backMenuButton.png", mainWindow)

    buttons = []
    buttons.extend((newRando1, newRando2, newRando3,
                    newRando4, newRando5, newRando6, newBackButton))

    # Paint buttons and images to screen
    mainWindow.fill((55, 55, 55))

    for button in buttons:
        button.renderButton()

    isRunning = True

    while (isRunning):
        pygame.display.update()
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
