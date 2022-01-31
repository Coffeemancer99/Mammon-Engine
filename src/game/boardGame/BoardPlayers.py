import pygame.sprite


# Need to make a BoardPlayer Array


class BoardPlayer(pygame.sprite.Sprite):
    def __init__(self, playerID):
        pygame.sprite.Sprite.__init__(self)
        # Need to add pieces for the players
        self.playerID = playerID
        self.inventory = []

    def setInventory(self, inventory):
        self.inventory.append(inventory)

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


player1 = BoardPlayer(1)
# player2 = BoardPlayer(2)
# player3 = BoardPlayer(3)
# player4 = BoardPlayer(4)
