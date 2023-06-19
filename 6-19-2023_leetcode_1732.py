from typing import List


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        maxHeight = 0
        currHeight = gain[0]
        # Bug: Misses the last height from finding the maximum height
        for i in range(1, len(gain)):
            if currHeight > maxHeight:
                maxHeight = currHeight
            currHeight += gain[i]
        return maxHeight
