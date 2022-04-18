import pygame

from src.game.boardGame.boardPlayers import BoardPlayer
from src.game.boardGame.boardGame import rollOneDice, goesFirstScreen, setPlacementsForBoardPlayers

"""
    About this file:
    This is a file that will be the runner of the application
"""
import time
import src.engine.menus.mainmenu as mainMenu
import src.engine.scenecreator.sceneCreator as sceneCreator
import random


def main():
    pygame.init()
    framerate=60
    scale = 1 #Sets the scale of ALL png's
    pygame.display.set_caption("Mammon-Engine")
    mainMenu.launch(512, 448, framerate, scale)
    # w, h = pygame.display.get_surface().get_size()


if(__name__ == "__main__"):
    main()