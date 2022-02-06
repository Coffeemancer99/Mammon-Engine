# This stores a pool of items and return one item from a list that will be put into item array of the boardPlayer
import random


def initGoodItems():
    goodItems = [Item("G-pickPlayerToLoseMG", False, None), Item("G-thirdDice", False, None),
                 Item("G-speedBoostMG", False, None), (Item("G-gainMoneyRandom", False, None)),
                 Item("G-teleportClose", False, None), Item("G-sabotageDice", False, None),
                 Item("G-stealItem", False, None), Item("G-opponentLoseTurn", False, None)]
    return goodItems

    # Make a init good function and a init bad function.
    # Make a new object instead of the str thing i was doing on listOfInventoryItems
    # Don't store the functionality in the object class


def initBadItems():
    badItems = [Item("B-moveOneSpotLess", True, None), Item("B-invertedControlMG", True, None),
                Item("B-changeSpots", True, None), Item("B-loseMoneyRandom", True, None),
                Item("B-loseTurn", False, None), Item("B-oneDice", False, None), Item("B-moveToPrevSpot", False, None)]
    return badItems


class Item:
    def __init__(self, name, isbad, rarity):
        self.name = name
        self.isbad = isbad
        self.rarity = rarity

    def getName(self):
        return self.name

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
class ItemFunctionality:
    pass
