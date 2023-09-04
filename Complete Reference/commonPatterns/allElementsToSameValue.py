# Making all elements to same value given that one element can be changed at a time
from typing import Dict


def allElementsToSameValue(cntEachElements: Dict[int, int]):
    sum = 0
    ma = 0
    for j in range(0, 26):
        val = cntEachElements[j]
        sum += val
        ma = max(ma, val)
    return sum - ma


print(allElementsToSameValue(cntEachElements={"123": 12}))
