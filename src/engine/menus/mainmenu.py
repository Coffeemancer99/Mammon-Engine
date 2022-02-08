import pygame
import time
import src.engine.menus.testgame as testgame
#Launches main menu
import src.engine.menus.settings as settings
import src.engine.scenecreator.drawTileMap as drawTileMap
def launch(width, height, framerate, scale):
    clock = pygame.time.Clock()  # Clock used for frame rate
    mainWindow = pygame.display.set_mode((width, height)) #The main window display

    #Button images
    newGameImg=pygame.image.load("../../data/assets/sprites/newgame.png")
    settingsImg=pygame.image.load("../../data/assets/sprites/settings.png")
    #Scale images
    newGameImg=pygame.transform.scale(newGameImg, ((newGameImg.get_width()) * scale, (newGameImg.get_height()) * scale))
    settingsImg=pygame.transform.scale(settingsImg, ((settingsImg.get_width()) * scale, (settingsImg.get_height()) * scale))

    #TEST IMAGES
    groundSprite = pygame.image.load("../../data/assets/sprites/groundSprite1.png")
    groundSprite = pygame.transform.scale(groundSprite, ((groundSprite.get_width()) * scale, (groundSprite.get_height()) * scale))

    images = [None, groundSprite]

    #Paint them on screen
    mainWindow.blit(newGameImg, (0,0)) #1
    mainWindow.blit(settingsImg, (0,112*scale)) #2

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
                if (pos[1]<112*scale and pos[1]>=0):
                    print("NEW GAME PRESSED")
                    currMap = testgame.startGame()
                    drawTileMap.drawScene(mainWindow, currMap, images)
                    #return
                #Settings button
                if (pos[1]>112*scale and pos[1]<224*scale):
                    print("SETTINGS")
                    return settings.launch(width, height, framerate, mainWindow, scale)


            #
            # if event.type == pygame.KEYDOWN:
            #     if event.key == pygame.K_LEFT:
            #         print("YO")


