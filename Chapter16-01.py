#16강 우선순위 큐(Priority Queue)
# FIFO (First-In First-Out)
# Eq => 6 7 3 2
# Dq => 2 3 6 7 (값이 작은 것이 우선순위가 높을 때)

# Enqueue 할 때 우선순위 순서를 유지하도록
# Dequeue 할 때 우선순위 높은 것을 선택 -> 모든 원소를 다 봐야하기 때문에 불리함
# -> 전자가 더 유리하다

# 선형 배열 이용
# 연결 리스트 이용
# -> 시간적으로 볼 때 연결리스트가 유리함(중간 삽입이 빈번하기 때문)
# -> 메모리 공간 소요에서는 선형 배열이 유리 
# -> 그러나 시간적으로 유리한 것을 선택하는 것 좋음

#getAt 사용x, curr로 가리킴, getAt메소드를 이용하면 포지션까지 세어감.

class Node:

    def __init__(self, item):
        self.data = item
        self.prev = None
        self.next = None


class DoublyLinkedList:

    def __init__(self):
        self.nodeCount = 0
        self.head = Node(None)
        self.tail = Node(None)
        self.head.prev = None
        self.head.next = self.tail
        self.tail.prev = self.head
        self.tail.next = None


    def __repr__(self):
        if self.nodeCount == 0:
            return 'LinkedList: empty'

        s = ''
        curr = self.head
        while curr.next.next:
            curr = curr.next
            s += repr(curr.data)
            if curr.next.next is not None:
                s += ' -> '
        return s


    def getLength(self):
        return self.nodeCount


    def traverse(self):
        result = []
        curr = self.head
        while curr.next.next:
            curr = curr.next
            result.append(curr.data)
        return result


    def reverse(self):
        result = []
        curr = self.tail
        while curr.prev.prev:
            curr = curr.prev
            result.append(curr.data)
        return result


    def getAt(self, pos):
        if pos < 0 or pos > self.nodeCount:
            return None

        if pos > self.nodeCount // 2:
            i = 0
            curr = self.tail
            while i < self.nodeCount - pos + 1:
                curr = curr.prev
                i += 1
        else:
            i = 0
            curr = self.head
            while i < pos:
                curr = curr.next
                i += 1

        return curr


    def insertAfter(self, prev, newNode):
        next = prev.next
        newNode.prev = prev
        newNode.next = next
        prev.next = newNode
        next.prev = newNode
        self.nodeCount += 1
        return True


    def insertAt(self, pos, newNode):
        if pos < 1 or pos > self.nodeCount + 1:
            return False

        prev = self.getAt(pos - 1)
        return self.insertAfter(prev, newNode)


    def popAfter(self, prev):
        curr = prev.next
        next = curr.next
        prev.next = next
        next.prev = prev
        self.nodeCount -= 1
        return curr.data


    def popAt(self, pos):
        if pos < 1 or pos > self.nodeCount:
            return None

        prev = self.getAt(pos - 1)
        return self.popAfter(prev)


    def concat(self, L):
        self.tail.prev.next = L.head.next
        L.head.next.prev = self.tail.prev
        self.tail = L.tail

        self.nodeCount += L.nodeCount


class PriorityQueue:

    def __init__(self):
        self.queue = DoublyLinkedList()


    def size(self):
        return self.queue.getLength()

    def isEmpty(self):
        return self.size() == 0

    def enqueue(self, x):
        newNode = Node(x)
        curr = self.queue.head

        while curr.next.data != None and x >= curr.next.data:
            curr = curr.next
        self.queue.insertAfter(curr, newNode)

    def dequeue(self):
        return self.queue.popAt(self.queue.getLength())

    def peek(self):
        return self.queue.getAt(self.queue.getLength()).data





def solution():
    test = PriorityQueue()
    test.__init__()
    test.enqueue(6)
    test.enqueue(7)
    test.enqueue(3)
    test.enqueue(2)
    print(test.queue)
    return 0

solution()

# <우선순위 큐에 대한 잘못된 오류들>
# 우선순위 큐가 힙이라는 것은 널리 알려진 오류이다. 
# 우선순위 큐는 "리스트"나 "맵"과 같이 추상적인 개념이다; 
# 마치 리스트는 연결 리스트나 배열로 구현될 수 있는 것과 같이, 
# 우선순위 큐는 힙이나 다양한 다른 방법을 이용해 구현될 수 있다.


# <시간복잡도>
# 배열 기반 데이터 삽입의 시간 복잡도 : O(n)
# 배열 기반 데이터 삭제의 시간 복잡도 : O(1)
# 연결 리스트 기반 데이터 삽입의 시간 복잡도 : O(n)
# 연결 리스트 기반 데이터 삭제의 시간 복잡도 : O(1)
# 힙 기반 데이터 삽입의 시간 복잡도 : O(log2의 n)
# 힙 기반 데이터 삭제의 시간 복잡도 : O(log2의 n)

# 우선순위 큐를 구현하는데 히프가 많이 사용됩니다.

# 히프/힙(Heap)
# 1. 완전 이진 트리(complete binary tree)
# 2. 최대 히프(max heap) or 최소 히프(min heap)

# - 히프의 노드 추가(insert) 연산과 추출(extract) 연산의 시간 복잡도는 O(log2n)
# - 그렇기 때문에 히프의 삽입 연산을 이용하는 히프 정렬(heap sort) 최악, 평균, 최선 모두 시간 복잡도는 O(log2n)


# 우선순위 큐(priority queue)는 일반적인 큐의 특성을 가지지 않고 다음과 같은 특성을 가집니다.
# - 일반적인 큐와 같이 FIFO(First-In-First-Out)의 성질을 가진 것이 아니라,
# 반환 순서는 삽입되는 순서와는 상관없이 오직 키값의 크기에 의해 결정됨
# - 히프는 우선순위 큐를 구현하는 가장 효과적인 방법 중 하나.
# 최대 히프에서 자료를 하나씩 삭제하면 우선순위가 높은 순으로 반환
# 최소 히프에서 자료를 하나씩 삭제하면 우선순위가 낮은 순으로 반환

# - 무엇보다도
# 히프의 insert, extract 연산의 시간 복잡도가
# 리스트 자료 삭제, 삽입 연산의 시간 복잡도 O(n)보다
# 효율적이기 때문에 속도 면에서 개선된다.

# [출처] 히프(heap)와 우선순위 큐(priority queue)|작성자 예비개발자



