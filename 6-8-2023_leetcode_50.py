import math


class Solution:
    def __init__(self):
        self.dp = [-1] * 32

    def myPow(self, x: float, n: int) -> float:
        if n == 1:
            return x
        if n == 0:
            return 1

        if n < 0:
            n = -1 * n
            return 1 / self.myPow(x, n)

        if n & 1:
            nthPower = round(math.log2((n - 1)))
            if self.dp[nthPower] == -1:
                mPow = self.myPow(x, (n - 1) >> 1)
                self.dp[nthPower] = mPow * mPow * x
            return self.dp[nthPower]

        nthPower = round(math.log2(n))
        if self.dp[nthPower] == -1:
            mPow = self.myPow(x, n >> 1)
            self.dp[nthPower] = mPow * mPow

        return self.dp[nthPower]


print(Solution().myPow(2, 11))
