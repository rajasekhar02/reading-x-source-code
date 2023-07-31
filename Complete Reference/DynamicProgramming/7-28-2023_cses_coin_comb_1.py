def combinationsOfDenominations(amount, noOfCoins, coins):
    dp = [0] * (amount + 1)
    CONSTANT = 1000000007
    dp[0] = 1
    for i in range(1, amount + 1):
        for j in range(0, noOfCoins):
            if i - coins[j] < 0:
                break
            dp[i] += dp[i - coins[j]] % CONSTANT
            dp[i] = dp[i] % CONSTANT
    return dp[amount]


[n, x] = list(map(int, input().split(" ")))
coins = list(map(int, input().split(" ")))
coins = sorted(coins)
print(combinationsOfDenominations(x, n, coins))
