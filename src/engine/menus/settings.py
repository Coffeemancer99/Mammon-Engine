import pygame
import src.engine.menus.mainmenu as mainmenu
def launch(width, height, framerate, window, scale):
    pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()  # Clock used for frame rate
    window.fill((0, 0, 0))
    #Button images
    windowSizeImg=pygame.image.load("../../data/assets/sprites/windowsize.png")
    sizesPng=pygame.image.load("../../data/assets/sprites/sizes.png")
    backPng = pygame.image.load("../../data/assets/sprites/back.png")
    #Rescale images
    windowSizeImg=pygame.transform.scale(windowSizeImg, ((windowSizeImg.get_width()) * scale, (windowSizeImg.get_height()) * scale))
    sizesPng=pygame.transform.scale(sizesPng, ((sizesPng.get_width()) * scale, (sizesPng.get_height()) * scale))
    backPng = pygame.transform.scale(backPng, ((backPng.get_width()) * scale, (backPng.get_height()) * scale))
    #Paint them on screen
    window.blit(windowSizeImg, (0,0)) #1
    window.blit(sizesPng, (0,112*scale)) #2
    window.blit(backPng, (0, 335 * scale))  # 4

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

                #Resolution Option
                if (pos[1]>111*scale and pos[1]<224*scale):
                    #SMALL RES
                    if(pos[0]>0 and pos[0]<142*scale):
                        return launch(512, 448, framerate, window, 1)

                    #MEDIUM RES
                    if(pos[0]>142*scale and pos[0]<332*scale):
                        return launch(512*2, 448*2, framerate, window, 2)
                    #LARGE ERS
                    if(pos[0]>332*scale and pos[0]<448*scale):
                        return launch(512 * 3, 448 * 3, framerate, window, 3)

                #Back Button
                if (pos[1] > 335 * scale and pos[1] < 448* scale):
                    return mainmenu.launch(width, height, framerate, scale)
