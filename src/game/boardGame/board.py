'''
OLD CODE
board.py created by Andrew Bunn
Board class implemented by Andrew Bunn
'''

class Board:
    def __init__(self):
        pass


    def generateBoard(self, width, height):
        """
        generates a 2d list of lists of dimensions "width" and "height"
        :param width: width of board
        :param height: height of board
        """
        self.width = width
        self.height = height
        # init a matrix of lists
        self.matrix = [[[] for x in range(width)] for y in range(height)]


    def getWidth(self):
        """
        get the width of the board
        :return: returns board width
        """
        return self.width


    def getHeight(self):
        """
        get the height of the board
        :return: returns the board height
        """
        return self.height


    def placeObject(self, x, y, obj):
        """
        places the specified object on the board at the specified location
        :param x: x coord
        :param y: y coord
        :param obj: object to be inserted
        """
        self.matrix[x-1][y-1].append(obj)


    def getObjsAt(self, x, y):
        """
        get objects out of a coord\
        CURRENTLY just returns what is at a coord
        :param x: x coord
        :param y: y coord
        :return: return a list of what lies at the specified coordinate
        """
        if(x > self.width or x < 1):
            return None
        if(y > self.height or y < 1):
            return None

        return self.matrix[x-1][y-1]


    def debugBoard(self):
        """
        prints out the whole board cell by cell
        """
        for x in range(0, self.width):
            for y in range(0, self.height):
                print(x+1, y+1, self.getObjsAt(x+1, y+1))