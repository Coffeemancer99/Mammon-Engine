#Authored by Drake Farmer

import random
import src.minigame as minigames
import pygame
import os

# Calling runMinigame will display a rotating list of minigames, select one, and run it
# Once a minigame has ended it returns the scores and runMinigame will reward players

# IMPORTANT!
    # Minigame return is expected to be an array of length 4

    # [p1Winnings, p2Winnings, p3Winnings, p4Winnings, item]

        # p1 winnings - p4Winnings is how much p1 won from the minigame. Accepts positive and negative ints
        # item is only used during duel minigames. Any other minigames should return "None" here!


def runMinigame(mainWindow, scale, framerate):
    clock = pygame.time.Clock()
    isRunning = True
    gameList = []
    # Do once:
        # Get minigames, save to array
        # Draw background rectangle
        # initial draw of first 3 minigames on rectangle
        # Create array of len 2 to hold 3 minigames on "wheel"
    for (dirs) in os.walk(minigames):
        for name in dirs:
            gameList.append(name)

    print("Minigames found:")
    for (names) in gameList:
        print(names + " | ")



    while (isRunning):
        clock.tick(framerate)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                isRunning = False

#Set up secondary game loop

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