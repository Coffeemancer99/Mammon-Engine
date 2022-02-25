#This function will handle any object that remains still for the duration of a scene.
def staticHandler(staticTiles, obj):
    for tile in staticTiles: #For every tile in the tile list
        # Vertical Case
        if tile.rectCol.colliderect(obj.rect.x, obj.rect.y + obj.dY, obj.width-5, obj.height):#Y collision has occured
            if(tile.rectCol.top == obj.rect.bottom): #When the acting object touches the ground...
                obj.jumped = False #They are no longer jumping
            if obj.velY < 0: #If the acting object is moving up but is colliding, they should no longer be moving
                obj.dY = tile.rectCol.bottom - obj.rect.top
                obj.vel_y = 0
            else: #This handles the positive y velocity, the acting object should not exceed the tile below
                obj.dY = tile.rectCol.top - obj.rect.bottom
                obj.vel_y = 0 #Prevent them from falling further
        # Horizontal case. If they are going to hit a tile the next frame, don't let them
        if tile.rectCol.colliderect(obj.rect.x + obj.dX, obj.rect.y, obj.width, obj.height):
            obj.dX = 0




