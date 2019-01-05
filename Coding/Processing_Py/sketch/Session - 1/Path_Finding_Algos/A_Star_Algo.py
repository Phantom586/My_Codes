from random import random
cols = 50
rows = 50
grid = [None]*cols

openSet = []
closedSet = []
path = []

def heuristic(a, b):
    d = dist(a.i, a.j, b.i, b.j)
    #d = abs(a.i-b.i) + abs(a.j-b.j)
    return d

def removeFromArray(arr, elt):
    # Range Modified to Traverse array in Reverse Order
    for i in range(len(arr) - 1, -1, -1):
        if arr[i] == elt:
            list_splice(arr, i, 1)

class Spot(object):
    def __init__(self, i, j):
        self.i = i
        self.j = j
        self.f = 0
        self.g = 0
        self.h = 0
        self.neighbors = []
        self.previous = None
        self.wall = False

        if random() < 0.2:
            self.wall = True

    def show(self, col):
        #fill(col)
        if self.wall:
            fill(0)
            noStroke()
            ellipse(self.i * w + w / 2, self.j * h + h / 2, w / 2, h / 2)

        #rect(self.i * w, self.j * h, w - 1, h - 1)

    def addNeighbors(self, grid):
        i = self.i
        j = self.j
        if i < cols - 1:
            self.neighbors.append(grid[i + 1][j])
        if i > 0:
            self.neighbors.append(grid[i - 1][j])
        if j < rows - 1:
            self.neighbors.append(grid[i][j + 1])
        if j > 0:
            self.neighbors.append(grid[i][j - 1])
        if i > 0 and j > 0:
            self.neighbors.append(grid[i - 1][j - 1])
        if i < cols - 1 and j > 0:
            self.neighbors.append(grid[i + 1][j - 1])
        if i > 0 and j < rows - 1:
            self.neighbors.append(grid[i - 1][j + 1])
        if i < cols - 1 and j < rows - 1:
            self.neighbors.append(grid[i + 1][j + 1])


def setup():
    global start,end,openSet,w,h
    size(600,600)
    print('A*')

    w = width / cols
    h = height / rows

    for i in range(cols):
        grid[i] = [None]*rows

    for i in range(cols):
        for j in range(rows):
            grid[i][j] = Spot(i, j)

    for i in range(cols):
        for j in range(rows):
            grid[i][j].addNeighbors(grid)

    start = grid[0][0]
    end = grid[cols - 1][rows - 1]
    start.wall = False
    end.wall = False

    openSet.append(start)

    #print(grid)

def draw():
    global openSet,closedSet,path,current
    if len(openSet) > 0:
        winner = 0
        for i in range(len(openSet)):
            if openSet[i].f < openSet[winner].f:
                winner = i

        current = openSet[winner]

        if current == end:
            noLoop()
            print("DONE!!")

        removeFromArray(openSet, current)
        closedSet.append(current)

        neighbors = current.neighbors
        for i in range(len(neighbors)):
            neighbor = neighbors[i]
            if neighbor not in closedSet and not neighbor.wall:
                tempG = current.g + 1
                newPath = False

                if neighbor in openSet:
                    if tempG < neighbor.g:
                        neighbor.g = tempG
                        newPath = True
                else:
                    neighbor.g = tempG
                    newPath = True
                    openSet.append(neighbor)

                if newPath:
                    neighbor.h = heuristic(neighbor,  end)
                    neighbor.f = neighbor.g + neighbor.h
                    neighbor.previous = current

    else:
        # No Solution\
        print('No Solution!!')
        noLoop()
        return

    background(255)

    for i in range(cols):
        for j in range(rows):
            grid[i][j].show(color(255))

    # for i in closedSet:
    #     i.show(color(255, 0, 0))

    # for i in openSet:
    #     i.show(color(0, 255, 0))

    path = []
    temp = current
    while(temp.previous):
        path.append(temp)
        temp = temp.previous

    #for i in range(len(path)):
        #path[i].show(color(0, 0, 255))

    noFill()
    stroke(255, 0, 255)
    strokeWeight(w / 2)
    beginShape()
    for i in range(len(path)):
        vertex(path[i].i * w + w / 2, path[i].j * h + h / 2)
    endShape()


def list_splice(target, start, delete_count=None, *items):
    """Remove existing elements and/or add new elements to a list.

    target        the target list (will be changed)
    start         index of starting position
    delete_count  number of items to remove (default: len(target) - start)
    *items        items to insert at start index

    Returns a new list of removed items (or an empty list)
    """
    if delete_count == None:
        delete_count = len(target) - start

    # store removed range in a separate list and replace with *items
    total = start + delete_count
    removed = target[start:total]
    target[start:total] = items

    return removed