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

    def findClosestElementsTwoPointers(
        self, arr: List[int], k: int, x: int
    ) -> List[int]:
        low = 0
        high = len(arr) - 1
        while high - low >= k:
            if abs(arr[high] - x) >= abs(arr[low] - x):
                high -= 1
            else:
                low += 1
        return arr[low : high + 1]
