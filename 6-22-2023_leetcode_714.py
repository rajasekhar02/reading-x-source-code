from typing import List


class Solution:
    def __init__(self):
        self.dp = []

    def maxProfitNotWorking(self, prices: List[int], fee: int) -> int:
        maxA = 0
        minA = 10e5
        profit = 0
        for i in range(0, len(prices)):
            if prices[i] < minA:
                minA = prices[i]
            elif prices[i] > maxA:
                maxA = prices[i]
            # else:
            #     profit = (maxA-minA) - fee
            #     minA = prices[i]
            #     maxA = 0

        return profit

    def maxProfit(self, prices: List[int], fee: int) -> int:
        self.dp = [[-1] * len(prices) for i in range(0, 2)]
        return self.recurse(prices, fee, 0, 0, -1)

    def recurseWithForLoops(self, prices, fee, trans_status, pos, bought_pos):
        if pos == len(prices):
            if trans_status == 0:
                return 0
            else:
                return -1 * prices[bought_pos]

        max_profit = 0
        if self.dp[trans_status][pos] != -1:
            return self.dp[trans_status][pos]
        if trans_status == 1:
            # selling the stocks
            for sold_pos in range(pos, len(prices)):
                if prices[sold_pos] <= prices[bought_pos]:
                    continue
                curr_transaction_profit = prices[sold_pos] - prices[bought_pos] - fee
                total_profit = curr_transaction_profit + max(
                    0, self.recurse(prices, fee, 0, sold_pos + 1, -1)
                )
                max_profit = max(total_profit, max_profit)
        else:
            # buying the stocks
            for i in range(pos, len(prices)):
                total_profit = self.recurse(prices, fee, 1, i + 1, i)
                max_profit = max(total_profit, max_profit)
        self.dp[trans_status][pos] = max_profit
        return self.dp[trans_status][pos]

    def recurse(self, prices, fee, trans_status, pos, bought_pos):
        if pos == len(prices):
            # return 0
            if trans_status == 0:
                return 0
            else:
                return -1 * prices[bought_pos]

        max_profit = 0
        # if self.dp[trans_status][pos] != -1:
        #     return self.dp[trans_status][pos]

        if trans_status == 1:
            # selling the stocks
            # for sold_pos in range(pos, len(prices)):
            # if prices[sold_pos] <= prices[bought_pos]:
            #     continue
            curr_transaction_profit = prices[pos] - prices[bought_pos] - fee
            total_profit = curr_transaction_profit + self.recurse(
                prices, fee, 0, pos + 1, -1
            )
            max_profit = max(total_profit, max_profit)
        else:
            # buying the stocks
            # for i in range(pos, len(prices)):
            total_profit = self.recurse(prices, fee, 1, pos + 1, pos)
            max_profit = max(total_profit, max_profit)

        profit_for_nothing = self.recurse(
            prices, fee, trans_status, pos + 1, bought_pos
        )

        # self.dp[trans_status][pos] =
        return max(max_profit, profit_for_nothing)

    # SOLD: 0, BOUGHT: 1
    def recurseWorking(self, prices, fee, trans_status, pos):
        if pos == len(prices):
            return 0

        max_profit = 0

        if self.dp[trans_status][pos] != -1:
            return self.dp[trans_status][pos]

        if trans_status == 1:
            # selling the stocks
            # for sold_pos in range(pos, len(prices)):
            # if prices[sold_pos] <= prices[bought_pos]:
            #     continue
            curr_transaction_profit = prices[pos] - fee
            total_profit = curr_transaction_profit + max(
                0, self.recurse(prices, fee, 0, pos + 1)
            )
            max_profit = max(total_profit, max_profit)
        else:
            # buying the stocks
            # for i in range(pos, len(prices)):
            total_profit = -prices[pos] + self.recurse(prices, fee, 1, pos + 1)
            max_profit = max(total_profit, max_profit)

        profit_for_nothing = self.recurse(prices, fee, trans_status, pos + 1)
        self.dp[trans_status][pos] = max(max_profit, profit_for_nothing)
        return self.dp[trans_status][pos]


prices = [1, 3, 2, 8, 4, 9]
fee = 2
solution = Solution()
print(solution.maxProfit(prices, fee), solution.dp)
