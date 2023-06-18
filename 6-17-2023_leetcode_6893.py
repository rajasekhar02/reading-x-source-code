from typing import List


class Solution:
    def specialPerm(self, nums: List[int]) -> int:
        nums = sorted(nums)
        ans = self.recurse(nums)
        return ans
    def recurse(self, nums):
        