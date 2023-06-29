class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
#         calculate frequencies
        maxLenSemi = 0
        firstSemisPos = -1
        startSemiPos = 0
        endSemiPos = 0  
              
        for i in range(0,len(s)-1):
            if s[i] == s[i+1]:
                if firstSemisPos > -1:
                    lenSemi = i - startSemiPos + 1
                    if maxLenSemi < lenSemi:
                        maxLenSemi = lenSemi
                    startSemiPos = firstSemisPos + 1
                    firstSemisPos = i
                    continue
                firstSemisPos = i
        lenSemi = len(s) - startSemiPos 
        if maxLenSemi < lenSemi:
            maxLenSemi = lenSemi
        return maxLenSemi
    
s = "5494" #"5223456711111112567523233"
print(Solution().longestSemiRepetitiveSubstring(s))