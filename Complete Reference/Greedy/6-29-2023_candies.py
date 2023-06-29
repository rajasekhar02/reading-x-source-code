# https://www.hackerrank.com/challenges/candies/problem

def candiesNotWorking(n, arr):
    ans = [1]*n
    # this logic fail when the testcase is a decreasing sequence
    """
    Input:
    3
    3
    2
    1
    Output:         Expected Output:
    [2,2,1]         [3,2,1]
    sum = 5         sum = 6
                    
    """
    for i in range(1,n):
        if arr[i] > arr[i-1]:
            ans[i] = ans[i-1]+1
        elif arr[i-1] > arr[i] and ans[i-1] <= ans[i]:
            ans[i-1] = ans[i]+1
    return sum(ans)

def candies(n, arr):
    ans = [1]*n
    # I didn't seperated for loop for dealing with increasing and decreasing cases
    # So some test cases fails
    for i in range(1,n):
        if arr[i] > arr[i-1]:
            ans[i] = ans[i-1]+1
    for i in range(n-1,0,-1):
        if arr[i-1] > arr[i] and ans[i-1] <= ans[i]:
            ans[i-1] = ans[i]+1
    return sum(ans)