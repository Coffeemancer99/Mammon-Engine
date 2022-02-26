import node
class graph():
    def __init__(self):
        self.root = None

    def add(self, value, nID):
        if(self.root==None):
            self.root = node.node(value, nID)
            return self.root
        newNode = node.node(value, nID)
        return newNode

