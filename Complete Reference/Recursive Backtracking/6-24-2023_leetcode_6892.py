from collections import defaultdict
from typing import List


class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        dictWords = defaultdict(lambda: "")
        count = 0
        for i in words:
            rev = i[::-1]

            if dictWords[rev] != "":
                count += 1
                dictWords[rev] = ""
                continue
            dictWords[i] = rev
        return count


words = ["cd", "ac", "dc", "ca", "zz", "dc", "cd", "dc", "zz", "a", "a", "a"]
print(Solution().maximumNumberOfStringPairs(words))
