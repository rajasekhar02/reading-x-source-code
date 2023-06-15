from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        total_area = 0
        for i in range(0, len(height) - 2):
            right_max_height = height[i + 1]
            right_max_height_index = i + 1
            block_occupied = 0
            for j in range(i + 2, len(height)):
                if right_max_height < height[j]:
                    right_max_height = height[j]
                    right_max_height_index = j
                block_occupied += height[j]
            total_area = (right_max_height_index - i) * min(height[i], right_max_height)
            i = right_max_height_index - 1
        return total_area


h = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print(Solution().trap(h))
