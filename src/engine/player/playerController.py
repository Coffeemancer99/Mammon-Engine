import pygame


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
        self.isGrounded = False

    def update(self):
        jumpHeight = 16
        curX = 0
        curY = 0
        fallSpeed = 1
        terminalV = 6

        key = pygame.key.get_pressed()
        if key[pygame.K_UP] and self.jumped == False and self.isGrounded:
            self.velY = -jumpHeight # negative moves up
            self.isGrounded = False
            self.jumped = True
        if key[pygame.K_UP] == False:
            self.jumped = False
        if key[pygame.K_LEFT]:
            curX = movementLeftRight(curX, -4)
        if key[pygame.K_RIGHT]:
            curX = movementLeftRight(curX, 4)

        # add some form of gravity
        self.velY = applyGravityPlayer(self.isGrounded, self.velY, fallSpeed, terminalV)

        # make sure to set curY
        curY += self.velY

        # update coords
        self.rect.x += curX
        self.rect.y += curY
