"""
For a = [10, 2], the output should be solution(a) = 1344.

a[0] ∘ a[0] = 10 ∘ 10 = 1010,
a[0] ∘ a[1] = 10 ∘ 2 = 102,
a[1] ∘ a[0] = 2 ∘ 10 = 210,
a[1] ∘ a[1] = 2 ∘ 2 = 22.
So the sum is equal to 1010 + 102 + 210 + 22 = 1344.
"""


def solution(a):
    sumAllElements = 0
    sumPows10 = 0
    a = sorted(a)
    for i in range(0, len(a)):
        sumAllElements += a[i]
        sumPows10 += getNearestPow10(a[i])
    total = 0
    for i in range(0, len(a)):
        total += a[i] * sumPows10 + sumAllElements
    return total


def getNearestPow10(num):
    pow10s = [10, 100, 1000, 10000, 100000, 1000000, 10000000]
    low = 0
    high = len(pow10s) - 1
    ans = len(pow10s)
    while low <= high:
        mid = low + (high - low) // 2
        if pow10s[mid] > num:
            high = mid - 1
            ans = mid
        else:
            low = mid + 1
    if ans == len(pow10s):
        return 1e10
    return pow10s[ans]
