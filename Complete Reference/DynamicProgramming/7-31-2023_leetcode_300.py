class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = []
        for i in range(len(nums) + 1):
            dp.append([])
            for j in range(len(nums) + 1):
                dp[i].append(-100000)
        newNums = [-100000]
        for i in nums:
            newNums.append(i)
        return self.recurse(0, 1, newNums, dp)

    def recurse(self, prevBigNumId, currIndex, nums, dp):
        if currIndex == len(nums):
            return 0

        if dp[prevBigNumId][currIndex] != -100000:
            return dp[prevBigNumId][currIndex]

        if nums[prevBigNumId] >= nums[currIndex]:
            """
            don't pick this element
            """
            dp[prevBigNumId][currIndex] = self.recurse(
                prevBigNumId, currIndex + 1, nums, dp
            )
            return dp[prevBigNumId][currIndex]

        """
        pick this element 
        don't pick this element
        """
        lenPickedCurrId = 1 + self.recurse(currIndex, currIndex + 1, nums, dp)
        lenNotPickedCurrId = self.recurse(prevBigNumId, currIndex + 1, nums, dp)
        dp[prevBigNumId][currIndex] = max(lenPickedCurrId, lenNotPickedCurrId)
        return dp[prevBigNumId][currIndex]
