from typing import List
import math


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counts = [0, 0]
        elements = [-1e9 - 2, -1e9 - 2]
        minCount = (len(nums) // 3) + 1
        for i in nums:
            # I missed elements[1] != i case
            if counts[0] == 0 and elements[1] != i:
                counts[0] = 1
                elements[0] = i
            elif counts[1] == 0 and elements[0] != i:
                counts[1] = 1
                elements[1] = i
            elif elements[0] == i:
                counts[0] += 1
            elif elements[1] == i:
                counts[1] += 1
            else:
                counts[0] -= 1
                counts[1] -= 1

        counts = [0, 0]
        # I didn't come up with recounting the freq logic
        for i in nums:
            if elements[0] == i:
                counts[0] += 1
            elif elements[1] == i:
                counts[1] += 1

        if counts[0] >= minCount and counts[1] >= minCount:
            return elements
        elif counts[0] >= minCount:
            return [elements[0]]
        elif counts[1] >= minCount:
            return [elements[1]]
        else:
            return []
