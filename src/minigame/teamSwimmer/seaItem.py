import src.engine.physics.physics as physics
from src.engine.physics.physics import Object, DynamicObject, RectObject, DynamicRect
from src.engine.physics.spritegen import *
import src.engine.physics.terrain as terrain
import src.minigame.exampleGame.myObjects as myObjects
import pygame
import time
from src.minigame.timer.timer import timer as timer
framerate = 60
"""
    seaItem: This class inherits DynamicObjects and serves as an item that the players must grab/avoid 
    in the minigame "Earn your Keep" (Team Swimmer). 
    Parameters:
        :param sprite: The sprite to be rendered in the main game loop
        :param scale: The scale of the sprite 
        :param x: The x position of the item
        :param y: The y position of the item 
        :param objects: All the objects currently in the scene
        :param fallSpeed: The speed the object falls, determined randomnly in the dropCoin function in teamSwimmer.py
        :param isBad: Determines if the item is a bad item (skull) which will make players lose points and stun them shortly
        :param name: The name of the item
        :param mass: The mass of the item 
"""
class seaItem(DynamicObject):
    def __init__(self, sprite, scale, x, y, objects, fallSpeed, isBad = False, name="undefinedBall", mass = 10):
        DynamicObject.__init__(self, sprite, scale, x, y, objects, name, mass)
        self.isBad = isBad
        self.cost = 0
        bloopSound = ""
        self.fallSpeed = fallSpeed*scale
        self.x=x
        self.y=y
        self.alive = True
        #If the item is bad, we only need to worry about loading one sound
        if(self.isBad):
            bloopSound = "data/assets/sounds/damaged.mp3"
        #If the item is good, we need to worry about loading multiple sounds to have a consecutive sound change
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

    def fall(self):
        self.momY += 0.35*self.fallSpeed

    def damagedSound(self, consec):
        if(consec>0 and not self.isBad): #If the player has grabbed one coin prior..
            if(consec<2): #Player two pitches higher
                self.seq2.play()
            else: #Play one pitch higher
                self.seq3.play()
            return
        self.sound.play() #Otherwise just play the normal sound

    def timeUntilDeletion(self):
        pass