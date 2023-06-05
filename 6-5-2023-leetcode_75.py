from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        """
         Use Git commits to see improvement of the algorithm
        """
        """Solution in Words
            3-way partitioning algorithm
            * zeros are maintained at the start of the array
            * twos are maintained at the end of the array
            * inner while loops are used to handle situations such as [2,0,2] or [0,1,0]
        """
        zeros = 0
        twos = len(nums) - 1
        ones = 0
        while ones <= twos:
            if nums[ones] == 2:
                temp = nums[twos]
                nums[twos] = nums[ones]
                nums[ones] = temp
                twos -= 1
            elif nums[ones] == 0:
                temp = nums[zeros]
                nums[zeros] = nums[ones]
                nums[ones] = temp
                zeros += 1
                ones += 1
            else:
                ones += 1


arr = [0, 1, 2, 2, 1, 0, 0, 0]
Solution().sortColors(arr)
print(arr)
