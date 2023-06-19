from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums = sorted(nums)
        for i in range(0,len(nums)):
            visitedNums = 0
            perm = self.dfs(i,len(nums), nums, visitedNums)
            for j in perm:
                j.append(nums[i])
                ans.append(j)
        return ans
    def dfs(self, pos, N, nums, visited) -> List[List[int]]:
        if N == 0:
            return [[]]
        visited |= (1 << (pos))
        ans = []
        for i in range(0,len(nums)):
            if visited & (1 << (i)): continue
            ans1 = self.dfs(i, N-1, nums, visited)
            for j in ans1:
                j.append(nums[i])
                ans.append(j)
        if len(ans) == 0:
            return [[]]
        return ans