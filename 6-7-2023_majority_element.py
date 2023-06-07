from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return self.dcMajority(nums, 0, len(nums) - 1)[0]

    # does not work all the cases
    def dcMajority(self, nums, start, end):
        if start < end:
            mid = (start + end) // 2
            majorEle1 = self.dcMajority(nums, start, mid)
            majorEle2 = self.dcMajority(nums, mid + 1, end)
            if majorEle1[0] == majorEle2[0]:
                return [majorEle1[0], max(majorEle1[1], majorEle2[1]) + 1]
            elif majorEle2[1] > majorEle1[1]:
                return majorEle2
            else:
                return majorEle1
        return [nums[start], 0]


nums = [6, 5, 5]
print(Solution().majorityElement(nums))
