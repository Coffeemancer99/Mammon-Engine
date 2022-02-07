import pygame
import time
#Launches main menu
def launch(width, height, framerate):
    clock = pygame.time.Clock()  # Clock used for frame rate
    mainWindow = pygame.display.set_mode((512, 448))
    newGameImg=pygame.image.load("../../data/assets/sprites/newgame.png")
    mainWindow.blit(newGameImg, (0,0))
    pygame.display.update()
    isRunning=True
    while(isRunning):
        clock.tick(framerate)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                isRunning=False
            #KEYBOARD INPUTS
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                if (pos[1]<=112 and pos[1]>=0):
                    return


            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    print("YO")


