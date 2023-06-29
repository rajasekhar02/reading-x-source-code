import math


class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 1:
            return x

        if n == 0:
            return 1

        if n < 0:
            n = -1 * n
            return 1 / self.myPow(x, n)

        if n & 1:
            mPow = self.myPow(x, (n - 1) >> 1)
            return mPow * mPow * x

        mPow = self.myPow(x, n >> 1)
        return mPow * mPow


print(Solution().myPow(1.2, 1 << 6))
