import math
N = int(input())
print(math.floor(math.log10(N))+1 if N > 0  else 1)
