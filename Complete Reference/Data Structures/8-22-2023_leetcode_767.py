class Solution:
    def reorganizeString(self, s: str) -> str:
        # self.rearrangeByPQ(s)
        return self.rearrangeOddEven(s)

    def recurseCaller(self, s):
        charsFreq = Counter(s)
        return self.recurse(charsFreq, "")

    def recurse(self, charsFreq, usedChar):
        countCharsGtZero = 0
        for i in charsFreq:
            if i != usedChar and charsFreq[i] > 0:
                newCharsFreq = charsFreq.copy()
                newCharsFreq[i] -= 1
                rearrStr = self.recurse(newCharsFreq, i)
                if rearrStr != "":
                    return rearrStr + usedChar
            if charsFreq[i] > 0:
                countCharsGtZero += 1
        if charsFreq[usedChar] >= 1 or countCharsGtZero >= 1:
            return ""
        return usedChar
    
    def rearrangeByPQ(self,s):
        charsFreq = Counter(s)
        pq = []
        for i in charsFreq:
            heappush(pq, (-charsFreq[i], i))
        ans = []
        while len(pq) > 0:
            freq, char = heappop(pq)
            if not ans or ans[-1] != char:
                ans.append(char)
                # print(ans, freq, pq)
                if (freq + 1) < 0:
                    heappush(pq, (freq + 1, char))
            else:
                if len(pq) == 0: return ''
                freq2, char2 = heappop(pq)
                # if ans[-1] != char2: # this statement is not needed because ans[-1] already matches with char
                ans.append(char2)
                if (freq2+1) < 0:
                    heappush(pq, (freq2+1, char2))
                heappush(pq, (freq, char))
        return "".join(ans)
    
    def rearrangeOddEven(self, s):
        charsFreq = Counter(s)
        listCharsFreq = map(lambda x: [x[0],x[1]],charsFreq.items())
        listCharsFreq = sorted(listCharsFreq, key = lambda x: x[1], reverse=True)
        if 2*listCharsFreq[0][1] > len(s)+1:
            return ""
        newS = [""]*len(s)
        idForListChar = 0
        item = listCharsFreq[idForListChar]
        idForListChar += 1
        # fill even indices
        for i in range(0, len(s), 2):
            if item[1] == 0:
                item = listCharsFreq[idForListChar]
                idForListChar+=1
            newS[i] = item[0]
            item[1] -= 1
        # fill odd indices
        for i in range(1, len(s), 2):
            if item[1] == 0:
                item = listCharsFreq[idForListChar]
                idForListChar+=1
            newS[i] = item[0]
            item[1] -= 1
        return "".join(newS)
        