def getMinimalCoinsDenomination(amount, coins):
    dp = [1000008] * (amount + 1)
    dp[0] = 1
    for i in coins:
        if i > amount:
            continue
        dp[i] = 1
    for iAmount in range(1, amount + 1):
        if dp[iAmount] != 1000008:
            continue
        for jCoin in range(0, len(coins)):
            if (iAmount - coins[jCoin]) < 0:
                # ( Sorting the coins and using break ) instead of continue will get rid of unnecessary
                # calculation of cost for bigger testcases
                break
            dp[iAmount] = min(dp[iAmount], 1 + dp[iAmount - coins[jCoin]])
    if dp[amount] == 1000008:
        return -1
    return dp[amount]


[n, x] = list(map(int, input().split(" ")))
coins = list(map(int, input().split(" ")))
coins = sorted(coins)
print(getMinimalCoinsDenomination(x, coins))
