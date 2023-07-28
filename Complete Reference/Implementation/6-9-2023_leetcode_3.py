class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dicChar = {}
        maxLen = 0
        start = 0
        currLen = 0
        for id, i in enumerate(s):
            # this condition handles all the elements that are in the discarded string
            # tmmzuxt => in this after discarding m the letter t is also discarded so this handles that condition
            if i in dicChar and start < dicChar[i]:
                if maxLen < currLen:
                    maxLen = currLen
                start = dicChar[i]
                currLen = id - start + 1
                dicChar[i] = id + 1
            else:
                currLen += 1
                dicChar[i] = id + 1
        if currLen > maxLen:
            maxLen = currLen
        return maxLen


s = "bbtablud"
print(Solution().lengthOfLongestSubstring(s))
