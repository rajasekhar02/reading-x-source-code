from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = sorted(candidates)
        ans = self.recurse(candidates, 0, target)
        return ans[1]

    def recurse(self, candidates, start, target):
        if target == 0:
            return (True, [])
        ans = []
        foundSolution = False
        for i in range(start, len(candidates)):
            if (target - candidates[i]) < 0:
                continue
            # key logic to skip duplicates that is i > start
            if i > start and candidates[i] == candidates[i - 1]:
                continue
            (solValid, possibleComb) = self.recurse(
                candidates, i + 1, target - candidates[i]
            )
            if not solValid:
                continue
            foundSolution = True
            if len(possibleComb) == 0:
                ans.append([candidates[i]])
                continue
            for eachComb in possibleComb:
                newList = [*eachComb]
                newList.append(candidates[i])
                ans.append(newList)
        return (foundSolution, ans)


candidates = [2, 5, 2, 1, 2]  # [10, 1, 2, 7, 6, 1, 5]
target = 6
print(Solution().combinationSum2(candidates, target))
