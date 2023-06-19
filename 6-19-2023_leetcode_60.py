class Solution:
    def __init__(self):
        self.facts = [1,1]

    def getPermutation(self, n: int, k: int) -> str:
        for i in range(2, n+1):
            self.facts.append(self.facts[-1]*i)
        final_num = self.recurse(1, n, 0, k, "", set())
        return final_num

    def recurse(self, pos, n, permutation_num, k, curr_str, setOfUsedNums):
        curr_pos = pos
        remainPos = n - curr_pos
        numsCnt = permutation_num
        if pos == (n+1):
            return curr_str
        for i in range(1, n+1):
            if i in setOfUsedNums: continue
            numsCnt += self.facts[remainPos]
            if numsCnt >= k:
                curr_str += str(i)
                numsCnt -= self.facts[remainPos]
                setOfUsedNums.add(i)
                break
        return self.recurse(pos+1, n, numsCnt, k, curr_str, setOfUsedNums)
n = 3
k = 1
print(Solution().getPermutation(n, k))