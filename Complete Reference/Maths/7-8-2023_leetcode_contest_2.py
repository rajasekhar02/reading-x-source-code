import math


class Solution:
    def minimumBeautifulSubstrings(self, s: str) -> int:
        val = self.recurse(s, 0)
        if val >= 18:
            return -1
        return val

    def getPowOf5(self, num):
        low = 0
        high = 18
        ans = -1
        while low <= high:
            mid = low + (high - low) // 2
            if pow(5, mid) == num:
                return mid
            elif pow(5, mid) < num:
                low = low + 1
            else:
                high = high - 1
        return ans

    def recurse(self, s, start):
        if start == len(s):
            return 0
        if s[start] == "0":
            # print(s[start], "returned")
            return 18
        num = 0
        minVal = 18
        for i in range(start, len(s)):
            if s[i] == "0":
                num = num << 1
                continue
            num = (num << 1) + 1
            powOf5 = math.log(num) / math.log(5)
            # self.getPowOf5(num)  #
            """
            key point: As I am checking for zero for floating values
            take 1e-5 or less as to check whether value is equal to zero
            """
            if powOf5 - int(powOf5) < 1e-5 or num == 1:
                val = 1 + self.recurse(s, i + 1)
                minVal = min(minVal, val)
        return minVal


print(Solution().minimumBeautifulSubstrings("10110111111011"))
