import pygame

'''
Created by: Andrew Bunn
SpriteLoader class is here just so I do not have to specify a path 
every time i want to load an image at this level in the file system
'''


class SpriteLoader:
    def __init__(self):
        pass

    def loadImage(self, name):
        """
        loads an image from the working directory "D:\Mammon-Engine"
        :param name: string for name of image you want loaded
        :return: return the loaded image
        """
        return pygame.image.load("data/assets/sprites/" + name)
