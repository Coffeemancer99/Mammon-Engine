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

    # Do some magical operator overload magic
    def __lt__(self, other):
        return self.getPlacementInGame() < other.getPlacementInGame()

    def setInventory(self, inventory):
        self.inventory.append(inventory)

    def setStartCountDown(self, startCountDown): # Make this -
        self.startCountDown += startCountDown

    def setBlit1(self, blit):
        self.blit = blit

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

    def resetStartCountDown(self):
        self.startCountDown = 4

    def clearBadInventory(self):
        for i in range(len(self.inventory)):
            if "B-" in self.inventory[i]:
                self.inventory.pop(i)
