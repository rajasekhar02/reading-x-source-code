def removing_digits(n, dp):
    if n >= 0 and n < 10:
        return n != 0
    if dp[n] != 100000:
        return dp[n]
    temp = n
    minVal = 100000
    while temp > 0:
        rem = temp % 10
        if rem == 0:
            temp = temp // 10
            continue
        val = 1 + removing_digits(n - rem, dp)
        temp = temp // 10
        minVal = min(val, minVal)
    dp[n] = minVal
    return minVal


def removing_digits_itr_dp(n, dp):
    dp[0] = 0
    for i in range(1, n + 1):
        temp = i
        minVal = 10000000
        while temp > 0:
            rem = temp % 10
            if rem == 0:
                temp = temp // 10
                continue
            val = 1 + dp[i - rem]
            temp = temp // 10
            minVal = min(val, minVal)
        dp[i] = minVal
    # print(dp)
    return dp[n]


n = int(input())  #  27  #
dp = [0] * (n + 1)
print(removing_digits_itr_dp(n, dp))
