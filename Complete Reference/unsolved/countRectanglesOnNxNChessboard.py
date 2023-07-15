# Video Reference: https://www.youtube.com/watch?v=DIsW_6u7jrA


def countRectangles(n):
    MOD = 1000000007
    rectangles = (n * n + 1) % MOD / 2
    rectangles *= rectangles
    squares = (n * (n + 1) * (2 * n + 1) / 6) % MOD
    ans = (rectangles - squares + MOD) % MOD
    return ans


print(countRectangles(13))
