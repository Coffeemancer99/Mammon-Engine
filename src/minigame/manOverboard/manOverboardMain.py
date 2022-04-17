import pygame

from src.minigame.manOverboard import manOverboardGame


def main():
    mainWindow = pygame.display.set_mode((512, 448))
    return manOverboardGame.startGame(mainWindow, scale=1, framerate=60)

if(__name__ == "__main__"):
    main()