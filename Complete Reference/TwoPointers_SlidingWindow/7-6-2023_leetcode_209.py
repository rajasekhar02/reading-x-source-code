from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        sumA = 0
        minLen = 10e6
        start = 0
        itert = 0
        while start < len(nums) and itert < len(nums):
            while sumA < target and itert < len(nums):
                sumA += nums[itert]
                itert += 1
            while sumA >= target:
                minLen = min(itert - start, minLen)
                sumA -= nums[start]
                start += 1

        if minLen == 10e6:
            return 0
        return minLen
