# Bubble sort: 
# sequential comparison of adjacent items
# regardless of item arrangement: reqire n-1 passes
# sum of first n integers is n(n+1)/2
# Best case: already ordered-> no exchange O(n)
# Worst case: every comparison will cause an exchange
#             avg exchange half of the time
#             O(n^2)
def bubbleSort(numlist):
    for passnum in range(len(numlist)-1, 0, -1):
        for i in range(passnum):
            if numlist[i] > numlist[i+1]:
                # python implementation
                # numlist[i], numlist[i+1] = numlist[i+1], numlist[i]
                temp = numlist[i]
                numlist[i] = numlist[i+1]
                numlist[i+1] = temp

# Short bubble sort:
# Passing through the entire list allows bubble sort
# to determine if the list is sorted and stop
def shortBubbleSort(numlist):
    # implement exchange variable to determine whether
    exchange = True
    passnum = len(numlist)-1
    while passnum > 0 and exchange:
        exchange = False
        for i in range(passnum):
            if numlist[i] > numlist[i+1]:
                exchange = True
                temp = numlist[i]
                numlist[i] = numlist[i+1]
                numlist[i+1] = temp
        passnum = passnum - 1


