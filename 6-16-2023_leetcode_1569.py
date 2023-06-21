import math
from typing import List


class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        # no of topological orderings
        return self.recurse(nums)

    def recurse(self, nums):
        if len(nums) == 1:
            return 1

        left = []
        right = []
        for i in range(1, len(nums)):
            if nums[0] < nums[i]:
                right.append(nums[i])
            else:
                left.append(nums[i])

        return (
            math.comb(len(nums), len(left)) * self.recurse(left) * self.recurse(right)
        )
