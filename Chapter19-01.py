#19강 이진트리 - 넓이 우선순회 BFT
#같은 레벨의 노드들을 왼쪽부터 
#재귀 방식 비효율
#큐를 사용하면 좋을 듯
#자신을 꺼내고 자식이 있으며 자식 다 넣기
#       A
#   B       C
# D   E   F   G
#H          J
#
# A/  /B/C/  /D/E  /F/G/  /H/   /J/        =>EQ
#   A      B     C      D    E/F   G/H/J   =>DQ


# 1. (초기화) traversal <- 빈리스트, q <- 빈큐
# 2. 빈트리가 아니면, root node 를 q에 추가(enqueue)
# 3. q가 비어있지 않은 동안
#     3.1 node <-q 에서 원소를 추출 (dequeue)
#     3.2 node를 방문
#     3.3 node의 왼쪽, 오른쪽 자식 (있으면 들을)q에 추가


class ArrayQueue:

    def __init__(self):
        self.data = []

    def size(self):
        return len(self.data)

    def isEmpty(self):
        return self.size() == 0

    def enqueue(self, item):
        self.data.append(item)

    def dequeue(self):
        return self.data.pop(0)

    def peek(self):
        return self.data[0]


class Node:

    def __init__(self, item):
        self.data = item
        self.left = None
        self.right = None


class BinaryTree:

    def __init__(self, r):
        self.root = None(r)


    def bft(self):
        traversal = []
        queue = ArrayQueue()
#       A
#   B       C
# D   E   F   G
#H          J
#
# A/  /B/C/  /D/E  /F/G/  /H/   /J/        =>EQ
#   A      B     C      D    E/F   G/H/J   =>DQ
        if self.root:
            queue.enqueue(self.root)
            while queue.size() != 0:
                node = queue.dequeue()
                traversal.append(node.data)

                if node.left:
                    queue.enqueue(node.left)
                if node.right:
                    queue.enqueue(node.right)
        return traversal


def solution(x):
    return 0