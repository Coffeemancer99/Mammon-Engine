import pygame
from collections.abc import Iterable
import math

def grab_sprite(address, scale):
    sprite = pygame.image.load(address)
    sprite = pygame.transform.scale(sprite, (int((sprite.get_width()) *scale), int((sprite.get_height()) *scale)))    # scales the sprites
    return sprite

def generate_polygon(points, scale, color = (0,255,0,255), size = None):
    points = [(scale*point[0], scale*point[1]) for point in points]
    if size: size = [scale*x for x in size]
    else: # size = size of box encapsulating points
        xValues = [scale*point[0] for point in points]
        yValues = [scale*point[1] for point in points]
        size = [max(xValues) - min(xValues), max(yValues) - min(yValues)]
    # print("\tsize = ", size)
    sprite = pygame.Surface(size, flags=pygame.SRCALPHA)
    pygame.draw.polygon(sprite, color, points)
    # sprite = pygame.transform.scale(sprite, (int((sprite.get_width()) *scale), int((sprite.get_height()) *scale)))
    return sprite

def generate_circle(radius, scale, color = (255,0,0,255)):
    return generate_ellipse(2*radius,2*radius, scale, color)

def generate_ellipse(width, height, scale, color = (255,255,0,255)):
    # scale = math.sqrt(scale)
    sprite = pygame.Surface((scale*width, scale*height), flags = pygame.SRCALPHA)
    pygame.draw.ellipse(sprite,color,pygame.Rect((0,0),(scale*width,scale*height)))
    return sprite

def generate_rectangle(width, height, scale, color = (0,255,255)):
    return generate_polygon([[0,0],[width,0], [width,height], [0,height]], scale, color, size = (width,height))
