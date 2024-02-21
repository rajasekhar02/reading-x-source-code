arr = [11, 81, 94, 43, 3]
from typing import List
from collections import deque

# def getMinForPowerOf2(arr):
#     lenArr = len(arr)
#     max2Power = 0
#     powers2 = []
#     noOfElementsForPower2 = []
#     for i in range(0, 64):
#         power2 = 1 << i
#         if (power2) > lenArr:
#             max2Power = 1 << (i - 1)
#             break
#         elif (power2) == lenArr:
#             powers2.append(power2)
#             noOfElementsForPower2.append(lenArr - power2 + 1)
#             max2Power = 1 << (i)
#             break
#         powers2.append(power2)
#         noOfElementsForPower2.append(lenArr - power2 + 1)
#     minForPowerOf2 = [*arr]
#     print(powers2, max2Power, noOfElementsForPower2, minForPowerOf2)
#     for i in range(1, len(powers2)):
#         offset = len(minForPowerOf2) - noOfElementsForPower2[i - 1]
#         for j in range(0, noOfElementsForPower2[i]):
#             minForPowerOf2.append(
#                 min(
#                     minForPowerOf2[offset + j],
#                     minForPowerOf2[offset + powers2[i - 1] + j],
#                 )
#             )
#     print(minForPowerOf2)
#     return minForPowerOf2


# if __name__ == "__main__":
#     minForPowerOf2 = getMinForPowerOf2(arr)
#     sumEs = 0
#     for i in minForPowerOf2:
#         sumEs += i
#         sumEs %= 1e9 + 7


class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        print(arr)
        # min element from left of the arr
        stackOfMinEleIndex = deque()
        left = [0] * len(arr)
        for i in range(0, len(arr)):
            while stackOfMinEleIndex and arr[stackOfMinEleIndex[-1]] >= arr[i]:
                stackOfMinEleIndex.pop()
            if stackOfMinEleIndex:
                left[i] = i - stackOfMinEleIndex[-1]
            else:
                left[i] = i + 1
            stackOfMinEleIndex.append(i)
        print(left)
        right = [0] * len(arr)
        stackOfMinEleIndex = deque()
        for i in range(len(arr) - 1, -1, -1):
            while stackOfMinEleIndex and arr[stackOfMinEleIndex[-1]] >= arr[i]:
                stackOfMinEleIndex.pop()
            if stackOfMinEleIndex:
                right[i] = stackOfMinEleIndex[-1] - i
            else:
                right[i] = len(arr) - i
            stackOfMinEleIndex.append(i)
        print(right)
        sumAll = 0
        for i in range(0, len(arr)):
            sumAll = (sumAll + (arr[i] * left[i] * right[i])) % (1000000007)
        return sumAll


print(Solution().sumSubarrayMins(arr))
