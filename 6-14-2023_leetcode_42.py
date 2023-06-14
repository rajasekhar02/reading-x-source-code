from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        prev_height = 0
        prev_index = 0
        desc_blocks_area = 0
        asc_blocks_area = 0
        area_occupied_by_blocks = 0
        for i in range(0, len(height)):
            curr_height = height[i]
            if curr_height == 0:
                continue
            if prev_height == 0 and curr_height > 0:
                prev_height = curr_height
                prev_index = i
            elif prev_height <= curr_height:
                asc_blocks_area += (
                    (i - prev_index - 1) * prev_height
                ) - area_occupied_by_blocks
                area_occupied_by_blocks = 0
                desc_blocks_area = 0
                prev_height = curr_height
                prev_index = i
            elif prev_height > curr_height:
                if desc_blocks_area > 0:
                    desc_blocks_area += curr_height - height[i - 1]
                else:
                    desc_blocks_area += (i - prev_index - 1) * curr_height
                area_occupied_by_blocks += curr_height
        print(asc_blocks_area)
        return asc_blocks_area + desc_blocks_area
