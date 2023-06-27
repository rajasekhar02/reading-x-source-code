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
    return greedy(arr,k)

# def combinations(n,k):
#     res = 1
#     for i in range(n-k+1,n):
#         res *= i
#     for i in range(2, k):
#         res /= i
#     return res

def combinations(n,k):
    res = 1
    for i in range(1, k):
        res *= (n-k+i) / i
    return int(res + 0.01)
    

def greedy(arr,k):
    size = len(arr)
    bitCount = []
    for i in range(0,32):
        bitCount.append([0,[]])
    for i in range(0,size):
        strList = list(format(arr[i],"b").rjust(32,"0"))
        for j in range(0,len(strList)):
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

print(maximalANDSubsequences([6,46,7,36,25,17,23,12,50,47],2))
"""
5
10 5
43,17,37,24,47,10,38,14,5,44 
10 5
49,8,41,35,0,16,30,2,9,0 
10 3
35,44,43,24,0,34,1,27,2,19 
10 2
6,46,7,36,25,17,23,12,50,47 
10 4
3,13,20,36,9,38,18,14,6,13 


6,3,7,0
"""