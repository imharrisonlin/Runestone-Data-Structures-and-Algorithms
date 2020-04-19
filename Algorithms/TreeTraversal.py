from TreeDS import BinaryTree

# Preorder tree traversal: visit node, left subtree preorder traversal, 
# followed by right subtree preorder traversal
def preorder(tree):
    if tree:
        print(tree.getRootVal())
        preorder(tree.getLeftChild())
        preorder(tree.getRightChild())
#############preorder as a internal tree method
# def preorder(self):
#     print(self.key)
#     if self.leftChild():
#         self.leftChild.preorder()
#     if self.rightChild():
#         self.rightChild.preorder()



# Postorder tree traversal: left subtree postorder traversal, 
# followed by right subtree postorder traversal, visit node
def postorder(tree):
    if tree != None:
        postorder(tree.getLeftChild())
        postorder(tree.getRightChild())
        print(tree.getRootVal)
############example: the evaluation function of a parse tree
def postorderEval(tree):
    opers = {'+':operator.add, '-':operator.sub, '*':operator.mul, '/':operator.truediv}
    res1 = None
    res2 = None
    if tree:
        res1 = postorder(tree.getLeftChild())
        res2 = postorder(tree.getRightChild())
        if res1 and res2:
            return opers[tree.getRootVal()](res1, res2)
        else:
            return tree.getRootVal()



# Inorder tree traversal: left subtree inorder traversal, visit node
# followed by right subtree inorder traversal
def inorder(tree):
  if tree != None:
      inorder(tree.getLeftChild())
      print(tree.getRootVal())
      inorder(tree.getRightChild())
#############example: return original expression from parse tree
def printexp(tree):
    sVal = ""
    if tree:
        sVal = '(' + printexp(tree.getLeftChild())
        sVal = sVal + str(tree.getRootVal())
        sVal = sVal + printexp(tree.getRightChild())+')'
    return sVal

