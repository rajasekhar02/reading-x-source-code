from typing import List


class Solution:
    def __init__(self):
        self.dp = []

    def maxSubArray(self, nums: List[int]) -> int:
        return self.kadanesAlgorithm(nums)

    def kadanesAlgorithm(self, nums):
        # kadane algorithm
        sum = 0
        max = min(nums)
        for i in nums:
            sum += i
            if sum > max:
                max = sum
            if sum < 0:
                sum = 0
        return max

    def maxSubArrayRec(self, nums: List[int]) -> int:
        return self.recursiveSubRoutine(nums, False, 0)

    def recursiveSubRoutine(self, nums, takeIt, pos) -> int:
        if pos == len(nums):
            # I stuggled to come up with this logic
            # at the end of the tranversal if takeIt is True
            # which means in need to nums[len(nums)] elements
            # which does not exist So we return 0
            # otherwise return -infinity
            return 0 if takeIt else -1e5

        if takeIt:
            return max(0, self.recursiveSubRoutine(nums, True, pos + 1) + nums[pos])

        return max(
            self.recursiveSubRoutine(nums, True, pos + 1) + nums[pos],
            self.recursiveSubRoutine(nums, False, pos + 1),
        )
        """Recursive Intuition
            there are 3 possible paths
            1. stay without taking any elements
            2. If we start taking elements then we can exit from taking elements and we don't start again taking the elements            
        """

    def recursiveSubRoutine(self, nums, takeIt, pos) -> int:
        if pos == len(nums):
            return 0 if takeIt else -1e5

        if takeIt:
            return max(0, self.recursiveSubRoutine(nums, True, pos + 1) + nums[pos])
        # If we take the current element then we should take all the next elements
        return max(
            self.recursiveSubRoutine(nums, True, pos + 1) + nums[pos],
            self.recursiveSubRoutine(nums, False, pos + 1),
        )

    def maxSubArrayTopDownDP(self, nums: List[int]) -> int:
        self.dp = [[] * len(nums)] * 2
        return self.recursiveDPSubRoutine(nums, False, 0)
