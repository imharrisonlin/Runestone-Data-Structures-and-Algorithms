# Parse tree for mathamatical expression:
#   1. How to build a parse tree from a fully parenthesized mathematical expression.
#   2. How to evaluate the expression stored in a parse tree.
#   3. How to recover the original mathematical expression from a parse tree.

# Part 1 build a parse tree
from BasicDS import Stack
from TreesDS import BinaryTree


def buildParseTree(pexp):
    plist = pexp.split()
    pStack = Stack()
    eTree = BinaryTree('')
    pStack.push(eTree)
    currentTree = eTree

    for i in plist:
        if i == '(':
            currentTree.insertLeft('')
            pStack.push(currentTree)
            currentTree = currentTree.getLeftChild()
        elif i in ['+', '-', '*', '/']:
            currentTree.setRootVal(i)
            currentTree.insertRight('')
            pStack.push(currentTree)
            currentTree = currentTree.getRightChild()
        elif i == ')':
            currentTree = pStack.pop()
        elif i not in ['+', '-', '*', '/', ')']:
            try:
                currentTree.setRootVal(int(i))
                parent = pStack.pop()
                currentTree = parent
            except ValueError:
                raise ValueError("token ' {} ' is not a valid integer".format(i))

    return eTree

# Part 2 evaluate the parse tree with recursion
import operator
def evaluate(parseTree):
    opers = {'+':operator.add, '-':operator.sub, '*':operator.mul, '/':operator.truediv}

    leftC = parseTree.getLeftChild()
    rightC = parseTree.getRightChild()

    if leftC and rightC:
        fn = opers[parseTree.getRootVal()]
        return fn(evaluate(leftC),evaluate(rightC))
    else:
        return parseTree.getRootVal()

pt = buildParseTree("( 3 + ( 4 * 5 ) )")
print(evaluate(pt))