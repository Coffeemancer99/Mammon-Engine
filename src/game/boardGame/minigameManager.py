#Authored by Drake Farmer

import random
import time
import src.minigame as minigames
import pygame
import pygame.freetype
import os
pygame.font.init()
pygame.freetype.init()
# S E T T I N G S
debug = 1                       # display error messages if set to 1, verbose if set to 2
spinnerSize = 3                 # How many tags show up on the spinner.     Default is 3
growRate = 10                   # Rate at which spinner grows and shrinks   Default is 10
spinnerMargin = 10              # How much of a margin the spinner box has  Default is 10
tagBuffer = 5/spinnerSize       # How much space is between each tag        Default is 5
BLACK = (0, 0, 0)               # Color used for font
spinnerSpeed = 0.05             # Speed of the spinner loop
preFill = 0                     # Pre-fills the spinner on initiation. [DO NOT USE! DOES NOT WORK!]

sysfont = pygame.font.get_default_font()                            # Initialize font


# Calling runMinigame will display a rotating list of minigames, select one, and run it
# Once a minigame has ended it returns the scores and runMinigame will reward players

# IMPORTANT!
    # Minigame return is expected to be an array of length 4

    # [p1Winnings, p2Winnings, p3Winnings, p4Winnings, item]

        # p1 winnings - p4Winnings is how much p1 won from the minigame. Accepts positive and negative ints
        # item is only used during duel minigames. Any other minigames should return "None" here!


# Create a class that we will call to create spinner objects easily
    # mainWindow: game screen
    # x: x position of tag
    # y: y position of tag
    # width: width of tag
    # height: height of tag
    # maxHeight: maximum height of our tag
    # scale: Scale of the game window
    # sprite: sprite image
    # name: name on tag
class spinnerTag():
    def __init__(self, mainWindow, x, y, width, height, maxHeight, scale, sprite, name, growRate):
        self.mainWindow = mainWindow
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.maxHeight = maxHeight
        self.scale = scale
        self.sprite = sprite
        self.sprite = pygame.transform.scale(self.sprite, ((self.width) * scale, (self.height) * scale))
        self.name = name
        self.growRate = growRate                                      # Basically, will grow to max / shrink to min in 10 frames
        self.font = None
        self.text = None


    def grow(self):
        changeRate = (self.height/self.growRate)
        self.height = self.height + changeRate
        if(self.height > self.maxHeight):
            self.height = self.maxHeight
            return True
        self.sprite = pygame.transform.smoothscale(self.sprite, (self.width, self.height ))
        self.y = self.y + changeRate#((self.maxHeight-(spinnerMargin/2))/self.growRate)

    def shrink(self):
        changeRate = (self.height/self.growRate)
        self.height = self.height - changeRate
        if(self.height < 0):
            self.height = 1
        self.sprite = pygame.transform.smoothscale(self.sprite, (self.width, self.height))
        self.y = self.y + (changeRate+(changeRate/self.growRate))#(self.height/self.growRate)#((self.maxHeight-(spinnerMargin/2))/self.growRate)


    def move(self, spinnerHeight, spinnerY):
        #changeRate = (((self.y-((self.height+spinnerMargin)/self.growRate))-spinnerY)/self.growRate)
        changeRate = (((spinnerHeight-(self.height+tagBuffer))-(self.y-spinnerY))/growRate)/(spinnerSize-2)
        self.y = self.y + changeRate
        #print("New Y Position for minigame ",self.name,": ", self.y)

    def renderText(self):
        self.font = pygame.font.SysFont(sysfont, int(self.height))
        self.text = self.font.render(self.name, True, BLACK)
        textRect = self.text.get_rect(center=(self.x+(self.width/2), self.y+(self.height/2)))
        self.mainWindow.blit(self.text, textRect)


path = __file__ + "\..\..\..\minigame"                              # Set the path to the minigame folder

def runMinigame(mainWindow, scale, framerate, players):
    clock = pygame.time.Clock()                                         # Used for framerate
    isRunning = True
    spinnerBG = pygame.image.load("data/assets/sprites/bluebox.png")    # pre-load background image for the spinner
    spinnerHeight = 0                                                   # Height of our spinner box
    tagBG = pygame.image.load("data/assets/sprites/testingButton.png")     # pre-load background image for spinner tag
    winX = pygame.display.get_surface().get_size()[0]                   # Get the x-dimension of the window
    winY = pygame.display.get_surface().get_size()[1]                   # Get the y-dimension of the window
    pointer = 0                                                         # Keep track of where we are in the games list
    spins = 0                                                           # How many times will the spinner spin?
    gamePool = [None] * spinnerSize                                                       # Array to hold minigames actively on the spinner

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
    tagHeight = ((spinnerHeight-spinnerMargin) / spinnerSize) - tagBuffer                         # Save our tag height for future use
    tagWidth = spinnerWidth - spinnerMargin                             # Save our tag width for future use

    spins = random.randrange( len(gameList), (spinnerSize*len(gameList)) )  # How many times will we spin the spinner?

    if(debug):
        print("spinnerHeight: ", spinnerHeight,
              "spinnerWidth: ", spinnerWidth,
              "tagHeight: ", tagHeight,
              "winX/2: ", winX/2,
              "winY/2: ", winY/2,
              "tagPos: ", (winY/2+((tagHeight/2)*(spinnerSize-0))))

    if(preFill):
        for i in range(spinnerSize):                                        # Fill gamePool with some games to initiate the spinning
            # mainWindow, x, y, width, height, maxHeight, scale, sprite, name, growRate
            if(i==spinnerSize-1):
                newHeight = tagHeight / growRate
            else:
                newHeight = tagHeight
            tag = spinnerTag(mainWindow,
                        spinnerX,
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

    # BTW not doing this to get extra lines, doing this for readability. Up to you if you wanna count this as one line or 10
    tag = spinnerTag(mainWindow,
            spinnerX + (spinnerMargin/2),
            spinnerY + (spinnerMargin/2),
            tagWidth,
            tagHeight / growRate,
            tagHeight,
            scale,
            tagBG,
            gameList[pointer],
            growRate)
    pointer = pointer + 1
    gamePool[0] = tag
    while (isRunning):
        clock.tick(framerate)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                isRunning = False
        pygame.display.update()
        mainWindow.blit(spinnerBG, ((winX/2)-(spinnerWidth/2), (winY/2)-(spinnerHeight/2)))
        time.sleep(spinnerSpeed)
        if spins > 0:
            # All gamePool[1+] will be full of None, which would usually throw an error. I use this horrible try/except process
            # here to avoid running into an error when the game is still filling up the gamePool
            try:
                list(map(lambda x: mainWindow.blit(x.sprite, (x.x, x.y)), gamePool))  # Draw tags
            except:
                pass
            try:
                list(map(lambda x: x.renderText(), gamePool))
            except:
                pass
            result = gamePool[0].grow()
            if(debug==2):
                print("Growing minigame ", gamePool[0].name)
                print("Result for minigame ",gamePool[0].name,":", result)
            try:
                for i in gamePool[1:-1]:
                    if(debug==2):print(" Moving minigame" , i.name)
                    i.move(spinnerHeight, spinnerY)
                #map(lambda x: print("Moving minigame ", x.name), gamePool[1:-1])
                #map(lambda x: x.move(), gamePool[1:-1])
            except:
                pass
            try:
                pass
                gamePool[-1].shrink()
                if(debug==2):print("Shrinking minigame ", gamePool[-1].name)
            except:
                pass

            if(result):
                if(debug==2):print("DELETE AND SHIFT!")
                for i in range(len(gamePool)-1, 0, -1):
                    if(debug==2):print("Moving tag at [",i-1,"] to [",i,"]")
                    gamePool[i] = gamePool[i-1]
                if(debug==2):print("Make a new tab")
                tag = spinnerTag(mainWindow,
                            spinnerX + (spinnerMargin/2),
                            spinnerY + (spinnerMargin/2),
                            tagWidth,
                            tagHeight / growRate,
                            tagHeight,
                            scale,
                            tagBG,
                            gameList[pointer],
                            growRate)
                pointer = pointer + 1
                if(pointer>=len(gameList)):
                    pointer = 0
                gamePool[0] = tag
                spins = spins - 1
                if (debug): print("Spins: ", spins)

        else:
            print("!!! SPINNER HAS STOPPED SPINNING !!!")
            middle = (len(gamePool)-1)/2
            selectedGame = gamePool[int(middle)].name
            print("Selected minigame is: ", selectedGame)
            result = [1, 2, 3, 4, None]#Launch minigame here minigame folder -> minigame -> gameMain.py.launch()
            gamePath = __file__ + "\..\..\..\minigame" + "\\" + selectedGame
            print("grabbing launch file from: ", gamePath)




            print("Minigame ended")
            isDuel = result[4]
            if(not isDuel):
                print("Standard - rewarding players")
                for player in players:
                    player.setMoney(result[player.getPlayerID()-1])
                    print("--Rewarding Player ", player.getPlayerID(), " $", result[player.getPlayerID()-1])
            else:
                print("Duel - rewarding victor")
                    # "loseItem" means that this player has lost the item stored in result[4]
                    # "gainItem" means that this player has gained the item stored in result[4]
                    #figure out duel logic here
            print("Minigame state completed")
            time.sleep(5)
            isRunning = False
    print("Exiting back to minigame state function")