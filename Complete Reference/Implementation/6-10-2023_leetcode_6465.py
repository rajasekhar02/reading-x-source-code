from collections import Counter
class Solution:
    def smallestString(self, s: str) -> str:
        listStr = []
        addRemaining = False
        # charFreqs = Counter(s)
        # if charFreqs['a'] == len(s):
        #     return "".join(["a"]*(len(s)-1))+"z"
        prevC = s[0]
        charAndFreqs = []
        count = 1
        for i in range(1,len(s)):
            if prevC != s[i]:
                charAndFreqs.append([prevC, count])
                prevC = s[i]
                count = 1
                continue
            count+=1
        if(count > 0):
            charAndFreqs.append([prevC, count])
        
        if charAndFreqs[0][0] == "a" and charAndFreqs[0][1] == len(s):
            return "".join(["a"]*(len(s)-1))+"z"
        
        for id,i in enumerate(charAndFreqs):
            if id == 0 and i[0] == "a":
                listStr.append("".join([i[0]]*i[1]))
                continue
            elif i[0] == "a":
                listStr.append("".join([i[0]]*i[1]))
                addRemaining = True
            elif addRemaining:
                listStr.append("".join([i[0]]*i[1]))
            else:
                listStr.append( "".join([chr(ord(i[0])-1)]*i[1]) )
        return "".join(listStr)
    
    
s = "baa"
print(Solution().smallestString(s))