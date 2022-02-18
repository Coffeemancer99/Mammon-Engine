

class PathManager:

    def __init__(self):
        pass

    def setBoard(self, board):
        self.board = board

    # look at type attr to see if list at board location contains tile type
    def getMovesFromCurPos(self, x, y, typeAttr):
        allMoves = []

        nw = self.board.getObjsAt(x - 1, y + 1)
        allMoves.append(nw)

        w = self.board.getObjsAt(x - 1, y)
        allMoves.append(w)

        sw = self.board.getObjsAt(x - 1, y - 1)
        allMoves.append(sw)

        s = self.board.getObjsAt(x, y - 1)
        allMoves.append(s)

        se = self.board.getObjsAt(x + 1, y - 1)
        allMoves.append(se)

        e = self.board.getObjsAt(x + 1, y)
        allMoves.append(e)

        ne = self.board.getObjsAt(x + 1, y + 1)
        allMoves.append(ne)

        n = self.board.getObjsAt(x, y + 1)
        allMoves.append(n)

        result = []
        for move in allMoves:
            if move:  # if the current space being looked at is not empty
                if typeAttr in move:
                    result.append(move)

        return result