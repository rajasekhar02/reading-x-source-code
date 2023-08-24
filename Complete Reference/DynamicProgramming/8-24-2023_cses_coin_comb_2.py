def recurse(coins, startIndex, remPrice):
    if startIndex >= len(coins):
        return int(remPrice == 0)
    if (remPrice - coins[startIndex]) < 0:
        return 0
    combNotTakeCurrCoin = recurse(coins, startIndex + 1, remPrice)
    combTakeCurrCoin = ((remPrice - coins[startIndex]) == 0) + recurse(
        coins, startIndex, remPrice - coins[startIndex]
    )
    totalComb = combNotTakeCurrCoin + combTakeCurrCoin
    totalComb = totalComb % 1000000007
    return totalComb


if __name__ == "__main__":
    [n, x] = list(map(int, input().split(" ")))
    coins = list(map(int, input().split(" ")))
    coins = sorted(coins)
    # print(coins, recurse(coins, 0, x))
    dp = []
    for price in range(0, x + 1):
        dp.append([])
        value = int(price == 0)
        for coin in range(0, n + 1):
            dp[price].append(value)

    for price in range(1, x + 1):
        for coin in range(1, len(coins) + 1):
            # as I am not taking the present coin I will be maintain the previous coins combinations at the present coin
            notTake = dp[price][coin - 1]
            dp[price][coin] = notTake
            if (price - coins[coin - 1]) < 0:
                break
            take = dp[price - coins[coin - 1]][coin]
            dp[price][coin] += take
            dp[price][coin] = dp[price][coin] % 1000000007
    print(dp[x][n])
