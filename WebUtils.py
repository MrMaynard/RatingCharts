import urllib.request

def getContent(url):
    print("Reading HTML from: " + url)
    return str(urllib.request.urlopen(url).read())