from typing import List


class Solution:
    def alternatingSubarray(self, nums: List[int]) -> int:
        maxLen = -1
        for i in range(0, len(nums) - 1):
            if nums[i + 1] != nums[i] + 1:
                continue
            count = 1
            eql1 = True
            for j in range(i + 1, len(nums) - 1):
                if eql1 and nums[j] == nums[j + 1] - 1:
                    count += 1
                elif eql1 == False and nums[j] == nums[j + 1] + 1:
                    count += 1
                else:
                    break
            maxLen = max(maxLen, count)
        return maxLen


lis = [
    [2, 3, 4, 3, 4],
    [3, 4, 3, 4, 3],
    [4, 5, 6],
    [1, 1, 1, 1],
    [13, 14, 15, 14],
    [1, 2, 1],
]

for i in lis:
    print(Solution().alternatingSubarray(i))
