# https://www.hackerrank.com/contests/python-recruitment-02/challenges/pawn-prime-jump/problem
def max_game_score(cells):
    # Write your code here
    n = len(cells)
    primes = getPrimes(n)
    dp = [primes[-1]*-10001]*(n)
    dp[0] = 0
    
    for i in range(n-1):
        dp[i+1] = max(dp[i+1], dp[i]+cells[i+1])
        for primeId in range(len(primes)):
            if  (i+primes[primeId]) >= n:
                continue;
            dp[i+primes[primeId]] = max(
                dp[i+primes[primeId]],
                dp[i]+cells[i+primes[primeId]]
            )
    return dp[n-1]
