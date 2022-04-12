# This stores a pool of items and return one item from a list that will be put into item array of the boardPlayer
import random
from enum import Enum, auto

"""
    File authored by Joel Tanig
    98 lines

"""


class ItemType(Enum):
    BADITEM = auto()
    GOODITEM = auto()
    BARTERITEM = auto()


def initGoodItems():
    goodItems = [Item("G-destroyAllBadItems", False, None, 40), Item("G-thirdDice", False, None, 15),
                 Item("G-speedBoostMG", False, None, 10), (Item("G-gainMoneyRandom", False, None, 30)),
                 Item("G-teleportClose", False, None, 25), Item("G-sabotageDice", False, None, 15),
                 Item("G-stealItem", False, None, 40), Item("G-opponentLoseTurn", False, None, 50)]
    return goodItems

    # Make a init good function and a init bad function.
    # Make a new object instead of the str thing i was doing on listOfInventoryItems
    # Don't store the functionality in the object class


def initBadItems():
    badItems = [Item("B-moveOneSpotLess", True, None, 15), Item("B-invertedControlMG", True, None, 40),
                Item("B-changeSpots", True, None, 40), Item("B-loseMoneyRandom", True, None, 30),
                Item("B-loseTurn", True, None, 40), Item("B-oneDice", True, None, 20)]
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

    def getPrice(self):
        return self.price


class ItemHandler:
    def __init__(self, isMammonInPlay):
        # B = bad item and G = good item
        self.isMammonInPlay = isMammonInPlay
        self.listOfGoodItems = initGoodItems()
        self.listOfBadItems = initBadItems()
        # Need to do logic for 33, 66 percent logic and insert it into the player class of its list

    def getItemRegTileBlock(self):
        picked = random.choice(range(0, 100))
        if picked < 33:
            print("bad")
            badItem = random.choice(self.listOfBadItems)
            return badItem
        else:
            print("good")
            goodItem = random.choice(self.listOfGoodItems)
            return goodItem

    def getBadItem(self):
        return random.choice(self.listOfBadItems)

    def getGoodItem(self):
        return random.choice(self.listOfGoodItems)  # 41


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
