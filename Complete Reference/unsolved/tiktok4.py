#
# Complete the 'getPrefixScores' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def getPrefixScores(arr):
    # Write your code here
    MOD = 10**9+7
    maxArr = []
    max = 0
    for id,i in enumerate(arr):
        if i > max:
            max = i
        maxArr.append((max*(id+1)) % MOD)
    prefixsum = [arr[0]]
    for i in range(1, len(arr)):
        prefixsum.append((prefixsum[i-1]+arr[i]) % MOD)
    prefixsum2 = [prefixsum[0]]
    for i in range(1, len(prefixsum)):
        prefixsum2.append((prefixsum2[i-1]+prefixsum[i]) % MOD)
    
    return [(maxArr[i]+prefixsum2[i]) % MOD for i in range(0, len(arr))]
\
