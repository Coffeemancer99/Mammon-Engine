import pygame


'''
SpriteLoader class is here just so I do not have to specify a path 
every time i want to load an image at this level in the file system
'''
class SpriteLoader:
    def __init__(self):
        pass

    def loadImage(self, name):
        return pygame.image.load("../../../data/assets/sprites/" + name)