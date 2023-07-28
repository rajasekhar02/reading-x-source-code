class Solution:
    def minCoinsTrail1(self, coins, M, V):
        # FAILED
        # code here
        # V = 26, M = 5
        # coins = [3,7,6,11,8]
        coins = sorted(coins, reverse=True)
        minCoins = 1e6 + 1
        for i in range(0, M):
            tempV = V
            pos = i
            coinsUsed = 0
            while pos < M and tempV > 0:
                if tempV < coins[pos]:
                    pos += 1
                    continue
                print(tempV, coins[pos], pos, coinsUsed, tempV // coins[pos])
                coinsUsed += tempV // coins[pos]
                tempV = tempV % coins[pos]
                pos += 1
            print(coinsUsed, tempV)
            if tempV == 0:
                minCoins = min(minCoins, coinsUsed)
        if minCoins == 1e6 + 1:
            return -1
        else:
            return minCoins

    def minCoinsTrail2(self, coins, M, V):
        # FAILED
        allPricesIncluV = [1e6 + 1] * (V + 1)
        allPricesIncluV[0] = 0
        # for i in coins:
        #     allPricesIncluV[i] = 1
        coins = sorted(coins, reverse=True)
        for i in range(1, V):
            for j in range(0, M):
                if coins[j] == i:
                    allPricesIncluV[coins[j]] = 1
                    continue
                # Using division will take the coins maximum times so we should use subtraction
                if (i // coins[j]) > 0:
                    allPricesIncluV[i] = min(
                        allPricesIncluV[i],
                        (i // coins[j]) + allPricesIncluV[i % coins[j]],
                    )
        if allPricesIncluV[V] == 1e6 + 1:
            return -1
        else:
            return allPricesIncluV[V]

    def minCoins(self, coins, M, V):
        # SUCCEEDED
        allPricesIncluV = [1e6 + 1] * (V + 1)
        allPricesIncluV[0] = 0
        # for i in coins:
        #     allPricesIncluV[i] = 1
        coins = sorted(coins, reverse=True)
        for i in range(1, V + 1):
            for j in range(0, M):
                if coins[j] == i:
                    allPricesIncluV[coins[j]] = 1
                    continue
                if i - coins[j] < 0:
                    continue
                # Using division will take the coins maximum times so we should use subtraction
                # this solution works because the min denominations are already filled with min coins required
                # So the denominations for larger values will be optimal
                allPricesIncluV[i] = min(
                    allPricesIncluV[i], 1 + allPricesIncluV[i - coins[j]]
                )
        # print(allPricesIncluV)
        if allPricesIncluV[V] == 1e6 + 1:
            return -1
        else:
            return allPricesIncluV[V]
