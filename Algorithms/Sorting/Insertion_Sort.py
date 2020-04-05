# Insertion sort: 
# Always maintains a sorted sublist with one item larger
# Each new item is "inserted" into the correct sublist position
# Best case: only one comparison needed without going in the while loop
#            O(n)
# Worst case: O(n^2)
def insertionSort(numlist):
    for index in range(1, len(numlist)):
        currentVal = numlist[index]
        position = index
        
        # keeps track of current value until current value
        # is greater than the value at position, then exit while and insert
        while position > 0 and numlist[position-1] > currentVal:
            numlist[position] = numlist[position-1]
            position = position - 1
        
        numlist[position] = currentVal

alist = [54,26,93,17,77,31,44,55,20]
insertionSort(alist)
print(alist)