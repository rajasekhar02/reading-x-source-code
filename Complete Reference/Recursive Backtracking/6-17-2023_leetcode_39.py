from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = sorted(candidates)
        ans = self.recurse(candidates, 0, target)
        return ans[1]

    def recurse(self, candidates, startFromCadid, target):
        if target == 0:
            return ("VALID", [])
        ans = []
        foundSolution = False
        for id, i in enumerate(candidates):
            if id < startFromCadid or (target - i) < 0:
                continue
            (solValidity, allPossibleCombinations) = self.recurse(
                candidates, id, target - i
            )
            if solValidity == "INVALID":
                continue
            foundSolution = True
            if len(allPossibleCombinations) == 0:
                ans.append([i])
            else:
                for eachSol in allPossibleCombinations:
                    newList = [*eachSol]
                    newList.append(i)
                    ans.append(newList)
        if foundSolution:
            return ("VALID", ans)
        return ("INVALID", ans)


candidates = [2]
target = 1
print(Solution().combinationSum(candidates, target))
