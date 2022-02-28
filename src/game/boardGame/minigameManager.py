#Authored by Drake Farmer

import random
import time
import src.minigame as minigames
import pygame
import os
debug = 1           # display error messages if set to 1
spinnerSize = 3     # How many tags show up on the spinner
growRate = 10       # Rate at which spinner grows and shrinks

# Calling runMinigame will display a rotating list of minigames, select one, and run it
# Once a minigame has ended it returns the scores and runMinigame will reward players

# IMPORTANT!
    # Minigame return is expected to be an array of length 4

    # [p1Winnings, p2Winnings, p3Winnings, p4Winnings, item]

        # p1 winnings - p4Winnings is how much p1 won from the minigame. Accepts positive and negative ints
        # item is only used during duel minigames. Any other minigames should return "None" here!


# Create a class that we will call to create spinner objects easily
    # x: x position of tag
    # y: y position of tag
    # width: width of tag
    # height: height of tag
    # maxHeight: maximum height of our tag
    # scale: Scale of the game window
    # sprite: sprite image
    # name: name on tag
class spinnerTag():
    def __init__(self, x, y, width, height, maxHeight, scale, sprite, name, growRate):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.maxHeight = maxHeight
        self.scale = scale
        self.sprite = sprite
        self.sprite = pygame.transform.scale(self.sprite, ((width) * scale, (height) * scale))
        self.name = name
        self.growRate = growRate                                      # Basically, will grow to max / shrink to min in 10 frames


    def grow(self):
        changeRate = (self.growRate/self.height)*2
        self.height = self.height + changeRate
        if(self.height > self.maxHeight):
            self.height = self.maxHeight
            return True
        self.sprite = pygame.transform.scale(self.sprite, (self.width, self.height ))
        self.y = self.y - changeRate/2.5

    def shrink(self):
        changeRate = (self.growRate/self.height)*2
        self.height = self.height - changeRate
        if(self.height < 0):
            self.height = 1
        self.sprite = pygame.transform.scale(self.sprite, (self.width, self.height))
        self.y = self.y - changeRate/2.5


    def move(self):
        changeRate = (self.growRate/self.height)
        self.y = self.y - changeRate/2.5


path = __file__ + "\..\..\..\minigame"                              # Set the path to the minigame folder

def runMinigame(mainWindow, scale, framerate):
    clock = pygame.time.Clock()                                         # Used for framerate
    isRunning = True
    spinnerBG = pygame.image.load("data/assets/sprites/bluebox.png")    # pre-load background image for the spinner
    spinnerHeight = 0                                                   # Height of our spinner box
    tagBG = pygame.image.load("data/assets/sprites/testingButton.png")     # pre-load background image for spinner tag
    winX = pygame.display.get_surface().get_size()[0]                   # Get the x-dimension of the window
    winY = pygame.display.get_surface().get_size()[1]                   # Get the y-dimension of the window
    pointer = 0                                                         # Keep track of where we are in the games list
    spins = 0                                                           # How many times will the spinner spin?
    gamePool = []                                                       # Array to hold minigames actively on the spinner

    if(debug):print("Finding minigames in " + os.getcwd() + path)
    gameList = os.listdir(path)                                         # Get all of the minigame names from the minigame folder

    if(debug):
        print("Minigames found:")
        for (names) in gameList:
            print(names + " | ", end='')
        print()
        print("Scale: ", scale)
        print("winX: ", winX)
        print("winY: ", winY)

    #for i in range(spinnerSize):                                        # fill our gamePool array with first games up to spinnerSize
    #    if(debug):print("i: ", i, ". pointer: ", pointer)
    #    gamePool.append(gameList[pointer])
    #    pointer = pointer + 1
    #if(debug):print(gamePool)


    spinnerHeight = (winY/(3*scale))
    spinnerWidth = (winX/(2*scale))
    spinnerX = (winX/2)-(spinnerWidth/2)
    spinnerY = (winY/2)-(spinnerHeight/2)
    spinnerBG = pygame.transform.scale(spinnerBG, (spinnerWidth, spinnerHeight))     #Set the size of the spinnerBG, then draw it
    mainWindow.blit(spinnerBG, ((winX/2)-(spinnerWidth/2), (winY/2)-(spinnerHeight/2)))
    tagHeight = spinnerHeight / spinnerSize                             # Save our tag height for future use

    spins = random.randrange( len(gameList), (spinnerSize*len(gameList)) )  # How many times will we spin the spinner?

    if(debug):
        print("spinnerHeight: ", spinnerHeight,
              "spinnerWidth: ", spinnerWidth,
              "tagHeight: ", tagHeight,
              "winX/2: ", winX/2,
              "winY/2: ", winY/2,
              "tagPos: ", (winY/2+((tagHeight/2)*(spinnerSize-0))))

    for i in range(spinnerSize):                                        # Fill gamePool with some games to initiate the spinning
        # x, y, width, height, maxHeight, scale, sprite, name, growRate
        if(i==spinnerSize-1):
            newHeight = tagHeight / growRate
        else:
            newHeight = tagHeight
        tag = spinnerTag(spinnerX,
                         spinnerY+(tagHeight*(spinnerSize-(i+1))),
                         spinnerWidth,
                         newHeight,
                         tagHeight,
                         scale,
                         tagBG,
                         gameList[pointer],
                         growRate)
        print(">>",tagHeight, spinnerSize, i, tagHeight*(spinnerSize-(i+1)))
        pointer = pointer + 1
        if(pointer>=len(gameList)):                                      # Edgecase in case somebody sets spinnerSize > total minigames
            pointer = 0
        gamePool.append(tag)
    if(debug):
        for tag in gamePool:
            print(tag.name, "|", tag.y, ", ", tag.height)



    if(debug):print("Spins: ", spins)
    while (isRunning):
        clock.tick(framerate)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                isRunning = False
        pygame.display.update()
        mainWindow.blit(spinnerBG, ((winX/2)-(spinnerWidth/2), (winY/2)-(spinnerHeight/2)))
        time.sleep(0.25)
        if spins > 0:
            list(map(lambda x: mainWindow.blit(x.sprite, (x.x, x.y)), gamePool))  # Draw tags

            result = gamePool[0].grow()
            print("Result:", result)
            for i in range(1, len(gamePool)-1):
                gamePool[i].move()
            gamePool[-1].shrink()

            if(result):
                print("DELETE AND SHIFT!")
                for i in range(len(gamePool)-1, 1, -1):
                    print("delete i:", i)
                    gamePool[i] = gamePool[i-1]
                print("Make a new tab")
                tag = spinnerTag(spinnerX,
                                 spinnerY + (tagHeight * (spinnerSize - (i + 1))),
                                 spinnerWidth,
                                 tagHeight,
                                 tagHeight,
                                 scale,
                                 tagBG,
                                 gameList[pointer],
                                 growRate)
                pointer = pointer + 1
                if(pointer>=len(gameList)):
                    pointer = 0
                gamePool[0] = tag
            result = False
            # grow gamePool[0]
            # move gamePool[0]-gamePool[len(gamePool)-1]
            # if shrink gamePool[len(gamePool)]
                # move all gamepools up one
                #create a new gamepool

        else:
            pass
                        #For loop
                            #grow array[0] slightly and move down
                            #move array[1] down slightly
                            #shrink array[0] slightly
                            #if array[2] size is small enough...
                                #move array[1] to array[2]
                                #move array[0] to array[1]
                                #Create a new text display with next minigame on it, set height to start height and put in array[0]
                        #Not in for loop
                            #Once we exit for loop...
                            #Select minigame in array[1]
                            #result = minigame folder -> minigame -> gameMain.py.launch()
                            #print("Minigame ended")
                            #isDuel = result[4]
                            #if(!isDuel):
                                #print("Standard - rewarding players")
                                #player1.addmoney(result[0])
                                #player2.addmoney(result[1])
                                #player3.addmoney(result[2])
                                #player4.addmoney(result[3])
                            #else:
                                #print("Duel - rewarding victor")
                                #figure out duel logic here
                        #print("Minigame state completed")
                        #quit minigame