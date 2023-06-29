from collections import defaultdict

def solution(a, m, k):
    dictNums = defaultdict(lambda: -1)
    pairEqSumk = [-1,-1]
    currRange = [0, m-1]
    countRanges = 0
    
    for i in range(0, len(a)):
        if i >= m:
            if pairEqSumk[0] >= currRange[0]:
                countRanges += 1
            currRange = [i-m+1, i]
        if dictNums[k - a[i]] != -1:
            # Actual Bug: dictNums[k - a[i]] >= currentRange[0] =>
            # Fix: dictNums[k - a[i]] >= pairEqSumk[0] => 
            if pairEqSumk[0] < dictNums[k-a[i]]:
                pairEqSumk = [dictNums[k-a[i]], i]
        dictNums[a[i]] = i 
    if pairEqSumk[0] >= currRange[0]:
        countRanges += 1
    return countRanges