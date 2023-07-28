from typing import List


class Solution:
    def minCost(self, nums: List[int], x: int) -> int:
        itemsPrice = [i for i in nums]            
        totalItems = len(nums)
        minSum = 10e9
        sum = 0  
        for k in itemsPrice:
            sum += k
        minSum = sum
        for i in range(1, totalItems+1):
            # costOfRotation = x
            for j in range(0,totalItems):
                newPrice = nums[((j+i)%totalItems)] 
                if itemsPrice[j] > newPrice:
                    itemsPrice[j] = newPrice
            sum = 0  
            for k in itemsPrice:
                sum += k
            minSum = min(minSum,(i*x)+sum)
        return minSum
   
nums = [15,150,56,69,214,203]

x = 42

print(Solution().minCost(nums, x))