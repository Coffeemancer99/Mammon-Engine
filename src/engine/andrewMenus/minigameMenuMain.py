import pygame
import time
import minigameTypeMenu


def main():
    mainWindow = pygame.display.set_mode((512, 448))
    pygame.init()
    framerate = 60
    scale = 1 #Sets the scale of ALL png's
    pygame.display.set_caption("Mammon-Engine")
    minigameTypeMenu.launchMinigameMenu(mainWindow, framerate, scale)
    # w, h = pygame.display.get_surface().get_size()


if(__name__ == "__main__"):
    main()