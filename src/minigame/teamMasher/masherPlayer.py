import pygame

class masherPlayer():
    def __init__(self, team, left, right):
        self.team = team
        self.currButton = 0
        self.stunTimer = 0
        self.cycles = 0
        self.left = left
        self.right = right

    def getInput(self):
        if self.stunTimer < 0: #If the player is stunned, decrease timer
            self.stunTimer -= 1
            return
        buttonPressed = pygame.key.get_pressed() #Get user input
        if(buttonPressed[self.right] and self.currButton == 0): #If it is their turn to press the right key
            self.currButton = 1
        elif(buttonPressed[self.left] and self.currButton == 1): #If it is their turn to press the left key
            self.currButton = 0
            self.cycles += 1 #Back to beginning, increase score/cycle count


