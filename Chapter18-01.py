#17강 트리
#노드 (nodes) : 값과 정보를 가지고 있는 하나의 구조체
#간선 (edges) : 노드를 연결하는 선으로 노드 사이를 연결
#루트 노드 (root node) : 가장 상위 노드로 부모를 가지지 않는 노드
#리프 노드 (leaf nodes) : 가장 하위 노드로 자식을 가지지 않는 노드
#내부 노드 (internal nodes) : 자식 노드가 있는 노드
#부모 (parent) 노드
#자식 (child) 노드
#형제 (Sibiling) 노드 : 	같은 부모 노드의 자식 노드
#노드의 수준 (level) : 루트 노드부터의 거리
#노드의 차수 (degree) : 노드의 자식 갯수
#트리의 높이 (height) - 또는, 깊이 (depth) : 트리에서 부모에서 자식으로 내려갈 때, depth가 1 증가, root는 depth 0
#부분 트리 (서브트리; subtrees)
#이진 트리 (binary trees) : 한 노드가 가질 수 있는 자식 노드의 수가 제한되어 있지 않은 일반적인 트리와 달리, 최대 2개까지의 자식 노드만을 가질 수 있다
#포화 이진 트리 (full binary trees) : 모든 레벨의 노드가 꽉 찬 이진 트리를 의미
#완전 이진 트리 (complete binary trees) :마지막 레벨 이전까지는 포화 이진 트리이다가 
#   마지막 레벨에서 노드가 왼쪽부터 차례대로 채워져 있는 트리를 의미
#이진 트리의 종류는 포화 이진 트리(Full Binary Tree)와 완전 이진 트리(Complete Binary Tree), 편향 이진 트리(Skewed Binary Tree)가 있다. 



#18강 이진트리
#자식이 최대 두개!! -> 생각하기 쉬운 트리라서 기본적으로 사용

#이진트리의 추상적 자료구조
# 연산의 정의
# size() - 현재 트리에 포함되어 있는 노드의 수를 구함
# depth() - 현재 트리의 깊이 (또는 높이 height) 를 구함
# 순회 (traversal) ***

#     data
# left    right

# Node
#     data
#     left child
#     right child

#이진트리는 root만 가리키기만 해도 간선으로 연결되어 있어 연산 가능

# 전체 이진트리의 size()
# = left subtree의 size() + right subtree의 size() + (자기자신)   => 재귀적으로 구함

# 전체 이진트리의 depth()
# = left subtree의 depth() 와 right subtree의 depth() 중 더 큰것 + 1(자기자신) => 재귀적으로 구함


# 이진트리의 순회 (Traversal)
# - 깊이 우선 순회 (depth first traversal)
#     - 중위순회 inorder
#     - 전위순회 preorder
#     - 후위순회 postorder
# - 넓이 우선 순회 (breadth first traversal)

#        A
#    B       C
#  D   E   F   G
# H          J

# 중위 : H - D - B - E - A - F - J - C - G
# 전위 : A - B - D - H - E - C - F - J - G
# 후위 : H - D - E - B - J - F - G - C - A


class Node:

    def __init__(self, item):
        self.data = item
        self.left = None
        self.right = None


    def size(self):
        l = self.left.size() if self.left else 0
        r = self.right.size() if self.right else 0
        return l + r + 1


    def depth(self):
        l = self.left.depth() if self.left else 0
        r = self.right.depth() if self.right else 0
        d = l+1 if l >= r else r+1
        return d


class BinaryTree:

    def __init__(self, r):
        self.root = r

    def size(self):
        if self.root:
            return self.root.size()
        else:
            return 0


    def depth(self):
        if self.root:
            return self.root.depth()
        else:
            return 0


def solution(x):
    return 0
