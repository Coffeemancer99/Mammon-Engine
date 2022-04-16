import random


# Note the items get destroyed after it is called in the inventory screen
class ItemInterface:
    def getName(self) -> str:
        """Returns the name of the item"""
        pass

    def isBad(self) -> bool:
        """Returns a boolean if it is a bad item"""
        pass

    def getPrice(self) -> int:
        """Returns a price of a bad item"""
        pass

    def getRarity(self) -> float:
        """Returns the rarity of an item"""
        pass

    def getFunctionality(self, player, player2) -> bool:
        """Gets the functionality of an item
        :param player: The player we are using the item
        :param player2: The player we want affected from the item
        :return: If the Item was able to be used or not
        """
        pass

    def getButtonImage(self) -> str:
        """Returns the png image associated with that item"""
        pass


# Let's make good items first....
class DestroyAllBadItemsItem(ItemInterface):
    def getName(self):
        return "DestroyAllBadItemsItem"

    def isBad(self):
        return False

    def getPrice(self):
        return 40

    def getRarity(self):
        return 0.05

    def getFunctionality(self, player, player2):
        didPop = False
        for i in range(player.getInventoryLength()):
            if player.getInventoryItem(i).isBad:
                player.getInventory.pop(i)
                didPop = True
        return didPop

    def getButtonImage(self):
        # TODO: NEED IMAGE
        pass


class ThirdDiceItem(ItemInterface):
    def getName(self):
        return "ThirdDiceItem"

    def isBad(self):
        return False

    def getPrice(self):
        return 15

    def getRarity(self):
        return 0.13

    def getFunctionality(self, player, player2):
        if player.toggleSetThirdDiceroll:
            return False
        player.toggleSetThirdDiceroll()
        print(f"Player {player.getPlayerID} now has a third dice roll")
        return True

    def getButtonImage(self):
        # TODO: NEED IMAGE
        pass


class SpeedBoostItem(ItemInterface):
    def getName(self):
        return "SpeedBoostItem"

    def isBad(self):
        return False

    def getPrice(self):
        return 10

    def getRarity(self):
        return 0.18

    def getFunctionality(self, player, player2):
        if player.toggleSpeedBoost():
            return False
        player.toggleSpeedBoost()
        return True

    def getButtonImage(self):
        # TODO: NEED IMAGE
        pass


class GainMoneyRandomItem(ItemInterface):
    def getName(self):
        return "GainMoneyRandomItem"

    def isBad(self):
        return False

    def getPrice(self):
        return 30

    def getRarity(self):
        return 0.25

    def getFunctionality(self, player, player2):
        money = random.choice(range(0, 51))
        player.setMoney(money)  # Now need to display the money
        print(f"Player {player.getPlayerID()} got {money} and now has {player.getMoney()}")

    def getButtonImage(self):
        # TODO: NEED IMAGE
        pass


class TeleportCloseItem(ItemInterface):
    def getName(self):
        return "TeleportCloseItem"

    def isBad(self):
        return False

    def getPrice(self):
        return 25

    def getRarity(self):
        return 0.05

    def getFunctionality(self, player, player2):
        pass

    def getButtonImage(self):
        # TODO: NEED IMAGE
        pass


class SabotageDice(ItemInterface):
    def getName(self):
        return "SabotageDiceItem"

    def isBad(self):
        return False

    def getPrice(self):
        return 15

    def getRarity(self):
        return 0.10

    def getFunctionality(self, player, player2):
        if player2.getOneDiceRollBad():
            print(f"Player {player2.getPlayerID} already has the debuff of having only one Dice Roll")
            return False
        player2.toggleSetOneDiceroll()
        print(f"Player {player.getPlayerID()} made Player {player2.getPlayerID()} only roll one dice")
        return True

    def getButtonImage(self):
        # TODO: NEED IMAGE
        pass


class StealItem(ItemInterface):
    def getName(self):
        return "StealItemItem"

    def isBad(self):
        return False

    def getPrice(self):
        return 40

    def getRarity(self):
        return 0.16

    def getFunctionality(self, player, player2):
        if player2.getInventoryLength() == 0:
            return False
        # Get the winning players requested item
        player.setInventory(player2.removeInventoryItem(player.getItemIndex()))
        return True

    def getButtonImage(self):
        # TODO: NEED IMAGE
        pass


class OpponentLoseTurnItem(ItemInterface):
    def getName(self):
        return "OpponentLoseTurnItem"

    def isBad(self):
        return False

    def getPrice(self):
        return 50

    def getRarity(self):
        return 0.08

    def getFunctionality(self, player, player2):
        if player2.getLostTurn():
            return False
        player2.setLostTurn()
        return True

    def getButtonImage(self):
        # TODO: NEED IMAGE
        pass


# Let's do the bad items now....
class MoveOneSpotLess(ItemInterface):
    def getName(self):
        return "OpponentLoseTurnItem"

    def isBad(self):
        return True

    def getPrice(self):
        return 15

    def getRarity(self):
        return 0.222

    def getFunctionality(self, player, player2):
        if player.getMoveOneSpotLess():
            return False
        player.toggleMoveOneSpotLess()
        return True

    def getButtonImage(self):
        # TODO: NEED IMAGE
        pass


class InvertedControlsItem(ItemInterface):
    def getName(self):
        return "InvertedControlsItem"

    def isBad(self):
        return True

    def getPrice(self):
        return 40

    def getRarity(self):
        return 0.222

    def getFunctionality(self, player, player2):
        if player.getInvertedControls():
            print(f"Player {player.getPlayerID} already has inverted controls on")
            return False
        print(f"Player {player.getPlayerID()} now has set inverted Controls")
        player.setInvertedControls(True)
        return True

    def getButtonImage(self):
        # TODO: NEED IMAGE
        pass


class ChangeSpotsItem(ItemInterface):
    def getName(self):
        return "ChangeSpotsItem"

    def isBad(self):
        return True

    def getPrice(self):
        return 40

    def getRarity(self):
        return 0.192

    def getFunctionality(self, player, player2):
        pass

    def getButtonImage(self):
        # TODO: NEED IMAGE
        pass


class LostMoneyRandomItem(ItemInterface):
    def getName(self):
        return "LostMoneyRandomItem"

    def isBad(self):
        return True

    def getPrice(self):
        return 40

    def getRarity(self):
        return 0.192

    def getFunctionality(self, player, player2):
        pass

    def getButtonImage(self):
        # TODO: NEED IMAGE
        pass


class OneDiceItem(ItemInterface):
    def getName(self):
        return "OneDiceItem"

    def isBad(self):
        return True

    def getPrice(self):
        return 20

    def getRarity(self):
        return 0.172

    def getFunctionality(self, player, player2):
        if player.getOneDiceRollGood():
            return False
        player.toggleSetOneDicerollGood()
        return True

    def getButtonImage(self):
        # TODO: NEED IMAGE
        pass
