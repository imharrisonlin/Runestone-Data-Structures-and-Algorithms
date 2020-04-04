#########Exploring a maze###########
# Input variables:
#   maze is representation of the map using a list of lists
#   startRow, startColumn are the coordinates for the start position in the map

def searchFrom(maze, startRow, startColumn):
    maze.updatePosition(startRow, startColumn)
   #  Check for base cases:
   #  1. We have run into an obstacle, return false
    if maze[startRow][startColumn] == OBSTACLE:
        return False
    #  2. We have found a square that has already been explored
    if maze[startRow][startColumn] == TRIED:
        return False
    # 3. Success, an outside edge not occupied by an obstacle
    if maze.isExit(startRow,startColumn):
        maze.updatePosition(startRow, startColumn, PART_OF_PATH)
        return True
    maze.updatePosition(startRow, startColumn, TRIED)

    # Otherwise, use logical short circuiting to try each
    # direction in turn (if needed)
    found = searchFrom(maze, startRow-1, startColumn) or \
            searchFrom(maze, startRow+1, startColumn) or \
            searchFrom(maze, startRow, startColumn-1) or \
            searchFrom(maze, startRow, startColumn+1)
    if found:
        maze.updatePosition(startRow, startColumn, PART_OF_PATH)
    else:
        maze.updatePosition(startRow, startColumn, DEAD_END)
    return found


#########Dynamic Programming#########

####Minimum Coins (not dynamic only recursive)#########
# Base case is when the change is an exact amount of one of our coins
# If not, recursive call while adding one coin,
# and reducing the change amount by the value of the coin selected
def MinCoin(coinValueList, change):
    minCoins = change
    # Base case when change equals a coin value
    if change in coinValueList:
        return 1
    else:
        # Select the coins which are less than the change amount
        for i in [c for c in coinValueList if c <= change]:
            # Recursive call to find the min number of coins
            numCoins = 1 + MinCoin(coinValueList, change-i)
            if numCoins < minCoins:
                minCoins = numCoins
    return minCoins

# print(MinCoin([1, 5, 10, 25], 63))

####Minimum Coins Revised (Caching or memoization)#########
# Known results for the number of coins for a change amount
# is saved after the recursive call.
# No repetitive recursion calls on the same change value 
# Added parameter knownResults to save the results

# ** This method is known as memoization or caching
def revMinCoin(coinValueList, change, knownResults):
    minCoins = change
    # Base case when change equals a coin value
    if change in coinValueList:
        knownResults[change] = 1
        return 1
    elif knownResults[change] > 0:
        return knownResults[change]
    else:
        # Select the coins which are less than the change amount
        for i in [c for c in coinValueList if c <= change]:
            # Recursive call to find the min number of coins
            numCoins = 1 + revMinCoin(coinValueList, change-i, knownResults)
            
            # If the numCoins is less than the minCoins after a recursive call
            # make the minCoins equal to that nodes answer
            # and save the 
            if numCoins < minCoins:
                minCoins = numCoins
                knownResults[change] = minCoins
    return minCoins

# print(revMinCoin([1, 5, 10, 25], 63, [0]*64 ))


####Minimum Coins Dynamic Programming#############
# Dynamic programming solution considers using all possible coins
# to make change for the amount specified by cents
# then takes the minimum amount and stores the result in the minCoins list
def dpMakeChange(coinValueList, change, minCoins):
    for cents in range(change+1):
        coinCount = cents
        for j in [c for c in coinValueList if c <= cents]:
            if minCoins[cents-j] + 1 < coinCount:
                coinCount = minCoins[cents-j] + 1
        minCoins[cents] = coinCount
    return minCoins[change]

# print(dpMakeChange([1, 5, 10, 25], 63, [0]*64 ))

# ****** Show which coins were used********
# We can track the coin used by modifying the dpMakeChange algorithm
# and including a printCoins function that walks backward through
# the table to print the value of each coin used
def dpMakeChange(coinValueList, change, minCoins, coinsUsed):
    for cents in range(change+1):
        coinCount = cents
        newCoin = 1
        for j in [c for c in coinValueList if c <= cents]:
            if minCoins[cents-j] + 1 < coinCount:
                coinCount = minCoins[cents-j] + 1
                newCoin = j
        minCoins[cents] = coinCount
        coinsUsed[cents] = newCoin
    return minCoins[change]

def printCoins(coinsUsed, change):
    coin = change
    while coin > 0:
        thisCoin = coinsUsed[coin]
        print(thisCoin)
        coin = coin - thisCoin

def main():
    amnt = 33
    clist = [1, 5, 8, 10, 25]
    coinsUsed = [0]*64
    coinCount = [0]*64

    print("making change for", amnt, "requires")
    print(dpMakeChange(clist,amnt,coinCount,coinsUsed), "coins")
    print("They are:")
    printCoins(coinsUsed,amnt)
    print("The used list is as follows:")
    print(coinsUsed)

# main()


#######Art thief problem########
'''
Suppose you are a computer scientist/art thief who has broken into a major art gallery. 
All you have with you to haul out your stolen art is your knapsack which only holds W pounds of art, but for every piece of art you know its value and its weight. 
Write a dynamic programming function to help you maximize your profit.
Here is a sample problem for you to use to get started: Suppose your knapsack can hold a total weight of 20. 
You have 5 items as follows:
item     weight      value
  1        2           3
  2        3           4
  3        4           8
  4        5           8
  5        9          10 '''
    
class ArtItem:
    def __init__(self, id, weight, value):
        self.id = id
        self.weight = weight
        self.value = value

def dpMaxValue(itemlist, maxweight, valuelist, weightUsed):
    for pound in range(maxweight+1):
        profit = 0
        useditem = None
        for item in [i for i in itemlist if i.weight <= pound]:
            if valuelist[pound - item.weight] + item.value > profit:
                profit = valuelist[pound-item.weight] + item.value
                useditem = item
        
        valuelist[pound] = profit
        weightUsed[pound] = useditem

    return valuelist[maxweight]

def printweights(weightUsed, maxweight):
    pound = maxweight
    while pound > 0:
        itemWeight = weightUsed[pound].weight
        print(itemWeight)
        pound = pound - itemWeight

def main():
    maxweight = 20
    itemlist = [ArtItem(1,2,3), ArtItem(2,3,4), ArtItem(3,4,8), ArtItem(4,5,8), ArtItem(5,9,10)]
    valuelist = [0] * (maxweight + 1)
    weightUsed = [0] * (maxweight + 1)

    print("Maximum profit for {} pounds is:".format(maxweight))
    print(dpMaxValue(itemlist, maxweight,valuelist, weightUsed))
    print("The weights used for obtaining the max profit are:")
    printweights(weightUsed,maxweight)

# main()

def editDistance(str1, str2, m, n, copy, indel):
    # initiaize the matrix table to store results of subproblems
    dp = [ [0 for i in range(m + 1)] for j in range(n + 1)]
    
    # Fill dp[][] in bottom up manner
    for i in range(n + 1):
        for j in range(m + 1):

            # Base case for first string is empty,
            # insert all of the characters to match second string
            if i == 0:
                dp[i][j] = j

            # Base case for second string is empty,
            # delete all of the character from first string
            elif j == 0:
                dp[i][j] = i
            
            # if last characters are the same then ignore the last char
            # and recur for remaining string
            elif str1[j-1] == str2[i-1]:
                dp[i][j] = dp[i-1][j-1]

            # if last characters are different then find the minimum
            # cost from all the operations possible
            else:
                dp[i][j] = 1 + min(dp[i][j-1],   # insert affects row
                                   dp[i-1][j],   # delete affects column
                                   dp[i-1][j-1]) # replace points to the previous subproblem
        
    return dp

def main():
    str1 = 'apple'
    str2 = 'apartss'
    copy = 1
    indel = 1
    dpTable = editDistance(str1, str2, len(str1), len(str2), copy, indel)

    for row in dpTable:
        print(row)
main()
