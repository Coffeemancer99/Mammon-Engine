# This stores a pool of items and return one item from a list that will be put into item array of the boardPlayer
class PoolOfItems:
    def __init__(self, isMammonInPlay, forceBadItem):
        listOfInventoryItems = ["B-invertedControlsMG", "B-moveOneSpotLess", "B-ChangeSpots",
                                "B-loseMoney", "G-pickPlayerToLoseMG",
                                "B-loseTurn", "B-oneDice", "B-moveToPrevSpot" "G-thirdDice", "G-speedBoostMG"]
        self.isMammonInPlay = isMammonInPlay
        self.forceBadItem = forceBadItem
        if self.isMammonInPlay == True:
            listOfInventoryItems.append("MAMMON")
        # Need to do logic for 33, 66 percent logic and insert it into the player class of its list
