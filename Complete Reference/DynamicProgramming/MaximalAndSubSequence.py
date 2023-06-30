import math
def maximalANDSubsequencesBF(arr, k):
    # write your code here
    return recurse(arr,0,k, (1<<63)-1)

def recurse(arr, start, k, compVal):
    size = len(arr)
    if k==0:
        return compVal, 1
    maxVal = -1
    maxCount = 0
    for i in range(start, (size-k+1)):
        val, count = recurse(arr, i+1, k-1, compVal&arr[i])
        if val > maxVal:
            maxVal = val
            maxCount = count
        elif val == maxVal:
            maxCount += count
    return maxVal, maxCount


def maximalANDSubsequences(arr, k):
    # write your code here
    return greedy2(arr,k)

"""
Accepted Solution
Time Complexity:  32 * N
Space Complexity: N
"""
def greedy2(arr,k):
    size = len(arr)
    temp = arr
    for j in range(32,0,-1):
        temp2 = []        
        for i in range(0,len(temp)):
            if temp[i] & (1<<j):
                temp2.append(temp[i])
        if len(temp2) >= k:
            temp = temp2
    maxVal = temp[0]
    for i in range(1, len(temp)):
        maxVal &= temp[i]
    maxValSets = temp
    noOfSubsequences = math.comb(len(maxValSets), k)
    if noOfSubsequences == 0:
        return maxVal, 1
    return maxVal, math.comb(len(maxValSets), k)


def combinations(n,k):
    res = 1
    for i in range(1, k):
        res *= (n-k+i) / i
    return int(res + 0.01)
    
"""
Time Complexity:  32*2* N
Space Complexity: N * N
"""
def greedy(arr,k):
    size = len(arr)
    bitCount = []
    for i in range(0,32):
        bitCount.append([0,[]])
    for i in range(0,size):
        strList = list(format(arr[i],"b").rjust(32,"0")) # O(32)
        for j in range(0,len(strList)): # O(32)
            bitCount[j][0] += int(strList[j])
            if int(strList[j]) == 1:
                bitCount[j][1].append(f'{arr[i]}_{i}')
    maxVal = -1
    maxValSets = set()
    for i in range(0, 32):
        if bitCount[i][0] < k:
            continue
        if maxVal == -1:
            maxVal = 1 << (32-i-1)
            maxValSets = set(bitCount[i][1])
        else:
            tempSet = maxValSets
            tempSet2 = bitCount[i][1]
            tempSet3 = tempSet.intersection(tempSet2)
            if len(tempSet3) >= k:
                maxVal |= 1<<(32-i-1)
                maxValSets = tempSet3 
    if maxVal == -1:
        return 0, math.comb(len(arr),k)
    noOfSubsequences = math.comb(len(maxValSets), k)
    if noOfSubsequences == 0:
        return maxVal, 1
    return maxVal, math.comb(len(maxValSets), k)


print(maximalANDSubsequences([3,13,20,36,9,38,18,14,6,13],4))
"""
5
10 5
43,17,37,24,47,10,38,14,5,44 o/p: 32,1
10 5
49,8,41,35,0,16,30,2,9,0  o/p: 0, 252
10 3
35,44,43,24,0,34,1,27,2,19 o/p: 34, 1
10 2
6,46,7,36,25,17,23,12,50,47 o/p: 46, 1
10 4
3,13,20,36,9,38,18,14,6,13 o/p: 8, 1
4 4
6,3,7,0 o/p: 0, 1
"""