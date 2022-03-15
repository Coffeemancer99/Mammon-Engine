import pygame

#A player class for the dancing minigame engine. Need to communicate with note.py class
class dancePlayer():
    def __init__(self, left, right, up, down):
        self.left = left
        self.right = right
        self.up = up
        self.down = down
        self.score = 0

    def checkInput(self):
        danceInput = pygame.key.get_pressed()
        if(danceInput[self.left]):
            return self.left
        if(danceInput[self.right]):
            return self.right
        if(danceInput[self.up]):
            return self.up
        if(danceInput[self.down]):
            return self.down

