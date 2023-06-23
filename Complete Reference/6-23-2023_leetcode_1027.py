from typing import List
from collections import defaultdict

class Solution:
    def __init__(self):
        self.visited = []
    def longestArithSeqLength(self, nums: List[int]) -> int:
        diffOf2 = [ [0]*len(nums) for i in range(0,len(nums)) ]
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                diffOf2[i][j] = nums[j]-nums[i]
        # print(diffOf2)
        maxVal = 0
        self.visited = [defaultdict(int) for i in range(0,len(nums))]
        # for i in range(len(nums)-1, -1, -1):
        val = self.dfs(0,diffOf2,-1e5)
        maxVal = max(maxVal,val)
        return maxVal
    
    def longestArithSeqLengthNotWorkingDP(self, nums: List[int]) -> int:
        dp = [defaultdict(int) for i in range(0,len(nums))]
        for j in range(1,len(nums)):
            dp[0][nums[j]-nums[0]] = 1
        maxVal = 0
        maxDiff= 0
        for i in range(1,len(nums)):
            for j in range(i+1,len(nums)):
                # if dp[i][nums[j]-nums[i]] > 0:
                dp[i][nums[j]-nums[i]] = 1+dp[i-1][nums[j]-nums[i]]
            
            for k in dp[i]:
                if maxVal < dp[i][k]:
                    maxVal = dp[i][k]
                    maxDiff = k
        print(maxDiff,dp)
        return maxVal+1        
    def dfs(self, pos, diffOf2, val):
        if pos == len(diffOf2)-1:
            return 1
        maxLenSeries = 1
        for j in range(pos+1,len(diffOf2[pos])):
            if val == -1e5:
                lenSeries = 1 + self.dfs(j, diffOf2, diffOf2[pos][j])
                maxLenSeries = max(lenSeries,maxLenSeries)
            elif val == diffOf2[pos][j]:
                lenSeries = 1 + self.dfs(j, diffOf2, diffOf2[pos][j])
                maxLenSeries = max(lenSeries,maxLenSeries)
        return maxLenSeries

nums= [1,1,0,0,1,0,0,1,0,1,0,1,1,1,0,1,1,0,1,1,0,0,1,1,0,1,0,1,1,0,1,1,1,1,1,0,1,0,0,0,0,0,0,0,1,0,0,1,1,1,0,0,0,0,0,1,1,1,0,0,1,1,1,1,1,0,0,0,1,1,1,1,1,1,0,1,1,0,0,0,1,1,1,1,0,0,1,1,1,0,0,0,1,0,1,0,1,1,1,0,1,1,0,1,1,1,0,1,1,1,0,1,0,1,0,0,0,1,1,0,0,0,0,1,1,0,0,1,0,0,1,0,1,0,0,0,0,0,1,1,1,1,1,0,1,1,0,0,0,0,0,0,1,1,1,0,1,1,0,1,1,1,0,1,0,1,0,0,1,0,0,1,0,0,1,1,0,1,0,0,1,1,0,1,0,0,0,1,0,1,1,1,1,1,0,0,0,1,0,0,1,0,1,1,1,1,0,1,1,0,0,0,0,1,0,1,0,1,1,1,1,1,0,0,0,0,0,1,0,0,0,1,0,1,0,0,0,0,0,1,1,1,0,0,1,1,1,0,1,1,0,1,1,1,0,1,0,0,1,0,1,0,0,1,0,1,1,1,1,1,1,1,1,0,1,0,1,1,1,0,1,1,0,1,0,0,0,1,0,1,0,0,0,0,1,0,0,0,1,0,1,1,1,0,1,0,0,1,0,1,0,0,0,1,0,1,0,1,1,0,0,1,1,0,0,1,0,1,1,1,1,0,1,1,1,0,0,0,1,0,0,1,1,0,0,1,0,0,0,0,0,0,1,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,0,1,1,1,1,0,0,0,1,0,0,0,1,1,0,1,0,1,0,0,0,0,1,1,0,0,1,1,0,0,1,1,1,0,0,0,0,1,0,1,1,1,1,1,1,1,1,1,1,1,0,1,0,1,1,0,0,1,0,0,0,1,0,0,0,0,1,1,1,0,1,1,0,0,1,0,0,1,0,0,1,0,0,1,1,0,0,1,1,0,0,0,1,1,0,1,0,0,0,0,0,1,0,0,0,1,0,0,0,1,1,1,0,1,1,0,1,1,0,0,0,1,0,0,0,0,1,0,0,0,1,0,0,0,0,0,1,0,1,1,0,1,0,1,0,1,0,0,0,0,1,1,0,0,0,1,1,0,1,1,0,1,1,0,0,0,0,1,1,0,0,1,1,0,0,0,0,0,0,0,1,0,1,1,1,0,0,0,1,1,0,1,0,0,1,0,0,0,1,1,0,0,0,0,1,1,0,0,1,1,0,1,0,0,0,1,1,0,1,0,0,0,1,1,1,1,1] #[20,1,15,3,10,5,8] #[20,1,15,15,15] #[3,6,9,12]#[9,4,7,2,10] #
print(Solution().longestArithSeqLength(nums))