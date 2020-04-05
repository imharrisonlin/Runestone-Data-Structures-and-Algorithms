# Shell sort: diminishing incement sort
# Improves on the insertion sort
# Breaks the list into number of smaller sublists
# *Uses an increment (gap) to create a sublist
# and sort the sublist to conduct shell sort
# Finally, the single list is sorted with insertion sort
# O(n^2) but by changing the increment, using 2^k -1, O(n^(3/2) can be performed)
def shellSort(numlist):
    sublistGap = len(numlist)//2
    while sublistGap > 0:
        for startpos in range(sublistGap):
            gapInsertionSort(numlist, startpos, sublistGap)
        
        print("After increments of size", sublistGap,
                "The list is", numlist)
        
        sublistGap = sublistGap // 2

def gapInsertionSort(numlist, start, gap):
    for i in range(start + gap, len(numlist), gap):
        currentVal = numlist[i]
        position = i

        while position >= gap and numlist[position-gap] > currentVal:
            numlist[position] = numlist[position-gap]
            position = position - gap
        
        numlist[position] = currentVal

alist = [54,26,93,17,77,31,44,55,20]
shellSort(alist)
print(alist)