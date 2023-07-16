"""
Problem Type 1:
    X such that 0 <= X <= R
    find the count of numbers in [0,R] that satisfies f(x) 

Problem Type 2:
    X such that L <= X <= R
    find the count of numbers in [L,R] that satisfies f(X)
    Ans: dp[R] - dp[L-1]
"""

def bruteforce(L, R, x):
    def check(num, sum):
        tempSum = 0
        for i in str(num):
            tempSum += ord(i)-ord('0')
        if tempSum == sum:
            return True
        return False
    res = 0
    for i in range(L, R+1):
        if check(i, x):
            res+=1
    return res

def solve(num, n, x, tight):
    if x < 0: return 0

    if n == 1:
        if x >= 0 and x <=9:
            return 1
        return 0

    if dp[n][x][tight] != -1:
        return dp[n][x][tight]

    ub = 9

    if tight:
        ub = ord(num[len(num)-n]) - ord('0')

    answer = 0

    for dig in range(0,ub+1):
        # Key Things Learnt:             vvvv
        answer += solve(num, n-1, x-dig, tight & (dig == ub))

    dp[n][x][tight] = answer

    return dp[n][x][tight]

dp = []
for i in range(0, 101):
    dp.append([])
    for j in range(0, 181):
        dp[i].append([])
        for k in range(0,2):
            dp[i][j].append(-1)


L = "0"
R = "11235"
print(bruteforce(0, 11235, 5))
print(solve(R, len(R), 5, 1))