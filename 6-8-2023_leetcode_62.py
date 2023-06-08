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
        self.initializeDP(2, n)
        return self.optimalSol(m - 1, n - 1)

    def subOptimaluniquePath(self, m: int, n: int) -> int:
        self.initializeDP(m, n)
        return self.iterDP(m - 1, n - 1)

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

    def iterDP(self, posm, posn):
        self.dp[0][0] = 0
        for i in range(0, posm + 1):
            for j in range(0, posn + 1):
                if i == 0:
                    self.dp[i][j] = 1
                elif j == 0:
                    self.dp[i][j] = 1
                else:
                    self.dp[i][j] = self.dp[i - 1][j] + self.dp[i][j - 1]
        return self.dp[posm][posn]

    def optimalSol(self, posm, posn):
        # self.dp[0][0] = 0
        for j in range(0, posn + 1):
            self.dp[0][j] = 1
        self.dp[1][0] = 1
        for it in range(0, posm):
            for j in range(1, posn + 1):
                self.dp[1][j] = self.dp[0][j] + self.dp[1][j - 1]
            for j in range(0, posn + 1):
                self.dp[0][j] = self.dp[1][j]
        return self.dp[0][posn] if posm == 0 else self.dp[1][posn]


m = 2
n = 4
print(Solution().uniquePaths(m, n))
