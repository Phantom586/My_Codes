def setup():
    global img
    size(1366, 768)
    img = loadImage("1080p.jpg")
    
def draw():
    global img
    background(0)
    image(img, 0, 0, 1366, 768)
