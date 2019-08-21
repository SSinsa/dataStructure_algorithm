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

prec = {
    '*': 3, '/': 3,
    '+': 2, '-': 2,
    '(': 1
}

def solution(S):
    opStack = ArrayStack()
    answer = ''
    for s in S:
        if s in prec:
            if opStack.isEmpty():
                opStack.push(s)
                continue
            elif prec[opStack.peek()] - prec[s] in (1, 0):
                answer += opStack.pop()
                opStack.push(s)
            else:
                opStack.push(s)
        elif s == ')':
            while opStack.peek() != '(':
                temp = opStack.pop()
                answer = answer + temp
            opStack.pop()
        else :
            answer = answer + s
    if opStack.isEmpty():
        return answer
    else:
        while opStack.size() != 0:
            answer += opStack.pop()
    return answer