import pygame
from src.engine.physics.physics import movementLeftRight, applyGravityPlayer


'''
playerController.py created by Andrew Bunn
Player class implemented by Andrew Bunn
'''

class Player():
    def __init__(self, x, y, scale,  upKey, leftKey, rightKey, downKey, sprite):
        self.scale = scale
        self.sprite = sprite
        self.sprite = pygame.transform.scale(self.sprite, ((self.sprite.get_width()) * scale, (self.sprite.get_height()) * scale))

        self.rect = self.sprite.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.velY = 0

        self.upKey =  upKey
        self.leftKey = leftKey
        self.rightKey = rightKey
        self.downKey = downKey

        self.width = self.sprite.get_width()
        self.height = self.sprite.get_height()

        self.score = 0

        self.dX = 0
        self.dY = 0

    '''
    update - updates the player position based on inputs
    '''
    def update(self):
        self.dX = 0
        self.dY = 0
        transformSpeed = 4 * self.scale

        key = pygame.key.get_pressed()
        # if key[self.upKey]:
        #     self.dY = movementLeftRight(self.dY, -transformSpeed)
        # if key[self.downKey]:
        #     self.dY = movementLeftRight(self.dY, transformSpeed)
        if key[self.leftKey]:
            self.dX = movementLeftRight(self.dX, -transformSpeed)
        if key[self.rightKey]:
            self.dX = movementLeftRight(self.dX, transformSpeed)

        self.dY += self.velY

        return self


#ONLY UPDATE RECTANGLE IN ONE PLACE!!! O_O SHARED MUTABLE STATE OH MY
    def updateRect(self):
        self.rect.x += self.dX
        self.rect.y += self.dY