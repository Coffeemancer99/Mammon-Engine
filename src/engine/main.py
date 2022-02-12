import pygame

from src.game.boardGame.boardPlayers import BoardPlayer
from src.game.boardGame.boardGame import rollOfDice, goesFirstScreen, setPlacementsForBoardPlayers

"""
    About this file:
    This is a file that will be the runner of the application
"""
import time
import src.engine.menus.mainmenu as mainMenu
import src.engine.scenecreator.sceneCreator as sceneCreator
import random


def main():
    #print("Welcome to the Mammon Engine!")
    # This is the logic for who goes first in the board game

    pygame.init()
    clock=pygame.time.Clock() #Clock used for frame rate
    framerate=60
    scale = 1 #Sets the scale of ALL png's
    pygame.display.set_caption("Mammon-Engine")
    #For resize use second arg: pygame.RESIZABLE
    isRunning = True
    background = (255,255,255)
    # w, h = pygame.display.get_surface().get_size()

    mainMenu.launch(512, 448, framerate, scale)


if(__name__ == "__main__"):
    main()