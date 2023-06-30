from typing import List


class Solution:
    def minimizeConcatenatedLength(self, words: List[str]) -> int:
        dictChars = []
        for i in range(0, 26):
            dictChars.append([])
            for j in range(0, 26):
                dictChars[-1].append([0, 0])
        # dictChars[0].append(1)
        for i in words:
            # print(ord(i[0]) - ord("a"), ord(i[-1]) - ord("a"))
            # print(dictChars[ord(i[0]) - ord("a")])
            dictChars[ord(i[0]) - ord("a")][ord(i[-1]) - ord("a")][0] += len(i)
            dictChars[ord(i[0]) - ord("a")][ord(i[-1]) - ord("a")][1] += 1
        
        for start in range(0,26):
            for end in range(0,26):
                if start == end:
                    continue
                dictChars[i][j][0] += dictChars[j][i][0]
                dictChars[i][j][0] -= min(dictChars[i][j][1],dictChars[j][i][1]) - 1
        minLen = 0
        for start in range(0,26):
            for end in range(0,26):
                if start < end:
                    continue
                minLen += dictChars[i][j][]
words = ["ab", "b"]
print(Solution().minimizeConcatenatedLength(words))
