from typing import List


class Solution:
    def __init(self):
        self.subsetSizeAtPos = []

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        size = len(nums)
        self.subsetSizeAtPos = [1] * (size + 1)
        increment = size
        self.subsetSizeAtPos[increment] = 1
        i = increment - 1
        self.subsetSizeAtPos[i] = 2
        j = i - 1
        while j >= 0:
            if nums[i] == nums[j]:
                self.subsetSizeAtPos[j] = (
                    self.subsetSizeAtPos[i] + self.subsetSizeAtPos[increment]
                )
            else:
                self.subsetSizeAtPos[j] = self.subsetSizeAtPos[i] * 2
                increment = i
            i -= 1
            j -= 1
        # print(self.subsetSizeAtPos)
        return self.recurse(nums, 0, size)
        # return 0

    def recurse(self, nums, pos, N):
        if N == 0:
            return [[]]
        lis = self.recurse(nums, pos + 1, N - 1)
        start = 0
        end = self.subsetSizeAtPos[pos + 1]

        if pos + 1 < len(nums) and nums[pos] == nums[pos + 1]:
            start = self.subsetSizeAtPos[pos + 2]
            end = self.subsetSizeAtPos[pos + 1]
        # print(size, start, end, pos + 1 < len(nums))

        for i in range(start, end):
            newList = [*lis[i]]
            newList.append(nums[pos])
            lis.append(newList)
        # print(lis, len(lis))
        return lis


print(Solution().subsetsWithDup([1, 2, 2]))  # [1, 1, 2, 2, 2, 3, 3, 3, 4, 5, 6]
