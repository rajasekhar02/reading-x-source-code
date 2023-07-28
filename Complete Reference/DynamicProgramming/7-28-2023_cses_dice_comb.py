def totalCombinationsWithSum(sum, dp):
    CONSTANT = 1000000007
    if sum == 0:
        return 1
    if dp[sum] != -1:
        return dp[sum]
    count = 0
    for i in range(1, 7):
        if sum < i:
            continue
        count += totalCombinationsWithSum(sum - i, dp) % CONSTANT
        count %= CONSTANT
    dp[sum] = count
    return dp[sum]


def totalCombinationsWithSumLoop(sum):
    dp = [0] * (sum + 1)
    CONSTANT = 1000000007
    dp[0] = 1
    dp[1] = 1
    for i in range(2, sum + 1):
        for j in range(1, 7):
            if i < j:
                break
            dp[i] += dp[i - j] % CONSTANT
            dp[i] %= CONSTANT
    return dp[sum]


n = int(input())
print(totalCombinationsWithSumLoop(n))
