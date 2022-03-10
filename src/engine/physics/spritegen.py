import pygame

def grab_sprite(address):
    sprite = pygame.image.load(address)
    sprite = pygame.transform.scale(sprite, ((sprite.get_width()) /2, (sprite.get_height()) /2))
    return sprite

def generate_polygon(points, color = (0,255,0,255), size = None):
    if not size: # size = size of box encapsulating points
        xValues = [point[0] for point in points]
        yValues = [point[1] for point in points]
        size = (max(xValues) - min(xValues), max(yValues) - min(yValues))
    sprite = pygame.Surface(size, flags=pygame.SRCALPHA)
    pygame.draw.polygon(sprite, color, points)
    return sprite

def generate_circle(radius, color = (255,0,0,255)):
    return generate_ellipse(2*radius,2*radius,color)

def generate_ellipse(width, height, color = (255,255,0,255)):
    sprite = pygame.Surface((width, height), flags = pygame.SRCALPHA)
    pygame.draw.ellipse(sprite,color,pygame.Rect((0,0),(width,height)))
    return sprite

def generate_rectangle(width, height, color = (0,255,255)):
    return generate_polygon([[0,0],[width,0], [width,height], [0,height]], color, size = (width,height))
