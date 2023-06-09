class Solution:
    def maxLen(self, n, arr):
        # Code here
        sum = 0
        maxi = 0
        dicSum = {}
        for i in range(0, n):
            sum += arr[i]
            if sum == 0:
                maxi = i + 1
            else:
                if sum in dicSum:
                    maxi = max(maxi, i - dicSum[sum])
                else:
                    dicSum[sum] = i
        return maxi
