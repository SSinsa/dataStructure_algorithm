class MaxHeap:

    def __init__(self):
        self.data = [None]


    def insert(self, item):
        self.data.append(item)
        nodeIdx = self.data.index(item)
        
        while nodeIdx//2 != 0 and item > self.data[nodeIdx//2]:
            self.data[nodeIdx], self.data[nodeIdx//2] = self.data[nodeIdx//2], self.data[nodeIdx]
            nodeIdx = nodeIdx//2
            
def solution(x):
    return 0
