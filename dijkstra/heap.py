# an indexed priority queue

from operator import gt, lt

class Heap:
    heap = [None]
    value = {}
    indices = {}            # keep track of an item's index in the list representing the tree
    comparator = None

    def __init__(self, maxq=False):
        if maxq:
            self.comparator = gt
        else:
            self.comparator = lt

    def contains(self, item):
        return item in self.indices     # constant-time operation
        
    def empty(self):
        return len(self.heap) == 1      # the list only has the dummy item in it

    # given two item's indices, swap their positions
    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
        self.indices[self.heap[i]] = i
        self.indices[self.heap[j]] = j

    # given two item's indices, 
    # decide whether the item in the i-th position of the tree/list is prior
    def is_prior(self, i, j):
        return self.comparator(self.value[self.heap[i]], self.value[self.heap[j]])

    # given an item's index, try to percolate the item up the tree
    def bubble_up(self, pos):
        parent = pos // 2

        while parent >= 1 and self.is_prior(pos, parent):
            self.swap(pos, parent)

            pos = parent
            parent = pos // 2
            
    # given an item's index, try to percolate down the tree
    def bubble_down(self, pos):
        left = pos * 2

        while left < len(self.heap):
            # of the node's two children, take the one with the higher priority
            right = left + 1
            if right < len(self.heap) and self.is_prior(right, left):
                m = right
            else:
                m = left

            # if item isn't less prior, it can stay where it is
            if not self.is_prior(m, pos):
                break
            
            self.swap(pos, m)
            
            pos = m
            left = pos * 2

    # place an item of some value in the tree
    def insert(self, item, val):
        # place the item in the tree and set its value
        self.heap.append(item)
        self.value[item] = val
        
        # set the item's index
        pos = len(self.heap) - 1
        self.indices[item] = pos

        # sort out the new order
        self.bubble_up(pos)

    # remove and return the top-priority element
    def remove(self):
        if self.empty():
            return None

        # remove the top-priority element
        m = self.heap[1]
        self.value.pop(m)
        self.indices.pop(m)
        
        # replace top-priority item with lowest priority item
        # sort out the new order
        u = self.heap.pop()         # lowest priority item is at the end of the list
        if not self.empty():        # top-priority item could be lowest priority item
            self.heap[1] = u
            self.indices[u] = 1
            self.bubble_down(1)

        return m

    # update an item's value
    def update(self, item, val):
        self.value[item] = val
        pos = self.indices[item]
        self.bubble_up(pos)         # bubble_up() assumes the item's priority increases
