import timeit
# Sequential search
#   Best Case, Worst Case, Avg Case
# T:    O(1)      O(n)        n/2
def sequentialSearch(numslist, n):
    pos = 0
    found = False

    while not found:
        if numslist[pos] == n:
            found = True
        # this effectively changes the time complexity
        # for the best case of the ordered list to O(1)
        elif numslist[pos] > n:
            break
        else:
            pos = pos + 1
    
    return found

# def main():
    # numslist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
    # n = 9    
    # print(sequentialSearch(numslist, n))


# Binary search
#   Best Case, Worst Case, Avg Case
# T:    O(1)      O(n)        n/2
def binarySearch(numslist, n):
    first = 0
    last = len(numslist)-1
    found = False

    while first <= last and not found:
        midpoint = (first + last)//2
        if numslist[midpoint] == n:
            found = True
        else:
            if n < numslist[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1
    return found

# Recursive call for binary search
def rebinarySearch(numslist, n):
    # Base case
    if len(numslist) == 0:
        return False
    else:
        midpoint = len(numslist)//2
        if numslist[midpoint] == n:
            return True
        else:
            if n < numslist[midpoint]:
                return rebinarySearch(numslist[:midpoint], n)
            else:
                return rebinarySearch(numslist[midpoint+1:], n)
            

# def main():
#     testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
#     print(binarySearch(testlist, 3))
#     print(binarySearch(testlist, 13))
    
#     print(rebinarySearch(testlist, 3))
#     print(rebinarySearch(testlist, 13))


# Hashing Search
# T: O(1) for searching
#***************************************
# Hashing a string using Ordinal values
import unittest
def strhash(astring, tablesize):
    sum = 0
    for c in astring:
        sum = sum + ord(c)
    return sum % tablesize

# def main():
#     print(strhash('cat', 11), 4)

# Unittest for the funtion output
# class MyTest(unittest.TestCase):
#     def test(self):
#         self.assertEqual(strhash('cat',11), 4)
# unittest.main()

def linearProbHash(numlist, hashtable):
    tablesize = len(hashtable)
    for num in numlist:
        hashval = num % 11
        if hashtable[hashval] == None:
            hashtable[hashval] = num
        else:
            newslot = rehash(hashval, hashtable)
            hashtable[newslot] = num
    return hashtable[:-1]

def rehash(oldhash, hashtable):
    newhashval = (oldhash + 1) % 11
    while hashtable[newhashval] != None:
        newhashval = (newhashval + 1) % 11
    return newhashval

def main():
    tablesize = 11
    hashtable = [None for s in range(tablesize+1)]
    numlist = [113 , 117 , 97 , 100 , 114 , 108 , 116 , 105 , 99]

    print('normal table:')
    print(hashtable)
    print('after hashing')
    print(linearProbHash(numlist, hashtable))

main()