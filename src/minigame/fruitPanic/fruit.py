import pygame
from src.engine.physics.physics import movementLeftRight, applyGravityPlayer




class Fruit():
    def __init__(self, x, y, scale, sprite):
        self.scale = scale
      #  self.sprite = pygame.image.load("../../data/assets/sprites/bolSprite.png")
        self.sprite = sprite
        self.sprite = pygame.transform.scale(self.sprite, ((self.sprite.get_width()) * scale, (self.sprite.get_height()) * scale))
        # may need to scale later
        self.rect = self.sprite.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.velY = 0


        self.width = self.sprite.get_width()
        self.height = self.sprite.get_height()

        self.dX = 0
        self.dY = 0

    def update(self):
        self.dX = 0
        self.dY = 0
        jumpHeight = 16*self.scale
        curX = 0
        curY = 0
        fallSpeed = 1*self.scale
        terminalV = 3*self.scale

        # add some form of gravity
        self.velY = applyGravityPlayer(self.velY, fallSpeed, terminalV)
        # make sure to set curY
        self.dY += self.velY


#ONLY UPDATE RECTANGLE IN ONE PLACE!!! O_O SHARED MUTABLE STATE OH MY
    def updateRect(self):
        self.rect.x += self.dX
        self.rect.y += self.dY