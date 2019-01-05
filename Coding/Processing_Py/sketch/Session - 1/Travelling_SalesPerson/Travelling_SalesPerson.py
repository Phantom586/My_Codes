cities = []
totalCities = 6
orders = []

recordDistance = 0

totalPermutations = 0
count = 0

def setup():
    size(800, 600)
    for i in range(totalCities):
        v = PVector(random(width), random(height/2))
        cities.append(v)
        orders.append(i)

    d = calcDistance(cities, orders)
    global recordDistance,bestEver,totalPermutations
    recordDistance = d
    bestEver = orders[:]

    totalPermutations = factorial(totalCities)
    print(totalPermutations)

def draw():
    global bestEver,totalPermutations
    background(0)
    fill(255)
    for i in range(len(cities)):
        ellipse(cities[i].x, cities[i].y, 4, 4)

    stroke(255)
    strokeWeight(1)
    noFill()
    beginShape()
    for i in range(len(orders)):
        n = orders[i]
        vertex(cities[n].x, cities[n].y)
    endShape()

    translate(0, height/2)
    stroke(255, 0, 255)
    strokeWeight(4)
    noFill()
    beginShape()
    for i in range(len(orders)):
        n = bestEver[i]
        vertex(cities[n].x, cities[n].y)
    endShape()

    # i = floor(random(len(cities)))
    # j = floor(random(len(cities)))
    # swap(cities, i, j)

    d = calcDistance(cities, orders)
    global recordDistance
    if d < recordDistance:
        recordDistance = d
        bestEver = orders[:]
        print(recordDistance)

    textSize(30)
    # s = ''
    # for i in range(len(orders)):
    #     s += str(orders[i])
    # fill(255)
    global count
    percent = 100 * (count / totalPermutations)
    text(percent, 20, height/2 - 50)

    nextOrder()


def swap(a, i, j):
    a[i],a[j] = a[j],a[i]


def calcDistance(points, orders):
    sum = 0
    for i in range(len(orders) - 1):
        cityA = points[orders[i]]
        cityB = points[orders[i+1]]
        d = dist(cityA.x, cityA.y, cityB.x, cityB.y)
        sum += d
    return sum



#Lexical Ordering Algorithm
def nextOrder():
    global orders,count
    count += 1
    largestI = -1
    for i in range(len(orders) - 1):
        if orders[i] < orders[i + 1]:
            largestI = i
    if largestI == -1:
        noLoop()
        print('finished')
    #STEP 2 :
    largestJ = -1
    for j in range(len(orders)):
        if orders[largestI] < orders[j]:
            largestJ = j
    
    #STEP 3 :
    swap(orders, largestI, largestJ)

    #STEP 4 : reverse array from largestI + 1 till end
    endArray = list_splice(orders, largestI + 1)
    endArray.reverse()
    orders = orders + endArray

    # textSize(64)
    # s = ''
    # for i in range(len(orders)):
    #     s += str(orders[i])
    # fill(255)
    # text(s, 20, height/2)


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

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)