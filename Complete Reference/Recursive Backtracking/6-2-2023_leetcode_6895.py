class Solution:
    def longestString(self, x: int, y: int, z: int) -> int:
        longestLen = z * 2
        minOfXY = min(x, y)
        longestLen += minOfXY * 4
        x -= minOfXY
        y -= minOfXY
        if x > 0 or y > 0:
            return longestLen + 2
        else:
            return longestLen


x = 1
y = 2
z = 1
print(Solution().longestString(x, y, z))
