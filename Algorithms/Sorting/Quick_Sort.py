# Quick sort
# Uses devide and conquer similar to merge sort
# while not using additional storage compared to merge sort (creating left and right half of the list)
# It is possible that the list may not be divided in half
# Recursive call on quicksortHelper
# Base case: first < last (if len(list) <= 1 list is sorted)
# 
# The partition function occurs at the middle it will be O(logn) divisions
# Finding the splitpoint requires n items to be checked
# O(nlogn) on average
# Worst case: the split may be skewed to the left or the right
#             resulting in dividing the list into 0 items and n-1 items
#             the overhead of the recursion required
#             O(n^2) time complexity
# ----------------------------------------------------------------------------------------------------------
# Can eleviate the potential of worst case uneven division
# by using different ways of choosing the pivot value (ex. median of three)
# Median of three: consider first, middle, and last element in the list
#                  pick the median value and use it for the pivot value


def quickSort(nlist):
    quickSortHelper(nlist, 0, len(nlist)-1)

def quickSortHelper(nlist, first, last):
    if first < last:
        splitpoint = partition(nlist, first, last)

        quickSortHelper(nlist,first,splitpoint-1)
        quickSortHelper(nlist,splitpoint+1,last)

def partition(nlist,first,last):
    pivotValue = nlist[first]

    leftmark = first+1
    rightmark = last

    done = False
    while not done:

        while leftmark <= rightmark and nlist[leftmark] < pivotValue:
            leftmark = leftmark + 1
        while nlist[rightmark] > pivotValue and rightmark >= leftmark:
            rightmark = rightmark - 1
        
        if rightmark < leftmark:
            done = True
        else:
            temp = nlist[leftmark]
            nlist[leftmark] = nlist[rightmark]
            nlist[rightmark] = temp
    
    temp = nlist[first]
    nlist[first] = nlist[rightmark]
    nlist[rightmark] = temp

    return rightmark

alist = [54,26,93,17,77,31,44,55,20]
quickSort(alist)
print(alist)
print(partition.__doc__)