'''
playerController.py created by Andrew Bunn
Player class implemented by Andrew Bunn

'''

'''
board.py created by Andrew Bunn
Board class implemented by Andrew Bunn
'''

class Board:
    def __init__(self):
        pass

    '''
    generateBoard - generates a 2d list of lists of dimensions
                    width and height
    width - width of the board
    height - height of the board
    '''
    def generateBoard(self, width, height):
        self.width = width
        self.height = height
        # init a matrix of zeros
        self.matrix = [[[] for x in range(width)] for y in range(height)]
        # need to init with lists

    '''
    getWidth - returns board width
    '''
    def getWidth(self):
        return self.width

    '''
    getHeight - returns board height
    '''
    def getHeight(self):
        return self.height

    '''
    placeObject - places the specified object on the board at
                  the specified location
    x - x coordinate
    y - y coordinate
    obj - object to be inserted
    '''
    def placeObject(self, x, y, obj):
        self.matrix[x-1][y-1].append(obj)

    '''
    getObjsAt - return whatever lies at the specified coordinate
                (will be a list)
    x - x coordinate
    y - y coordinate
    '''
    # get objects out of a coord
    # CURRENTLY just returns what is at a coord
    def getObjsAt(self, x, y):
        if(x > self.width or x < 1):
            return None
        if(y > self.height or y < 1):
            return None

        return self.matrix[x-1][y-1]


    # def isSpotOpen(self, x, y):
    #     return True

    '''
    debugBoard - prints out the whole board cell by cell
    '''

    def debugBoard(self):
        for x in range(0, self.width):
            for y in range(0, self.height):
                print(x+1, y+1, self.getObjsAt(x+1, y+1))