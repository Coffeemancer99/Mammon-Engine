import pygame.sprite

"""
    File authored by Joel Tanig
    55 lines
    The storage for each board player
"""


class BoardPlayer(pygame.sprite.Sprite):
    def __init__(self, playerID):
        pygame.sprite.Sprite.__init__(self)
        # Need to add pieces for the players
        self.prevPosition = 0
        self.currentPosition = 0
        self.placementInGame = 0
        self.money = 10
        self.lostTurn = False
        self.playerID = playerID
        self.inventory = []
        self.diceOnePlacement = 0
        self.diceTwoPlacement = 0
        self.blit = None
        self.startCountDown = 4
        self.speedBoost = False
        self.oneDiceRollBad = False
        self.oneDiceRollGood = False
        self.secondDiceRoll = False
        self.itemIndex = 0
        self.moveOneSpotLess = False
        self.invertedControls = False

    # Do some magical operator overload magic
    def __lt__(self, other):
        return self.getPlacementInGame() < other.getPlacementInGame()

    def setInventory(self, item):
        self.inventory.append(item)

    def setStartCountDown(self, startCountDown): # Make this -
        self.startCountDown += startCountDown

    def setBlit1(self, blit):
        self.blit = blit

    def setItemIndex(self, index):
        self.itemIndex = index

    def setBlit2(self, blit):
        self.blit = blit

    def setDiceOnePlacement(self, dice):
        self.diceOnePlacement = dice

    def setDiceTwoPlacement(self, dice):
        self.diceTwoPlacement = dice

    def removeInventoryItem(self, index):
        return self.inventory.pop(index)

    def setLostTurn(self):
        self.lostTurn = not self.lostTurn

    def setMoney(self, money):
        self.money += money

    def setPlacementInGame(self, placementInGame):
        self.placementInGame = placementInGame

    def setCurrentPosition(self, currentPosition):
        self.currentPosition = currentPosition

    def setPrevPosition(self, prevPosition):
        self.prevPosition = prevPosition

    def setInvertedControls(self, flag):
        self.invertedControls = flag

    def getBlit1(self):
        return self.blit

    def getBlit2(self):
        return self.blit

    def getInventory(self):
        return self.inventory

    def getMoney(self):
        return self.money

    def getPlacementInGame(self):
        return self.placementInGame

    def getCurrentPosition(self):
        return self.currentPosition

    def getPrevPosition(self):
        return self.prevPosition

    def getPlayerID(self):
        return self.playerID

    def getLostTurn(self):
        return self.lostTurn

    def getInventoryLength(self):
        return len(self.inventory)

    def getInventoryItem(self, index):
        return self.inventory[index]

    def getDiceOnePlacement(self):
        return self.diceOnePlacement

    def getDiceTwoPlacement(self):
        return self.diceTwoPlacement

    def getStartCountDown(self):
        return self.startCountDown

    def getItemIndex(self):
        return self.itemIndex

    def getOneDicerollBad(self):
        return self.oneDiceRollBad

    def getOneDiceRollGood(self):
        return self.oneDiceRollGood

    def getMoveOneSpotLess(self):
        return self.moveOneSpotLess

    def getInvertedControls(self):
        return self.invertedControls

    def getSecondDiceroll(self):
        return self.secondDiceRoll

    def resetStartCountDown(self):
        self.startCountDown = 4

    def toggleSpeedBoost(self):
        self.speedBoost = not self.speedBoost
        return self.speedBoost

    def toggleSetOneDicerollBad(self):
        self.oneDiceRollBad = not self.oneDiceRollBad
        return self.oneDiceRollBad

    def toggleSetOneDicerollGood(self):
        self.oneDiceRollGood = not self.oneDiceRollGood
        return self.oneDiceRollGood

    def toggleSetSecondDiceroll(self):
        self.secondDiceRoll = not self.secondDiceRoll
        return self.secondDiceRoll

    def toggleMoveOneSpotLess(self):
        self.moveOneSpotLess = not self.moveOneSpotLess
        return not self.moveOneSpotLess

    def clearBadInventory(self):
        # for i in range(len(self.inventory)):
        #     if "B-" in self.inventory[i]:
        #         self.inventory.pop(i)
        for i in range(len(self.inventory)):
            if self.getInventoryItem(i).isBad():
                self.inventory.pop(i)