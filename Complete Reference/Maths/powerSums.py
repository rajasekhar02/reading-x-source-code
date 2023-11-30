def powerSum(X, N):
    # Write your code here
    def recurse(value, start):
        if value == 0:
            return 1
        totalCombs = 0
        for i in range(start, value+1):
            powV = pow(i, N)
            if powV > X:
                break
            totalCombs += recurse(value-powV, i+1)
        return totalCombs
    return recurse(X, 1)
