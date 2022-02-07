import pygame

def launch(width, height, framerate, window):
    clock = pygame.time.Clock()  # Clock used for frame rate
    window.fill((0, 0, 0))
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
                    print("WE ARE IN SETTINGS")
                    return
                #Settings button
                if (pos[1]>112 and pos[1]<224):
                    return