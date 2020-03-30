from BasicDS import Deque

# Palindrome problem, palindrome ex: ogopogo, toot
def pal_checker(text):
    charDeque = Deque()

    for ch in text:
        charDeque.addRear(ch)
    
    stillEqual = True

    while charDeque.size() > 1 and stillEqual:
        first = charDeque.removeFront()
        last = charDeque.removeRear()
        if first != last:
            stillEqual = False
    
    return stillEqual
    
print(pal_checker("abcdefgfedcba"))
print(pal_checker('ogopogo'))
print(pal_checker('amanda'))