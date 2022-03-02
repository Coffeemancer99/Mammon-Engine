import pygame
import math
import src.engine.physics.physics as physics


def from_straight(x1, y1, x2, y2):
    toReturn = math.atan((y2-y1)/(x2-x1)) + (math.pi/2)
    if toReturn < 0:
        toReturn += 2*math.pi
    return toReturn