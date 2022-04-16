import src.engine.physics.physics as physics
from src.engine.physics.physics import Object, DynamicObject, RectObject, DynamicRect
from src.engine.physics.spritegen import *
import src.engine.physics.terrain as terrain
import src.minigame.exampleGame.myObjects as myObjects
import pygame
import time
from src.minigame.timer.timer import timer as timer
framerate = 60

class seaItem(DynamicObject):
    def __init__(self, sprite, scale, x, y, objects, isBad = False, name="undefinedBall", mass = 10):
        DynamicObject.__init__(self, sprite, scale, x, y, objects, name, mass)
        self.isBad = isBad
        self.cost = 0
        bloopSound = ""
        if(self.isBad):
            bloopSound = "data/assets/sounds/damaged.mp3"
        else:
            bloopSound = "data/assets/sounds/coin.mp3"
            seq2 = "data/assets/sounds/coin2.mp3"
            seq3 = "data/assets/sounds/coin3.mp3"
            sound2 = pygame.mixer.Sound(seq2)
            sound2.set_volume(100000000)
            sound3 = pygame.mixer.Sound(seq3)
            sound3.set_volume(100000000)
            self.seq2 = sound2
            self.seq3 = sound3
        sound1 = pygame.mixer.Sound(bloopSound)
        sound1.set_volume(100000000)
        self.sound = sound1
      #  pygame.event.wait()


    def fall(self):
        self.momY += 0.35

    def damagedSound(self, consec):
        if(consec>0 and not self.isBad):
            if(consec<2):
                self.seq2.play()
            else:
                self.seq3.play()
            return
        self.sound.play()

      #  pygame.event.wait()