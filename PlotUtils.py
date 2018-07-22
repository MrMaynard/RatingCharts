import random

def getRandomColor(r, g, b):
    red = random.randint(0, 256)
    green = random.randint(0, 256)
    blue = random.randint(0, 256)
    red = (red + r) / 2
    green = (green + g) / 2
    blue = (blue + b) / 2
    return (red, green, blue)

def color2PlotlyString(t, a):
    return 'rgba({}, {}, {}, {})'.format(t[0], t[1], t[2], a)

