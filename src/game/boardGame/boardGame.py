import pygame
import math
import time
import src.engine.scenecreator.drawTileMap as drawTileMap
import random
from src.game.boardGame.boardPlayers import BoardPlayer
from enum import Enum, auto
from src.game.boardGame2.board import Board
from src.game.boardGame2.spriteLoader import SpriteLoader

"""
    File authored by Joel Tanig
"""


class States(Enum):
    PLAYERMOVE = auto()
    ANNIMATING = auto()
    STARTMINIGAME = auto()


def getTypeOfTile(currentTile, player):
    if currentTile.typeOfTile == "Regular":
        # If it is a regular tile, we just need to give them 5 coins
        player.setMoney(5)
    elif currentTile.typeOfTile == "Dual":
        pass
    elif currentTile.typeOfTile == "Store":
        pass
    elif currentTile.typeOfTile == "Bad":
        amountLost = rollOfDice(6)
        player.setMoney(amountLost)
    elif currentTile.typeOfTile == "Gate":
        pass


"""
    Rolls one dice
    
    :param: x - how many sides the dice has
    :return: - int type: dice roll 

"""


def rollOfDice(x):
    return random.choice(range(1, x + 1))


"""
    The function determines who gets to go first in using 2 dice rolls. It edits the player method of 
    .setPlacementsInGame. This function does not return anything and it does not sort by placements
    so sorting would have to happen using the .sort method right after this function is called
    
    :param: listOfPlayers - listOfPlayerObjects to be edited
    :param: listOfPlacements - listofPlacements is a list of 0 number of 0 associated with each player
    :param: listOfDice - listOfDice is a list of dice the game in rolling associated with (eg. 6) with 4 players
    = [6, 6, 6, 6]
    :return: - None 

"""


def setPlacementsForBoardPlayers(listOfPlayers, listOfPlacements, listOfDice):
    while True:
        listOfDice = list(map(lambda x: rollOfDice(x) + rollOfDice(x), listOfDice))
        print(listOfDice)
        listOfDiceSet = set(listOfDice)
        # If there is no duplicates, break
        if len(listOfDice) == len(listOfDiceSet):
            break

    # We now have the placements of each player on who will now go in order
    for i in range(len(listOfDice)):
        maxValue = max(listOfDice)
        maxIndex = listOfDice.index(maxValue)
        listOfPlacements[maxIndex] = i + 1
        listOfDice[maxIndex] = 0
        print("List of placements is", listOfPlacements)
    for i in range(len(listOfDice)):
        listOfPlayers[i].setPlacementInGame(listOfPlacements[i])
        print("List of placements is", listOfPlayers[i].getPlacementInGame())


"""
    The function is determines who goes first as each player gets to roll dice to determine their fate
    
    :param: mainWindow - window of the game
    :param: scale - the scale of the game
    :param: frameRate - frame rate of the game
    :return: - None 
    
"""


def goesFirstScreen(mainWindow, scale, frameRate, listOfPlayers, board):
    clock = pygame.time.Clock()  # Clock used for frame rate
    # First start the game by rolling dice, this will contain no duplicates
    listOfPlacements = [0, 0, 0, 0]
    listOfDice = [6, 6, 6, 6]
    setPlacementsForBoardPlayers(listOfPlayers, listOfPlacements, listOfDice)
    # Sort players by placements
    listOfPlayers.sort()
    # @NEED TO DO SOME SORT OF SCREEN THAT "ROLLS" DICE (Exciting) :)

    isRunning = True
    while isRunning:
        clock.tick(frameRate)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                isRunning = False


"""
    The function is runs the logic of when it's a player turn
    
    :param: player - the player who's turn it is
    :return: - None 
    
"""


#TODO: Refactor this later
def getPlayerTurn(player, board):
    # We are going to assume 2 dice rolls for now
    diceRoll = rollOfDice(3)
    # @Need someone to animate this dice roll stuff
    return diceRoll
    # @Need to get andrew's graph working so i can even do this check with the tiles
    # Second check, from the method, do what the tile says and set params from the player class
    # Repeat until all players have gone and done a turn so we can do the mini game


"""
    The function is what starts the BoardGame and is the runner for the main game and the mini-games

    :param: mainWindow - window of the game
    :param: scale - the scale of the game
    :param: frameRate - frame rate of the game
    :return: - None 
    
"""


def startGame(mainWindow, scale, framerate, board):
    currentState = States.PLAYERMOVE
    currentPlayer = 0
    moveTracker = 0
    numOfSpots = 0
    playerSelectFork = 0
    clock = pygame.time.Clock()
    # init the players
    playerOne = BoardPlayer(1)
    playerTwo = BoardPlayer(2)
    playerThree = BoardPlayer(3)
    playerFour = BoardPlayer(4)
    playerOne.image = SpriteLoader().loadImage("testPlayer.png")
    playerTwo.image = SpriteLoader().loadImage("testPlayer2.png")
    playerThree.image = SpriteLoader().loadImage("testPlayer3.png")
    playerFour.image = SpriteLoader().loadImage("testPlayer4.png")
    # TODO: NEED TO GET THE TILE MAP FROM ANDREW

    listOfPlayers = [playerOne, playerTwo, playerThree, playerFour]

    firstIterationOfGame = True
    while True:
        clock.tick(framerate)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                break
            pos = pygame.mouse.get_pos()
            if firstIterationOfGame:
                # This is to activate the screen on who goes first
                firstIterationOfGame = not firstIterationOfGame
                goesFirstScreen(mainWindow, scale, framerate, listOfPlayers, board)
                continue
            # Game starts here
            # for each player in listOfPlayers, make them do a move by rolling dice and going to a tile
            if currentState == States.PLAYERMOVE:
                moveTracker = getPlayerTurn(listOfPlayers[currentPlayer], board)
                currentState = States.ANNIMATING
            if currentState == States.ANNIMATING:
                nextTiles = board.getPotentialMoves(listOfPlayers[currentPlayer])
                # If I see a fork in the road, then we need to pick which path to go to next
                if len(nextTiles) > 1:
                    # TODO: Need to make the selection screen for multiple paths
                    if playerSelectFork == 0:
                        board.movePlayer(nextTiles[0], listOfPlayers[currentPlayer])
                    elif playerSelectFork == 1:
                        board.movePlayer(nextTiles[1], listOfPlayers[currentPlayer])
                    elif playerSelectFork == 2:
                        board.movePlayer(nextTiles[2], listOfPlayers[currentPlayer])
                else:
                    # If we have no fork in the road, then we just go straight
                    board.movePlayer(nextTiles[0], listOfPlayers[currentPlayer])
                numOfSpots += 1
            if numOfSpots == moveTracker:
                # If we reach here, that means that we are done animating
                numOfSpots = 0
                # We set the player's position to where they are now within the tile after all the potential paths
                # they went
                listOfPlayers[currentPlayer].setCurrentPosition(board.getCurrentTile(listOfPlayers[currentPlayer]))
                getTypeOfTile(board.getCurrentTile(listOfPlayers[currentPlayer]), listOfPlayers[currentPlayer])
                if currentPlayer == 4:
                    currentState = States.STARTMINIGAME
                else:
                    currentPlayer += 1
                    currentState = States.PLAYERMOVE
            # Once all the players are done here, we start a random mini-game
            if States.STARTMINIGAME:
                currentPlayer = 0
                # TODO: This is where drake comes in start here Drake
                pass

    #########################################################################################
    # playerOne = BoardPlayer(1)
    # playerTwo = BoardPlayer(2)
    # playerThree = BoardPlayer(3)
    # playerFour = BoardPlayer(4)
    # listOfPlayers = [playerOne, playerTwo, playerThree, playerFour]
    # listOfPlacements = [0, 0, 0, 0]
    # listOfDice = [6, 6, 6, 6]
    # setPlacementsForBoardPlayers(listOfPlayers, listOfPlacements, listOfDice)
    # listOfPlayers.sort()
    # for i in range(len(listOfPlayers)):
    #     print(listOfPlayers[i].getPlayerID())

    ##############################################################################################
