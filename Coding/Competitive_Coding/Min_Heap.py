# A min heap is a Complete binary Tree in which the value in each internal node is maller than or equal to the values
# in the children of that node.
# Mapping the Elements of a Heap into an array is trivial : If a node is stored at 'k' index, then its left child is
# stored at index '2k + 1' and its right child at index '2k + 2'.


class MinHeap:

    size = 0
    maxsize = 0
    heap = [0]
    front = 1

    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.size = 0
        MinHeap.heap[0] = -1

    @staticmethod
    def parent(pos):
        return pos // 2

    @staticmethod
    def leftChild(pos):
        return 2 * pos

    @staticmethod
    def rightChild(pos):
        return (2 * pos) + 1

    def isLeaf(self, pos):
        if (pos >= (self.size / 2)) and (pos <= self.size):
            return True
        else:
            return False

    def swap(self, p1, p2):
        MinHeap.heap[p1], MinHeap.heap[p2] = MinHeap.heap[p2], MinHeap.heap[p1]

    def minHeapify(self, pos):
        if not self.isLeaf(pos):
            if (MinHeap.heap[pos] > MinHeap.heap[self.leftChild(pos)]) or (MinHeap.heap[pos] > MinHeap.heap[self.rightChild(pos)]):
                if MinHeap.heap[self.leftChild(pos)] < MinHeap.heap[self.rightChild(pos)]:
                    self.swap(pos, self.leftChild(pos))
                    self.minHeapify(self.leftChild(pos))
                else:
                    self.swap(pos, self.rightChild(pos))
                    self.minHeapify(self.rightChild(pos))

    def insert(self, element):
        if self.size >= self.maxsize:
            return
        MinHeap.heap.append(element)
        self.size += 1
        current = self.size

        while MinHeap.heap[current] < MinHeap.heap[self.parent(current)]:
            self.swap(current, self.parent(current))

    def remove(self):
        popped = MinHeap.heap[self.front]
        self.size -= 1
        MinHeap.heap[self.front] = MinHeap.heap[self.size]
        self.minHeapify(self.front)
        return popped

    def print(self):
        for i in range(1, int(self.size/2)+1):
            print("PARENT : ", MinHeap.heap[i], " LEFT CHILD : ", MinHeap.heap[2 * i], " RIGHT CHILD : ", MinHeap.heap[2 * i + 1])

    def minHeap(self):
        for i in range(self.size//2, 1, -1):
            self.minHeapify(i)


mHeap = MinHeap(15)
mHeap.insert(5)
mHeap.insert(3)
mHeap.insert(17)
mHeap.insert(10)
mHeap.insert(84)
mHeap.insert(19)
mHeap.insert(6)
mHeap.insert(22)
mHeap.insert(9)
mHeap.minHeap()

mHeap.print()
print(mHeap.heap)
print("Min Value is : ", mHeap.remove())
print(mHeap.heap)
