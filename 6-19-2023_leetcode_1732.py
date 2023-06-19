from typing import List


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        currHeight = gain[0]
        maxHeight = max(0, gain[0])
        for i in range(1, len(gain)):
            currHeight += gain[i]
            if currHeight > maxHeight:
                maxHeight = currHeight
        return maxHeight
