#11강 강의 내용 
#비어있는 스택에서 데이터 원소를 꺼내려 할 때 -> 스택 언더플로우
#스택의 추상적 자료구조 구현
# 배열을 이용하여 구현 - python 리스트와 메서드를 이용
# 연결리스트를 이용하여 구현 - 양방향 연결리스트 구현

# 연산의 정의
# - size()
# - isEmpty()
# - push(x)
# - pop() -> 스택의 맨 위에 저장된 데이터 원소를 제거하면서 반환
# - peek() -> 스택의 맨 위에 저장된 데이터 원소를 반환 (제거x)


class ArrayStack:

    def __init__(self):
        self.data = []

    def size(self):
        return len(self.data)

    def isEmpty(self):
        return self.size() == 0

    def push(self, item):
        self.data.append(item)

    def pop(self):
        return self.data.pop()

    def peek(self):
        return self.data[-1]


def solution(expr):
    match = {
        ')': '(',
        '}': '{',
        ']': '['
    }
    S = ArrayStack()
    for c in expr:
        if c in '({[':
            S.push(c)
        elif c in match:
            if S.isEmpty():
                return False
            else:
                t = S.pop()
                if t != match[c]:
                    return False
    return True
