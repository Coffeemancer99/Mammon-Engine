import random
from src.game.boardGame.itemInventory import initGoodItems, initBadItems
# @NEED a Store Screen and this Store must be destroyed and remade every time the tile is called

"""
    File authored by Joel Tanig
    35 lines
"""


class Store:
    def __init__(self):
        self.listOfGoodItems = initGoodItems()
        self.listOfBadItems = initBadItems()
        # The store will have 4 items to buy, 3 items that are good and 1 that is bad
        storeInventory = []
        storeInventory.append(random.choice(self.listOfGoodItems))
        storeInventory.append(random.choice(self.listOfGoodItems))
        storeInventory.append(random.choice(self.listOfGoodItems))
        storeInventory.append(random.choice(self.listOfBadItems))
        self.storeInventory = storeInventory

        # Need to make a screen that picks items and for each "iteration" increase or deprecate the index

    def buyItem(self, player, index):
        priceOfItem = self.storeInventory[index].getPrice()
        if player.getMoney() >= priceOfItem:
            player.setMoney(-priceOfItem)
            player.setInventory(self.storeInventory[index])
            print(f"Player {player.getPlayerID()} got {self.storeInventory[index].getName()}")
            return True
        elif player.getInventoryLength() >= 4:
            print(f"Player {player.getPlayerID()} is full in inventory space")
            return False
        else:
            print(f"Player {player.getPlayerID()} has {player.getMoney()} coins and the item amount is {priceOfItem} coins")
            return False

    def sellItem(self, player, index):
        # The price of the selling item that player wants to sell will be 20 percent off the original price
        priceOfSellingItem = player.getInventoryItem(index).getPrice() - int(
            20 * player.getInventoryItem(index).getPrice() / 100)
        print(priceOfSellingItem)
        print(player.setMoney(priceOfSellingItem))
        print(
            f"Player {player.getPlayerID()} has sold item {player.getInventoryItem(index).name} and now has {player.getMoney()}")
        player.removeInventoryItem(index)
