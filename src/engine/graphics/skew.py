# Work in progress. Take a sprite, and line-by-line, stretch the pixels to skew it.

def skew_line(line, m): # WORK IN PROGRESS m = end length
    n = 0 # n = start length, not counting empty pixels
    for pixel in line:
        if pixel: n += 1
    r = m/n # each pixel in line gets stretched to r pixels, on average
    empty = len(line) - m # amount of empty space left after skewing
    assert r > 1
    toReturn = [0]*(int(empty/2)); empty -= int(empty/2)
    # print("m = {}, n = {}, r = {}, empty: {}, {}".format(m,n,r, empty, int(empty/2)))
    score = 0
    numAdded = 0
    for pixel in line:
        if not pixel: continue
        score += r
        while score >= 1:
            score -= 1
            toReturn.append(pixel)
            numAdded += 1
    if(score > 0):
        score = 0
        toReturn.append(toReturn[-1])
    if(empty):
        for i in range(empty):
            toReturn.append(0)
    print("m = {}, n = {}, r = {}, score: {}".format(m,n,r, score))
    print("toReturn = ", toReturn)

    return toReturn

def skew_image(image, scale): # WORK IN PROGRESS
    # TODO: rotate image before and after
    height = image.get_height()
    width = image.get_width()
    array = pygame.PixelArray(image)
    for i in len(array):
        row = [col[i] for col in array]

    row = [col[0] for col in array]
    numPixels = 0
    for pixel in row:
        if not pixel: continue
        numPixels += 1


    array.close
    return toReturn