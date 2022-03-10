import pygame
import math
import src.engine.physics.physics as physics


def from_straight(p1, p2, p3 = (0,0)):
    (x1, y1) = p1; (x2, y2) = p2
    toReturn = math.atan((y2-y1)/(x2-x1)) + (math.pi/2)
    while toReturn < 0:
        toReturn += 2*math.pi
    return toReturn

def from_ellipse(width,height,x2,y2):
    a = math.sqrt(width)
    b = math.sqrt(height)
    theta = math.atan((a*y2)/(b*x2))
    return theta