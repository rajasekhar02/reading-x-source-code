from typing import List

"""
Observations:
1. Always calculate the area between (maxLeft, Left) and (maxRight, Right)
2. 
"""
class Solution:
    def trap(self, height: List[int]) -> int:
        total_area = 0
        left = 0
        right = len(height) - 1
        maxLeft = 0
        maxRight = 0
        while left <= right:
            if height[left] <= height[right]:
                if height[left] > maxLeft:
                    maxLeft = height[left]
                else:
                    total_area += maxLeft - height[left]
                left += 1
            else:
                if height[right] > maxRight:
                    maxRight = height[right]
                else:
                    total_area += maxRight - height[right]
                right -= 1
        return total_area


h = [
    10,
    0,
    8,
    0,
    6,
    0,
    4,
    0,
    6,
    0,
    8,
    0,
    10,
]  # [0,1,0,2,0,3,0,4,0,3,0,2,0,1]#[4, 2, 0, 3, 2, 5]  # [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print(Solution().trap(h))
