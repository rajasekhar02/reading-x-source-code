[n, x] = list(map(int, input().split(" ")))
prices = list(map(int, input().split(" ")))
pages = list(map(int, input().split(" ")))
pricesAndPages = list(zip(prices, pages))
# sorting by prices
pricesAndPages = sorted(pricesAndPages, key=lambda x: x[0])

dp = []
for j in range(0, x + 1):
    dp.append([])
    for i in range(0, n + 1):
        dp[j].append(0)


def recurse(pricesAndPages, startIndex, remPrice, dp):
    if startIndex >= len(pricesAndPages):
        return 0
    if dp[remPrice][startIndex] != 0:
        return dp[remPrice][startIndex]
    notTake = recurse(pricesAndPages, startIndex + 1, remPrice, dp)
    dp[remPrice][startIndex] = notTake
    if (remPrice - pricesAndPages[startIndex][0]) < 0:
        return dp[remPrice][startIndex]
    take = pricesAndPages[startIndex][1] + recurse(
        pricesAndPages, startIndex + 1, remPrice - pricesAndPages[startIndex][0], dp
    )
    dp[remPrice][startIndex] = max(dp[remPrice][startIndex], notTake)
    return dp[remPrice][startIndex]


def iterateDP(pricesAndPages, startIndex, almostPrice, dp):
    for tempRemPrice in range(1, almostPrice + 1):
        # for tempStartIndex in range(len(pricesAndPages) - 1, -1, -1):
        for tempStartIndex in range(1, len(pricesAndPages) + 1):
            # Actual: I kept the below code after the if condition which results in not calculating the notTake if take is not possible

            # corrected
            notTake = dp[tempRemPrice][tempStartIndex - 1]
            dp[tempRemPrice][tempStartIndex] = notTake
            if (tempRemPrice - pricesAndPages[tempStartIndex - 1][0]) < 0:
                break
            """Actual
            take = dp[tempRemPrice][tempStartIndex + 1] + pricesAndPages[tempStartIndex][1] 
            """
            # corrected
            take = (
                dp[tempRemPrice - pricesAndPages[tempStartIndex - 1][0]][
                    tempStartIndex - 1
                ]
                + pricesAndPages[tempStartIndex - 1][1]
            )

            dp[tempRemPrice][tempStartIndex] = max(
                dp[tempRemPrice][tempStartIndex], take
            )
    return dp[almostPrice][n]


print(iterateDP(pricesAndPages, 0, x, dp))
