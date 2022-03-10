import pygame
import src.engine.physics.physics as physics
import src.engine.physics.normal as normal
import functools
from functools import partial
from src.engine.physics.spritegen import *
import math

class Terrain(physics.Object):
    def __init__(self, sprite, scale, x, y, name = "undefinedTerrain", frict = 0.7, edges = None, normalFuns = None):
        physics.Object.__init__(self, sprite, scale, x, y, name, frict)
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
    if (x2 == x1): # vertical line
        return ((x3 in [x1, x1-1, x1+1]) and (y3 >= min(y1,y2)) and (y3 <= max(y1,y2)))
    if (y2 == y1): # horizontal line
        return ((y3 in [y1, y1-1, y1+1]) and (x3 >= min(x1,x2)) and (x3 <= max(x1,x2)))

    m = (y2-y1)/(x2-x1)
    b = y1-(m*x1)

    y = m*x3 + b
    floor = math.floor(y)
    # if((x3 == 99) & (y3 == -1)):
    #     print("({: },{: }) between ({: },{: }) & ({: },{: })".format(x3, y3, x1, y1, x2, y2), end="\t\t")
    #     print("y = " + str(m) + "x + " + str(b) + " \t->\t (x3,y) = (" + str(x3) + ", " + str((m * x3 + b)) + ")\t\t", end="")
    #
    #     print("\n{}\t{}\t{}\t{}".format(x3, y, math.floor(y), math.floor(y)+1))
    #     print("")

    return((floor == y3) or (floor +1 == y3) or (floor - 1 == y3))

def from_polygon(points, scale, color = (0,255,0,255), name = "undefinedPolygon", frict = 0.7):
    xValues = [point[0] for point in points]
    yValues = [point[1] for point in points]
    minX = min(xValues); maxX = max(xValues)
    minY = min(yValues); maxY = max(yValues)
    for point in points:
        point[0] -= minX
        point[1] -= minY
    sprite = generate_polygon(points,color, size = (maxX - minX, maxY - minY))

    outline = []; edges = []; normalFuns = []
    for point in pygame.mask.from_surface(sprite).outline():
        if point not in outline:
            outline.append(point)

    print("outline = {}".format(outline))
    for i in range(len(points)):
        edges.append(list(filter((partial(is_between, points[i], points[(i+1)%len(points)])), outline)))
        normalFuns.append(partial(normal.from_straight,points[i], points[(i+1)%len(points)]))
        print("for {} and {}, points_between = {}".format(points[i], points[(i+1)%len(points)], list(filter((partial(is_between, points[i], points[(i+1)%len(points)])), outline))))
    print("")

    return Terrain(sprite, scale, minX, minY, name, frict, edges)

