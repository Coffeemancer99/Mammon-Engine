import pygame
class tile():
    def __init__(self, img, x, y):
        self.img = img
        self.rectCol = img.get_rect()
        self.rectCol.x = x
        self.rectCol.y = y

    #Takes in a scale integer and scales the current image
    def scale(self, scale):
        self.img=pygame.transform.scale(self.img, ((self.img.get_width()) * scale, (self.img.get_height()) * scale))