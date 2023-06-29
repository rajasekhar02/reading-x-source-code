from heapq import heappush, nsmallest
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        return self.solveWithHeuristic(prices)

    def recurse(self, arr, boughtAmount, day):
        if day == len(arr):
            return 0
        if boughtAmount >= 0:
            return max(
                self.recurse(arr, boughtAmount, day + 1), arr[day] - boughtAmount
            )
        return max(self.recurse(arr, arr[day], day + 1), self.recurse(arr, -1, day + 1))

    # Unnecessary use of heap but it gave the idea for heuristic solution
    def solveWithHeap(self, prices):
        h = []
        maxProfit = -1
        for id, price in enumerate(prices):
            if id > 0:
                maxProfit = max(price - nsmallest(1, h)[0], maxProfit)
            heappush(h, price)
        return max(0, maxProfit)

    def solveWithHeuristic(self, prices):
        minBuyingPrice = 1e5
        maxSellingPrice = -1
        maxProfit = 0
        for id, price in enumerate(prices):
            if id == 0:
                minBuyingPrice = min(minBuyingPrice, price)
                continue
            if price < minBuyingPrice:
                minBuyingPrice = price
                maxSellingPrice = -1
                continue
            if price > maxSellingPrice:
                maxSellingPrice = price
                maxProfit = max(maxProfit, maxSellingPrice - minBuyingPrice)
                continue
        return maxProfit
