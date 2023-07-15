from os import *
from sys import *
from collections import *
from math import *


def minimumCost(row, column, l, w):
    # Write your code here
    # Return an integer
    return recurse(l, w, row, column)


def recurse(row, column, l, w):
    if row == 1:
        return sum(w)
    if column == 1:
        return sum(l)
    maxLen = 0
    maxLIndex = 0
    for i in range(0, len(l)):
        if maxLen < l[i]:
            maxLen = l[i]
            maxLIndex = i
    maxWid = 0
    maxWIndex = 0
    for i in range(0, len(w)):
        if maxWid < w[i]:
            maxWid = w[i]
            maxWIndex = i
    if maxLen > maxWid:
        return (
            maxLen
            + recurse(maxLIndex + 1, column, l[:maxLIndex], w)
            + recurse(row - maxLIndex - 1, column, l[maxLIndex + 1 :], w)
        )
    return (
        maxWid
        + recurse(row, maxWIndex + 1, l, w[:maxWIndex])
        + recurse(row, column - maxWIndex - 1, l, w[maxWIndex + 1 :])
    )


Testcases = [[[1, 2], [2, 1], 3, 3]]

for t in Testcases:
    print(minimumCost(*t))
