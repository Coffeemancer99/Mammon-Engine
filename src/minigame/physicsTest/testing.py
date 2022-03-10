import src.engine.physics.physics as physics
import src.engine.physics.terrain as terrain
import src.minigame.physicsTest.ball as ball
import pygame
import time
import math # for dev values
from functools import partial
import unittest
import pathlib
workingDirectory = pathlib.PurePosixPath('../../engine')

class MyTestCase(unittest.TestCase):
    def testMoveX(self):
        obj = physics.DynamicObject(pygame.image.load(workingDirectory.joinpath("data/assets/sprites/bluebox.png")), 1, 0, 0, mass = 10)
        obj.momX = 100; obj.momY = 100
        obj.update(airRes = 1, maxMom = 101)
        physics.velHandler(obj, [obj]) # no other objects to run into
        self.assertTrue(obj.x == 10, "horizontal movement not proportional to momentum")

    def testMoveY(self):
        obj = physics.DynamicObject(pygame.image.load(workingDirectory.joinpath("data/assets/sprites/bluebox.png")),1, 0, 0, mass=10)
        obj.momX = 100
        obj.momY = 100
        obj.update(airRes=1, maxMom=101)
        physics.velHandler(obj, [obj])  # no other objects to run into
        self.assertTrue(obj.y == 10, "vertical movement not proportional to momentum")

    def testOverlap(self):
        t1 = terrain.from_polygon([[0,0],[100,0],[100,2]],1)
        t2 = terrain.from_polygon([[0,0],[0,100],[2,100]],1)
        self.assertTrue(t1.mask.overlap(t2.mask,(0,0)), "terrain sharing a vertex not overlapping")

    def testhorizontalA(self):
        p1 = (0,0)
        p2 = (10,0)
        self.assertTrue(terrain.is_between(p1,p2,(5,0)))
        self.assertFalse(terrain.is_between(p1,p2,(15,0)))
        self.assertFalse(terrain.is_between(p1,p2,(1,2)))
        self.assertTrue(terrain.is_between(p1,p2,(0,0))) # if testPoint in [point1, point2]

    def testhorizontalB(self):
        p2 = (0, 0)
        p1 = (10, 0)
        self.assertTrue(terrain.is_between(p1, p2, (5, 0)))
        self.assertFalse(terrain.is_between(p1, p2, (15, 0)))
        self.assertFalse(terrain.is_between(p1, p2, (1, 2)))
        self.assertTrue(terrain.is_between(p1, p2, (0, 0)))  # if testPoint in [point1, point2]

    def testverticalA(self):
        p1 = (0,0)
        p2 = (0,10)
        self.assertTrue(terrain.is_between(p1, p2, (0,5)))
        self.assertFalse(terrain.is_between(p1, p2, (0,15)))
        self.assertFalse(terrain.is_between(p1,p2,(2,1)))
        self.assertTrue(terrain.is_between(p1, p2, (0, 0)))  # if testPoint in [point1, point2]

    def testverticalB(self):
        p2 = (0, 0)
        p1 = (0, 10)
        self.assertTrue(terrain.is_between(p1, p2, (0, 5)))
        self.assertFalse(terrain.is_between(p1, p2, (0, 15)))
        self.assertFalse(terrain.is_between(p1, p2, (2, 1)))
        self.assertTrue(terrain.is_between(p1, p2, (0, 0)))  # if testPoint in [point1, point2]

    def testDiagonalSimpleA(self):
        p1 = (0,0)
        p2 = (10,10)
        self.assertTrue(terrain.is_between(p1,p2, (5,5)))
        self.assertFalse(terrain.is_between(p1,p2, (2,0)))

    def testDiagonalSimpleB(self):
        p2 = (0,0)
        p1 = (10,10)
        self.assertTrue(terrain.is_between(p1,p2, (5,5)))
        self.assertFalse(terrain.is_between(p1,p2, (2,0)))

    def testDiagonalA(self):
        p1 = (0,0)
        p2 = (200,69)
        self.assertTrue(terrain.is_between(p1,p2,(100,35)))
        self.assertFalse(terrain.is_between(p1,p2,(100,37)))

    def testDiagonalB(self):
        p2 = (0,0)
        p1 = (200,69)
        self.assertTrue(terrain.is_between(p1,p2,(100,35)))
        self.assertFalse(terrain.is_between(p1,p2,(100,37)))

    def testIsBetweenLeftovers(self): # are all points in an outline put into an edge?
        points = [[0,0],[69,420],[33,380],[11,69]]
        obj = terrain.from_polygon(points,1)
        outline = []; edges = []
        for point in obj.mask.outline():
            if point not in outline:
                outline.append(point)
        for i in range(len(points)):
            edges.append(list(filter((partial(terrain.is_between, points[i], points[(i + 1) % len(points)])), outline)))

        leftovers = []
        for point in outline:
            PointInEdges = False
            for edge in edges:
                if point in edge:
                    PointInEdges = True
                    break
            self.assertTrue(PointInEdges)

if __name__ == '__main__':
    unittest.main()
