import pygame

class masherPlayer():
    def __init__(self, team, firstButton, secondButton):
        self.team = team
        self.currButton = 0
        self.stunTimer = 0
        self.cycles = 0
        self.firstButton = firstButton
        self.secondButton = secondButton
        self.isTurn = 0
        self.score = 0

    def getInput(self):
        if self.stunTimer < 0: #If the player is stunned, decrease timer
            self.stunTimer -= 1
            return
        buttonPressed = pygame.key.get_pressed() #Get user input
        if(buttonPressed[self.firstButton] and self.currButton == 0): #If it is their turn to press the right key
            if(self.isTurn):
                self.currButton = 1
                self.isTurn=0
                return 1 #Pass the turn over
            else:
                print("You pressed when it wasn't your turn!")
                stunTimer = 90
                return 0 #Pass the turn over
        elif(buttonPressed[self.secondButton] and self.currButton == 1): #If it is their turn to press the left key
            if(self.isTurn):
                self.currButton = 0
                self.cycles += 1  # Back to beginning, increase score/cycle count
                self.isTurn = 0
                self.score += 1
                return 1 #Pass the turn over
            else:
                print("You pressed when it wasn't your turn!")
                stunTimer = 90
                return 0 #Pass the turn over




