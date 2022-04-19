import pygame

'''
image.py
Created by Andrew Bunn
Used to make an image for displaying
'''


class Image:

    def __init__(self, x, y, width, height, scale, imagePath, window, displayNow):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.scale = scale
        self.imagePath = imagePath  # string
        self.window = window
        self.displayNow = displayNow  # BOOLEAN
        self.renderThis = False

    def renderImage(self):
        image = pygame.image.load(self.imagePath)
        image = pygame.transform.scale(image,
                                       ((image.get_width()) * self.scale,
                                        (image.get_height()) * self.scale))

        self.window.blit(image, (self.x * self.scale, self.y * self.scale))
        pygame.display.update()


    def renderImageNoUpdate(self):
        image = pygame.image.load(self.imagePath)
        image = pygame.transform.scale(image,
                                       ((image.get_width()) * self.scale,
                                        (image.get_height()) * self.scale))

        self.window.blit(image, (self.x * self.scale, self.y * self.scale))
