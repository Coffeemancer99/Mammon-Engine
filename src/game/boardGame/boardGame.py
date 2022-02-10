import pygame
import math
import time
import src.engine.scenecreator.drawTileMap as drawTileMap
import random
from src.game.boardGame.BoardPlayers import BoardPlayer



def rollOfDice(x):
     return random.choice(range(1, 6+1))


def goesFirstScreen(mainWindow, scale, framerate, listOfPlayers):
    clock = pygame.time.Clock()  # Clock used for frame rate
    # First start the game by rolling dice
    p1Dice = 0
    p2Dice = 0
    p3Dice = 0
    p4Dice = 0
    listOfDice = [p1Dice, p2Dice, p3Dice, p4Dice]
    queen = list(map(rollOfDice, listOfDice))
    print(queen)
    isRunning = True
    while (isRunning):
        clock.tick(framerate)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                isRunning = False
        # for i in range(len(listOfDice)):
        #     listOfDice[i] = rollOfDice(6)
        map(rollOfDice, listOfDice)
    # Need to check who has the highest dice

def startGame(mainWindow, scale, framerate):
    # PLACE IMAGES
    # Load the map
    # currMap = getGameMap()
    # drawTileMap.drawScene(mainWindow, currMap, images)
    clock = pygame.time.Clock()
    # init the players
    playerOne = BoardPlayer(1)
    playerTwo = BoardPlayer(2)
    playerThree = BoardPlayer(3)
    playerFour = BoardPlayer(4)
    listOfPlayers = [playerOne, playerTwo, playerThree, playerFour]

    firstIterationOfGame = True
    isRunning = True
    while (isRunning):
        clock.tick(framerate)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                isRunning = False
            pos = pygame.mouse.get_pos()
            if firstIterationOfGame:
                firstIterationOfGame = not firstIterationOfGame
                goesFirstScreen(mainWindow, scale, framerate, listOfPlayers)
                continue

            # Have a else statement that starts the game