import pygame
import src.engine.collision as collision

# import esper
from src.engine.physics.physics import movementLeftRight, applyGravityPlayer


class Player():
    def __init__(self, x, y):
        self.sprite = pygame.image.load("../../data/assets/sprites/bolSprite.png")
        # may need to scale later
        self.rect = self.sprite.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.velY = 0
        self.jumped = False

        self.width = self.sprite.get_width()
        self.height = self.sprite.get_height()

        self.dX = 0
        self.dY = 0


    def update(self):
        self.dX = 0
        self.dY = 0
        jumpHeight = 16
        curX = 0
        curY = 0
        fallSpeed = 1
        terminalV = 6

        key = pygame.key.get_pressed()
        if key[pygame.K_UP] and self.jumped == False:
            self.velY = -jumpHeight # negative moves up

            self.jumped = True
        if key[pygame.K_UP] == False:
            self.jumped = False
        if key[pygame.K_LEFT]:
            self.dX = movementLeftRight(self.dX, -4)
        if key[pygame.K_RIGHT]:
            self.dX = movementLeftRight(self.dX, 4)
        # add some form of gravity
        self.velY = applyGravityPlayer(self.velY, fallSpeed, terminalV)
        # make sure to set curY
        self.dY += self.velY


#ONLY UPDATE RECTANGLE IN ONE PLACE!!!
    def updateRect(self):
        self.rect.x += self.dX
        self.rect.y += self.dY