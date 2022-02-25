import pygame
from src.engine.physics.physics import movementLeftRight, applyGravityPlayer




class Fruit():
    def __init__(self, x, y, speed, scale, sprite, fId, badFruit):
        self.fruitId = fId
        self.badFruit = badFruit
        self.scale = scale
        self.sprite = sprite
        self.sprite = pygame.transform.scale(self.sprite, ((self.sprite.get_width()) * scale/2, (self.sprite.get_height()) * scale/2))
        self.rectCol = self.sprite.get_rect()
        self.rectCol.x = x
        self.rectCol.y = y
        self.velY = 0

        self.speed = speed

        self.width = self.sprite.get_width()
        self.height = self.sprite.get_height()

        self.dX = 0
        self.dY = 0

    def update(self):
        self.dX = 0
        self.dY = 0

        fallSpeed = 2 * self.speed * self.scale
        terminalV = 4 * self.scale

        # add some form of gravity
        self.velY = applyGravityPlayer(self.velY, fallSpeed, terminalV)
        # make sure to set curY
        self.dY += self.velY


#ONLY UPDATE RECTANGLE IN ONE PLACE!!! O_O SHARED MUTABLE STATE OH MY
    def updateRect(self):
        self.rectCol.x += self.dX
        self.rectCol.y += self.dY

    def __repr__(self):
        return(str(self.fruitId))