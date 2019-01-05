from math import ceil
from random import randrange

symbolSize = 26

def setup():
    global symbol,symbolSize
    size(1920, 1080)
    global streams
    streams = []
    x = 0
    for i in range(width / symbolSize):
        stream = Stream()
        stream.generateSymbols(x, randrange(-1000, 0))
        streams.append(stream)
        x += symbolSize
    textSize(symbolSize)

def draw():
    global streams
    background(0, 150)
    for i in streams:
        i.render()
    

class Symbol(object):
    def __init__(self, x, y, speed, first):
        self.x = x
        self.y = y
        self.first = first
        self.speed = speed
        self.value = ' '
        self.switchInterval = floor(randrange(2, 20))

    def setToRandomSymbol(self):
        if frameCount % self.switchInterval == 0:
            self.value = chr(randrange(31, 128))   

    def rain(self):
        if self.y > height:
            self.y = 0
        else:
            self.y += self.speed


class Stream(object):
    def __init__(self):
        self.symbols = []
        self.totalSymbols = floor(randrange(5, 30))
        self.speed = randrange(5, 20)

    def generateSymbols(self, x, y):
        first = floor(randrange(0, 5)) == 1
        for i in range(self.totalSymbols + 1):
            symbol = Symbol(x, y, self.speed, first)
            symbol.setToRandomSymbol()
            self.symbols.append(symbol)
            y -= symbolSize
            first = False

    def render(self):
        for i in self.symbols:
            if i.first:
                fill(180, 255, 180)
            else:
                fill(0, 255, 70)
            text(i.value, i.x, i.y)
            i.rain()
            i.setToRandomSymbol()