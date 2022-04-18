from src.engine.physics import physics as physics
from src.engine.physics.physics import DynamicObject
import pygame
from src.minigame.timer.timer import timer as timer

framerate=60
class textFloat():
    def __init__(self, scale, x, y, score, color=(0,0,0), timerEnabled=True):

        self.x = x
        self.y = y
        self.scoreFont = pygame.font.SysFont('Comic Sans MS', 30*scale)
        self.durTimer = timer(1, framerate)
        self.timerEnabled = timerEnabled
        self.sprite = self.scoreFont.render(str(score), False, color)
        self.alive = True
        self.color=color

    def timeUntilDeletion(self):
        self.durTimer.decrement()
        if(self.timerEnabled and self.durTimer.isFinished()):

            self.alive = False