#Authored by Drake Farmer

import random
import time
import src.minigame as minigames
import pygame
import pygame.freetype
import os
import sys
pygame.font.init()
#pygame.freetype.init()
sysfont = pygame.font.get_default_font()                            # Initialize font

#>> INITIALIZE VARIABLES
atMaxFlag = 0                   # Used to keep track of whether or not we have reached max speed during spinup
atStartFlag = 0                 # Used to keep track of whether or not we have reached the start speed during spinDown
startSpeed = 0                  # Used if spinDown is enabled

#>> SETTINGS
debug = 1                       # display error messages if set to 1, verbose if set to 2
spinnerSize = 3              # How many tags show up on the spinner.     Default is 3
growRate = 10                   # Rate at which spinner grows and shrinks   Default is 10
spinnerMargin = 10              # How much of a margin the spinner box has  Default is 10
tagBuffer = 5/spinnerSize       # How much space is between each tag        Default is 5
FONTCOLOR = (0, 0, 0)           # Color used for font
spinUp = 1                      # if set to 1, spinner will "speed up" to, rather than start at spinnerSpeed
spinDown = 1                    # if set to 1, spinner will spin down when reaching the selection
spinnerSpeed = 0.5                # this sets the starting speed of the spinner. 0 is fastest
                                # If using spinUp, this is the speed the wheel will START at
speedRate = 1                   # if using spinUp, this is the exponential rate the spinner will speed up to.
                                #   (x = x * speedRate). Setting this to 1 makes the speed increase linear
acceleration = .05              # if using spinUp, this is the starting value that the spinner will begin to
                                # accelerate by
maxSpeed = 0                    # if using spinUp, this sets the maximum speed of the spinner
preFill = 0                     # Pre-fills the spinner on initiation. [DO NOT USE! DOES NOT WORK!]

#>> UPDATING VARIABLES
if(spinDown):startSpeed = spinnerSpeed


# Calling runMinigame will display a rotating list of minigames, select one, and run it
# Once a minigame has ended it returns the scores and runMinigame will reward players

# IMPORTANT!
    # Minigame return is expected to be an array of length 4

    # [p1Winnings, p2Winnings, p3Winnings, p4Winnings, item]

        # p1 winnings - p4Winnings is how much p1 won from the minigame. Accepts positive and negative ints
        # item is only used during duel minigames. Any other minigames should return "None" here!


# Create a class that we will call to create spinner objects easily
class spinnerTag():
    def __init__(self, mainWindow, x, y, width, height, maxHeight, scale, sprite, name, growRate):
        self.mainWindow = mainWindow    #Holds the game screen
        self.x = x                      # x position of our tag
        self.y = y                      # y position of our tag
        self.width = width              # width of our tag
        self.height = height            # height of our tag
        self.maxHeight = maxHeight      # maximum height of our tag
        self.scale = scale              # game scale
        self.sprite = sprite            # image for our tag
        self.sprite = pygame.transform.smoothscale(self.sprite, ((self.width) * scale, (self.height) * scale))
        self.name = name                # name of the minigame on the tag
        self.growRate = growRate        # rate at which tag grows & shrinks
        self.font = None                # variable used to initialize font
        self.text = None                # variable used to render font

    # grow is called when the tag is at the top of the spinner and must "spin" forward
    def grow(self):
        changeRate = (self.height/self.growRate)    # Get the growth rate
        self.height = self.height + changeRate      # grow the tag
        if(self.height > self.maxHeight):           # Make sure we haven't exceeded the maximum height of the tag
            self.height = self.maxHeight            # This part is a bit weird, since the spinner waits for this guy to
            return True                             # grow before advancing the spinner
        self.sprite = pygame.transform.smoothscale(self.sprite, (self.width, self.height )) # Resize the tag
        self.y = self.y + changeRate#((self.maxHeight-(spinnerMargin/2))/self.growRate)
        # Move tag down slightly

    # shrink is called when the tag is at the bottom of the spinner and must "spin" backwards
    def shrink(self):
        changeRate = (self.height/self.growRate)    # Get the growth rate
        self.height = self.height - changeRate      # Shrink the tag
        if(self.height < 0):                        # Make sure we don't divide by zero
            self.height = 1
        self.sprite = pygame.transform.smoothscale(self.sprite, (self.width, self.height)) # Resize the tag
        self.y = self.y + (changeRate+(changeRate/self.growRate))#(self.height/self.growRate)#((self.maxHeight-(spinnerMargin/2))/self.growRate)
        # to move down while shrinking, take the change rate and add in the change rate divided by the grow rate to
        # adjust for the area of the tag we are losing

    # move is called when the tag is in the center and must just move down the spinner
    def move(self, spinnerHeight, spinnerY):
        #changeRate = (((self.y-((self.height+spinnerMargin)/self.growRate))-spinnerY)/self.growRate)
        #changeRate = (((spinnerHeight-(self.height+tagBuffer))-(self.y-spinnerY))/growRate)/(spinnerSize-2)
        changeRate = ((((spinnerHeight-(self.height+tagBuffer)) - (self.y - spinnerY)) - (tagBuffer*(spinnerSize-2)))/growRate)
        # to get the rate of change for our tag, we find the area of the spinner box minus our tag space, subtract the
        # area above our tag, remove the buffer space for our other tags, and then divide the remaining space based on
        # the grow rate
        self.y = self.y + changeRate
        #print("New Y Position for minigame ",self.name,": ", self.y)

    def renderText(self):
        self.font = pygame.font.SysFont(sysfont, int(self.height))
        self.text = self.font.render(self.name, True, FONTCOLOR)
        textRect = self.text.get_rect(center=(self.x+(self.width/2), self.y+(self.height/2)))
        self.mainWindow.blit(self.text, textRect)


                            # Set the path to the minigame folder

def runMinigame(mainWindow, scale, framerate, players, spinnerSpeed=spinnerSpeed, acceleration=acceleration, atMaxFlag=atMaxFlag, atStartFlag=atStartFlag):
    path = "/../../minigame"
    #>> INITIALIZE VARIABLES
    clock = pygame.time.Clock()                                         # Used for framerate
    isRunning = True                                                    # Used to maintain gameloop
    spinnerHeight = 0                                                   # Height of our spinner box
    winX = mainWindow.get_width()                                       # Get the x-dimension of the window
    winY = mainWindow.get_height()                                      # Get the y-dimension of the window
    pointer = 0                                                         # Keep track of where we are in the games list
    spins = 0                                                           # How many times will the spinner spin?
    gamePool = [None] * spinnerSize  # Array to hold minigames actively on the spinner

    winningPlayer = None                                                #Identifies winner and loser in duels
    losingPlayer = None                                                 #Identifies winner and loser in duels
    itemIndex = None                                                    #Stores item index of item for item duels

    #>> PRE-LOADING
    spinnerBG = pygame.image.load("data/assets/sprites/bluebox.png")    # pre-load background image for the spinner
    tagBG = pygame.image.load("data/assets/sprites/testingButton.png")  # pre-load background image for spinner tag

    if(debug):print("Finding minigames in " + os.getcwd() + path)
    path=os.getcwd()+"/src/game/boardGame"+path
    gameList = os.listdir(path)                                         # Get all of the minigame names from the minigame folder

    if(debug):
        print("Minigames found:")
        for (names) in gameList:
            print(names + " | ", end='')
        print()
        print("Scale: ", scale)
        print("winX: ", winX)
        print("winY: ", winY)

    # Old function that would fill gameList with only the names of the directories in minigame
    #for i in range(spinnerSize):                       # fill our gamePool array with first games up to spinnerSize
    #    if(debug):print("i: ", i, ". pointer: ", pointer)
    #    gamePool.append(gameList[pointer])
    #    pointer = pointer + 1
    #if(debug):print(gamePool)


    spinnerHeight = (winY/(3*scale))        # Set the height of the spinnerBox to be 1/3 the size of the height of the window
    spinnerWidth = (winX/(2*scale))         # Set the width of the spinnerBox to be half the size of the width of the window
    spinnerX = (winX/2)-(spinnerWidth/2)    # Set the spinner X location by adding half the width of the spinnerbox to half the width of the window
    spinnerY = (winY/2)-(spinnerHeight/2)   # Set the spinner Y location by adding half the height of the spinnerbox to half the height of the window
    spinnerBG = pygame.transform.scale(spinnerBG, (spinnerWidth, spinnerHeight))     #Set the size of the spinnerBG, then draw it
    mainWindow.blit(spinnerBG, ((winX/2)-(spinnerWidth/2), (winY/2)-(spinnerHeight/2)))
    tagHeight = ((spinnerHeight-spinnerMargin) / spinnerSize) - tagBuffer            # Save our tag height for future use
    tagWidth = spinnerWidth - spinnerMargin                                          # Save our tag width for future use

    spins = random.randrange( len(gameList), (spinnerSize*len(gameList)) )
    # Randomly generate a number of spins based on a number between the number of minigames and the number of
    # tags times the number of minigames

    if(debug):
        print("spinnerHeight: ", spinnerHeight,
              "spinnerWidth: ", spinnerWidth,
              "tagHeight: ", tagHeight,
              "winX/2: ", winX/2,
              "winY/2: ", winY/2,
              "tagPos: ", (winY/2+((tagHeight/2)*(spinnerSize-0))))

    # If enabled, preFill will already fill the spinnerBox with tags to give the impression of a spinning cylinder,
    # rather than watching the tags "spin" into view
    # !!! THIS DOES NOT WORK, DO NOT ENABLE !!!
    if(preFill):
        for i in range(spinnerSize):                # Create a tag based on how many tags we want in the spinner
            # mainWindow, x, y, width, height, maxHeight, scale, sprite, name, growRate
            if(i==spinnerSize-1):                   #Is this the last spinner?
                newHeight = tagHeight / growRate    #Make it shorter to fit
            else:
                newHeight = tagHeight
            # Create the tag
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
            if(debug):print(">>",tagHeight, spinnerSize, i, tagHeight*(spinnerSize-(i+1)))
            pointer = pointer + 1                   # This pointer keeps track of where we are in the minigames list
            if(pointer>=len(gameList)):             # Edgecase in case somebody sets spinnerSize > total minigames
                pointer = 0
            gamePool[i] = tag                       #Add this tag into our gamePool array
        if(debug):
            for tag in gamePool:
                print(tag.name, "|", tag.y, ", ", tag.height)
    else:
        # Alternatively, just put the first tag in and let the rest cycle in naturally
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
        pointer = pointer + 1                       # This pointer keeps track of where we are in the minigame directory
        gamePool[0] = tag                           # Add this to our gamePool array

    ##>> START OF MINIGAME MANAGER LOOP
    while (isRunning):
        clock.tick(framerate)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                isRunning = False
        # Set up the variables for spinUp
        if(spinUp and not atMaxFlag):                           # Should we accelerate?
            spinnerSpeed = spinnerSpeed - acceleration          # decrease the delay
            acceleration = (acceleration * speedRate)           # Increase acceleration
            if(debug==2):print("Speed after removing acceleration: ", spinnerSpeed)
            if(spinnerSpeed<maxSpeed):                          # Did we reach maximum speed?
                if(debug):print("At maximum speed, speed: ", spinnerSpeed, " maxSpeed: ", maxSpeed)
                atMaxFlag = 1                                   # Don't come here again
                spinnerSpeed = maxSpeed                         # Set speed to maximum (in case we overshot)

        pygame.display.update()                                 # Redraw screen
        mainWindow.blit(spinnerBG, ((winX/2)-(spinnerWidth/2), (winY/2)-(spinnerHeight/2))) # Redraw the spinner box
        time.sleep(spinnerSpeed)                                # Wait the spinnerSpeed (This is how spinner speed works)
        if spins > 0:                                           # Do we still have spins left?
            # All gamePool[1+] will be full of None, which would usually throw an error. I use this horrible try/except
            # process here to avoid running into an error when the game is still filling up the gamePool
            try:
                # Go through all of gamepool and draw the tags in
                list(map(lambda x: mainWindow.blit(x.sprite, (x.x, x.y)), gamePool))  # Draw tags
            except:
                pass
            try:
                # Go through all of gamePool and draw the text in
                list(map(lambda x: x.renderText(), gamePool))
            except:
                pass
                # Grow the first tag in the gamePool array
            result = gamePool[0].grow()
            if(debug==2):
                print("Growing minigame ", gamePool[0].name)
                print("Result for minigame ",gamePool[0].name,":", result)
            try:
                # Iterate through all of the tags in the move section of gamePool and make them move.
                # (This is mostly used for when spinnerSize>3)
                for i in gamePool[1:-1]:
                    if(debug==2):print(" Moving minigame" , i.name)
                    i.move(spinnerHeight, spinnerY)
                # I could not get this to work with the map function. No clue why
                #map(lambda x: print("Moving minigame ", x.name), gamePool[1:-1])
                #map(lambda x: x.move(), gamePool[1:-1])
            except:
                pass
            try:
                # Make the final tag in our array shrink
                gamePool[-1].shrink()
                if(debug==2):print("Shrinking minigame ", gamePool[-1].name)
            except:
                pass

            if(result):                                         # Did our first tag fully grow?
                if(debug==2):print("DELETE AND SHIFT!")
                for i in range(len(gamePool)-1, 0, -1):         # Iterate backwards through gamePool
                    if(debug==2):print("Moving tag at [",i-1,"] to [",i,"]")
                    gamePool[i] = gamePool[i-1]                 # Move all tags up a location in the gamePool
                if(debug==2):print("Make a new tab")
                tag = spinnerTag(mainWindow,                    # Create a new tag
                            spinnerX + (spinnerMargin/2),
                            spinnerY + (spinnerMargin/2),
                            tagWidth,
                            tagHeight / growRate,
                            tagHeight,
                            scale,
                            tagBG,
                            gameList[pointer],
                            growRate)
                pointer = pointer + 1                           # The pointer keeps track of where we are in the minigames list
                if(pointer>=len(gameList)):                     # Do we need to wrap the pointer back around?
                    pointer = 0
                gamePool[0] = tag                               # Set our new tag in the first position of the gamePool array
                spins = spins - 1                               # Reduce our spins
                if (debug): print("Spins: ", spins)

            # Start of spinDown
            if( (spins==1) and (spinDown) and not atStartFlag):                     #Check to see if we're getting near the end
                spinnerSpeed = spinnerSpeed + acceleration                          #decrease speed
                acceleration = (acceleration /speedRate)/spinnerSize                #increase deceleration
                if (debug == 2): print("Speed after adding acceleration: ", spinnerSpeed)
                if (spinnerSpeed > startSpeed):                                     #Have we reached the starting speed?
                    if (debug): print("At start speed, speed: ", spinnerSpeed, " maxSpeed: ", startSpeed)
                    atStartFlag = 1                                                 #Make sure we don't come back
                    spinnerSpeed = startSpeed
        else:
            middle = (len(gamePool)-1)/2                    # Get the middle of the gamePool array
            selectedGame = gamePool[int(middle)].name       # Get the name of our selected game
            if(debug):print("Selected minigame is: ", selectedGame)
            gamePath = __file__ + "\..\..\..\minigame\\" + selectedGame    # Get the path to our game
            if(debug):print("grabbing launch file from: ", gamePath)
            sys.path.append(gamePath)                       # add the path to the correct minigame folder
            try:                                            # try and import the launch file
                import launch
            except:
                print("ERROR minigameManager.py, import of launch failed! Does ", selectedGame," have a python script called 'launch.py'?")
                sys.path.pop()                              # delete path to the game folder
                return True
            sys.path.pop()
            # delete the path to the game folder so we don't bloat sys.path or accidentally call another minigame
            try:
                result = launch.startGame(mainWindow,scale, framerate)  # try and run the startGame() function
            except:
                print("ERROR minigameManager.py, running startGame function failed! Does ", selectedGame, " have a function called 'startGame()'?")
                del sys.modules['launch']  # some early black magic
                return True
            if(debug):print("Result: ", result)

                                        #                   /\
                                        #                  /  \
                                        #                 |    |
                                        #               --:'''':--
                                        #                 :'_' :
                                        #                 _:"":\___
            # perform illegal python       ' '      ____.' :::     '._
            del sys.modules['launch']   # . *=====<<=)           \    :
            # black magic to delete        .  '      '-'-'\_      /'._.'
            # the imported launch                           \====:_ ""
                                        #                  .'     \\
                                        #                 :       :
                                        #                /   :    \
                                        #               :   .      '.
                                        #               :  : :      :
                                        #               :__:-:__.;--'
                                        #               '-'   '-'

            isDuel = result[4]                              # used to sort between money and item rewards
            #If index 4 of result is "item", we move on to item. Anything else we just award money
            if(isDuel != "item"):                                 # Check if duel is for money
                if(debug):print("Money - Rewarding players")
                for player in players:                      # Iterate through the players
                    player.setMoney(result[player.getPlayerID()-1]) # reward correct player
                    if(debug):print("--Rewarding Player ", player.getPlayerID(), " $", result[player.getPlayerID()-1])
            else:
                if(debug):print("Items - rewarding victor")
                # This is the item reward, used exclusively for duels
                #player location with a negative number (should be -1 for consistency) is the winner
                #player location with positive number is the loser and is also the item index in their inventory to be lost
                #losingPlayer = list(filter(lambda x: x=="loser", result))
                for i in range(len(players)):                           #Couldn't make this as a filter because I need to know array index location
                    playerID = players[i].getPlayerID()                 #Get the playerID that corresponds with this position
                    if (debug): print("[", i, "]: ", playerID)
                    if(result[playerID-1]<0):winningPlayer = players[i] #save the winning player
                    if(result[playerID-1]>0):                           #save the losing player
                        losingPlayer = players[i]
                        itemIndex = result[playerID-1]                  #save the item index
                if(debug):print("Giving player ", winningPlayer.getPlayerID(), " player ", losingPlayer.getPlayerID(), "'s item at index ", itemIndex)
                try:
                    winningPlayer.setInventory(losingPlayer.removeInventoryItem(itemIndex)) #Take item from loser and give it to winner
                except:
                    print("ERROR minigameManager.py couldn't grab item [", itemIndex, "] from player",losingPlayer.getPlayerID(),". Is the index out of range?")
            if(debug):print("Minigame state completed")
            time.sleep(2)                                   # Wait for two seconds so players can see what game won
            isRunning = False                               # End our loop
    if(debug):print("Exiting back to minigame state function")
    return False