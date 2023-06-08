class Solution:
    def __init__(self):
        self.dp = []

    def initializeDP(self, m, n):
        for i in range(0, m):
            lis = []
            for j in range(0, n):
                lis.append(-1)
            self.dp.append(lis)

    def uniquePaths(self, m: int, n: int) -> int:
        self.initializeDP(m, n)
        return self.recurDP(m - 1, n - 1)

    def recur(self, posm, posn):
        if posm == 0 or posn == 0:
            return 1
        return self.recur(posm - 1, posn) + self.recur(posm, posn - 1)

    def recurDP(self, posm, posn):
        if posm == 0 or posn == 0:
            self.dp[posm][posn] = 1
        elif self.dp[posm][posn] > -1:
            return self.dp[posm][posn]
        else:
            self.dp[posm][posn] = self.recur(posm - 1, posn) + self.recur(
                posm, posn - 1
            )
        return self.dp[posm][posn]


m = 3
n = 7
print(Solution().uniquePaths(m, n))
