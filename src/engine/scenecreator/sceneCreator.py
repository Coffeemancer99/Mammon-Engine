import pygame
#This function creates a straight line of sprites.
#Window = The current pygame window, sprite = the sprite to paint
#numBlocks = the number of blocks to paint, spriteSize = the size of the sprite (one side)
def createPlatform(window, sprite, ground, numBlocks, spriteSize):
    w, h = pygame.display.get_surface().get_size()
    start = 0
    while(start<numBlocks):
        window.blit(sprite, (0+start*spriteSize,h-spriteSize))
        start+=1

    return window