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
        # newNums = [-100000]
        return self.recurse(-1, 0, nums, dp)

    def recurse(self, prevBigNumId, currIndex, nums, dp):
        if currIndex == len(nums):
            return 0

        if dp[prevBigNumId][currIndex] != -100000:
            return dp[prevBigNumId][currIndex]

        """
        don't pick this element
        """
        dp[prevBigNumId][currIndex] = self.recurse(
            prevBigNumId, currIndex + 1, nums, dp
        )

        if (prevBigNumId == -1) or (nums[prevBigNumId] < nums[currIndex]):
            """
            pick this element
            don't pick this element
            """
            lenPickedCurrId = 1 + self.recurse(currIndex, currIndex + 1, nums, dp)
            dp[prevBigNumId][currIndex] = max(
                lenPickedCurrId, dp[prevBigNumId][currIndex]
            )
        return dp[prevBigNumId][currIndex]
