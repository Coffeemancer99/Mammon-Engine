def staticHandler(staticTiles, obj):
    for tile in staticTiles: #For every tile in the tile list
        if tile.rectCol.colliderect(obj.rect.x, obj.rect.y + obj.dY, obj.width-5, obj.height): # A collision has occurred
            # Vertical Case
            if(tile.rectCol.top == obj.rect.bottom):
                obj.jumped = False
            if obj.velY < 0:

                obj.dY = tile.rectCol.bottom - obj.rect.top
                obj.vel_y = 0
            else:
                obj.dY = tile.rectCol.top - obj.rect.bottom
                obj.vel_y = 0
        if tile.rectCol.colliderect(obj.rect.x + obj.dX, obj.rect.y, obj.width, obj.height):

            obj.dX = 0




