import pygame
import time
import random

from src.game.boardGame import itemInventory
from src.game.boardGame.Items import InvertedControlsItem
from src.game.boardGame.Store import Store
from src.game.boardGame.boardPlayers import BoardPlayer
from enum import Enum, auto

from src.game.boardGame.inventoryMenuStuff.inventoryMenu import InventoryMenu
from src.game.boardGame.itemInventory import ItemHandler, ItemFunctionalityBad, ItemFunctionalityGood
from src.game.boardGame.minigameManager import runMinigame
from src.game.boardGame2.boardRenderer import BoardRenderer
from src.game.boardGame2.spriteLoader import SpriteLoader
from src.minigame.teamSwimmer import teamSwimmer
from src.game.boardGame.inventoryMenuStuff.inventoryMenuCreatorFunctions import *

"""
    575 total
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
        print(f"The type of tile is {currentTile.typeOfTile}")
        player.setMoney(5)
        print(f"Player {player.getPlayerID()} now has {player.getMoney()} money")
    elif currentTile.typeOfTile == "Dual":
        print(f"The type of tile is {currentTile.typeOfTile}")
    elif currentTile.typeOfTile == "Store":
        print(f"The type of tile is {currentTile.typeOfTile}")
        return storeScreen(mainWindow, scale, framerate, player)
    elif currentTile.typeOfTile == "Bad":
        print(f"The type of tile is {currentTile.typeOfTile}")
        amountLost = rollOneDice(6)
        print(f"The amount loss in this bad tile is {amountLost}")
        print(f"Player {player.getPlayerID()} now has {player.getMoney()} money")
        player.setMoney(amountLost)
    elif currentTile.typeOfTile == "Gate":
        print(f"The type of tile is {currentTile.typeOfTile}")


# def inventoryScreen(mainWindow, scale, framerate, currentPlayer):
#     clock = pygame.time.Clock()
#     transaction = False
#     getItemBadFunctionality = ItemFunctionalityBad()
#     getItemGoodFunctionality = ItemFunctionalityGood()
#     # We will let die4.png represent empty inventory spots
#     listOfItemImages = ["die4.png","die4.png","die4.png","die4.png"]
#     # TODO: Need to figure out how to get each inventory item and blit different images with them
#     for i in range(currentPlayer.getInventoryLength()):
#         ## TODO: WILL JUST BLIT DICE1.PNG FOR NOW
#         listOfItemImages[i] = "die1.png"
#
#     inventoryItemOne = SpriteLoader().loadImage(listOfItemImages[0])
#     inventoryItemTwo = SpriteLoader().loadImage(listOfItemImages[1])
#     inventoryItemThree = SpriteLoader().loadImage(listOfItemImages[2])
#     inventoryItemFour = SpriteLoader().loadImage(listOfItemImages[3])
#
#     inventoryItemOne = pygame.transform.scale(inventoryItemOne,
#                                               ((inventoryItemOne.get_width()) * scale, (inventoryItemOne.get_height())*scale))
#     inventoryItemTwo = pygame.transform.scale(inventoryItemTwo,
#                                               ((inventoryItemTwo.get_width()) * scale, (inventoryItemTwo.get_height())*scale))
#     inventoryItemThree = pygame.transform.scale(inventoryItemThree,
#                                               ((inventoryItemThree.get_width()) * scale,
#                                                (inventoryItemThree.get_height()) * scale))
#     inventoryItemFour = pygame.transform.scale(inventoryItemFour,
#                                               ((inventoryItemFour.get_width()) * scale,
#                                                (inventoryItemFour.get_height()) * scale))
#
#     mainWindow.fill((55, 55, 55))
#     # Put buttons here
#     mainWindow.blit(inventoryItemOne, (32 * scale, 32 * scale))
#     mainWindow.blit(inventoryItemTwo, (32 * scale, 112 * scale))
#     mainWindow.blit(inventoryItemThree, (32 * scale, 208 * scale))
#     mainWindow.blit(inventoryItemFour, (412 * scale, 356 * scale))
#
#
#     isRunning = True
#     while isRunning:
#         pygame.display.update()
#         clock.tick(framerate)  # 39
#         key = pygame.key.get_pressed()
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 isRunning = False
#             if event.type == pygame.MOUSEBUTTONUP:
#                 click = pygame.mouse.get_pos()
#                 print(click)
#                 # Buying logic
#                 if (click[0] > 32 * scale) and (click[0] <= 488 * scale):  # x
#                     if (click[1] > 24 * scale) and (click[1] <= 60 * scale):  # y
#                         print(f"Using {currentPlayer.getInventoryItem(0).getName()} item")
#                         if currentPlayer.getInventoryItem(0).isBad():
#                             getItemBadFunctionality.getFunctionality(currentPlayer.getInventoryItem(0).getName(),currentPlayer)
#                         else:
#                             getItemGoodFunctionality.getFunctionality(currentPlayer.getInventoryItem(0).getName(),currentPlayer)
#                     elif (click[1] > 112 * scale) and (click[1] <= 176 * scale):
#                         print(f"Using {currentPlayer.getInventoryItem(1).isBad()} item")
#                         if currentPlayer.getInventoryItem(1).isBad():
#                             getItemBadFunctionality.getFunctionality(currentPlayer.getInventoryItem(1).getName(),currentPlayer)
#                         else:
#                             getItemGoodFunctionality.getFunctionality(currentPlayer.getInventoryItem(1).getName(),currentPlayer)
#                     elif (click[1] > 208 * scale) and (click[1] <= 252 * scale):
#                         print(f"Using {currentPlayer.getInventoryItem(2).getName()} item")
#                         if currentPlayer.getInventoryItem(2).isBad():
#                             getItemBadFunctionality.getFunctionality(currentPlayer.getInventoryItem(2).getName(),currentPlayer)
#                         else:
#                             getItemGoodFunctionality.getFunctionality(currentPlayer.getInventoryItem(2).getName(),currentPlayer)
#                     elif (click[1] > 304 * scale) and (click[1] <= 328 * scale):
#                         print(f"Using {currentPlayer.getInventoryItem(3).getName()} item")
#                         if currentPlayer.getInventoryItem(3).isBad():
#                             getItemBadFunctionality.getFunctionality(currentPlayer.getInventoryItem(3).getName(),currentPlayer)
#                         else:
#                             getItemGoodFunctionality.getFunctionality(currentPlayer.getInventoryItem(3).getName(),currentPlayer)
#                     if transaction:
#                         currentPlayer.getInventory()
#                         isRunning = False


# TODO: Andrew, recreate this
"""This function is a inventory screen that gets passed in

    :param mainWindow: window that the user sees
    :param scale: how big or small the window is based on scale
    :param framerate: how much framerate the window will have
    :param currentPlayer: the currentPlayer's inventory
    :param listOfPlayers: the listOfPlayers in the whole game
    
    THIS IS A TEST FUNCTION THAT WILL BE RECREATED BY ANDREW
"""
def inventoryScreen(mainWindow, scale, framerate, currentPlayer, listOfPlayers):
    playerThatIsTargetted = 1
    clock = pygame.time.Clock()

    # Make the images
    itemImages = makeAllImages(mainWindow, scale, currentPlayer)

    # Make the buttons
    invMenuButtons = makeAllButtons(mainWindow, framerate, scale, currentPlayer, itemImages, listOfPlayers)

    # Make the menu
    invScreen = InventoryMenu("Inventory", buttons=invMenuButtons, images=itemImages,
                              currentPlayer=currentPlayer, listOfPlayers=listOfPlayers)
    # Launch the menu
    invScreen.launch(mainWindow, framerate)

    transaction = False
    inventoryItemOne = SpriteLoader().loadImage(currentPlayer.getInventoryItem(0).getButtonImage())
    inventoryItemTwo = SpriteLoader().loadImage(currentPlayer.getInventoryItem(1).getButtonImage())
    inventoryItemThree = SpriteLoader().loadImage(currentPlayer.getInventoryItem(2).getButtonImage())
    inventoryItemFour = SpriteLoader().loadImage(currentPlayer.getInventoryItem(3).getButtonImage())

    inventoryItemOne = pygame.transform.scale(inventoryItemOne,
                                              ((inventoryItemOne.get_width()) * scale,
                                               (inventoryItemOne.get_height()) * scale))
    inventoryItemTwo = pygame.transform.scale(inventoryItemTwo,
                                              ((inventoryItemTwo.get_width()) * scale,
                                               (inventoryItemTwo.get_height()) * scale))
    inventoryItemThree = pygame.transform.scale(inventoryItemThree,
                                                ((inventoryItemThree.get_width()) * scale,
                                                 (inventoryItemThree.get_height()) * scale))
    inventoryItemFour = pygame.transform.scale(inventoryItemFour,
                                               ((inventoryItemFour.get_width()) * scale,
                                                (inventoryItemFour.get_height()) * scale))

    mainWindow.fill((55, 55, 55))
    # Put buttons here
    mainWindow.blit(inventoryItemOne, (32 * scale, 32 * scale))
    mainWindow.blit(inventoryItemTwo, (32 * scale, 112 * scale))
    mainWindow.blit(inventoryItemThree, (32 * scale, 208 * scale))
    mainWindow.blit(inventoryItemFour, (412 * scale, 356 * scale))

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
                        print(f"Using {currentPlayer.getInventoryItem(0).getName()} item")
                        if not currentPlayer.currentPlayer.getInventoryItem(0).affectSecondPlayer():
                            currentPlayer.getInventoryItem(0).getFunctionality(currentPlayer, None)
                        else:
                            # TODO: Andrew, make another screen saying, which player you would like to select
                            currentPlayer.getInventoryItem(0).getFunctionality(currentPlayer,
                                                                               listOfPlayers[playerThatIsTargetted])
                    elif (click[1] > 112 * scale) and (click[1] <= 176 * scale):
                        print(f"Using {currentPlayer.getInventoryItem(1).isBad()} item")
                        if not currentPlayer.currentPlayer.getInventoryItem(1).affectSecondPlayer():
                            currentPlayer.getInventoryItem(1).getFunctionality(currentPlayer, None)
                        else:
                            # TODO: Andrew, make another screen saying, which player you would like to select
                            currentPlayer.getInventoryItem(0).getFunctionality(currentPlayer,
                                                                               listOfPlayers[playerThatIsTargetted])
                    elif (click[1] > 208 * scale) and (click[1] <= 252 * scale):
                        print(f"Using {currentPlayer.getInventoryItem(2).getName()} item")
                        if not currentPlayer.currentPlayer.getInventoryItem(2).affectSecondPlayer():
                            currentPlayer.getInventoryItem(2).getFunctionality(currentPlayer, None)
                        else:
                            # TODO: Andrew, make another screen saying, which player you would like to select
                            currentPlayer.getInventoryItem(2).getFunctionality(currentPlayer,
                                                                               listOfPlayers[playerThatIsTargetted])
                    elif (click[1] > 304 * scale) and (click[1] <= 328 * scale):
                        print(f"Using {currentPlayer.getInventoryItem(3).getName()} item")
                        if not currentPlayer.currentPlayer.getInventoryItem(3).affectSecondPlayer():
                            currentPlayer.getInventoryItem(3).getFunctionality(currentPlayer, None)
                        else:
                            # TODO: Andrew, make another screen saying, which player you would like to select
                            currentPlayer.getInventoryItem(3).getFunctionality(currentPlayer,
                                                                               listOfPlayers[playerThatIsTargetted])
                    if transaction:
                        currentPlayer.getInventory()
                        isRunning = False


"""This function is a store and it gets passed in

    :param mainWindow: window that the user sees
    :param scale: how big or small the window is based on scale
    :param framerate: how much framerate the window will have
    :param currentPlayer: the currentPlayer's inventory
    THIS IS A TEST FUNCTION THAT WILL BE RECREATED BY ANDREW
    
"""
# TODO: Andrew, recreate this
def storeScreen(mainWindow, scale, framerate, currentPlayer):
    clock = pygame.time.Clock()
    transaction = False
    store = Store()

    # TODO: Need to blit different images that relate to the storeInventory list
    gooditemOne = SpriteLoader().loadImage(store.storeInventory[0].getButtonImage())
    gooditemTwo = SpriteLoader().loadImage(store.storeInventory[1].getButtonImage())
    gooditemThree = SpriteLoader().loadImage(store.storeInventory[2].getButtonImage())
    gooditemFour = SpriteLoader().loadImage(store.storeInventory[3].getButtonImage())

    gooditemOne = pygame.transform.scale(gooditemOne,
                                         ((gooditemOne.get_width()) * scale, (gooditemOne.get_height()) * scale))
    gooditemTwo = pygame.transform.scale(gooditemTwo,
                                         ((gooditemTwo.get_width()) * scale, (gooditemTwo.get_height()) * scale))
    gooditemThree = pygame.transform.scale(gooditemThree,
                                           ((gooditemThree.get_width()) * scale, (gooditemThree.get_height()) * scale))
    gooditemFour = pygame.transform.scale(gooditemFour,
                                          ((gooditemFour.get_width()) * scale, (gooditemFour.get_height()) * scale))

    mainWindow.fill((55, 55, 55))
    # Put buttons here
    mainWindow.blit(gooditemOne, (32 * scale, 32 * scale))
    mainWindow.blit(gooditemTwo, (32 * scale, 112 * scale))
    mainWindow.blit(gooditemThree, (32 * scale, 208 * scale))
    mainWindow.blit(gooditemFour, (412 * scale, 356 * scale))

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
                        print("Bought Good item 4")
                        transaction = store.buyItem(currentPlayer, 3)
                    if transaction:
                        currentPlayer.getInventory()
                        isRunning = False

                if (click[0] > 4 * scale) and (click[0] <= 100 * scale):  # x
                    if (click[1] > 412 * scale) and (click[1] <= 444 * scale):  # y
                        print("Sold item")
                        # TODO: Andrew, figure out how to sell item using the index
                        store.sellItem(currentPlayer, 0)


"""
    This function rolls dice on the screen, it is also important to note that the dice rolls
    are already determined in the setPlacementsForBoardPlayers function as I wanted to make sure we had no
    duplicates
"""


# TODO: Andrew, Use this
def rollingDiceAnnimation(mainWindow, scale, framerate, listOfPlayers):
    # Note that scale is one for now
    # Set up all the buttons
    dice1 = SpriteLoader().loadImage("die1.png")
    dice2 = SpriteLoader().loadImage("die2.png")
    dice3 = SpriteLoader().loadImage("die3.png")
    dice4 = SpriteLoader().loadImage("die4.png")
    dice5 = SpriteLoader().loadImage("die5.png")
    dice6 = SpriteLoader().loadImage("die6.png")
    diceWindow = mainWindow
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
                        currentPlayer.setBlit1(True)
                    elif currentPlayer.getDiceOnePlacement() == 2:
                        diceWindow.blit(dice2, (256, 256))
                        currentPlayer.setBlit1(True)
                    elif currentPlayer.getDiceOnePlacement() == 3:
                        diceWindow.blit(dice3, (256, 256))
                        currentPlayer.setBlit1(True)
                    elif currentPlayer.getDiceOnePlacement() == 4:
                        diceWindow.blit(dice4, (256, 256))
                        currentPlayer.setBlit1(True)
                    elif currentPlayer.getDiceOnePlacement() == 5:
                        diceWindow.blit(dice5, (256, 256))
                        currentPlayer.setBlit1(True)
                    elif currentPlayer.getDiceOnePlacement() == 6:
                        diceWindow.blit(dice6, (256, 256))
                        currentPlayer.setBlit1(True)
                    diceState = DiceStates.DICETWO  # 60
                elif diceState == DiceStates.DICETWO:
                    if currentPlayer.getDiceTwoPlacement() == 1:
                        diceWindow.blit(dice1, (256, 256))
                        currentPlayer.setBlit2(True)
                    elif currentPlayer.getDiceTwoPlacement() == 2:
                        diceWindow.blit(dice2, (256, 256))
                        currentPlayer.setBlit2(True)
                    elif currentPlayer.getDiceTwoPlacement() == 3:
                        diceWindow.blit(dice3, (256, 256))
                        currentPlayer.setBlit2(True)
                    elif currentPlayer.getDiceTwoPlacement() == 4:
                        diceWindow.blit(dice4, (256, 256))
                        currentPlayer.setBlit2(True)
                    elif currentPlayer.getDiceTwoPlacement() == 5:
                        diceWindow.blit(dice5, (256, 256))
                        currentPlayer.setBlit2(True)
                    elif currentPlayer.getDiceTwoPlacement() == 6:
                        diceWindow.blit(dice6, (256, 256))
                        currentPlayer.setBlit2(True)
                    currentPlayerIndex += 1
                    if currentPlayerIndex == 4:
                        isRunning = False
                    diceState = DiceStates.DICEONE
                time.sleep(0.01)
                pygame.display.update()
            elif key[pygame.K_SPACE] and not rollingDice:
                rollingDice = True
        if rollingDice:
            number = rollOneDice(6)
            if number == 1:
                diceWindow.blit(dice1, (256, 256))
            elif number == 2:
                diceWindow.blit(dice2, (256, 256))
            elif number == 3:
                diceWindow.blit(dice3, (256, 256))
            elif number == 4:
                diceWindow.blit(dice4, (256, 256))
            elif number == 5:
                diceWindow.blit(dice5, (256, 256))
            elif number == 6:
                diceWindow.blit(dice6, (256, 256))
        time.sleep(0.01)
        pygame.display.update()
    listOfPlayers.sort()


"""
    Rolls one dice
    
    :param: x - how many sides the dice has
    :return: - int type: dice roll 

"""


def rollOneDice(x):
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
        listOfDice1 = list(map(lambda x: rollOneDice(x), listOfDice))
        for i in range(len(listOfDice1)):
            listOfPlayers[i].diceOnePlacement = listOfDice1[i]
        # List of everyone's second dice
        listOfDice2 = list(map(lambda x: rollOneDice(x), listOfDice1))
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
    # First start the game by rolling dice, this will contain no duplicates
    listOfPlacements = [0, 0, 0, 0]
    listOfDice = [6, 6, 6, 6]
    setPlacementsForBoardPlayers(listOfPlayers, listOfPlacements, listOfDice)
    # Sort players by placements

    for i in range(len(listOfPlayers)):
        print(f"The order of the players are {listOfPlayers[i].getPlayerID()}")

    rollingDiceAnnimation(mainWindow, scale, frameRate, listOfPlayers)


"""
    The function is what starts the BoardGame and is the runner for the main game and the mini-games

    :param mainWindow - window of the game
    :param scale - the scale of the game
    :param frameRate - frame rate of the game
    :param board - the board that will be used for the game
    :return - None 
    
"""


def startGame(mainWindow, scale, framerate, board):
    currentState = States.FIRSTITERATION
    currentPlayer = 0
    playerMovement = 0
    numOfSpots = 0
    playerSelectFork = 0  # TODO: change to 1 or 0 for a different path
    clock = pygame.time.Clock()
    renderer = BoardRenderer(board, mainWindow, scale)
    # init the players
    playerOne = BoardPlayer(1)
    playerTwo = BoardPlayer(2)
    playerThree = BoardPlayer(3)
    playerFour = BoardPlayer(4)

    playerOne.image = SpriteLoader().loadImage("testPlayer.png")
    playerTwo.image = SpriteLoader().loadImage("testPlayer2.png")
    playerThree.image = SpriteLoader().loadImage("testPlayer3.png")
    playerFour.image = SpriteLoader().loadImage("testPlayer4.png")

    listOfPlayers = [playerOne, playerTwo, playerThree, playerFour]
    startTile = board.getStartTile()
    for i in range(len(listOfPlayers)):
        startTile.players.append(listOfPlayers[i])

    isRunning = True
    goingBackToStart = False

    TESTSTORE = True
    # storeScreen(mainWindow, scale, framerate, listOfPlayers[currentPlayer])
    print("Press ENTER to enter the dice rolling phase then SPACE start dice rolling")
    while isRunning:  # 170
        clock.tick(framerate)
        key = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                isRunning = False
            # TODO: Andrew Need to make a button and a screen that shows if the player is going to do something with their inventory
            if key[pygame.K_RETURN]:
                if currentState == States.FIRSTITERATION:
                    # This is to activate the screen on who goes first
                    currentState = States.PLAYERMOVE
                    goesFirstScreen(mainWindow, scale, framerate, listOfPlayers, board)
                    # storeScreen(mainWindow, scale, framerate, listOfPlayers[currentPlayer])
                    time.sleep(2)
                    continue
                # Game starts here
                # For each player in listOfPlayers, make them do a move by rolling dice and going to a tile

            # TODO: Andrew Need to make a inventory screen here
            if key[pygame.K_i]:
                if currentState == States.PLAYERMOVE:
                    inventoryScreen(mainWindow, scale, framerate, listOfPlayers[currentPlayer], currentPlayer)
                    time.sleep(1)
                    continue
            if key[pygame.K_SPACE]:  # End turn and move the character
                print(f"Player {listOfPlayers[currentPlayer].getPlayerID()} turn")
                if currentState == States.PLAYERMOVE:
                    # If the player lost their turn, skip
                    if listOfPlayers[currentPlayer].getLostTurn():
                        # Set it to false
                        listOfPlayers[currentPlayer].setLostTurn()
                        currentPlayer += 1
                    # TODO: DO CHECKS HERE START HEREEEEEEEEEEEEEEe
                    if listOfPlayers[currentPlayer].getOneDicerollBad():
                        playerMovement = 1
                        print(f"Player {listOfPlayers[currentPlayer].getPlayerID()} can only move one spot because of an item")
                        listOfPlayers[currentPlayer].toggleSetOneDicerollBad()
                    # Get the player movement here, first check if they can roll 2 dice or only 1 based on an item
                    elif listOfPlayers[currentPlayer].getSecondDiceroll():
                        print(f"Player {listOfPlayers[currentPlayer]} has 2 dice rolls and will roll 2 dice")
                        playerMovement = rollTwoDice(6)
                        listOfPlayers[currentPlayer].toggleSetSecondDiceroll()
                    else:
                        playerMovement = rollOneDice(6)
                    # Check if they have to move one spot less based on an item
                    if listOfPlayers[currentPlayer].getMoveOneSpotLess():
                        playerMovement -= 1
                        listOfPlayers[currentPlayer].toggleMoveOneSpotLess()
                        print(f"Player {listOfPlayers[currentPlayer].getPlayerID()} activated a bad item of "
                              f"moving one spot less but they"
                              f" were {listOfPlayers[currentPlayer].getStartCountDown()} moves from getting sent "
                              f"to the start ")
                        # Save the last move the player did
                    listOfPlayers[currentPlayer].setPrevPosition(listOfPlayers[currentPlayer].getCurrentPosition())
                    listOfPlayers[currentPlayer].setCurrentPosition(playerMovement)
                    print(f"Player {listOfPlayers[currentPlayer].getPlayerID()} rolled a {playerMovement}")
                    # If the player did not use a bad item in 4 turns. They have to go back to the beginning
                    if listOfPlayers[currentPlayer].getStartCountDown() <= 0:
                        listOfPlayers[currentPlayer].setPrevPosition(0)
                        listOfPlayers[currentPlayer].setCurrentPosition(0)
                        listOfPlayers[currentPlayer].resetStartCountDown()
                        goingBackToStart = True
                        listOfPlayers[currentPlayer].clearBadInventory()
                    # If we see a bad item in our inventory, we have to decrement the setStartCountDown
                    inventory = listOfPlayers[currentPlayer].getInventory()
                    flagForBadItems = True
                    for i in range(len(inventory)):
                        if inventory[i].isBad():
                            listOfPlayers[currentPlayer].setStartCountDown(-1)
                            flagForBadItems = False
                            break
                    if flagForBadItems:
                        listOfPlayers[currentPlayer].resetStartCountDown()
                        print(
                            f"Player {listOfPlayers[currentPlayer].getPlayerID()} have no bad items in their "
                            f"inventory and the counter for bad items was reset!")
                    # if TESTSTORE: # This is for testing the Bad inventory, uncomment to test
                    #     listOfPlayers[currentPlayer].setMoney(1000)
                    #     listOfPlayers[currentPlayer].setInventory(InvertedControlsItem())
                    #     #storeScreen(mainWindow, 1, 60, listOfPlayers[currentPlayer])
                    #     itemHandler = ItemHandler(False)
                    #     item = itemHandler.getItemRegTileBlock()
                    #     print(f"And the fucking item isssssssssssssssss {item.getName()}")
                    #     TESTSTORE = False
                    print(f"Player {listOfPlayers[currentPlayer].getPlayerID()} countdown timer is {listOfPlayers[currentPlayer].getStartCountDown()}")
                    # TODO: Andrew MAKE A SCREEN TOO THAT SAY WHAT IS HAPPENING
                    currentState = States.ANNIMATING
                if currentState == States.ANNIMATING:
                    while True:  # 190
                        nextTiles = board.getPotentialMoves(listOfPlayers[currentPlayer])
                        # If I see a fork in the road, then we need to pick which path to go to next
                        if not goingBackToStart:
                            if len(nextTiles) > 1:
                                # TODO: Andrew Need to make the selection screen for multiple paths
                                if playerSelectFork == 0:
                                    board.movePlayer(nextTiles[0], listOfPlayers[currentPlayer])
                                elif playerSelectFork == 1 and playerSelectFork >= len(nextTiles):
                                    board.movePlayer(nextTiles[1], listOfPlayers[currentPlayer])
                                elif playerSelectFork == 2 and playerSelectFork >= len(nextTiles):
                                    board.movePlayer(nextTiles[2], listOfPlayers[currentPlayer])
                            else:
                                # If we have no fork in the road, then we just go straight
                                board.movePlayer(nextTiles[0], listOfPlayers[currentPlayer])  # 200
                        else:
                            board.movePlayer(board.getStartTile(), listOfPlayers[currentPlayer])
                            renderer.render()
                            time.sleep(1)  # Don't take out the sleep!
                            # Must be the length of players -1
                            if currentPlayer == 3:
                                currentState = States.STARTMINIGAME
                                break
                            else:
                                currentPlayer += 1
                                currentState = States.PLAYERMOVE
                                break  # 213
                        numOfSpots += 1
                        if numOfSpots == playerMovement and not goingBackToStart:
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
                        time.sleep(1)  # Don't take out the sleep!
                # Once all the players are done here, we start a random mini-game
                if currentState == States.STARTMINIGAME:
                    renderer.render()
                    time.sleep(1)  # Don't take out the sleep!
                    currentPlayer = 0
                    result = True
                    while result:  # Keep trying to launch minigames until it works.
                        result = runMinigame(mainWindow, scale, framerate, listOfPlayers)
                        if result:  # Something went wrong
                            miniGameObject = teamSwimmer.startGame(mainWindow, scale, framerate)
                            for i in range(len(listOfPlayers)):
                                print(
                                    f"Player {listOfPlayers[i].getPlayerID()} money WAS {listOfPlayers[i].getMoney()}")
                                listOfPlayers[i].setMoney(miniGameObject.earnings[i])
                                print(
                                    f"Player {listOfPlayers[i].getPlayerID()} earnings was {miniGameObject.earnings[i]}")
                                print(
                                    f"Player {listOfPlayers[i].getPlayerID()} money IS NOW {listOfPlayers[i].getMoney()}")
                            # print("ERROR! minigameManager.py Failed to launch minigame! Attempting to respin...")
                            result = False
                    currentState = States.PLAYERMOVE
            goingBackToStart = False
            renderer.render()  # 225
