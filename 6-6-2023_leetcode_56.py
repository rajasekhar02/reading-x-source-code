from typing import *


def mergeOverlappingIntervals(arr: List[List[int]]) -> List[List[int]]:
    # Write your code here.
    currMergeList = 0

    sorted(arr, key=lambda x: x[0])

    for i in range(1, len(arr)):
        a = arr[currMergeList][0]
        b = arr[currMergeList][1]
        c = arr[i][0]
        d = arr[i][1]

        if c > b:
            currMergeList += 1
            arr[currMergeList][0] = c
            arr[currMergeList][1] = d
            continue
        if d > b:
            arr[currMergeList][1] = d
    return arr[: currMergeList + 1]


Q = [[1, 4], [3, 3], [3, 3], [3, 3], [3, 4], [4, 4], [5, 5], [5, 5], [5, 6]]
print(mergeOverlappingIntervals(Q))
