# Linear data structures class implementation

# Stack with end of the list as the top stack
class Stack:
    """
    Stack linear data structure

    Instance variables:
        None
    """

    def __init__(self):
            self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        return self.items.append(item)
    
    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

# Stack with beginning of the list as the top stack
# The pop(0) and insert operator are O(n) this is a lot slower
# compared to the Stack ADT where pop() and append() are O(1)
class Stack_front:
    """
    Stack linear data structure

    Instance variables:
        None
    """

    def __init__(self):
            self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        return self.items.insert(0,item)
    
    def pop(self):
        return self.items.pop(0)

    def peek(self):
        return self.items[0]

    def size(self):
        return len(self.items)


# Queue data structure with rear at index 0 and front at end of list
class Queue:
    """
    Queue linear data structure

    Instance variables:
        None
    """

    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)
    
    def enqueue(self, item):
        self.items.insert(0, item)
    
    def dequeue(self):
        return self.items.pop()


# Deque: double eneded queue
# items can be queued from the rear or the front end
# existing items can be removed from either end
# Provides the capabilities of stacks and queues in a single DS
# ****Does ot require the LIFO or FIFO ordering****
class Deque():
    """
    Queue linear data structure

    Instance variables:
        None
    """

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []
    
    def size(self):
        return len(self.items)
    
    def addFront(self, item):
        self.items.append(item)
    
    def addRear(self, item):
        self.items.insert(0,item)

    def removeFront(self):
        return self.items.pop()
    
    def removeRear(self):
        return self.items.pop(0)


# Unordered list: linked list
# location of the first item must be explicitly specified.
# First item: Head, Last item has no next item
# *** Node class, subunit of linked list. All the nodes are liked from head to tail
class Node:
    """
    Abstract data type
    
    Instance variable:
        initdata: initialize with data in the node
    """

    def __init__(self, initdata):
        self.data = initdata
        self.next = None
    
    def getData(self):
        return self.data
    
    def getNext(self):
        return self.next
    
    def setData(self, newData):
        self.data = newData
    
    def setNext(self, newNext):
        self.next = newNext

class UnorderedList:
    """
    Unordered linear data structure

    Instance variable:
        None
    """

    # When creating a linked list, the head refers to None
    def __init__(self):
        self.head = None

    def show(self):
        current = self.head
        items = []
        while current != None:
            items.append(current.getData())
            current = current.getNext()
        return items

    def isEmpty(self):
        return self.head == None

    def add(self,item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    # size, search and remove: based on linked list traversal
    def size(self):
        current = self.head
        count = 0

        while current != None:
            count += 1
            current = current.getNext()
        
        return count
    
    def search(self,item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
        
        return found

    def remove(self,item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()
        
        if previous == None:
            self.head  = current.getNext()
        else:
            previous.setNext(current.getNext())

    # Currently O(n) by tracking the tail of linked list,
    # append operator can be O(1)
    def append(self,item):
        current = self.head
        if current:
            while current.getNext() != None:
                current = current.getNext()
            current.setNext(Node(item))
        else:
            self.head = Node(item)

    def insert(self,item,pos):
        current = self.head
        temp = Node(item)
        count = 0

        while current != None and count < pos:
            current = current.getNext()
            count += 1
        if current is None:
            print('Index out of bounds')
        else:
            temp.setNext(current.getNext())
            current.setNext(temp)

    def index(self,item):
        current = self.head
        pos = 0
        found = False
        while current != None and not found:
            if current.getData() == item:
                return pos
            else:
                current = current.getNext()
                pos += 1
    
    def pop(self,pos):
        current = self.head
        previous = None
        count = 0
        
        while current.getNext() != None and count < pos:
            previous = current
            current = current.getNext()
            count += 1
        if previous == None:
            self.head = current.getNext()
            item = current.getData()
        else:
            previous.setNext(current.getNext())
            item = current.getData()
        return item
        
# LLst = UnorderedList()
# LLst.add(123)
# LLst.add('hi')
# LLst.append('end')
# print(LLst.show())
# print(LLst.size())
# LLst.insert('inserted to 2', 2)
# print(LLst.show())
# print(LLst.size())
# print(LLst.index('inserted to 2'))
# print(LLst.pop(0))


# Ordered list: linked list
# location of the first item must be explicitly specified.
# First item: Head, Last item has no next item
# Order of the list is desc or ascend

class OrderedList:
    """
    OrderedList, linked list

    Instance variable:
        None
    """

    def __init__(self):
        self.head = None

    def show(self):
        current = self.head
        items = []
        while current != None:
            items.append(current.getData())
            current = current.getNext()
        return items

    def isEmpty(self):
        return self.head == None

    # size, search and remove: based on linked list traversal
    def size(self):
        current = self.head
        count = 0

        while current != None:
            count += 1
            current = current.getNext()
        
        return count

    def remove(self,item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()
        
        if previous == None:
            self.head  = current.getNext()
        else:
            previous.setNext(current.getNext())

    # since the ordering of the linked list is known
    # it is possible to stop before the end of the linked list
    # ex. [1, 3, 5, 7, 9], if the value we want is 4 we can stop the search
    #     once we past 3 and see 5
    def search(self, item):
        current = self.head
        found = False
        stop = False
        while current != None and not found and not stop:
            if current.getData() == item:
                found = True
            else:
                if current.getData() > item:
                    stop = True
                else:
                    current = current.getNext()
        
        return found
    
    def add(self, item):
        current = self.head
        previous = None
        stop = False
        while current !=None and not stop:
            # If first item in the list is greaters the the item
            if current.getData() > item:
                stop = True
            else:
                previous = current
                current = current.getNext()
        
        temp = Node(item)
        if previous == None:
            temp.setNext(self.head)
            self.head = temp
        else:
            temp.setNext(current)
            previous.setNext(temp)
            