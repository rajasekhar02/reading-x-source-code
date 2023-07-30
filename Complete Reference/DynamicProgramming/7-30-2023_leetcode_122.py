class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = []
        for i in range(0, len(prices)):
            dp.append([-1,-1])
        # return self.recurse(0, 0, prices, dp)
        return self.iterDP(prices)
    """
        What i did to convert from recursive to iterative dp
    """
    def recurse(self, startIndex, bought, prices, dp):
        """ Hint for Coverting to Iter DP
         this line is equal to initializing 
         dp[len(prices)][0] = 0
         dp[len(prices)][1] = 0
        """ 
        if startIndex == len(prices):
            return 0
        """ Hint for Coverting to Iter DP
        neglect below 2 lines
        """
        if dp[startIndex][bought] != -1:
            return dp[startIndex][bought]
        maxProfit = 0
        i = startIndex
        if bought == 0:
            # for i in range(startIndex, len(prices)):
            """ Hint for Coverting to Iter DP

                dp[i][0] = max(dp[i+1][0], dp[i+1][1]-prices[i])
                
                where:
                dp[i][0] => is equavilatent to line 43 i.e dp[startIndex][0]
                dp[i+1][0] => self.recurse(i+1, 0, prices, dp)
                dp[i+1][1] - prices[i] => self.recurse(i+1, 1, prices, dp)-prices[i]
            """
            profit = self.recurse(i+1, 1, prices, dp)-prices[i]
            profitNotBuyingToday = self.recurse(i+1, 0, prices, dp)
            maxProfit = max(profitNotBuyingToday, profit)
        else:
            """ Hint for Coverting to Iter DP
            Same as above
            """
            # for i in range(startIndex, len(prices)):
            profit = self.recurse(i+1, 0, prices, dp)+prices[i]
            profitNotSellingToday = self.recurse(i+1, 1, prices, dp)
            maxProfit = max(profitNotSellingToday, profit)
        dp[startIndex][bought] = maxProfit
        return maxProfit
    
    def iterDP(self, prices):
        # 0 => bought
        # 1 => sold
        dp = []
        for i in range(0, len(prices)+1):
            dp.append([0,0])
        for i in range(len(prices)-1, -1, -1):
            dp[i][0] = max(dp[i+1][0], dp[i+1][1]-prices[i])
            dp[i][1] = max(dp[i+1][1], dp[i+1][0]+prices[i])
        print(dp)
        return dp[0][0]