def setup():
    size(1920, 1080)
    global PImage img
    img = loadImage("1080p.jpg")

def draw():
    global img
    image(img, 0, 0)
