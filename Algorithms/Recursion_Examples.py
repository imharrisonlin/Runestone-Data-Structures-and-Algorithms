# listSum easy example
def listsum(numList):
    if len(numList) == 1:
        return numList[0]
    else:
        return numList[0] + listsum(numList[1:])

# write a function that takes a string as a parameter and returns
# a new string that is the reverse of the old string
def reverse(s):
    if s == "":
        return s
    else:
        return reverse(s[1:]) + s[0]
        # return s[-1] + reverse(s[:-1])

# Palindrome checker in recursion
def isPalindrome(word):
    # Base case if len of the word is 0 or 1 it is palindrome
    if len(word) < 2:
        return True
    # compare the first and last char
    if word[0] != word[-1]:
        return False
    # recursive call, remove the first and last char to compare next chars
    return isPalindrome(word[1:-1])

# Convert integer to string of specified base
def toStr(n,base):
    convertStr = '0123456789ABCDEF'
    if n < base:
        return convertStr[n]
    else:
        return toStr(n//base, base) + convertStr[n % base]

# Convert integer to string of specified base
# using a stack
from BasicDS import Stack
rStack = Stack()
def toStr(n,base):
    convertStr = '0123456789ABCDEF'
    while n > 0:    
        if n < base:
            rStack.push(convertStr[n])
        else:
            rStack.push(convertStr[n % base])
        n = n // base
    res = ""
    while not rStack.isEmpty():
        res = res + rStack.pop()
    return res


# Recursion Visualized: Using turtle graphics module
import turtle

# myTurtle = turtle.Turtle()
# myWin = turtle.Screen()

# def drawSpiral(myTurtle, linelen):
#     if linelen > 0:
#         myTurtle.forward(linelen)
#         myTurtle.right(90)
#         drawSpiral(myTurtle, linelen-5)
    
# drawSpiral(myTurtle,150)
# myWin.exitonclick()

# using turtle to draw a tree with recursion
def tree(branchLen,t):
    if branchLen > 5:
        t.forward(branchLen)
        t.right(20)
        tree(branchLen-15,t)
        t.left(40)
        tree(branchLen-15,t)
        t.right(20)
        t.backward(branchLen)

def main():
    t = turtle.Turtle()
    myWin = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color("green")
    tree(70,t)
    myWin.exitonclick()

# Using turtle to draw a Sierpinski Triangle with recursion
def drawTriangle(points,color,myTurtle):
    myTurtle.fillcolor(color)
    myTurtle.up()
    myTurtle.goto(points[0][0],points[0][1])
    myTurtle.down()
    myTurtle.begin_fill()
    myTurtle.goto(points[1][0],points[1][1])
    myTurtle.goto(points[2][0],points[2][1])
    myTurtle.goto(points[0][0],points[0][1])
    myTurtle.end_fill()

def getMid(p1,p2):
    return ( (p1[0]+p2[0]) / 2, (p1[1] + p2[1]) / 2)

def sierpinski(points,degree,myTurtle):
    colormap = ['blue','red','green','white','yellow',
                'violet','orange']
    drawTriangle(points,colormap[degree],myTurtle)
    if degree > 0:
        sierpinski([points[0],
                        getMid(points[0], points[1]),
                        getMid(points[0], points[2])],
                   degree-1, myTurtle)
        sierpinski([points[1],
                        getMid(points[0], points[1]),
                        getMid(points[1], points[2])],
                   degree-1, myTurtle)
        sierpinski([points[2],
                        getMid(points[2], points[1]),
                        getMid(points[0], points[2])],
                   degree-1, myTurtle)

def main():
   myTurtle = turtle.Turtle()
   myWin = turtle.Screen()
   myPoints = [[-100,-50],[0,100],[100,-50]]
   sierpinski(myPoints,3,myTurtle)
   myWin.exitonclick()

