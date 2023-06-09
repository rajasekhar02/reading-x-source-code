from typing import List


class Solution:
    def twoSum(self, nums, start, target, listStartSeq):
        i = start
        size = len(nums)
        j = size - 1
        listAns = []
        while i < size and j >= 0 and i < j:
            if (nums[i] + nums[j]) < target:
                i += 1
            elif (nums[i] + nums[j]) > target:
                j -= 1
            else:
                ans = [k for k in listStartSeq]
                ans.append(nums[i])
                ans.append(nums[j])
                # i += 1
                j -= 1
                listAns.append(ans)
        return listAns

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums = sorted(nums)
        possibleSets = []
        visitedSets = set()
        for i in range(len(nums) - 3):
            for j in range(i + 1, len(nums) - 2):
                ans = self.twoSum(
                    nums, j + 1, target - (nums[i] + nums[j]), [nums[i], nums[j]]
                )
                for k in ans:
                    strList = "_".join([str(h) for h in k])
                    if strList in visitedSets:
                        continue
                    visitedSets.add(strList)
                    possibleSets.append(k)
        return possibleSets

    def fourSumBetter(self, nums: List[int], target: int) -> List[List[int]]:
        nums = sorted(nums)
        possibleSets = []
        visitedSets = set()
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    pos = self.binary_search(
                        nums,
                        k + 1,
                        len(nums) - 1,
                        target - (nums[i] + nums[j] + nums[k]),
                    )
                    if pos == len(nums):
                        continue
                    newList = [nums[i], nums[j], nums[k], nums[pos]]
                    strList = "_".join([str(i) for i in newList])
                    if strList in visitedSets:
                        continue
                    visitedSets.add(strList)
                    possibleSets.append(newList)
        return possibleSets

    def binary_search(self, nums, start, end, target):
        low = start
        high = end
        ans = end + 1
        while low <= high:
            mid = (low + high) // 2

            if nums[mid] > target:
                high = mid - 1
            elif nums[mid] < target:
                low = mid + 1
            else:
                ans = mid
                break
        return ans


nums = [1, 0, -1, 0, -2, 2]
target = 0
print(Solution().fourSum(nums, target))
