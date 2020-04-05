# Merge Sort: Divide and conquer
# Recursive algorithm, continuously splits a list in half
# Base case: If list is empty or has 1 item, it is sorted
# 
# If the list has more than one item invoke a merge sort on both halves
# once the two halves are sorted, call a merge
# Splitting: the list by calling mergeSort is similarto binary search
# T: O(logn)
# Merging: list of size n requires n operations to merge the items back to the list
# T: O(n)
# Thus, MergeSort requies
# T: O(nlogn)
# **** Merge sort uses extra space to hold the two halves of the list, can be a problem for large data sets

def mergeSort(nlist):
    print('splitting...', nlist)
    if len(nlist) > 1:
        mid = len(nlist) // 2
        lefthalf = nlist[:mid]
        righthalf = nlist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i = 0
        j = 0
        k = 0
        
        while i < len(lefthalf) and j < len(righthalf):
            # This if condition ensures a "stable algorithm" by
            # maintaining the order of the duplicate items in a list
            if lefthalf[i] <= righthalf[j]:
                nlist[k] = lefthalf[i]
                i = i+1
            else:
                nlist[k] = righthalf[j]
                j = j+1
            k = k+1
            print("i:{} j:{} k:{}".format(i,j,k))

        while i < len(lefthalf):
            nlist[k] = lefthalf[i]
            i = i+1
            k = k+1
            print("i:{} j:{} k:{}".format(i,j,k))

        while j < len(righthalf):
            nlist[k] = righthalf[j]
            j = j+1
            k = k+1
            print("i:{} j:{} k:{}".format(i,j,k))
    print("Merging", nlist)

alist = [54,26,93,17,77,31,44,55,20]
mergeSort(alist)
print(alist)
