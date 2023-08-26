from collections import defaultdict


def recurse(array, pos, prev_value, upBnd, n):
    if pos == n:
        return 1
    allCombs = 0
    if array[pos] == 0:
        start = 1 if prev_value <= 1 else (prev_value - 1)
        end = upBnd if prev_value == 0 else min((prev_value + 1), upBnd)
        for i in range(start, end + 1):
            if abs(prev_value - i) <= 1 or prev_value == 0:
                allCombs += recurse(array, pos + 1, i, upBnd, n)
                allCombs = allCombs % 1000000007
    else:
        if abs(array[pos] - prev_value) <= 1:
            allCombs = recurse(array, pos + 1, array[pos], upBnd, n)
    return allCombs


def iterativeDP2():
    [n, upBnd] = list(map(int, input().split(" ")))
    array = list(map(int, input().split(" ")))
    dp = []
    for i in range(0, n):
        dp.append([])
        for j in range(0, upBnd + 1):
            dp[i].append(0)

    # Base cases initialization
    if array[n - 1] == 0:
        for i in range(1, upBnd + 1):
            dp[n - 1][i] = 1
    else:
        dp[n - 1][array[n - 1]] = 1

    # core logic
    for pos in range(n - 2, -1, -1):
        if array[pos] != 0:
            for newValue in [array[pos] - 1, array[pos], array[pos] + 1]:
                if newValue >= 1 and newValue <= upBnd:
                    dp[pos][array[pos]] += dp[pos + 1][newValue]
                    dp[pos][array[pos]] %= 1000000007
            continue
        for possible_value in range(1, upBnd + 1):
            for newValue in [
                possible_value - 1,
                possible_value,
                possible_value + 1,
            ]:
                if newValue >= 1 and newValue <= upBnd:
                    dp[pos][possible_value] += dp[pos + 1][newValue]
                    dp[pos][possible_value] %= 1000000007
    print(sum(dp[0]) % 1000000007)


if __name__ == "__main__":
    [n, upBnd] = list(map(int, input().split(" ")))
    array = list(map(int, input().split(" ")))
    dp = []
    for i in range(0, n):
        dp.append([])
        for j in range(0, upBnd + 1):
            dp[i].append(0)

    if array[n - 1] == 0:
        for i in range(1, upBnd + 1):
            dp[n - 1][i] = 1
    else:
        dp[n - 1][array[n - 1]] = 1

    for pos in range(n - 2, -1, -1):
        # Struggled for this logic
        prev_value = array[pos]
        if array[pos] != 0:
            dp[pos][prev_value] += dp[pos + 1][array[pos]]
            dp[pos][prev_value] %= 1000000007
            if array[pos] < upBnd:
                dp[pos][prev_value] += dp[pos + 1][array[pos] + 1]
                dp[pos][prev_value] %= 1000000007
            if array[pos] > 1:
                dp[pos][prev_value] += dp[pos + 1][array[pos] - 1]
                dp[pos][prev_value] %= 1000000007
            continue
        for possible_value in range(1, upBnd + 1):
            dp[pos][possible_value] += dp[pos + 1][possible_value]
            dp[pos][possible_value] %= 1000000007
            if possible_value < upBnd:
                dp[pos][possible_value] += dp[pos + 1][possible_value + 1]
                dp[pos][possible_value] %= 1000000007
            if possible_value > 1:
                dp[pos][possible_value] += dp[pos + 1][possible_value - 1]
                dp[pos][possible_value] %= 1000000007
    # failed to get this logic
    print(sum(dp[0]) % 1000000007)
