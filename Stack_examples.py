from BasicDS import Stack

# Check for balance of parentheses
def parCheck(symbolstring):
    s = Stack()
    balanced = True
    
    for index in range(len(symbolstring)):
        symbol = symbolstring[index]
        if symbol in "([{":
            s.push(symbol)
        elif symbol in ")]}":
            if s.isEmpty() == True:
                balanced = False
                break
            else:
                top = s.pop()
                if not matches(top,symbol):
                    balanced = False
                    break

    if balanced and s.isEmpty():
        return True
    else:
        return False

def matches(open,close):
    opens = "([{"
    closes = ")]}"
    return opens.index(open) == closes.index(close)

# print(parCheck('()'))
# print(parCheck('(())))'))
# print(parCheck('(()(())(((()))))'))
# print(parCheck('([{5+6}])'))


# Decimal to binary
def divideBy2(decNum):
    remstack = Stack()

    while decNum > 0:
        rem = decNum % 2
        remstack.push(rem)
        decNum = decNum // 2

    binstring = ''
    while not remstack.isEmpty():
        binstring = binstring + str(remstack.pop())
    return binstring

def baseConverter(decNum, base):
    digits = "0123456789ABCDEF"
    remstack = Stack()

    while decNum > 0:
        rem = decNum % base
        remstack.push(rem)
        decNum = decNum // base

    binstring = ''
    while not remstack.isEmpty():
        binstring = binstring + digits[remstack.pop()]
    return binstring

# print(baseConverter()


# Precidence of equation, Infix to postfix or prefix notation
import string

def infixToPostfix(expr):
    prec = {'**': 4,
            '*': 3,
            '/': 3,
            '+': 2,
            '-': 2,
            '(': 1
           }

    opStack = Stack()
    postfixList = []
    tokenList = expr.split()
    alpha = set(string.ascii_uppercase)

    for token in tokenList:
        if token in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' or token in '0123456789':
            postfixList.append(token)
        elif token == '(':
            opStack.push(token)
        elif token == ')':
            toptoken = opStack.pop()
            while toptoken != '(':
                postfixList.append(toptoken)
                toptoken = opStack.pop()
        else:
            # must put not Stack.isEmpty() first to evaluate if there is a operation token or not
            while (not opStack.isEmpty()) and (prec[opStack.peek()] >= prec[token]):
                postfixList.append(opStack.pop())
            opStack.push(token)
    
    while not opStack.isEmpty():
        postfixList.append(opStack.pop())
    return " ".join(postfixList)

# print(infixToPostfix("( A + B ) * C "))
# print(infixToPostfix("( A + B ) * C - ( D - E ) * ( F + G )"))
# print(infixToPostfix("( A + B ) * ( C + D )"))
print(infixToPostfix('5 * 3 ** ( 4 - 2 )'))

# Precidence of equation, postfix calculation given after infixToPostfix output
def postfixEval(postfixExpr):
    operandstack = Stack()

    tokenlist = postfixExpr.split()

    for token in tokenlist:
        if token in '01234567891011121314151617181920':
            operandstack.push(int(token))
        else:
            operand2 = operandstack.pop()
            operand1 = operandstack.pop()
            result = doMath(operand1, operand2, token)
            operandstack.push(result)
    return operandstack.pop()

def doMath(operand1, operand2, operator):
    if operator == '*':
        return operand1 * operand2
    elif operator == '/':
        return operand1 / operand2
    elif operator == '+':
        return operand1 + operand2
    else:
        return operand1 - operand2

# print(postfixEval('7 8 + 3 2 + /'))
# print(infixToPostfix('6 + ( 2 * ( 5 - 8 ) ) / 2'))
# print(postfixEval('6 2 5 8 - * 2 / +'))
# print(postfixEval('17 10 + 3 * 9 /'))