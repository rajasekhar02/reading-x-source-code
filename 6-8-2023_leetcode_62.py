class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return self.recur(m - 1, n - 1)

    def recur(self, posm, posn):
        if posm == 0:
            return 1
        if posn == 0:
            return 1
        return self.recur(posm - 1, posn) + self.recur(posm, posn - 1)


m = 3
n = 7
print(Solution().uniquePaths(m, n))
