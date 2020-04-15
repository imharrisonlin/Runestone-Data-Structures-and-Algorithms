# Tree representation: Nodes and References
class BinaryTree:
    """
    Abstract data structure Binary Tree

    Instance variables:
        node ("key")
        leftChild
        rightChild
    """
    
    def __init__(self, rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self, newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t
            
    def insertRight(self, newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t

    def getRootVal(self):
        return self.key
    
    def setRootVal(self, obj):
        self.key = obj

    def getLeftChild(self):
        return self.leftChild

    def getRightChild(self):
        return self.rightChild


#############################################################################
# Tree representation: List of Lists
def listoflistTree():
    def BinaryTreeList(r):
        return [r, [], []]

    # Add a subtree to the left of the root node
    def insertLeft(root,newBranch):
        t = root.pop(1)
        if len(t) > 0:
            root.insert(1, [newBranch, t, []])
        else:
            root.insert(1, [newBranch, [], []])
        return root

    # Add a subtree to the left of the root node
    def insertRight(root,newBranch):
        t = root.pop(2)
        if len(t) > 0:
            root.insert(2, [newBranch, [], t])
        else:
            root.insert(2, [newBranch, [], []])
        return root

    # Access funtions for setting the root and getting the root and left/right child
    def getRootVal(root):
        return root[0]

    def setRootVal(root, newVal):
        root[0] = newVal

    def getLeftChild(root):
        return root[1]

    def getRightChild(root):
        return root[2]





