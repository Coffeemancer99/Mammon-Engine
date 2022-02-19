# This stores a pool of items and return one item from a list that will be put into item array of the boardPlayer
import random


def initGoodItems():
    goodItems = [Item("G-pickPlayerToLoseMG", False, None, 40), Item("G-thirdDice", False, None, 15),
                 Item("G-speedBoostMG", False, None, 10), (Item("G-gainMoneyRandom", False, None, 30)),
                 Item("G-teleportClose", False, None, 25), Item("G-sabotageDice", False, None, 15),
                 Item("G-stealItem", False, None, 40), Item("G-opponentLoseTurn", False, None, 50)]
    return goodItems

    # Make a init good function and a init bad function.
    # Make a new object instead of the str thing i was doing on listOfInventoryItems
    # Don't store the functionality in the object class


def initBadItems():
    badItems = [Item("B-moveOneSpotLess", True, None, 15), Item("B-invertedControlMG", True, None, 40),
                Item("B-changeSpots", True, None,40), Item("B-loseMoneyRandom", True, None,30),
                Item("B-loseTurn", True, None, 40), Item("B-oneDice", True, None,20), Item("B-moveToPrevSpot", True, None, 15)]
    return badItems


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
        return random.choice(self.listOfGoodItems)


# This class will handle all the functionality, put this is a separate file
class ItemFunctionalityBad:
    def __init__(self, name=""):
        self.name = name

    def getFunctionality(self, name, player):
        if name == "B-moveOneSpotLess":
            pass
        elif name == "B-invertedControlMG":
            pass
        elif name == "B-changeSpots":
            pass
        elif name == "B-loseMoneyRandom":
            pass
        elif name == "B-loseTurn":
            player.setLostTurn()  # Need to reset this lost turn later
        elif name == "B-oneDice":
            pass
        elif name == "B-moveToPrevSpot":
            pass


class ItemFunctionalityGood:
    pass
