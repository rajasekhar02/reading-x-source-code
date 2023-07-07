class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        left = 0
        right = 0
        ans = 0
        cntT = 0
        cntF = 0
        while left < len(answerKey) and right < len(answerKey):
            cntT += answerKey[right] == "T"
            cntF += answerKey[right] == "F"
            if cntF > k:
                ans = max(ans, cntT + k)
                while left < len(answerKey) and cntF > k:
                    cntF -= answerKey[left] == "F"
                    cntT -= answerKey[left] == "T"
                    left += 1
            elif cntT > k:
                ans = max(ans, cntF + k)
                while left < len(answerKey) and cntT > k:
                    cntF -= answerKey[left] == "F"
                    cntT -= answerKey[left] == "T"
                    left += 1
            right += 1
        return ans

    def maxConsecutiveAnswersBS(self, answerKey: str, k: int) -> int:
        # Using Binary search to find the valid sliding window size
        # why it works ?
        # if it satisfies the for len = l then all the windows sizes less than l will be satisfied
        low = 1
        high = len(answerKey)
        ans = len(answerKey)
        while low <= high:
            mid = low + (high - low) // 2
            if not self.slider(mid, answerKey, k):
                high = mid - 1
            else:
                low = mid + 1
                ans = mid
        return ans

    def slider(self, windowsize, answerKey, k):
        cntT = 0
        cntF = 0
        for i in range(0, windowsize):
            cntT += answerKey[i] == "T"
            cntF += answerKey[i] == "F"
        if min(cntT, cntF) < k:
            return True
        for i in range(windowsize, len(answerKey)):
            cntT -= answerKey[i - windowsize]
            cntF -= answerKey[i - windowsize]
            cntT += answerKey[i] == "T"
            cntF += answerKey[i] == "F"
            if min(cntT, cntF) < k:
                return True
        return False

    def maxConsecutiveAnswersNotWorking(self, answerKey: str, k: int) -> int:
        ans = 0
        cntT = 0
        cntF = 0
        start = 0
        cntChsLessThanK = True
        for i in range(0, len(answerKey)):
            cntT += answerKey[i] == "T"
            cntF += answerKey[i] == "F"
            # print(cntT, cntF, ans)
            if cntT > cntF and cntF == k:
                cntChsLessThanK = False
                goForward = i + 1
                tCntF = cntF
                tCntT = cntT
                while tCntF == k and goForward < len(answerKey):
                    tCntF += answerKey[goForward] == "F"
                    tCntT += answerKey[goForward] == "T"
                    goForward += 1
                ans = max(ans, tCntT + min(k, tCntF))
                temp = i - k
                while answerKey[start] == "T" and temp > 1:
                    cntT -= 1
                    start += 1
                    temp -= 1
            elif cntF > cntT and cntT == k:
                cntChsLessThanK = False
                goForward = i + 1
                tCntF = cntF
                tCntT = cntT
                while tCntT == k and goForward < len(answerKey):
                    tCntF += answerKey[goForward] == "F"
                    tCntT += answerKey[goForward] == "T"
                    goForward += 1
                ans = max(ans, tCntF + min(k, tCntT))
                temp = i - k
                while answerKey[start] == "F" and temp > 1:
                    cntF -= 1
                    start += 1
                    temp -= 1
        if cntChsLessThanK:
            return len(answerKey)
        return ans
