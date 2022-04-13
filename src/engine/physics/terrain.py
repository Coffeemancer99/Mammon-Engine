import pygame
import src.engine.physics.physics as physics
import src.engine.physics.normal as normal
import functools
from functools import partial
from src.engine.physics.spritegen import *
import math

class Terrain(physics.Object):
    def __init__(self, sprite, scale, x, y, objects, name = "undefinedTerrain", frict = 0.7, edges = None, normalFuns = None):
        physics.Object.__init__(self, sprite, scale, x, y, objects, name, frict)
        self.edges = edges
        self.normalFuns = normalFuns

def is_between(point1, point2, testPoint):
    if testPoint in [point1, point2]:
        return True

    point1 = list(point1); point2 = list(point2); testPoint = list(testPoint)
    point1[1] = -point1[1];     point2[1] = -point2[1];     testPoint[1] = -testPoint[1]

    if(abs(point1[1] - point2[1]) > abs(point1[0] - point2[0])): # if dY > dX
        for point in [point1, point2, testPoint]: #rotate points to minimize computer error with slope calculation
            backup = point[1]
            point[1] = point[0]
            point[0] = backup
    (x1, y1) = point1; (x2,y2) = point2; (x3,y3) = testPoint

    if (y2 == y1): # horizontal or rotated vertical line
        return ((y3 in [y1, y1-1, y1+1]) and (x3 >= min(x1,x2)) and (x3 <= max(x1,x2)))

    m = (y2-y1)/(x2-x1)
    b = y1-(m*x1)

    y = m*x3 + b
    floor = math.floor(y)

    return((floor == y3) or (floor +1 == y3) or (floor - 1 == y3))

def from_polygon(points, scale, objects, color = (0,255,0,255), name = "undefinedPolygon", frict = 0.7):
    xValues = [point[0] for point in points]
    yValues = [point[1] for point in points]
    minX = min(xValues); maxX = max(xValues)
    minY = min(yValues); maxY = max(yValues)
    for point in points:
        point[0] -= minX
        point[1] -= minY
    sprite = generate_polygon(points,scale,color, size = (maxX - minX, maxY - minY))

    outline = []; edges = []; normalFuns = []
    for point in pygame.mask.from_surface(sprite).outline():
        if point not in outline:
            outline.append(point)

    # print("outline = {}".format(outline))
    # for i in range(len(points)):
    #     edges.append(list(filter((partial(is_between, points[i], points[(i+1)%len(points)])), outline)))
    #     normalFuns.append(partial(normal.from_straight,points[i], points[(i+1)%len(points)]))
    #     print("for {} and {}, points_between = {}".format(points[i], points[(i+1)%len(points)], list(filter((partial(is_between, points[i], points[(i+1)%len(points)])), outline))))
    # print("")

    return Terrain(sprite, scale, minX, minY, objects, name, frict, edges)

