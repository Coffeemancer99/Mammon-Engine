import pygame
#import esper

class Player():
    def __init__(self, x, y):
        self.sprite = pygame.image.load("../../data/assets/sprites/bolSprite.png")
        # may need to scale later
        self.rect = self.sprite.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.velY = 0
        self.jumped = False
        self.isGrounded=False

    def update(self):

        curX = 0
        curY = 0

        key = pygame.key.get_pressed()
        if key[pygame.K_UP] and self.jumped == False and self.isGrounded:
            self.velY = -16  # negative moves up
            self.isGrounded = False
            self.jumped = True
        if key[pygame.K_UP] == False:
            self.jumped = False
        if key[pygame.K_LEFT]:
            curX -= 4
        if key[pygame.K_RIGHT]:
            curX += 4

        # add some form of gravity
        if self.isGrounded:
            self.velY = 0
        else:
            self.velY += 1
            if(self.velY > 6):
                self.velY = 6

        # make sure to set curY
        curY += self.velY

        # update coords
        self.rect.x += curX
        # if self.isGrounded:
        #     self.rect.y +=0
        # else:
        self.rect.y += curY
