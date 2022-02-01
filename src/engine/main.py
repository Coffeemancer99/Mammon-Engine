import pygame
import math

"""
    About this file:
    This is a file that will be the runner of the application
"""
import time

import src.engine.scenecreator.sceneCreator as sceneCreator

def main():
    print("Welcome to the Mammon Engine!")
    pygame.init()
    clock=pygame.time.Clock() #Clock used for frame rate
    framerate=60
    scale = 1 #Sets the scale of ALL png's
    pygame.display.set_caption("Mammon-Engine")
    #For resize use second arg: pygame.RESIZABLE
    mainWindow=pygame.display.set_mode((512,448))
    isRunning = True
    testImg = pygame.image.load("../../data/assets/sprites/testSprite.png")
    grndSprite1 = pygame.image.load("../../data/assets/sprites/groundSprite1.png")
    testImg = pygame.transform.scale(testImg, ((testImg.get_width()*2)*scale, (testImg.get_height()*2)*scale))
    grndSprite1 = pygame.transform.scale(grndSprite1, (64, 64))

    ground=[]
    mainWindow.fill((255, 255, 255))

    mainWindow.blit(testImg, (0, 0))

    background = (255,255,255)


    w, h = pygame.display.get_surface().get_size()

    #This draws the vertical and horizontal bars
    mainWindow=sceneCreator.createPlatform(mainWindow, grndSprite1, ground, 512/64, 64,0,h, True)
    mainWindow = sceneCreator.createPlatform(mainWindow, grndSprite1, ground, 512 / 64, 64, 0, h, False)
    mainWindow = sceneCreator.createPlatform(mainWindow, grndSprite1, ground, 512 / 64, 64, 0, 64, False)
    mainWindow = sceneCreator.createPlatform(mainWindow, grndSprite1, ground, 512 / 64, 64, w-64, h, True)
    mainWindow.blit(testImg, (0, 0))  # This draws the person
    changeDetected=False
    pygame.display.update()
    #DANGEROUS TERRITORY
    #MAIN GAME LOOP
    while(isRunning):
        clock.tick(framerate)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                isRunning=False
        time.sleep(1)
        if(changeDetected):
            sceneCreator.clearBG(mainWindow, background)
            changeDetected=False
    print("Goodbye")


if(__name__ == "__main__"):
    main()