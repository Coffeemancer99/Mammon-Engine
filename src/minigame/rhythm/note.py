from src.minigame.timer import timer
import pygame
class note():
    def __init__(self, direction, held, framerate, isHeld=False, holdTimer=0):
        self.direction = direction #Direction/button of note
        self.held = held #Does the note need to be held?
        self.timeStartup = 0.2 #Number of seconds for the user to click the timer
        #Different scores for how well the user clicks in time
        self.goodScore = 0.15
        self.okayScore = 0.10
        #Timer that ticks down and validates that notes are okay
        self.beginTime = timer.timer(self.timeStartup, framerate)
        #For held notes
        self.isHeld = isHeld
        self.holdTimer = timer.timer(holdTimer, framerate)
        self.heldScore = 0
        self.heldQuality = 0

    #Activates the note, checks if it is within the specified frame range
    def activateNote(self, userInput):
        if(userInput != self.direction):
            return #User did not the direction of this note
        if(self.beginTime.currTime>=self.goodScore): #Good hit
            return 3
        elif(self.beginTime.currTime>=self.okayScore): #Okay hit
            return 2
        elif(self.beginTime.currTime>=0): #There was an attempt
            return  1

    #Activates the held note, checks if they hit within a specified frame range (different for held)
    def isHeldValid(self):
        if (self.beginTime.currTime >= self.goodScore):  # Good hit
            self.isHeld = True
            self.heldQuality = 3
        elif (self.beginTime.currTime >= 0):  # Okay hit
            self.isHeld = True
            self.heldQuality = 2

    #Checks if user is still holding the value down
    def holdValid(self):
        if(self.isHeld and self.holdTimer.currTime > 0):
            self.heldScore += self.heldQuality
        self.holdTimer.decrement()
