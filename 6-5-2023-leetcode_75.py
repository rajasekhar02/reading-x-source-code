from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        """Solution in Words
            3-way partitioning algorithm
            * zeros are maintained at the start of the array
            * twos are maintained at the end of the array
            * inner while loops are used to handle situations such as [2,0,2] or [0,1,0]
        """
        zeros = 0
        twos = len(nums) - 1
        i = 0
        while i < len(nums):
            while nums[i] == 2 and twos >= 0 and i < twos:
                temp = nums[twos]
                nums[twos] = nums[i]
                nums[i] = temp
                twos -= 1

            while nums[i] == 0 and zeros < len(nums) and i > zeros:
                temp = nums[zeros]
                nums[zeros] = nums[i]
                nums[i] = temp
                zeros += 1

            i += 1


arr = [0, 1, 2, 2, 1, 0, 0, 0]
Solution().sortColors(arr)
print(arr)
