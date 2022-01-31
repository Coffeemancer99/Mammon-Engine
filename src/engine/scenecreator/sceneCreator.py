import pygame
from src.engine import ecs
from src.engine import physics

# from ..ecs import entity -- EXAMPLE OF OTHER WAY

#This function creates a straight line of sprites.
#Window = The current pygame window, sprite = the sprite to paint
#numBlocks = the number of blocks to paint, spriteSize = the size of the sprite (one side)
#Start X/Start Y = The position to start
#up = Boolean, true is vertical platform false is horizontal
def createPlatform(window, sprite, ground, numBlocks, spriteSize, startX, startY, up):

    start = 0
    while(start<numBlocks):
        if(up):
            window.blit(sprite, (startX, startY - (start * spriteSize)))
        else:
            window.blit(sprite, (startX + (start * spriteSize), startY - spriteSize))
        start+=1
    return window



# ground can be a list i append objs to