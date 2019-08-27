#20강 이진탐색트리
#하나를 기준으로 그 값보다 작은 것은 전부 왼쪽, 큰 값은 전부 오른쪽에 존재
#배열을 이룬 이진탐색과 비슷

# 장점
# - 데이터 원소의 추가, 삭제가 용이
# 단점
# - 공간 소요가 큼(배열은 데이터만 주르륵 나열하는데, 트리는 부모와 자식들의 값을 모두 가지고 있어야해서)

# 항상 O(logn)의 탐색 복잡도?? -> 이진탐색트리가 항상 이 복잡도를 가지지 않음

# 이진 탐색 트리의 추상적 자료구조
# - 데이터 : 각 노드는 key, value의 쌍으로 표현
# insert(key,data) - 트리에 주어진 데이터 원소를 추가
# remove(key) - 특정 원소를 트리로부터 삭제
# lookup(key) - 특정 원소를 검색
# inorder() - 키의 순서대로 데이터 원소를 나열
# min() max() - 최소 키, 최대 키를 가지는 원소를 각각 탐색


class Node:

    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.left = None
        self.right = None


    def insert(self, key, data):
        if key < self.key:
            if self.left:
                self.left.insert(key, data) 
            else:
                self.left=Node(key,data)
        elif key > self.key:
            if self.right:
                self.right.insert(key, data)
            else:
                self.right=Node(key,data)    
        else: raise KeyError('KeyError')


    def inorder(self):
        traversal = []
        if self.left:
            traversal += self.left.inorder()
        traversal.append(self)
        if self.right:
            traversal += self.right.inorder()
        return traversal


class BinSearchTree:

    def __init__(self):
        self.root = None


    def insert(self, key, data):
        if self.root:
            self.root.insert(key, data)
        else:
            self.root = Node(key, data)


    def inorder(self):
        if self.root:
            return self.root.inorder()
        else:
            return []


def solution(x):
    return 0