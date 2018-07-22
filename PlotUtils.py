import random

mixFactor = 0.75

def getRandomColor(r, g, b):
    red = random.randint(0, 256)
    green = random.randint(0, 256)
    blue = random.randint(0, 256)
    red = int((red * mixFactor) + (r * (1 - mixFactor)))
    green = int((green * mixFactor) + (g * (1 - mixFactor)))
    blue = int((blue * mixFactor) + (b * (1 - mixFactor)))
    return (red, green, blue)

def color2PlotlyString(t, a):
    return 'rgba({}, {}, {}, {})'.format(t[0], t[1], t[2], a)

def buildTitle(episode):
    return "Season " + str(episode.season) + \
           ", Episode " + str(episode.number) + " - " + episode.title

