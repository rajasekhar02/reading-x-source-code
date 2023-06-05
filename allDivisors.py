import math
N = int(input())
listOfDivisors = []
# O(sqrt(N))
for i in range(1, math.ceil(math.sqrt(N))):
    if N % i == 0:
        listOfDivisors.append(N/i)
        listOfDivisors.append(i)
print(sorted(listOfDivisors))
