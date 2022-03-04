import pygame
import time
import random
from src.game.boardGame.Store import Store
from src.game.boardGame.boardPlayers import BoardPlayer
from enum import Enum, auto
from src.game.boardGame.minigameManager import runMinigame
from src.game.boardGame2.boardRenderer import BoardRenderer
from src.game.boardGame2.spriteLoader import SpriteLoader

"""
    475 total
    File authored by Joel Tanig
    273 lines
"""


class States(Enum):
    FIRSTITERATION = auto()
    PLAYERMOVE = auto()
    ANNIMATING = auto()
    STARTMINIGAME = auto()


class DiceStates(Enum):
    DICEONE = auto()
    DICETWO = auto()


def getTypeOfTile(currentTile, player, mainWindow, scale, framerate):
    if currentTile.typeOfTile == "Regular":
        # If it is a regular tile, we just need to give them 5 coins
        player.setMoney(5)
    elif currentTile.typeOfTile == "Dual":
        pass
    elif currentTile.typeOfTile == "Store":
        return storeScreen(mainWindow, scale, framerate, player)
    elif currentTile.typeOfTile == "Bad":
        amountLost = rollOfDice(6)
        player.setMoney(amountLost)
    elif currentTile.typeOfTile == "Gate":
        pass


# TODO: Start here
# TODO: Remodel to MVC later, fix pixel math, and make new images
# This function is the "store" that will be in the game and I am using dice.png as placeholder
# images for now 
def storeScreen(mainWindow, scale, framerate, currentPlayer):
    clock = pygame.time.Clock()
    transaction = False
    store = Store()

    # TODO: Need to blit different images that relate to the storeInventory list
    gooditemOne = SpriteLoader().loadImage("die1.png")
    gooditemTwo = SpriteLoader().loadImage("die2.png")
    gooditemThree = SpriteLoader().loadImage("die3.png")
    baditemOne = SpriteLoader().loadImage("die4.png")

    gooditemOne = pygame.transform.scale(gooditemOne,
                                         ((gooditemOne.get_width()) * scale, (gooditemOne.get_height()) * scale))
    gooditemTwo = pygame.transform.scale(gooditemTwo,
                                         ((gooditemTwo.get_width()) * scale, (gooditemTwo.get_height()) * scale))
    gooditemThree = pygame.transform.scale(gooditemThree,
                                           ((gooditemThree.get_width()) * scale, (gooditemThree.get_height()) * scale))
    baditemOne = pygame.transform.scale(baditemOne,
                                        ((baditemOne.get_width()) * scale, (baditemOne.get_height()) * scale))

    mainWindow.fill((55, 55, 55))
    # Put buttons here
    mainWindow.blit(gooditemOne, (32 * scale, 32 * scale))
    mainWindow.blit(gooditemTwo, (32 * scale, 112 * scale))
    mainWindow.blit(gooditemThree, (32 * scale, 208 * scale))
    mainWindow.blit(baditemOne, (412 * scale, 356 * scale))

    isRunning = True
    while isRunning:
        pygame.display.update()
        clock.tick(framerate)  # 39
        key = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                isRunning = False
            if event.type == pygame.MOUSEBUTTONUP:
                click = pygame.mouse.get_pos()
                print(click)
                # Buying logic
                if (click[0] > 32 * scale) and (click[0] <= 488 * scale):  # x
                    if (click[1] > 24 * scale) and (click[1] <= 60 * scale):  # y
                        print("Bought Good item 1")
                        transaction = store.buyItem(currentPlayer, 0)
                    elif (click[1] > 112 * scale) and (click[1] <= 176 * scale):
                        print("Bought Good item 2")
                        transaction = store.buyItem(currentPlayer, 1)
                    elif (click[1] > 208 * scale) and (click[1] <= 252 * scale):
                        print("Bought Good item 3")
                        transaction = store.buyItem(currentPlayer, 2)
                    elif (click[1] > 304 * scale) and (click[1] <= 328 * scale):
                        print("Bad item 1")
                        transaction = store.buyItem(currentPlayer, 3)
                    if transaction:
                        currentPlayer.getInventory()
                        isRunning = False
                # TODO: Need to do selling logic
                if (click[0] > 4 * scale) and (click[0] <= 100 * scale):  # x
                    if (click[1] > 412 * scale) and (click[1] <= 444 * scale):  # y
                        print("Sold item")
                        store.sellItem(currentPlayer, 0)


"""
    This function rolls dice on the screen, it is also important to note that the dice rolls
    are already determined in the setPlacementsForBoardPlayers function as I wanted to make sure we had no
    duplicates
"""


def rollingDiceAnnimation(scale, framerate, listOfPlayers):
    # Note that scale is one for now
    # Set up all the buttons
    dice1 = SpriteLoader().loadImage("die1.png")
    dice2 = SpriteLoader().loadImage("die2.png")
    dice3 = SpriteLoader().loadImage("die3.png")
    dice4 = SpriteLoader().loadImage("die4.png")
    dice5 = SpriteLoader().loadImage("die5.png")
    dice6 = SpriteLoader().loadImage("die6.png")
    diceWindow = pygame.display.set_mode((512, 448))  # 27
    # Set up the scaling

    dice1 = pygame.transform.scale(dice1, ((dice1.get_width()) * scale, (dice1.get_height()) * scale))
    dice2 = pygame.transform.scale(dice2, ((dice2.get_width()) * scale, (dice2.get_height()) * scale))
    dice3 = pygame.transform.scale(dice3, ((dice3.get_width()) * scale, (dice3.get_height()) * scale))
    dice4 = pygame.transform.scale(dice4, ((dice4.get_width()) * scale, (dice4.get_height()) * scale))
    dice5 = pygame.transform.scale(dice5, ((dice5.get_width()) * scale, (dice5.get_height()) * scale))
    dice6 = pygame.transform.scale(dice6, ((dice6.get_width()) * scale, (dice6.get_height()) * scale))

    rollingDice = False
    isRunning = True
    clock = pygame.time.Clock()
    currentPlayerIndex = 0
    diceState = DiceStates.DICEONE
    while isRunning:
        clock.tick(framerate)  # 39
        key = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                isRunning = False
            if key[pygame.K_SPACE] and rollingDice:
                rollingDice = False
                currentPlayer = listOfPlayers[currentPlayerIndex]
                if diceState == DiceStates.DICEONE:
                    if currentPlayer.getDiceOnePlacement() == 1:
                        diceWindow.blit(dice1, (256, 256))
                    elif currentPlayer.getDiceOnePlacement() == 2:
                        diceWindow.blit(dice2, (256, 256))
                    elif currentPlayer.getDiceOnePlacement() == 3:
                        diceWindow.blit(dice3, (256, 256))
                    elif currentPlayer.getDiceOnePlacement() == 4:
                        diceWindow.blit(dice4, (256, 256))
                    elif currentPlayer.getDiceOnePlacement() == 5:
                        diceWindow.blit(dice5, (256, 256))
                    elif currentPlayer.getDiceOnePlacement() == 6:
                        diceWindow.blit(dice6, (256, 256))
                    diceState = DiceStates.DICETWO  # 60
                elif diceState == DiceStates.DICETWO:
                    if currentPlayer.getDiceTwoPlacement() == 1:
                        diceWindow.blit(dice1, (256, 256))
                    elif currentPlayer.getDiceTwoPlacement() == 2:
                        diceWindow.blit(dice2, (256, 256))
                    elif currentPlayer.getDiceTwoPlacement() == 3:
                        diceWindow.blit(dice3, (256, 256))
                    elif currentPlayer.getDiceTwoPlacement() == 4:
                        diceWindow.blit(dice4, (256, 256))
                    elif currentPlayer.getDiceTwoPlacement() == 5:
                        diceWindow.blit(dice5, (256, 256))
                    elif currentPlayer.getDiceTwoPlacement() == 6:
                        diceWindow.blit(dice6, (256, 256))
                    currentPlayerIndex += 1
                    if currentPlayerIndex == 4:
                        isRunning = False
                    diceState = DiceStates.DICEONE
                time.sleep(0.01)
                pygame.display.update()
            elif key[pygame.K_SPACE] and not rollingDice:
                rollingDice = True
        if rollingDice:
            number = rollOfDice(6)
            if number == 1:
                diceWindow.blit(dice1, (256, 256))
                pass
            elif number == 2:
                diceWindow.blit(dice2, (256, 256))
                pass
            elif number == 3:
                diceWindow.blit(dice3, (256, 256))
                pass
            elif number == 4:
                diceWindow.blit(dice4, (256, 256))
                pass
            elif number == 5:
                diceWindow.blit(dice5, (256, 256))
                pass
            elif number == 6:
                diceWindow.blit(dice6, (256, 256))
                pass
        time.sleep(0.01)
        pygame.display.update()
    listOfPlayers.sort()
    pass  # 105


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


def rollTwoDice(x):
    return random.choice(range(1, x + 1)) + random.choice(range(1, x + 1))


"""
    This determines the placement of each player and it makes sure that the dice that is rolled
    will contain no duplicates what so ever
    
    :param: listOfPlayers - listOfPlayerObjects to be edited
    :param: listOfPlacements - listofPlacements is a list of 0 number of 0 associated with each player
    :param: listOfDice - listOfDice is a list of dice the game in rolling associated with (eg. 6) with 4 players
    
"""


def setPlacementsForBoardPlayers(listOfPlayers, listOfPlacements, listOfDice):  # 110
    while True:
        # First rolled dice
        # Second rolled dice
        # Use map to add them together
        # List of everyone's first dice
        listOfDice1 = list(map(lambda x: rollOfDice(x), listOfDice))
        for i in range(len(listOfDice1)):
            listOfPlayers[i].diceOnePlacement = listOfDice1[i]
        # List of everyone's second dice
        listOfDice2 = list(map(lambda x: rollOfDice(x), listOfDice1))
        for i in range(len(listOfDice2)):
            listOfPlayers[i].diceTwoPlacement = listOfDice2[i]
        # List of everyone's combined dice
        addedDice = list(map(lambda x, y: x + y, listOfDice1, listOfDice2))
        print(addedDice)
        listOfDiceSet = set(addedDice)
        # If there is no duplicates, break
        if len(addedDice) == len(listOfDiceSet):
            break

    listOfDice = addedDice
    for i in range(len(listOfDice1)):
        print(f"Player {listOfPlayers[i].getPlayerID()} dice are....")  # 125
        print(listOfPlayers[i].getDiceOnePlacement())
        print(listOfPlayers[i].getDiceTwoPlacement())
    # We now have the placements of each player on who will now go in order
    for i in range(len(listOfDice)):
        maxValue = max(listOfDice)
        maxIndex = listOfDice.index(maxValue)
        listOfPlacements[maxIndex] = i + 1
        listOfDice[maxIndex] = 0
        print("List of placements is", listOfPlacements)
    for i in range(len(listOfDice)):
        listOfPlayers[i].setPlacementInGame(listOfPlacements[i])
        print("List of placements is", listOfPlayers[i].getPlacementInGame())  # 136


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

    for i in range(len(listOfPlayers)):
        print(f"The order of the players are {listOfPlayers[i].getPlayerID()}")

    rollingDiceAnnimation(scale, frameRate, listOfPlayers)


"""
    The function is runs the logic of when it's a player turn
    
    :param: player - the player who's turn it is
    :return: - None 
    
"""


# TODO: Refactor this later
def getPlayerTurn(player, board):
    # We are going to assume 2 dice rolls for now
    diceRoll = rollOfDice(6)
    # @Need someone to animate this dice roll stuff
    return diceRoll  # 147
    # @Need to get andrew's graph working so i can even do this check with the tiles
    # Second check, from the method, do what the tile says and set params from the player class
    # Repeat until all players have gone and done a turn so we can do the mini game


"""
    The function is what starts the BoardGame and is the runner for the main game and the mini-games

    :param: mainWindow - window of the game
    :param: scale - the scale of the game
    :param: frameRate - frame rate of the game
    :param: board - the board that will be used for the game
    :return: - None 
    
"""


def startGame(mainWindow, scale, framerate, board):
    currentState = States.FIRSTITERATION
    currentPlayer = 0
    playerMovement = 0
    numOfSpots = 0
    playerSelectFork = 0
    clock = pygame.time.Clock()
    renderer = BoardRenderer(board)
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
    startTile = board.getStartTile()
    for i in range(len(listOfPlayers)):
        startTile.players.append(listOfPlayers[i])

    isRunning = True
    # storeScreen(mainWindow, scale, framerate, listOfPlayers[currentPlayer])
    while isRunning:  # 170
        clock.tick(framerate)
        key = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                isRunning = False
            if key[pygame.K_SPACE]:
                if currentState == States.FIRSTITERATION:
                    # This is to activate the screen on who goes first
                    currentState = States.PLAYERMOVE
                    goesFirstScreen(mainWindow, scale, framerate, listOfPlayers, board)
                    # storeScreen(mainWindow, scale, framerate, listOfPlayers[currentPlayer])
                    time.sleep(2)
                    continue
                # Game starts here
                # for each player in listOfPlayers, make them do a move by rolling dice and going to a tile
                if currentState == States.PLAYERMOVE:
                    # If the player lost their turn, skip
                    if listOfPlayers[currentPlayer].getLostTurn():
                        # Set it to false
                        listOfPlayers[currentPlayer].setLostTurn()
                        currentPlayer += 1
                    playerMovement = getPlayerTurn(listOfPlayers[currentPlayer], board)
                    print(f"Player {listOfPlayers[currentPlayer].getPlayerID()} rolled a {playerMovement}")
                    currentState = States.ANNIMATING
                if currentState == States.ANNIMATING:
                    while True:  # 190
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
                            board.movePlayer(nextTiles[0], listOfPlayers[currentPlayer])  # 200

                        numOfSpots += 1
                        if numOfSpots == playerMovement:
                            # If we reach here, that means that we are done animating
                            numOfSpots = 0
                            # We set the player's position to where they are now within the tile after all the
                            # potential paths they went
                            aPlayer = listOfPlayers[currentPlayer]
                            listOfPlayers[currentPlayer].setCurrentPosition(board.getCurrentTile(aPlayer))
                            getTypeOfTile(board.getCurrentTile(aPlayer), listOfPlayers[currentPlayer], mainWindow,
                                          framerate, scale)
                            # Must be the length of players -1
                            if currentPlayer == 3:
                                currentState = States.STARTMINIGAME
                                break
                            else:
                                currentPlayer += 1
                                currentState = States.PLAYERMOVE
                                break  # 213
                        renderer.render()
                        time.sleep(0.25)  # Don't take out the sleep!
                # Once all the players are done here, we start a random mini-game
                if currentState == States.STARTMINIGAME:
                    currentPlayer = 0
                    result = True
                    while(result):  #Keep trying to launch minigames until it works.
                        result = runMinigame(mainWindow, scale, framerate, listOfPlayers)
                        if(result): #Something went wrong
                            print("ERROR! minigameManager.py Failed to launch minigame! Attempting to respin...")
                    currentState = States.PLAYERMOVE
            renderer.render()  # 225

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
