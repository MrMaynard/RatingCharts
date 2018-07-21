import random

def getRandomColor(r, g, b):
    red = random.randint(0, 256)
    green = random.randint(0, 256)
    blue = random.randint(0, 256)
    red = (red + r) / 2
    green = (green + g) / 2
    blue = (blue + b) / 2
    return (red, green, blue)

def toPlotlyString(r, g, b):
    return 'rgba({}, {}, {}, .9)'.format(r, g, b)

