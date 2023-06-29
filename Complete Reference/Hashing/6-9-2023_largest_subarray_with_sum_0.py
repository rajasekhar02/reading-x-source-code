class Solution:
    def maxLen(self, n, arr):
        # Logic Intuition:
        # revisiting of the same sum means the sum of the elements between this range is equal 0
        # As we need the longest we dont need to replace the first occurence position of the sum

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
