# def combinationsOfDenominations(amount, noOfCoins, coins):
#     dp = [0 for i in range(0, amount + 1)]
#     CONSTANT = 1000000007
#     dp[0] = 1
#     # minCoin = min(coins)
#     for i in range(1, amount + 1):
#         for j in range(0, noOfCoins):
#             if i - coins[j] < 0:
#                 break
#             dp[i] = (dp[i] + dp[i - coins[j]]) % CONSTANT
#             # dp[i] = dp[i] % CONSTANT
#     return dp[amount]


# n, x = map(int, input().split(" "))
# coins = list(map(int, input().split(" ")))
# coins = sorted(coins)
# print(combinationsOfDenominations(x, n, coins))
if __name__ == "__main__":
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    dp = [0] * (m + 1)
    dp[0] = 1
    for i in range(1, m + 1):
        for j in range(n):
            if a[j] > i:
                break
            dp[i] = (dp[i] + dp[i - a[j]]) % 1000000007
            # dp[i] = dp[i] % 1000000007
    print(dp[m])
