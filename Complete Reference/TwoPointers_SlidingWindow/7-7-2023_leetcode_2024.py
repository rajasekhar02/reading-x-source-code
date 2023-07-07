class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        ans = k
        cnt = [0, 0]
        for i in range(0, k):
            cnt[int(answerKey[i] == "T")] += 1
        left = 0
        right = k
        while left < len(answerKey) and right < len(answerKey):
            cnt[int(answerKey[right] == "T")] += 1
            while min(cnt[0], cnt[1]) > k:
                cnt[int(answerKey[left] == "T")] -= 1
                left += 1
            ans = max(ans, right - left + 1)
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
        for i in range(0, len(answerKey)):
            cntT += answerKey[i] == "T"
            cntF += answerKey[i] == "F"
            """
                Key Point:
                For Testcase: answerKey = "FFTFTTTFFF", k = 1
                By using the min function, the algorithm ensures that it considers the minimum count between "T" and "F" at each step. 
                This allows the algorithm to properly handle cases where the count of either "T" or "F" exceeds k and adjust the sliding window accordingly.
            """
            # print(cntT, cntF, ans)
            minCnt = min(cntT, cntF)
            while minCnt > k:
                cntT -= answerKey[start] == "T"
                cntF -= answerKey[start] == "F"
                start += 1
                minCnt = min(cntT, cntF)
            ans = max(ans, cntT + cntF)
        return ans
