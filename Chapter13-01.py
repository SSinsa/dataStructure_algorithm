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


def splitTokens(exprStr):
    tokens = []
    val = 0
    valProcessing = False
    for c in exprStr:
        if c == ' ':
            continue
        if c in '0123456789':
            val = val * 10 + int(c)
            valProcessing = True
        else:
            if valProcessing:
                tokens.append(val)
                val = 0
            valProcessing = False
            tokens.append(c)
    if valProcessing:
        tokens.append(val)

    return tokens


def infixToPostfix(tokenList):
    prec = {
        '*': 3,
        '/': 3,
        '+': 2,
        '-': 2,
        '(': 1,
    }

    opStack = ArrayStack()
    postfixList = []
    for s in tokenList:
        if s in prec:
            if opStack.isEmpty():
                opStack.push(s)
                continue
            elif prec[opStack.peek()] - prec[s] in (1, 0):
                postfixList.append(opStack.pop())
                opStack.push(s)
            else:
                opStack.push(s)
        elif s == ')':
            while opStack.peek() != '(':
                temp = opStack.pop()
                postfixList.append(temp)
            opStack.pop()
        else :
            postfixList.append(s)
    if opStack.isEmpty():
        return postfixList
    else:
        while opStack.size() != 0:
            postfixList.append(opStack.pop())
    return postfixList


def postfixEval(tokenList):
    opSet = {'+','-','*','/'}
    while not tokenList:
        for s in tokenList:
            if s in opSet:
                front = tokenList.pop(tokenList.index(s)-2)
                back = tokenList.pop(tokenList.index(s)-1)
                if s == '+':
                    tokenList.insert(tokenList.index(s), front + back)
                elif s == '-':
                    tokenList.insert(tokenList.index(s), front - back)
                elif s == '*':
                    tokenList.insert(tokenList.index(s), front * back)
                else:
                    tokenList.insert(tokenList.index(s), float(front) / float(back))


def solution(expr):
    tokens = splitTokens(expr)
    postfix = infixToPostfix(tokens)
    val = postfixEval(postfix)
    return val