vals = [1, 2, 3]

def setup():
    size(800, 600)

def draw():
    background(0)
    global vals
    print(vals)

    #STEP 1 :
    largestI = -1
    for i in range(len(vals) - 1):
        if vals[i] < vals[i + 1]:
            largestI = i
    if largestI == -1:
        noLoop()
        print('finished')

    #STEP 2 :
    largestJ = -1
    for j in range(len(vals)):
        if vals[largestI] < vals[j]:
            largestJ = j
    
    #STEP 3 :
    swap(vals, largestI, largestJ)

    #STEP 4 : reverse array from largestI + 1 till end
    endArray = list_splice(vals, largestI + 1)
    endArray.reverse()
    vals = vals + endArray

    textSize(64)
    s = ''
    for i in range(len(vals)):
        s += str(vals[i])
    fill(255)
    text(s, 20, height/2)

def swap(a, i, j):
    a[i],a[j] = a[j],a[i]

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