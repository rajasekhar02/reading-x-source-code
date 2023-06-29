from collections import defaultdict


class Solution:
    def solve(self, A, B):
        xr = 0
        dicXOR = {}  # defaultdict(int)
        # value is 1 because to cover cases where B == A[i]
        dicXOR[xr] = 1
        cnt = 0
        for i in A:
            xr = xr ^ i

            x = xr ^ B

            if x in dicXOR:
                cnt += dicXOR[x]

            if xr in dicXOR:
                dicXOR[xr] += 1
            else:
                dicXOR[xr] = 1
        return cnt


A = [4, 2, 2, 6, 4]
B = 6
print(Solution().solve(A, B))
