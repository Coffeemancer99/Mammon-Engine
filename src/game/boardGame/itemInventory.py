# This stores a pool of items and return one item from a list that will be put into item array of the boardPlayer
import random
from enum import Enum, auto
import numpy

"""
    File authored by Joel Tanig
    98 lines

"""


class ItemType(Enum):
    BADITEM = auto()
    GOODITEM = auto()
    BARTERITEM = auto()


def initGoodItems():
    goodItems = [Item("G-destroyAllBadItems", False, 0.05, 40), Item("G-thirdDice", False, 0.13, 15),
                 Item("G-speedBoostMG", False, 0.18, 10), (Item("G-gainMoneyRandom", False, 0.25, 30)),
                 Item("G-teleportClose", False, 0.05, 25), Item("G-sabotageDice", False, 0.10, 15),
                 Item("G-stealItem", False, 0.16, 40), Item("G-opponentLoseTurn", False, 0.08, 50)]
    return goodItems

    # Make a init good function and a init bad function.
    # Make a new object instead of the str thing i was doing on listOfInventoryItems
    # Don't store the functionality in the object class


def initBadItems():
    badItems = [Item("B-moveOneSpotLess", True, 0.19, 15), Item("B-invertedControlMG", True, 0.19, 40),
                Item("B-changeSpots", True, 0.16, 40), Item("B-loseMoneyRandom", True, 0.16, 30),
                Item("B-loseTurn", True, 0.16, 40), Item("B-oneDice", True, 0.14, 20)]
    return badItems  # 12


def initBarterItems():
    barterItems = [BarterItem("W-BarterItemOne", False, None, 15), BarterItem("W-BarterItemTwo", False, None, 15),
                   BarterItem("W-BarterItemThree", False, None, 15), BarterItem("W-BarterItemFour", False, None, 15)]
    return barterItems  # 12


class Item:
    def __init__(self, name, isbad, rarity, price):
        self.name = name
        self.isbad = isbad
        self.rarity = rarity
        self.price = price

    def getName(self):
        return self.name

    def isBad(self):
        return self.isbad

    def getPrice(self):
        return self.price






class ItemHandler:
    def __init__(self, isMammonInPlay):
        # B = bad item and G = good item
        self.isMammonInPlay = isMammonInPlay
        self.listOfGoodItems = initGoodItems()
        self.listOfBadItems = initBadItems()

    def getItemRegTileBlock(self):
        # This can be a good item 66 percent of the time and a bad item 44 percent of the time
        picked = random.choice(range(0, 100))
        if picked < 33:
            print("bad")
            weights = list((map(lambda x: x.rarity, self.listOfBadItems)))
            print(f"And the weights are...... {weights}")
            badItem = random.choices(self.listOfBadItems, weights)[0]
            return badItem
        else:
            print("good")
            weights = list((map(lambda x: x.rarity, self.listOfGoodItems)))
            print(f"And the weights are...... {weights}")
            goodItem = random.choices(self.listOfGoodItems, weights)[0]
            return goodItem

    def getBadItem(self):
        weights = list((map(lambda x: x.rarity, self.listOfBadItems)))
        return random.choices(self.listOfBadItems, weights)[0]

    def getGoodItem(self):
        weights = list((map(lambda x: x.rarity, self.listOfGoodItems)))
        return random.choices(self.listOfGoodItems, weights)[0]  # 41


# This class will handle all the functionality, put this is a separate file
class ItemFunctionalityBad:
    def __init__(self, name=""):
        self.name = name

    # Need to refactor later as I am breaking open closed :(
    def getFunctionality(self, name, player):
        if name == "B-moveOneSpotLess": # You have to move one spot less
            pass
        elif name == "B-invertedControlMG": # Your controls will be inverted
            pass
        elif name == "B-changeSpots": # A player you pick changes a spot with you
            pass
        elif name == "B-loseMoneyRandom":
            money = random.choice(range(0, 51))
            if player.getMoney() < money:
                player.money = 0
            else:
                player.setMoney(-money)
        elif name == "B-loseTurn":
            player.setLostTurn()  # Need to reset this lost turn later
        elif name == "B-oneDice": # You only get oneDice roll
            diceRoll = random.choice(range(1, 6 + 1))
            return diceRoll
            pass
        elif name == "B-moveToPrevSpot":
            pass


class ItemFunctionalityGood:
    def __init__(self, name=""):
        self.name = name

    def getFunctionality(self, name, player, index=None, player2=None):
        if name == "G-thirdDice":
            diceRoll = random.choice(range(1, 6 + 1)) + random.choice(range(1, 6 + 1)) + random.choice(range(1, 6 + 1))
            return diceRoll
        elif name == "G-destroyAllBadItems":
            player.clearBadInventory()
        elif name == "G-speedBoostMG":
            pass
        elif name == "G-gainMoneyRandom":
            money = random.choice(range(0, 101))
            player.setMoney(money) # Now need to display the money
        elif name == "G-teleportClose":
            player.setLostTurn()  # Need to reset this lost turn later
        elif name == "G-sabotageDice": # Player 2 here represents in the person we are hurting, player 1 can pick what dice to throw out
            # Need to make a screen that makes player 1 pick what dice player 2 can destroy
            pass
        elif name == "G-stealItem": # Player 1 takes player 2's item using index
            # Need to make a screen that steals an item from player 3
            if player.getInventoryLength >= 4:
                print("Cant steal item as you have the max inventory size")
            item = player2.getInventoryItem(index)
            player.setInventory(item)
        elif name == "G-opponentLoseTurn":
            player.setLostTurn()


class BarterItem(Item):
    def __init__(self, name, isBad, rarity, price):
        super().__init__(name, isBad, rarity, price)
