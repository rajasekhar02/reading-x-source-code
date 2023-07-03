from typing import List


class Solution:
    def __init__(self):
        self.minimumFairness = 8 * 10e5

    def distributeCookies(self, cookies: List[int], k: int) -> int:
        self.recurse(cookies, len(cookies) - 1, [0] * k, k)
        return self.minimumFairness

    def recurse(self, cookies, ibag, assignedK, k):
        if ibag == -1:
            self.minimumFairness = min(max(assignedK), self.minimumFairness)
            return
        # key step: to reduce the search space
        currMax = max(assignedK)
        if currMax > self.minimumFairness:
            return
        for i in range(0, k):
            assignedK[i] += cookies[ibag]
            self.recurse(cookies, ibag - 1, assignedK, k)
            assignedK[i] -= cookies[ibag]
