from typing import List


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        maxHeight = 0
        currHeight = gain[0]
        for i in range(1, len(gain)):
            # Bug: Skipping the 1st height from finding max height reached
            currHeight += gain[i]
            if currHeight > maxHeight:
                maxHeight = currHeight
        return maxHeight
