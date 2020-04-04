# Selection sort: improved bubble sort
# After one pass, selects the largest value in the list 
# Places it at the final position
# O(n^2) 
def selectionSort(numlist):
    for fillpos in range(len(numlist)-1, 0 , -1):
        posOfMax = 0
        for position in range(1, fillpos+1):
            if numlist[position] > numlist[posOfMax]:
                posOfMax = position
        
        temp = numlist[posOfMax]
        numlist[posOfMax] = numlist[fillpos]
        numlist[fillpos] = temp

alist = [54,26,93,17,77,31,44,55,20]
selectionSort(alist)
print(alist)