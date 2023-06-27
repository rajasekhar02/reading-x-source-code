def maximalANDSubsequences(arr, k):
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

print(maximalAndSubsequences([3,13,20,36,9,38,18,14,6,13],4))
