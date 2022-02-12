import pygame.sprite


class BoardPlayer(pygame.sprite.Sprite):
    def __init__(self, playerID):
        pygame.sprite.Sprite.__init__(self)
        # Need to add pieces for the players
        self.prevPosition = None
        self.currentPosition = None
        self.placementInGame = 0
        self.money = 10
        self.lostTurn = False
        self.playerID = playerID
        self.inventory = []

    # Do some magical operator overload magic
    def __lt__(self, other):
        return self.getPlacementInGame() < other.getPlacementInGame()

    def setInventory(self, inventory):
        self.inventory.append(inventory)

    def setLostTurn(self):
        self.lostTurn = not self.lostTurn

    def setMoney(self, money):
        self.money = money

    def setPlacementInGame(self, placementInGame):
        self.placementInGame = placementInGame

    def setCurrentPosition(self, currentPosition):
        self.currentPosition = currentPosition

    def setPrevPosition(self, prevPosition):
        self.prevPosition = prevPosition

    def getInventory(self):
        return self.inventory

    def getMoney(self):
        return self.getMoney

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


