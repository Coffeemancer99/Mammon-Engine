import pygame
import time
#Launches main menu
import src.engine.menus.settings as settings
def launch(width, height, framerate):
    clock = pygame.time.Clock()  # Clock used for frame rate
    mainWindow = pygame.display.set_mode((width, height)) #The main window display

    #Button images
    newGameImg=pygame.image.load("../../data/assets/sprites/newgame.png")
    settingsImg=pygame.image.load("../../data/assets/sprites/settings.png")
    #Paint them on screen
    mainWindow.blit(newGameImg, (0,0)) #1
    mainWindow.blit(settingsImg, (0,112)) #2

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
                #new game button
                if (pos[1]<112 and pos[1]>=0):
                    return
                #Settings button
                if (pos[1]>112 and pos[1]<224):
                    print("SETTINGS")
                    return settings.launch(width, height, framerate, mainWindow)


            #
            # if event.type == pygame.KEYDOWN:
            #     if event.key == pygame.K_LEFT:
            #         print("YO")


