from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        element = 0
        for i in nums:
            if count == 0:
                count = 1
                element = i
            elif element == i:
                count += 1
            else:
                count -= 1
        return element


nums = [3, 2, 3]
print(Solution().majorityElement(nums))
