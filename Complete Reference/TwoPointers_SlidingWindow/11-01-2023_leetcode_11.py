class Solution:
    def maxArea(self, height: List[int]) -> int:
        """Summary
            1. Pointers at extremes
            2. update the pointer pointing the lower height
        """
        maxE = 0
        i = 0
        j = len(height)-1
        while i<j:
            maxE = max(maxE, (j-i)*min(height[j],height[i]))
            if height[i] < height[j]:
                i+=1
            else:
                j-=1
        return maxE
