from spriteLoader import SpriteLoader

class Player:

    # make x and y their tile's x and y
    x = None
    y = None
    width = None
    height = None
    image = SpriteLoader().loadImage("testSprite.png")


    def __init__(self):
        pass