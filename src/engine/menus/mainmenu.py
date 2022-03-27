import pygame
import src.engine.menus.testgame as testgame
#Launches main menu
import src.engine.menus.settings as settings
import src.minigame.fruitPanic.handGame as handGame
import src.minigame.physicsTest.physicstest as physicstest
import src.engine.andrewMenus.mapSelectionMenu as boardMenu
from src.engine.physics.spritegen import *

def launch(width, height, framerate, scale):
    clock = pygame.time.Clock()  # Clock used for frame rate
    mainWindow = pygame.display.set_mode((width, height)) #The main window display
    #Button images
    newGameImg = grab_sprite("data/assets/sprites/newgame.png", 2*scale)
    settingsImg = grab_sprite("data/assets/sprites/settings.png", 2*scale)
    minigames = grab_sprite("data/assets/sprites/minigames.png", 2*scale)

    #TODO: Replace with functional operators later, use relative size of window instead of hardcoded values
    #Paint them on screen
    mainWindow.blit(newGameImg, (0,0)) #1
    mainWindow.blit(settingsImg, (0,112*scale)) #2
    mainWindow.blit(minigames, (0, 224 * scale))  # 2

    pygame.display.update()
    isRunning=True

    handTest = True
    while(isRunning):
        clock.tick(framerate)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                isRunning=False
            #KEYBOARD INPUTS
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                #new game button
                if (pos[1]<112*scale and pos[1]>=0):
                    print("NEW GAME PRESSED")
                    return boardMenu.launchMapMenu(mainWindow, framerate, scale)
                #Settings button
                if (pos[1]>112*scale and pos[1]<224*scale):
                    print("SETTINGS")
                    return settings.launch(width, height, framerate, mainWindow, scale)
                if (pos[1]>224*scale and pos[1]<336*scale):
                    print("MINIGAMES")
                    return minigameTypeMenu.launchMinigameMenu(mainWindow, framerate, scale)
                    # return physicstest.startGame(mainWindow, scale, framerate)
                    # return handGame.startGame(mainWindow, scale, framerate)





