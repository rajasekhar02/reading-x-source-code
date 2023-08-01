if __name__ == "__main__":
    n, x = map(int, input().split())
    coins = list(map(int, input().split()))
    coins = sorted(coins)
    dp = [0] * (x + 1)
    dp[0] = 1
    for coinId in range(0, n):
        for j in range(0, x - coins[coinId] + 1):
            dp[j + coins[coinId]] = dp[j + coins[coinId]] + dp[j]
            dp[j + coins[coinId]] %= 1000000007
        # print(dp, coins[coinId])
    print(dp[x])


def comb_2_2dDP(amount, noOfCoins, coins):
    dp = []
    for i in range(0, noOfCoins + 1):
        dp.append([])
        for j in range(0, amount + 1):
            dp[i].append(0)
    dp[0][0] = 1
    for coinId in range(1, noOfCoins + 1):
        for targetAmount in range(0, amount + 1):
            dp[coinId][targetAmount] = dp[coinId - 1][targetAmount]
            left = targetAmount - coins[coinId - 1]
            if left >= 0:
                dp[coinId][targetAmount] += dp[coinId][left]
                dp[coinId][targetAmount] %= 1000000007
    print(dp)
    return dp[noOfCoins][targetAmount]


def comb_2_recur(amount, start, coins, dp):
    if amount == 0:
        return 1
    if dp[amount] != 0:
        return dp[amount]
    ans = 0
    for i in range(start, len(coins)):
        if amount - coins[i] >= 0:
            ans += comb_2_recur(amount - coins[i], i, coins, dp)
    dp[amount] = ans
    return ans


# n = 3
# x = 9
# coins = [2, 3, 5]
# # dp = [0] * (x + 1)
# print(comb_2_2dDP(x, len(coins), coins))
