from collections import defaultdict
def solution(a, k):
    if len(a) == 1: return 0
    a = sorted(a)
    dictOfRemainders = defaultdict(int)
    ans = 0
    dictOfRemainders[k] = 0
    for i in range(0,len(a)):
        rem = (a[i]%k)
        if a[i] == k and a[i-1] == a[i]: 
            dictOfRemainders[rem] += 1
            continue
        otherNum =  k-rem
        if dictOfRemainders[otherNum] > 0:
            ans+=dictOfRemainders[otherNum]
    # Stuggle to find which values to store in the dictionary
    # But finally figured out that I need to save the count of remainders
    # KEY STEP 1
        dictOfRemainders[rem] += 1
    # KEY STEP 2
    # counting combinations of numbers such that both the numbers are divible by k
    ans += ((dictOfRemainders[0]) * (dictOfRemainders[0]-1)) >> 1
    return ans
            