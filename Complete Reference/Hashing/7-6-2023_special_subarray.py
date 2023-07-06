from os import *
from sys import *
from collections import *
from math import *

from typing import List


def specialSubarray(n: int, arr: List[int]) -> List[int]:
    # write your code here
    dictNum = defaultdict(lambda: [0, 0, 0, 0])
    arr = arr[:n]
    for id, i in enumerate(arr):
        if dictNum[i][0] == 0:
            dictNum[i][0] = 1  # count
            dictNum[i][1] = id  # start
            dictNum[i][2] = id  # end
            dictNum[i][3] = i
            continue
        dictNum[i][0] += 1
        dictNum[i][2] = id
    specialSubArray = None
    for i in dictNum:
        if specialSubArray == None:
            specialSubArray = dictNum[i]
            continue
        if specialSubArray[0] > dictNum[i][0]:
            continue
        if specialSubArray[0] < dictNum[i][0]:
            specialSubArray = dictNum[i]
            continue
        lenSpec = specialSubArray[2] - specialSubArray[1]
        newSpec = dictNum[i][2] - dictNum[i][1]
        if newSpec < lenSpec:
            specialSubArray = dictNum[i]
            continue
        # newSpec == lenSpec because of without this condition I took 1.5 hr to find this condition
        # So write the context that are true at this region
        if newSpec == lenSpec and specialSubArray[1] > dictNum[i][1]:
            specialSubArray = dictNum[i]
            continue
    return arr[specialSubArray[1] : specialSubArray[2] + 1]
