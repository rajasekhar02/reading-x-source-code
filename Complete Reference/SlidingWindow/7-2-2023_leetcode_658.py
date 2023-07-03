from typing import List


class Solution:
    def findClosestElementsBS(self, arr: List[int], k: int, x: int) -> List[int]:
        low = 0
        # key step 1: To search a block subtracting the block size from the total length
        high = len(arr) - k - 1
        ans = high + 1
        while low <= high:
            mid = low + (high - low) // 2
            # key step 2:  the below is the main condition for binary search to work
            if arr[mid + k] - x >= x - arr[mid]:
                high = mid - 1
                ans = mid
            else:
                low = mid + 1

        return arr[ans : ans + k]

    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        low = 0
        high = len(arr) - k - 1
        ans = high + 1
        while low <= high:
            mid = (low + high) // 2
            if (arr[mid] - x) >= (arr[mid + k] - x):
                high = mid - 1
                ans = mid
            else:
                low = mid + 1

        return arr[ans : ans + k + 1]

    def findClosestElementsNotOptimal(
        self, arr: List[int], k: int, x: int
    ) -> List[int]:
        index = self.lower_bound(arr, 0, len(arr) - 1, x)
        pivot = index
        if k == 1:
            return arr[index : index + 1]
        if pivot == len(arr):
            return arr[-1 : -1 * k]
        if pivot == 0:
            return arr[0:k]
        leftBound = index
        rightBound = index + 1
        while leftBound > 0 and rightBound < len(arr) and (rightBound - leftBound) < k:
            leftDiff = arr[leftBound] - x
            rightDiff = arr[rightBound] - x
            print(leftDiff, rightDiff)
            if leftDiff < rightDiff:
                leftBound -= 1
            else:
                rightBound += 1
        remainingClosest = k - (rightBound - leftBound)
        print(remainingClosest, leftBound, rightBound)
        if remainingClosest == 0:
            return arr[leftBound:rightBound]
        if rightBound == len(arr):
            leftBound -= remainingClosest
            return arr[leftBound:rightBound]
        if leftBound == 0:
            rightBound += remainingClosest
            return arr[leftBound:rightBound]

    def lower_bound(self, arr, start, end, target):
        low = start
        high = end
        ans = end + 1
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] >= target:
                high = mid - 1
                ans = mid
            else:
                low = mid + 1

        return ans
