import pygame
import src.engine.scenecreator.tile as tile
#Takes in a tilemap of integers and a list of images. Paints the images on the screen.
#Only called once for static objects but will be used for extra layers later.
def drawScene(window, tilemap, images):
    window.fill((0, 0, 0)) #Blank out the screen
    for row in range(len(tilemap)): #For every row in the tilemap
        for col in range(len(tilemap[0])): #For every sprite in this row
            spriteValue = tilemap[row][col] #Get numerical value for sprite
            if(spriteValue==0): #If no sprite is here, skip over it
                continue
            currImage = images[spriteValue] #Get reference to sprite (indexes correspond to sprites)
            x = col * currImage.get_width() #Find it's position on the tilemap and multiply that by the image res
            y = row * currImage.get_height()
            window.blit(currImage, (x, y)) #Paint the sprite on screen

#Similar to DrawScene but is more useful for static tiles. Sprites that do not need to be rendered every
#time can be referenced here without relying on the draw function.
def generateTiles(tilemap, images):
    staticTiles = []
    for row in range(len(tilemap)): #For every row in the tilemap
        for col in range(len(tilemap[0])): #For every sprite in this row
            spriteValue = tilemap[row][col] #Get numerical value for sprite
            if(spriteValue==0): #If no sprite is here, skip over it
                continue
            currImage = images[spriteValue] #Get reference to sprite (indexes correspond to sprites)
            x = col * currImage.get_width() #Find the sprites position on the tilemap and multiply by the image res
            y = row * currImage.get_height()
            newTile = tile.tile(currImage, x, y) #Create a tile object with the specified position
            staticTiles.append(newTile) #Add it to the list of tile objects to return at ends
    return staticTiles
