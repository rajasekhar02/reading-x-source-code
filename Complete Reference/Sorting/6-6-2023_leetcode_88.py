import math
from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m
        j = n
        while i > 0 and j > 0:
            if nums1[i - 1] < nums2[j - 1]:
                nums1[i + j - 1] = nums2[j - 1]
                j -= 1
            elif nums1[i - 1] > nums2[j - 1]:
                nums1[i + j - 1] = nums1[i - 1]
                i -= 1
            else:
                nums1[i + j - 1] = nums1[i - 1]
                nums1[i + j - 2] = nums2[j - 1]
                j -= 1
                i -= 1
        while j > 0:
            nums1[i + j - 1] = nums2[j - 1]
            j -= 1


# nums1 = [2, 5, 6, 0, 0, 0]
# m = 3
# nums2 = [1, 2, 3]
# n = 3
nums1 = [2, 3, 4, 5, 6, 0]
m = 5
nums2 = [1]
n = 1


Solution().merge(nums1, m, nums2, n)
print(nums1)
