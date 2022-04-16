class minigameData():
    def __init__(self, player1W, player2W, player3W, player4W, player1E, player2E, player3E, player4E):
        self.totalPlayers = [player1W, player2W, player3W, player4W]
        self.earnings = [player1E, player2E, player3E, player4E]
        #Factored, much more effective
        # self.player1W = player1W
        # self.player2W = player2W
        # self.player3W = player3W
        # self.player4W = player4W

    def playerOneWon(self):
        return self.totalPlayers[0]

    def playerTwoWon(self):
        return self.totalPlayers[1]

    def playerThreeWon(self):
        return self.totalPlayers[2]

    def playerFourWon(self):
        return self.totalPlayers[3]

    def playerOneEarnings(self):
        return self.earnings[0]

    def playerTwoEarnings(self):
        return self.earnings[1]

    def playerThreeEarnings(self):
        return self.earnings[2]

    def playerFourEarnings(self):
        return self.earnings[3]