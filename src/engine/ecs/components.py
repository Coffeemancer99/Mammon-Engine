import pygame
import esper


#   Houses all components

#   Velocity defines the changes in position to be made
#   Velocity component from
#   https://github.com/benmoran56/esper/blob/master/examples/pygame_example.py
class Velocity:
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

#  ------------------------------------------------------------------------------

#   Renderable component from
#   https://github.com/benmoran56/esper/blob/master/examples/pygame_example.py
class Renderable:
    def __init__(self, xPos, yPos, image):
        self.image = image
        self.x = xPos
        self.y = yPos
        self.w = image.get_width()
        self.h = image.get_height()


