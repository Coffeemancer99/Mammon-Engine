# This stores a pool of items and return one item from a list that will be put into item array of the boardPlayer
import random


def initGoodItems(itemName):
    goodItems = []
    goodItems.append("G-pickPlayerToLoseMG")
    # Make a init good function and a init bad function.
    # Make a new object instead of the str thing i was doing on listOfInventoryItems
    # Don't store the functionality in the object class
    # Make the Pool of items class call the init functions and set it equal to good and bad lists
    # Delete list of inventory items

def initBadItems(itemName):
    pass


class Item:
    def __init__(self, name, isbad, rarity):
        self.name = name
        self.isbad = isbad
        self.rarity = rarity



class PoolOfItems:
    def __init__(self, isMammonInPlay, forceBadItem):
        # B = bad item and G = good item
        listOfInventoryItems = ["B-invertedControlsMG", "B-moveOneSpotLess", "B-changeSpots",
                                "B-loseMoneyRandom", "G-pickPlayerToLoseMG",
                                "B-loseTurn", "B-oneDice", "B-moveToPrevSpot" "G-thirdDice", "G-speedBoostMG",
                                "G-gainMoneyRandom", "G-teleportClose", "G-sabotageDice", "G-stealItem",
                                "G-opponentLoseTurn"]

        self.isMammonInPlay = isMammonInPlay
        self.forceBadItem = forceBadItem

        if self.isMammonInPlay:
            listOfInventoryItems.append("MAMMON")

        self.listOfGoodItems = []
        for i in range(len(listOfInventoryItems)):
            if listOfInventoryItems[i][0] == "G":
                self.listOfGoodItems.append(listOfInventoryItems[i])

        self.listOfBadItems = []
        for i in range(len(listOfInventoryItems)):
            if listOfInventoryItems[i][0] == "B":
                self.listOfBadItems.append(listOfInventoryItems[i])

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
