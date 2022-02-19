import unittest
import time
import pygame

from src.game.boardGame.boardGame import getPlayerTurn, startGame
from src.game.boardGame.boardPlayers import BoardPlayer
from src.game.boardGame2.firstBoard import FirstBoard




def main():
    pygame.init()
    framerate = 60
    firstBoard = FirstBoard()
    board = firstBoard.testFirstBoard()
    scale = 1  # Sets the scale of ALL png's
    pygame.display.set_caption("Mammon-Engine")
    mainWindow = pygame.display.set_mode((512, 448)) #The main window display
    startGame(mainWindow,scale,framerate,board)
    # w, h = pygame.display.get_surface().get_size()



if __name__ == "__main__":
    main()