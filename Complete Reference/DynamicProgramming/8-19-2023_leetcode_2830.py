class Solution:
    def __init__(self):
        self.dp = [-1]

    def maximizeTheProfit(self, n: int, offers: List[List[int]]) -> int:
        offers = sorted(offers, key=lambda x: x[0])
        self.dp = [-1] * len(offers)
        return self.recurse(offers, 0)

    def recurse(self, offers, currOffer):
        if currOffer == len(offers):
            return 0
        if self.dp[currOffer] != -1:
            return self.dp[currOffer]
        notTake = self.recurse(offers, currOffer + 1)
        ind = self.lowerbound(
            offers, currOffer + 1, len(offers) - 1, offers[currOffer][1]
        )
        take = offers[currOffer][2] + self.recurse(offers, ind)
        self.dp[currOffer] = max(take, notTake)
        return self.dp[currOffer]

    def lowerbound(self, offers, start, end, target):
        low = start
        high = end
        ans = end + 1
        while low <= high:
            mid = low + ((high - low) // 2)
            if offers[mid][0] > target:
                high = mid - 1
                ans = mid
            else:
                low = mid + 1
        return ans
