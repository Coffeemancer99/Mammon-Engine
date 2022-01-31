import pygame
from src.engine import ecs
from src.engine import physics

# from ..ecs import entity -- EXAMPLE OF OTHER WAY

#This function creates a straight line of sprites.
#Window = The current pygame window, sprite = the sprite to paint
#numBlocks = the number of blocks to paint, spriteSize = the size of the sprite (one side)

def createPlatform(window, sprite, ground, numBlocks, spriteSize):
    w, h = pygame.display.get_surface().get_size()
    start = 0
    while(start<numBlocks):
        window.blit(sprite, (0+start*spriteSize,h-spriteSize))      # Location of the block, store!!
        start+=1

    return window


# ground can be a list i append objs to