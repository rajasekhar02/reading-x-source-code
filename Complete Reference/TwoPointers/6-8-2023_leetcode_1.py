from typing import List


class Solution:
    # using two pointer method
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        newNums = [[i, id] for id, i in enumerate(nums)]
        # Always forgetting to assign the output of sorted funtion to the list
        newNums = sorted(newNums, key=lambda x: x[0])
        i = 0
        j = len(newNums) - 1
        while i < j:
            if newNums[i][0] + newNums[j][0] > target:
                j -= 1
            elif newNums[i][0] + newNums[j][0] < target:
                i += 1
            else:
                return [newNums[i][1], newNums[j][1]]

        return [0, 0]

    def twoSum2(self, nums: List[int], target: int) -> List[int]:
        newNums = [[i, id] for id, i in enumerate(nums)]
        # Always forgetting to assign the output of sorted funtion to the list
        newNums = sorted(newNums, key=lambda x: x[0])
        for id, i in enumerate(newNums):
            pos = self.binary_search(newNums, id + 1, len(newNums) - 1, target - i[0])
            if pos < len(newNums):
                return [i[1], newNums[pos][1]]
        return [0, 0]

    def binary_search(self, nums, start, end, target):
        low = start
        high = end
        ans = end + 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid][0] > target:
                high = mid - 1
            elif nums[mid][0] < target:
                low = mid + 1
            else:
                ans = mid
                break
        return ans
